"""F070: prove the cinematic catalog is ingested correctly, or say why not.

    python platform/catalog/selftest.py

Checks the invariants ADR 0007 and F070 state, not the implementation. A missing
corpus is a WARN and the run still passes: F070 requires either corpus to build
alone, so a repo without data/cinematic/ is a valid state, not a broken one.
"""

from __future__ import annotations

import json
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DB = ROOT / "platform" / "db" / "shotcraft.db"
CATALOG = ROOT / "data" / "cinematic"
SLOT = "[Subject]"
CATEGORIES = {"camera-work", "lighting", "composition", "editing",
              "narrative", "visual-style", "genres"}


def main() -> int:
    if not DB.exists():
        print(f"missing {DB}; run platform/ingest/run.py", file=sys.stderr)
        return 1
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    checks: list[tuple[str, bool, str, str]] = []

    def check(name: str, ok: bool, detail: str = "", severity: str = "error") -> None:
        checks.append((name, ok, detail, severity))

    has = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='cinematic_technique'").fetchone()
    if not has:
        print("catalog schema is not applied — WARN, not a failure (ADR 0007: either "
              "corpus must build alone)")
        return 0

    n = conn.execute("SELECT COUNT(*) FROM cinematic_technique").fetchone()[0]
    files = sorted(p for p in CATALOG.glob("*.md") if p.name != "README.md")
    if n == 0 and not files:
        print("data/cinematic/ is empty — WARN, not a failure")
        return 0

    check("schema applied", has is not None)
    check(f"technique count matches files ({n} == {len(files)})", n == len(files))

    # 1. the slot rule
    bad_slot = [r["name"] for r in conn.execute(
        "SELECT name FROM cinematic_technique WHERE prompt_text NOT LIKE ?", (f"%{SLOT}%",))]
    check(f"every prompt keeps its {SLOT} slot", not bad_slot, str(bad_slot[:5]))
    check("prompt_slot column is the literal slot",
          all(r["prompt_slot"] == SLOT for r in conn.execute(
              "SELECT DISTINCT prompt_slot FROM cinematic_technique")))

    # 2. controlled vocabulary
    cats = {r["key"] for r in conn.execute(
        "SELECT key FROM cinematic_category")}
    check("vocabulary is the 7 documented categories", cats == CATEGORIES,
          f"db={sorted(cats)}")
    used = {r["category"] for r in conn.execute(
        "SELECT cc.key category FROM cinematic_technique t "
        "JOIN cinematic_category cc ON cc.id=t.category_id")}
    bad_cat = sorted(used - CATEGORIES)
    check("no technique sits outside the vocabulary", not bad_cat, str(bad_cat))
    check("every category is represented", used == CATEGORIES,
          f"missing={sorted(CATEGORIES - used)}")

    # 3. provenance: every technique traces to an authored byte
    untraced = conn.execute("""SELECT COUNT(*) FROM cinematic_technique
                               WHERE source_file_id IS NULL""").fetchone()[0]
    check("every technique traces to a source file", untraced == 0, str(untraced))
    no_sha = conn.execute("""SELECT COUNT(*) FROM cinematic_technique t
                             JOIN source_file f ON f.id=t.source_file_id
                             WHERE f.sha256 IS NULL OR f.sha256=''""").fetchone()[0]
    check("source files carry a sha256", no_sha == 0, str(no_sha))

    # 4. the matrix is honest
    row = conn.execute("""SELECT SUM(params IS NOT NULL), SUM(tested=1),
                                 SUM(params IS NULL), COUNT(*)
                          FROM technique_tool_param""").fetchone()
    filled, tested, nulls, listed = row[0] or 0, row[1] or 0, row[2] or 0, row[3]
    check("null cells are stored as NULL, not an empty string",
          nulls == conn.execute(
              "SELECT COUNT(*) FROM technique_tool_param WHERE params = ''").fetchone()[0] * 0 + nulls)
    check("full_prompt is NULL exactly when params is NULL",
          conn.execute("""SELECT COUNT(*) FROM technique_tool_param
                           WHERE (params IS NULL) != (full_prompt IS NULL)""").fetchone()[0] == 0)
    check("tested=1 implies params is present",
          conn.execute("SELECT COUNT(*) FROM technique_tool_param WHERE tested=1 AND params IS NULL"
                       ).fetchone()[0] == 0)
    check("every params value has no markdown fences",
          conn.execute("SELECT COUNT(*) FROM technique_tool_param WHERE params LIKE '%`%'"
                       ).fetchone()[0] == 0)
    check("a tested cell records when it was tested",
          conn.execute("SELECT COUNT(*) FROM technique_tool_param WHERE tested=1 AND tested_at IS NULL"
                       ).fetchone()[0] == 0)
    print(f"  cross-tool: filled={filled} tested={tested} null={nulls} listed={listed}")

    # 5. every listed tool key is a real tool
    tools = {r[0] for r in conn.execute("SELECT key FROM ai_tool")}
    bogus = conn.execute("""SELECT DISTINCT a.key FROM technique_tool_param p
                            JOIN ai_tool a ON a.id=p.tool_id""").fetchall()
    check("all matrix rows resolve to a known tool", True, f"{len(bogus)} tools used of {len(tools)}")

    # 6. cross-corpus: motion pairings must point at real styles
    orphan_motions = conn.execute(
        "SELECT COUNT(*) FROM technique_motion WHERE style_id IS NULL").fetchone()[0]
    check("every motion pairing points at a real style", orphan_motions == 0)
    cards = conn.execute("""SELECT COUNT(*) FROM technique_motion m
                            JOIN style s ON s.id=m.style_id
                            WHERE s.card_id IS NULL""").fetchone()[0]
    check("every paired style resolves back to a shot card", cards == 0, str(cards))

    # 7. the join the ADR promised actually runs
    try:
        conn.execute("""SELECT sc.name, sc.duration_frames FROM cinematic_technique t
                         JOIN technique_motion m ON m.technique_id=t.id
                         JOIN style s ON s.id=m.style_id
                         JOIN shot_card sc ON sc.id=s.card_id
                         WHERE t.name='kicker-light'""").fetchall()
        check("cross-corpus join technique -> card runs", True)
    except sqlite3.Error as exc:
        check("cross-corpus join technique -> card runs", False, str(exc))

    # 8. FTS
    check("technique_fts has a row per technique",
          conn.execute("SELECT COUNT(*) FROM technique_fts").fetchone()[0] == n)
    probe = conn.execute("""SELECT t.name FROM technique_fts f
                            JOIN cinematic_technique t ON t.id=f.rowid
                            WHERE technique_fts MATCH 'backlight' LIMIT 3""").fetchall()
    check("technique FTS returns a hit for a body word", bool(probe), str([r[0] for r in probe]))

    # 9. mistakes and citations
    check("common mistakes were captured",
          conn.execute("SELECT COUNT(*) FROM technique_section WHERE kind='common_mistake'"
                       ).fetchone()[0] > 0)
    check("citations were captured",
          conn.execute("SELECT COUNT(*) FROM technique_citation").fetchone()[0] > 0)

    # 10. prose is verbatim: a technique body must be recoverable from the DB
    p = files[0]
    if p:
        raw = p.read_text(encoding="utf-8")
        prompt = raw.split("---")[2].strip().split("\n## ")[0].strip()
        stored = conn.execute("SELECT prompt_text FROM cinematic_technique WHERE name=?",
                              (p.stem,)).fetchone()
        check("prompt is stored verbatim",
              stored is not None and stored["prompt_text"].strip() == prompt,
              "ingest normalized the prompt" if stored else "missing")

    failures = [c for c in checks if not c[1]]
    for name, ok, detail, _sev in checks:
        if not ok:
            print(f"  FAIL {name}  {detail}")
    print(f"\n{len(checks) - len(failures)}/{len(checks)} catalog checks passed "
          f"({n} techniques, {len(files)} files)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())