# AGENTS.md

Project conventions for this workspace. Read before changing anything.

## What this repo is

A platform built **beside** an upstream open-source project
(`upstream/video-shotcraft`, Apache-2.0), not a fork of it.

- **Upstream is read-only.** `upstream/video-shotcraft/` is a pinned clone and is
  git-ignored. Never edit it. Never commit it.
- **Our work lives in** `platform/`, `wiki/`, `site/`, `docs/`, `specs/`.
- The database (`platform/db/shotcraft.db`) is the single source of truth for
  every index. Downstream consumers read the DB, never upstream markdown/TSX.

## Routing

| situation | agent |
|---|---|
| "where is X", "how does Y work", "which cards fit Z" | `explorer` |
| "which cinematic techniques fit this brief", "what are the Kling params for X" | `explorer` |
| make the change for the current feature | `implementer` |
| prove a feature works end to end, then set `passes` | `verifier` |
| run a build/render/mirror that produces lots of output | `runner` |

See `.opencode/agents/README.md`. **`verifier` is the only role allowed to set
`passes: true` in `specs/feature-list.json`.**

## Hard rules

1. **`upstream/` is never modified.** If a task appears to need it, the task is
   mis-specified.
2. **The DB is generated.** Edit `platform/ingest/schema.sql` or the parsers, not
   `shotcraft.db`. Re-run the ingest.
3. **`wiki/` is generated.** Edit `platform/wiki/build_wiki.py`, not the markdown.
   Hand-editing is a bug.
4. **Prose from upstream is stored twice** — verbatim plus normalized. Never
   replace the verbatim column with the normalized value; the parenthetical
   rationale in `能量` is the signal.
5. **Card↔style links come from the demo directory**, not from
   `gallery/api/library.json`. Upstream's file is lossy (31 keys have no matching
   demo). Divergences go in `gallery_style`, not into the bin.
6. **Search must cascade**: `unicode61` → `trigram` (≥3 chars) → `LIKE`.
   `unicode61` cannot match inside a Chinese phrase; `trigram` cannot do 1–2
   character queries. Both facts were found by testing.
7. **FTS5 is matched by table name, never by alias** — `alias MATCH` raises
   `no such column`. Resolve hits through a CTE.
8. **`data/cinematic/` is source and is versioned with us; `upstream/` is source
   and is pinned to someone else's SHA.** Two corpora, one DB (ADR 0007). Never
   edit `data/cinematic/*.md` from a generator, and never let an ingest write
   into it. `[Subject]` in a prompt is a slot, not a token to expand.

## Commands

```powershell
scripts\init.ps1                              # clone + ingest + wiki, idempotent
python platform/ingest/run.py                 # upstream tree -> shotcraft.db
python platform/wiki/build_wiki.py            # DB -> wiki/
python platform/query.py stats                # the numbers everything quotes
python platform/query.py cards --energy high --max-frames 60
python platform/query.py card crash-zoom-punch # params + pitfalls + styles
python platform/query.py search 弹簧           # works in zh, en and slugs
python platform/mirror_site.py --media        # live site + mp4 release
python platform/bump_upstream.py --check      # has upstream moved?
python platform/brand_kit.py install shotcraft   # brand over the template
python platform/catalog/import_cinematique.py     # re-import the catalog corpus
python platform/catalog/build_briefs.py --lint    # 150 cinematic.brief/1 files
python platform/catalog/selftest.py           # catalog invariants, 31 checks
python platform/query.py technique --category lighting
python platform/query.py technique-motions dolly-shot
python platform/query.py optimize-all dolly-shot   # every tool, every tested flag
```

An absent `data/cinematic/` is a WARN, not a failure — either corpus builds alone.
The catalog is **150 techniques imported from the MIT-licensed `cinematique`
project**, not authored here; 791 of 1050 cross-tool cells are filled and
**0 are tested**, because the source matrix records a `FILLED`/`TODO` status and
no verification column. A bump is `git clone && python
platform/catalog/import_cinematique.py && git diff`.

## Gates

Every one of these has caught a real defect. `scripts\init.ps1` runs the first
four and fails if any does.

```powershell
python platform/doctor.py                     # 0 error / 7 warn / 41 pass
python platform/docs_freshness.py             # 67/67 claims, 7 negative tests
python platform/catalog/layer_gate.py         # no feature claims done that is not
python platform/catalog/selftest.py           # 31/31
python platform/api/selftest.py               # 53/53
python platform/site/selftest.py              # 99/99, real Chrome
python platform/wiki/audit_quality.py         # 28/28, 24 craft questions
python platform/prompts/build_prompts.py --lint
python platform/site/check_coverage.py        # en 100%, zh 99.7%, ru 99.7%
python platform/site/translate.py report      # 371 attributed, 0 reviewed
python platform/_gate_test.py                 # proves docs_freshness can fail
```

`platform/site/translate.py` is the i18n worklist. `list` for what to translate,
`apply` for a batch, `verify` for what is left, `prune` for placeholder entries
that have no source, `report` for who wrote what. It refuses a value equal to the
slug, a value copied from another locale, a value still in CJK, and a string with
untranslated latin words in it — each of which is a way a machine pass looks
finished and is not.

**Authorship is replayed, not stored.** `translation_provenance` is derived from
the committed `site/locales/_batch_*.json` files, because `run.py` deletes and
rebuilds the database on every run and a provenance column on a derived table
survives exactly until the next ingest. A batch may claim `reviewed` only by
naming a `reviewed_by`; nothing in this repo can upgrade its own work.

`platform/docs_freshness.py` is the one people forget exists. A number written in
prose is a promise that someone can check it, and this is the checker: 67 claims
across the narrative docs, each verified against the index. A claim whose anchor
phrase is gone is reported as **no longer verified** rather than passing, because
a check that switches off when a paragraph is rewrapped is a check that has
stopped working.

When you write a number into a document that the index can answer, add it to the
`CLAIMS` list in that file. That is the whole discipline.

`platform/catalog/layer_gate.py` is the one to run before trusting the ledger: it
re-runs each passing feature's cited verification and fails if it no longer
holds. A `verified_by` note is an assertion; running it is evidence.

Set `$env:PYTHONIOENCODING="utf-8"` before any of these on Windows, or CJK
output prints as `?`. The files themselves are correct UTF-8 — the console is
the problem.

## Decisions

Read `docs/adr/` before proposing an architecture change:

| ADR | decision |
|---|---|
| 0001 | monorepo, upstream pinned and read-only |
| 0002 | SQLite + FTS5 as the single index |
| 0003 | the LLM wiki is generated, never hand-written |
| 0004 | i18n: JSON dictionaries, locale-prefixed URLs, hreflang |
| 0005 | independent fork, own brand, upstream credited |
| 0006 | SDD loop with a verifier-owned completion gate |
| 0007 | the cinematic-technique catalog is a second corpus in the same DB |

## Money and licensing

Two things an LLM will get confidently wrong if not told:

- **The Apache-2.0 core is free to fork and resell.** Anything we sell must be an
  outcome, a service, or support.
- **Remotion requires a paid licence for companies, and `video-talkcraft` is
  PolyForm Noncommercial.** Both are hard constraints, not preferences. See
  `docs/monetization/brainstorm.md`.

## Commit discipline

- One commit per feature, message references the feature id: `F012: locale URLs + hreflang`.
- Generated artefacts go in the same commit as the generator change that
  produced them, so no diff ever shows output without its cause.
- Upstream bumps are their own commit: re-run ingest, regenerate, review the
  `wiki/index.json` stats diff.