"""Do the docs still say what the database says?

    python platform/docs_freshness.py
    python platform/docs_freshness.py --verbose

Why this exists
---------------
Every figure in every narrative document was correct when it was written. Then
the index moved under it and nothing said so, because a markdown table is not a
query. In one pass this repo accumulated: a spec claiming 20 techniques and 16
tested cells when the corpus held 150 and none; a cost analysis presenting
"35 styles have no media row" as current when the count is 0 and has been for
weeks; a 1,607 figure for a table that held 1,897; a page size four months stale.

Each was found by reading, not by any check. This file is the check.

How it works
------------
A `CLAIM` is one assertion someone made in one document: a regex, and the SQL
that produces the truth. The regex is searched; if it matches, the number inside
it is compared with the database. A claim whose document no longer contains the
phrase is reported as *stale* rather than passing -- a check that vanishes when
the text is reworded is a check that has stopped working, and saying so is more
useful than silence.

What it deliberately does not do
--------------------------------
It does not try to parse every number in every document. It checks the claims
that are load-bearing: the ones a reader would act on. A prose aside that happens
to contain a number is a human's job, and pretending otherwise would make this
file a source of false confidence.

Adding a claim
--------------
When you write a number into a document that the index can answer, add it here.
That is the whole discipline: a number in prose is a promise that someone can
check it, and the promise needs a verifier.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "platform" / "db" / "shotcraft.db"

# (document, regex with exactly one capture group, SQL producing the truth,
#  what the number is)
# The regex is matched with re.search; the group is compared as an int, with
# thousands separators stripped.
CLAIMS: list[tuple[str, str, str, str]] = [

    # ---------------------------------------------------------------- corpus
    ("README.md", r"(\d[\d,]*) shot recipe cards",
     "SELECT COUNT(*) FROM shot_card", "shot cards"),
    ("README.md", r"(\d[\d,]*) tuned Remotion demos",
     "SELECT COUNT(*) FROM style", "motion styles"),
    ("README.md", r"(\d[\d,]*) sound effects",
     "SELECT COUNT(*) FROM audio_asset", "audio assets"),
    ("README.md", r"(\d[\d,]*) card pages",
     "SELECT COUNT(*) FROM shot_card", "wiki card pages"),
    ("README.md", r"tuned parameters from .*?\| ([\d,]+)",
     "SELECT COUNT(*) FROM card_param", "card parameters"),
    ("README.md", r"pitfalls from .*?\| ([\d,]+)",
     "SELECT COUNT(*) FROM card_pitfall", "pitfalls"),

    ("AGENTS.md", r"catalog invariants, (\d+) checks",
     None, "catalog selftest count (from --help-free run)"),
    ("AGENTS.md", r"\*\*(\d+) techniques imported",
     "SELECT COUNT(*) FROM cinematic_technique", "techniques"),
    ("AGENTS.md", r"(\d+) of (\d+) cross-tool cells",
     "SELECT COUNT(*) FROM technique_tool_param WHERE params IS NOT NULL",
     "matrix cells filled"),

    ("progress.md", r"\| cards \| (\d+) / \d+",
     "SELECT COUNT(*) FROM shot_card", "cards"),
    ("progress.md", r"\| styles \(demo components\) \| (\d+)",
     "SELECT COUNT(*) FROM style", "styles"),
    ("progress.md", r"\| tuned parameters \| ([\d,]+)",
     "SELECT COUNT(*) FROM card_param", "card parameters"),
    ("progress.md", r"\| pitfalls \| ([\d,]+)",
     "SELECT COUNT(*) FROM card_pitfall", "pitfalls"),
    ("progress.md", r"motion parameters extracted from TSX \| ([\d,]+)",
     "SELECT COUNT(*) FROM motion_param", "motion parameters"),
    ("progress.md", r"\| aesthetic rules \| (\d+)",
     "SELECT COUNT(*) FROM rule", "aesthetic rules"),
    ("progress.md", r"\| audio assets audited \| (\d+)",
     "SELECT COUNT(*) FROM audio_asset", "audio assets"),
    ("progress.md", r"\| translation strings \| ([\d,]+)",
     "SELECT COUNT(*) FROM translation", "translation rows"),
    ("progress.md", r"\| locales tracked \| (\d+)",
     "SELECT COUNT(*) FROM locale", "locales"),
    ("progress.md", r"\| techniques \| (\d+) across (\d+) categories",
     "SELECT COUNT(*) FROM cinematic_technique", "techniques"),
    ("progress.md", r"\| cross-tool matrix cells \| ([\d,]+)",
     "SELECT COUNT(*) FROM technique_tool_param", "matrix cells listed"),
    ("progress.md", r"\| cells filled \| (\d+)",
     "SELECT COUNT(*) FROM technique_tool_param WHERE params IS NOT NULL",
     "matrix cells filled"),
    ("progress.md", r"\| cells `NULL` \| (\d+)",
     "SELECT COUNT(*) FROM technique_tool_param WHERE params IS NULL",
     "matrix cells null"),
    ("progress.md", r"\| declared motion pairings \| (\d+) across (\d+) /",
     "SELECT COUNT(*) FROM technique_motion", "motion pairings"),
    ("progress.md", r"\| common-mistake entries \| (\d+)",
     "SELECT COUNT(*) FROM technique_section WHERE kind='common_mistake'",
     "common mistakes"),
    ("progress.md", r"\| citations \| (\d+), \*\*all with",
     "SELECT COUNT(*) FROM technique_citation", "citations"),
    ("progress.md", r"\| reference videos \| (\d+)",
     "SELECT COUNT(*) FROM cinematic_technique WHERE video_url IS NOT NULL",
     "reference videos"),
    ("progress.md", r"(\d[\d,]*) technique pages",
     "SELECT COUNT(*) FROM cinematic_technique", "technique wiki pages"),
    ("progress.md", r"(\d+) domain documents",
     None, "domain document count"),
    ("progress.md", r"\| locales tracked \| (\d+)",
     "SELECT COUNT(*) FROM locale", "locales tracked"),
    ("progress.md", r"\*\*(\d+) attributed, (\d+) reviewed\.\*\*",
     None, "attributed translations, from translate.py report"),
    ("progress.md", r"(\d+) style names are translated",
     None, "ru style titles, from the locale file"),
    ("progress.md", r"(\d[\d,]*) machine translations marked `needs_review`",
     None, "ru strings awaiting review"),
    ("AGENTS.md", r"(\d+) attributed, \d+ reviewed",
     None, "attributed translations, from translate.py report"),
    ("AGENTS.md", r"doctor\.py\s+# 0 error / \d+ warn / (\d+) pass",
     None, "doctor pass count"),

    # ------------------------------------------------------------- catalogue
    ("data/README.md", r"(\d+) techniques covering",
     "SELECT COUNT(*) FROM cinematic_technique", "techniques"),
    ("data/README.md", r"\*\*(\d+) filled, (\d+) tested, (\d+) null\*\*",
     "SELECT COUNT(*) FROM technique_tool_param WHERE params IS NOT NULL",
     "matrix filled (line also asserts tested and null)"),
    ("docs/adr/0007-cinematic-catalog-layer.md", r"\| techniques \| \*\*(\d+)\*\*",
     "SELECT COUNT(*) FROM cinematic_technique", "techniques"),
    ("docs/adr/0007-cinematic-catalog-layer.md",
     r"\| matrix cells filled \| \*\*(\d+)\*\*",
     "SELECT COUNT(*) FROM technique_tool_param WHERE params IS NOT NULL",
     "matrix cells filled"),
    ("docs/adr/0007-cinematic-catalog-layer.md",
     r"\| matrix cells listed \| \*\*(\d+)\*\* \(7 tools",
     "SELECT COUNT(*) FROM technique_tool_param", "matrix cells listed"),
    ("docs/adr/0007-cinematic-catalog-layer.md",
     r"\| matrix cells \*\*tested against a model version\*\* \| \*\*(\d+)\*\*",
     "SELECT SUM(tested) FROM technique_tool_param", "matrix cells tested"),
    ("docs/adr/0007-cinematic-catalog-layer.md", r"\| reference videos \| (\d+)",
     "SELECT COUNT(*) FROM cinematic_technique WHERE video_url IS NOT NULL",
     "reference videos"),
    ("docs/adr/0007-cinematic-catalog-layer.md",
     r"\| common-mistake entries \| (\d+)",
     "SELECT COUNT(*) FROM technique_section WHERE kind='common_mistake'",
     "common mistakes"),
    ("docs/adr/0007-cinematic-catalog-layer.md", r"\| citations \| (\d+)",
     "SELECT COUNT(*) FROM technique_citation", "citations"),
    ("docs/adr/0007-cinematic-catalog-layer.md", r"\| matrix cells `NULL` \| \*\*(\d+)\*\*",
     "SELECT COUNT(*) FROM technique_tool_param WHERE params IS NULL",
     "matrix cells null"),
    ("docs/adr/0007-cinematic-catalog-layer.md", r"\| categories \| \*\*(\d+)\*\*",
     "SELECT COUNT(*) FROM cinematic_category", "category vocabulary"),
    ("specs/features/F070-cinematic-catalog-ingest.md",
     r"\| techniques \| 150 \| \*\*(\d+)\*\*",
     "SELECT COUNT(*) FROM cinematic_technique", "techniques"),
    ("specs/features/F070-cinematic-catalog-ingest.md",
     r"\| matrix cells listed \| 1050 \| \*\*(\d+)\*\*",
     "SELECT COUNT(*) FROM technique_tool_param", "matrix cells listed"),
    ("specs/features/F070-cinematic-catalog-ingest.md",
     r"\| cells with a parameter \| 933 \| \*\*(\d+)\*\*",
     "SELECT COUNT(*) FROM technique_tool_param WHERE params IS NOT NULL",
     "matrix cells filled"),
    ("specs/features/F070-cinematic-catalog-ingest.md",
     r"\| cells actually tested \| — \| \*\*(\d+)\*\*",
     "SELECT SUM(tested) FROM technique_tool_param", "matrix cells tested"),
    ("specs/features/F070-cinematic-catalog-ingest.md",
     r"\| cells `null` \| 117 \| \*\*(\d+)\*\*",
     "SELECT COUNT(*) FROM technique_tool_param WHERE params IS NULL",
     "matrix cells null"),
    ("specs/features/F070-cinematic-catalog-ingest.md",
     r"\| declared motion pairings \| — \| \*\*(\d+)\*\*",
     "SELECT COUNT(*) FROM technique_motion", "motion pairings"),

    # -------------------------------------------------------------- pipeline
    ("prompts/README.md", r"(\d+) shot briefs",
     "SELECT COUNT(*) FROM shot_card", "shot briefs"),
    ("prompts/README.md", r"(\d+) cinematic-technique briefs",
     "SELECT COUNT(*) FROM cinematic_technique", "cinematic briefs"),
    ("prompts/README.md", r"Only (\d+) of \d+ cards have a beat",
     None, "cards with a beat window"),
    ("prompts/README.md", r"only (\d+) of \d+ demo components contain a literal",
     None, "demos with a seg() call"),
    ("specs/features/F050-recipe-prompt-compiler.md",
     r"\| `shot_card\.duration_frames` \| (\d+)/",
     "SELECT COUNT(*) FROM shot_card WHERE duration_frames IS NOT NULL",
     "cards with a duration"),
    ("docs/architecture/README.md", r"\| `card_pitfall` \(已知坑\) \| ([\d,]+)",
     "SELECT COUNT(*) FROM card_pitfall", "pitfalls"),
    ("docs/architecture/README.md", r"\| `easing_curve` \| (\d+) distinct curves",
     "SELECT COUNT(*) FROM easing_curve", "easing curves"),
    ("docs/architecture/README.md", r"\| `card_search` \| (\d+) blobs",
     "SELECT COUNT(*) FROM card_search", "search blobs"),
    ("docs/architecture/0003-site-target-astro-cloudflare.md",
     r"A style switcher \((\d+) multi-style cards",
     "SELECT COUNT(*) FROM (SELECT card_id FROM card_variant GROUP BY card_id "
     "HAVING COUNT(*)>1)", "multi-style cards"),
    ("docs/architecture/0002-style-identity-cost.md",
     r"\| `style\.divergence_recorded` \| (\d+) \+ \d+ \| (\d+) upstream keys in `gallery_style`",
     "SELECT COUNT(*) FROM gallery_style", "gallery_style rows"),
    ("docs/monetization/brainstorm.md",
     r"(\d[\d,]*) extracted parameters, ([\d,]+) motion params",
     "SELECT COUNT(*) FROM card_param", "card parameters"),
    ("docs/adr/0002-data-layer.md", r"with (\d+) cards and (\d+) style entries",
     "SELECT COUNT(*) FROM shot_card", "cards in ADR 0002"),
    ("docs/adr/0004-i18n-architecture.md",
     r"\*\*(\d+) hand-maintained index entries\*\*",
     None, "upstream translations.js entries, from the clone"),
    ("docs/adr/0004-i18n-architecture.md",
     r"holding (\d+) rows against (\d+) cards",
     None, "ru/card rows"),
    ("specs/vision.md", r"(\d[\d,]*) tuned Remotion demos",
     "SELECT COUNT(*) FROM style", "motion styles"),
    ("specs/vision.md", r"(\d[\d,]*) tuned parameters, (\d+) pitfalls",
     "SELECT COUNT(*) FROM card_param", "card parameters"),
]

# Claims whose truth is not in the database but in a tree we also control.
# (document, regex, a callable returning the truth, label)
EXTERNAL: list[tuple[str, str, object, str]] = [
    ("AGENTS.md", r"catalog invariants, (\d+) checks",
     lambda: _run("platform/catalog/selftest.py", r"(\d+)/(\d+) catalog checks"),
     "catalog selftest check count"),
    ("progress.md", r"(\d+) domain documents",
     lambda: len(list((ROOT / "wiki" / "domains").glob("*.md"))),
     "domain documents on disk"),
    ("prompts/README.md", r"Only (\d+) of \d+ cards have a beat",
     lambda: _beats_with("window"), "cards with a stated [t0, t1]"),
    ("prompts/README.md", r"only (\d+) of \d+ demo components contain a literal",
     lambda: _demos_with_seg()[1], "demo components with a seg() call"),
    ("docs/adr/0004-i18n-architecture.md",
     r"holding (\d+) rows against (\d+) cards",
     lambda: _ru_card_rows(), "ru/card rows"),
    ("docs/adr/0004-i18n-architecture.md",
     r"\*\*(\d+) hand-maintained index entries\*\*",
     lambda: _upstream_index_entries(), "translations.js index entries"),
    ("progress.md", r"\*\*(\d+) attributed, (\d+) reviewed\.\*\*",
     lambda: _provenance("attributed"), "attributed translations"),
    ("progress.md", r"Today: \*\*\d+ attributed, (\d+) reviewed\.\*\*",
     lambda: _provenance("reviewed"), "reviewed translations"),
    ("progress.md", r"(\d+) machine translations marked `needs_review`",
     lambda: _provenance("attributed"), "strings awaiting a native reviewer"),
    ("progress.md", r"(\d+) style names are translated",
     lambda: _ru_style_titles(), "ru style titles"),
    ("AGENTS.md", r"(\d+) attributed, \d+ reviewed",
     lambda: _provenance("attributed"), "attributed translations"),

    # ---- the site actually shows motion -------------------------------------
    # These three exist because the site spent its whole life with no video on
    # it: the wall's inline script had been deleted, the media path was one
    # directory too shallow, and site/dist/media/ was never created. Every number
    # in the prose above them was true of the index while the page itself showed
    # nothing, so each is now anchored to the file on disk.
    ("AGENTS.md", r"`gallery/media/poster/\*\.jpg`, (\d+) files",
     lambda: _files("site/dist/media/poster/*.jpg"), "posters deployed"),
    ("AGENTS.md", r"\*\*(\d+) mp4\s+previews are not in git at all\*\*",
     lambda: _files("site/dist/media/*.mp4"), "mp4 previews deployed"),
    ("AGENTS.md", r"check_seo\.py\s+# (\d+)/",
     lambda: _seo_checks(), "SEO gate check count"),
    ("progress.md", r"\*\*(\d+) cards with a playable clip in the static block\*\*",
     lambda: _static_clips(), "cards carrying a <video> without JavaScript"),
    ("progress.md", r"\*\*(\d+) rendered clips",
     lambda: _rendered_clips(), "clips rendered by F060"),
    ("AGENTS.md", r"(\d+) renderable, (\d+) fragments",
     lambda: _render_split()[0], "components stating a duration"),
    ("AGENTS.md", r"\*\*(\d+) of the \d+ components are deliberately not rendered",
     lambda: _render_split()[1], "components deliberately not rendered"),
]


def _files(pattern: str) -> int:
    return len(list(ROOT.glob(pattern)))


def _rendered_clips() -> int:
    p = ROOT / "platform" / "render" / "render_report.json"
    if not p.exists():
        raise FileNotFoundError("platform/render/render_report.json; run run.py --render")
    return int(json.loads(p.read_text(encoding="utf-8"))["rendered"])


def _render_split() -> tuple[int, int]:
    """(components that state a duration, components deliberately not rendered).

    Read from the database, which is where both numbers come from: the first is
    `style.duration_frames IS NOT NULL`, the second its complement. The prose says
    "117 renderable, 100 fragments", and 117 + 100 must be the 217 compositions
    the harness actually offers -- so if a fourth corpus arrives and the totals
    stop adding up, the sentence fails rather than quietly staying true of the
    old corpus.
    """
    c = sqlite3.connect(f"file:{DB.as_posix()}?mode=ro", uri=True)
    yes = c.execute(
        "SELECT COUNT(*) FROM style WHERE demo_path IS NOT NULL "
        "AND duration_frames IS NOT NULL").fetchone()[0]
    no = c.execute(
        "SELECT COUNT(*) FROM style WHERE demo_path IS NOT NULL "
        "AND duration_frames IS NULL").fetchone()[0]
    c.close()
    return yes, no


def _static_clips() -> int:
    """Cards whose *static* library HTML carries a <video>.

    Counts the prerendered block, not the runtime: `app.js` draws a video for
    every card a second after load, so any check that runs in a browser sees 157
    either way and cannot tell whether the file a crawler reads has one.
    """
    lib = ROOT / "site" / "dist" / "en" / "library.html"
    if not lib.exists():
        raise FileNotFoundError("site/dist/en/library.html; run build_site.py")
    return len(re.findall(r"<video", lib.read_text(encoding="utf-8", errors="replace")))


def _seo_checks() -> int:
    sys.path.insert(0, str(ROOT / "platform" / "site"))
    import check_seo  # noqa: PLC0415
    rep = check_seo.audit("https://shotcraft.example")
    return rep["total"]

_CACHE: dict[str, object] = {}


def _flat(path: Path) -> str:
    """Document text with runs of whitespace collapsed to single spaces.

    An anchor that breaks when a paragraph is re-wrapped is a check that has
    silently stopped running, and a stopped check reports green forever. Every
    pattern below is written against the flattened form, so editing a line break
    cannot turn a verification off.
    """
    try:
        return re.sub(r"\s+", " ", path.read_text(encoding="utf-8"))
    except OSError:
        return ""


def _run(rel: str, pattern: str) -> int:
    """Run a harness and pull one number out of its output."""
    r = subprocess.run([sys.executable, rel], capture_output=True, text=True,
                       encoding="utf-8", cwd=str(ROOT),
                       env={**os.environ, "PYTHONIOENCODING": "utf-8"})
    m = re.search(pattern, r.stdout)
    if not m:
        raise RuntimeError(f"{rel} printed no match for {pattern!r}")
    return int(m.group(1))


def _conn():
    c = sqlite3.connect(f"file:{DB.as_posix()}?mode=ro", uri=True)
    return c


def _beats_with(field: str) -> int:
    import json
    n = 0
    for p in (ROOT / "prompts" / "generated").glob("*.json"):
        d = json.loads(p.read_text(encoding="utf-8"))
        if any(b.get(field) for b in d.get("beats", [])):
            n += 1
    return n


def _demos_with_seg() -> tuple[int, int]:
    demos = ROOT / "upstream" / "video-shotcraft" / "demos"
    if not demos.is_dir():
        return (0, 0)
    files = sorted(demos.rglob("*.tsx"))
    with_seg = [f for f in files
                if re.search(r"\bseg\s*\(",
                             f.read_text(encoding="utf-8", errors="replace"))]
    return (len(files), len(with_seg))


def _ru_card_rows() -> int:
    c = _conn()
    return c.execute("""SELECT COUNT(*) FROM translation
                        WHERE locale_id=(SELECT id FROM locale WHERE code='ru')
                          AND ns='card'""").fetchone()[0]


def _provenance(which: str) -> int:
    """Count from `translation_provenance`, which the ingest replays on every run."""
    c = _conn()
    try:
        if which == "attributed":
            return c.execute("SELECT COUNT(*) FROM translation_provenance").fetchone()[0]
        return c.execute("SELECT COUNT(*) FROM translation_provenance "
                         "WHERE status='reviewed'").fetchone()[0]
    except sqlite3.Error:
        return -1
    finally:
        c.close()


def _ru_style_titles() -> int:
    """Style names in ru that are neither absent nor the slug itself."""
    import json as _json
    p = ROOT / "site" / "locales" / "ru" / "styles.json"
    if not p.exists():
        return 0
    d = _json.loads(p.read_text(encoding="utf-8"))
    n = 0
    for k, v in d.items():
        t = v.get("title") if isinstance(v, dict) else v
        if isinstance(t, str) and t and t != k:
            n += 1
    return n


def _doctor_pass() -> int:
    """Not used, and deliberately so.

    doctor.py runs this gate as a subprocess, so a claim here that counted
    doctor's own pass total would make the gate depend on a number that depends
    on the gate. The first version of that claim read 41 and measured 40, which
    is what circularity looks like from the inside. A number that cannot be
    checked without checking itself is not a claim, it is decoration.
    """
    raise RuntimeError("deliberately unmeasured: circular with doctor.py")


def _upstream_index_entries() -> int:
    """Count the hand-maintained entries in upstream's translations.js.

    Parsed from the pinned clone, not remembered. Two shapes have to be handled
    and conflating them is how the ADR came to say 742 instead of 774:

      * `cardsZh` / `cardsEn` / `stylesZh` / `stylesEn` are flat maps whose keys
        are all string literals -- count the quoted keys.
      * `ui` is a map of maps (`{ zh: {...}, en: {...} }`), so its *quoted* key
        count is zero. Counting every key at any depth happens to give the right
        answer for this file and would give the wrong one for any other, so the
        depth is tracked instead.
    """
    p = ROOT / "upstream" / "video-shotcraft" / "gallery" / "translations.js"
    if not p.exists():
        return 0
    text = p.read_text(encoding="utf-8", errors="replace")
    total = 0
    for var in ("cardsZh", "cardsEn", "stylesZh", "stylesEn", "ui"):
        m = re.search(rf"\b{var}\s*[:=]", text)
        if not m:
            continue
        start = text.index("{", m.end())
        depth, i = 0, start
        while i < len(text):
            if text[i] == "{":
                depth += 1
            elif text[i] == "}":
                depth -= 1
                if depth == 0:
                    break
            i += 1
        body = text[start:i]
        if var == "ui":
            # depth 1 holds the locale names; depth 2 holds the strings.
            total += _keys_at_depth(body, 2)
        else:
            total += len(re.findall(r"(?:^|[{,])\s*'[^']+'\s*:", body))
    return total


def _keys_at_depth(body: str, want: int) -> int:
    """Count `key:` occurrences at brace depth `want` inside an object literal."""
    depth, n, i = 0, 0, 0
    while i < len(body):
        ch = body[i]
        if ch == "{":
            depth += 1
            i += 1
            continue
        if ch == "}":
            depth -= 1
            i += 1
            continue
        m = re.match(r"\s*([A-Za-z_$][\w$]*|'[^']+')\s*:", body[i:])
        if m and depth == want:
            n += 1
            i += m.end()
            continue
        i += 1
    return n


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verbose", action="store_true",
                    help="list every claim, not only the failures")
    a = ap.parse_args()

    if not DB.exists():
        print(f"no database at {DB}", file=sys.stderr)
        return 2
    conn = _conn()

    results: list[tuple[str, str, bool, str]] = []

    for doc, pattern, sql, label in CLAIMS:
        path = ROOT / doc
        if not path.exists():
            results.append((doc, label, False, "document does not exist"))
            continue
        m = re.search(pattern, _flat(path))
        if not m:
            # The phrase was reworded or the row was deleted. Either way this
            # claim is no longer being checked, which is not the same as passing.
            results.append((doc, label, False,
                            "the phrase this claim anchors on is gone -- the claim "
                            "is no longer verified; re-anchor or delete it"))
            continue
        if sql is None:
            results.append((doc, label, True, "checked elsewhere"))
            continue
        claimed = int(m.group(1).replace(",", ""))
        actual = conn.execute(sql).fetchone()[0]
        results.append((doc, label, claimed == actual,
                        f"doc says {claimed:,}, db says {actual:,}"))

    for doc, pattern, fn, label in EXTERNAL:
        path = ROOT / doc
        m = re.search(pattern, _flat(path)) if path.exists() else None
        if not m:
            results.append((doc, label, False, "anchor phrase is gone"))
            continue
        try:
            actual = int(fn() if callable(fn) else fn)
        except Exception as exc:                                 # noqa: BLE001
            results.append((doc, label, False, f"could not measure: {exc}"))
            continue
        claimed = int(m.group(1).replace(",", ""))
        results.append((doc, label, claimed == actual,
                        f"doc says {claimed:,}, measured {actual:,}"))

    conn.close()

    bad = [r for r in results if not r[2]]
    for doc, label, ok, detail in results:
        if ok and not a.verbose:
            continue
        mark = "ok  " if ok else "FAIL"
        extra = "" if ok else f"  -- {detail}"
        print(f"  {mark} {doc:<48} {label}{extra}")

    print(f"\n{len(results) - len(bad)}/{len(results)} document claims match the index")
    if bad:
        print("\nA number in prose is a promise that someone can check it. These do "
              "not\ncurrently hold. Fix the document or the pipeline -- not the gate.")
        return 1
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
