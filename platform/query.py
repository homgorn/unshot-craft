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

    elif cmd == "technique":
        # Second corpus (ADR 0007). Reports honestly when data/cinematic/ has
        # not been ingested rather than pretending the command does not exist.
        if not table(cur, "SELECT name FROM sqlite_master WHERE type='table' AND name='cinematic_technique'"):
            print("catalog corpus is not ingested (WARN, not an error):\n"
                  "  platform/catalog/schema.sql was not applied. Run platform/ingest/run.py.")
            return 0
        n = cur.execute("SELECT COUNT(*) FROM cinematic_technique").fetchone()[0]
        if n == 0:
            print("catalog corpus is empty (WARN, not an error):\n"
                  "  data/cinematic/ has no technique files yet. See data/cinematic/README.md.")
            return 0
        where, args = ["1=1"], []
        if cat := opt("--category"):
            where.append("cc.key=?"); args.append(cat)
        if lvl := opt("--level"):
            where.append("t.level=?"); args.append(lvl)
        if (tname := opt("--name")):
            where.append("t.name=?"); args.append(tname)
        rows = table(cur, f"""SELECT t.name, cc.key category, t.level,
            (SELECT COUNT(*) FROM technique_motion m WHERE m.technique_id=t.id) motions,
            (SELECT COUNT(*) FROM technique_tool_param p WHERE p.technique_id=t.id AND p.params IS NOT NULL) cells,
            (SELECT COUNT(*) FROM technique_tool_param p WHERE p.technique_id=t.id AND p.tested=1) tested
            FROM cinematic_technique t JOIN cinematic_category cc ON cc.id=t.category_id
            WHERE {' AND '.join(where)} ORDER BY cc.sort_order, t.name""", args)
        print(fmt_md(cur, rows))

    elif cmd == "technique-detail":
        slug = rest[0] if rest else ""
        t = table(cur, """SELECT t.name, t.title, cc.key category, t.level,
            t.lede_text, t.when_to_use_text, t.directing_text, t.image_url, t.video_url,
            t.source_path FROM cinematic_technique t
            JOIN cinematic_category cc ON cc.id=t.category_id WHERE t.name=?""", (slug,))
        if not t:
            print(f"unknown technique: {slug}")
            return 1
        t = t[0]
        print(f"# {t['title']}  ({t['name']})")
        print(f"category={t['category']}  level={t['level']}  source={t['source_path']}")
        print("\n## Prompt (verbatim, [Subject] intact)")
        print(table(cur, "SELECT prompt_text FROM cinematic_technique WHERE name=?", (slug,))[0]["prompt_text"])
        for key, label in (("lede_text", "Lede"), ("when_to_use_text", "When to use"),
                           ("directing_text", "Directing the AI")):
            if t[key]:
                print(f"\n## {label}\n{t[key]}")
        print("\n## Common mistakes")
        print(fmt_md(cur, table(cur, "SELECT ord, text FROM technique_section WHERE technique_id="
                                      "(SELECT id FROM cinematic_technique WHERE name=?) "
                                      "AND kind='common_mistake' ORDER BY ord", (slug,))))
        print("\n## Cross-tool matrix")
        print(fmt_md(cur, table(cur, """SELECT a.key tool, a.label, p.params, p.version_tag,
            p.tested, CASE WHEN p.full_prompt IS NULL THEN 'null' ELSE 'composed' END full_prompt
            FROM technique_tool_param p JOIN ai_tool a ON a.id=p.tool_id
            WHERE p.technique_id=(SELECT id FROM cinematic_technique WHERE name=?)
            ORDER BY a.key""", (slug,))))
        print("\n## Shot cards that can realize it")
        print(fmt_md(cur, table(cur, """SELECT m.kind, s.key style, sc.name card, sc.category,
            sc.duration_frames frames, e.label_zh energy FROM technique_motion m
            JOIN style s ON s.id=m.style_id
            LEFT JOIN shot_card sc ON sc.id=s.card_id
            LEFT JOIN energy_level e ON e.id=sc.energy_level_id
            WHERE m.technique_id=(SELECT id FROM cinematic_technique WHERE name=?)
            ORDER BY sc.energy_rank DESC NULLS LAST, s.key""", (slug,))))

    elif cmd == "optimize":
        # F073: one call, one question — "given a technique and a tool, what do I
        # send, and what motion card carries it?" The honest answer when a cell is
        # untested or empty is to say so, not to compose a plausible prompt.
        slug = opt("--technique") or (rest[0] if rest else "")
        tool = opt("--tool") or (rest[1] if len(rest) > 1 else "")
        if not slug:
            print("usage: query.py optimize <slug> --tool <key>")
            print("tools: mj61, runway_gen3, veo2, kling15, luma, pika15, sora")
            return 2
        t = table(cur, """SELECT t.id, t.name, t.title, t.prompt_text FROM cinematic_technique t
                          WHERE t.name=?""", (slug,))
        if not t:
            print(f"unknown technique: {slug}")
            return 1
        t = t[0]
        print(f"{t['title']}  ({t['name']})")
        if not tool:
            rows = table(cur, """SELECT a.key, p.params, p.tested FROM technique_tool_param p
                                 JOIN ai_tool a ON a.id=p.tool_id WHERE p.technique_id=?
                                 ORDER BY a.key""", (t["id"],))
            print(fmt_md(cur, rows))
            print("\nre-run with --tool <key> for one tool")
            return 0
        cell = table(cur, """SELECT a.key, a.label, a.param_style, p.params, p.full_prompt,
                                    p.version_tag, p.tested, p.tested_at
                             FROM technique_tool_param p JOIN ai_tool a ON a.id=p.tool_id
                             WHERE p.technique_id=? AND a.key=?""", (t["id"], tool))
        if not cell:
            print(f"no matrix row for {tool} on {slug}: this tool has not been researched "
                  f"for this technique (null, not a guess)")
            return 1
        c0 = cell[0]
        print(f"tool      : {c0['label']} ({c0['param_style']})")
        print(f"version   : {c0['version_tag'] or 'unstated'}")
        if c0["params"]:
            print(f"params    : {c0['params']}")
            print(f"tested    : {'yes, ' + str(c0['tested_at']) if c0['tested'] else 'NO — untested'}")
            print("\n## Send this")
            print(c0["full_prompt"])
        else:
            print("params    : null")
            print("\nThis cell is empty on purpose: an untested tool parameter is an "
                  "untested claim.\nUse the base prompt below and record what you change.")
            print("\n## Base prompt (verbatim)")
            print(t["prompt_text"])
        print("\n## Carry it with")
        print(fmt_md(cur, table(cur, """SELECT m.kind, s.key style, sc.name card, sc.duration_frames frames
                                         FROM technique_motion m JOIN style s ON s.id=m.style_id
                                         LEFT JOIN shot_card sc ON sc.id=s.card_id
                                         WHERE m.technique_id=? ORDER BY s.key""", (t["id"],))))

    elif cmd == "stats":
        print(json.dumps({r[0]: r[1] for r in cur.execute(
            "SELECT 'cards',COUNT(*) FROM shot_card UNION ALL SELECT 'styles',COUNT(*) FROM style "
            "UNION ALL SELECT 'card_params',COUNT(*) FROM card_param UNION ALL SELECT 'pitfalls',COUNT(*) FROM card_pitfall "
            "UNION ALL SELECT 'motion_params',COUNT(*) FROM motion_param UNION ALL SELECT 'rules',COUNT(*) FROM rule "
            "UNION ALL SELECT 'sfx',COUNT(*) FROM audio_asset UNION ALL SELECT 'translations',COUNT(*) FROM translation "
            "UNION ALL SELECT 'gallery_orphans',COUNT(*) FROM gallery_style")},
          indent=2))
        # Second corpus: reported separately so an empty catalog can never be
        # mistaken for a complete one (ADR 0007).
        has = table(cur, "SELECT name FROM sqlite_master WHERE type='table' AND name='cinematic_technique'")
        if not has:
            print("catalog: schema not applied (WARN)")
            return 0
        n = cur.execute("SELECT COUNT(*) FROM cinematic_technique").fetchone()[0]
        if n == 0:
            print("catalog: data/cinematic/ is empty (WARN)")
            return 0
        row = cur.execute("""SELECT SUM(params IS NOT NULL), SUM(tested=1), SUM(params IS NULL),
                                    COUNT(*) FROM technique_tool_param""").fetchone()
        print(f"techniques        : {n}")
        print(f"cross-tool cells  : filled={row[0] or 0} tested={row[1] or 0} null={row[2] or 0} of {row[3]} listed")
        print(f"motion pairings   : {cur.execute('SELECT COUNT(*) FROM technique_motion').fetchone()[0]}")
        print(f"  categories      : {cur.execute('SELECT COUNT(DISTINCT category_id) FROM cinematic_technique').fetchone()[0]}/7")

    else:
        print(__doc__)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))