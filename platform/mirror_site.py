"""Mirror the live GitHub Pages site (and optionally the mp4 release assets).

    python platform/mirror_site.py --out upstream/site-mirror
    python platform/mirror_site.py --out upstream/site-mirror --media     # + all mp4s

Why this exists separately from the repo clone:

* the repo carries `gallery/` — the site *source*;
* the deployed site carries more: `gallery/media/*.mp4` (214 previews) and
  `gallery/api/showcase.json`, both downloaded at deploy time from the
  `gallery-media` / `showcase-media` GitHub releases, neither present in git.

The local checkout therefore has 0 of 214 previews. Any work on the library page
(SEO, localisation, indexing) needs them, so mirror them explicitly.

Exits non-zero if the mirror is incomplete, so it can gate a pipeline.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

BASE = "https://vincentwei1021.github.io/video-shotcraft"
ROOT = Path(__file__).resolve().parents[1]
USER_AGENT = "shotcraft-mirror/1.0 (+architecture research)"
SKIP_SUFFIX = (".mp4", ".mov", ".webm")


def fetch(url: str, timeout: float = 30.0, retries: int = 3) -> bytes:
    last: Exception | None = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            last = exc
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"failed {url}: {last}")


def crawl(out: Path, max_pages: int = 400) -> list[str]:
    """Depth-2 crawl of same-origin html, staying inside the site prefix."""
    seen: set[str] = set()
    queue = [BASE + "/"]
    pages: list[str] = []
    while queue and len(pages) < max_pages:
        url = queue.pop(0)
        if url in seen:
            continue
        seen.add(url)
        try:
            body = fetch(url).decode("utf-8", errors="replace")
        except RuntimeError as exc:
            print(f"  ! {exc}", file=sys.stderr)
            continue
        rel = url[len(BASE):].strip("/") or "index.html"
        target = out / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(body, encoding="utf-8")
        pages.append(rel)
        print(f"  + {rel} ({len(body):,} bytes)")
        for href in re.findall(r'(?:href|src)="([^"#?]+)"', body):
            if href.startswith("#") or href.startswith("mailto:"):
                continue
            # absolute and protocol-relative URLs are external: skip rather than
            # concatenating them onto BASE (which produced 404s on every one)
            if href.startswith(("http://", "https://", "//", "/")):
                if href.startswith(BASE):
                    rel = href[len(BASE):].strip("/")
                    if rel.endswith(".html") and rel not in seen:
                        queue.append(href)
                continue
            if re.match(r"^[a-z][a-z0-9+.-]*:", href, re.I):   # other schemes
                continue
            if href.endswith(SKIP_SUFFIX) or href.endswith((".jpg", ".svg", ".png", ".json", ".css", ".js", ".txt", ".xml")):
                continue
            nxt = BASE + "/" + href.lstrip("./")
            if nxt.startswith(BASE) and nxt not in seen:
                queue.append(nxt)
    return pages


def assets_from_library(out: Path, workers: int = 8) -> tuple[int, int]:
    """Pull media/*.mp4 and media/poster/*.jpg listed in library.json."""
    lib_file = out / "api" / "library.json"
    if not lib_file.exists():
        try:
            (out / "api").mkdir(parents=True, exist_ok=True)
            lib_file.write_bytes(fetch(BASE + "/api/library.json"))
        except RuntimeError as exc:
            print(f"  ! {exc}", file=sys.stderr)
            return 0, 0
    lib = json.loads(lib_file.read_text(encoding="utf-8"))
    urls: list[str] = []
    for card in lib.get("cards", []):
        for st in card.get("styles", []):
            media = st.get("media") or {}
            url = media.get("url") if isinstance(media, dict) else media
            if url:
                urls.append(url.split("?")[0])
            urls.append(f"./media/poster/{st.get('key')}.jpg")

    ok = fail = 0
    seen: set[str] = set()

    def grab(rel: str) -> bool:
        if rel in seen:
            return True
        seen.add(rel)
        path = out / rel.lstrip("./")
        if path.exists() and path.stat().st_size > 0:
            return True
        try:
            data = fetch(BASE + "/" + rel.lstrip("./"), timeout=60)
        except RuntimeError:
            return False
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        return True

    with ThreadPoolExecutor(max_workers=workers) as pool:
        for rel, good in zip(urls, pool.map(grab, urls)):
            ok += int(good)
            fail += int(not good)
    return ok, fail


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="upstream/site-mirror")
    ap.add_argument("--media", action="store_true",
                    help="also download every mp4 preview and poster (large)")
    a = ap.parse_args()
    out = ROOT / a.out
    out.mkdir(parents=True, exist_ok=True)

    print(f"mirroring {BASE} -> {out}")
    pages = crawl(out)
    print(f"pages: {len(pages)}")

    if a.media:
        print("downloading media (this is the big one)…")
        ok, fail = assets_from_library(out)
        print(f"assets ok={ok} fail={fail}")
        if fail:
            print(f"WARNING: {fail} assets missing", file=sys.stderr)

    # verify against library.json, the same check deploy-pages.yml performs
    lib_file = out / "api" / "library.json"
    missing: list[str] = []
    if lib_file.exists():
        lib = json.loads(lib_file.read_text(encoding="utf-8"))
        for card in lib.get("cards", []):
            for st in card.get("styles", []):
                media = st.get("media") or {}
                url = media.get("url") if isinstance(media, dict) else media
                if url and not (out / url.split("?")[0].lstrip("./")).exists():
                    missing.append(url.split("?")[0])
    print(json.dumps({"pages": len(pages), "missing_previews": len(missing),
                      "sample_missing": missing[:5]}, indent=2))
    return 1 if missing and a.media else 0


if __name__ == "__main__":
    raise SystemExit(main())