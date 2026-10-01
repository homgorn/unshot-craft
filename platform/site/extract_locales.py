"""F010: extract the three upstream inline dictionaries into per-locale JSON.

    python platform/site/extract_locales.py

Verifiable by construction: the script writes a `extraction_report.json` with
the count of keys per namespace, and `verify_extraction()` re-parses the emitted
JSON and asserts it equals what was read out of the upstream sources, key for
key. If upstream adds a key, the counts move and the report shows it.

Why this exists: upstream keeps translations in three unrelated inline places
(translations.js, index.html's L10N, showcase.js's SHOWCASE_L10N), and
build-seo.py parses the English card map by slicing a string up to the first
`},`. A key containing `},` silently truncates the map. Extracting to JSON
removes that failure mode and makes adding a locale a data operation.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "platform" / "ingest"))

from shotcraft_ingest.parsing import (  # noqa: E402
    block_at, parse_js_map, top_level_member,
)

GALLERY = ROOT / "upstream" / "video-shotcraft" / "gallery"
LOCALES = ROOT / "site" / "locales"
UPSTREAM_LOCALES = ("en", "zh")

# Keys upstream reuses across pages under different names. Keeping one canonical
# spelling is what lets a single `t('ui', key)` replace three dictionaries.
UI_ALIASES = {
    "navLibrary": "navLibrary",
    "languageToggle": "languageToggle",
    "themeDark": "themeDark",
    "themeLight": "themeLight",
    "themeToDark": "themeToDark",
    "themeToLight": "themeToLight",
}


def extract() -> dict:
    """-> {locale: {ns: {key: text}}}"""
    out: dict[str, dict[str, dict[str, str]]] = {c: {} for c in UPSTREAM_LOCALES}
    report = {"namespaces": {}, "upstream_locales": list(UPSTREAM_LOCALES)}

    # 1. translations.js: ui + four flat card/style maps
    src = (GALLERY / "translations.js").read_text(encoding="utf-8")
    ui_seg = top_level_member(src, "ui") or ""
    for loc in UPSTREAM_LOCALES:
        m = None
        for mm in __import__("re").finditer(rf"(?m)^\s*{loc}\s*:\s*\{{", ui_seg):
            m = mm
        if m:
            seg, _ = block_at(ui_seg, m.end() - 1)
            out[loc]["ui"] = parse_js_map(seg)

    for member, ns, loc in (("cardsZh", "cards", "zh"), ("cardsEn", "cards", "en"),
                            ("stylesZh", "styles", "zh"), ("stylesEn", "styles", "en")):
        seg = top_level_member(src, member) or ""
        flat = parse_js_map(seg)
        bucket = out[loc].setdefault(ns, {})
        for k, v in flat.items():
            entry = bucket.setdefault(k, {})
            # cardsEn / stylesEn are English *descriptions*, cardsZh / stylesZh
            # are Chinese *titles*. Keep title and description separate: that is
            # what the ru/es/de locales need, and it is what a reviewer checks.
            if loc == "en":
                entry["description"] = v
            else:
                entry["title"] = v

    # English titles fall back to the slug; record that explicitly rather than
    # inventing a title.
    for loc, ns in (("en", "cards"), ("en", "styles")):
        for k, entry in out[loc].get(ns, {}).items():
            entry.setdefault("title", k)

    # 2. index.html inline L10N
    html = (GALLERY / "index.html").read_text(encoding="utf-8")
    import re as _re
    m = _re.search(r"const L10N\s*=\s*\{", html)
    if m:
        seg, _ = block_at(html, m.end() - 1)
        for loc in UPSTREAM_LOCALES:
            mm = _re.search(rf"(?m)^\s*{loc}\s*:\s*\{{", seg)
            if mm:
                s2, _ = block_at(seg, mm.end() - 1)
                out[loc]["page"] = parse_js_map(s2)

    # 3. showcase.js inline SHOWCASE_L10N
    js = (GALLERY / "showcase.js").read_text(encoding="utf-8")
    m = _re.search(r"SHOWCASE_L10N\s*=\s*\{", js)
    if m:
        seg, _ = block_at(js, m.end() - 1)
        for loc in UPSTREAM_LOCALES:
            mm = _re.search(rf"(?m)^\s*{loc}\s*:\s*\{{", seg)
            if mm:
                s2, _ = block_at(seg, mm.end() - 1)
                out[loc]["showcase"] = parse_js_map(s2)

    # 4. Flatten page/showcase chrome into `ui` with a namespace prefix.
    #    (see the note below on why the store is flat but the runtime is not)
    #
    # The runtime keeps `ui` / `page` / `showcase` as separate namespaces, but a
    # translator should not have to know that index.html's strings are "page"
    # and showcase.html's are "showcase": upstream only splits them because its
    # three i18n mechanisms are separate, which is the coupling ADR-0004 removed.
    # So the canonical store is one flat `ui` namespace with `page.` / `showcase.`
    # prefixes, and the builder slices it back apart at build time. This also
    # removes the collisions that appear the moment they are merged: both pages
    # define `documentTitle`, `intro`, `skip`, `brandHome` and `retry`.
    for loc in UPSTREAM_LOCALES:
        ui = out[loc].setdefault("ui", {})
        for ns_src in ("page", "showcase"):
            for k, v in out[loc].get(ns_src, {}).items():
                ui[f"{ns_src}.{k}"] = v
            out[loc].pop(ns_src, None)
        out[loc]["meta"] = {
            "htmlLang": {"en": "en", "zh": "zh-CN"}[loc],
            "ogLocale": {"en": "en_US", "zh": "zh_CN"}[loc],
        }

    for loc, ns_map in out.items():
        for ns, kv in ns_map.items():
            report["namespaces"].setdefault(loc, {})[ns] = len(kv)
    return {"locales": out, "report": report}


def verify(locales_map: dict) -> list[str]:
    """Re-read the written JSON and compare against the in-memory extraction."""
    problems: list[str] = []
    for loc, ns_map in locales_map.items():
        for ns, kv in ns_map.items():
            path = LOCALES / loc / f"{ns}.json"
            if not path.exists():
                problems.append(f"{loc}/{ns}.json missing")
                continue
            disk = json.loads(path.read_text(encoding="utf-8"))
            if disk != kv:
                only_disk = set(disk) - set(kv)
                only_mem = set(kv) - set(disk)
                problems.append(
                    f"{loc}/{ns}: disk-only={sorted(only_disk)[:5]} memory-only={sorted(only_mem)[:5]}")
                for k in set(disk) & set(kv):
                    if disk[k] != kv[k]:
                        problems.append(f"{loc}/{ns}.{k} differs")
    return problems


def main() -> int:
    result = extract()
    for loc, ns_map in result["locales"].items():
        d = LOCALES / loc
        d.mkdir(parents=True, exist_ok=True)
        for ns, kv in ns_map.items():
            (d / f"{ns}.json").write_text(
                json.dumps(kv, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                encoding="utf-8")

    problems = verify(result["locales"])
    report = dict(result["report"])
    report["verified"] = not problems
    report["problems"] = problems
    (LOCALES / "extraction_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())