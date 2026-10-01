"""Exercise every API route, including the read-only guarantee.

    python platform/api/selftest.py

Uses the live server if BASE is set, otherwise starts one on a free port.
Fails loudly: this is the verifier's tool for F020.
"""
from __future__ import annotations

import json
import os
import socket
import subprocess
import sys
import time
import urllib.error
import urllib.request

ROOT = __import__("pathlib").Path(__file__).resolve().parents[2]


def free_port() -> int:
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]
    s.close()
    return p


def start(port: int):
    return subprocess.Popen(
        [sys.executable, str(ROOT / "platform" / "api" / "serve.py"), "--port", str(port)],
        cwd=str(ROOT), stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
        env={**os.environ, "PYTHONIOENCODING": "utf-8"})


def call(base: str, path: str, method: str = "GET"):
    req = urllib.request.Request(base + path, method=method)
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return r.status, json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        try:
            return e.code, json.loads(body)
        except json.JSONDecodeError:
            return e.code, body


def main() -> int:
    base = os.environ.get("BASE")
    proc = None
    if not base:
        port = free_port()
        proc = start(port)
        base = f"http://localhost:{port}"
        for _ in range(50):
            code, _ = call(base, "/health")
            if code == 200:
                break
            time.sleep(0.2)

    failures: list[str] = []
    checks: list[tuple[str, bool, str]] = []

    def check(name: str, ok: bool, detail: str = "") -> None:
        checks.append((name, ok, detail))
        if not ok:
            failures.append(f"{name}: {detail}")

    try:
        code, health = call(base, "/health")
        check("/health 200", code == 200, str(code))
        check("routes listed", len(health.get("endpoints", [])) >= 10)

        code, stats = call(base, "/stats")
        check("/stats 200", code == 200)
        check("stats.cards=157", stats.get("cards") == 157, str(stats.get("cards")))
        check("stats.styles=218", stats.get("styles") == 218, str(stats.get("styles")))
        # motion_params grows whenever the TSX extractor gains a pattern, so
        # assert the floor and the invariant rather than a frozen count.
        check("stats.motion_params >= 1800", stats.get("motion_params", 0) >= 1800,
              str(stats.get("motion_params")))
        check("stats has upstream_sha", bool(stats.get("upstream_sha")))

        code, cards = call(base, "/cards")
        check("/cards 200", code == 200)
        check("/cards returns 157", len(cards.get("items", [])) == 157,
              str(len(cards.get("items", []))))

        code, cam = call(base, "/cards?category=camera")
        items = cam.get("items", [])
        check("/cards?category=camera filters", items and all(i["category"] == "camera" for i in items),
              f"{len(items)} items")

        code, hi = call(base, "/cards?energy=high")
        items = hi.get("items", [])
        check("/cards?energy=high filters", items and all(i["energy"] == "high" for i in items),
              f"{len(items)} items")

        code, short = call(base, "/cards?max_frames=20")
        items = short.get("items", [])
        check("/cards?max_frames filters",
              items and all((i["duration_frames"] or 999) <= 20 for i in items), f"{len(items)}")

        code, zh = call(base, "/cards?q=%E8%BD%AC%E5%9C%BA")   # 转场, 2 chars
        check("/cards?q= 转场 (short, LIKE path)", code == 200 and len(zh.get("items", [])) > 0,
              f"{len(zh.get('items', []))} hits")
        code, zh3 = call(base, "/cards?q=%E8%BD%AC%E5%9C%BA%E7%9A%84")  # 转场的, 3 chars
        check("/cards?q= 转场的 (trigram path)", code == 200 and len(zh3.get("items", [])) > 0,
              f"{len(zh3.get('items', []))} hits")
        code, en = call(base, "/cards?q=spring")
        check("/cards?q=spring finds styles+cards", code == 200 and len(en.get("items", [])) > 0,
              f"{len(en.get('items', []))} hits")

        code, card = call(base, "/cards/crash-zoom-punch")
        check("/cards/{slug} 200", code == 200)
        check("card has 2 styles (directory is authoritative, not library.json)",
              len(card.get("styles", [])) == 2, str([s["key"] for s in card.get("styles", [])]))
        check("card has parameters", len(card.get("parameters", [])) >= 3,
              str(len(card.get("parameters", []))))
        check("card has pitfalls", len(card.get("pitfalls", [])) >= 1)
        check("card energy is high", card.get("energy") == "high", str(card.get("energy")))

        code, miss = call(base, "/cards/no-such-card")
        check("/cards/{unknown} 404", code == 404, str(code))

        code, styles = call(base, "/styles")
        check("/styles 200", code == 200 and len(styles.get("items", [])) == 218,
              str(len(styles.get("items", []))))

        code, style = call(base, "/styles/blur-slide")
        check("/styles/{key} 200", code == 200)
        check("style has motion parameters", len(style.get("parameters", [])) >= 5,
              str(len(style.get("parameters", []))))
        check("style lists easings", isinstance(style.get("easings"), list))

        code, ez = call(base, "/easing")
        check("/easing 200", code == 200 and len(ez.get("items", [])) > 0)
        check("house curve ranked first", ez["items"][0]["spec"] == "bezier(0.3,0,0.2,1)",
              ez["items"][0]["spec"])

        code, rules = call(base, "/rules")
        check("/rules 200", code == 200 and len(rules.get("items", [])) == 27,
              str(len(rules.get("items", []))))
        fams = {r["family"] for r in rules.get("items", [])}
        check("rules cover 5 families", fams == {"R", "Q", "S", "C", "P"}, str(fams))

        code, lic = call(base, "/licenses")
        blocking = {l["subject"] for l in lic.get("items", []) if l["blocking"]}
        check("Remotion marked blocking", any("Remotion" in s for s in blocking), str(blocking))
        check("PolyForm marked blocking", any("talkcraft" in s for s in blocking), str(blocking))

        code, opp = call(base, "/opportunities")
        check("/opportunities 200", code == 200 and len(opp.get("items", [])) == 5,
              str(len(opp.get("items", []))))

        code, cats = call(base, "/categories")
        check("/categories 200", code == 200 and len(cats.get("items", [])) == 10)

        code, loc = call(base, "/locales")
        check("/locales 200", code == 200 and len(loc.get("items", [])) == 9,
              str(len(loc.get("items", []))))

        # read-only guarantee
        for m in ("POST", "PUT", "PATCH", "DELETE"):
            code, _ = call(base, "/stats", m)
            check(f"{m} rejected 405", code == 405, str(code))

        code, _ = call(base, "/nope")
        check("unknown route 404", code == 404, str(code))
    finally:
        if proc:
            proc.terminate()
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()

    passed = sum(1 for _, ok, _ in checks if ok)
    for name, ok, detail in checks:
        if not ok:
            print(f"  FAIL {name}  {detail}")
    print(f"\n{passed}/{len(checks)} checks passed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())