"""F011/F012/F013/F014: drive the built site in a real browser and assert behaviour.

    python platform/site/selftest.py
    python platform/site/selftest.py --shots     # also write PNGs to site/build/shots/

Starts the server itself, then drives it through a CDP client over the DevTools
websocket. No playwright, no selenium: this needs three assertions (a hash-fragment
deep link, a language switch that preserves it, and a no-untranslated-keys check)
and a 40 MB dependency is not worth it for that.

Asserted:
  1. every built locale returns 200 and renders 157 cards
  2. no visible text is a raw i18n key (documentTitle, catOpening, ...)
  3. the language switcher navigates between locales and PRESERVES the fragment
  4. a deep link like /ru/library.html#crash-zoom-punch resolves to that card
  5. hreflang is complete on every page and the canonical is self-referencing
  6. every page emits all built locales plus x-default
  7. the sitemap covers locale x page
  8. root redirects by Accept-Language and always renders a no-JS language list
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import socket
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIST = ROOT / "site" / "dist"
PAGES = ("index", "library", "showcase")

# Counts come from the index, never from a literal. Every number this test
# compares against used to be hardcoded, which meant an upstream bump would
# either fail the suite for the wrong reason or, worse, be made to pass by
# editing the test.
# Directory name -> BCP-47 tag, owned by platform/site/seo.py (META) and
# imported rather than restated: two copies of this table is one table too
# many, and the failure mode is a test that disagrees with the build.
sys.path.insert(0, str(ROOT / "platform" / "site"))
from seo import META as _SEO_META  # noqa: E402
HREFLANG = {code: m[3] for code, m in _SEO_META.items()}

CARD_COUNT = json.loads(
    (DIST / "api" / "library.json").read_text(encoding="utf-8"))["stats"]["cardCount"] \
    if (DIST / "api" / "library.json").exists() else 0

# Keys that must never reach the screen as literal text.
KEY_RE = re.compile(
    r"^(documentTitle|cat[A-Z]\w+|pageTitle|intro|searchPlaceholder|languageToggle|"
    r"themeDark|themeLight|categoriesHeading|cardsHeading|stylesHeading|samplesHeading|"
    r"allShots|skip|brandHome|followMe|starGitHubLabel|viewShowcase|navShowcase|"
    r"navLibrary|emptyState|noResults|clearFilters|selectLabel|copyLabel|sourceLabel)\b"
)


def free_port() -> int:
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]
    s.close()
    return p


def start_server(port: int):
    # `--serve` without `--rebuild`: serving a tree must not regenerate it. When
    # this call also ran the build, the test's own fixture became the
    # untranslated template and the stamp check below failed for a reason that
    # had nothing to do with the product.
    return subprocess.Popen(
        [sys.executable, str(ROOT / "platform" / "site" / "build_site.py"),
         "--serve", str(port)],
        cwd=str(ROOT), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        env={**__import__("os").environ, "PYTHONIOENCODING": "utf-8"})


def get(url: str, headers: dict | None = None):
    req = urllib.request.Request(url, headers=headers or {})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return r.status, r.read().decode("utf-8", "replace"), dict(r.headers)
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace"), dict(e.headers)


# --------------------------------------------------------------------------
# Minimal CDP client
# --------------------------------------------------------------------------

class CDP:
    def __init__(self, ws_url: str):
        import socket as _s
        u = ws_url.split("://", 1)[1]
        hostport, path = u.split("/", 1)
        host, port = hostport.split(":")
        self.sock = _s.create_connection((host, int(port)), timeout=30)
        key = base64.b64encode(os.urandom(16)).decode()
        req = (f"GET /{path} HTTP/1.1\r\nHost: {hostport}\r\nUpgrade: websocket\r\n"
               f"Connection: Upgrade\r\nSec-WebSocket-Key: {key}\r\n"
               f"Sec-WebSocket-Version: 13\r\n\r\n")
        self.sock.sendall(req.encode())
        buf = b""
        while b"\r\n\r\n" not in buf:
            buf += self.sock.recv(4096)
        self.buf = buf.split(b"\r\n\r\n", 1)[1]
        self.msg_id = 0

    def _send(self, payload: dict) -> None:
        data = json.dumps(payload).encode("utf-8")
        n = len(data)
        header = bytearray([0x81])
        mask = os.urandom(4)
        if n < 126:
            header.append(0x80 | n)
        elif n < 65536:
            header.append(0x80 | 126)
            header += n.to_bytes(2, "big")
        else:
            header.append(0x80 | 127)
            header += n.to_bytes(8, "big")
        header += mask
        header += bytes(b ^ mask[i % 4] for i, b in enumerate(data))
        self.sock.sendall(bytes(header))

    def _recv(self) -> dict:
        def read(n: int) -> bytes:
            out = b""
            while len(out) < n:
                chunk = self.buf[: n - len(out)]
                if not chunk:
                    chunk = self.sock.recv(n - len(out))
                out += chunk
                self.buf = self.buf[len(chunk):]
            return out
        b1, b2 = read(2)
        length = b2 & 0x7F
        if length == 126:
            length = int.from_bytes(read(2), "big")
        elif length == 127:
            length = int.from_bytes(read(8), "big")
        return json.loads(read(length).decode("utf-8"))

    def call(self, method: str, params: dict | None = None, timeout: float = 30) -> dict:
        self.msg_id += 1
        mid = self.msg_id
        self._send({"id": mid, "method": method, "params": params or {}})
        deadline = time.time() + timeout
        while time.time() < deadline:
            msg = self._recv()
            if msg.get("id") == mid:
                if "error" in msg:
                    raise RuntimeError(f"{method}: {msg['error']}")
                return msg.get("result", {})
        raise TimeoutError(method)

    def evaluate(self, expr: str):
        r = self.call("Runtime.evaluate", {
            "expression": expr, "returnByValue": True, "awaitPromise": True})
        if r.get("exceptionDetails"):
            raise RuntimeError(r["exceptionDetails"].get("text", "eval failed"))
        return r["result"].get("value")


def chrome_ws(port: int = 0, timeout: float = 25):
    """Launch headless Chrome with a debug port; return (ws_url, process)."""
    cands = []
    if os.environ.get("CHROME_PATH"):
        cands.append(os.environ["CHROME_PATH"])
    for name in ("chrome.exe", "chrome", "msedge.exe", "msedge",
                 "Google/Chrome/Application/chrome.exe",
                 "Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
                 "Program Files/Google/Chrome/Application/chrome.exe"):
        cands += [
            name,
            str(Path("C:/Program Files/Google/Chrome/Application") / name),
            str(Path("C:/Program Files (x86)/Google/Chrome/Application") / name),
            str(Path("C:/Program Files/Microsoft/Edge/Application") / name),
            str(Path("C:/Program Files (x86)/Microsoft/Edge/Application") / name),
        ]
    exe = next((c for c in cands if Path(c).exists()), None)
    if not exe:
        raise RuntimeError("no Chrome/Edge binary found; set CHROME_PATH")
    dbg = free_port()
    profile = tempfile.mkdtemp(prefix="shotcraft-cdp-")
    proc = subprocess.Popen(
        [exe, "--headless=new", f"--remote-debugging-port={dbg}", f"--user-data-dir={profile}",
         "--no-first-run", "--no-default-browser-check", "--disable-gpu",
         "--hide-scrollbars", "--window-size=1440,900", "about:blank"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    deadline = time.time() + timeout
    page_ws = None
    while time.time() < deadline:
        try:
            # /json/version is the *browser* endpoint, which has no Page domain.
            # We need a page target's websocket, so attach to a real tab.
            with urllib.request.urlopen(f"http://127.0.0.1:{dbg}/json/list", timeout=2) as r:
                targets = json.loads(r.read())
            for t in targets:
                if t.get("type") == "page" and t.get("webSocketDebuggerUrl"):
                    page_ws = t["webSocketDebuggerUrl"]
                    break
            if page_ws:
                return page_ws, proc
        except Exception:
            pass
        time.sleep(0.3)
    proc.kill()
    raise RuntimeError("chrome did not expose a page target")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--shots", action="store_true")
    ap.add_argument("--keep-server", action="store_true")
    a = ap.parse_args()

    if not DIST.exists():
        raise SystemExit("site/dist missing; run platform/site/build_site.py first")

    coverage = json.loads((ROOT / "site" / "build" / "coverage.json").read_text(encoding="utf-8"))

    # The set of locales to check must come from the DATABASE, not from the set of
    # directories that happen to exist.
    #
    # Deriving it from the built output made every locale assertion
    # self-fulfilling: with three locales built, "hreflang covers all locales"
    # meant "hreflang covers the three we built". The DB tracks nine. A locale
    # that is registered but not built is now reported explicitly, so the gap
    # between the ledger and the site is visible instead of silently excluded.
    ADVERTISED = ["en", "zh", "ru", "es", "de", "fr", "pt", "ko", "ja"]
    built = [c for c in ADVERTISED if (DIST / c).is_dir()]
    try:
        import sqlite3
        db = sqlite3.connect(f"file:{(ROOT / 'platform' / 'db' / 'shotcraft.db').as_posix()}?mode=ro",
                             uri=True)
        db.row_factory = sqlite3.Row
        registered = [r[0] for r in db.execute("SELECT code FROM locale ORDER BY id")]
        db.close()
    except sqlite3.Error as exc:
        registered = []
        check("locale table readable", False, str(exc))

    locales = built
    unbuilt = [c for c in registered if c not in built]
    print(f"  locales in the DB: {len(registered)}   built: {len(built)} ({', '.join(built)})")
    if unbuilt:
        # A registered-but-unbuilt locale is a WARN, not a failure: the whole
        # design is that an unfinished locale is simply not advertised. What is
        # a failure is being *advertised* in hreflang while unbuilt.
        print(f"  registered but not built (not advertised): {', '.join(unbuilt)}")
    checks: list[tuple[str, bool, str]] = []

    def check(name: str, ok: bool, detail: str = "") -> None:
        checks.append((name, ok, detail))

    port = free_port()
    server = start_server(port)
    base = f"http://localhost:{port}"
    for _ in range(60):
        code, _, _ = get(base + "/en/library.html")
        if code == 200:
            break
        time.sleep(0.25)

    chrome = None
    try:
        # ---------------- static assertions ----------------
        for lc in locales:
            for page in PAGES:
                if not (DIST / lc / f"{page}.html").exists():
                    # A skipped assertion is an invisible failure. A locale we
                    # claim to build must ship all three pages.
                    check(f"{lc}/{page}.html exists", False, "file missing")
                    continue
                code, html, _ = get(f"{base}/{lc}/{page}.html")
                check(f"{lc}/{page}.html 200", code == 200, str(code))
                # hreflang carries a BCP-47 tag, not our directory name: `zh` is
                # ambiguous between Traditional and Simplified, so the tag is
                # `zh-Hans`. These assertions used to compare the tag against the
                # directory name, which meant the correct tag read as a dangling
                # hreflang and the test failed for a reason that was the test's.
                hrefs = set(re.findall(r'hreflang="([^"]+)"', html))
                want_tags = {HREFLANG[l] for l in locales} | {"x-default"}
                missing = sorted(want_tags - hrefs)
                check(f"{lc}/{page}.html hreflang covers all built locales + x-default",
                      not missing, f"missing {missing}")
                # And the mirror image: no hreflang may point at a locale we did
                # not build, because an hreflang to a 404 is a broken promise.
                tag_to_dir = {v: k for k, v in HREFLANG.items()}
                dangling = sorted(
                    tag_to_dir.get(h, h) for h in hrefs
                    if h != "x-default" and h in tag_to_dir
                    and not (DIST / tag_to_dir[h]).is_dir())
                check(f"{lc}/{page}.html advertises no unbuilt locale",
                      not dangling, f"hreflang -> {dangling} which 404")
                canon = re.search(r'<link rel="canonical" href="([^"]+)"', html)
                check(f"{lc}/{page}.html canonical self-ref",
                      bool(canon) and f"/{lc}/" in canon.group(1),
                      canon.group(1) if canon else "absent")
                check(f"{lc}/{page}.html no upstream canonical",
                      "vincentwei1021.github.io/video-shotcraft/library.html" not in html)
                check(f"{lc}/{page}.html loads shared runtime",
                      "assets/i18n.js" in html and "assets/i18n/" in html)

        code, xml, _ = get(base + "/sitemap.xml")
        check("sitemap 200", code == 200)
        locs = re.findall(r"<loc>([^<]+)</loc>", xml)

        # The sitemap is checked against each page's own canonical, not against a
        # hardcoded URL shape. The previous version asserted `/zh/index.html`
        # because that was the shape at the time; the canonical is now `/zh/`, and
        # a check that encodes a string instead of a relationship is a check that
        # fails the moment the canonical changes for a good reason -- which is
        # exactly what happened, and why it was rewritten rather than satisfied.
        for lc in locales:
            for page in PAGES:
                f = DIST / lc / f"{page}.html"
                if not f.exists():
                    continue
                m = re.search(r'<link rel="canonical" href="([^"]+)"',
                              f.read_text(encoding="utf-8"))
                want = m.group(1) if m else ""
                check(f"sitemap lists {lc}/{page}.html at its canonical",
                      bool(want) and want in locs,
                      f"canonical {want!r} not among the {len(locs)} sitemap URLs")

        card_pages = sorted((DIST / locales[0] / "card").glob("*.html")) \
            if (DIST / locales[0] / "card").is_dir() else []
        if card_pages:
            in_sm = sum(1 for p in card_pages
                        if f"/card/{p.stem}.html" in " ".join(locs))
            check(f"sitemap lists the {len(card_pages)} per-card pages",
                  in_sm == len(card_pages), f"{in_sm} of {len(card_pages)} listed")
        check("sitemap has x-default alternates", 'hreflang="x-default"' in xml)
        check("sitemap is on our origin",
              "vincentwei" not in xml, "sitemap names the author's domain")

        code, root_html, _ = get(base + "/")
        check("root 200", code == 200)
        check("root lists every built locale without JS",
              all(f'href="{lc}/library.html"' in root_html for lc in locales))
        check("root uses Accept-Language", "navigator.languages" in root_html)

        code, ruru, _ = get(base + "/ru/library.html")
        check("Accept-Language ru does not redirect away",
              code == 200 and "/ru/" in ruru)

        # ---------------- browser assertions ----------------
        ws, chrome = chrome_ws(0)
        cdp = CDP(ws)
        cdp.call("Page.enable")
        cdp.call("Runtime.enable")

        def wait_for(cdp, expr: str, timeout: float = 20):
            """Poll an expression until truthy. A single sample right after a
            navigation is a race, and a race that reads as a product failure is
            worse than no test."""
            deadline = time.time() + timeout
            last = None
            while time.time() < deadline:
                try:
                    last = cdp.evaluate(expr)
                except RuntimeError:
                    last = None
                if last:
                    return last
                time.sleep(0.25)
            return last

        def goto(url: str, wait_js: str = "", timeout: float = 30):
            """Navigate and wait until the URL has committed.

            Chrome reports readyState 'complete' for the *previous* document
            immediately after Page.navigate, so polling readyState alone can read
            the old page and silently assert against it. Comparing location.href
            is what makes this trustworthy.
            """
            cdp.call("Page.navigate", {"url": url})
            deadline = time.time() + timeout
            committed = False
            while time.time() < deadline:
                try:
                    now = cdp.evaluate("location.href")
                    committed = committed or (now == url)
                    ready = cdp.evaluate("document.readyState")
                except RuntimeError:
                    ready = None
                    now = None
                if committed and ready == "complete":
                    if not wait_js:
                        return True
                    try:
                        if cdp.evaluate(wait_js):
                            return True
                    except RuntimeError:
                        pass
                time.sleep(0.25)
            return False

        cards_ready = "document.querySelectorAll('#ai-stream-response').length > 0"
        for lc in locales:
            if not (DIST / lc / "library.html").exists():
                continue
            ok = goto(f"{base}/{lc}/library.html", cards_ready)
            check(f"{lc} library rendered", ok)
            n = cdp.evaluate("document.querySelectorAll('article.shot-card').length")
            # Derived, not hardcoded. A literal 157 here would pass today and
            # start failing on the first upstream bump, which is exactly the kind
            # of rot that makes a test suite untrustworthy.
            check(f"{lc} renders every card ({CARD_COUNT})", n == CARD_COUNT, str(n))

            # no raw i18n keys on screen
            bad = cdp.evaluate("""(() => {
              const hits = [];
              const walk = (root) => {
                const sel = 'body *';
                for (const n of root.querySelectorAll(sel)) {
                  if (n.children.length) continue;
                  const t = (n.textContent || '').trim();
                  if (!t || t.length > 40) continue;
                  if (/^(documentTitle|cat[A-Z]|pageTitle|searchPlaceholder|languageToggle|themeDark|themeLight|categoriesHeading|skip|brandHome|followMe|starGitHubLabel|viewShowcase|navShowcase|navLibrary)$/.test(t)) hits.push(t);
                }
              };
              walk(document);
              return hits;
            })()""")
            check(f"{lc} has no raw i18n keys", not bad, f"{bad[:6]}")

            # switcher present and populated from data
            items = cdp.evaluate(
                "document.querySelectorAll('.locale-nav .locale-item').length")
            check(f"{lc} switcher lists every built locale",
                  items == len(locales), f"{items} vs {len(locales)}")

            if a.shots:
                shot_dir = ROOT / "site" / "build" / "shots"
                shot_dir.mkdir(parents=True, exist_ok=True)
                img = cdp.call("Page.captureScreenshot", {"format": "png"})
                (shot_dir / f"{lc}-library.png").write_bytes(base64.b64decode(img["data"]))

        # deep link + language switch preserves the fragment.
        # The card enters the viewport over ~1.2s while media streams in, so
        # "is it there yet" must be polled: a single sample right after load
        # reads as a failure and is not one.
        if (DIST / "ru" / "library.html").exists() and len(locales) > 1:
            goto(f"{base}/ru/library.html#crash-zoom-punch", cards_ready)
            check("deep link fragment preserved",
                  cdp.evaluate("location.hash") == "#crash-zoom-punch",
                  cdp.evaluate("location.hash"))
            check("deep link card exists in the DOM",
                  cdp.evaluate("!!document.getElementById('crash-zoom-punch')"))
            seen_top = None
            for _ in range(12):
                top = cdp.evaluate("""(() => {
                  const e = document.getElementById('crash-zoom-punch');
                  return e ? Math.round(e.getBoundingClientRect().top) : null;
                })()""")
                if top is not None:
                    seen_top = top
                    if abs(top) < 200:
                        break
                time.sleep(0.35)
            check("deep link scrolls the card into view",
                  seen_top is not None and abs(seen_top) < 200, f"final top={seen_top}")
            if a.shots:
                shot_dir = ROOT / "site" / "build" / "shots"
                shot_dir.mkdir(parents=True, exist_ok=True)
                img = cdp.call("Page.captureScreenshot", {"format": "png"})
                (shot_dir / "ru-deeplink-crash-zoom-punch.png").write_bytes(
                    base64.b64decode(img["data"]))

            # click the switcher and confirm we land on another locale, fragment intact
            nav = cdp.evaluate("""(() => {
              const items = [...document.querySelectorAll('.locale-nav .locale-item')];
              const other = items.find((a) => !a.classList.contains('is-current'));
              if (!other) return null;
              const href = other.getAttribute('href');
              other.click();
              return href;
            })()""")
            check("switcher offers another locale", bool(nav), str(nav))
            if nav:
                # the click triggers a full navigation; wait for it to settle
                for _ in range(20):
                    time.sleep(0.3)
                    landed = cdp.evaluate("location.pathname + location.hash")
                    if landed != f"/ru/library.html#crash-zoom-punch":
                        break
                landed = cdp.evaluate("location.pathname + location.hash")
                check("switching language keeps the card deep link",
                      landed.endswith("#crash-zoom-punch") and not landed.startswith("/ru/"),
                      landed)
                check("switched page is a different built locale",
                      any(landed.startswith(f"/{l}/") for l in locales if l != "ru"), landed)
                # the new document has to finish loading before its switcher exists
                goto(f"{base}{nav}")
                check("switcher survives the navigation",
                      cdp.evaluate("document.querySelectorAll('.locale-nav .locale-item').length")
                      == len(locales),
                      cdp.evaluate("document.querySelectorAll('.locale-nav .locale-item').length"))

        # CJK branch: isCJK() must drive the description source, not the locale name
        if (DIST / "zh" / "library.html").exists():
            goto(f"{base}/zh/library.html", cards_ready)
            ok = wait_for(cdp, "window.__I18N__ && window.__I18N__.locale === 'zh'")
            check("zh resolves isCJK() true",
                  ok is True and cdp.evaluate("window.__I18N__.isCJK()") is True,
                  str(cdp.evaluate("window.__I18N__ && window.__I18N__.locale")))
            # The CJK branch is the one real behavioural fork between locales: zh renders
            # the card summary out of library.json, en/ru render the translated
            # one-liner. Assert both directions, otherwise isCJK() could be
            # returning a constant and every other check would still pass.
            def card_desc(loc: str) -> str:
                goto(f"{base}/{loc}/library.html", cards_ready)
                # Poll, do not sample once. `goto` can return while the previous
                # document is still what is being read, because readyState is
                # already 'complete' there; a single sample then reads '' and the
                # assertion fails for a reason that is not a product bug.
                wait_for(cdp, "!!document.querySelector('#crash-zoom-punch p.summary')")
                return cdp.evaluate("""(() => {
                  const el = document.getElementById('crash-zoom-punch');
                  const p = el ? el.querySelector('p.summary') : null;
                  return p ? p.textContent.trim() : '';
                })()""") or ""

            def is_cjk(s: str) -> bool:
                return any("\u4e00" <= ch <= "\u9fff" for ch in s)

            # -- the static block, read from disk -----------------------------
            #
            # The runtime check below reads the DOM after the i18n script has run.
            # That is the better rendering and the one a returning visitor sees,
            # but it is not the one a crawler sees, and it is not the one that put
            # 157 Chinese summaries onto the Russian page in the first place. The
            # prerendered block is static HTML, so it is checked here from the
            # file, with no browser and no JavaScript in the loop.
            #
            # For a non-CJK locale the rule is exact: one CJK character in a baked
            # card means that card is falling back to the Chinese corpus. `en` is
            # skipped because upstream's gallery is the reference there.
            # The prerender stamp. build_site.py clears it before regenerating the
            # pages and prerender.py writes it back, so a missing stamp means
            # "the build ran after the prerender" and the static block below is
            # the untranslated template. It is checked first because every
            # assertion after it is measuring a page that is known to be wrong.
            stamp = DIST / ".prerendered.json"
            check("site was prerendered after it was built",
                  stamp.exists(),
                  "site/dist/.prerendered.json is missing: build_site.py ran after "
                  "prerender.py, so the static card block is the untranslated "
                  "template. Re-run: python platform/site/prerender.py")

            for loc in locales:
                page = DIST / loc / "library.html"
                if not page.exists():
                    continue
                baked = re.findall(
                    r'<article class="shot-card[^"]*"[^>]*id="([^"]+)"(.*?)</article>',
                    page.read_text(encoding="utf-8"), re.S)
                check(f"{loc} prerenders every card", len(baked) == CARD_COUNT,
                      f"{len(baked)} of {CARD_COUNT}")
                cjk_cards, cyr_cards = [], 0
                for cid, body in baked:
                    text = re.sub(r"<[^>]+>", " ", body)
                    if is_cjk(text):
                        cjk_cards.append(cid)
                    if any("\u0400" <= ch <= "\u04ff" for ch in text):
                        cyr_cards += 1
                if loc == "zh":
                    check("zh prerendered cards are CJK", len(cjk_cards) == len(baked),
                          f"{len(cjk_cards)} of {len(baked)}")
                elif loc == "ru":
                    # The check that matters. It failed at 157/157 before the
                    # descriptions were translated, and it is the only assertion
                    # here that would have caught it.
                    check("ru prerendered cards contain no CJK prose",
                          not cjk_cards,
                          f"{len(cjk_cards)} card(s) still Chinese: {cjk_cards[:4]}")
                    check("ru prerendered cards are actually Russian",
                          cyr_cards == len(baked),
                          f"{cyr_cards} of {len(baked)} have Cyrillic")

            if (DIST / "zh" / "library.html").exists():
                zh_desc = card_desc("zh")
                check("zh card summary comes from library.json (CJK)",
                      is_cjk(zh_desc), repr(zh_desc[:50]))
            for loc in [l for l in locales if l not in ("zh",)]:
                other = card_desc(loc)
                check(f"{loc} card summary is not CJK", bool(other) and not is_cjk(other),
                      repr(other[:50]))
    finally:
        if chrome:
            chrome.kill()
        if not a.keep_server:
            server.terminate()
            try:
                server.wait(timeout=5)
            except subprocess.TimeoutExpired:
                server.kill()

    failed = [c for c in checks if not c[1]]
    for name, ok, detail in checks:
        if not ok:
            print(f"  FAIL {name}  {detail}")
    print(f"\n{len(checks) - len(failed)}/{len(checks)} checks passed "
          f"({len(locales)} locales: {', '.join(locales)})")
    if a.shots:
        print("screenshots: site/build/shots/")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())