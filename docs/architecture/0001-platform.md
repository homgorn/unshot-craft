# SDD 0001 — Shotcraft platform architecture

- Status: current, living document
- Last verified against code: 2026-10-01, upstream SHA `5ddbf521038b0a7accfb6dc1e0a9eb29c67277ab`
- Verification tool: `python platform/doctor.py` → **6 errors, 12 warnings**
- ADRs: [0002 data layer](adr/0002-data-layer.md) · [0003 LLM wiki](adr/0003-llm-wiki.md) · [0004 i18n](adr/0004-i18n-architecture.md) · [0005 upstream policy](adr/0005-upstream-policy.md)

> Numbering note: the ADR series starts at 0002. Slots 0002–0005 are referenced by
> `decision_log.adr` and were written to match. **0001 is unaccounted for** — either
> it was never committed or it belongs to a retired decision. Resolve before adding
> new ADRs, or the series will acquire a second gap.

---

## 1. What this system is

One upstream repository (Apache-2.0, ~10.1k stars) describing 157 cinematic
motion-technique "shot recipe cards", each with a Markdown card, one or more Remotion
`.tsx` reference implementations, a motion preview MP4, and Chinese methodology docs.

We turn that into three products from one index: an **LLM wiki**, a **localized
site**, and eventually a **service**. All three are projections of one SQLite
database. None of them owns data.

## 2. Layer map

```
upstream/video-shotcraft/          pinned, READ-ONLY, Apache-2.0
  references/shots/<cat>/<slug>.md     157 cards  ─┐
  demos/<cat>/<slug>/<Comp>.tsx        216 comps   ─┤ ground truth
  gallery/api/library.json             214 styles ─┤ (hand-authored upstream)
  gallery/translations.js              742 index  ─┤
  assets/audio/**                      154 files ─┤
        │
        │  platform/ingest/run.py   (+ shotcraft_ingest/{parsing,motion}.py)
        ▼
platform/db/shotcraft.db            SQLite + FTS5, 39 tables, 9,394 rows, 7.3 MB
        │
        ├──► platform/wiki/build_wiki.py  ──► wiki/          (LLM surface)
        ├──► platform/mirror_site.py      ──► site/          (browser surface)
        ├──► platform/query.py            ──► CLI/stdin      (agent surface)
        └──► docs/, docs/monetization/    ──► human surface
```

Rule of the architecture: **everything below `platform/db/` is disposable.** If a
consumer is wrong, rebuild it. Nothing hand-edits generated output.

## 3. The core defect: `style.key` has two authorities

This is the single most important thing in this document, because it silently
corrupts every consumer.

Upstream has two identities for one style ("式"):

| Source | Example | Count |
|---|---|---|
| `library.json` → `styles[].key`, hand-authored | `basic-3d-scene`, `crash-zoom-punch`, `whip-pan` | **214** |
| `kebab(<Comp>.tsx)` filename, derived | `basic-3-dscene`, `crash-zoom-real`, `whip-pan-real` | **218** |

They disagree on **34 keys**, spanning **20 of the 157 cards**. Consequences,
all measured:

- `style_media` URLs point at `./media/<derived-key>.mp4`, which does not exist
  upstream. **35 styles have no media row at all**; 366 rows carry `bytes=0`.
- `stylesZh`/`stylesEn` join on the upstream key. The English style index resolves
  for only **96 of 214** — the rest have no English name and no English one-liner.
- `Basic3DScene` mangles to `basic-3-dscene`: the kebab rule inserts a hyphen on
  *both* sides of a digit boundary, so `3D` becomes `3-D`. Same for
  `Terminal3D → terminal-3-d`, `Carousel3D → carousel-3-d`, and every `…V2` file.
- Three upstream keys are **lost entirely** — `basic-3d-scene`, `carousel-3d`,
  `terminal-3d` — because fuzzy `norm()` matching also fails on the mangled form.
  Those three cards' previews are unreachable from the database.

The current mitigation is `gallery_style`, a second table holding the 31 unmatched
upstream keys. That is the wrong shape: it leaves two parallel style tables for
every consumer to `UNION`, and it still loses the three digit cases.

### The fix

Make **`library.json styles[].key` the single authority for style identity**, and
treat the `.tsx` file as the *implementation* of that identity rather than its source
of the key.

```
ShotStyle.key          ← upstream library.json, verbatim, never derived
ShotStyle.card_id      ← the card, authoritative from library.json
ShotStyle.demo_path    ← implementation, resolved inside demos/<cat>/<slug>/
ShotStyle.match_method ← norm | basename | ordinal | manual | none
ShotStyle.implementation_status ← ok | missing-demo | not-a-style
```

Variant↔demo resolution inside one card directory is the only genuinely ambiguous
step, and it is now **explicit and auditable** rather than silent:

1. `norm()` exact collision (upstream's own fuzzy key from `gen-index.mjs:18`) — covers
   `Basic3DScene ↔ basic-3d-scene`, `TerminalTypewriter ↔ terminal-typewriter`.
2. demo basename equals the slug (single-style cards) — the common case.
3. declaration order, when `len(styles) == len(demos)` — deterministic, recorded as `ordinal`.
4. otherwise `implementation_status='missing-demo'` and the style still exists with
   its media, its description and its translations. **A missing implementation is a
   fact to record, not a row to drop.**
5. `not-a-style`: `VerticalTicker.tsx` (helper) and `ClipCardLooping.tsx`
   (needs real footage) leave `style` and become `source_file` rows with
   `role='demo', skip_reason=…`. They are components, not recipes.

Invariant, enforced by `doctor.py`:

> every upstream `style.key` resolves to exactly one row in exactly one table, and
> `style` contains no key that upstream does not know.

## 4. Target site architecture: Astro + Cloudflare

Current state: `site/` is empty; `platform/mirror_site.py` was just added and
`gallery/` upstream is hand-written vanilla HTML/JS with **three separate L10N
mechanisms** (see ADR 0004).

**Decision: Astro static output on Cloudflare Pages, media on R2.**

```
platform/db/shotcraft.db
   │
   ├─ build ─► site/  (Astro, static)
   │            content collections load from a DB export, not hand-written content
   │            routes:  /[locale]/  ·  /[locale]/cards/[slug]/  ·  /[locale]/domains/[x]/
   │            i18n:     src/i18n/*.ts generated from translation rows
   │                       no hand-maintained index dictionaries
   │            islands:  only where interaction is needed (style switcher,
   │                       search box). Everything else ships zero JS.
   │
   └─ media ─► R2 bucket, served via a custom domain
                gallery/media/<style-key>.mp4     (214 previews)
                gallery/media/poster/<style-key>.jpg (64 posters)
```

Why this shape:

- **Static output, not SSR.** All 157×9 pages are known at build time from the DB.
  Nothing is per-request. SSR would add a Worker and a latency floor to buy nothing.
- **Cloudflare Pages over Workers.** The site is read-only and static; Pages gives
  preview deploys per PR and cache rules without writing a Worker. Take a Worker
  only when auth or paid gating appears (i.e. at the monetization stage).
- **R2 over the GitHub release.** Upstream keeps preview MP4s in a
  `gallery-media` release because git is the wrong place for video. So do we — but
  R2, so that `media` and `site` share one origin and one cache policy, and the
  `?v=<epoch-ms>` cache-buster currently embedded in every `library.json` URL can
  become a real content hash. Zero egress cost, which matters for a 214-video CDN.
- **Zero-JS default.** The upstream gallery ships `app.js`, `showcase.js` and
  `translations.js` to render cards that are really just Markdown. Astro renders
  them at build time; we ship interactivity only where a shot style switcher or
  instant search genuinely needs it.

Media URL contract, replacing the derived key:

```
/media/preview/<style-key>.mp4     immutable, content-hashed, cached forever
/media/poster/<style-key>.jpg     immutable
```

`style-key` is the upstream key. One identity, one URL, and a missing preview is a
`404` that `doctor.py` predicts from the DB rather than discovers in production.

## 5. Invariants

Asserted by `platform/doctor.py`; exit code 1 on any ERROR.

| Invariant | Check | Status now |
|---|---|---|
| DB is structurally sound | `db.integrity`, `db.foreign_keys` | pass |
| Every upstream style key resolves to one identity | `style.identity.reachable` | **FAIL** 211/214 |
| Style identity lives in one table | `style.single_table` | **FAIL** 31 quarantined |
| No filename-derived keys | `style.kebab_casing` | **FAIL** 7 mangled |
| Every style has preview + poster | `media.coverage` | **FAIL** 35 missing |
| Every FTS index is populated | `search.*` | **FAIL** `param_fts` 0/1057 |
| Provenance and attribution are recorded | `complete.*` | WARN 2 empty tables |
| Licence blockers propagate to assets | `license.audio_consistency` | **FAIL** |
| Taxonomy and counts match upstream | `taxonomy.*`, `counts.*` | pass |
| Wiki is in step with the DB | `wiki.*` | pass |
| Every ADR referenced by `decision_log` exists | `docs.adr_links` | WARN (fixed by this PR) |

Non-negotiable rules for anyone editing the pipeline:

1. `style.key` is never derived from a filename.
2. The database is only written by ingest.
3. Nothing under `wiki/`, `site/` is hand-edited.
4. `schema.sql` and `run.py` change together, or `doctor.py` fails.
5. A missing value is `NULL`. "Absent" is never encoded in prose.

## 6. State of play

**Working.** Card ingest (157), taxonomy, parameter extraction (1,057 rows),
pitfalls (792), sections (793), motion parameters (1,607 across 213/218 styles),
easing curves (50 with usage counts), rules (27 across 5 families), audio assets
(154), licences (6), locales (9), wiki generation (157 pages + 9 domain essays +
`llms.txt`/`llms-full.txt`/`openapi.json`).

**Broken, in priority order.**

| # | Defect | Impact | Fix |
|---|---|---|---|
| 1 | Style identity split across two tables; 3 keys lost | previews and translations unreachable for 34 styles | §3 |
| 2 | `param_fts` empty | "find the parameter cards" returns nothing; 1,057 rows invisible | one INSERT loop |
| 3 | `audio_asset.commercial_ok` all 1 while `license_registry` blocks 6 files | **legal exposure on any paid delivery** | derive from registry |
| 4 | 26/157 cards have no `energy_level` | energy queries silently drop a sixth of the corpus | add `n/a` + arc rungs, or store `energy_text` only |
| 5 | `style_media.bytes` all 0 | cannot size a CDN budget | measure on disk |
| 6 | `source_commit`, `attribution_entry` empty | provenance and attribution unqueryable | populate from `git log` / ATTRIBUTION.md |
| 7 | `ru/card` namespace holds 259 keys for 157 cards | workbench label dictionaries mixed with slug keys | split namespaces |
| 8 | `style_fts` 183 vs 218 styles | 35 styles unfindable by name | rebuild after §3 |
| 9 | Upstream `generatedAt`/`revision` unwritten and stale | client change-detection cannot work | derive them, or delete |

**Not started.** `site/` (Astro), Cloudflare deployment, the paid surface,
any ADR above 0005.

## 7. Sequencing

Ordered by dependency, not by appeal.

**Part 1 — make the index true.** §3 style identity, then defects 2–8.
Everything downstream inherits correctness or inherits its absence; there is no
point building a site on an index that loses three card identities. Ends when
`doctor.py` reports zero errors.

**Part 2 — docs and decisions.** `docs/architecture`, `docs/adr`, `docs/monetization`,
`docs/research`. Mostly done in this pass; the ADR gap at slot 0001 is still open.

**Part 3 — Astro + Cloudflare site.** Only meaningful after Part 1, because every
page is a projection. Brings up `site/` from empty and retires the three upstream
L10N mechanisms in favour of ADR 0004.

**Part 4 — monetization.** Gated on a legal gate, not a feature gate: the
`video-talkcraft` PolyForm Noncommercial lineage in `workbench/` and the 6
untraceable audio files must be resolved before any paid offering. See
[docs/monetization/0001-monetization-architecture.md](../monetization/0001-monetization-architecture.md).