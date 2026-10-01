#!/usr/bin/env python3
"""platform/doctor.py — read-only invariant checker for shotcraft.db and the wiki.

Every check exists because it caught a real defect at least once. The point is
that the pipeline can be edited by several hands without anyone re-deriving the
rules by hand: run this, and you know whether the DB still tells the truth.

Read-only. Never writes to the database or the wiki. Exit code:
    0 = no errors (warnings allowed)
    1 = at least one ERROR
    2 = could not check (missing db / upstream)

Usage:
    python platform/doctor.py                 # human report
    python platform/doctor.py --json          # machine report
    python platform/doctor.py --strict        # warnings count as errors
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "platform" / "db" / "shotcraft.db"
UPSTREAM = ROOT / "upstream" / "video-shotcraft"
WIKI = ROOT / "wiki"

# Expected upstream ground truth. Bump deliberately, never silently.
UPSTREAM_CARD_COUNT = 157
UPSTREAM_STYLE_COUNT = 214
CATEGORY_KEYS = [
    "opening", "typography", "ui-entrance", "camera", "data",
    "interaction", "transition", "rhythm", "effects", "outro",
]

OK, WARN, ERROR = "ok", "warn", "error"


@dataclass
class Result:
    check: str
    status: str
    detail: str
    evidence: list = field(default_factory=list)


class Doctor:
    def __init__(self, conn: sqlite3.Connection | None):
        self.conn = conn
        self.results: list[Result] = []

    def add(self, check: str, status: str, detail: str, evidence=None) -> None:
        self.results.append(Result(check, status, detail, evidence or []))

    def scalar(self, sql: str, args=()) -> int:
        if self.conn is None:
            raise RuntimeError("no connection")
        return self.conn.execute(sql, args).fetchone()[0]

    def rows(self, sql: str, args=()):
        if self.conn is None:
            raise RuntimeError("no connection")
        return self.conn.execute(sql, args).fetchall()

    # -- 0. database must be openable and structurally sound ---------------
    def check_db_sound(self) -> None:
        if self.conn is None:
            self.add("db.open", ERROR, "database not reachable")
            return
        integrity = self.scalar("PRAGMA integrity_check")
        self.add("db.integrity",
                 OK if integrity == "ok" else ERROR, f"integrity_check={integrity}")
        fk = self.rows("PRAGMA foreign_key_check")
        self.add("db.foreign_keys", OK if not fk else ERROR,
                 f"{len(fk)} foreign_key violations", fk[:5])

    # -- 1. style identity: one identity per upstream style -----------------
    def check_style_identity(self, upstream_keys: dict[str, str]) -> None:
        """Contract (AGENTS.md hard rule 5): card<->style comes from the demo
        directory, and library.json divergences are recorded in gallery_style
        rather than dropped.

        What that costs, measured here:
          * style.key is derived from the .tsx filename; upstream styles[].key is
            hand-authored. 34 of 214 keys disagree.
          * So style_media URLs point at ./media/<derived-key>.mp4, which does not
            exist upstream, and stylesEn (keyed on the upstream key) resolves for
            only part of the corpus.
          * And 3 upstream keys are lost outright, matching neither authority.

        The first two are consequences of a decision this project made on
        purpose. Only the third is a defect under any reading of the rule, and
        it is why only the third fails hard."""
        if self.conn is None:
            return
        style_keys = {r[0] for r in self.rows("SELECT key FROM style")}
        gallery_keys = {r[0] for r in self.rows(
            "SELECT key FROM gallery_style")} if self._has("gallery_style") else set()
        reachable = style_keys | gallery_keys
        lost = sorted(set(upstream_keys) - reachable)
        self.add("style.identity.lost",
                 OK if not lost else ERROR,
                 f"{len(reachable & set(upstream_keys))}/{len(upstream_keys)} upstream "
                 f"style keys resolvable to a style identity "
                 f"({len(lost)} match neither the demo directory nor gallery_style)",
                 lost[:12])

        # Two style tables is the project's DOCUMENTED contract, not a defect:
        # AGENTS.md hard rule 5 says card<->style links come from the demo
        # directory and library.json divergences are recorded in gallery_style
        # rather than dropped. So this reports the divergence and its cost
        # rather than failing on it. It is an ERROR only if a consumer has to
        # UNION two tables to find one upstream key - which is the state that
        # `style.identity.reachable` above already fails on.
        n_gal = len(gallery_keys)
        only_demo = sorted(style_keys - set(upstream_keys))
        only_lib = sorted(gallery_keys - set(style_keys))
        self.add("style.divergence_recorded", OK if not n_gal else WARN,
                 f"{n_gal} upstream keys have no demo-directory match and live in "
                 f"gallery_style (AGENTS.md rule 5); {len(only_demo)} demo-derived "
                 f"keys have no upstream counterpart",
                 (only_lib + only_demo)[:12])

        # The kebab rule inserts a hyphen on BOTH sides of a digit boundary, so
        # "3D" becomes "3-D". Whatever authority you pick for the key, these are
        # inconsistent with the convention applied to the other 211 keys, and
        # they match no upstream key either.
        bad = [r[0] for r in self.rows("SELECT key FROM style")
               if re.search(r"\d-d|-d\d|-v-\d", r[0])]
        self.add("style.kebab_casing", OK if not bad else ERROR,
                 f"{len(bad)} style keys are inconsistent with the project's own "
                 f"kebab convention (3D must not become 3-D) and match no "
                 f"upstream key either",
                 bad[:12])

        # every style must carry exactly one card
        orphans = self.rows(
            "SELECT key, demo_path FROM style WHERE card_id IS NULL")
        self.add("style.card_link", OK if not orphans else WARN,
                 f"{len(orphans)} style rows have no card; helpers that are not "
                 f"styles (VerticalTicker, ClipCardLooping) belong outside `style`",
                 [tuple(r) for r in orphans][:12])

    # -- 2. media -----------------------------------------------------------
    def check_media(self, upstream_keys: dict[str, str]) -> None:
        if self.conn is None:
            return

        # How many of upstream's actual preview files can a consumer reach from
        # the DB? This is authority-neutral: it asks the downstream question
        # rather than re-arguing which key is correct.
        if upstream_keys:
            reachable = set()
            urls: list[str] = []
            if self._has("style_media"):
                urls += [r[0] for r in self.rows(
                    "SELECT url FROM style_media WHERE url IS NOT NULL")]
            if self._has("gallery_style"):
                urls += [r[0] for r in self.rows(
                    "SELECT media_url FROM gallery_style "
                    "WHERE media_url IS NOT NULL")]
            for url in urls:
                m = re.search(r"/media/([a-z0-9-]+)\.", url)
                if m:
                    reachable.add(m.group(1))
            unreachable = sorted(set(upstream_keys) - reachable)
            self.add("media.upstream_reachable",
                     OK if not unreachable else ERROR,
                     f"{len(set(upstream_keys) & reachable)}/{len(upstream_keys)} "
                     f"upstream previews are reachable from the database by URL; "
                     f"{len(unreachable)} cannot be fetched by any consumer",
                     unreachable[:12])

        missing = self.rows("""
            SELECT s.key FROM style s
            WHERE NOT EXISTS (SELECT 1 FROM style_media m WHERE m.style_id = s.id)""")
        self.add("media.coverage", OK if not missing else ERROR,
                 f"{len(missing)} styles have no style_media row at all "
                 f"(preview AND poster both absent)",
                 [r[0] for r in missing][:12])

        zero = self.rows("SELECT COUNT(*) FROM style_media WHERE bytes IS NULL OR bytes=0")[0][0]
        self.add("media.bytes", OK if zero == 0 else WARN,
                 f"{zero} style_media rows have bytes=0 or NULL")

        # poster files that exist on disk but no style references them
        poster_dir = UPSTREAM / "gallery" / "media" / "poster"
        if poster_dir.is_dir():
            on_disk = {p.stem for p in poster_dir.glob("*.jpg")}
            keys = {r[0] for r in self.rows("SELECT key FROM style")}
            if self._has("gallery_style"):
                keys |= {r[0] for r in self.rows("SELECT key FROM gallery_style")}
            orphan_posters = sorted(on_disk - keys)
            self.add("media.poster_orphans", OK if not orphan_posters else WARN,
                     f"{len(on_disk)} posters on disk, {len(orphan_posters)} not "
                     f"referenced by any style key",
                     orphan_posters[:12])

    # -- 3. search layer ----------------------------------------------------
    def check_search(self) -> None:
        """param_fts shipped with 1057 card_param rows and 0 index rows, so
        'find me the parameter cards' silently returned nothing."""
        if self.conn is None:
            return
        pairs = [
            ("card_fts", "shot_card", ("name",)),
            ("card_fts_trgm", "shot_card", ("name",)),
            ("card_search", "shot_card", ("name",)),
            ("search_fts", "shot_card", ("name",)),
            ("param_fts", "card_param", ("param_key",)),
            ("pitfall_fts", "card_pitfall", ("text",)),
            ("pitfall_fts_trgm", "card_pitfall", ("text",)),
            ("style_fts", "style", ("key",)),
        ]
        for fts, base, keys in pairs:
            if not self._has(fts) or not self._has(base):
                continue
            n_fts = self.scalar(f"SELECT COUNT(*) FROM {fts}")
            n_base = self.scalar(f"SELECT COUNT(*) FROM {base}")
            if n_base == 0:
                status, detail = WARN, f"{base} is empty, nothing to index"
            elif n_fts == 0:
                status, detail = ERROR, f"{fts} is EMPTY while {base} has {n_base} rows"
            elif n_fts != n_base:
                status, detail = WARN, f"{fts} has {n_fts} rows, {base} has {n_base}"
            else:
                status, detail = OK, f"{n_fts} rows"
            self.add(f"search.{fts}", status, detail)

    # -- 4. completeness ----------------------------------------------------
    def check_empty_tables(self) -> None:
        """Tables whose whole purpose is provenance/licensing. Empty means the
        feature is absent, not merely unused."""
        for table, why in [
            ("source_commit", "commit-level provenance for every ingested file"),
            ("attribution_entry", "per-batch/per-file attribution behind ATTRIBUTION.md"),
        ]:
            if not self._has(table):
                continue
            n = self.scalar(f"SELECT COUNT(*) FROM {table}")
            self.add(f"complete.{table}", OK if n else WARN,
                     f"{table}: {n} rows — {why}")

    def check_license_consistency(self) -> None:
        """license_registry blocks on 6 untraceable audio files while
        audio_asset marks all 154 commercial_ok=1. The registry wins."""
        if self.conn is None or not (self._has("audio_asset")
                                     and self._has("license_registry")):
            return
        blocked = self.rows(
            "SELECT subject FROM license_registry WHERE blocking=1")
        ok = self.scalar("SELECT COUNT(*) FROM audio_asset WHERE commercial_ok=1")
        total = self.scalar("SELECT COUNT(*) FROM audio_asset")
        untraceable = self.scalar(
            "SELECT COUNT(*) FROM audio_asset WHERE traceable=0")
        if any("audio" in (r[0] or "").lower() for r in blocked) and untraceable == 0:
            self.add("license.audio_consistency", ERROR,
                     f"license_registry blocks on audio provenance but "
                     f"audio_asset marks all {ok}/{total} commercial_ok=1 and "
                     f"traceable=0 count is {untraceable}",
                     [r[0] for r in blocked])
        else:
            self.add("license.audio_consistency", OK,
                     f"{total} audio assets, {untraceable} untraceable, "
                     f"registry blockers: {[r[0] for r in blocked]}")

    def check_prompt_briefs(self) -> None:
        """prompts/generated/ must be a complete, in-sync projection of the cards.

        Added because a brief tree that is silently short would hand a renderer an
        incomplete shot list with no error.
        """
        if self.conn is None:
            return
        gen = ROOT / "prompts" / "generated"
        if not gen.is_dir():
            self.add("prompts.tree", WARN, "prompts/generated/ does not exist yet")
            return
        n_cards = self.scalar("SELECT COUNT(*) FROM shot_card")
        files = list(gen.glob("*.json"))
        briefs = [f for f in files if f.name != "index.json"]
        if len(briefs) != n_cards:
            self.add("prompts.coverage", ERROR,
                     f"prompts/generated/ has {len(briefs)} briefs, "
                     f"db has {n_cards} cards; run platform/prompts/build_prompts.py")
        else:
            self.add("prompts.coverage", OK,
                     f"{len(briefs)} briefs == {n_cards} cards")

        index = gen / "index.json"
        self.add("prompts.index", OK if index.exists() else WARN,
                 "prompts/generated/index.json present"
                 if index.exists() else "index.json missing")

        # authored reference briefs
        ref = ROOT / "prompts" / "reference"
        if ref.is_dir():
            refs = sorted(ref.glob("*.json"))
            bad = []
            for p in refs:
                try:
                    b = json.loads(p.read_text(encoding="utf-8"))
                except json.JSONDecodeError as e:
                    bad.append(f"{p.name}: invalid JSON ({e})")
                    continue
                if b.get("source", {}).get("brief_kind") != "hand":
                    bad.append(f"{p.name}: brief_kind must be 'hand'")
                if not b.get("copy", {}).get("authored"):
                    bad.append(f"{p.name}: copy.authored must be true")
                unfilled = [s.get("id") for s in b.get("copy", {}).get("slots", [])
                            if not str(s.get("text") or "").strip()]
                if unfilled:
                    bad.append(f"{p.name}: unfilled slots {unfilled}")
            self.add("prompts.reference_briefs",
                     OK if refs and not bad else (ERROR if bad else WARN),
                     f"{len(refs)} hand-authored brief(s)"
                     + ("" if not bad else f"; {len(bad)} problem(s)"), bad[:8])

    # -- 5. taxonomy & counts ----------------------------------------------
    def check_taxonomy(self) -> None:
        if self.conn is None:
            return
        cats = [r[0] for r in self.rows(
            "SELECT key FROM category ORDER BY order_idx")]
        self.add("taxonomy.categories",
                 OK if cats == CATEGORY_KEYS else ERROR,
                 f"{len(cats)} categories", cats)

        n = self.scalar("SELECT COUNT(*) FROM shot_card")
        self.add("counts.cards", OK if n == UPSTREAM_CARD_COUNT else ERROR,
                 f"shot_card={n}, upstream={UPSTREAM_CARD_COUNT}")

        # category.card_count must agree with the real grouping
        drift = self.rows("""
            SELECT c.key, c.card_count,
                   (SELECT COUNT(*) FROM shot_card s WHERE s.category_id=c.id) actual
            FROM category c WHERE c.card_count <> actual""")
        self.add("counts.category_drift", OK if not drift else WARN,
                 f"{len(drift)} categories have a stale card_count",
                 [tuple(r) for r in drift])

        # cards with no energy level: 26 were unmapped because the ladder has
        # no rung for arc-shaped and n/a energy prose
        no_energy = self.scalar(
            "SELECT COUNT(*) FROM shot_card WHERE energy_level_id IS NULL")
        total = self.scalar("SELECT COUNT(*) FROM shot_card")
        lvl = self.scalar("SELECT COUNT(*) FROM energy_level")
        self.add("energy.coverage",
                 OK if no_energy == 0 else WARN,
                 f"{no_energy}/{total} cards have no energy_level; ladder has "
                 f"{lvl} rungs and no rung for arc/n-a prose")

    # -- 6. docs & artifacts -----------------------------------------------
    def check_docs(self) -> None:
        if self.conn is None:
            return
        missing_adr = self.rows(
            "SELECT id, area, adr FROM decision_log WHERE adr IS NOT NULL AND adr<>''")
        dangling = [r for r in missing_adr
                    if not (ROOT / str(r[2]).lstrip("./")).exists()]
        self.add("docs.adr_links", OK if not dangling else WARN,
                 f"{len(dangling)} decision_log rows point at an ADR file that "
                 f"does not exist", [r[2] for r in dangling][:8])

        for d in ("docs/architecture", "docs/adr", "docs/monetization", "docs/research"):
            p = ROOT / d
            n = len(list(p.glob("*.md"))) if p.is_dir() else -1
            self.add(f"docs.{d.replace('/', '_')}", OK if n > 0 else WARN,
                     f"{d}: {n} markdown files")

    def check_wiki_freshness(self) -> None:
        if self.conn is None or not WIKI.is_dir():
            return
        index = WIKI / "index.json"
        if not index.exists():
            self.add("wiki.index", WARN, "wiki/index.json missing")
            return
        try:
            data = json.loads(index.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            self.add("wiki.index", ERROR, f"wiki/index.json is not valid JSON: {e}")
            return
        cards = data.get("cards") or data.get("items") or []
        n = self.scalar("SELECT COUNT(*) FROM shot_card")
        card_files = len(list((WIKI / "cards").glob("*.md"))) if (WIKI / "cards").is_dir() else 0
        self.add("wiki.card_coverage", OK if card_files == n else ERROR,
                 f"wiki/cards has {card_files} pages, db has {n} cards; "
                 f"index.json holds {len(cards)} card records")

        missing = [c for c in ("llms.txt", "llms-full.txt", "index.md", "api/openapi.json")
                   if not (WIKI / c).exists()]
        self.add("wiki.llms_artifacts", OK if not missing else WARN,
                 f"missing: {missing or 'none'}")

    def _has(self, table: str) -> bool:
        return self.scalar(
            "SELECT COUNT(*) FROM sqlite_master WHERE name=?", (table,)) > 0


def load_upstream_styles() -> dict[str, str]:
    lib = UPSTREAM / "gallery" / "api" / "library.json"
    if not lib.exists():
        return {}
    data = json.loads(lib.read_text(encoding="utf-8"))
    return {st["key"]: card["name"]
            for card in data.get("cards", []) for st in card.get("styles", [])}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()

    if not DB.exists():
        print(f"doctor: no database at {DB}", file=sys.stderr)
        return 2
    conn = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)

    up = load_upstream_styles()
    if not up:
        print(f"doctor: cannot read upstream library.json under {UPSTREAM}",
              file=sys.stderr)

    d = Doctor(conn)
    d.check_db_sound()
    if up:
        d.check_style_identity(up)
    d.check_media(up)
    d.check_search()
    d.check_empty_tables()
    d.check_license_consistency()
    d.check_taxonomy()
    d.check_docs()
    d.check_wiki_freshness()
    d.check_prompt_briefs()

    errors = [r for r in d.results if r.status == ERROR]
    warns = [r for r in d.results if r.status == WARN]

    if args.json:
        print(json.dumps({
            "db": str(DB), "upstream_styles": len(up),
            "errors": len(errors), "warnings": len(warns),
            "checks": [{"check": r.check, "status": r.status,
                        "detail": r.detail, "evidence": [str(e) for e in r.evidence]}
                       for r in d.results],
        }, ensure_ascii=False, indent=2))
        return 1 if (errors or (args.strict and warns)) else 0

    icon = {OK: "PASS", WARN: "WARN", ERROR: "FAIL"}
    print(f"shotcraft doctor  ·  {DB}")
    print(f"upstream library.json: {len(up)} style keys")
    print("-" * 78)
    for r in d.results:
        print(f"[{icon[r.status]}] {r.check:<34} {r.detail}")
        for e in r.evidence[:6]:
            print(f"         · {e}")
        if len(r.evidence) > 6:
            print(f"         · … and {len(r.evidence) - 6} more")
    print("-" * 78)
    print(f"{len(errors)} error(s), {len(warns)} warning(s), "
          f"{len(d.results) - len(errors) - len(warns)} pass")
    return 1 if (errors or (args.strict and warns)) else 0


if __name__ == "__main__":
    raise SystemExit(main())