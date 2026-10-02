"""F011/F012/F013: build the locale-prefixed static site.

    python platform/site/build_site.py
    python platform/site/build_site.py --serve 4178

Input : site/locales/<code>/*.json        (source of truth, ADR-0004)
        upstream/video-shotcraft/gallery/  (templates + static assets)
Output: site/dist/<locale>/{index,library,showcase}.html
        site/dist/assets/{app.js,showcase.js,styles.css,i18n.js,i18n/<code>.js}
        site/dist/api/library.json
        site/dist/index.html              (Accept-Language redirect + no-JS list)
        site/dist/sitemap.xml
        site/build/coverage.json

The three upstream inline i18n mechanisms are collapsed into one runtime
(site/build/runtime/i18n.js). app.js and showcase.js are patched by an ordered,
asserted replacement list: if an upstream edit moves an anchor, the build fails
loudly instead of silently serving an untranslated page.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GALLERY = ROOT / "upstream" / "video-shotcraft" / "gallery"
LOCALES_DIR = ROOT / "site" / "locales"
DIST = ROOT / "site" / "dist"
RUNTIME = ROOT / "site" / "build" / "runtime"

PAGES = ("index", "library", "showcase")
LOCALE_ORDER = ("en", "zh", "ru", "es", "de", "fr", "pt", "ko", "ja")

# Names and hreflang tags. Locales absent from this table are not built at all,
# so an unfinished locale cannot accidentally ship behind an hreflang tag.
META = {
    "en": ("en-US", "English", "en_US", "ltr"),
    "zh": ("zh-CN", "中文", "zh_CN", "ltr"),
    "ru": ("ru-RU", "Русский", "ru_RU", "ltr"),
    "es": ("es-ES", "Español", "es_ES", "ltr"),
    "de": ("de-DE", "Deutsch", "de_DE", "ltr"),
    "fr": ("fr-FR", "Français", "fr_FR", "ltr"),
    "pt": ("pt-BR", "Português", "pt_BR", "ltr"),
    "ko": ("ko-KR", "한국어", "ko_KR", "ltr"),
    "ja": ("ja-JP", "日本語", "ja_JP", "ltr"),
}

# --------------------------------------------------------------------------
# Asserted patch sets. Each entry: (find, replace, expected_count, label)
# A changed upstream file must fail the build here, not ship broken.
# --------------------------------------------------------------------------

APP_PATCHES: list[tuple[str, str, int, str]] = [
    ("const translations = window.GALLERY_I18N;",
     "const translations = window.__I18N__.legacy();\n"
     "// the switcher is generated from data, so a new locale needs no HTML edit\n"
     "window.__I18N__.mountSwitcher();", 1, "i18n source"),
    ("const libraryEndpoint = staticGallery ? './api/library.json' : '/api/library';",
     "const libraryEndpoint = staticGallery ? '../api/library.json' : '/api/library';", 1, "library path"),
    ("  language: savedLanguage === 'zh' ? 'zh' : 'en',",
     "  language: window.__I18N__.locale,", 1, "locale from URL"),
    ("const text = (key) => translations.ui[state.language][key] || key;",
     "const text = (key) => window.__I18N__.s('ui', key);", 1, "text()"),
    ("""const cardName = (card) => state.language === 'zh'
  ? translations.cardsZh[card.name] || card.name
  : card.name;""",
     "const cardName = (card) => window.__I18N__.t('cards', card.name).title || card.name;", 1, "cardName"),
    ("""const styleName = (style) => state.language === 'zh'
  ? translations.stylesZh[style.key] || style.label
  : style.key;""",
     "const styleName = (style) => window.__I18N__.t('styles', style.key).title || style.key;", 1, "styleName"),
    # The card description had two sources, so the same card read one way in the
    # static HTML and another way a second later.
    #
    # The prerender writes the locale's own description from `cards.json`. The
    # runtime's path for the same field is `cardDescription()`, and it read
    # `translations.stylesEn` / `cardsEn` -- **English on every locale**. So
    # /ru/library.html served Russian descriptions from the prerender and English
    # ones from the runtime, and which one a reader saw depended on whether
    # app.js had finished re-rendering.
    #
    # Two earlier attempts at this failed in instructive ways, and both are why
    # the patch is anchored on the whole function body now:
    #
    # * patching the bare line `return (multi && style?.description) || ...`
    #   with `required=1` matched the **CJK branch** of `cardDescription` and
    #   turned it into a call to itself -- unbounded recursion, thrown on the
    #   first zh or ja render;
    # * declaring a new `const cardDescription` collided with the one upstream
    #   already had, and `SyntaxError: Identifier 'cardDescription' has already
    #   been declared` killed the whole runtime -- on every locale.
    #
    # Both were invisible to every gate, because the file is valid and the
    # static block still carries the right text. Only the browser console caught
    # the second, which is why the selftest reads page errors.
    #
    # Note the style description is not a fallback for the card one here: the
    # `styles` namespace holds titles only, in every locale, because style
    # descriptions were never translated. Card descriptions were.

    ("  if (state.language === 'zh') {",
     "  if (window.__I18N__.isCJK()) {", 1, "description branch"),
    ("  document.documentElement.lang = state.language === 'zh' ? 'zh-CN' : 'en';",
     "  document.documentElement.lang = window.__I18N__.htmlLang();", 1, "html lang"),
    ("  elements.languageToggleLabel.textContent = state.language === 'zh' ? 'EN' : '中文';",
     "  elements.languageToggle.hidden = true;", 1, "hide inline toggle"),
    ("  const subtitle = state.language === 'zh' ? card.name : '';",
     "  const subtitle = window.__I18N__.isCJK() ? card.name : '';", 1, "subtitle"),
    # Upstream renders cards asynchronously and never reads location.hash, so a
    # deep link such as library.html#crash-zoom-punch never scrolls anywhere.
    # The wiki links to card anchors, so this has to work.
    ("""elements.themeToggle.addEventListener('click', () => {""",
     """window.__I18N__.scrollToHash = () => {
  const id = decodeURIComponent(location.hash.slice(1));
  if (!id) return;
  // recompute switcher hrefs too: a deep link may have arrived as a bare
  // fragment change, in which case the page never reloaded and the hrefs
  // captured at mount time are stale.
  window.__I18N__.refreshSwitcher();
  const el = document.getElementById(id);
  if (el) el.scrollIntoView({block: 'start'});
};

elements.themeToggle.addEventListener('click', () => {""", 1, "hash scroll helper"),
    # Cards are rendered by loadLibrary(), so the scroll must happen after that
    # promise settles — not after a filter click.
    ("""showLoadingCards();
loadLibrary();""",
     """showLoadingCards();
// deep links resolve after the cards exist; upstream never reads location.hash,
// so library.html#crash-zoom-punch used to land at the top of the page.
loadLibrary().then(() => window.__I18N__.scrollToHash());""", 1, "hash scroll on load"),
    ("""elements.languageToggle.addEventListener('click', () => {
  state.language = state.language === 'zh' ? 'en' : 'zh';
  try {
    localStorage.setItem('video-shot-gallery-language', state.language);
  } catch {}
  applyLanguage();
  render();
});""",
     """elements.languageToggle.addEventListener('click', () => {
  const codes = window.__I18N__.locales.map((l) => l.code);
  const next = codes[(codes.indexOf(window.__I18N__.locale) + 1) % codes.length];
  location.href = window.__I18N__.urlFor(next);
});""", 1, "toggle navigates"),
    ("""const cardDescription = (card, style) => {
  const multi = card.styles.length > 1;
  if (window.__I18N__.isCJK()) {
    return (multi && style?.description) || card.summary || card.intention;
  }
  return (multi && translations.stylesEn[style?.key])
    || translations.cardsEn[card.name] || card.name.split('-').join(' ');
};""",
     """const cardDescription = (card, style) => {
  // One source for both paths: the locale. The prerender already reads
  // `cards.json` for this field, and reading a different one here is what made
  // the static and runtime views disagree. The style branch is gone rather than
  // redirected: the `styles` namespace carries titles only, in every locale,
  // because style descriptions were never translated.
  //
  // The fallbacks are the *corpus*, not a prettified slug. `zh` is the source
  // locale: its card entries carry no `description`, because upstream's Chinese
  // prose already IS the description and lives in `card.summary`. Dropping that
  // fallback put 'crash zoom punch' on the Chinese page -- a slug with the
  // dashes replaced by spaces, which is worse than either language's real text.
  return window.__I18N__.t('cards', card.name).description
    || card.summary || card.intention || card.name.split('-').join(' ');
};""", 1, "cardDescription reads the locale"),
]

SHOWCASE_PATCHES: list[tuple[str, str, int, str]] = [
    ("const SHOWCASE_L10N = {", "const SHOWCASE_L10N_UNUSED = {", 1, "neutralize inline dict"),
    ("const state = {",
     "// the switcher is generated from data, so a new locale needs no HTML edit\n"
     "window.__I18N__.mountSwitcher();\nconst state = {", 1, "mount switcher"),
    ("const text = (key) => SHOWCASE_L10N[state.language][key] || SHOWCASE_L10N.en[key] || key;",
     "const text = (key) => window.__I18N__.s('showcase', key);", 1, "showcase text()"),
    ("  language: (() => {\n"
     "    try { return localStorage.getItem('video-shot-gallery-language') === 'zh' ? 'zh' : 'en'; } catch { return 'en'; }\n"
     "  })(),",
     "  language: window.__I18N__.locale,", 1, "showcase locale"),
    ("  document.documentElement.lang = state.language === 'zh' ? 'zh-CN' : 'en';",
     "  document.documentElement.lang = window.__I18N__.htmlLang();", 1, "showcase html lang"),
    ("  elements.languageToggleLabel.textContent = state.language === 'zh' ? 'EN' : '中文';",
     "  elements.languageToggle.hidden = true;", 1, "showcase hide toggle"),
    ("  state.language = state.language === 'zh' ? 'en' : 'zh';\n"
     "  try { localStorage.setItem('video-shot-gallery-language', state.language); } catch {}\n"
     "  applyLanguage();\n  render();",
     "  const codes = window.__I18N__.locales.map((l) => l.code);\n"
     "  location.href = window.__I18N__.urlFor(\n"
     "    codes[(codes.indexOf(window.__I18N__.locale) + 1) % codes.length]);", 1, "showcase toggle"),
]

# `expected` is 0 for anchors that legitimately vary per page: the builder only
# complains when an anchor that must exist is missing.
LOCALE_CSS = """  /* Data-driven language switcher (site/build/runtime/i18n.js) */
  /* Inline flag: always visible, no hover needed, so a Russian or Japanese
     visitor who cannot decode Latin script can still find their language. */
  .locale-nav { position: relative; }
  .locale-flag {
    display: inline-flex; align-items: center; justify-content: center;
    border: 1px solid var(--line); border-radius: 999px;
    padding: .38rem .95rem; background: rgba(14,14,12,.35);
    backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px);
    color: var(--muted); font: inherit; font-size: .8rem; cursor: pointer;
    white-space: nowrap; list-style: none;
    transition: color 150ms ease, border-color 150ms ease;
  }
  .locale-flag:hover { color: var(--text); border-color: rgba(211,146,60,.65); }
  .locale-flag-icon { display: inline-flex; align-items: center; margin-right: .4rem; }
  .locale-flag-icon svg { width: 15px; height: 15px; fill: none; stroke: currentColor;
                          stroke-width: 1.6; stroke-linecap: round; stroke-linejoin: round; }
  .locale-list {
    position: absolute; right: 0; top: calc(100% + 8px); z-index: 20;
    display: flex; flex-direction: column; min-width: 168px; padding: 6px;
    background: rgba(14,14,12,.97); border: 1px solid var(--line);
    border-radius: 12px; box-shadow: 0 16px 48px rgba(0,0,0,.55);
    opacity: 0; visibility: hidden; transform: translateY(-4px);
    transition: opacity 150ms ease, transform 150ms ease, visibility 150ms;
  }
  .locale-nav:hover .locale-list, .locale-nav:focus-within .locale-list,
  .locale-nav.is-open .locale-list {
    opacity: 1; visibility: visible; transform: translateY(0);
  }
  .locale-item {
    display: block; padding: 8px 12px; border-radius: 8px;
    color: var(--muted); font-size: .86rem; text-decoration: none;
  }
  .locale-item:hover { background: rgba(240,237,229,.08); color: var(--text); }
  .locale-item.is-current { color: var(--accent); font-weight: 700; }
  /* the upstream inline toggle is superseded by the switcher above */
  .language-toggle[hidden] { display: none; }
"""

HTML_PATCHES: list[tuple[str, str, int, str]] = [
    ('<link rel="stylesheet" href="./styles.css">',
     '<link rel="stylesheet" href="../assets/styles.css">', 0, "css"),
    ('<script src="./translations.js" defer></script>', "", 0, "drop translations.js"),
    ('<script src="./app.js" defer></script>',
     '<script src="../assets/i18n/{code}.js"></script>\n'
     '  <script src="../assets/i18n.js"></script>\n'
     '  <script src="../assets/app.js" defer></script>', 0, "app scripts"),
    ('<script src="./showcase.js" defer></script>',
     '<script src="../assets/i18n/{code}.js"></script>\n'
     '  <script src="../assets/i18n.js"></script>\n'
     '  <script src="../assets/showcase.js" defer></script>', 0, "showcase scripts"),
    ('href="./logo-mark.svg"', 'href="../assets/logo-mark.svg"', 0, "favicon"),
    ('src="./logo-mark-reverse.svg"', 'src="../assets/logo-mark-reverse.svg"', 0, "logo reverse"),
    ('src="./logo-mark.svg"', 'src="../assets/logo-mark.svg"', 0, "logo"),
    ('fetch(\'./api/library.json\'', "fetch('../api/library.json'", 0, "index fetch"),
    # ADR-0005: an independent fork with its own brand. Upstream's name is
    # hardcoded in the topbar of every page and it is the first thing a visitor
    # reads -- while the manifest, the icons, the structured data and every social
    # card this project generates already say `shotcraft`. The page and its own
    # metadata were disagreeing about who this is.
    #
    # Deliberately NOT a `data-i18n` key: a brand name is a proper noun and is
    # spelled the same in every language. Putting it in the locale JSON would
    # mean three copies that must stay identical, and a locale that "translated"
    # it would be the bug.
    ('<span>VIDEO SHOTCRAFT</span>', '<span>shotcraft</span>', 0, "brand name"),
    ('<span>video-shotcraft</span>', '<span>shotcraft</span>',
     0, "brand name, lowercase"),
    # Media paths are rewritten by prefix, not by quoting style. Two separate
    # entries used to try to match `'./media/...'` and `` `./media/...` ``, and
    # the wall's own source uses backticks -- so the poster entry never matched
    # and the clips pointed one directory too shallow. `apply_patches` counts
    # matches and the count was `required=0`, so a miss was silent: 64 posters
    # and 214 clips, all fetched from a URL that 404s.
    ("./media/", "../media/", 0, "wall media paths"),
    ('href="./showcase.html"', 'href="../{code}/showcase.html"', 0, "nav showcase"),
    ('href="./library.html"', 'href="../{code}/library.html"', 0, "nav library"),
    ('href="./"', 'href="../{code}/"', 0, "nav home"),
    # Upstream hardcodes its own origin into canonical/og:url. Ours must be
    # self-referencing per locale, so the upstream values are stripped and
    # re-emitted by inject_head(). A second canonical pointing at the author's
    # domain tells a crawler the two pages are duplicates of *his*, which would
    # hand the ranking to the upstream site on every locale we build.
    ('<link rel="canonical" href="https://vincentwei1021.github.io/video-shotcraft/"', "", 0, "strip canonical index"),
    ('<link rel="canonical" href="https://vincentwei1021.github.io/video-shotcraft/library.html"', "", 0, "strip canonical library"),
    ('<link rel="canonical" href="https://vincentwei1021.github.io/video-shotcraft/showcase.html"', "", 0, "strip canonical showcase"),
    ('<meta property="og:url" content="https://vincentwei1021.github.io/video-shotcraft/', '<meta property="og:url" content="{origin}/{code}/', 0, "og:url"),
    ('content="https://vincentwei1021.github.io/video-shotcraft/og-image.jpg', 'content="{origin}/assets/og-image.jpg', 0, "og:image"),
]


def load_locale(code: str) -> dict:
    """Read a locale into runtime namespaces.

    On disk a locale is a flat `ui.json` with `page.` / `showcase.` prefixes,
    because that is what a translator wants to see. The runtime wants three
    namespaces, because `page.*` and `ui` can legitimately share a word
    (`documentTitle` exists on both library and showcase). Slicing here keeps
    that detail in one place.
    """
    d = LOCALES_DIR / code
    if not d.is_dir():
        return {}
    out: dict[str, dict] = {}
    for f in sorted(d.glob("*.json")):
        if f.stem.startswith("_") or f.stem == "MISSING":
            continue
        out[f.stem] = {k: v for k, v in json.loads(f.read_text(encoding="utf-8")).items()
                       if not k.startswith("_")}
    ui = out.setdefault("ui", {})
    for prefix in ("page", "showcase"):
        bucket = out.setdefault(prefix, {})
        for k in [k for k in ui if k.startswith(prefix + ".")]:
            bucket[k[len(prefix) + 1:]] = ui.pop(k)
    return out


def fill(tmpl: str, code: str, origin: str) -> str:
    """Substitute only our own placeholders.

    `str.format` is wrong here: the JS replacements contain CSS/JS braces, so a
    format() call dies on the first literal `{`. Placeholders are therefore
    replaced by literal string substitution, which cannot misread a brace.
    """
    return tmpl.replace("{code}", code).replace("{origin}", origin.rstrip("/"))


def apply_patches(src: str, patches, code: str, problems: list[str], label: str,
                  origin: str = "") -> str:
    for find, repl, expected, name in patches:
        n = src.count(find)
        if expected and n != expected:
            problems.append(f"{label}.{name}: anchor matched {n}x, expected {expected}")
            continue
        if not expected and n == 0:
            continue
        src = src.replace(find, fill(repl, code, origin))
    return src


def head_block(code: str, page: str, origin: str, locales: list[str]) -> str:
    """hreflang + canonical + og:locale. Emitted on every page of every locale."""
    tags = [f'    <link rel="canonical" href="{origin}/{code}/{page}.html">',
            f'    <meta property="og:locale" content="{META[code][2]}">']
    tags += [f'    <meta property="og:locale:alternate" content="{META[l][2]}">'
             for l in locales if l != code]
    tags += [f'    <link rel="alternate" hreflang="{l}" href="{origin}/{l}/{page}.html">'
             for l in locales]
    tags.append('    <link rel="alternate" hreflang="x-default" href="{0}/en/{1}.html">'.format(origin, page))
    return "\n".join(tags)


def build() -> dict:
    problems: list[str] = []
    warnings: list[str] = []
    present = [c for c in LOCALE_ORDER if (LOCALES_DIR / c).is_dir()]
    if not present:
        raise SystemExit("no locales found; run platform/site/extract_locales.py first")

    # Only locales that actually have content are advertised. An empty scaffold
    # directory must not produce an hreflang cluster pointing at blank pages:
    # that is precisely the "scaled content abuse" pattern search engines punish.
    locales = []
    for c in present:
        if c in ("en", "zh"):
            locales.append(c)
            continue
        ns = load_locale(c)
        cards = ns.get("cards", {})
        titled = sum(1 for v in cards.values() if v.get("title"))
        ui = len(ns.get("ui", {}))
        if titled == 0 and ui == 0:
            print(f"  skip {c}: no translated content (scaffold only)")
            continue
        locales.append(c)
    if not locales:
        raise SystemExit("every locale is empty")

    if DIST.exists():
        shutil.rmtree(DIST)
    (DIST / "assets" / "i18n").mkdir(parents=True, exist_ok=True)
    (DIST / "api").mkdir(parents=True, exist_ok=True)

    # ---- static assets -----------------------------------------------------
    for name in ("styles.css", "logo-mark.svg", "logo-mark-reverse.svg", "og-image.jpg"):
        src = GALLERY / name
        if src.exists():
            shutil.copy2(src, DIST / "assets" / name)
    shutil.copy2(GALLERY / "api" / "library.json", DIST / "api" / "library.json")
    shutil.copy2(RUNTIME / "i18n.js", DIST / "assets" / "i18n.js")
    # The switcher is generated, so its CSS ships with the generated CSS rather
    # than being patched into a third hand-maintained copy of styles.css.
    css = (DIST / "assets" / "styles.css").read_text(encoding="utf-8") if (DIST / "assets" / "styles.css").exists() else ""
    if css:
        (DIST / "assets" / "styles.css").write_text(css + "\n" + LOCALE_CSS, encoding="utf-8")
    media_report = deploy_media(problems, warnings)

    # ---- patched JS --------------------------------------------------------
    app = apply_patches((GALLERY / "app.js").read_text(encoding="utf-8"),
                        APP_PATCHES, "en", problems, "app.js")
    (DIST / "assets" / "app.js").write_text(app, encoding="utf-8")
    sc = apply_patches((GALLERY / "showcase.js").read_text(encoding="utf-8"),
                       SHOWCASE_PATCHES, "en", problems, "showcase.js")
    (DIST / "assets" / "showcase.js").write_text(sc, encoding="utf-8")

    # ---- per-locale data + pages ------------------------------------------
    origin = "https://shotcraft.example"   # overridden by --origin at deploy
    # Every generated bundle carries ALL built locales, keyed ns -> locale -> key.
    # Shipping only the active locale would break the runtime's `locale -> en`
    # fallback chain with no network available to fetch a second file.
    bundles = {c: load_locale(c) for c in locales}
    merged: dict[str, dict[str, dict]] = {}
    for c, ns_map in bundles.items():
        for ns, kv in ns_map.items():
            merged.setdefault(ns, {})[c] = kv
    # 'en' must always be present as the fallback, even if its own dir is absent
    if "en" not in locales and load_locale("en"):
        for ns, kv in load_locale("en").items():
            merged.setdefault(ns, {}).setdefault("en", kv)

    coverage: dict[str, dict] = {}
    for code in locales:
        meta = {"htmlLang": META[code][0], "nativeName": META[code][1],
                "ogLocale": META[code][2], "dir": META[code][3]}
        merged.setdefault("meta", {})[code] = {**meta}

        payload = {
            "locale": code,
            "fallback": "en",
            "locales": [{"code": c, "nativeName": META[c][1], "htmlLang": META[c][0]}
                        for c in locales],
            "ns": merged,
        }
        (DIST / "assets" / "i18n" / f"{code}.js").write_text(
            "window.__I18N_DATA__ = " + json.dumps(payload, ensure_ascii=False, indent=None) + ";\n",
            encoding="utf-8")

        page_problems: list[str] = []
        for page in PAGES:
            tmpl = GALLERY / f"{page}.html"
            if not tmpl.exists():
                continue
            html = tmpl.read_text(encoding="utf-8")
            if page == "index":
                html = strip_inline_l10n(html)
            html = apply_patches(html, HTML_PATCHES, code, page_problems, f"{page}.html", origin)
            html = inject_runtime(html, code)
            html = inject_head(html, code, page, origin, locales)
            html = inject_switcher(html)
            d = DIST / code
            d.mkdir(parents=True, exist_ok=True)
            if page == "index":
                assert_wall(html, code, page_problems)
            (d / f"{page}.html").write_text(html, encoding="utf-8")
        # Only a locale whose pages are broken fails the build; a per-locale
        # problem must not be reported once per locale.
        if page_problems:
            problems.extend(sorted(set(page_problems)))

        coverage[code] = measure_coverage(code, bundles[code])

    write_root_index(locales, origin)
    write_sitemap(locales, origin)
    (ROOT / "site" / "build" / "coverage.json").write_text(
        json.dumps(coverage, ensure_ascii=False, indent=2), encoding="utf-8")

    return {"locales": locales, "coverage": coverage, "problems": problems,
            "warnings": warnings, "media": media_report}


def deploy_media(problems: list[str], warnings: list[str]) -> dict:
    """Assemble site/dist/media from the two places the media actually live.

    Upstream's git tree holds **posters only** -- `gallery/media/poster/*.jpg`,
    64 files, 0.8 MB. The **214 mp4 previews are not in git at all**; they are
    published as GitHub releases and `platform/mirror_site.py --media`
    downloads them into `upstream/site-mirror/media/`. That split is the whole
    reason the site shipped with no motion, and the previous code could not have
    found the videos even if it had worked.

    It symlinked `site/dist/media` at `gallery/media`. Two things went wrong and
    neither was visible:

    * **the symlink failed.** Windows without developer mode raises `OSError`,
      and the handler was `pass` -- so the directory simply was not there;
    * **even on success it would have been posters without videos**, since the
      mp4s are in the other tree.

    So: copy both, and fail loudly when a source is missing. "The site built fine
    and has no video" is not a state anyone should be able to reach by accident,
    and the failure that produced it was a bare `pass`.

    Copying rather than linking is deliberate. A symlink does not survive being
    uploaded to Cloudflare Pages, and it does not survive being opened by someone
    who has not run the mirror.
    """
    posters = GALLERY / "media" / "poster"
    videos = ROOT / "upstream" / "site-mirror" / "media"

    n_posters = n_videos = 0
    if posters.is_dir():
        dest = DIST / "media" / "poster"
        dest.mkdir(parents=True, exist_ok=True)
        for p in posters.glob("*.jpg"):
            shutil.copy2(p, dest / p.name)
            n_posters += 1
    else:
        warnings.append(
            f"no posters at {posters}; the wall will fall back to the clip's own "
            f"first frame. Run: python platform/mirror_site.py --media")

    if videos.is_dir():
        for p in videos.glob("*.mp4"):
            shutil.copy2(p, DIST / "media" / p.name)
            n_videos += 1
        # The mirror also parks posters next to the clips; skip them, they are
        # already copied from the tree that is in git.
    else:
        warnings.append(
            f"no video previews at {videos}. The 214 mp4 files are NOT in "
            f"upstream's git tree -- they are GitHub release assets, so a fresh "
            f"clone legitimately has none until you run "
            f"`python platform/mirror_site.py --media` (128 MB). The site will "
            f"build and every page will say it is a catalogue of motion with "
            f"nothing to play, which is the state this function exists to make "
            f"visible. platform/site/check_seo.py fails on it.")

    if not n_videos and not warnings:
        warnings.append("site/dist/media has no mp4; the motion wall will be blank")
    return {"posters": n_posters, "videos": n_videos}


def assert_wall(html: str, code: str, problems: list[str]) -> None:
    """The home page must still contain the motion wall.

    A check on the *output*, not on the patch that is supposed to produce it. The
    patch count was `required=0`, which makes "the wall's media paths were not
    rewritten" indistinguishable from "the wall is not there at all" -- and the
    second of those is what actually happened, invisibly, for the whole life of
    this site.

    Three independent ways to ship a home page with no motion, all of which
    passed every gate:
      1. the inline script deleted along with the L10N dictionary,
      2. the media path left one directory too shallow, so every fetch 404s,
      3. `site/dist/media/` absent entirely because a symlink failed.
    Each is invisible to a test that reads the DOM and looks for cards. So this
    reads the static file and looks for the thing itself.
    """
    if "createElement('video')" not in html and 'createElement("video")' not in html:
        problems.append(
            f"{code}/index.html: the motion wall is gone -- no createElement('video') "
            f"in the static file. Something removed or never emitted the inline script.")
    if "../media/" not in html:
        problems.append(
            f"{code}/index.html: no '../media/' path, so every poster and clip "
            f"request resolves to a 404. The path rewrite did not apply.")


def strip_inline_l10n(html: str) -> str:
    """Retire index.html's inline L10N dictionary and hand applyLanguage() over.

    The dictionary is replaced *in place*, and the enclosing `<script>` block is
    left alone. That is not a stylistic preference.

    The first version removed the whole block from the opening `<script>` to the
    matching `</script>`, reasoning that a dictionary cannot outlive its script.
    On index.html that was wrong: `const L10N` and the 16-clip motion wall share
    **one** script, so deleting the block deleted the wall as well. The build
    produced a home page with 16 empty tiles, no `<video>`, no `fetch`, and no
    error -- and every gate was green, because no gate had ever asserted that the
    page still contains the thing that makes it a home page.

    `L10N` has exactly one reader, `t()`, and `t()` has no call sites left once
    `applyLanguage()` is replaced below, so an empty object is inert rather than
    broken. Sibling scripts are now untouchable by construction.
    """
    m = re.search(r"const L10N = \{", html)
    if m:
        depth, i, quote = 0, m.end() - 1, None
        end_at = None
        while i < len(html):
            ch = html[i]
            if quote:
                if ch == "\\":
                    i += 2
                    continue
                if ch == quote:
                    quote = None
            elif ch in "'\"`":
                quote = ch
            elif ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    end_at = i
                    break
            i += 1
        if end_at is not None:
            html = html[:m.start()] + "const L10N = {};" + html[end_at + 1:]
        else:
            # An unbalanced brace means the dictionary was never parsed
            # correctly, and guessing where it ends would be a silent corruption.
            raise SystemExit(
                "index.html: `const L10N = {` has no matching `}`. Refusing to "
                "guess where it ends -- the previous behaviour deleted the "
                "enclosing <script>, which on this page also holds the motion wall.")

    # the state block still declares language + applyLanguage(); the runtime
    # owns them now
    html = re.sub(r"const state = \{[^}]*\};",
                "const state = { language: window.__I18N__.locale };", html, count=1)
    html = re.sub(r"[ \t]*const t = \(key\) =>[^\n]*\n", "", html, count=1)
    # the inline applyLanguage() body is replaced by the shared runtime's apply()
    html = re.sub(
        r"function applyLanguage\(\) \{.*?\n\}",
        "function applyLanguage() { window.__I18N__.apply(document); }",
        html, count=1, flags=re.S)
    html = html.replace("    applyLanguage();\n",
                        "    applyLanguage();\n    window.__I18N__.mountSwitcher();\n")
    return html


def inject_head(html: str, code: str, page: str, origin: str, locales: list[str]) -> str:
    block = head_block(code, page, origin, locales)
    if "</title>" in html:
        return html.replace("</title>", f"</title>\n{block}", 1)
    return block + "\n" + html


def inject_runtime(html: str, code: str) -> str:
    """Load the locale bundle and the shared runtime on every page.

    index.html carries its logic inline and so has no external <script> to
    anchor on; library/showcase do, but only after HTML_PATCHES has run. Doing
    it here means one rule for all three pages instead of one per template.
    The runtime must load BEFORE the page script, since that script reads
    window.__I18N__ at parse time.
    """
    tags = (f'<script src="../assets/i18n/{code}.js"></script>\n'
            f'    <script src="../assets/i18n.js"></script>')
    if "assets/i18n.js" in html:
        return html
    if "</body>" in html:
        return html.replace("</body>", f"  {tags}\n</body>", 1)
    return html + "\n" + tags


def inject_switcher(html: str) -> str:
    """Put the data-driven language switcher inside the existing top bar.

    The runtime fills [data-locale-switcher] from the locale list, so adding a
    locale never means editing HTML again. Anchored on the brand link, which
    every page has and which is the last topbar element before the nav.
    """
    nav = ('<nav class="locale-nav" data-locale-switcher aria-label="Language">'
           '<button class="locale-flag" type="button" aria-expanded="false" aria-haspopup="true">'
           '<span class="locale-flag-icon" aria-hidden="true">'
           '<svg viewBox="0 0 24 24" focusable="false"><circle cx="12" cy="12" r="9.2"/>'
           '<path d="M2.8 12h18.4M12 2.8c2.5 2.6 3.8 5.7 3.8 9.2S14.5 18.6 12 21.2'
           'c-2.5-2.6-3.8-5.7-3.8-9.2S9.5 5.4 12 2.8Z"/></svg></span>'
           '<span data-locale-current>en</span></button></nav>')
    if "data-locale-switcher" in html:
        return html
    # library/showcase: the upstream toggle button, whichever class it uses
    m = re.search(r'<button class="(?:language-toggle|topbar-toggle)"[^>]*id="languageToggle".*?</button>',
                  html, re.S)
    if m:
        return html[:m.end()] + nav + html[m.end():]
    m = re.search(r'(<nav class="topbar-nav".*?)(</nav>)', html, re.S)
    if m:
        return html[:m.end()] + nav + html[m.end():]
    m = re.search(r'(<header class="topbar".*?)(</header>)', html, re.S)
    if m:
        return html[:m.end()] + nav + html[m.end():]
    return html


def is_real(ns_name: str, key: str, value, en_value, code: str, src: str) -> bool:
    """Does this entry count as *translated*, not merely present?

    Present-but-inherited is the trap. A card title copied from `en` is the slug;
    a chrome key copied from `en` is byte-identical. Counting presence alone
    reported ru at 100% while every description was still English.

    The source locale is 100% by definition: for `en`, presence IS translated.
    """
    if code == src:
        return value is not None
    if ns_name in ("ui", "page", "showcase"):
        return value is not None and value != en_value
    if isinstance(value, dict):
        title = value.get("title")
        if title and title != key:
            return True
        return bool(value.get("description"))
    return bool(value)


def measure_coverage(code: str, ns: dict) -> dict:
    """Coverage against the en namespace sizes, split by namespace.

    `code == 'en'` is the source locale and is always 100% by definition.
    """
    en = load_locale("en")
    out = {}
    for ns_name, keys in en.items():
        if ns_name == "meta":
            continue
        total = len(keys)
        have = sum(1 for k, ev in keys.items()
                   if is_real(ns_name, k, ns.get(ns_name, {}).get(k), ev, code, "en"))
        out[ns_name] = {"total": total, "translated": have,
                        "pct": round(100.0 * have / total, 1) if total else 100.0}
    total = sum(v["total"] for v in out.values())
    have = sum(v["translated"] for v in out.values())
    return {"namespaces": out, "overall_pct": round(100.0 * have / total, 1) if total else 0.0}


def write_root_index(locales: list[str], origin: str) -> None:
    """Root: Accept-Language redirect, with a real no-JS list underneath."""
    opts = ",\n        ".join(
        f'{{code:"{c}",tag:"{META[c][0].split("-")[0]}",name:"{META[c][1]}"}}' for c in locales)
    links = "\n".join(
        f'      <li><a href="{c}/library.html" lang="{META[c][0]}" hreflang="{c}">{META[c][1]}</a></li>'
        for c in locales)
    (DIST / "index.html").write_text(f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>shotcraft — shot library</title>
<link rel="alternate" hreflang="x-default" href="{origin}/en/library.html">
{chr(10).join(f'<link rel="alternate" hreflang="{c}" href="{origin}/{c}/library.html">' for c in locales)}
<style>
  body {{ font: 16px/1.6 system-ui, sans-serif; background:#0e0e0c; color:#f0ede5;
         margin:0; min-height:100vh; display:grid; place-items:center; }}
  ul {{ list-style:none; padding:0; display:flex; gap:.6rem; flex-wrap:wrap; justify-content:center; }}
  a {{ color:#d3923c; }}
</style>
</head>
<body>
<main>
  <p>Redirecting to your language…</p>
  <noscript><p>Choose a language:</p></noscript>
  <ul>
{links}
  </ul>
</main>
<script>
(function () {{
  var locales = [
        {opts}
      ];
  var url = location.pathname + location.search + location.hash;
  var seg = url.split('/').filter(Boolean);
  if (seg.length && locales.some(function (l) {{ return l.code === seg[0]; }})) return;
  var chosen = null;
  try {{ chosen = localStorage.getItem('shotcraft-locale'); }} catch (e) {{}}
  if (chosen && locales.some(function (l) {{ return l.code === chosen; }})) {{
    location.replace('/' + chosen + '/library.html');
    return;
  }}
  var tags = (navigator.languages || [navigator.language || 'en']).map(function (t) {{
    return String(t).slice(0, 2).toLowerCase();
  }});
  for (var i = 0; i < tags.length; i += 1) {{
    var hit = locales.find(function (l) {{ return l.tag === tags[i]; }});
    if (hit) {{ location.replace('/' + hit.code + '/library.html'); return; }}
  }}
  location.replace('/en/library.html');
}})();
</script>
</body>
</html>
""", encoding="utf-8")


def write_sitemap(locales: list[str], origin: str) -> None:
    entries = []
    for page in ("index", "library", "showcase"):
        for c in locales:
            loc = f"{origin}/{c}/{page}.html"
            alts = "".join(
                f'<xhtml:link rel="alternate" hreflang="{o}" href="{origin}/{o}/{page}.html"/>'
                for o in locales)
            alts += f'<xhtml:link rel="alternate" hreflang="x-default" href="{origin}/en/{page}.html"/>'
            entries.append(f"  <url><loc>{loc}</loc>{alts}</url>")
    (DIST / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + "\n".join(entries) + "\n</urlset>\n", encoding="utf-8")
    shutil.copy2(GALLERY / "robots.txt", DIST / "robots.txt") if (GALLERY / "robots.txt").exists() else None


def serve(port: int) -> None:
    """Serve dist/ and stay up. Windows-friendly: ThreadingHTTPServer so a
    browser loading 60+ previews cannot starve the handler thread."""
    import functools
    import http.server
    import socketserver

    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(DIST))

    class T(socketserver.ThreadingTCPServer):
        allow_reuse_address = True
        daemon_threads = True

    with T(("127.0.0.1", port), handler) as httpd:
        print(f"serving {DIST} at http://localhost:{port}", flush=True)
        httpd.serve_forever()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--origin", default="https://shotcraft.example")
    ap.add_argument("--serve", type=int, default=0,
                    help="serve site/dist on this port")
    ap.add_argument("--rebuild", action="store_true",
                    help="rebuild even when --serve is given. Off by default: a "
                         "server that regenerates the tree it is serving will "
                         "silently undo the prerender, which is how the Russian "
                         "page came to serve the untranslated template during a "
                         "test run")
    a = ap.parse_args()

    serving_only = bool(a.serve) and not a.rebuild
    if serving_only and not DIST.exists():
        print("site/dist missing; run platform/site/build_site.py first",
              file=sys.stderr)
        return 2

    if serving_only:
        print(f"serving {DIST} on http://localhost:{a.serve} (not rebuilding)")
        serve(a.serve)
        return 0

    # Invalidate the prerender stamp BEFORE building. This build regenerates every
    # page from the template, so any static block prerender.py baked into it is
    # about to be overwritten. Deleting the stamp first means that a build run
    # after a prerender leaves the tree in a state a gate can detect, instead of
    # one where the Russian page has quietly reverted to the Chinese corpus.
    stamp = DIST / ".prerendered.json"
    if stamp.exists():
        stamp.unlink()
        print("note: cleared the prerender stamp; re-run platform/site/prerender.py "
              "or the static card block will be the untranslated template")

    res = build()
    # `problems` blocks the build; `warnings` does not. A missing media mirror is
    # a warning here and a hard failure in check_seo.py, which is the single gate
    # a release runs. Two authorities for one fact is how a gate stops being one.
    print(json.dumps({"locales": res["locales"],
                      "coverage": {k: v["overall_pct"] for k, v in res["coverage"].items()},
                      "media": res["media"],
                      "warnings": res["warnings"],
                      "problems": res["problems"]}, ensure_ascii=False, indent=2), flush=True)
    if res["problems"]:
        return 1
    if a.serve:
        serve(a.serve)
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())