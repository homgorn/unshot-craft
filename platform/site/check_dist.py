"""Structural audit of `site/dist` as written to disk.

    python platform/site/check_dist.py
    python platform/site/check_dist.py --json

Why this exists separately from `check_seo.py`
----------------------------------------------
`check_seo.py` asks whether the metadata is *present and correct*. This asks
whether the file is a *valid document whose references resolve* -- questions a
metadata checker cannot ask, because they are not about metadata.

Every finding below shipped with 369 passing assertions:

* `404.html` was three complete HTML documents concatenated into one file. A
  doctype after `</html>` is a parse error the tree builder ignores, so a
  browser rendered the English 404 and then appended the Chinese and Russian
  bodies into the same document.
* Two `og:site_name` values on every chrome page -- upstream's 380 lines before
  ours, and a scraper takes the first. `re.search` cannot see a second match, so
  the check that asserted ours was present was satisfied by ours while the one a
  reader would see was upstream's.
* A bare `>` text node inside `<head>` on all nine pages, from a tag whose
  opening had been stripped by an earlier pass and whose closing survived.
* `showcase.js` fetched `./api/showcase.json`, which from `/en/showcase.html` is
  `/en/api/showcase.json`, and `site/dist/api/` held exactly one file. All three
  showcase pages rendered their load-error branch.
* 471 `href="/<locale>/source/<slug>.md"` links, emitted by `app.js` at runtime,
  to a directory that does not exist.

The last one is the shape of the whole problem: **it is only in the DOM after
JavaScript has run**, and every gate that read the static file was looking at
markup that had not yet produced it. So the checks below resolve URLs out of the
runtime's own templates as well as out of the static HTML.

What is asserted
----------------
1. exactly one `<!doctype html>` and one `</html>` per file
2. no text node inside `<head>` that is not whitespace
3. every `og:*`, `twitter:*`, `name=`, `property=` meta key appears at most once
4. no page carries upstream's project name (`video-shotcraft`), which ADR-0005
   makes a defect rather than an attribution
5. every `href` / `src` / `poster` / `contentUrl` / `thumbnailUrl` / `manifest` /
   `start_url` / icon `src` resolves on disk, relative to its own directory
6. every URL template in `app.js` and `showcase.js` resolves, so the runtime
   cannot 404 what the static file never mentioned
7. every URL **in the JSON payload** resolves from the directory of the page that
   renders it, because `app.js` turns those strings into `href` values verbatim
8. every `html[lang="..."]` selector names a language the build actually emits,
   so language-dependent CSS is not silently dead
9. `<video>` poster coverage, because a posterless looping tile is a black
   rectangle for as long as it takes to decode
10. the origin is not the `.example` placeholder, unless explicitly allowed
11. every custom property the *generated* CSS uses is defined in **both** themes
12. that CSS clears 4.5:1 in both themes, measured rather than asserted
13. the deploy directory carries `_headers`, and its path patterns start at
    column 0

A note on 7 and 8, because both are the same lesson. 471 `sourceUrl` links
dangled through a full rebuild with the files present and the string looking
correct, because `./x` is relative to the *page*, not to the payload. And six
`html[lang="zh-CN"]` rules governing CJK letter-spacing sat on the Chinese home
page while `<html lang>` said `zh-Hans` -- so they never applied, and nothing
reported it. Both are invisible to a check that reads the static HTML, because
both only exist once the file is interpreted.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIST = ROOT / "site" / "dist"
LOCALES_DIR = ROOT / "site" / "locales"

sys.path.insert(0, str(ROOT / "platform"))
from _env import load as _load_env  # noqa: E402

sys.path.insert(0, str(ROOT / "platform" / "site"))
# `indented_non_header` knows the Cloudflare `_headers` format. Imported rather than
# restated, so the builder and this gate cannot disagree about what valid is -- the
# first version of this check flagged all 14 correctly-indented header lines, which
# is how a gate becomes one nobody runs.
from build_site import indented_non_header  # noqa: E402

_load_env()
DEFAULT_ORIGIN = "https://shotcraft.example"

LOCALES = ("en", "zh", "ru")
PAGES = ("index", "library", "showcase")

# Upstream's *project* name. `check_seo.py` already blocks the author's domain;
# this blocks the name, which is what actually reaches a reader and a social card.
UPSTREAM_NAME = "video-shotcraft"

# URL templates in the runtime scripts: `'./x'` and `"../x"` inside fetch() and
# template literals. Quoted, so a path inside prose is not mistaken for one.
URL_LITERAL = re.compile(r"""['"]((?:\.\.?/)[^'"`\s]{2,120})['"]""")

# Meta keys that are *legitimately* repeatable, per the OpenGraph protocol, and
# which the "no duplicated meta keys" check must therefore not flag.
#
# `og:locale:alternate` is one tag per other locale: a card page has two, with
# two different values. A page with two of them is a correct hreflang cluster, not
# a bug -- the first version of this check flagged 480 of 471 card pages for it,
# which is the failure mode of a gate nobody can satisfy. A gate that is wrong
# gets deleted, and then the real duplicates it was meant to catch go with it.
REPEATABLE = {
    "og:locale:alternate",
    "og:image",
    "og:image:secure_url",
    "og:video",
    "og:video:secure_url",
    "article:tag",
}


def built() -> list[str]:
    return [c for c in LOCALES if (DIST / c / "library.html").exists()]


def head_of(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="replace").split("</head>", 1)[0]


def resolves(target: str, base: Path) -> bool:
    """Does `target`, resolved against the page's own directory, exist?"""
    clean = target.split("?")[0].split("#")[0].strip()
    if not clean:
        return True                      # "#anchor" and "?" alone
    if clean.startswith(("http://", "https://", "mailto:", "tel:", "data:")):
        return True                      # checked separately if it is ours
    if clean.startswith("/"):
        return (DIST / clean.lstrip("/")).exists()
    if clean.startswith("{{") or "{{" in clean or "${" in clean:
        return True                      # a template literal, resolved per item
    return (base / clean).exists()


CSS_BEGIN = "/* >>> generated by platform/site/build_site.py -- do not edit */"
CSS_END = "/* <<< end generated */"

# WCAG 2.1 minimum for normal text. `styles.css` states in its own comments that
# every token clears 4.5:1 on its surfaces; this is the check that would notice if
# one stopped doing so.
MIN_CONTRAST = 4.5


def _rgb(token: str) -> tuple[int, int, int, float] | None:
    """Parse one colour literal into (r, g, b, alpha). None if not a colour."""
    t = token.strip().rstrip(";").strip()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", t, re.I)
    if m:
        h = m.group(1)
        if len(h) == 3:
            r, g, b = (int(c * 2, 16) for c in h)
            return r, g, b, 1.0
        if len(h) == 4:
            r, g, b, a = (int(c * 2, 16) for c in h)
            return r, g, b, a / 255
        if len(h) == 6:
            return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), 1.0
        if len(h) == 8:
            return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16),
                    int(h[6:8], 16) / 255)
        return None
    m = re.fullmatch(r"rgba?\(([^)]+)\)", t, re.I)
    if m:
        parts = [p.strip() for p in re.split(r"[,\s/]+", m.group(1)) if p.strip()]
        if len(parts) not in (3, 4):
            return None
        try:
            nums = [int(round(float(p.rstrip("%")))) for p in parts[:3]]
            a = float(parts[3]) if len(parts) == 4 else 1.0
        except ValueError:
            return None
        if all(p.endswith("%") for p in parts[:3]):
            nums = [int(round(float(p.rstrip("%")) * 255 / 100)) for p in parts[:3]]
        return nums[0], nums[1], nums[2], a
    return None


def _resolve(value: str, theme: dict[str, str], depth: int = 0) -> tuple[int, int, int, float] | None:
    """Resolve a CSS colour value against one theme's custom properties."""
    if depth > 8:
        return None
    v = value.strip()
    m = re.fullmatch(r"var\(\s*(--[\w-]+)\s*(?:,\s*(.+))?\s*\)", v, re.S)
    if m:
        name, fallback = m.group(1), m.group(2)
        if name in theme:
            return _resolve(theme[name], theme, depth + 1)
        return _resolve(fallback, theme, depth + 1) if fallback else None
    return _rgb(v)


def _luminance(c: tuple[int, int, int, float]) -> float:
    def ch(x: int) -> float:
        x = x / 255
        return x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4
    r, g, b, _ = c
    return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)


def _contrast(fg: tuple[int, int, int, float], bg: tuple[int, int, int, float]) -> float:
    a, b = _luminance(fg), _luminance(bg)
    hi, lo = max(a, b), min(a, b)
    return (hi + 0.05) / (lo + 0.05)


def _flatten(c: tuple[int, int, int, float], over: tuple[int, int, int, float]) -> tuple[int, int, int, float]:
    if c[3] >= 1.0:
        return c
    a = c[3]
    return (round(c[0] * a + over[0] * (1 - a)),
            round(c[1] * a + over[1] * (1 - a)),
            round(c[2] * a + over[2] * (1 - a)), 1.0)


def _theme_tokens(css: str, selector: str) -> dict[str, str]:
    m = re.search(re.escape(selector) + r"\s*\{(.*?)\}", css, re.S)
    if not m:
        return {}
    return {k: v.strip() for k, v in
            re.findall(r"(--[\w-]+)\s*:\s*([^;]+)", m.group(1))}


def audit(origin: str, allow_placeholder: bool) -> dict:
    lines: list[str] = []
    fails: list[str] = []
    total = 0

    def ck(ok: bool, name: str, detail: object = "") -> None:
        """One assertion.

        `detail` may be a callable, and should be when computing it would be
        wasted work or would index into a list that is empty on the passing path.
        The first version of the `_headers` check wrote `stray[0]` inline, so the
        gate crashed on the *successful* tree with `IndexError` -- a check that
        fails when the site is correct and passes when it is broken, inverted by
        the accident. Lazy detail makes that shape impossible to write.
        """
        nonlocal total
        total += 1
        if ok:
            lines.append(f"  ok   {name}")
        else:
            text = detail() if callable(detail) else detail
            lines.append(f"  FAIL {name}  -- {text}")
            fails.append(f"{name}: {text}")

    locales = built()
    if not locales:
        return {"lines": ["  site/dist has no built locales; run build_site.py"],
                "passed": 0, "total": 0, "failures": ["no built locales"]}

    # ---- 8. the origin must be real before a deploy ------------------------
    ck(not origin.endswith(".example") or allow_placeholder,
       f"origin is not the placeholder ({origin})",
       "every canonical, og:url, sitemap entry and JSON-LD url names this host. "
       "Set SITE_ORIGIN in .env, or pass --allow-placeholder-origin to build a "
       "non-deployable tree deliberately")

    docs = sorted(p for p in DIST.rglob("*.html"))
    ck(bool(docs), "site/dist has HTML to audit", "none found")

    bad_shape, bad_head, dup_meta, brand, dangling = [], [], [], [], []
    lang_selectors: set[str] = set()
    declared_langs: set[str] = set()
    videos_total = videos_with_poster = 0

    for p in docs:
        rel = p.relative_to(DIST).as_posix()
        html = p.read_text(encoding="utf-8", errors="replace")
        head = head_of(p)
        base = p.parent

        if html.count("<!doctype html>") != 1 or html.count("</html>") != 1:
            bad_shape.append(f"{rel}: {html.count('<!doctype html>')} doctype(s), "
                             f"{html.count('</html>')} </html>")

        # A line that is only `>` is a text node: a tag opened on one line and
        # closed on the next, with the opening removed by an earlier pass.
        for m in re.finditer(r"^[ \t]*>[ \t]*$", head, re.M):
            bad_head.append(f"{rel}:{head[:m.start()].count(chr(10)) + 1}")

        keys = re.findall(r'<meta[^>]*\b(?:property|name)="([^"]+)"', head)
        for k in set(keys):
            if k in REPEATABLE:
                continue
            if keys.count(k) > 1:
                dup_meta.append(f"{rel}: {k} x{keys.count(k)}")

        if UPSTREAM_NAME in html:
            for m in re.finditer(rf"[^\n]{{0,40}}{UPSTREAM_NAME}[^\n]{{0,40}}", html):
                brand.append(f"{rel}: {m.group(0).strip()[:80]}")

        for attr in ("href", "src", "poster"):
            for m in re.finditer(rf'\b{attr}="([^"]+)"', html):
                if not resolves(m.group(1), base):
                    dangling.append(f"{rel}: {attr}={m.group(1)[:70]}")
        for m in re.finditer(r'"(?:contentUrl|thumbnailUrl)"\s*:\s*"([^"]+)"', html):
            if not resolves(m.group(1).replace(origin, ""), DIST):
                dangling.append(f"{rel}: {m.group(1)[:70]}")

        # `html[lang="..."]` selectors are how the template switches typography.
        # If one names a language no built page declares, every rule behind it is
        # dead CSS -- silently, with no error anywhere.
        #
        # This is the shape of a defect that shipped: `seo.py` wrote `<html
        # lang="zh-Hans">` while the Chinese home page carried six
        # `html[lang="zh-CN"]` rules for CJK letter-spacing and padding. All six
        # were inert, on the one page whose language they exist to correct, and
        # nothing said so. Collect the selectors and check them against the lang
        # values actually emitted.
        for m in re.finditer(r'html\[lang="([^"]+)"\]', html):
            lang_selectors.add(m.group(1))
        m = re.search(r'<html[^>]*\blang="([^"]+)"', html)
        if m:
            declared_langs.add(m.group(1))

        n_vid = len(re.findall(r"<video", html))
        n_pos = len(re.findall(r'<video[^>]*\sposter="', html))
        videos_total += n_vid
        videos_with_poster += min(n_pos, n_vid)

    ck(not bad_shape, f"every document is one HTML document ({len(docs)} files)",
       f"{len(bad_shape)} malformed: {bad_shape[:3]}")
    ck(not bad_head, "no text nodes inside <head>",
       f"{len(bad_head)} stray '>' at {bad_head[:4]}")
    ck(not dup_meta, "no duplicated meta keys",
       f"{len(dup_meta)}: {sorted(set(dup_meta))[:4]}")
    ck(not brand, f"no page carries upstream's name ({UPSTREAM_NAME})",
       f"{len(brand)} occurrences, e.g. {brand[:3]}")
    ck(not dangling, "every reference in the static HTML resolves",
       f"{len(dangling)} dangling, e.g. {dangling[:4]}")

    # ---- the payload's own URLs, resolved the way the page resolves them -----
    # `app.js` renders `card.sourceUrl` into an `href` verbatim. So a URL in
    # `library.json` is a URL in the DOM, and its base is the *page's* directory
    # (`/<locale>/library.html`), not the payload's.
    #
    # The runtime-URL check above cannot see these: it reads string literals out
    # of the script, and this one arrives as data. When `sourceUrl` was first
    # rewritten to `./source/<category>/<slug>.md` it still dangled -- `./` is
    # relative to `/en/`, so every one of the 471 links pointed at
    # `/en/source/...`. The tree exists, the string looks right, and 471 links
    # 404.
    payload_bad = []
    lib_json = DIST / "api" / "library.json"
    if lib_json.exists():
        try:
            payload = json.loads(lib_json.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            payload_bad.append(f"api/library.json does not parse: {exc}")
            payload = {}
        for card in payload.get("cards", []):
            for field in ("sourceUrl", "posterUrl", "clipUrl", "thumbnailUrl"):
                val = card.get(field)
                if not val or "${" in val or "{{" in val:
                    continue
                for page_dir in (DIST / "en", DIST / "zh", DIST / "ru"):
                    if not page_dir.is_dir():
                        continue
                    if not resolves(val, page_dir):
                        payload_bad.append(
                            f"{card.get('name', '?')}.{field}={val} "
                            f"from {page_dir.name}/")
                        break
    ck(not payload_bad,
       "every URL in library.json resolves from the page that renders it",
       lambda: f"{len(payload_bad)} dangling, e.g. {payload_bad[:3]}. These are "
               f"`href` values by the time JavaScript has run, so a static crawl "
               f"of the HTML never sees them")

    # ---- language-dependent CSS is actually live ---------------------------
    dead = sorted(lang_selectors - declared_langs)
    ck(not dead,
       f"every html[lang=] selector matches a language the build emits "
       f"({len(lang_selectors)} selector(s), {len(declared_langs)} lang(s))",
       lambda: f"no page declares {dead}, so the rules behind those selectors "
               f"are dead CSS -- for CJK typography that means the letter-spacing "
               f"and padding corrections never apply")

    # ---- 6. URLs the runtime builds ---------------------------------------
    runtime_bad = []
    for name in ("app.js", "showcase.js"):
        f = DIST / "assets" / name
        if not f.exists():
            continue
        src = f.read_text(encoding="utf-8", errors="replace")
        for m in URL_LITERAL.finditer(src):
            target = m.group(1)
            if "${" in target or "{{" in target:
                continue
            if not resolves(target, DIST / "assets"):
                runtime_bad.append(f"{name}: {target}")
    ck(not runtime_bad, "every URL the runtime builds resolves",
       f"{len(runtime_bad)} dangling, e.g. {sorted(set(runtime_bad))[:4]}")

    # ---- 7. poster coverage on the library --------------------------------
    lib = DIST / "en" / "library.html"
    if lib.exists():
        h = lib.read_text(encoding="utf-8", errors="replace")
        n_vid = len(re.findall(r"<video", h))
        n_pos = len(re.findall(r'<video[^>]*\sposter="', h))
        ck(n_vid and n_pos >= n_vid * 0.95,
           f"library videos carry a poster ({n_pos}/{n_vid})",
           f"{n_vid - n_pos} tiles render as a black rectangle until the clip "
           f"decodes; only {len(list((DIST / 'media' / 'poster').glob('*.jpg')))} "
           f"poster files exist, so this needs posters generated from the clips")

    ck(videos_total > 0, "the site ships video at all",
       "a catalogue of motion with no <video> on any page")

    # ---- 9/10. our generated CSS, in both themes ----------------------------
    # Scoped to the block build_site.py marks as generated. Upstream's own 1800
    # lines are not audited: a finding we cannot fix without editing a pinned
    # read-only tree is not a gate, it is a complaint. The block we own is
    # measured exactly, in both themes.
    #
    # The defect this exists for: `.locale-flag` set a hardcoded
    # `background: rgba(14,14,12,.35)` next to `color: var(--muted)`. In the light
    # theme that composited to rgb(164,163,159) under rgb(113,109,100) -- 2.03:1,
    # against a 4.5:1 requirement. A hardcoded colour cannot follow a theme, and
    # pairing it with a themed colour is how it survived a palette where every
    # token carried a comment stating the ratio it clears.
    css_path = DIST / "assets" / "styles.css"
    if css_path.exists():
        css = css_path.read_text(encoding="utf-8", errors="replace")
        if CSS_BEGIN in css and CSS_END in css:
            block = css.split(CSS_BEGIN, 1)[1].split(CSS_END, 1)[0]
            themes = {"light": _theme_tokens(css, ":root"),
                      "dark": _theme_tokens(css, ':root[data-theme="dark"]')}

            missing_tok, low_contrast = [], []
            for rule in re.finditer(r"([^{}]+)\{([^{}]*)\}", block):
                sel, body = rule.group(1).strip(), rule.group(2)
                if sel.startswith("/*") or not sel:
                    continue
                decls = dict(re.findall(r"([\w-]+)\s*:\s*([^;]+)", body))

                for prop, raw in decls.items():
                    for tok in re.findall(r"var\(\s*(--[\w-]+)", raw):
                        absent = [t for t, v in themes.items() if tok not in v]
                        if absent:
                            missing_tok.append(
                                f"{sel} {prop}: {tok} undefined in {'/'.join(absent)}")

                fg_raw = decls.get("color")
                bg_raw = decls.get("background") or decls.get("background-color")
                if not fg_raw or not bg_raw:
                    continue
                for tname, theme in themes.items():
                    page = _resolve(theme.get("--bg", "#fff"), theme)
                    bg = _resolve(bg_raw, theme)
                    fg = _resolve(fg_raw, theme)
                    if not bg or not fg or not page:
                        continue
                    bg = _flatten(bg, page)
                    fg = _flatten(fg, bg)
                    ratio = _contrast(fg, bg)
                    if ratio < MIN_CONTRAST:
                        low_contrast.append(
                            f"{sel} [{tname}] {ratio:.2f}:1 "
                            f"(text {fg_raw.strip()[:28]} on {bg_raw.strip()[:28]})")

            ck(not missing_tok,
               "every custom property the generated CSS uses exists in both themes",
               f"{len(missing_tok)}: {sorted(set(missing_tok))[:3]}. A token defined "
               f"in one theme resolves to nothing in the other, so the rule silently "
               f"changes or stops applying when the reader switches")
            ck(not low_contrast,
               f"generated CSS clears {MIN_CONTRAST}:1 in both themes",
               f"{len(low_contrast)} below, e.g. {low_contrast[:2]}")
        else:
            ck(False, "generated CSS is delimited for audit",
               f"no {CSS_BEGIN.strip()} sentinel in the built styles.css, so the "
               f"switcher's rules cannot be told from upstream's. "
               f"build_site.py appends them")

    # ---- 11. the deploy directory is self-contained -------------------------
    # Cloudflare Pages reads `_headers` from the directory it publishes. The file
    # lived at the repository root, which governs nothing, so the site shipped with
    # the host's default headers: no CSP, no `nosniff`, no `immutable` on 128 MB of
    # video. A hand-copied file is a file that is forgotten exactly once.
    headers = DIST / "_headers"
    if headers.exists():
        raw = headers.read_text(encoding="utf-8", errors="replace")
        patterns = [ln.strip() for ln in raw.splitlines()
                    if ln.strip() and not ln.lstrip().startswith(("#", "!"))]
        # A path pattern must begin at column 0; `Name: value` headers are meant
        # to be indented under it. So the defect is an indented line that is not a
        # header -- it reads as a pattern and matches nothing. ` /media/*` was
        # exactly that, and it governed 128 MB of video.
        stray = indented_non_header(raw)
        ck(not stray, "every _headers path pattern starts at column 0",
           lambda: f"{len(stray)} indented non-header line(s), "
                   f"e.g. {stray[0].strip()[:50]!r} -- reads as a pattern and "
                   f"matches nothing")
        ck(any(p.startswith("/media/") for p in patterns),
           "_headers governs the media path",
           f"128 MB of mp4 with no rule: {patterns[:6]}")
        ck(any("Content-Security-Policy" in ln for ln in patterns),
           "_headers sets a Content-Security-Policy",
           lambda: "the deploy directory ships with the host's default headers")
    else:
        ck(False, "the deploy directory carries _headers",
           "site/dist/_headers is absent, so the published site gets no CSP, no "
           "nosniff and no cache headers. build_site.py copies it")

    passed = total - len(fails)
    return {"lines": lines, "passed": passed, "total": total, "failures": fails,
            "docs": len(docs), "videos": videos_total,
            "videos_with_poster": videos_with_poster}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--origin", default=os.environ.get("SITE_ORIGIN", DEFAULT_ORIGIN))
    ap.add_argument("--allow-placeholder-origin", action="store_true",
                    help="permit https://shotcraft.example, for a tree that is "
                         "not being deployed")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    rep = audit(a.origin, a.allow_placeholder_origin)
    if a.json:
        print(json.dumps(rep, ensure_ascii=False, indent=2))
    else:
        for line in rep["lines"]:
            print(line)
        print(f"\n{rep['passed']}/{rep['total']} structural checks passed "
              f"({rep['docs']} documents, {rep['videos']} <video>)")
    return 1 if rep["failures"] else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())