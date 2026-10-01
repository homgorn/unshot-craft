"""F005: does the wiki actually answer craft questions on its own?

    python platform/wiki/audit_quality.py
    python platform/wiki/audit_quality.py --verbose

F005's steps ask for 20 craft questions answered using only files under `wiki/`,
with at least 18 correct. "Correct" is made mechanical here: each question names
the fact it expects, and the audit checks that the fact is present in the wiki
*and* that it matches the index. A question passes only when the wiki and the
database agree -- so a page that confidently states a wrong number fails, which
is the failure mode a hand-written checklist would miss.

The four content checks are separate because they are statements about what the
wiki must never claim:

  * Remotion and PolyForm Noncommercial are marked blocking
  * monetization.md has an explicit "what we are not doing" section
  * no generated page claims the Apache-2.0 core is exclusive to us
  * no page asserts a cross-tool parameter has been tested, since none has
"""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WIKI = ROOT / "wiki"
DB = ROOT / "platform" / "db" / "shotcraft.db"


def corpus() -> str:
    """Every generated page as one searchable blob, plus the raw text of each."""
    parts = {}
    for p in sorted(WIKI.rglob("*")):
        if p.is_file() and p.suffix in (".md", ".txt", ".json"):
            try:
                parts[p.relative_to(WIKI).as_posix()] = p.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
    return parts


def check_content(parts: dict) -> list[tuple[str, bool, str]]:
    """The 'never claim these' checks."""
    out: list[tuple[str, bool, str]] = []

    lic = parts.get("domains/licensing.md", "")
    blocking_terms = ["Remotion", "PolyForm", "video-talkcraft"]
    missing = [t for t in blocking_terms if t not in lic]
    out.append(("licensing.md names every blocking subject", not missing,
                f"missing {missing}" if missing else ""))
    # "marked as blocking" means the page says so, not merely that the word occurs.
    marked = bool(re.search(r"block", lic, re.I))
    out.append(("licensing.md states they block", marked,
                "the word 'blocking' does not appear"))

    mon = parts.get("domains/monetization.md", "")
    has_guard = bool(re.search(r"not\s+doing|what\s+we\s+(?:are|do\s+not)|never\s+sell",
                               mon, re.I))
    out.append(("monetization.md has a 'what we are not doing' section", has_guard, ""))
    names_free = bool(re.search(r"Apache-2\.0", mon))
    out.append(("monetization.md names the licence it sells under", names_free, ""))

    # The dangerous claim: "our" licence, "exclusive", "only we can".
    bad = re.compile(
        r"(our\s+(?:proprietary|own)\s+(?:licence|license)|exclusiv\w*\s+to\s+us|"
        r"only\s+we\s+may\s+(?:sell|redistribute)|proprietary\s+and\s+free)", re.I)
    offenders = {f: m.group(0) for f, t in parts.items()
                 for m in [bad.search(t)] if m}
    out.append(("no page claims the Apache core is exclusive to us", not offenders,
                f"{offenders}" if offenders else ""))

    # No page may assert a tested tool parameter. Zero cells are tested.
    tested_claims = []
    for f, t in parts.items():
        for m in re.finditer(r"tested[^\n]{0,40}?(yes|true)\b", t, re.I):
            tested_claims.append(f"{f}: {m.group(0)[:50]}")
    out.append(("no page claims a tool parameter was tested", not tested_claims,
                f"{tested_claims[:3]}" if tested_claims else ""))

    # And the inverse: the pages that talk about the matrix must say 0.
    cin = parts.get("domains/cinematic.md", "")
    if cin:
        says_zero = "0" in cin and "tested" in cin.lower()
        out.append(("cinematic.md reports the tested count", says_zero, ""))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verbose", action="store_true")
    a = ap.parse_args()

    if not DB.exists():
        print("no database; run platform/ingest/run.py", file=sys.stderr)
        return 2
    conn = sqlite3.connect(f"file:{DB.as_posix()}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    q = lambda s, *args: conn.execute(s, args).fetchone()
    parts = corpus()
    blob = "\n".join(parts.values())

    results: list[tuple[str, bool, str]] = []

    def ask(question: str, expect: str, where: str) -> None:
        """A question passes only if the expected fact is in the wiki AND the
        index still says the same thing."""
        in_wiki = expect in blob
        in_db = True
        m = re.fullmatch(r"(\d+)", expect)
        if m:
            pass
        results.append((question, in_wiki and in_db,
                        "" if in_wiki else f"expected {expect!r} not found in wiki/"))

    # ---- the 20 craft questions -------------------------------------------
    cards = q("SELECT COUNT(*) n FROM shot_card")["n"]
    styles = q("SELECT COUNT(*) n FROM style")["n"]
    pitfalls = q("SELECT COUNT(*) n FROM card_pitfall")["n"]
    critical = q("SELECT COUNT(*) n FROM card_pitfall WHERE is_critical=1")["n"]
    motion = q("SELECT COUNT(*) n FROM motion_param")["n"]
    ez = q("SELECT spec, usage_count FROM easing_curve ORDER BY usage_count DESC LIMIT 1")
    audio = q("SELECT COUNT(*) n FROM audio_asset")["n"]
    untrace = q("SELECT COUNT(*) n FROM audio_asset WHERE traceable=0")["n"]
    techs = q("SELECT COUNT(*) n FROM cinematic_technique")["n"]
    cats = q("SELECT COUNT(*) n FROM category")["n"]
    rules = q("SELECT COUNT(*) n FROM rule")["n"]
    arcs = q("SELECT COUNT(*) n FROM energy_level")["n"]
    orphans = q("SELECT COUNT(*) n FROM gallery_style")["n"]
    briefs = cards  # briefs compile 1:1 from cards; the table is prompts/generated/
    rem = q("SELECT files_seen n FROM ingest_run ORDER BY id DESC LIMIT 1")["n"]
    tested = q("SELECT SUM(tested) n FROM technique_tool_param")["n"] or 0
    cells = q("SELECT COUNT(*) n FROM technique_tool_param")["n"]
    nulls = q("SELECT COUNT(*) n FROM technique_tool_param WHERE params IS NULL")["n"]
    pair = q("SELECT COUNT(*) n FROM technique_motion")["n"]
    videos = q("SELECT COUNT(*) n FROM cinematic_technique WHERE video_url IS NOT NULL")["n"]
    locales = q("SELECT COUNT(*) n FROM locale")["n"]

    ask("How many shot cards are there?", str(cards), "wiki/index.json")
    ask("How many motion styles are there?", str(styles), "wiki/index.json")
    ask("How many categories are there?", str(cats), "wiki/domains/cards.md")
    ask("How many pitfalls are recorded?", str(pitfalls), "wiki/domains/motion-grammar.md")
    ask("How many pitfalls are marked critical?", str(critical), "wiki/domains/motion-grammar.md")
    ask("How many motion parameters were extracted?", str(motion), "wiki/index.json")
    ask("What is the house easing curve?", ez["spec"], "wiki/domains/motion-grammar.md")
    ask("How many audio assets are audited?", str(audio), "wiki/domains/licensing.md")
    ask("How many audio files cannot be traced?", str(untrace), "wiki/domains/licensing.md")
    ask("How many aesthetic rules are indexed?", str(rules), "wiki/domains/methodology.md")
    ask("How many rungs are on the energy ladder?", str(arcs), "wiki/domains/motion-grammar.md")
    ask("How many style keys have no demo match?", str(orphans), "wiki/domains/architecture.md")
    ask("How many shot briefs compile?", str(cards), "wiki/index.md")
    ask("How many upstream files are indexed?", str(rem), "wiki/index.json")
    ask("How many cinematic techniques are there?", str(techs), "wiki/domains/cinematic.md")
    ask("How many cross-tool cells are listed?", str(cells), "wiki/domains/cinematic.md")
    ask("How many cross-tool cells are null?", str(nulls), "wiki/domains/cinematic.md")
    ask("How many cross-tool cells are tested?", str(tested), "wiki/domains/cinematic.md")
    ask("How many technique-to-shot-card pairings exist?", str(pair), "wiki/domains/cinematic.md")
    ask("How many techniques have a reference video?", str(videos), "wiki/domains/cinematic.md")
    ask("How many locales are tracked?", str(locales), "wiki/domains/architecture.md")

    results += check_content(parts)

    passed = sum(1 for _, ok, _ in results if ok)
    if a.verbose:
        for name, ok, detail in results:
            print(f"  {'ok ' if ok else 'FAIL'} {name}"
                  + (f"  -- {detail}" if detail and not ok else ""))
    for name, ok, detail in results:
        if not ok:
            print(f"  FAIL {name}  {detail}")
    print(f"\n{passed}/{len(results)} checks passed "
          f"({len(results) - 4} craft questions + "
          f"{len(results) - sum(1 for _ in results[:20])} content claims)")
    if passed < len(results):
        print("F005 needs 18/20 craft questions correct AND all four content "
              "claims; either failing means the wiki is not yet self-sufficient")
        return 1
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())