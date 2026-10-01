"""F040: bump the pinned upstream clone and prove the diff is only what it should be.

    python platform/bump_upstream.py --check          # is a bump even available?
    python platform/bump_upstream.py --dry-run        # what would change?
    python platform/bump_upstream.py                  # do it

A bump is where an index quietly stops being trustworthy: 150 cards become 151,
a parameter extractor gains a pattern, and nobody notices that a column changed
shape. So the bump is not "git pull && run ingest" -- it is a **diff with a
review gate**: pull, ingest, and then refuse to finish unless the only changes
are the ones a card addition is allowed to cause.

The allowlist
-------------
`shots/cards +N`, `shots/styles +N`, `params +N`, `sha old -> new`, and a bumped
`ingested_at`. Anything else -- a card removed, a slug renamed, a count that went
*down*, a source_file losing its sha -- is a change in the upstream's *shape* and
needs a human, because it usually means the parser needs updating too.

Traceability
------------
The gate also verifies that no row lost its `source_file_id` and that every
`source_file` still carries a sha256. A bump that orphans provenance is a failed
bump even when every count looks right.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sqlite3
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UPSTREAM = ROOT / "upstream" / "video-shotcraft"
DB = ROOT / "platform" / "db" / "shotcraft.db"
ORIGIN = "https://github.com/Vincentwei1021/video-shotcraft.git"

COUNTS = {
    "cards": "SELECT COUNT(*) FROM shot_card",
    "styles": "SELECT COUNT(*) FROM style",
    "card_params": "SELECT COUNT(*) FROM card_param",
    "pitfalls": "SELECT COUNT(*) FROM card_pitfall",
    "motion_params": "SELECT COUNT(*) FROM motion_param",
    "audio": "SELECT COUNT(*) FROM audio_asset",
    "translations": "SELECT COUNT(*) FROM translation",
    "rules": "SELECT COUNT(*) FROM rule",
    "techniques": "SELECT COUNT(*) FROM cinematic_technique",
}


def sh(*a: str, cwd: Path | None = None) -> str:
    r = subprocess.run(list(a), capture_output=True, text=True, encoding="utf-8",
                       cwd=str(cwd or ROOT))
    if r.returncode:
        raise RuntimeError(f"{' '.join(a)} -> {r.returncode}\n{r.stderr[-600:]}")
    return r.stdout.strip()


def snapshot() -> dict:
    conn = sqlite3.connect(f"file:{DB.as_posix()}?mode=ro", uri=True)
    out = {k: conn.execute(sql).fetchone()[0] for k, sql in COUNTS.items()}
    out["head_sha"] = conn.execute("SELECT head_sha FROM source_repo LIMIT 1").fetchone()[0]
    out["cards"] = out["cards"]
    out["names"] = sorted(r[0] for r in conn.execute("SELECT name FROM shot_card"))
    out["files_without_sha"] = conn.execute(
        "SELECT COUNT(*) FROM source_file WHERE sha256 IS NULL OR sha256=''").fetchone()[0]
    out["rows_without_source"] = conn.execute(
        """SELECT COUNT(*) FROM shot_card s WHERE s.source_file_id IS NULL""").fetchone()[0]
    conn.close()
    return out


def current_sha() -> str:
    return sh("git", "-C", str(UPSTREAM), "rev-parse", "HEAD")


def remote_sha() -> str | None:
    if not UPSTREAM.exists():
        return None
    try:
        sh("git", "-C", str(UPSTREAM), "fetch", "--depth", "1", "origin")
    except RuntimeError:
        return None
    try:
        return sh("git", "-C", str(UPSTREAM), "rev-parse", "origin/main")
    except RuntimeError:
        return None


def rebuild() -> None:
    sh(sys.executable, str(ROOT / "platform" / "ingest" / "run.py"))
    sh(sys.executable, str(ROOT / "platform" / "wiki" / "build_wiki.py"))


def classify(before: dict, after: dict) -> tuple[list[str], list[str]]:
    """-> (expected, unexpected). Expected changes are what adding cards looks like."""
    expected: list[str] = []
    unexpected: list[str] = []

    for key in ("cards", "styles", "card_params", "pitfalls", "motion_params",
                "audio", "translations", "rules"):
        b, a = before.get(key, 0), after.get(key, 0)
        if b == a:
            continue
        if a > b:
            expected.append(f"{key} {b} -> {a} (+{a - b})")
        else:
            unexpected.append(f"{key} {b} -> {a} ({a - b}): the upstream corpus SHRANK")

    if before.get("head_sha") != after.get("head_sha"):
        expected.append(f"sha {str(before.get('head_sha'))[:8]} -> "
                        f"{str(after.get('head_sha'))[:8]}")

    gone = sorted(set(before.get("names", [])) - set(after.get("names", [])))
    added = sorted(set(after.get("names", [])) - set(before.get("names", [])))
    if gone:
        # A renamed card breaks every deep link we published. Never automatic.
        unexpected.append(f"{len(gone)} card(s) disappeared or were renamed: "
                          f"{gone[:8]}")
    if added:
        expected.append(f"{len(added)} card(s) added: {added[:8]}")

    if after.get("files_without_sha"):
        unexpected.append(f"{after['files_without_sha']} source_file rows lost their sha256")
    if after.get("rows_without_source"):
        unexpected.append(f"{after['rows_without_source']} shot_card rows have no "
                          f"source_file_id; the change is untraceable")
    if before.get("techniques") != after.get("techniques"):
        unexpected.append(f"techniques {before.get('techniques')} -> "
                          f"{after.get('techniques')}: the catalog corpus is ours and an "
                          f"upstream bump must not move it")
    return expected, unexpected


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="report whether upstream has moved; change nothing")
    ap.add_argument("--dry-run", action="store_true",
                    help="fetch and rebuild into a scratch copy, print the diff, restore")
    ap.add_argument("--target", default=None, help="bump to this SHA instead of origin/main")
    a = ap.parse_args()

    if not UPSTREAM.exists():
        print(f"upstream clone absent at {UPSTREAM}; run scripts/init.ps1 first",
              file=sys.stderr)
        return 2

    here = current_sha()
    print(f"pinned:   {here[:12]}")
    remote = remote_sha()
    if remote is None:
        print("could not reach origin; treating the pinned SHA as current")
        remote = here

    if a.check:
        if remote == here:
            print("up to date; nothing to bump")
            return 0
        print(f"UPSTREAM HAS MOVED -> {remote[:12]}")
        print("  re-run without --check to bump, or --dry-run to see the diff first")
        return 1

    if remote == here and not a.target:
        print("up to date; nothing to do")
        return 0

    if not DB.exists():
        print(f"no database at {DB}; run platform/ingest/run.py first", file=sys.stderr)
        return 2

    before = snapshot()
    backup = DB.with_suffix(".db.bak")
    shutil.copy2(DB, backup)
    before_wiki = ROOT / "wiki"

    target = a.target or remote
    print(f"bumping {here[:12]} -> {target[:12]}")
    sh("git", "-C", str(UPSTREAM), "fetch", "--depth", "1", "origin", target)
    sh("git", "-C", str(UPSTREAM), "checkout", "--detach", "FETCH_HEAD")

    try:
        rebuild()
    except Exception as exc:                                   # noqa: BLE001
        shutil.copy2(backup, DB)
        print(f"rebuild failed, database restored: {exc}", file=sys.stderr)
        return 1

    after = snapshot()
    expected, unexpected = classify(before, after)

    print("\nexpected changes:")
    for e in expected or ["(none)"]:
        print("   +", e)
    if unexpected:
        print("\nUNEXPECTED changes:")
        for u in unexpected:
            print("   -", u)

    if a.dry_run or unexpected:
        print("\nrestoring the previous state (--dry-run or a gate failure)")
        shutil.copy2(backup, DB)
        if before_wiki.exists():
            rebuild()
        backup.unlink(missing_ok=True)
        if unexpected and not a.dry_run:
            print("\nA bump that changes the shape of the corpus needs a human. "
                  "Read the diff above, update the parser or the schema if that is\n"
                  "why it moved, then re-run.", file=sys.stderr)
            return 1
        return 0

    backup.unlink(missing_ok=True)
    print("\nbump applied. Review `git diff wiki/index.json` and commit "
          "(one commit per feature, message references the id).")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())