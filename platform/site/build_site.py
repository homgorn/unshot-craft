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
from datetime import datetime, timezone
from pathlib import Path

import os
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _env import load as _load_env  # noqa: E402

_load_env()
DEFAULT_ORIGIN = "https://shotcraft.example"

# Upstream's repository, used for the "Star on GitHub" button, the showcase
# submission link and the star count. EMPTY by default, and the three sites
# that use it are then neutralised rather than repointed -- see
# `github_patches()`.
GITHUB_REPO = os.environ.get("SITE_GITHUB_REPO", "").strip()


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

# The last two statements of upstream's own `applyLanguage()`, verbatim, in both
# app.js and showcase.js. Used as the anchor for handing the rest of the
# attribute contract to the shared runtime -- see the two patches that use it.
ARIA_LOOP = (
    "  document.querySelectorAll('[data-i18n-aria-label]').forEach((node) => {\n"
    "    node.setAttribute('aria-label', text(node.dataset.i18nAriaLabel));\n"
    "  });")

APP_PATCHES: list[tuple[str, str, int, str]] = [
    ("const translations = window.GALLERY_I18N;",
     "const translations = window.__I18N__.legacy();\n"
     "// the switcher is generated from data, so a new locale needs no HTML edit\n"
     "window.__I18N__.mountSwitcher();", 1, "i18n source"),
    ("const libraryEndpoint = staticGallery ? './api/library.json' : '/api/library';",
     "const libraryEndpoint = staticGallery ? '../api/library.json' : '/api/library';", 1, "library path"),
    # The media URLs inside library.json are `./media/<name>.mp4?v=…` and they are
    # emitted into `data-src` **verbatim**. That resolves against the page, so on
    # `/ru/library.html` every clip was fetched from `/ru/media/…` and 404'd.
    #
    # The prerendered block had its paths rewritten, the runtime's did not -- which
    # is why the page played correctly at first paint and went blank a moment later
    # as app.js replaced it. Both halves came from the same payload and only one
    # was corrected.
    #
    # `required=2` because this exact miss is silent: the file is valid, the static
    # block is right, every gate passes, and the only evidence is a 404 line in a
    # dev server's log. Two sites emit the URL -- an `<img>` for a style with a
    # still and a `<video>` for the rest -- and patching one leaves a whole class
    # of clip 404ing, so the count is asserted rather than accepted.
    ('${escapeHtml(style.media.url)}',
     '${escapeHtml(mediaUrl(style.media.url))}', 2, "media url depth"),
    ("const libraryEndpoint = staticGallery ? '../api/library.json' : '/api/library';",
     "const libraryEndpoint = staticGallery ? '../api/library.json' : '/api/library';\n"
     "  // `library.json` states media paths relative to the site root. A page lives\n"
     "  // one directory down, so the prefix has to be added here rather than by\n"
     "  // rewriting the payload -- the payload is the index, and ADR 0002 says the\n"
     "  // database is the source of truth for it.\n"
     "  const mediaUrl = (u) => (u || '').replace(/^\\.\\/media\\//, '../media/');",
     1, "mediaUrl helper"),
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

  // Place the target once and then keep placing it until it stops moving.
  //
  // One `scrollIntoView` was enough to be wrong: it runs in a microtask after
  // `loadLibrary()` resolves, but the grid is still settling at that point --
  // the skeleton tiles are replaced by real ones and the row heights change
  // afterwards. So the offset was computed against a layout that no longer
  // existed, and the card landed 277px or 513px from where it belonged. The
  // browser suite caught this as an intermittent failure of its own assertion,
  // which is the only reason it was ever seen at all.
  //
  // Also offset for the topbar. It is `position: sticky` and 66px tall, so
  // `block: 'start'` puts the target's top edge *underneath* it -- the heading
  // of the card you asked to see is hidden by the bar you scrolled past.
  const place = () => {
    const el = document.getElementById(id);
    if (!el) return null;
    const bar = document.querySelector('.topbar');
    const gap = bar ? Math.round(bar.getBoundingClientRect().height) + 12 : 12;
    const top = Math.max(0, Math.round(
      el.getBoundingClientRect().top + window.scrollY - gap));
    window.scrollTo({top: top, behavior: 'auto'});
    return top;
  };

  let last = null;
  let frames = 0;
  const settle = () => {
    // If the reader has scrolled since we last placed it, they have taken over.
    // Yanking the page back mid-read is worse than landing 200px out.
    if (last !== null && Math.abs(window.scrollY - last) > 8) return;
    const now = place();
    frames += 1;
    if (now !== null && now === last) return;      // the offset held: done
    last = now;
    if (frames < 30) requestAnimationFrame(settle);  // ~500ms at 60fps
  };
  settle();
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
    # Hand every translation attribute to the one runtime, on this page too.
    #
    # index.html gets this for free: `strip_inline_l10n` replaces its inline
    # `applyLanguage()` with `window.__I18N__.apply(document)`. library.html and
    # showcase.html keep upstream's own `applyLanguage()`, which handles
    # `data-i18n` and `data-i18n-aria-label` and nothing else -- so
    # `data-i18n-placeholder`, `data-i18n-title` and `data-l10n` are inert there,
    # and both loops resolve against `ui` whatever `data-ns` says.
    #
    # That last part is why the search box used to work by accident rather than
    # by design: upstream hardcodes `elements.searchInput.placeholder =
    # text('searchPlaceholder')`, so the Russian placeholder appeared on /ru/
    # while the `data-i18n-placeholder` that `check_seo.py` asserts was never read
    # on that page at all. A gate that passes on an attribute nothing consumes is
    # not evidence the attribute works.
    #
    # `apply()` is idempotent and re-applies `data-i18n` with `data-ns` honoured,
    # so calling it after upstream's loops is additive rather than conflicting.
    # No fallback namespace: upstream's `text()` on this page is `s('ui', key)`,
    # which is also the runtime's default.
    (ARIA_LOOP, ARIA_LOOP + "\n  window.__I18N__.apply(document);",
     1, "library honours every attribute kind"),
]

SHOWCASE_PATCHES: list[tuple[str, str, int, str]] = [
    ("const SHOWCASE_L10N = {", "const SHOWCASE_L10N_UNUSED = {", 1, "neutralize inline dict"),
    # Dead data: the table above is renamed out of use and the runtime replaces
    # every read of it, yet it still ships unreachable Chinese containing the
    # upstream name. Emptied rather than deleted, because these two literals are
    # the only unambiguous way to reach inside a table we no longer execute.
    ("'社区作品展示 | video-shotcraft'", "''", 1, "dead showcase title"),
    ("'社区用 video-shotcraft 做出的产品视频", "'", 1, "dead showcase intro"),
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
    # The manifest was fetched as `./api/showcase.json`, which resolves against
    # the page. From `/en/showcase.html` that is `/en/api/showcase.json`, and
    # `site/dist/api/` holds exactly one file: `library.json`. So all three
    # showcase pages fell into their own load-error branch and rendered nothing,
    # while every gate passed -- `check_seo.py` never fetches it.
    #
    # `required=1`, so a change in the upstream path becomes a build failure
    # rather than a silently empty page.
    ("fetch('./api/showcase.json'", "fetch('../api/showcase.json'",
     1, "showcase manifest path"),
    # Same reason as the library patch above: upstream's `applyLanguage()` here
    # handles two of the five attribute kinds and ignores `data-ns`. The showcase
    # page is the one that uses `showcase.*` keys, so an annotation the page
    # resolves against the `ui` namespace renders the wrong string.
    #
    # `fallbackNs` is 'showcase' and not left at the default 'ui': upstream's own
    # `text()` on this page is `s('showcase', key)`, so a bare `data-i18n=
    # "navLibrary"` in the shipped template means `showcase.navLibrary`. Calling
    # apply() with the default instead replaced "Библиотека кадров" with the
    # literal word `navLibrary` on /ru/showcase.html.
    (ARIA_LOOP,
     ARIA_LOOP + "\n  window.__I18N__.apply(document, 'showcase');",
     1, "showcase honours every attribute kind"),
]

# `expected` is 0 for anchors that legitimately vary per page: the builder only
# complains when an anchor that must exist is missing.
LOCALE_CSS = """
  /* A GitHub affordance that has nowhere to point, because SITE_GITHUB_REPO is
     unset. Hidden rather than left as a dead anchor: a button that does nothing
     reads as a bug, and on this project it would also be pointing a stranger's
     repository at anyone who pressed it. Set SITE_GITHUB_REPO in .env and the
     class never appears. */
  .is-unavailable, .repo-absent { display: none; }

  /* Data-driven language switcher (site/build/runtime/i18n.js) */
  /* Inline flag: always visible, no hover needed, so a Russian or Japanese
     visitor who cannot decode Latin script can still find their language.

     Colours come from the token system, like every other topbar control
     (`.topbar-link`, `.topbar-toggle`). The first version of this block set
     `background: rgba(14,14,12,.35)` and `color: var(--muted)` -- a hardcoded
     *dark* pill, which measured 2.03:1 in the light theme: the text colour was
     the light theme's muted grey, sitting on a dark scrim the light theme never
     asked for. Two defects in one declaration. A hardcoded colour cannot follow
     a theme, and pairing it with a themed colour is how it slipped through a
     palette where every token had been given a comment stating which ratios it
     clears.

     The switcher is not a special case that needs its own surface, so it does not
     get one. */
  .locale-nav { position: relative; }
  .locale-flag {
    display: inline-flex; align-items: center; justify-content: center;
    border: 1px solid var(--line); border-radius: 999px;
    padding: .38rem .95rem; background: var(--surface); color: var(--text);
    box-shadow: 0 2px 8px var(--control-shadow);
    font: inherit; font-size: .8rem; cursor: pointer;
    white-space: nowrap; list-style: none;
    transition: background 150ms ease, color 150ms ease, border-color 150ms ease;
  }
  .locale-flag:hover { background: var(--control-hover); border-color: var(--faint); }
  .locale-flag:active { background: var(--control-active); }
  .locale-flag:focus-visible { border-color: var(--accent); color: var(--accent-text); }
  .locale-flag-icon { display: inline-flex; align-items: center; margin-right: .4rem; }
  .locale-flag-icon svg { width: 15px; height: 15px; fill: none; stroke: currentColor;
                          stroke-width: 1.6; stroke-linecap: round; stroke-linejoin: round; }
  .locale-list {
    position: absolute; right: 0; top: calc(100% + 8px); z-index: 20;
    display: flex; flex-direction: column; min-width: 168px; padding: 6px;
    background: var(--surface); border: 1px solid var(--line);
    border-radius: 12px; box-shadow: var(--shadow);
    opacity: 0; visibility: hidden; transform: translateY(-4px);
    transition: opacity 150ms ease, transform 150ms ease, visibility 150ms;
  }
  .locale-nav:hover .locale-list, .locale-nav:focus-within .locale-list,
  .locale-nav.is-open .locale-list {
    opacity: 1; visibility: visible; transform: translateY(0);
  }
  .locale-item {
    display: block; padding: 8px 12px; border-radius: 8px;
    color: var(--text); font-size: .86rem; text-decoration: none;
  }
  .locale-item:hover { background: var(--control-hover); }
  .locale-item.is-current { color: var(--accent-text); font-weight: 700; }
  /* the upstream inline toggle is superseded by the switcher above */
  .language-toggle[hidden] { display: none; }
"""

def indented_non_header(raw: str) -> list[str]:
    """Lines in a Cloudflare `_headers` file that are indented but are not headers.

    The format has two kinds of line and the distinction is positional:

    * a **path pattern**, which must begin at column 0, because that is what
      starts a rule;
    * a **header**, `Name: value`, which is indented two spaces under the pattern
      it belongs to.

    So "indented" is not the defect -- 14 of this file's 22 lines are correctly
    indented headers, and a check that flags any indented line is a check that
    cannot be satisfied. The defect is an indented line that is *not* a header,
    because it then reads as a pattern and matches nothing.

    ` /media/*` was exactly that: one leading space, in the file whose rule
    governs 128 MB of video, and it shipped without error.

    Shared with `check_dist.py`, which imports it rather than restating the
    format, so the builder and the gate cannot disagree about what valid is.
    """
    bad: list[str] = []
    # `[A-Za-z0-9-]+:` then end-of-line-or-space. An empty value is legal -- it is
    # how the format removes a header -- so requiring a value after the colon
    # flagged `  Referrer-Policy:` as a pattern.
    header = re.compile(r"^\s+[A-Za-z0-9-]+:(?:\s|$)")
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if not line[0].isspace():
            continue                     # column 0: a pattern, as intended
        if not header.match(line):
            bad.append(line.rstrip())
    return bad


def github_patches() -> tuple[list, list]:
    """Point the GitHub affordances at *our* repository, or remove them.

    An independent fork that ships upstream's repository URL is making two false
    statements at once: that we are that project, and that the project lives at
    that address. Worse, the showcase's "Submit your video" filed a GitHub issue
    on a stranger's tracker, so a third party's community submissions landed in
    someone else's backlog.

    Neither can be fixed by guessing a URL, so `SITE_GITHUB_REPO` decides:

    * **set** -- every occurrence is repointed at that repository and the star
      count is fetched from it.
    * **unset** -- the star count fetch is removed, the two links are dropped and
      the count element is hidden. A page with no button is honest; a page with a
      button pointing at someone else's repo is not.

    The empty case is the default because this repository has no public address
    yet, and a placeholder URL would be indistinguishable from a real one in the
    built output.
    """
    if GITHUB_REPO:
        tag = GITHUB_REPO.replace("/", "-")
        # Both lists, because `apply_patches` asserts every entry matched and a
        # list handed to both app.js and the HTML pages fails on the entries that
        # belong to only one of them. The assertion is the point: relaxing a
        # `required` to make a list fit would restore the silent miss that let a
        # broken path ship in the first place.
        html = [('aria-label="video-shotcraft home"',
                 'aria-label="shotcraft home"', 0, "brand aria-label")]
        js = [
            ("https://github.com/Vincentwei1021/video-shotcraft",
             f"https://github.com/{GITHUB_REPO}", 0, "github repo link"),
            ("https://api.github.com/repos/Vincentwei1021/video-shotcraft",
             f"https://api.github.com/repos/{GITHUB_REPO}", 1, "star count api"),
            ("const CACHE_KEY = 'video-shotcraft-stars';",
             f"const CACHE_KEY = 'shotcraft-stars-{tag}';", 1, "star cache key"),
        ]
        html += [
            ("https://github.com/Vincentwei1021/video-shotcraft",
             f"https://github.com/{GITHUB_REPO}", 0, "github repo link"),
        ]
        js = []
        return html, js
    return _repo_empty_html() + _repo_star_html(), _repo_empty_js()


def _repo_empty_html():
    """Everything here is page-specific, so every entry is `required=0`.

    `apply_patches` asserts each entry matched on **every** file it is handed, and
    one list is handed to index, library and showcase alike. The hero button and
    the star count exist only on index; the submission link only on showcase.
    Relaxing `required` here is safe only because the guarantee moved to the
    written output: `build()` re-reads index.html and fails if any upstream
    repository reference survived. A patch with `required=0` and no output
    assertion is exactly how the media-path defect shipped.
    """
    return [
        # The submission link goes first: it is the one that writes into someone
        # else's tracker.
        ('<a href="https://github.com/Vincentwei1021/video-shotcraft" target="_blank"'
         ' rel="noreferrer">github.com/Vincentwei1021/video-shotcraft</a>',
         '<span class="repo-absent">no public repository yet</span>', 0,
         "showcase submission link"),
        # The hero button. Distinct from the footer link only by its class, so
        # the class is the anchor -- and rather than leave a dead anchor it is
        # marked, and hidden by `.is-unavailable` in LOCALE_CSS. A visible button
        # that goes nowhere is worse than no button.
        ('<a class="button-github" href="https://github.com/Vincentwei1021/video-shotcraft"',
         '<a class="button-github is-unavailable" aria-disabled="true" href="#"',
         0, "hero github button"),
        # The brand link's static aria-label. `data-i18n-aria-label="brandHome"`
        # replaces it at runtime, but the file on disk said the upstream name, and
        # that is what a crawler, a scraper and a screen reader with JS off read.
        ('aria-label="video-shotcraft home"',
         'aria-label="shotcraft home"', 0, "brand aria-label"),
        ('aria-label="Star video-shotcraft on GitHub"',
         'aria-label="Star shotcraft on GitHub"', 0, "star badge aria-label"),
        # The library page's star button. A different element from the hero's --
        # `social-badge`, not `button-github` -- which is why the first pass left
        # 21 of 42 occurrences alive.
        ('<a class="social-badge" data-platform="github"'
         ' href="https://github.com/Vincentwei1021/video-shotcraft"',
         '<a class="social-badge is-unavailable" aria-disabled="true" data-platform="github"'
         ' href="#"',
         0, "library star badge"),
        # The showcase submission button. `data-i18n` rewrites its label at
        # runtime, but the *href* is not a translated string and it was filing
        # third-party submissions into a stranger's issue tracker.
        ('<a class="showcase-submit"'
         ' href="https://github.com/Vincentwei1021/video-shotcraft/issues/new?template=showcase.yml"',
         '<a class="showcase-submit is-unavailable" aria-disabled="true" href="#"',
         0, "showcase submit button"),
        # The two static intro paragraphs. Both carry `data-i18n`, so a reader
        # with JavaScript sees our text -- but a crawler, a scraper and a reader
        # whose script fails all see the file's, and the file said the upstream
        # project's name in a sentence about what *this* site is. The locale
        # values are the truth; these are the fallback that has to agree.
        ('data-i18n="intro">video-shotcraft is an AI agent skill',
         'data-i18n="intro">shotcraft is an AI agent skill', 0, "intro (library)"),
        ('data-i18n="intro">Product videos the community made with video-shotcraft.',
         'data-i18n="intro">Product videos the community made with shotcraft.',
         0, "intro (showcase)"),
    ]


def _repo_empty_js():
    """Empty by design: nothing in app.js mentions the repository."""
    return []


def _repo_star_html():
    """The two star-count patches. These live in index.html's inline script.

    The fetch is upstream's star count for upstream's repository. Showing it on
    an independently branded fork claims an endorsement that does not exist, so
    with no repository configured it is pointed at nothing rather than at them.
    """
    return [
        ("""fetch('https://api.github.com/repos/Vincentwei1021/video-shotcraft')""",
         "fetch('')  // no repository configured; see SITE_GITHUB_REPO in .env\n"
         "      // The star count is upstream's number, not ours, and showing it\n"
         "      // on an independently branded fork implies an endorsement that does\n"
         "      // not exist.", 0, "star count fetch"),
        ("const CACHE_KEY = 'video-shotcraft-stars';",
         "const CACHE_KEY = 'shotcraft-stars-unconfigured';", 0,
         "star cache key"),
    ]


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


GITHUB_HTML, GITHUB_JS = github_patches()


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
    # ---- card sources, and the 471 links that point at them ------------------
    #
    # `library.json` says `"sourceUrl": "./source/<slug>.md"`, and `app.js`
    # renders it into an `href` verbatim -- so every card on every locale linked
    # to `/<locale>/source/<slug>.md`, a directory nothing ever created. 471 dead
    # links, invisible to a static crawl because they only exist in the DOM after
    # `app.js` has run, which is where every other check was looking.
    #
    # The files are real: `upstream/video-shotcraft/references/shots/` holds all
    # 157 of them, 575 KB, laid out as `<category>/<slug>.md`. So the fix is to
    # ship them, not to remove the link -- a card whose "Recipe" button goes
    # somewhere is strictly worse than one that opens the shot reference it was
    # written from, and those references are Apache-2.0 like everything else here.
    #
    # `sourceUrl` is rewritten to the real relative path rather than flattening
    # the tree, so the directory a reader lands in matches the category the card
    # belongs to.
    shots = ROOT / "upstream" / "video-shotcraft" / "references" / "shots"
    lib_src = GALLERY / "api" / "library.json"
    lib_dst = DIST / "api" / "library.json"
    if shots.is_dir() and lib_src.exists():
        shutil.copytree(shots, DIST / "source", dirs_exist_ok=True)
        payload = json.loads(lib_src.read_text(encoding="utf-8"))
        rewritten = 0
        for card in payload.get("cards", []):
            src = card.get("source") or ""
            prefix = "references/shots/"
            if src.startswith(prefix):
                # `../`, not `./`. The link is rendered by `app.js` into a page at
                # `/<locale>/library.html`, so `./source/x.md` resolves to
                # `/<locale>/source/x.md` and 404s; the tree lives at the site
                # root. One segment of depth, and the whole 471-link fix is dead
                # again -- which is why `check_dist.py` resolves this value out of
                # the payload rather than trusting the string.
                card["sourceUrl"] = "../source/" + src[len(prefix):]
                rewritten += 1
        lib_dst.write_text(json.dumps(payload, ensure_ascii=False, indent=None)
                           + "\n", encoding="utf-8")
        if rewritten != len(payload.get("cards", [])):
            problems.append(
                f"rewrote {rewritten} sourceUrl values for "
                f"{len(payload.get('cards', []))} cards; some had no "
                f"'references/shots/' source, so their Recipe link stays dead")
    else:
        problems.append(
            f"no shot sources at {shots}; every card's Recipe link would 404")
    # The showcase manifest is published by a release workflow on upstream's
    # repository and is not in the git clone, so `site/dist/api/showcase.json`
    # did not exist -- and `showcase.js` fell into its own load-error branch on
    # all three showcase pages. An error is the wrong thing to show for "nothing
    # has been submitted yet": the page has an empty state, written and styled,
    # and it is what the reader should see.
    #
    # So the manifest is emitted, empty, with a `state` the page can distinguish.
    # `submissions` being empty is the truth; a missing file is an accident.
    manifest = DIST / "api" / "showcase.json"
    if not manifest.exists():
        manifest.write_text(json.dumps({
            "version": 1,
            "generated": datetime.now(timezone.utc).date().isoformat(),
            "source": "built; upstream publishes real submissions per release",
            "state": "empty",
            "submissions": [],
        }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    shutil.copy2(RUNTIME / "i18n.js", DIST / "assets" / "i18n.js")
    # ---- patched CSS --------------------------------------------------------
    # The switcher is generated, so its CSS ships with the generated CSS rather
    # than being patched into a third hand-maintained copy of styles.css.
    #
    # Wrapped in sentinels so `check_dist.py` can tell this block from upstream's
    # 1800 lines and audit only the part we own. Boundary-detection by guessing
    # which rule came last is how a gate ends up auditing the wrong 40 lines and
    # reporting green.
    CSS_BEGIN = "/* >>> generated by platform/site/build_site.py -- do not edit */"
    CSS_END = "/* <<< end generated */"
    css_path = DIST / "assets" / "styles.css"
    css = css_path.read_text(encoding="utf-8") if css_path.exists() else ""
    if css:
        # Idempotent: a rebuild re-appends only when the sentinels are absent, so
        # running the builder twice cannot double the block.
        if CSS_BEGIN not in css:
            css_path.write_text(
                css + "\n" + CSS_BEGIN + "\n" + LOCALE_CSS.strip()
                + "\n" + CSS_END + "\n", encoding="utf-8")

    # ---- _headers ----------------------------------------------------------
    # Cloudflare Pages reads `_headers` from the directory it is told to publish,
    # so a file at the repository root governs nothing. The tree is `rmtree`'d and
    # rebuilt on every run, so the deploy directory is the only place a header file
    # can live -- and it was not being copied, which meant the site shipped with
    # whatever the host's defaults are: no CSP, no `nosniff`, no `immutable` on
    # 128 MB of video.
    #
    # Copied rather than generated, because the file is hand-authored and
    # Cloudflare-specific, and generating it would mean restating its syntax in
    # Python. Validated on the way through, because the one way this can be wrong
    # in a way nobody notices is a rule that parses but does not match: see the
    # column-0 check.
    headers_src = ROOT / "_headers"
    if headers_src.is_file():
        raw = headers_src.read_text(encoding="utf-8")
        stray = indented_non_header(raw)
        if stray:
            problems.append(
                f"_headers: {len(stray)} line(s) are indented but are not "
                f"`Name: value` headers, so they read as path patterns and match "
                f"nothing: {stray[0]!r}")
        (DIST / "_headers").write_text(raw, encoding="utf-8")
    else:
        problems.append(
            "no _headers at the repository root; the deploy directory will ship "
            "without CSP, nosniff or media cache headers")

    media_report = deploy_media(problems, warnings)

    # ---- patched JS --------------------------------------------------------
    app = apply_patches((GALLERY / "app.js").read_text(encoding="utf-8"),
                        APP_PATCHES + GITHUB_JS, "en", problems, "app.js")
    (DIST / "assets" / "app.js").write_text(app, encoding="utf-8")
    sc = apply_patches((GALLERY / "showcase.js").read_text(encoding="utf-8"),
                       SHOWCASE_PATCHES, "en", problems, "showcase.js")
    (DIST / "assets" / "showcase.js").write_text(sc, encoding="utf-8")

    # ---- per-locale data + pages ------------------------------------------
    # SITE_ORIGIN, then --origin, then the placeholder. The order matters:
    # a flag on the command line must beat a file, and a file must beat a
    # hardcoded default that nobody remembers to change.
    origin = os.environ.get("SITE_ORIGIN", DEFAULT_ORIGIN)
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
            html = apply_patches(html, HTML_PATCHES + GITHUB_HTML, code, page_problems,
                               f"{page}.html", origin)
            html = inject_runtime(html, code)
            html = inject_head(html, code, page, origin, locales)
            html = inject_switcher(html)
            d = DIST / code
            d.mkdir(parents=True, exist_ok=True)
            if page == "index":
                assert_wall(html, code, page_problems)
                # No page may still *link* upstream's repository. The patches
                # above are optional per page, so their success is proven here
                # rather than assumed: index carries the star fetch, the hero
                # button and the cache key, and any of the three surviving means
                # the page still claims to be that project and points a reader
                # at someone else's tracker.
                #
                # Scoped to what *this* step controls. The same name also appears
                # in upstream's JSON-LD, which `seo.py` strips in a later pass --
                # asserting it here failed the build on all three locales for a
                # defect two steps downstream was about to fix.
                # `platform/site/check_dist.py` is the net for the whole tree.
                for upstream_leftover in ('href="https://github.com/Vincentwei1021/video-shotcraft"',
                                          "api.github.com/repos/Vincentwei1021",
                                          "video-shotcraft-stars"):
                    if upstream_leftover in html:
                        page_problems.append(
                            f"{code}/index.html: still references "
                            f"{upstream_leftover!r} -- SITE_GITHUB_REPO handling "
                            f"did not apply; the page links upstream's repository")
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
    ap.add_argument("--origin", default=os.environ.get("SITE_ORIGIN", DEFAULT_ORIGIN))
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