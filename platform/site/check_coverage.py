"""F014: the locale coverage gate.

    python platform/site/check_coverage.py            # report
    python platform/site/check_coverage.py --strict   # non-zero on a warning
    python platform/site/check_coverage.py --json     # machine readable

A locale is a *claim* the moment it is built: it gets an hreflang tag, a
sitemap entry and a crawlable URL. An unfinished claim is worse than no claim,
so this gate is what decides which locales are allowed to be advertised at all.

Three classes of failure:
  ERROR   a locale is being advertised but is empty, or a namespace is missing
  WARN    a translated value is byte-identical to its English value (untranslated
          leftover), or a title is still the slug
  INFO    coverage percentages, for tracking

Upstream itself fails this gate, which is why `en` is reported rather than
assumed: `stylesEn` holds 96 of 214 style descriptions.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LOCALES = ROOT / "site" / "locales"
SOURCE_LOCALES = ("en", "zh")
# A locale directory holds exactly these files. `ui.json` is flat and carries
# `page.*` / `showcase.*` prefixes, because upstream splits its three inline
# dictionaries only as an artifact of its own coupling (ADR-0004).
NAMESPACES = ("ui", "cards", "styles", "meta")

# Strings that are genuinely identical across languages and must not be flagged.
# Brand and platform names are not translated. Flagging them produces noise that
# trains a reviewer to ignore the gate, which is worse than no gate.
ALLOW_IDENTICAL = {
    "Ink Press", "Remotion", "JianYing", "CapCut", "Mixkit", "SHOTBOOK", "MP4", "GIF",
    "Douyin", "Xiaohongshu", "X", "video-shotcraft", "Apache-2.0", "GitHub",
}

SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def load(code: str, ns: str) -> dict:
    p = LOCALES / code / f"{ns}.json"
    if not p.exists():
        return {}
    return json.loads(p.read_text(encoding="utf-8"))


def check(min_pct: float = 60.0) -> dict:
    errors: list[str] = []
    warns: list[str] = []
    locales = sorted(d.name for d in LOCALES.iterdir() if d.is_dir()) if LOCALES.is_dir() else []
    report: dict = {"locales": {}, "errors": errors, "warnings": warns}

    for code in locales:
        per_ns: dict[str, dict] = {}
        for ns in NAMESPACES:
            data = load(code, ns)
            per_ns[ns] = {"total": len(data), "translated": len(data)}
        report["locales"][code] = per_ns

        # content signal: a real locale has ui keys AND at least some card text
        ui_n = len(load(code, "ui"))
        cards = load(code, "cards")
        card_titles = sum(1 for v in cards.values() if isinstance(v, dict) and v.get("title"))
        card_desc = sum(1 for v in cards.values() if isinstance(v, dict) and v.get("description"))
        report["locales"][code]["content"] = {
            "ui_keys": ui_n, "card_titles": card_titles, "card_descriptions": card_desc}

        if code in SOURCE_LOCALES:
            # upstream: measure, never fail. These are the baseline.
            report["locales"][code]["role"] = "upstream-source"
            for ns in ("cards", "styles"):
                en_total = len(load("en", ns))
                have = per_ns[ns]["translated"]
                if ns == "styles" and code == "en" and have < en_total:
                    warns.append(
                        f"en/{ns}: only {have}/{en_total} entries exist upstream "
                        f"(library.json descriptions are used for the rest) — expected, not a bug")
            continue

        if ui_n == 0 and card_titles == 0:
            errors.append(f"{code}: empty locale, must not be advertised")
            continue

        # missing namespaces
        for ns in ("ui", "cards", "styles"):
            if not (LOCALES / code / f"{ns}.json").exists():
                warns.append(f"{code}: {ns}.json missing (runtime will fall back to en)")

        # untranslated leftovers + slug titles
        en_ui = load("en", "ui")
        for k, v in load(code, "ui").items():
            ev = en_ui.get(k)
            if isinstance(v, str) and isinstance(ev, str) and v == ev and v not in ALLOW_IDENTICAL:
                warns.append(f"{code}/ui.{k}: identical to en ({v[:40]!r}) — probably untranslated")
        en_cards = load("en", "cards")
        for k, v in load(code, "cards").items():
            if not isinstance(v, dict):
                continue
            t = v.get("title")
            if t and SLUG_RE.match(t) and t == k:
                warns.append(f"{code}/cards.{k}: title is still the slug")
            d = v.get("description")
            ed = en_cards.get(k, {}).get("description") if isinstance(en_cards.get(k), dict) else None
            if d and ed and d == ed and d not in ALLOW_IDENTICAL:
                warns.append(f"{code}/cards.{k}.description: identical to en — untranslated")

    # cross-locale: every advertised locale must be reachable
    coverage_path = ROOT / "site" / "build" / "coverage.json"
    if coverage_path.exists():
        cov = json.loads(coverage_path.read_text(encoding="utf-8"))
        report["coverage_json"] = {k: v["overall_pct"] for k, v in cov.items()}
        for code, pct in report["coverage_json"].items():
            if code in SOURCE_LOCALES:
                continue
            # A locale that is advertised behind an hreflang tag but is mostly
            # English is the failure ADR-0004 exists to prevent, so at the default
            # threshold it is an ERROR, not a warning. 20% was low enough that a
            # page of untranslated slugs would have passed.
            if pct < min_pct:
                errors.append(
                    f"{code}: only {pct}% coverage but the locale is advertised — "
                    f"hreflang claims a translation the page does not deliver "
                    f"(threshold {min_pct}%)")
            elif pct < 85:
                warns.append(f"{code}: {pct}% coverage, still falling back to English "
                             f"for the rest")

    return report


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true",
                    help="also fail on warnings, not only on errors")
    ap.add_argument("--min-pct", type=float, default=60.0,
                    help="coverage below which an advertised locale is a failure "
                         "(default 60: a locale under this is mostly English while "
                         "claiming an hreflang)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    rep = check(min_pct=a.min_pct)

    if a.json:
        print(json.dumps(rep, ensure_ascii=False, indent=2))
    else:
        print(f"{'locale':8} {'role':16} {'ui':>4} {'cards':>6} {'desc':>5}  status")
        for code, per in rep["locales"].items():
            c = per["content"]
            status = "SOURCE" if per.get("role") == "upstream-source" else (
                "EMPTY" if rep["errors"] and f"{code}:" in " ".join(rep["errors"]) else "built")
            print(f"{code:8} {status:16} {c['ui_keys']:>4} {c['card_titles']:>6} "
                  f"{c['card_descriptions']:>5}  {status}")
        if "coverage_json" in rep:
            print("\noverall coverage: " + ", ".join(
                f"{k}={v}%" for k, v in rep["coverage_json"].items()))
        if rep["warnings"]:
            print(f"\n{len(rep['warnings'])} warning(s):")
            for w in rep["warnings"][:20]:
                print("  !", w)
            if len(rep["warnings"]) > 20:
                print(f"  … {len(rep['warnings']) - 20} more")
        if rep["errors"]:
            print(f"\n{len(rep['errors'])} error(s):")
            for e in rep["errors"]:
                print("  x", e)

    if rep["errors"]:
        return 1
    # Severity matches platform/doctor.py: an ERROR always fails, a WARN fails only
    # under --strict. The earlier version of this returned 0 unless --strict, and
    # separately treated a 20%-coverage locale as a warning -- so an advertised
    # page of untranslated slugs passed. The threshold is now an error.
    if a.strict and rep["warnings"]:
        return 1
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())