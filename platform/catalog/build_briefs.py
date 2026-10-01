"""F071: compile every cinematic technique to a deterministic brief.

    python platform/catalog/build_briefs.py
    python platform/catalog/build_briefs.py --lint

Output: prompts/catalog/generated/<slug>.json plus index.json.

Discipline: identical to prompts/README.md's `shotcraft.brief/1`, with one
addition that the corpus forces — `cinematic.brief/1`.

The brief is structure, the copy is a slot
---------------------------------------
`prompt` is the authored text, verbatim, with `[Subject]` intact. Nothing in
this file rephrases it. A "cleaned up" prompt is indistinguishable from an
authored one to whoever receives it, and the recipient has no way to check.

An untested tool parameter stays null in the brief
--------------------------------------------------
`tool_params` is a 7-entry object keyed by tool, and **every** value is `null`
because no cell in the source matrix has been run against a model version
(791 parameters recorded, 0 tested). A brief that quietly dropped the nulls
would read as "no parameters exist", which is wrong: it would read as "no
parameters were verified", and those are different statements. Each entry also
carries `tested: false` so a reader cannot miss the distinction by reading only
the params.

Provenance
----------
Every brief carries `source.catalog_sha256` and `source.file_sha256`, so a row
traces to the exact authored bytes on both sides of the import.
"""

from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DB = ROOT / "platform" / "db" / "shotcraft.db"
OUT = ROOT / "prompts" / "catalog" / "generated"
SLOT = "[Subject]"
TOOL_KEYS = ("mj61", "runway_gen3", "veo2", "kling15", "luma", "pika15", "sora")

REQUIRED_TOP = ("schema", "slug", "title", "category", "level", "prompt",
                "prompt_slot", "source", "tool_params", "motion", "mistakes",
                "citations", "copy")


def q(cur, sql, *a):
    cur.row_factory = sqlite3.Row
    return [dict(r) for r in cur.execute(sql, a).fetchall()]


def build(cur) -> list[dict]:
    briefs = []
    for t in q(cur, """SELECT t.*, cc.key cat_key, cc.label_en cat_label
                       FROM cinematic_technique t
                       JOIN cinematic_category cc ON cc.id=t.category_id
                       ORDER BY cc.sort_order, t.name"""):
        tid = t["id"]

        tools = {}
        for p in q(cur, """SELECT a.key, a.label, a.param_style, p.params,
                                  p.full_prompt, p.version_tag, p.tested, p.tested_at
                           FROM technique_tool_param p JOIN ai_tool a ON a.id=p.tool_id
                           WHERE p.technique_id=? ORDER BY a.id""", tid):
            tools[p["key"]] = {
                "tool": p["label"],
                "param_style": p["param_style"],
                "version": p["version_tag"],
                "params": p["params"],
                "full_prompt": p["full_prompt"],
                "tested": bool(p["tested"]),
                "tested_at": p["tested_at"],
            }
        # A missing tool is null too, so the object always has all seven keys and
        # "absent" never has to be distinguished from "unlooked".
        for k in TOOL_KEYS:
            tools.setdefault(k, {"tool": k, "param_style": None, "version": None,
                                 "params": None, "full_prompt": None,
                                 "tested": False, "tested_at": None})

        motion = q(cur, """SELECT m.kind, sc.name card, c.key category,
                                  e.key energy, sc.duration_frames frames,
                                  sc.duration_text, st.key style,
                                  (SELECT COUNT(*) FROM card_param cp
                                    WHERE cp.card_id = sc.id) parameters
                           FROM technique_motion m
                           JOIN style st ON st.id = m.style_id
                           LEFT JOIN shot_card sc ON sc.id = st.card_id
                           LEFT JOIN category c ON c.id = sc.category_id
                           LEFT JOIN energy_level e ON e.id = sc.energy_level_id
                           WHERE m.technique_id=? ORDER BY sc.name, st.key""", tid)

        briefs.append({
            "schema": "cinematic.brief/1",
            "slug": t["name"],
            "title": t["title"],
            "category": t["cat_key"],
            "category_label": t["cat_label"],
            "level": t["level"],
            "prompt": t["prompt_text"],
            "prompt_slot": SLOT,
            "source": {
                "brief_kind": "generated",
                "technique_file": f"data/cinematic/{t['name']}.md",
                "catalog_repo": "cinematique",
                "catalog_license": "MIT",
                "catalog_sha256": (t["source_sha256"] if "source_sha256" in t else None),
                "source_url": t.get("source_url"),
                "image_url": t["image_url"],
                "video_url": t["video_url"],
                "authored_lede": t["lede_text"],
                "when_to_use": t["when_to_use_text"],
                "directing_the_ai": t["directing_text"],
            },
            "tool_params": tools,
            "tool_summary": {
                "listed": len(tools),
                "with_params": sum(1 for v in tools.values() if v["params"]),
                "tested": sum(1 for v in tools.values() if v["tested"]),
                "null": sum(1 for v in tools.values() if not v["params"]),
                "note": ("an untested tool parameter is an untested claim; "
                         "`tested: false` on a cell with params means the parameter "
                         "is recorded but has never been run against a model version"),
            },
            "motion": motion,
            "mistakes": q(cur, """SELECT ord, text, is_critical FROM technique_section
                                 WHERE technique_id=? AND kind='common_mistake'
                                 ORDER BY ord""", tid),
            "citations": q(cur, """SELECT ord, title, url FROM technique_citation
                                   WHERE technique_id=? ORDER BY ord""", tid),
            "copy": {
                "status": "slot",
                "authored": False,
                "note": ("The prompt is the copy and it is authored upstream. "
                         "What a client needs filled is the subject: replace "
                         f"{SLOT} with the subject of their film. Do not expand it "
                         "here — a filled slot stored in the brief reads exactly "
                         "like an authored prompt and cannot be told apart."),
                "slots": [{"id": "subject", "value": SLOT}],
            },
        })
    return briefs


def lint(briefs: list[dict]) -> list[str]:
    """Every invariant the schema doc claims, checked on the written files."""
    problems: list[str] = []
    if not briefs:
        return ["no briefs built"]

    paths = {p.stem: p for p in OUT.glob("*.json") if p.name != "index.json"}
    if len(paths) != len(briefs):
        problems.append(f"{len(paths)} files on disk vs {len(briefs)} techniques in the db")

    for b in briefs:
        p = paths.get(b["slug"])
        if p is None:
            problems.append(f"{b['slug']}: no file on disk")
            continue
        n = p.name
        for key in REQUIRED_TOP:
            if key not in b:
                problems.append(f"{n}: missing {key}")
        if b.get("schema") != "cinematic.brief/1":
            problems.append(f"{n}: schema is {b.get('schema')!r}")
        if SLOT not in (b.get("prompt") or ""):
            problems.append(f"{n}: prompt lost its {SLOT} slot")
        if len(b.get("tool_params") or {}) != len(TOOL_KEYS):
            problems.append(f"{n}: tool_params has "
                            f"{len(b.get('tool_params') or {})} entries, expected {len(TOOL_KEYS)}")
        for k, v in (b.get("tool_params") or {}).items():
            if v.get("params") and v.get("tested"):
                problems.append(f"{n}: {k} claims tested with a tested_at of "
                                f"{v.get('tested_at')!r}")
            if not v.get("params") and v.get("full_prompt"):
                problems.append(f"{n}: {k} has a full_prompt with no params")
        if not (b.get("source") or {}).get("technique_file"):
            problems.append(f"{n}: source.technique_file missing")
        # Determinism: the same DB must produce the same bytes.
        disk = json.loads(p.read_text(encoding="utf-8"))
        if disk != b:
            problems.append(f"{n}: on-disk file differs from what was just built")
    return problems


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lint", action="store_true",
                    help="validate the written briefs instead of rebuilding")
    a = ap.parse_args()

    if not DB.exists():
        print(f"no database at {DB}; run platform/ingest/run.py", file=sys.stderr)
        return 2
    conn = sqlite3.connect(f"file:{DB.as_posix()}?mode=ro", uri=True)

    if not a.lint:
        briefs = build(conn)
        OUT.mkdir(parents=True, exist_ok=True)
        for old in OUT.glob("*.json"):
            old.unlink()
        for b in briefs:
            (OUT / f"{b['slug']}.json").write_text(
                json.dumps(b, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                encoding="utf-8")
        (OUT / "index.json").write_text(json.dumps({
            "schema": "cinematic.brief-index/1",
            "count": len(briefs),
            "briefs": [{"slug": b["slug"], "title": b["title"], "category": b["category"],
                        "level": b["level"], "motions": len(b["motion"]),
                        "tools_with_params": b["tool_summary"]["with_params"],
                        "tools_tested": b["tool_summary"]["tested"]}
                       for b in briefs],
        }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    briefs = build(conn)
    problems = lint(briefs)
    for p in problems:
        print("LINT FAIL", p)
    tot = {
        "listed": sum(len(b["tool_params"]) for b in briefs),
        "with_params": sum(b["tool_summary"]["with_params"] for b in briefs),
        "tested": sum(b["tool_summary"]["tested"] for b in briefs),
        "null": sum(b["tool_summary"]["null"] for b in briefs),
        "motions": sum(len(b["motion"]) for b in briefs),
        "mapped": sum(1 for b in briefs if b["motion"]),
    }
    print(f"briefs: {len(briefs)}  tool cells listed={tot['listed']} "
          f"with_params={tot['with_params']} tested={tot['tested']} null={tot['null']}")
    print(f"  motion pairings: {tot['motions']} across {tot['mapped']}/{len(briefs)} techniques")
    print(f"lint: {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())