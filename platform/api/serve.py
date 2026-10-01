"""F020: a read-only HTTP API over the index.

    python platform/api/serve.py --port 8080

Serves the contract in wiki/api/openapi.json. Read-only by construction: the
route table below has no verb other than GET, and the SQLite connection is opened
read-only (`file:...?mode=ro`), so even a bug cannot mutate the index.

This exists because the same index has four consumers and only one of them is a
Python script: the site (build time), the wiki (build time), an agent CLI, and —
once there is traffic — something in a browser. A browser gets JSON over HTTP.

No framework. `http.server` is in the standard library and this is 10 endpoints.
"""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parents[2]
DB = ROOT / "platform" / "db" / "shotcraft.db"
OPENAPI = ROOT / "wiki" / "api" / "openapi.json"

ENERGY_RANK = ["low", "low-mid", "mid-low", "mid", "mid-high", "high", "very-high", "peak"]


def rows(cur, sql, args=()) -> list[dict]:
    cur.row_factory = sqlite3.Row
    return [dict(r) for r in cur.execute(sql, args).fetchall()]


def card_json(cur, name: str) -> dict | None:
    card = rows(cur, """
        SELECT s.name, s.summary_zh, s.use_zh, s.duration_text, s.duration_frames,
               s.energy_text, s.intention_zh, s.source_path,
               c.key AS category, c.label_en AS category_en, c.label_zh AS category_zh,
               e.key AS energy, e.label_zh AS energy_zh, e.rank AS energy_rank,
               s.updated_at, s.added_at
        FROM shot_card s
        JOIN category c ON c.id = s.category_id
        LEFT JOIN energy_level e ON e.id = s.energy_level_id
        WHERE s.name = ?""", (name,))
    if not card:
        return None
    card = card[0]
    card["tags"] = [r["key"] for r in rows(cur, """
        SELECT c.key FROM shot_card_tag t JOIN category c ON c.id = t.category_id
        WHERE t.card_id = (SELECT id FROM shot_card WHERE name = ?)""", (name,))]
    card["styles"] = rows(cur, """
        SELECT st.key, st.demo_path, st.component_name, st.duration_frames, st.family,
               st.gallery_style_key
        FROM card_variant v JOIN style st ON st.id = v.style_id
        JOIN shot_card s ON s.id = v.card_id WHERE s.name = ? ORDER BY st.key""", (name,))
    card["parameters"] = rows(cur, """
        SELECT p.param_key, p.typical_value, p.feel_note
        FROM card_param p JOIN shot_card s ON s.id = p.card_id
        WHERE s.name = ? ORDER BY p.ordinal""", (name,))
    card["pitfalls"] = rows(cur, """
        SELECT p.text, p.is_critical, p.rule_refs
        FROM card_pitfall p JOIN shot_card s ON s.id = p.card_id
        WHERE s.name = ? ORDER BY p.ordinal""", (name,))
    return card


def handle(conn, path: str, q: dict) -> tuple[int, object]:
    cur = conn.cursor()

    if path == "/stats":
        s = {r["k"]: r["n"] for r in rows(cur, """
            SELECT 'cards' k, COUNT(*) n FROM shot_card
            UNION ALL SELECT 'styles', COUNT(*) FROM style
            UNION ALL SELECT 'card_params', COUNT(*) FROM card_param
            UNION ALL SELECT 'pitfalls', COUNT(*) FROM card_pitfall
            UNION ALL SELECT 'motion_params', COUNT(*) FROM motion_param
            UNION ALL SELECT 'easing_curves', COUNT(*) FROM easing_curve
            UNION ALL SELECT 'rules', COUNT(*) FROM rule
            UNION ALL SELECT 'sfx', COUNT(*) FROM audio_asset
            UNION ALL SELECT 'translations', COUNT(*) FROM translation
            UNION ALL SELECT 'gallery_orphans', COUNT(*) FROM gallery_style""")}
        s["upstream_sha"] = rows(cur, "SELECT head_sha FROM source_repo LIMIT 1")[0]["head_sha"]
        return 200, s

    if path == "/cards":
        where, args = ["1=1"], []
        if cat := q.get("category", [None])[0]:
            where.append("c.key = ?"); args.append(cat)
        if en := q.get("energy", [None])[0]:
            keys = [k for k in en.split(",") if k in ENERGY_RANK]
            if keys:
                where.append(f"e.key IN ({','.join('?' * len(keys))})"); args += keys
        if (mx := q.get("max_frames", [None])[0]) and mx.isdigit():
            where.append("s.duration_frames <= ?"); args.append(int(mx))
        if (mn := q.get("min_frames", [None])[0]) and mn.isdigit():
            where.append("s.duration_frames >= ?"); args.append(int(mn))
        limit = min(int(q.get("limit", ["200"])[0] or 200), 500)
        term = q.get("q", [None])[0]
        if term:
            sql = """WITH hits AS (SELECT rowid rid FROM search_fts_trgm WHERE search_fts_trgm MATCH ?)
                    SELECT s.name, c.key AS category, e.key AS energy, s.duration_frames,
                           s.summary_zh AS summary
                    FROM hits JOIN shot_card s ON s.id = hits.rid
                    JOIN category c ON c.id = s.category_id
                    LEFT JOIN energy_level e ON e.id = s.energy_level_id LIMIT ?"""
            args2 = [f'"{term}"', limit] if len(term) >= 3 else [limit]
            if len(term) < 3:
                sql = """SELECT s.name, c.key AS category, e.key AS energy, s.duration_frames,
                                s.summary_zh AS summary FROM shot_card s
                         JOIN category c ON c.id = s.category_id
                         LEFT JOIN energy_level e ON e.id = s.energy_level_id
                         WHERE s.name LIKE ? OR s.summary_zh LIKE ? OR s.use_zh LIKE ?
                         LIMIT ?"""
                args2 = [f"%{term}%", f"%{term}%", f"%{term}%", limit]
            return 200, {"items": rows(cur, sql, args2)}
        return 200, {"items": rows(cur, f"""
            SELECT s.name, c.key AS category, e.key AS energy, s.duration_frames,
                   s.summary_zh AS summary
            FROM shot_card s JOIN category c ON c.id = s.category_id
            LEFT JOIN energy_level e ON e.id = s.energy_level_id
            WHERE {' AND '.join(where)}
            ORDER BY e.rank DESC NULLS LAST, s.name LIMIT ?""", args + [limit])}

    m = re.fullmatch(r"/cards/([a-z0-9\-]+)", path)
    if m:
        card = card_json(cur, m.group(1))
        return (200, card) if card else (404, {"error": f"unknown card: {m.group(1)}"})

    if path == "/styles":
        return 200, {"items": rows(cur, """
            SELECT st.key, c.key AS category, sc.name AS card, st.demo_path,
                   st.duration_frames, st.family, st.gallery_style_key
            FROM style st LEFT JOIN category c ON c.id = st.category_id
            LEFT JOIN shot_card sc ON sc.id = st.card_id ORDER BY st.key LIMIT ?""",
                         (min(int(q.get("limit", ["300"])[0] or 300), 500),))}

    m = re.fullmatch(r"/styles/([a-z0-9\-]+)", path)
    if m:
        key = m.group(1)
        found = rows(cur, "SELECT * FROM style WHERE key = ?", (key,))
        if not found:
            return 404, {"error": f"unknown style: {key}"}
        style = found[0]
        style["parameters"] = rows(cur, """
            SELECT kind, name, args_json, detail, line_no FROM motion_param
            WHERE style_id = (SELECT id FROM style WHERE key = ?) ORDER BY line_no""", (key,))
        style["easings"] = [r["spec"] for r in rows(cur, """
            SELECT e.spec FROM style_easing se JOIN easing_curve e ON e.id = se.easing_id
            WHERE se.style_id = (SELECT id FROM style WHERE key = ?) ORDER BY e.usage_count DESC""", (key,))]
        return 200, style

    if path == "/easing":
        return 200, {"items": rows(cur, """
            SELECT spec, usage_count, overshoot FROM easing_curve
            ORDER BY usage_count DESC LIMIT ?""",
                         (min(int(q.get("limit", ["50"])[0] or 50), 200),))}

    if path == "/rules":
        return 200, {"items": rows(cur, """
            SELECT family, rule_id, title, body, check_question FROM rule
            ORDER BY family, CAST(SUBSTR(rule_id, 2) AS INTEGER)""")}

    if path == "/licenses":
        return 200, {"items": rows(cur, """
            SELECT subject, spdx, url, commercial_use, blocking, obligation
            FROM license_registry ORDER BY blocking DESC, subject""")}

    if path == "/opportunities":
        return 200, {"items": rows(cur, """
            SELECT key, title, thesis, revenue_model, effort, time_to_first_revenue,
                   evidence, status FROM opportunity ORDER BY time_to_first_revenue""")}

    if path == "/categories":
        return 200, {"items": rows(cur, """
            SELECT key, label_en, label_zh, label_ru, card_count
            FROM category ORDER BY order_idx""")}

    if path == "/locales":
        return 200, {"items": rows(cur, """
            SELECT code, bcp47, name_en, native_name, status,
                   (SELECT COUNT(*) FROM translation t WHERE t.locale_id = locale.id) AS strings
            FROM locale ORDER BY id""")}

    if path == "/openapi.json":
        if OPENAPI.exists():
            return 200, json.loads(OPENAPI.read_text(encoding="utf-8"))
        return 404, {"error": "run platform/wiki/build_wiki.py first"}

    if path in ("/", "/health"):
        return 200, {"ok": True, "docs": "/openapi.json", "endpoints": [
            "/stats", "/cards", "/cards/{slug}", "/styles", "/styles/{key}",
            "/easing", "/rules", "/licenses", "/opportunities", "/categories", "/locales"]}

    return 404, {"error": f"no route: {path}"}


class Handler(BaseHTTPRequestHandler):
    conn: sqlite3.Connection

    def _send(self, code: int, payload: object) -> None:
        body = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "public, max-age=300")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:                      # noqa: N802
        u = urlparse(self.path)
        try:
            code, payload = handle(Handler.conn, u.path, parse_qs(u.query))
        except Exception as exc:                   # noqa: BLE001
            code, payload = 500, {"error": str(exc)}
        self._send(code, payload)

    def _reject(self) -> None:
        self._send(405, {"error": "read-only API", "allow": "GET"})

    do_POST = do_PUT = do_PATCH = do_DELETE = _reject  # noqa: N815

    def log_message(self, fmt, *args):
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8080)
    ap.add_argument("--db", default=str(DB))
    a = ap.parse_args()
    if not Path(a.db).exists():
        raise SystemExit(f"missing {a.db}; run platform/ingest/run.py first")
    # read-only connection: the index cannot be mutated through this process
    Handler.conn = sqlite3.connect(f"file:{Path(a.db).as_posix()}?mode=ro", uri=True,
                                   check_same_thread=False)
    srv = ThreadingHTTPServer(("127.0.0.1", a.port), Handler)
    print(f"shotcraft index API on http://localhost:{a.port} (read-only)", flush=True)
    srv.serve_forever()
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())