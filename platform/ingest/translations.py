"""Replay translation batches into `translation_provenance`.

    called by platform/ingest/run.py; safe to run standalone

Why this is a replay and not a preserved table
----------------------------------------------
`platform/ingest/run.py` deletes `platform/db/shotcraft.db` and rebuilds it, so
anything written into that file by hand survives exactly until the next ingest.
Authorship data -- who wrote a translation, and whether a native speaker has
signed it off -- cannot live there, or the record of who is responsible for a
line of Russian text disappears every time somebody runs the build.

So the authority is the batch files under `site/locales/_batch_*.json`, which
are committed, reviewable, and diffable, and the provenance table is *derived*
from them by replaying each one. That is the same contract the rest of the repo
uses: `wiki/` is derived from the DB, the DB is derived from upstream plus
`data/`, and here the DB is derived from upstream plus the batches.

A batch is the unit because it is the unit a human reviews. Replaying them in
sorted order means the last write for a key wins, and a corrected batch
supersedes the one before it without anyone having to remember to delete a row.

What is deliberately not here
-----------------------------
Nothing validates the *text* -- `platform/site/translate.py apply` does that, and
this runs after it. This only records the claim. A row saying `status='reviewed'`
is a claim by whoever put `reviewed_by` in the batch, and this file does not
upgrade it, second-guess it, or infer it.
"""

from __future__ import annotations

import json
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BATCH_GLOB = "site/locales/_batch_*.json"
VALID_METHOD = {"machine", "human", "vendor", "import"}


def batches() -> list[Path]:
    return sorted(Path(ROOT).glob(BATCH_GLOB))


def replay(conn: sqlite3.Connection) -> dict:
    paths = batches()
    if not paths:
        return {"batches": 0, "rows": 0,
                "note": "no batch files; translation_provenance stays empty, which "
                        "is the correct state for a repo with no authored locales"}

    have = conn.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table' "
                        "AND name='translation_provenance'").fetchone()[0]
    if not have:
        return {"batches": len(paths), "rows": 0,
                "error": "translation_provenance is absent from the schema; the "
                         "provenance of every translation is unrecorded"}

    # A rebuild starts from an empty database, so this is a clean slate by
    # construction. Truncating anyway keeps a standalone re-run idempotent.
    conn.execute("DELETE FROM translation_provenance")

    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    rows = 0
    problems: list[str] = []
    per_batch: dict[str, int] = {}

    for path in paths:
        try:
            b = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            problems.append(f"{path.name}: invalid JSON: {exc}")
            continue
        locale = b.get("locale")
        ns = b.get("namespace")
        method = b.get("method", "machine")
        reviewed_by = b.get("reviewed_by")
        status = "reviewed" if reviewed_by else b.get("status", "needs_review")
        if not locale or not ns:
            problems.append(f"{path.name}: no locale or namespace")
            continue
        if method not in VALID_METHOD:
            problems.append(f"{path.name}: method {method!r} is not one of "
                            f"{sorted(VALID_METHOD)}")
            continue
        # The one rule that cannot be bypassed: a batch cannot mark its own work
        # reviewed. If a file says status=reviewed with nobody named, that is a
        # claim with no author, and it lands as needs_review.
        if b.get("status") == "reviewed" and not reviewed_by:
            problems.append(f"{path.name}: claims status=reviewed with no "
                            f"reviewed_by; recorded as needs_review")
            status = "needs_review"

        lid = conn.execute("SELECT id FROM locale WHERE code=?", (locale,)).fetchone()
        if not lid:
            problems.append(f"{path.name}: locale {locale!r} is not registered")
            continue

        n = 0
        for key, value in (b.get("entries") or {}).items():
            fields = ((value or {}).items() if isinstance(value, dict)
                      else [(None, value)])
            for field, text in fields:
                if not isinstance(text, str) or not text.strip():
                    continue
                sub = f"{key}.{field}" if field else key
                conn.execute(
                    """INSERT INTO translation_provenance
                         (locale_id, ns, key, method, status, reviewed_by,
                          reviewed_at, tool, batch_file, updated_at)
                       VALUES (?,?,?,?,?,?,?,?,?,?)
                       ON CONFLICT(locale_id, ns, key) DO UPDATE SET
                         method=excluded.method, status=excluded.status,
                         reviewed_by=excluded.reviewed_by,
                         reviewed_at=excluded.reviewed_at,
                         tool=excluded.tool, batch_file=excluded.batch_file,
                         updated_at=excluded.updated_at""",
                    (lid[0], ns, sub, method, status, reviewed_by,
                     b.get("reviewed_on") if reviewed_by else None,
                     "machine-pass" if method == "machine" else None,
                     path.name, now))
                n += 1
                rows += 1
        per_batch[path.name] = n
        if n == 0:
            problems.append(f"{path.name}: replayed 0 rows -- an empty batch is "
                            f"either a mistake or a batch whose entries were all "
                            f"rejected")

    conn.commit()
    return {"batches": len(paths), "rows": rows, "per_batch": per_batch,
            "problems": problems}


def main() -> int:
    db = ROOT / "platform" / "db" / "shotcraft.db"
    if not db.exists():
        print(f"no database at {db}", file=sys.stderr)
        return 2
    conn = sqlite3.connect(db)
    try:
        rep = replay(conn)
    finally:
        conn.close()
    print(json.dumps(rep, ensure_ascii=False, indent=2))
    return 1 if rep.get("error") or rep.get("problems") else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
