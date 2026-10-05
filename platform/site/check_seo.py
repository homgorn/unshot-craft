"""Audit the built site the way a crawler reads it.

    python platform/site/check_seo.py
    python platform/site/check_seo.py --origin https://your.domain

Every assertion is made against `site/dist` as written to disk, not against the
template that produced it. That distinction is the whole point: five of the
defects this file exists to catch were invisible in the source and obvious in the
output, because upstream's HTML carries its own `lang`, its own canonical and its
own `og:url`, and a patch that replaces one of them leaves the others.

The checks are grouped by who is hurt when they fail:

  * **Correctness** -- a page that lies about itself. `lang` in the wrong
    language, two canonicals, structured data pointing at another domain.
  * **Reachability** -- a file a browser will request and not get. Every icon,
    every `og:image`, the manifest.
  * **Indexation** -- a page a crawler cannot find or will not trust. hreflang
    pointing at a stub, a sitemap that omits real pages.
  * **Rich results** -- the structured data that earns a carousel instead of a
    blue link.

A failure names the file and the line so it can be fixed without bisecting the
build.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

import os

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _env import load as _load_env  # noqa: E402

_load_env()
DEFAULT_ORIGIN = "https://shotcraft.example"


ROOT = Path(__file__).resolve().parents[2]
DIST = ROOT / "site" / "dist"
LOCALES_DIR = ROOT / "site" / "locales"

REQUIRED_FILES = [
    "favicon.ico",
    "site.webmanifest",
    "browserconfig.xml",
    "assets/logo-mark.svg",
    "assets/apple-touch-icon.png",
    "assets/icon-192.png",
    "assets/icon-512.png",
    "assets/safari-pinned-tab.svg",
    "robots.txt",
    "sitemap.xml",
]

# The site is a catalogue of motion. A build that ships without it has produced a
# text list, and that is not detectable from any tag in <head>.
MOTION_REQUIRED = {"media": 200, "media/poster": 1}

# Translated ui keys that nothing can display: not an attribute on any element of
# any built locale, and not a `t()` call in either script. 33, measured from a
# clean `scripts/init.ps1`, down from 65 before platform/site/localise_dom.py
# existed and from 37 while it was still unreproducible.
#
# That number used to be only reproducible from a clean build, because
# `localise_dom.py` wired a different number of keys on every run and each run
# left a differently annotated tree behind. It is now a pure function of the
# template and `site/locales/en/ui.json`: two clean builds produce byte-identical
# pages, and a second pass wires nothing. So the ceiling can be the exact count
# rather than a slack allowance over one that moved.
#
# The residue is not untranslated work. The English values in `en/ui.json` are
# English renderings of upstream's Chinese `translations.js` table -- 81 of them
# appear verbatim in that file and 0 in `app.js` -- so a key whose wording no code
# path ever emits has no display site. Closing one is a decision about which of
# two English wordings is right, which is why this is a ceiling rather than a
# zero: a gate that cannot be satisfied is a gate that gets deleted.
ORPHAN_CEILING = 33

KNOWN_LOCALES = ("en", "zh", "ru")


def head_of(path: Path) -> str:
    html = path.read_text(encoding="utf-8", errors="replace")
    return html.split("</head>", 1)[0]


def audit(origin: str) -> dict:
    lines: list[str] = []
    failures: list[str] = []
    total = 0

    def ck(ok: bool, name: str, detail: str = "") -> None:
        nonlocal total
        total += 1
        if ok:
            lines.append(f"  ok   {name}")
        else:
            lines.append(f"  FAIL {name}  -- {detail}")
            failures.append(f"{name}: {detail}")

    built = [c for c in KNOWN_LOCALES if (DIST / c / "library.html").exists()]
    if not built:
        return {"lines": ["  no built locales; run build_site.py"], "passed": 0,
                "total": 0, "failures": ["no built locales"]}
    lib = json.loads((DIST / "api" / "library.json").read_text(encoding="utf-8"))
    cards = lib["cards"]
    slugs = sorted(c["name"] for c in cards)

    # ------------------------------------------------------------- the motion
    # Three independent defects each shipped a site with no movement at all, and
    # every one of them passed every gate that existed at the time, because every
    # gate read the DOM after the runtime had patched it -- or read nothing about
    # motion at all. These read the static files and look for the thing itself.
    for code in built:
        idx = DIST / code / "index.html"
        if idx.exists():
            h = idx.read_text(encoding="utf-8", errors="replace")
            ck("createElement('video')" in h or 'createElement("video")' in h,
               f"{code}/index.html: the motion wall is present",
               "no createElement('video') in the static file -- the inline script "
               "was removed, or never emitted")
            ck("WALL_CLIPS" in h,
               f"{code}/index.html: the wall names its clips",
               "no WALL_CLIPS list, so the page cannot know what to play")
            ck("../media/" in h and '"./media/' not in h,
               f"{code}/index.html: media paths are one level up",
               "a './media/' path left unpatched resolves to /<locale>/media/ "
               "and every poster and clip 404s")
            ck("api/library.json" in h,
               f"{code}/index.html: the wall fetches the payload",
               "no reference to api/library.json")

        lib_page = DIST / code / "library.html"
        if lib_page.exists():
            h = lib_page.read_text(encoding="utf-8", errors="replace")
            body = h.split("</head>", 1)[1] if "</head>" in h else h
            n_vid = len(re.findall(r"<video", body))
            ck(n_vid > 0,
               f"{code}/library.html: the prerendered block carries motion",
               f"0 <video> in the static file; app.js draws one at runtime, so "
               f"this passes every DOM-based check and shows a crawler a text list "
               f"of {len(slugs)} cards")
            ck(n_vid >= len(slugs) * 0.5,
               f"{code}/library.html: most cards have a clip ({n_vid}/{len(slugs)})",
               "fewer than half the cards resolve to an mp4 on disk")
            # A <video> whose src 404s is worse than none: the browser shows a
            # broken frame and never recovers.
            bad = []
            for src in re.findall(r'<video[^>]*\ssrc="([^"]+)"', body):
                clean = src.split("?")[0].replace("../media/", "media/")
                if not (DIST / clean).exists():
                    bad.append(src)
                else:
                    poster = re.search(
                        r'<video[^>]*\ssrc="' + re.escape(src) +
                        r'"[^>]*\sposter="([^"]+)"', body)
                    if poster:
                        p = (DIST / poster.group(1).replace("../media/", "media/"))
                        if not p.exists():
                            bad.append(f"poster {poster.group(1)}")
            ck(not bad, f"{code}/library.html: every clip and poster resolves",
               f"{len(bad)} dangling, e.g. {bad[:3]}")

    # ----------------------------------------------- translations that are shown
    # `check_coverage.py` measures whether a string exists in a locale file. It
    # reported ru at 99.7 % while the search placeholder, the theme toggle, the
    # energy filter labels and the entire showcase page rendered in English,
    # because no element and no script carried a lookup for them. Coverage of a
    # translation nobody can read is not coverage.
    #
    # So this measures the other thing: how many translated keys have somewhere to
    # be displayed. The residue is expected and is a fact, not a failure -- the
    # English values in `en/ui.json` are English renderings of upstream's Chinese
    # `translations.js` table, so a key whose wording app.js never emits is
    # orphaned rather than untranslated. It is checked against a recorded ceiling
    # so it can be seen to grow.
    rep = LOCALES_DIR.parent / "build" / "localise_report.json"
    if rep.exists():
        loc = json.loads(rep.read_text(encoding="utf-8"))
        orphan = len(loc.get("orphaned", []))
        ck(orphan <= ORPHAN_CEILING,
           f"orphaned translation keys: {orphan} (ceiling {ORPHAN_CEILING})",
           "more translated strings have no display site than the recorded "
           "ceiling; each new one needs a decision, not a rebuild")
        # The three most prominent strings on a library page. A search box in the
        # wrong language on a localised page is the failure a reader notices first.
        #
        # Anchored on the element, not on the substring. `data-i18n-placeholder`
        # was once satisfied by an annotation sitting on the `<label>` that wraps
        # the search box rather than on the `<input>`, which is why the placeholder
        # was English on every locale while this check stayed green: it found the
        # string and never asked what it was attached to.
        #
        # `themeDark` is on `<span id="themeToggleLabel">`, not on the button:
        # `data-i18n` sets textContent, so putting it on the button would replace
        # the toggle's two icon `<svg>`s with the word "Dark".
        for code in built:
            lib = DIST / code / "library.html"
            if lib.exists():
                h = lib.read_text(encoding="utf-8", errors="replace")
                ck(re.search(r'<input[^>]*\bdata-i18n-placeholder="searchPlaceholder"', h)
                   is not None,
                   f"{code}/library.html: the search box is translatable",
                   "no data-i18n-placeholder on the <input>, so the placeholder "
                   "is English on every locale")
                ck(re.search(r'<span[^>]*\bid="themeToggleLabel"[^>]*\bdata-i18n="theme(To)?[DL]', h)
                   is not None,
                   f"{code}/library.html: the theme toggle is translatable",
                   "no data-i18n on #themeToggleLabel, so the toggle reads in "
                   "English on every locale")
    else:
        ck(False, "localise_dom report exists",
           "site/build/localise_report.json missing; run platform/site/localise_dom.py")

    # ---------------------------------------------------------------- files
    for f in REQUIRED_FILES:
        p = DIST / f
        ck(p.exists() and p.stat().st_size > 0, f"asset present: {f}",
           "missing or empty")

    for sub, floor in MOTION_REQUIRED.items():
        d = DIST / sub
        n = len([x for x in d.iterdir() if x.is_file()]) if d.is_dir() else 0
        ck(n >= floor, f"motion deployed: {sub}/ ({n} files)",
           f"fewer than {floor}; run python platform/mirror_site.py --media "
           f"then platform/site/build_site.py")

    for code in built:
        for og in (f"assets/og-{code}.jpg",):
            p = DIST / og
            ck(p.exists() and p.stat().st_size > 2000, f"social card: {og}",
               "missing or implausibly small")

    robots = (DIST / "robots.txt").read_text(encoding="utf-8") if (DIST / "robots.txt").exists() else ""
    ck("vincentwei" not in robots, "robots.txt is ours, not upstream's copy",
       f"still names the author's domain: {robots[:80]!r}")
    m = re.search(r"^Sitemap:\s*(\S+)", robots, re.M)
    ck(bool(m) and m.group(1).startswith(origin),
       "robots.txt advertises our own sitemap",
       f"found {m.group(1) if m else 'no Sitemap line'}")

    # ------------------------------------------------------------ per page
    for code in built:
        for page in ("index", "library", "showcase"):
            p = DIST / code / f"{page}.html"
            if not p.exists():
                continue
            head = head_of(p)
            html = p.read_text(encoding="utf-8")

            lang = re.search(r'<html[^>]*\blang="([^"]+)"', html)
            ck(bool(lang) and lang.group(1) != "en" or code == "en",
               f"{code}/{page}: <html lang> matches the locale",
               f"lang={lang.group(1) if lang else '(none)'} for locale {code}")

            canon = re.search(r'<link rel="canonical" href="([^"]+)"', head)
            ogu = re.search(r'property="og:url" content="([^"]+)"', head)
            ck(bool(canon) and bool(ogu) and canon.group(1) == ogu.group(1),
               f"{code}/{page}: canonical and og:url agree",
               f"canonical={canon.group(1) if canon else None} "
               f"og:url={ogu.group(1) if ogu else None}")

            ck(bool(canon) and origin in canon.group(1),
               f"{code}/{page}: canonical is on our origin",
               canon.group(1) if canon else "no canonical")
            ck("vincentwei" not in head,
               f"{code}/{page}: no upstream origin left in <head>",
               "an upstream canonical or og:url survived the patch")

            title = re.search(r"<title>(.*?)</title>", head, re.S)
            ck(bool(title) and title.group(1).strip() != "",
               f"{code}/{page}: has a title", "empty")
            desc = re.search(r'name="description" content="([^"]*)"', head)
            # The useful length is in *characters a reader sees*, and a CJK
            # character is roughly two Latin ones. A flat 60-300 floor made every
            # Chinese description fail -- and 16 Chinese characters is a whole
            # sentence, so the check was wrong, not the copy. Both ranges are
            # derived from the script of the string itself.
            if desc:
                text = desc.group(1)
                cjk_n = sum(1 for ch in text if "一" <= ch <= "鿿")
                weight = len(text) + cjk_n          # CJK counted twice
                lo, hi = (30, 160) if cjk_n > len(text) / 4 else (60, 320)
                ck(lo <= weight <= hi,
                   f"{code}/{page}: meta description length is sane",
                   f"{len(text)} chars ({cjk_n} CJK, weight {weight}), "
                   f"want {lo}-{hi} for a {'CJK' if lo == 30 else 'latin'} string")
            else:
                ck(False, f"{code}/{page}: meta description length is sane",
                   "no meta description at all")

            # Localisation: a description identical to en on a non-en page means
            # the share preview is in the wrong language.
            en_desc = re.search(r'name="description" content="([^"]*)"',
                                head_of(DIST / "en" / f"{page}.html")) \
                if (DIST / "en" / f"{page}.html").exists() else None
            if code != "en" and desc and en_desc:
                ck(desc.group(1) != en_desc.group(1),
                   f"{code}/{page}: description is not the English one",
                   "byte-identical to en")

            ck('name="twitter:card"' in head, f"{code}/{page}: twitter:card", "absent")
            ck("twitter:image:alt" in head, f"{code}/{page}: twitter:image:alt", "absent")
            ck('property="og:image:type"' in head, f"{code}/{page}: og:image:type", "absent")
            ck('name="theme-color"' in head, f"{code}/{page}: theme-color", "absent")
            ck('rel="manifest"' in head, f"{code}/{page}: manifest link", "absent")
            ck('rel="apple-touch-icon"' in head,
               f"{code}/{page}: apple-touch-icon", "absent")
            ck('name="robots"' in head, f"{code}/{page}: explicit robots meta", "absent")

            ogi = re.search(r'property="og:image" content="([^"]+)"', head)
            if ogi:
                target = ogi.group(1).split("?")[0].replace(origin, "")
                ck((DIST / target.lstrip("/")).exists(),
                   f"{code}/{page}: og:image resolves to a real file",
                   f"{ogi.group(1)} -> {target} not on disk")

            ld = re.findall(r'<script type="application/ld\+json">(.*?)</script>',
                            head, re.S)
            ck(bool(ld), f"{code}/{page}: has JSON-LD", "none emitted")
            # At least one block must describe the site itself; a second block
            # describing something else (an ItemList for the carousel) is
            # correct and must not be held to that requirement. Every block,
            # though, must be ours -- an inherited block naming the author's
            # domain is a lie about where this page lives.
            saw_site = False
            for block in ld:
                try:
                    data = json.loads(block)
                except json.JSONDecodeError as exc:
                    ck(False, f"{code}/{page}: JSON-LD parses", str(exc))
                    continue
                blob = json.dumps(data)
                ck("vincentwei" not in blob,
                   f"{code}/{page}: JSON-LD has no upstream url",
                   "structured data points at the author's site")
                if '"WebSite"' in blob:
                    saw_site = True
            ck(saw_site, f"{code}/{page}: JSON-LD declares a WebSite",
               "no block describes the site itself")

            hrefs = re.findall(r'hreflang="([^"]+)" href="([^"]+)"', head)
            ck(len(hrefs) >= len(built) + 1,
               f"{code}/{page}: hreflang covers every built locale + x-default",
               f"found {len(hrefs)}")
            dangling = [h for _, h in hrefs
                        if not (DIST / h.replace(origin, "").lstrip("/")).exists()]
            ck(not dangling, f"{code}/{page}: no hreflang points at a missing file",
               f"{dangling[:3]}")

    # ---------------------------------------------------------- card pages
    for code in built:
        d = DIST / code / "card"
        pages = sorted(d.glob("*.html")) if d.is_dir() else []
        ck(bool(pages), f"{code}: has per-card pages", "no card/ directory")
        if not pages:
            continue
        built_slugs = {p.stem for p in pages}
        ck(len(built_slugs) == len(slugs),
           f"{code}: one card page per card ({len(slugs)})",
           f"{len(built_slugs)} built, {len(slugs)} cards in the payload")

        # Distinctness across the whole set, not just the sample. One shared
        # image across 157 cards is the defect; checking four pages could not
        # see it if the shared one happened to be among them.
        imgs = set()
        for p in pages:
            m = re.search(r'property="og:image" content="([^"]+)"', head_of(p))
            if m:
                imgs.add(m.group(1))
        ck(len(imgs) == len(pages),
           f"{code}: every card page has its own og:image ({len(imgs)}/{len(pages)})",
           f"{len(pages) - len(imgs)} pages share an image with another card")

        # The declared VideoObject duration must be the clip's real length.
        #
        # Every derivable source in this repo is a different quantity from the
        # clip: `shot_card.duration_frames` is how long the shot should hold in a
        # film (11 frames for crash-zoom-punch), `style.duration_frames` is how
        # long the demo component runs (120). The preview is the second one, so
        # the first version declared PT0.4S on a 4-second video -- and 6 of 6
        # sampled clips were wrong, each plausible, because a short number is
        # exactly what a video object is supposed to have. Only the file is not
        # wrong, so only the file is asked.
        ff = shutil.which("ffprobe")
        sampled = pages[:4] + pages[len(pages) // 2:len(pages) // 2 + 2] + pages[-2:]
        wrong: list[str] = []
        undeclared = 0
        probed = 0
        for p in sampled:
            h = head_of(p)
            m = re.search(r'"contentUrl":\s*"([^"]+)"', h)
            d = re.search(r'"duration":\s*"PT([\d.]+)S"', h)
            if not m:
                continue
            if not d:
                undeclared += 1
                continue
            target = m.group(1).replace(origin, "").lstrip("/")
            clip = DIST / target
            if not (ff and clip.exists()):
                continue
            probed += 1
            out = subprocess.run(
                [ff, "-v", "error", "-show_entries", "format=duration", "-of", "json",
                 str(clip)], capture_output=True, text=True, errors="replace")
            try:
                real = float(json.loads(out.stdout)["format"]["duration"])
            except (json.JSONDecodeError, KeyError, ValueError):
                continue
            if abs(real - float(d.group(1))) > 0.25:
                wrong.append(f"{p.stem}: declares PT{d.group(1)}S, file is {real}s")
        ck(not wrong,
           f"{code}: every declared clip length matches the file ({probed} probed)",
           f"{len(wrong)} wrong, e.g. {wrong[:3]}")
        ck(undeclared == 0,
           f"{code}: every VideoObject states a duration ({undeclared} silent)",
           "a VideoObject with no duration is dropped from video rich results")

        sample = pages[:3] + pages[-1:]
        for p in sample:
            head = head_of(p)
            html = p.read_text(encoding="utf-8")
            canon = re.search(r'<link rel="canonical" href="([^"]+)"', head)
            ck(bool(canon) and f"/{code}/card/{p.stem}" in canon.group(1),
               f"{code}/card/{p.stem}: canonical is its own URL",
               canon.group(1) if canon else "no canonical")
            ck(origin in (canon.group(1) if canon else ""),
               f"{code}/card/{p.stem}: canonical on our origin", "")
            ogu = re.search(r'property="og:url" content="([^"]+)"', head)
            ck(bool(canon) and bool(ogu) and canon.group(1) == ogu.group(1),
               f"{code}/card/{p.stem}: canonical == og:url", "")
            ogi = re.search(r'property="og:image" content="([^"]+)"', head)
            # The image must exist *and* be this card's own. All 471 card pages
            # pointed at one blank placeholder: it was generated from an empty
            # title, it passed the existence check, and Facebook had already
            # cached it. Existence alone cannot catch that; only distinctness can.
            if ogi:
                target = ogi.group(1).replace(origin, "").lstrip("/")
                fp = DIST / target
                ck(fp.exists() and fp.stat().st_size > 2000,
                   f"{code}/card/{p.stem}: og:image exists",
                   f"{ogi.group(1)} -> {target} missing or empty")
                ck(f"/og-card/{p.stem}-{code}." in ogi.group(1),
                   f"{code}/card/{p.stem}: og:image is this card's own",
                   f"points at {ogi.group(1)}, which is shared")
            ck('property="og:type" content="article"' in head,
               f"{code}/card/{p.stem}: og:type is article", "")
            ld = re.findall(r'<script type="application/ld\+json">(.*?)</script>', head, re.S)
            ck(bool(ld), f"{code}/card/{p.stem}: has JSON-LD", "")
            if ld:
                try:
                    blob = json.dumps(json.loads(ld[0]))
                    ck('"TechArticle"' in blob,
                       f"{code}/card/{p.stem}: JSON-LD is a TechArticle", "")
                    ck('"BreadcrumbList"' in blob,
                       f"{code}/card/{p.stem}: JSON-LD has breadcrumbs", "")
                except json.JSONDecodeError as exc:
                    ck(False, f"{code}/card/{p.stem}: JSON-LD parses", str(exc))
            hrefs = re.findall(r'hreflang="([^"]+)" href="([^"]+)"', head)
            ck(len(hrefs) >= len(built) + 1,
               f"{code}/card/{p.stem}: hreflang cluster complete",
               f"found {len(hrefs)}")
            # The one that matters on a card page: no CJK left in a Russian card.
            body = html.split("</head>", 1)[1]
            text = re.sub(r"<[^>]+>", " ", body)
            if code == "ru":
                ck(not any("一" <= ch <= "鿿" for ch in text),
                   f"{code}/card/{p.stem}: no CJK on a Russian card page",
                   "the page falls back to the Chinese corpus")

    # ------------------------------------------------------------- sitemap
    sm = DIST / "sitemap.xml"
    if sm.exists():
        xml = sm.read_text(encoding="utf-8")
        n = len(re.findall(r"<url>", xml))
        ck("vincentwei" not in xml, "sitemap is on our origin", "upstream origin")
        for code in built:
            want = len(slugs) + 3
            got = len(re.findall(rf"/{code}/", xml))
            ck(got >= want, f"sitemap lists {code}'s pages ({want})",
               f"found {got}")
        ck(n > 0, "sitemap is not empty", f"{n} entries")

    passed = total - len(failures)
    return {"lines": lines, "passed": passed, "total": total,
            "failures": failures}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--origin", default=os.environ.get("SITE_ORIGIN", DEFAULT_ORIGIN))
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    rep = audit(a.origin)
    if a.json:
        print(json.dumps(rep, ensure_ascii=False, indent=2))
    else:
        for line in rep["lines"]:
            print(line)
        print(f"\n{rep['passed']}/{rep['total']} SEO checks passed")
    return 1 if rep["failures"] else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
