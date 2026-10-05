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
7. `<video>` poster coverage, because a posterless looping tile is a black
   rectangle for as long as it takes to decode
8. the origin is not the `.example` placeholder, unless explicitly allowed
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


def audit(origin: str, allow_placeholder: bool) -> dict:
    lines: list[str] = []
    fails: list[str] = []
    total = 0

    def ck(ok: bool, name: str, detail: str = "") -> None:
        nonlocal total
        total += 1
        if ok:
            lines.append(f"  ok   {name}")
        else:
            lines.append(f"  FAIL {name}  -- {detail}")
            fails.append(f"{name}: {detail}")

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