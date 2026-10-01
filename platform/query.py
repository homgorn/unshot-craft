"""Query the shotcraft index from the shell.

    python platform/query.py cards --energy high --category camera
    python platform/query.py search "пружина overshoot"
    python platform/query.py card crash-zoom-punch
    python platform/query.py easing
    python platform/query.py params blur-slide
    python platform/query.py pitfalls --critical
    python platform/query.py rules
    python platform/query.py licenses --blocking
    python platform/query.py opportunities
    python platform/query.py stats

Text output is compact markdown on purpose: these commands are meant to be
pasted into an agent transcript or a spec, not read in a pager.
"""

from __future__ import annotations

import json
import sqlite3
import sys
from pathlib import Path

DB = Path(__file__).resolve().parent / "db" / "shotcraft.db"

ENERGY_RANK = ["low", "low-mid", "mid-low", "mid", "mid-high", "high", "very-high", "peak"]


def table(cur, sql, args=()) -> list[sqlite3.Row]:
    return cur.execute(sql, args).fetchall()


def fmt_md(cur, rows) -> str:
    if not rows:
        return "(none)"
    cols = rows[0].keys()
    out = ["| " + " | ".join(cols) + " |", "|" + "|".join(["---"] * len(cols)) + "|"]
    for r in rows:
        out.append("| " + " | ".join("" if v is None else str(v) for v in r) + " |")
    return "\n".join(out)


def main(argv: list[str]) -> int:
    if not DB.exists():
        print(f"missing {DB}; run platform/ingest/run.py first", file=sys.stderr)
        return 1
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cmd, rest = argv[0], argv[1:]

    def opt(flag, cast=str):
        if flag in rest:
            return cast(rest[rest.index(flag) + 1])
        return None

    if cmd == "cards":
        where, args = ["1=1"], []
        if cat := opt("--category"):
            where.append("c.key=?"); args.append(cat)
        if en := opt("--energy"):
            ranks = [ENERGY_RANK.index(x) for x in en.split(",") if x in ENERGY_RANK]
            where.append(f"e.rank IN ({','.join('?' * len(ranks))})"); args += ranks
        if mx := opt("--max-frames", int):
            where.append("s.duration_frames<=?"); args.append(mx)
        if mn := opt("--min-frames", int):
            where.append("s.duration_frames>=?"); args.append(mn)
        rows = table(cur, f"""SELECT s.name, c.key category, COALESCE(e.label_zh, s.energy_text) energy,
            s.duration_frames frames, s.summary_zh summary
            FROM shot_card s JOIN category c ON c.id=s.category_id
            LEFT JOIN energy_level e ON e.id=s.energy_level_id
            WHERE {' AND '.join(where)} ORDER BY e.rank DESC NULLS LAST, s.duration_frames, s.name""", args)
        print(fmt_md(cur, rows))

    elif cmd == "search":
        # Search cascade, because no single index covers this corpus:
        #   unicode61  — word-level; the only one that works for 1-2 char CJK
        #   trigram    — substring in any script, but needs >= 3 characters
        #   LIKE       — the catch-all for anything shorter
        # NOTE: when the FTS table is aliased, MATCH must target the *alias*.
        q = " ".join(rest).strip() or "*"
        if q == "*":
            rows = table(cur, """SELECT s.name card, COALESCE(e.label_zh, s.energy_text) energy,
                    s.duration_frames frames, '' hit FROM shot_card s
                    LEFT JOIN energy_level e ON e.id=s.energy_level_id LIMIT 25""")
        else:
            cols = "s.name, COALESCE(e.label_zh, s.energy_text), s.duration_frames"
            # FTS5 must be matched by table name, so hits are resolved in a CTE
            # first; that also keeps ORDER BY rank and snippet() available.
            uni = table(cur, f"""WITH hits AS (
                    SELECT rowid AS rid, snippet(search_fts,1,'[',']','…',10) AS hit
                    FROM search_fts WHERE search_fts MATCH ?)
                SELECT {cols}, hits.hit FROM hits
                JOIN shot_card s ON s.id=hits.rid
                LEFT JOIN energy_level e ON e.id=s.energy_level_id LIMIT 25""", (f'"{q}"',))
            rows = uni
            if len(q) >= 3:
                tri = table(cur, f"""WITH hits AS (
                        SELECT rowid AS rid, snippet(search_fts_trgm,1,'[',']','…',10) AS hit
                        FROM search_fts_trgm WHERE search_fts_trgm MATCH ?)
                    SELECT {cols}, hits.hit FROM hits
                    JOIN shot_card s ON s.id=hits.rid
                    LEFT JOIN energy_level e ON e.id=s.energy_level_id LIMIT 25""", (f'"{q}"',))
                seen = {r[0] for r in rows}
                rows += [r for r in tri if r[0] not in seen]
            if not rows:
                rows = table(cur, """SELECT name, '', duration_frames, '[like]'
                    FROM shot_card WHERE name LIKE '%'||?||'%'
                       OR summary_zh LIKE '%'||?||'%' OR use_zh LIKE '%'||?||'%'
                       OR intention_zh LIKE '%'||?||'%' LIMIT 25""", (q, q, q, q))
            if not rows:
                rows = table(cur, """SELECT c.name, '', '', '[style]'
                    FROM style s JOIN shot_card c ON c.id=s.card_id
                    WHERE s.key LIKE '%'||?||'%' LIMIT 25""", (q,))
        print(fmt_md(cur, rows[:25]))

    elif cmd == "card":
        name = rest[0] if rest else ""
        rows = table(cur, """SELECT s.name, c.label_en category, COALESCE(e.label_zh, s.energy_text) energy,
            s.duration_text duration, s.summary_zh summary, s.use_zh use_when, s.intention_zh intention,
            s.source_path source FROM shot_card s JOIN category c ON c.id=s.category_id
            LEFT JOIN energy_level e ON e.id=s.energy_level_id WHERE s.name=?""", (name,))
        print(fmt_md(cur, rows))
        print("\n**styles**")
        print(fmt_md(cur, table(cur, """SELECT v.letter, st.key, st.demo_path, st.duration_frames frames,
            st.family FROM card_variant v JOIN style st ON st.id=v.style_id
            JOIN shot_card s ON s.id=v.card_id WHERE s.name=? ORDER BY st.key""", (name,))))
        print("\n**parameters**")
        print(fmt_md(cur, table(cur, """SELECT p.param_key, p.typical_value, p.feel_note
            FROM card_param p JOIN shot_card s ON s.id=p.card_id WHERE s.name=? ORDER BY p.ordinal""", (name,))))
        print("\n**pitfalls**")
        print(fmt_md(cur, table(cur, """SELECT p.is_critical critical, p.rule_refs rules, p.text
            FROM card_pitfall p JOIN shot_card s ON s.id=p.card_id WHERE s.name=? ORDER BY p.ordinal""", (name,))))

    elif cmd == "easing":
        print(fmt_md(cur, table(cur, """SELECT spec, usage_count styles, overshoot FROM easing_curve
            ORDER BY usage_count DESC LIMIT 25""")))

    elif cmd == "params":
        key = rest[0] if rest else ""
        print(fmt_md(cur, table(cur, """SELECT p.kind, p.name, p.args_json, p.line_no, p.raw
            FROM motion_param p JOIN style s ON s.id=p.style_id WHERE s.key=? ORDER BY p.line_no""", (key,))))

    elif cmd == "pitfalls":
        crit = "--critical" in rest
        rows = table(cur, f"""SELECT s.name card, p.rule_refs rules, p.text FROM card_pitfall p
            JOIN shot_card s ON s.id=p.card_id {'WHERE p.is_critical=1' if crit else ''}
            ORDER BY p.is_critical DESC, s.name LIMIT 60""")
        print(fmt_md(cur, rows))

    elif cmd == "rules":
        print(fmt_md(cur, table(cur, """SELECT family||rule_id id, substr(body,1,220) body FROM rule
            ORDER BY family, CAST(substr(rule_id,2) AS INTEGER)""")))

    elif cmd == "licenses":
        rows = table(cur, """SELECT subject, spdx, commercial_use, blocking, obligation
            FROM license_registry ORDER BY blocking DESC, subject""")
        print(fmt_md(cur, rows))

    elif cmd == "opportunities":
        print(fmt_md(cur, table(cur, """SELECT key, revenue_model model, effort, time_to_first_revenue
            first_revenue, status FROM opportunity ORDER BY time_to_first_revenue""")))

    elif cmd == "stats":
        print(json.dumps({r[0]: r[1] for r in cur.execute(
            "SELECT 'cards',COUNT(*) FROM shot_card UNION ALL SELECT 'styles',COUNT(*) FROM style "
            "UNION ALL SELECT 'card_params',COUNT(*) FROM card_param UNION ALL SELECT 'pitfalls',COUNT(*) FROM card_pitfall "
            "UNION ALL SELECT 'motion_params',COUNT(*) FROM motion_param UNION ALL SELECT 'rules',COUNT(*) FROM rule "
            "UNION ALL SELECT 'sfx',COUNT(*) FROM audio_asset UNION ALL SELECT 'translations',COUNT(*) FROM translation "
            "UNION ALL SELECT 'gallery_orphans',COUNT(*) FROM gallery_style")}, indent=2))

    else:
        print(__doc__)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))