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
```

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