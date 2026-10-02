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
9. **A test that reads the DOM after JavaScript has run cannot see a static
   defect.** This repo shipped a home page whose 16-clip motion wall had been
   deleted along with an inline dictionary, with the media path left one
   directory too shallow, and with `site/dist/media/` absent because a symlink
   raised `OSError` and the handler was `pass`. Every gate was green. The checks
   that found all three read the *static file* and look for the thing itself:
   `createElement('video')`, `../media/`, `<video` in the prerendered block.
   When a check can be written against the file on disk, write it there.

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

**The site has two media sources and neither is obvious.** `upstream/`'s git tree
holds **posters only** — `gallery/media/poster/*.jpg`, 64 files. The **214 mp4
previews are not in git at all**; they are GitHub release assets, downloaded by
`platform/mirror_site.py --media` into `upstream/site-mirror/media/`. A fresh
clone therefore builds a site that calls itself a catalogue of motion and has
nothing to play, and it does so without an error. `build_site.py` reports that
as a **warning** and `platform/site/check_seo.py` **fails** on it — one gate,
one authority. `mirror_site.py --media` is 128 MB and is not part of
`scripts\init.ps1`.

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
python platform/site/check_seo.py             # 369/369
python platform/site/translate.py report      # 371 attributed, 0 reviewed
python platform/render/run.py --list          # 118 renderable, 100 fragments
python platform/render/run.py --verify        # every claimed clip, frame-exact
python platform/_gate_test.py                 # proves docs_freshness can fail
```

`platform/render/run.py` is F060 and the only slow thing here. `--install` copies
the template into `platform/render/.work/` (never into `upstream/`, which is
read-only), discovers the external modules the demos import and adds the ones the
template's `package.json` omits, then installs. `--render` writes MP4s to
`render/out/` and a report to `platform/render/render_report.json`; `--verify`
reads each clip back with `ffprobe` and compares the frame count against the
index.

**118 of the 218 components state a duration and 117 are rendered.** The two
counts differ by one, and the difference is not an off-by-one: the harness joins
through `card_variant`, and `clip-card-looping` (120 frames, renderable) has no
card link — upstream has no card for it. So `--list` offers **217**
compositions, of which 117 state a duration.

**100 of the 218 components are deliberately not rendered.** They state no
duration — they are timeline fragments, not standalone films, and the seven that
export something duration-shaped export `BEAT_LEN=18` or `FPS=30`, neither of
which is a length. Rendering them at a guessed frame count produces a clip of the
wrong size that passes every byte-level check. `--include-unspecified` does it
anyway and labels every one.

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

Three things an LLM will get confidently wrong if not told:

- **The Apache-2.0 core is free to fork and resell.** Anything we sell must be an
  outcome, a service, or support.
- **Remotion's paid tier applies to companies above three people, not to
  individuals.** This repo is rendered by an individual, so the free tier applies
  and `platform/render/run.py` runs. Do not re-block the render on the strength of
  the licence alone — see the correction in
  `docs/monetization/0002-blocking-issues.md`. What matters is *which kind* of fact
  it is: a licence term binds whoever ships the code, a free tier is a fact about
  who is running it.
- **`video-talkcraft` is PolyForm Noncommercial** and that one *is* a hard
  constraint, because it binds whoever ships the code. We do not deliver it
  commercially.

## Commit discipline

- One commit per feature, message references the feature id: `F012: locale URLs + hreflang`.
- Generated artefacts go in the same commit as the generator change that
  produced them, so no diff ever shows output without its cause.
- Upstream bumps are their own commit: re-run ingest, regenerate, review the
  `wiki/index.json` stats diff.