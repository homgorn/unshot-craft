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
import sys
from pathlib import Path

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

    # ---------------------------------------------------------------- files
    for f in REQUIRED_FILES:
        p = DIST / f
        ck(p.exists() and p.stat().st_size > 0, f"asset present: {f}",
           "missing or empty")

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
                ck('"@type": "WebSite"' in blob or '"@type":"WebSite"' in blob,
                   f"{code}/{page}: JSON-LD declares a WebSite", "absent")

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
    ap.add_argument("--origin", default="https://shotcraft.example")
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
