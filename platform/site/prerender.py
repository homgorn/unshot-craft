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

# Scratch counters for the last render_block() call, so main() can report them
# without threading a mutable through the string builder.
BLOCKS: dict = {}


def esc(s: str) -> str:
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace('"', "&quot;"))


def load(code: str, name: str) -> dict:
    p = LOCALES / code / f"{name}.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def clip_for(card: dict, media_dir: Path) -> tuple[str, str | None]:
    """The (clip, poster) pair for a card, from the payload and the filesystem.

    Existence is checked against disk, not inferred from the payload. `library.json`
    lists a `media.url` for all 214 preview styles, and a URL in a JSON file is a
    claim rather than a fact: writing it into the HTML for a file that is not
    there produces a page whose video element 404s, which looks identical to one
    that works until someone presses play.
    """
    for s in card.get("styles", []):
        m = s.get("media") or {}
        url = m.get("url") or ""
        if not url or m.get("type") != "mp4":
            continue
        base = url.split("?")[0].replace("./media/", "").removesuffix(".mp4")
        clip = media_dir / f"{base}.mp4"
        if clip.exists():
            poster = media_dir / "poster" / f"{base}.jpg"
            # Only 64 of the 214 previews have a poster. A `poster` attribute
            # pointing at a missing file is worse than none: the browser shows
            # the broken frame instead of the video's own first frame.
            return f"../media/{base}.mp4", (
                f"../media/poster/{base}.jpg" if poster.exists() else None)
    return "", None


def render_block(code: str, lib: dict) -> str:
    cards = load(code, "cards")
    styles = load(code, "styles")
    media_dir = DIST / "media"
    rows: list[str] = []
    with_video = 0
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

        # The video is in the prerendered block, not only in app.js.
        #
        # app.js does render one at runtime, so every gate here was green while
        # the static file carried 157 cards and no motion. A crawler is not a
        # browser: it reads the file, sees text, and cannot tell that a <video>
        # would appear a second later. The 214 previews are the product, and the
        # prerender is the copy of the page that is actually served to the thing
        # that decides whether the page is worth indexing.
        clip, poster = clip_for(card, media_dir)
        media_tag = ""
        if clip:
            with_video += 1
            poster_attr = f' poster="{esc(poster)}"' if poster else ""
            # Wrapped in the site's own `.preview` container rather than a new
            # class: upstream's stylesheet already sizes `.preview video` to a
            # 16/9 crop, and a bare <video> would render at its natural 480x270
            # inside a card that is not 480 wide.
            media_tag = (
                f'        <div class="preview">\n'
                f'          <video src="{esc(clip)}"'
                f'{poster_attr} muted loop playsinline preload="metadata"'
                f' aria-label="{esc(title)}"></video>\n'
                f'        </div>\n')

        rows.append(
            f'      <article class="shot-card" id="{esc(name)}">\n'
            f"        <h3>{esc(title)}</h3>\n"
            f"        <p>{esc(desc)}</p>\n"
            f"{media_tag}"
            f"        <ul class=\"style-list\">\n"
            + ("\n".join(style_rows) + "\n" if style_rows else "")
            + "        </ul>\n"
            f"      </article>")
    BLOCKS["with_video"] = with_video
    return "\n".join(rows)


def main() -> int:
    if not DIST.exists():
        raise SystemExit("site/dist missing; run build_site.py first")
    lib = json.loads((DIST / "api" / "library.json").read_text(encoding="utf-8"))
    stats = lib["stats"]
    problems: list[str] = []
    warnings: list[str] = []
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

        # A prerender with no video in it is a build that succeeded and shipped
        # nothing worth looking at. It is reported rather than raised, because a
        # fresh clone legitimately has no media until `mirror_site.py --media`
        # has been run, and refusing to build at all would be worse than building
        # with the gap named. `platform/site/check_seo.py` is the gate that fails
        # on it -- one authority for the fact, not two.
        with_video = BLOCKS.get("with_video", 0)
        if with_video == 0:
            warnings.append(
                f"{code}: no card in the prerendered block has a playable clip. "
                f"site/dist/media holds "
                f"{len(list((DIST / 'media').glob('*.mp4'))) if (DIST / 'media').is_dir() else 0} "
                f"mp4; run `python platform/mirror_site.py --media` if that is 0, "
                f"then build_site.py. check_seo.py fails until you do.")
        elif with_video < len(lib["cards"]) * 0.5:
            warnings.append(
                f"{code}: only {with_video}/{len(lib['cards'])} cards got a clip; "
                f"the library reads as a text list for most of it")

        report[code] = {
            "cards_prerendered": len(lib["cards"]),
            "cards_with_locale_title": covered,
            "cards_with_clip": with_video,
            "cards_total": len(lib["cards"]),
            "title_coverage_pct": round(100.0 * covered / len(lib["cards"]), 1),
            "has_locale_description":
                sum(1 for v in cards.values()
                    if isinstance(v, dict) and v.get("description")),
            "meta_translated": sorted(k for k, v in meta.items() if v),
        }

    out = {"report": report, "warnings": warnings, "problems": problems}
    (ROOT / "site" / "build" / "prerender_report.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(out, ensure_ascii=False, indent=2))

    # A stamp, because the ordering here is load-bearing and fails silently.
    #
    # `prerender.py` bakes translated card text into the static HTML block, and
    # `build_site.py` regenerates that page from the template. Running the build
    # *after* the prerender therefore drops every translation and re-exposes the
    # Chinese corpus -- with no error, no warning, and a green selftest, because
    # the runtime check reads the DOM after the i18n script has patched it back.
    #
    # That is not hypothetical: it happened here, and the only reason it was
    # noticed is a check added afterwards that reads the static file with no
    # JavaScript in the loop. The stamp turns "the build ran after the prerender"
    # into a state a gate can see instead of a state nobody can.
    (DIST / ".prerendered.json").write_text(json.dumps({
        "locales": sorted(report),
        "cards_baked": {loc: report[loc].get("cards") for loc in sorted(report)},
        "built_by": "platform/site/prerender.py",
        "note": ("delete this and re-run build_site.py and it will not come back; "
                 "that is the point. scripts/init.ps1 runs build then prerender."),
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())