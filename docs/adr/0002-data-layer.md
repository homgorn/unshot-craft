# ADR 0002 — SQLite + FTS5 as the single index

- Status: accepted (in force — `platform/db/shotcraft.db`)
- Decided: 2026-10-01
- Supersedes: nothing

## Context

The upstream repo publishes `gallery/api/library.json`: a single-line JSON file
with 157 cards and 214 style entries. It is a *rendering* artifact for one
hand-written vanilla-JS gallery. It cannot carry what we need:

| Need | `library.json` | Verdict |
|---|---|---|
| Per-card parameter table (`## 参数表`) | absent — prose in the `.md` | not modelled |
| Extracted easing curves from the `.tsx` | absent | not modelled |
| 9 locales | absent (dictionaries live in `translations.js`) | not modelled |
| Audio licence provenance | absent (lives in a Markdown table) | not modelled |
| Card↔implementation join | filename convention only | unreliable (see ADR 0006) |
| Search | none | absent |

Every downstream consumer — LLM wiki, localized site, future SaaS — needs the
same rows exactly once. Three consumers reading three hand-maintained files is
how the drift we already found gets in.

## Decision

Use SQLite with FTS5 as the **only** index. `platform/ingest/` reads the pinned
upstream checkout and writes one database. Wiki, site and API are all *projections*
of that database.

## Rationale

- 157 cards × 9 locales × ~6 derived fields is a relational shape, not a document.
- SQLite ships with Python. No service to run, no migration toolchain, and the
  whole index is a 7 MB file that can be committed, diffed and shipped as an artifact.
- FTS5 gives us `unicode61` (word matching) **and** `trigram` (CJK substring
  matching) in the same file. CJK is why this is not Postgres FTS out of the box —
  we would need a separate CJK tokenizer for the same rows.
- Read-only access is how consumers open it. The DB is written exactly once, by
  ingest, and everything else is a `SELECT`.

## Consequences

Good:
- One ingest, N consumers. Adding a consumer costs a query, not an upstream PR.
- The database is a testable artifact: `platform/doctor.py` asserts invariants
  against it without a running server.
- Provenance is a first-class concern: `source_file.sha256` + `source_commit`
  mean every row can be traced to a byte and a commit.

Bad, and accepted:
- SQLite is not concurrent-write friendly. Accepted because there is exactly one writer.
- The DB is a derived artifact and can be rebuilt at any time. Therefore **nothing
  hand-edits it** — if you need a new field, change `schema.sql` and the ingest.
- Schema drift is the failure mode to fear: a DB built from an older `schema.sql`
  than the current code. `doctor.py` guards the specific instances we hit.

## Alternatives rejected

- **Parse `library.json` directly at build time.** Rejected: it is lossy exactly
  where our value is (params, easings, per-style descriptions, audio provenance).
- **Postgres + pgvector.** Rejected as premature: one writer, one process, no
  concurrent readers needing isolation. Revisit if the render-farm SaaS lands —
  that is the first feature that needs real concurrency.
- **Keep Markdown as the source and query it at request time.** Rejected: no
  structural query, no FTS, and every page would re-parse 157 files.