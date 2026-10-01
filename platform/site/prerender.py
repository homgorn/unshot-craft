"""Prerender the locale's card text into library.html for crawlers.

    python platform/site/prerender.py

Why this is not optional: upstream ships the English one-liners in the static
HTML of *every* locale, because `build-seo.py` writes one prerendered block from
`cardsEn`. A crawler that does not run JavaScript — which is most of them, and
all of the first indexing pass — would read English on /zh/library.html and
/ru/library.html. That is the exact failure ADR-0004 exists to prevent: a locale
URL that looks translated and is not.

What it does, per locale:
  * rewrites the block between `<!-- seo:cards:start -->` and `<!-- seo:cards:end -->`
    with that locale's own titles and descriptions, from site/locales/<code>/
  * rewrites <title>, meta description, h1, og:title, og:description from
    site/locales/<code>/meta.json when present
  * leaves app.js to re-render at runtime (the prerender is a no-JS fallback)

Fails loudly if a locale has no titles: a locale that cannot be prerendered must
not be published, because its static HTML is a lie.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIST = ROOT / "site" / "dist"
LOCALES = ROOT / "site" / "locales"

START = "<!-- seo:cards:start -->"
END = "<!-- seo:cards:end -->"

# Counts upstream renders into the page and normalises from library.json. They
# must match the real numbers or the static and dynamic views disagree.
COUNT_IDS = {"cardCount": "cards", "styleCount": "styles", "previewCount": "samples"}


def esc(s: str) -> str:
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace('"', "&quot;"))


def load(code: str, name: str) -> dict:
    p = LOCALES / code / f"{name}.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def render_block(code: str, lib: dict) -> str:
    cards = load(code, "cards")
    styles = load(code, "styles")
    rows: list[str] = []
    for card in lib["cards"]:
        name = card["name"]
        meta = cards.get(name, {}) if isinstance(cards.get(name), dict) else {}
        title = meta.get("title") or name
        desc = (meta.get("description")
                or (card.get("summary") or "")
                or (card.get("intention") or ""))
        keys = [s["key"] for s in card.get("styles", [])]
        style_rows = []
        for k in keys:
            sm = styles.get(k, {}) if isinstance(styles.get(k), dict) else {}
            style_rows.append(f"<li>{esc(sm.get('title') or k)}</li>")
        rows.append(
            f'      <article class="shot-card" id="{esc(name)}">\n'
            f"        <h3>{esc(title)}</h3>\n"
            f"        <p>{esc(desc)}</p>\n"
            f"        <ul class=\"style-list\">\n"
            + ("\n".join(style_rows) + "\n" if style_rows else "")
            + "        </ul>\n"
            f"      </article>")
    return "\n".join(rows)


def main() -> int:
    if not DIST.exists():
        raise SystemExit("site/dist missing; run build_site.py first")
    lib = json.loads((DIST / "api" / "library.json").read_text(encoding="utf-8"))
    stats = lib["stats"]
    problems: list[str] = []
    report: dict[str, dict] = {}

    for d in sorted(p for p in DIST.iterdir() if p.is_dir()):
        code = d.name
        page = d / "library.html"
        if not page.exists():
            continue
        html = page.read_text(encoding="utf-8")

        cards = load(code, "cards")
        titles = sum(1 for k, v in cards.items()
                     if isinstance(v, dict) and v.get("title"))
        # `en` is the source locale: its card titles ARE the slugs, by design,
        # so "title != slug" is not a coverage signal for it.
        is_source = code == "en"
        # A locale is only publishable if it covers most of the real card set.
        # `cards.json` may legitimately hold style keys too (they are looked up by
        # slug, and many slugs collide), so coverage is measured against the
        # actual card count rather than the entry count.
        covered = sum(1 for c in lib["cards"]
                      if isinstance(cards.get(c["name"]), dict)
                      and cards[c["name"]].get("title")
                      and (is_source or cards[c["name"]]["title"] != c["name"]))
        if titles == 0:
            problems.append(f"{code}: no card titles at all, cannot prerender")
            continue
        if not is_source and covered < len(lib["cards"]) * 0.5:
            problems.append(
                f"{code}: only {covered}/{len(lib['cards'])} cards have a locale title; "
                f"refusing to prerender a locale that is mostly English")
            continue

        block = render_block(code, lib)
        if START in html and END in html:
            head, rest = html.split(START, 1)
            _old, tail = rest.split(END, 1)
            html = f"{head}{START}\n{block}\n      {END}{tail}"
        else:
            problems.append(f"{code}: library.html has no seo:cards markers")

        # static counts must equal the real ones
        for dom_id, _label in COUNT_IDS.items():
            want = stats[{"cardCount": "cardCount", "styleCount": "styleCount",
                          "previewCount": "previewCount"}[dom_id]]
            html = re.sub(rf'(<dd id="{dom_id}"[^>]*>)[^<]*(</dd>)', rf"\g<1>{want}\g<2>", html)
            html = re.sub(rf'(id="{dom_id}"[^>]*>\s*)\d+', rf"\g<1>{want}", html)

        meta = load(code, "meta")
        for key, pattern in (
            ("title", r"<title>.*?</title>"),
            ("description", r'<meta name="description" content="[^"]*">'),
            ("ogTitle", r'<meta property="og:title" content="[^"]*">'),
            ("ogDescription", r'<meta property="og:description" content="[^"]*">'),
        ):
            val = meta.get(key)
            if not val:
                continue
            if key in ("title", "ogTitle"):
                html = re.sub(pattern, f"<title>{esc(val)}</title>" if key == "title"
                              else f'<meta property="og:title" content="{esc(val)}">', html, count=1)
            else:
                attr = "name" if key == "description" else "property"
                prop = "description" if key == "description" else "og:description"
                html = re.sub(pattern, f'<meta {attr}="{prop}" content="{esc(val)}">',
                              html, count=1)

        page.write_text(html, encoding="utf-8")
        report[code] = {
            "cards_prerendered": len(lib["cards"]),
            "cards_with_locale_title": covered,
            "cards_total": len(lib["cards"]),
            "title_coverage_pct": round(100.0 * covered / len(lib["cards"]), 1),
            "has_locale_description":
                sum(1 for v in cards.values()
                    if isinstance(v, dict) and v.get("description")),
            "meta_translated": sorted(k for k, v in meta.items() if v),
        }

    out = {"report": report, "problems": problems}
    (ROOT / "site" / "build" / "prerender_report.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())