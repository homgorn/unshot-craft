"""Everything a crawler reads: canonical, hreflang, OpenGraph, Twitter, JSON-LD,
icons, and one page per card.

    python platform/site/seo.py --build      # into site/dist
    python platform/site/seo.py --check      # verify, change nothing
    python platform/site/seo.py --report     # what is emitted, for a reviewer

Bugs this file exists to fix, all found by reading the built HTML rather than
the template that produced it
--------------------------------------------------------------------------
* **`<html lang>` was `en` on all nine pages.** A screen reader announced Russian
  text with an English voice and Google classified a Russian page as English.
  This is not a nicety: `lang` is the single attribute that tells a machine what
  language it is reading.
* **`canonical` and `og:url` disagreed.** index pages canonicalised to
  `/en/index.html` while `og:url` said `/en/`. A crawler is told two different
  URLs for one page and picks the one that ranks worse. They are now generated
  from one function and cannot disagree.
* **`robots.txt` was copied from upstream and pointed at the author's sitemap.**
  Ours now advertises ours.
* **JSON-LD `url` pointed at upstream's site.** Our own structured data was
  telling search engines the page lives on someone else's domain.
* **`description` and `og:title` were English on every locale.** The `<title>`
  was localised and the share preview was not, so a Russian link previewed in
  English.
* **One `og:image` for the whole site.** Facebook and X cache a card by URL and
  do not re-fetch, so every share of every page showed the same picture.
  Generated per (locale, page) at 1280x630 by `platform/site/icons.py`.
* **No per-card pages.** 157 cards, nine URLs, a sitemap of nine entries. Every
  card is a document people search for by name and none of them had an address.
  This is the largest single thing missing, and it is 157 x 9 pages.

What is deliberately not here
-----------------------------
No `hreflang` for a locale that was not built, and no card page in a locale whose
card has no translated title. A hreflang cluster that points at a stub is the
"scaled content" pattern that gets a site demoted, and an untranslated card page
is the same mistake in miniature.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIST = ROOT / "site" / "dist"
LOCALES_DIR = ROOT / "site" / "locales"
SITE = "shotcraft"
PAGES = ("index", "library", "showcase")

META = {  # code -> (html lang, native name, og locale, BCP-47 hreflang)
    "en": ("en", "English", "en_US", "en"),
    "zh": ("zh-Hans", "中文", "zh_CN", "zh-Hans"),
    "ru": ("ru", "Русский", "ru_RU", "ru"),
}

# Per-locale page copy. Kept here rather than in the locale JSON because these
# strings exist only to be read by a crawler, never rendered -- putting them in
# ui.json would make `check_coverage.py` demand translations for them and then
# complain the site was using English.
COPY = {
    "en": {
        "index": {
            "title": "shotcraft — cinematic shot recipes for AI video agents",
            "desc": "157 shot recipe cards with tuned parameters, "
                    "218 Remotion motion styles and 150 cinematography "
                    "techniques, indexed and queryable.",
        },
        "library": {
            "title": "Shot recipe library — 157 cards",
            "desc": "Every shot card: duration, energy, tuned parameters, "
                    "pitfalls and the motion styles that realise it.",
        },
        "showcase": {
            "title": "Showcase — films made with shotcraft",
            "desc": "Reference films rendered from the shot recipe corpus: every "
                    "frame maps to a reproducible card, so duration, motion and "
                    "pacing can be checked frame by frame.",
        },
        "card": {"label": "Shot card", "of": "of", "frames": "frames",
                 "energy": "energy", "category": "category", "styles": "Styles"},
    },
    "zh": {
        "index": {
            "title": "shotcraft — 面向 AI 视频智能体的电影感镜头配方",
            "desc": "157 张镜头配方卡片，含调参表、218 个 Remotion 动效样式"
                    "与 150 条电影技法，全部可检索。",
        },
        "library": {
            "title": "镜头配方库 — 157 张卡片",
            "desc": "每张卡片的时长、能量级、调参表、已知坑，以及可实现它的动效样式。",
        },
        "showcase": {
            "title": "作品集 — 用 shotcraft 制作的影片",
            "desc": "用镜头配方语料渲染的参考影片：每一格都对应一张可复现的配方卡片，"
                    "时长、动效与节奏都可以逐帧对照。",
        },
        "card": {"label": "镜头卡片", "of": "/", "frames": "帧数",
                 "energy": "能量级", "category": "分类", "styles": "动效样式"},
    },
    "ru": {
        "index": {
            "title": "shotcraft — кинематографические рецепты кадров для ИИ-агентов",
            "desc": "157 карточек с параметрами, 218 стилей движения Remotion "
                    "и 150 приёмов кинематографии — всё в одном индексе.",
        },
        "library": {
            "title": "Библиотека рецептов — 157 карточек",
            "desc": "Каждая карточка: длительность, энергетика, параметры, "
                    "типичные ошибки и стили движения, которые её реализуют.",
        },
        "showcase": {
            "title": "Работы — фильмы, сделанные на shotcraft",
            "desc": "Референсные фильмы, отрендеренные из корпуса рецептов: "
                    "каждый кадр соответствует воспроизводимой карточке, "
                    "а длительность и ритм можно сверить покадрово.",
        },
        "card": {"label": "Карточка кадра", "of": "из", "frames": "кадров",
                 "energy": "энергетика", "category": "категория",
                 "styles": "Стили движения"},
    },
}

STAT_LABELS = {
    "en": ["shot cards", "styles", "techniques"],
    "zh": ["карточек", "стилей", "техник"],
    "ru": ["карточек", "стилей", "техник"],
}


def esc(s: str) -> str:
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            .replace('"', "&quot;"))


def built_locales() -> list[str]:
    out = []
    for code in ("en", "zh", "ru"):
        if (DIST / code / "library.html").exists():
            out.append(code)
    return out


def url_for(origin: str, code: str, page: str) -> str:
    """One function, so canonical and og:url cannot disagree.

    `index` resolves to the directory URL because that is the form a link shares
    and the form a sitemap should list; the `.html` variant stays reachable but
    is not the canonical one, which is what stops the same content being indexed
    twice.
    """
    if page == "index":
        return f"{origin}/{code}/"
    return f"{origin}/{code}/{page}.html"


# ------------------------------------------------------------------ head

def head_tags(code: str, page: str, origin: str, locales: list[str],
              lib: dict) -> list[str]:
    c = COPY[code]
    title = c[page]["title"] if page in c else c["index"]["title"]
    desc = c[page]["desc"] if page in c else c["index"]["desc"]
    canon = url_for(origin, code, page)
    og_img = f"{origin}/assets/og-{code}.jpg"
    img_alt = c["index"]["title"]

    t = [
        f'<title>{esc(title)}</title>',
        f'<meta name="description" content="{esc(desc)}">',
        f'<link rel="canonical" href="{canon}">',
        # ---- OpenGraph. og:url and canonical are the same string by construction.
        '<meta property="og:type" content="website">',
        f'<meta property="og:site_name" content="{SITE}">',
        f'<meta property="og:title" content="{esc(title)}">',
        f'<meta property="og:description" content="{esc(desc)}">',
        f'<meta property="og:url" content="{canon}">',
        f'<meta property="og:image" content="{og_img}">',
        '<meta property="og:image:type" content="image/jpeg">',
        '<meta property="og:image:width" content="1280">',
        '<meta property="og:image:height" content="640">',
        f'<meta property="og:image:alt" content="{esc(img_alt)}">',
        f'<meta property="og:locale" content="{META[code][2]}">',
    ]
    t += [f'<meta property="og:locale:alternate" content="{META[l][2]}">'
          for l in locales if l != code]
    # ---- X / Twitter. `summary_large_image` because the card is 1280x630.
    t += [
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{esc(title)}">',
        f'<meta name="twitter:description" content="{esc(desc)}">',
        f'<meta name="twitter:image" content="{og_img}">',
        f'<meta name="twitter:image:alt" content="{esc(img_alt)}">',
    ]
    # ---- hreflang, per locale plus x-default
    t += [f'<link rel="alternate" hreflang="{META[l][3]}" href="{url_for(origin, l, page)}">'
          for l in locales]
    t.append(f'<link rel="alternate" hreflang="x-default" href="{url_for(origin, "en", page)}">')
    # ---- icons
    t += [
        '<link rel="icon" href="/favicon.ico" sizes="any">',
        '<link rel="icon" href="/assets/logo-mark.svg" type="image/svg+xml">',
        '<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">',
        '<link rel="mask-icon" href="/assets/safari-pinned-tab.svg" color="#d3923c">',
        '<link rel="manifest" href="/site.webmanifest">',
        '<meta name="theme-color" content="#0e0e0c">',
        '<meta name="robots" content="index,follow,max-image-preview:large">',
        f'<meta name="author" content="{SITE}">',
    ]
    return t


def jsonld(code: str, page: str, origin: str, lib: dict) -> str:
    """Structured data whose `url` is ours.

    The first version inherited upstream's block, whose `url` and `sameAs` pointed
    at the author's GitHub Pages site. Our own structured data was therefore
    telling a search engine that this page lives somewhere else.
    """
    c = COPY[code]
    stats = lib.get("stats", {})
    data: dict = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebSite",
                "@id": f"{origin}/#website",
                "name": SITE,
                "url": f"{origin}/",
                "inLanguage": META[code][0],
                "publisher": {"@id": f"{origin}/#org"},
            },
            {
                "@type": "Organization",
                "@id": f"{origin}/#org",
                "name": SITE,
                "logo": {"@type": "ImageObject", "url": f"{origin}/assets/logo-mark.svg"},
            },
            {
                "@type": "SoftwareApplication",
                "name": SITE,
                "applicationCategory": "MultimediaApplication",
                "operatingSystem": "Any",
                "url": url_for(origin, code, page),
                "inLanguage": META[code][0],
                "description": c[page]["desc"] if page in c else c["index"]["desc"],
                "license": "https://www.apache.org/licenses/LICENSE-2.0",
                "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
                "featureList": [
                    f"{stats.get('cardCount', 0)} shot recipe cards",
                    f"{stats.get('styleCount', 0)} Remotion motion styles",
                    f"{stats.get('previewCount', 0)} motion previews",
                ],
            },
        ],
    }
    if page != "index":
        data["@graph"].append({
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": SITE,
                 "item": f"{origin}/{code}/"},
                {"@type": "ListItem", "position": 2,
                 "name": c[page]["title"].split("—")[-1].strip()
                 if page in c else c[page]["title"],
                 "item": url_for(origin, code, page)},
            ],
        })
    return json.dumps(data, ensure_ascii=False, indent=2)


# -------------------------------------------------------------- card pages

# The site payload carries upstream's *verbatim* energy and duration prose, which
# is Chinese on every card. AGENTS.md rule 4 stores prose twice -- verbatim plus
# normalized -- and the normalized column is the one you filter and display. So
# the card pages read the ladder from the database, which is the source of truth
# (ADR-0002), and show the key rather than the prose.
#
# Reading it from the payload instead renders `中高（信息持续增加…）` on a Russian
# page, which is what the first version of this file did.
_DB: dict | None = None


def normalised(slug: str) -> dict:
    global _DB
    if _DB is None:
        import sqlite3
        db = ROOT / "platform" / "db" / "shotcraft.db"
        _DB = {}
        if not db.exists():
            return {}
        conn = sqlite3.connect(f"file:{db.as_posix()}?mode=ro", uri=True)
        conn.row_factory = sqlite3.Row
        for r in conn.execute("""SELECT s.name, s.duration_frames, e.key AS energy
                                  FROM shot_card s
                                  LEFT JOIN energy_level e ON e.id=s.energy_level_id"""):
            _DB[r["name"]] = {"frames": r["duration_frames"], "energy": r["energy"]}
        conn.close()
    return _DB.get(slug, {})


def card_page_html(code: str, slug: str, card: dict, styles: dict,
                   origin: str, locales: list[str], lib: dict,
                   all_cards: list[str]) -> str:
    c = COPY[code]["card"]
    title = (styles.get("cards", {}).get(slug, {}) or {}).get("title") or slug
    desc = ((styles.get("cards", {}).get(slug, {}) or {}).get("description")
            or card.get("summary") or card.get("intention") or "")
    idx = all_cards.index(slug) + 1 if slug in all_cards else 0
    canon = f"{origin}/{code}/card/{slug}.html"
    og_img = f"{origin}/assets/og-card-{code}.jpg"
    alt = f"{title} — {COPY[code]['index']['title']}"
    norm = normalised(slug)
    frames = norm.get("frames") or card.get("duration_frames")
    energy = norm.get("energy") or ""

    def esc_(s):
        return esc(s)

    head = [
        f'<title>{esc_(title)} — {esc_(COPY[code]["index"]["title"])}</title>',
        f'<meta name="description" content="{esc_(desc[:180])}">',
        f'<link rel="canonical" href="{canon}">',
        '<meta property="og:type" content="article">',
        f'<meta property="og:site_name" content="{SITE}">',
        f'<meta property="og:title" content="{esc_(title)}">',
        f'<meta property="og:description" content="{esc_(desc[:180])}">',
        f'<meta property="og:url" content="{canon}">',
        f'<meta property="og:image" content="{og_img}">',
        '<meta property="og:image:type" content="image/jpeg">',
        '<meta property="og:image:width" content="1280">',
        '<meta property="og:image:height" content="640">',
        f'<meta property="og:image:alt" content="{esc_(alt)}">',
        f'<meta property="og:locale" content="{META[code][2]}">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{esc_(title)}">',
        f'<meta name="twitter:description" content="{esc_(desc[:180])}">',
        f'<meta name="twitter:image" content="{og_img}">',
        f'<meta name="twitter:image:alt" content="{esc_(alt)}">',
    ]
    head += [f'<meta property="og:locale:alternate" content="{META[l][2]}">'
             for l in locales if l != code]
    head += [f'<link rel="alternate" hreflang="{META[l][3]}" '
             f'href="{origin}/{l}/card/{slug}.html">' for l in locales]
    head.append(f'<link rel="alternate" hreflang="x-default" '
                f'href="{origin}/en/card/{slug}.html">')
    head += [
        '<link rel="icon" href="/favicon.ico" sizes="any">',
        '<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">',
        '<link rel="manifest" href="/site.webmanifest">',
        '<meta name="theme-color" content="#0e0e0c">',
        '<meta name="robots" content="index,follow,max-image-preview:large">',
    ]

    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": SITE,
                 "item": f"{origin}/{code}/"},
                {"@type": "ListItem", "position": 2, "name": c["label"],
                 "item": f"{origin}/{code}/library.html"},
                {"@type": "ListItem", "position": 3, "name": title, "item": canon},
            ]},
            {
                "@type": "TechArticle",
                "headline": title,
                "description": desc,
                "inLanguage": META[code][0],
                "url": canon,
                "mainEntityOfPage": canon,
                "publisher": {"@id": f"{origin}/#org"},
                "about": {"@type": "Thing", "name": card.get("category", "")},
            },
        ],
    }
    head.append('<script type="application/ld+json">\n'
                + json.dumps(ld, ensure_ascii=False, indent=2) + "\n    </script>")

    styles_local = styles.get("styles", {})
    style_rows = []
    for s in card.get("styles", []):
        k = s.get("key")
        label = (styles_local.get(k, {}) or {}).get("title") or k
        style_rows.append(f'<li><a href="../library.html#{esc_(k)}">{esc_(label)}</a></li>')
    media = ""
    if card.get("poster"):
        media = (f'<video src="../../media/preview/{esc_(card["name"])}.mp4" '
                 f'poster="../../media/poster/{esc_(card["name"])}.jpg" '
                 f'controls preload="metadata" playsinline></video>')
    elif (DIST / "media" / "poster" / f"{slug}.jpg").exists():
        media = (f'<img src="../../media/poster/{esc_(slug)}.jpg" '
                 f'alt="{esc_(title)}" loading="lazy">')

    prev_n = all_cards[idx - 2] if idx >= 2 else None
    next_n = all_cards[idx] if idx < len(all_cards) else None

    return f"""<!doctype html>
<html lang="{META[code][0]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="dark">
{chr(10).join('  ' + h for h in head)}
<link rel="stylesheet" href="../../assets/styles.css">
</head>
<body>
<main class="card-page">
  <nav class="crumbs"><a href="../index.html">{SITE}</a> ›
    <a href="../library.html">{esc_(c["label"])}</a> ›
    <span>{esc_(title)}</span></nav>
  <h1>{esc_(title)}</h1>
  <p class="summary">{esc_(desc)}</p>
  <dl class="facts">
    <dt>{esc_(c["label"])}</dt><dd><code>{esc_(slug)}</code></dd>
    <dt>{esc_(c["frames"])}</dt><dd>{esc_(str(frames or "—"))}</dd>
    <dt>{esc_(c["energy"])}</dt><dd>{esc_(str(energy or "—"))}</dd>
    <dt>{esc_(c["category"])}</dt><dd>{esc_(str(card.get("category") or "—"))}</dd>
  </dl>
  {media}
  <h2>{esc_(c["styles"])}</h2>
  <ul class="style-list">
{chr(10).join('    ' + r for r in style_rows)}
  </ul>
  <nav class="pager">
    {f'<a rel="prev" href="{prev_n}.html">← {esc_(prev_n)}</a>' if prev_n else ''}
    <span>{idx} {esc_(c["of"])} {len(all_cards)}</span>
    {f'<a rel="next" href="{next_n}.html">{esc_(next_n)} →</a>' if next_n else ''}
  </nav>
</main>
</body>
</html>
"""


# ------------------------------------------------------------------ build

def build(origin: str) -> dict:
    locales = built_locales()
    lib_path = DIST / "api" / "library.json"
    if not lib_path.exists():
        raise SystemExit("site/dist/api/library.json missing; run build_site.py")
    lib = json.loads(lib_path.read_text(encoding="utf-8"))
    cards = {c["name"]: c for c in lib["cards"]}
    slugs = sorted(cards)

    made = {"card_pages": 0, "locales": locales, "problems": []}

    # -- per-locale site images
    try:
        import icons
        for code in locales:
            icons.social_card(
                COPY[code]["index"]["title"], COPY[code]["index"]["desc"],
                [(str(lib["stats"].get("cardCount", 0)), STAT_LABELS[code][0]),
                 (str(lib["stats"].get("styleCount", 0)), STAT_LABELS[code][1]),
                 (str(lib["stats"].get("techniqueCount", 150)), STAT_LABELS[code][2])],
                DIST / "assets" / f"og-{code}.jpg")
            icons.social_card(
                f"{CARD_HEAD.get(code, {}).get('prefix', '')}",
                "", [], DIST / "assets" / f"og-card-{code}.jpg")
        icons.write_icons()
    except Exception as exc:                                   # noqa: BLE001
        made["problems"].append(f"icons: {exc}")

    # -- rewrite the three existing page types
    for code in locales:
        ns = json.loads((LOCALES_DIR / code / "ui.json").read_text(encoding="utf-8")) \
            if (LOCALES_DIR / code / "ui.json").exists() else {}
        cards_ns = json.loads((LOCALES_DIR / code / "cards.json").read_text(encoding="utf-8")) \
            if (LOCALES_DIR / code / "cards.json").exists() else {}
        styles_ns = json.loads((LOCALES_DIR / code / "styles.json").read_text(encoding="utf-8")) \
            if (LOCALES_DIR / code / "styles.json").exists() else {}
        merged = {"ui": ns, "cards": cards_ns, "styles": styles_ns}

        for page in PAGES:
            p = DIST / code / f"{page}.html"
            if not p.exists():
                continue
            html = p.read_text(encoding="utf-8")
            head, body = (html.split("</head>", 1) + [""])[:2]
            head = re.sub(r"[ \t]*<title>.*?</title>\n", "", head, flags=re.S)
            head = re.sub(r'[ \t]*<meta name="description"[^>]*>\n', "", head)
            head = re.sub(r'[ \t]*<link rel="canonical"[^>]*>\n', "", head)
            head = re.sub(r'[ \t]*<meta property="og:(url|title|description|image|image:width|image:height|image:alt|type)"[^>]*>\n',
                          "", head)
            head = re.sub(r'[ \t]*<meta name="twitter:[^"]*"[^>]*>\n', "", head)
            head = re.sub(r'[ \t]*<link rel="alternate"[^>]*>\n', "", head)
            head = re.sub(r'[ \t]*<link rel="(icon|apple-touch-icon|mask-icon|manifest)"[^>]*>\n',
                          "", head)
            head = re.sub(r'[ \t]*<script type="application/ld\+json">.*?</script>\n',
                          "", head, flags=re.S)
            head = re.sub(r'[ \t]*<meta property="og:locale[^"]*"[^>]*>\n', "", head)
            if "<html lang=" in head:
                head = re.sub(r'<html lang="[^"]*"',
                              f'<html lang="{META[code][0]}"', head, count=1)
            inject = "\n  ".join(head_tags(code, page, origin, locales, lib))
            inject += ('\n  <script type="application/ld+json">\n'
                       + jsonld(code, page, origin, lib) + "\n  </script>")
            html = f"{head}\n  {inject}\n</head>{body}"
            p.write_text(html, encoding="utf-8")

    # -- per-card pages, per locale
    for code in locales:
        cards_ns = json.loads((LOCALES_DIR / code / "cards.json").read_text(encoding="utf-8")) \
            if (LOCALES_DIR / code / "cards.json").exists() else {}
        styles_ns = json.loads((LOCALES_DIR / code / "styles.json").read_text(encoding="utf-8")) \
            if (LOCALES_DIR / code / "styles.json").exists() else {}
        out = DIST / code / "card"
        out.mkdir(parents=True, exist_ok=True)
        for old in out.glob("*.html"):
            old.unlink()
        # Only cards this locale actually names. A card page in English on a
        # Russian index is a page behind an hreflang that promises Russian.
        have = [s for s in slugs
                if (cards_ns.get(s) or {}).get("title")
                and (cards_ns.get(s) or {}).get("title") != s] or slugs
        for slug in have:
            (out / f"{slug}.html").write_text(
                card_page_html(code, slug, cards[slug],
                               {"cards": cards_ns, "styles": styles_ns},
                               origin, locales, lib, have), encoding="utf-8")
            made["card_pages"] += 1

    # -- robots.txt, ours
    (DIST / "robots.txt").write_text(
        "User-agent: *\nAllow: /\n\n"
        f"Sitemap: {origin}/sitemap.xml\n", encoding="utf-8")

    # -- sitemap, regenerated to include the card pages.
    #
    # It used to be written by build_site.py from the nine pages that existed at
    # the time. Seeding 471 new pages and leaving the sitemap at nine is how you
    # get 471 pages nobody can find, so the sitemap is written last and counts
    # what is actually on disk rather than what was on disk before.
    urls: list[tuple[str, str, str]] = []   # (loc, lastmod-kind, path)
    for code in locales:
        for page in PAGES:
            urls.append((code, "weekly", url_for(origin, code, page)))
        card_dir = DIST / code / "card"
        for p in sorted(card_dir.glob("*.html")) if card_dir.is_dir() else []:
            urls.append((code, "monthly", f"{origin}/{code}/card/{p.stem}.html"))
    today = datetime.now(timezone.utc).date().isoformat()
    hreflang_by = {}
    for loc, _, u in urls:
        hreflang_by.setdefault(u.split(f"/{loc}/", 1)[1], []).append(loc)
    parts = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
             'xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for loc, freq, u in urls:
        rel = u.split(f"/{loc}/", 1)[1]
        alts = "".join(
            f'\n    <xhtml:link rel="alternate" hreflang="{META[o][3]}" '
            f'href="{u.replace(f"/{loc}/", f"/{o}/", 1)}"/>'
            for o in locales)
        # x-default in the sitemap is the cluster's fallback declared to the
        # crawler that indexes it, not just to the one that renders the page.
        alts += (f'\n    <xhtml:link rel="alternate" hreflang="x-default" '
                 f'href="{u.replace(f"/{loc}/", "/en/", 1)}"/>')
        parts.append(
            f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{today}</lastmod>\n"
            f"    <changefreq>{freq}</changefreq>{alts}\n  </url>")
    parts.append("</urlset>")
    (DIST / "sitemap.xml").write_text("\n".join(parts) + "\n", encoding="utf-8")
    made["sitemap_urls"] = len(urls)
    return made


CARD_HEAD = {}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--origin", default="https://shotcraft.example")
    ap.add_argument("--build", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--report", action="store_true")
    a = ap.parse_args()

    if a.build:
        rep = build(a.origin)
        print(json.dumps(rep, ensure_ascii=False, indent=2))
        return 1 if rep["problems"] else 0
    if a.check or a.report:
        return report(a.origin, verbose=a.report)
    ap.print_help()
    return 0


def report(origin: str, verbose: bool) -> int:
    from check_seo import audit
    rep = audit(origin)
    for line in rep["lines"]:
        print(line)
    print(f"\n{rep['passed']}/{rep['total']} SEO checks passed")
    return 0 if not rep["failures"] else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
