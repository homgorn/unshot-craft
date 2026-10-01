# progress

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