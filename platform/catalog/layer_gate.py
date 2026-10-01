"""Gate for the cinematic-technique layer (F070-F074).

    python platform/catalog/layer_gate.py

The previous version of this file asserted that every catalog feature ships
`passes: false`, on the grounds that "a feature must ship unproven". That was a
scaffold-era guard and it had two problems: it began failing the moment a feature
was honestly implemented, and it hardcoded an absolute path so it only ever ran
on one machine.

What replaced it checks the thing that guard was reaching for: **no catalog
feature may claim `passes: true` unless its cited verification actually passes
right now.** A `verified_by` note is an assertion; running it is evidence.
"""

from __future__ import annotations

import io
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CATALOG = ["F070", "F071", "F072", "F073", "F074"]

ok: list[str] = []
bad: list[str] = []


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def run(*argv: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, *argv], capture_output=True, text=True,
                          encoding="utf-8", cwd=str(ROOT),
                          env={**os.environ, "PYTHONIOENCODING": "utf-8"})


# ---------------------------------------------------------------------------
# 1. Ledger shape
# ---------------------------------------------------------------------------
feats = json.loads(read("specs/feature-list.json"))
by_id = {f["id"]: f for f in feats}
for i in CATALOG:
    if i not in by_id:
        bad.append(f"{i} missing from the ledger")
    elif not by_id[i].get("steps"):
        bad.append(f"{i} has no steps")
if len(feats) == 23:
    ok.append(f"ledger has {len(feats)} features")

# ---------------------------------------------------------------------------
# 2. A feature marked passing must carry a verification note that still holds.
# ---------------------------------------------------------------------------
for i in CATALOG:
    f = by_id.get(i, {})
    if not f.get("passes"):
        ok.append(f"{i}: open ({len(f.get('steps', []))} steps)")
        continue
    note = f.get("verified_by")
    if not note:
        bad.append(f"{i}: passes=true with no verified_by note -- an unevidenced claim")
        continue
    # The note must cite a runnable harness, not just assert a number.
    m = re.findall(r"(platform/[\w/]+\.py)", note)
    if not m:
        bad.append(f"{i}: verified_by cites no runnable script: {note[:90]!r}")
        continue
    missing = [s for s in set(m) if not (ROOT / s).exists()]
    if missing:
        bad.append(f"{i}: verified_by cites a script that does not exist: {missing}")
        continue
    ok.append(f"{i}: passes=true, cites {sorted(set(m))}")

# ---------------------------------------------------------------------------
# 3. The harnesses actually pass, run now.
# ---------------------------------------------------------------------------
for rel, needles in (
    ("platform/catalog/validate_schema.py", ("DDL: applied clean",)),
    ("platform/catalog/selftest.py", ("catalog checks passed",)),
):
    r = run(rel)
    if r.returncode != 0 or not all(n in r.stdout for n in needles):
        bad.append(f"{rel} failed:\n{r.stdout[-700:]}{r.stderr[-300:]}")
    else:
        tail = [l for l in r.stdout.splitlines() if l.strip()][-1]
        ok.append(f"{rel}: {tail.strip()}")

# ---------------------------------------------------------------------------
# 4. Docs the layer claims to have touched must actually mention it.
# ---------------------------------------------------------------------------
for rel, needle in (
    ("AGENTS.md", "data/cinematic/"),
    ("AGENTS.md", "0007"),
    ("docs/architecture/README.md", "data/cinematic/"),
    ("data/README.md", "[Subject]"),
    ("docs/adr/0007-cinematic-catalog-layer.md", "Status: accepted"),
    ("specs/features/F070-cinematic-catalog-ingest.md", "F070"),
    ("progress.md", "F070"),
):
    try:
        present = needle in read(rel)
    except OSError as exc:
        bad.append(f"{rel} unreadable: {exc}")
        continue
    (ok if present else bad).append(
        f"{rel} {'mentions' if present else 'does NOT mention'} {needle!r}")

# ---------------------------------------------------------------------------
# 5. The catalog's own upstream, if it is reachable on this machine.
#
# Optional by design: the corpus is imported into data/cinematic/ and committed,
# so a machine without the Cinematique checkout is a valid state, not a failure.
# ADR 0007 requires either corpus to build alone.
# ---------------------------------------------------------------------------
CI = Path(os.environ.get("CINEMATIQUE_DIR", r"C:\susa ai\cinematique"))
if CI.is_dir():
    for rel, needle in (("INTEGRATION.md", "shotcraft"),):
        p = CI / rel
        if not p.exists():
            bad.append(f"cinematique/{rel} missing")
        elif needle not in p.read_text(encoding="utf-8", errors="replace"):
            bad.append(f"cinematique/{rel} does not mention {needle!r}")
        else:
            ok.append(f"cinematique/{rel} mentions {needle!r}")
    lic = next((CI / n for n in ("LICENSE", "LICENSE.md") if (CI / n).exists()), None)
    if lic is None:
        bad.append("cinematique has no LICENSE file; the import assumes MIT")
    elif "MIT License" not in lic.read_text(encoding="utf-8", errors="replace"):
        bad.append(f"cinematique/{lic.name} is not MIT -- re-check the import terms")
    else:
        ok.append("cinematique licence is MIT, as the importer assumes")
else:
    ok.append(f"cinematique checkout absent at {CI} -- imported corpus still builds "
              f"(ADR 0007: either corpus must build alone)")

# ---------------------------------------------------------------------------
print(f"PASS ({len(ok)})")
for o in ok:
    print("  +", o)
if bad:
    print()
    print(f"FAIL ({len(bad)})")
    for b in bad:
        print("  -", b)
    sys.exit(1)
print()
print("layer is consistent; nothing here marks itself done that is not")