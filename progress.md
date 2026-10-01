# progress

## 2026-09-28 — cinematic catalog layer specified (ADR 0007, F070–F074)

### What was set up

**A second corpus, specified but not implemented.** The shot cards answer *how a
shot moves*. They cannot answer *what to shoot* — upstream renders design-system
demos, not films, so no card has an opinion on focal length, key direction or
colour science. The 150-technique cinematic catalog does, and it carries the
commercially interesting half: a cross-tool parameter matrix for Midjourney v6.1,
Runway Gen-3, Veo 2, Kling 1.5, Luma Dream Machine, Pika 1.5 and Sora.

| artifact | path | state |
|---|---|---|
| ADR | `docs/adr/0007-cinematic-catalog-layer.md` | accepted |
| Spec | `specs/features/F070-cinematic-catalog-ingest.md` | specified, `passes: false` |
| Ledger | `specs/feature-list.json` → `F070`–`F074` | 5 features, all `passes: false` |
| Source contract | `data/README.md` | written; `data/cinematic/` awaits 150 authored files |
| DDL | `platform/catalog/schema.sql` | 9 tables + 1 FTS5 index, **validated** |
| DDL gate | `platform/catalog/validate_schema.py` | applies the DDL, guards the FK assumption |

Verified: SQLite 3.49.1, FTS5 available, DDL applies clean after the upstream
schema, 7 categories and 7 tools seeded, 2 cross-corpus FKs declared and stubbed,
`[Subject]` survives compilation, 150 × 7 = 1,050 possible matrix cells of which
**117 are filled**.

### Findings that changed the design

8. **The catalog DDL cannot be applied standalone.** Two FKs cross the corpus
   boundary on purpose — `cinematic_technique.source_file_id` → `source_file` and
   `technique_motion.style_id` → `style` — because a row must be traceable to its
   authored byte and a motion pairing must point at a real style. Found by
   `validate_schema.py` on its first run. Fixed by ordering the schema files and
   by making the gate assert the count is exactly 2, so a third reference fails
   loudly instead of silently passing on stubs.
9. **The DDL ships as `platform/catalog/schema.sql`, not appended to
   `platform/ingest/schema.sql`.** The upstream schema is being edited for the
   upstream corpus; a 150-line append from another workstream is a merge conflict
   waiting to happen. The section number is kept so the two schemas read in the
   same order.
10. **`ai_tool.key` is version pinned** — `mj61`, `kling15`, `runway_gen3`. A
    parameter string is only valid for the model version it was written against,
    so `kling15` and a future `kling2` are different tools. The gate's first probe
    used `kling` and hit the NOT NULL on `tool_id`; that is the constraint working.
11. **33 unfilled matrix cells stay `NULL`.** Same rule as
    `render.duration_frames` on the 5 upstream technique cards: an untested tool
    parameter is an untested claim, and a plausible string in that cell is a
    claim we cannot defend to a client. `doctor.py` will print
    `filled_cross_tool_cells` so the number is visible rather than assumed.

### Relationship to the render blocker

The bridge makes a prompt decision and a motion curve meet in one query. It does
**not** unblock rendering: `F060` stays blocked on the Remotion commercial
licence question and the `video-talkcraft` PolyForm question, see
`docs/monetization/0002-blocking-issues.md`. The 109 missing video benchmarks are
a separate gap and are not produced by this layer.

### Next

F070–F074 need `data/cinematic/` populated with 150 authored files before the
ingest can be implemented against real input rather than a schema. The authoring
contract is `data/README.md`; the three rules that matter are: `[Subject]` is a
slot and is never expanded, an untested tool parameter is an empty cell, and
`styles:` is a declared relation rather than a guess.

## 2026-10-01 — project baseline (architecture phase)

### What was set up

**Upstream fetched and studied.** `upstream/video-shotcraft` at
`5ddbf52`, Apache-2.0, 989 tracked files. Two exploration agents produced the
structural map and the semantic map (card schema, parameter extraction strategy,
motion-design vocabulary, energy-curve selection heuristic).

**The index — built and working.** `platform/ingest/` is a dependency-free
Python pipeline (hand parsers for YAML-ish frontmatter, markdown tables, JS
object literals, and TSX motion literals). Output:

| | |
|---|---|
| cards | 157 / 157 |
| styles (demo components) | 218 |
| card→style links | 217 / 218 (only `clipcard-looping` is unlinked, upstream has no card for it) |
| tuned parameters | 1,057 |
| pitfalls | 792 (3 marked 命门) |
| motion parameters extracted from TSX | 1,607 |
| distinct bezier curves | 50 |
| aesthetic rules | 27 |
| audio assets audited | 154 |
| translation strings | 1,092 |
| locales tracked | 9 |

**The wiki — generated.** `wiki/` has `llms.txt`, `llms-full.txt` (~620 KB),
`index.json` (~317 KB), 157 card pages (`.md` + `.json` each), 9 domain
documents and an OpenAPI contract.

### Findings that changed the design

1. **`library.json` is lossy.** 31 gallery style keys have no matching demo
   component (e.g. `crash-zoom-punch` advertises one key while
   `demos/camera/crash-zoom-punch/` holds two). The authoritative card↔style link
   is the **demo directory name**. Divergences are kept in `gallery_style`.
2. **The site has no indexable per-language URL.** The locale lives in
   `localStorage`, so there is no `/ru/library.html`, no `hreflang`, and no way
   for a crawler or a share link to reach a non-English library. This blocks the
   primary revenue model → ADR-0004.
3. **`build-seo.py` parses the English card map by string slicing** (`up to the
   first },`). A key containing `},` silently truncates it. Removed from the plan.
4. **Search needs a cascade.** `unicode61` makes a whole Chinese phrase one
   token (`MATCH '转场'` → 0 hits). `trigram` fixes substrings but needs ≥3
   characters (`'转场'` → 0 hits there too). FTS5 rejects `alias MATCH`
   (`no such column`). Solution: `unicode61` → `trigram` → `LIKE`, with hits
   resolved through a CTE. Verified on 转场 / 弹簧 / overshoot / spring / cut /
   crash-zoom.
5. **Cards are written in Chinese**, so a latin FTS over the raw card text
   matches nothing. `card_search` pools every locale's description plus
   parameters, pitfalls and style keys into one blob per card — that is why
   Russian search works before we have translated anything.
6. **Upstream already ships a Russian workbench UI** (`workbench/i18n/ru/`),
   merged in the HEAD commit. Those 468 strings seed our `ru` locale for free.
7. **The mp4 previews are not in git.** A local checkout has 0 of 214; they come
   from the `gallery-media` GitHub release at deploy time. `mirror_site.py`
   exists because of this.

### Architecture decisions recorded

6 ADRs in `docs/adr/`: workspace layout, data layer, generated wiki, i18n,
upstream policy, SDD loop.

### SDD ledger

`specs/feature-list.json`: 15 features, 4 marked done (F001–F004), 11 pending.

Every done feature was executed, not assumed:

- F001 ingest reproduces the pinned tree
- F002 tables match the tree; divergences surfaced
- F003 search works in zh / en / slugs (6 queries)
- F004 wiki generates deterministically

`F005` is deliberately marked false: "the wiki answers 20 craft questions with
≥18 correct" needs an independent reader, not the author of the generator.

### Next

Build order is dependency order:

1. F010 — extract upstream translations to per-locale JSON, pixel-identical in en/zh
2. F011 — one i18n runtime replacing three inline mechanisms
3. F012 — locale-prefixed URLs, hreflang, canonical, locale-qualified sitemap
4. F013/F014 — generated per-locale dictionaries + a coverage gate
5. F006 — full site mirror including previews
6. Then, and only then, money: agency first (it needs no code), brand kits, and a
   hosted renderer only if inbound asks to *render* rather than *hire*.