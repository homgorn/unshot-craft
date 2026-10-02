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
| Source contract | `data/README.md` | written; `data/cinematic/` imports 150 files from the MIT Cinematique project |
| DDL | `platform/catalog/schema.sql` | 9 tables + 1 FTS5 index, **validated** |
| DDL gate | `platform/catalog/validate_schema.py` | applies the DDL, guards the FK assumption |

Verified: SQLite 3.49.1, FTS5 available, DDL applies clean after the upstream
schema, 7 categories and 7 tools seeded, 2 cross-corpus FKs declared and stubbed,
`[Subject]` survives compilation, 150 × 7 = 1,050 possible matrix cells of which
**791 are filled, 259 are null, and 0 have been tested**.

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
11. **259 unfilled matrix cells stay `NULL`, and all 791 filled ones are
    `tested: no`.** Same rule as `render.duration_frames` on the 5 upstream
    technique cards: an untested tool parameter is an untested claim, and a
    plausible string in that cell is a claim we cannot defend to a client.
    `doctor.py` prints `catalog.matrix` with filled/tested/null side by side,
    and `catalog.tested_claims_backed` requires a `tested_at` date behind any
    `tested=1` row — without one we cannot tell a real run from a flag someone
    set. The tested count is **0** and that is the honest state, not a gap: the
    source matrix has a `FILLED`/`TODO` status column and no verification column.
12. **All 150 citations carry `url IS NULL`.** The source lists sources as
    `Title — Publisher` with no link. `technique_citation.url` was `NOT NULL` and
    is now nullable, because a fabricated URL beside a real title costs more than
    a missing citation: a reviewer follows it, finds nothing, and stops trusting
    every other citation in the row.
13. **`visual-style` was removed from the category vocabulary rather than
    populated.** It was always empty — the source corpus has no such group — and a
    controlled-vocabulary entry nothing can populate makes `--category
    visual-style` look broken rather than absent. `visual-effects` was added
    alongside it, because the source has "Visual Effects & Promptable FX" as its
    own group and squashing it into `visual-style` would have returned rows that
    are not about visual style.
14. **The catalog is imported, not authored here.** `data/cinematic/` comes from
    a separate MIT-licensed project via `platform/catalog/import_cinematique.py`,
    with a per-file `upstream_sha256` so any row traces to the exact byte it came
    from. Editing one of those files by hand is a divergence from upstream, not a
    local decision — a stricter rule than the one that applies to corpora we
    author. See ADR-0007 for the reversal and what it cost.

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

**The locales — and the one debt that was worse than it looked.** `en` is the
reference, `zh` is upstream's own language, `ru` is ours. Coverage is measured by
*difference from en*, not by presence, because an inherited string is present and
untranslated:

| locale | chrome | card titles | card descriptions | overall |
|---|---|---|---|---|
| `en` | 103/103 | 157/157 | 157/157 | 100 % |
| `zh` | 103/104 | 157/157 | 0 (upstream wrote none) | 99.7 % |
| `ru` | 104/104 | 157/157 | **157/157** | **99.7 %** |

`ru` was published at 72.8 % and every one of its 157 cards showed a **Chinese
summary**: `prerender.py` prefers a locale `description`, falls back to the card's
Chinese `summary`, and no `description` existed. The site selftest read the DOM
*after* the i18n script had patched the page, so it saw a Russian page while a
crawler saw the Chinese one. Three things fixed it, in this order:

1. **The static block is now checked with no JavaScript in the loop.** 157/157
   cards carrying CJK prose fails `ru prerendered cards contain no CJK prose`.
2. **`platform/site/translate.py`** — the worklist, the batch applier, the
   verifier and the pruner. It refuses a value equal to the slug, a value copied
   from another locale, a value still in CJK, and a string with untranslated
   latin words in it. That last check caught five real defects in my own first
   pass, including `rests на несколько кадров` and `surrounding text раздвигается`.
3. **`ru/styles.json` was a fabricated file.** 96 keys whose `title` was the slug
   itself — which satisfied every key count ever written while translating
   nothing. `check_coverage.py` checked `cards` and `ui` and never `styles`. The
   check is now generic across namespaces, and 214 style names are translated.

**Authorship is replayed, not stored.** `run.py` deletes the database on every
run, so a provenance column on `translation` survived exactly until the next
ingest — and 371 machine translations marked `needs_review` became 371 rows with
no status at all. `translation_provenance` is now derived by replaying the
committed `site/locales/_batch_*.json` files, and a batch may claim `reviewed`
only by naming a `reviewed_by`. Today: **371 attributed, 0 reviewed.** The
Russian locale is published and complete, and none of it has been through a native
reviewer, which the database says out loud.

**The build ordering is enforced, not remembered.** `prerender.py` bakes
translations into the static HTML; `build_site.py` regenerates the page from the
template. Running the build after the prerender drops every translation silently.
`build_site.py` now clears a stamp, `prerender.py` writes it, and the selftest
refuses to run without it — which is how the culprit was found: `build_site.py
--serve`, used to start a test server, was rebuilding the tree it served.

**The site had no motion on it, through three separate faults at once.**
The home page's 16-clip wall was an inline script that shared a `<script>` block
with upstream's `L10N` dictionary, and the code that retired the dictionary
deleted the whole block; the media paths were rewritten by an `apply_patches`
entry written for single quotes when the source uses backticks, with
`required=0`, so the miss was silent; and `site/dist/media` was a symlink to
`gallery/media`, which holds **64 posters and no videos at all**, created inside a
`try` whose handler was `pass`, so on Windows it was simply never there. The 214
mp4 previews are GitHub release assets and are not in upstream's git tree — they
come from `platform/mirror_site.py --media`. Every gate was green throughout,
because every gate read the DOM after JavaScript had run. Now there are **157
cards with a playable clip in the static block**, each `<video>` checked against
disk before it is written, and `check_seo.py` fails on a home page without
`createElement('video')`, on a `./media/` path, on a dangling clip or poster, and
on an empty `site/dist/media/`.

**F060 renders.** `platform/render/run.py` produces **117 rendered clips** in
`render/out/`, 32.4 MB, and `--verify` reads all 117 back with `ffprobe` and
compares each frame count against the index. It runs in `platform/render/.work/`
because `npm install` writes into whatever directory it runs in and `upstream/`
is a pinned read-only clone. `check_seo.py` additionally verifies that every
declared `VideoObject` duration matches the real length of the file it names —
a check that exists because the first version took
`shot_card.duration_frames` (how long the shot should hold in a film) for the
clip's length (how long the demo component runs), declared `PT0.4S` on a
4-second video, and had 6 wrong out of 6 sampled, every one of them plausible.

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
| motion parameters extracted from TSX | 1,897 across 13 kinds |
| aesthetic rules | 27 |
| audio assets audited | 154 (5 untraceable, `commercial_ok=0`) |
| translation strings | 1,298 |
| locales tracked | 9 (3 built: en, zh, ru) |
| upstream files indexed | 989 + 150 catalog files |

**The catalog — imported.** `data/cinematic/` is 150 techniques from the
MIT-licensed `cinematique` project, not authored here:

| | |
|---|---|
| techniques | 150 across 7 categories |
| cross-tool matrix cells | 1,050 (7 tools × 150) |
| cells filled | 791 |
| cells `NULL` | 259 (37 source rows are `TODO`) |
| cells **tested against a model version** | **0** |
| declared motion pairings | 233 across 142 / 150 techniques |
| common-mistake entries | 450 |
| citations | 150, **all with `url IS NULL`** |
| reference videos | 41 (65 MB, committed) |

**The wiki — generated.** `wiki/` has `llms.txt` (13 KB),
`llms-full.txt` (~1.1 MB), `index.json` (~1.1 MB), 157 card pages
(`.md` + `.json` each), 150 technique pages, 10 domain documents and a
13-path OpenAPI contract.

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