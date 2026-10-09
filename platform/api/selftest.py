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

# Counts derived from the index under test. Hardcoded literals here would pass
# today and fail on the first upstream bump for the wrong reason, which is the
# difference between a test and a snapshot.
import json as _json
import sqlite3 as _sq

_conn = _sq.connect(f"file:{(ROOT / 'platform' / 'db' / 'shotcraft.db').as_posix()}?mode=ro",
                    uri=True)
_q = lambda sql: _conn.execute(sql).fetchone()[0]
CARD_COUNT = _q("SELECT COUNT(*) FROM shot_card")
STYLE_COUNT = _q("SELECT COUNT(*) FROM style")
RULE_COUNT = _q("SELECT COUNT(*) FROM rule")
LOCALE_COUNT = _q("SELECT COUNT(*) FROM locale")
CATEGORY_COUNT = _q("SELECT COUNT(*) FROM category")
PARAM_COUNT = _q("SELECT COUNT(*) FROM card_param")
MOTION_PARAM_COUNT = _q("SELECT COUNT(*) FROM motion_param")
TECHNIQUE_COUNT = _q("SELECT COUNT(*) FROM cinematic_technique")
TOOL_COUNT = _q("SELECT COUNT(*) FROM ai_tool")
_conn.close()


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

    # ------------------------------------------------------------------ F073
    # The optimizer's whole contract is that an untested cell cannot be mistaken
    # for a ready one, so these assertions are about the *shape* of the answer,
    # not just that a route exists.
    code, tech = call(base, "/techniques")
    check("/techniques 200", code == 200, str(code))
    items = tech.get("items", []) if isinstance(tech, dict) else []
    check("/techniques returns the whole catalog", len(items) == TECHNIQUE_COUNT,
          f"{len(items)} vs {TECHNIQUE_COUNT}")

    code, opt = call(base, "/optimize/dolly-shot")
    check("/optimize/{slug} 200", code == 200, str(code))
    check("/optimize returns the verbatim prompt with [Subject]",
          "[Subject]" in (opt.get("prompt") or ""), repr((opt.get("prompt") or "")[:40]))
    cells = opt.get("tool_params", {})
    check(f"/optimize returns all {TOOL_COUNT} tools", len(cells) == TOOL_COUNT,
          f"{len(cells)}")
    check("every cell carries an explicit tested flag",
          all(isinstance(v.get("tested"), bool) for v in cells.values()),
          "a cell without the flag is indistinguishable from a ready one")
    check("tested:false never hides a parameter",
          all(v.get("params") is None or v.get("tested") is False or v.get("tested_at")
              for v in cells.values()),
          "a parameter marked tested has no tested_at to back it")
    check("/optimize reports how many cells are tested",
          opt.get("summary", {}).get("tested") == 0,
          f"tested={opt.get('summary', {}).get('tested')}, expected 0 (ADR 0007)")
    check("/optimize summary adds up",
          opt.get("summary", {}).get("with_params", 0)
          + opt.get("summary", {}).get("null", 0) == TOOL_COUNT,
          str(opt.get("summary")))
    mot = opt.get("motion_pairings", [])
    check("/optimize returns declared motion pairings", len(mot) > 0, str(len(mot)))
    check("every pairing names a real shot card",
          all(m.get("card") for m in mot), "a pairing points at no card")

    code, one = call(base, "/optimize/dolly-shot?tool=mj61")
    check("/optimize?tool= restricts to one", code == 200 and len(one.get("tool_params", {})) == 1,
          str(code))
    code, bogus = call(base, "/optimize/dolly-shot?tool=midjouney")
    check("/optimize?tool=unknown 404 with the key list",
          code == 404 and "known_tools" in bogus, str(code))
    code, miss = call(base, "/optimize/no-such-technique")
    check("/optimize/{unknown} 404", code == 404, str(code))

    try:
        code, health = call(base, "/health")
        check("/health 200", code == 200, str(code))
        check("routes listed", len(health.get("endpoints", [])) >= 10)

        code, stats = call(base, "/stats")
        check("/stats 200", code == 200)
        check(f"stats.cards={CARD_COUNT}", stats.get("cards") == CARD_COUNT,
              str(stats.get("cards")))
        check(f"stats.styles={STYLE_COUNT}", stats.get("styles") == STYLE_COUNT,
              str(stats.get("styles")))
        check(f"stats.motion_params={MOTION_PARAM_COUNT}",
              stats.get("motion_params") == MOTION_PARAM_COUNT,
              str(stats.get("motion_params")))
        check("stats has upstream_sha", bool(stats.get("upstream_sha")))

        code, cards = call(base, "/cards")
        check("/cards 200", code == 200)
        check(f"/cards returns all {CARD_COUNT}",
              len(cards.get("items", [])) == CARD_COUNT,
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
        check(f"/styles returns all {STYLE_COUNT}",
              code == 200 and len(styles.get("items", [])) == STYLE_COUNT,
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
        check(f"/rules returns all {RULE_COUNT}",
              code == 200 and len(rules.get("items", [])) == RULE_COUNT,
              str(len(rules.get("items", []))))
        fams = {r["family"] for r in rules.get("items", [])}
        check("rules cover 5 families", fams == {"R", "Q", "S", "C", "P"}, str(fams))

        code, lic = call(base, "/licenses")
        blocking = {l["subject"] for l in lic.get("items", []) if l["blocking"]}
        # Remotion is NOT blocking: corrected 2026-10-02 in ingest/run.py
        # (LICENSE_ROWS) -- the paid tier binds companies above three people,
        # this repo is rendered by an individual, so the free tier applies.
        # `blocking` is about the code; the tier is a pricing question at
        # delivery time. Assert the corrected row, not the old refusal.
        by_subject = {l["subject"]: l for l in lic.get("items", [])}
        rem = by_subject.get("Remotion (render engine)", {})
        check("Remotion free-for-individuals, not blocking",
              rem.get("blocking") in (0, False)
              and rem.get("commercial_use") == "free-for-individuals",
              str(rem))
        check("PolyForm marked blocking", any("talkcraft" in s for s in blocking), str(blocking))

        code, opp = call(base, "/opportunities")
        check("/opportunities 200", code == 200 and len(opp.get("items", [])) == 5,
              str(len(opp.get("items", []))))

        code, cats = call(base, "/categories")
        check(f"/categories returns all {CATEGORY_COUNT}",
              code == 200 and len(cats.get("items", [])) == CATEGORY_COUNT,
              str(len(cats.get("items", []))))

        code, loc = call(base, "/locales")
        check(f"/locales returns all {LOCALE_COUNT}",
              code == 200 and len(loc.get("items", [])) == LOCALE_COUNT,
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