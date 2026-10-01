# Architecture

> Phase 1 (architecture) of the SDD loop. Nothing here is implemented except the
> data layer, which is deliberately built first because it is the part every
> other workstream depends on.

## 1. What we actually have

`upstream/video-shotcraft` is not a product, it is a **methodology packaged as an
agent skill**. Four coupled layers:

| layer | path | what it is |
|---|---|---|
| knowledge | `SKILL.md`, `references/` | 3 production modes, 9 hard rules, 157 shot cards, 27 aesthetic rules, an 8-stage pipeline |
| implementation | `demos/**/*.tsx`, `assets/lib/` | 218 tuned Remotion components — one TSX per motion style — plus reusable primitives |
| runnable | `template/`, `workbench/` | the validated 36.2 s Ink Press film (10 shots) and a CapCut-style browser timeline editor on port 5198 |
| distribution | `gallery/` | a static site: 157 cards, 214 previews, 2 locales, SEO prerender |

Plus `jianying-export/` (export the film as an editable CapCut CN draft) and
`assets/audio/` (154 tracks).

**Two join keys hold it together**, and every downstream product must respect them:

- `name` — the card slug. Identical in `references/shots/<cat>/<name>.md`,
  `gallery/source/<name>.md`, `library.json.cards[].name`, the demo directory
  name, and the `library.html#<name>` deep link.
- `key` — the style slug, kebab-case of the demo TSX basename, equal to
  `media/<key>.mp4`.

## 2. What we are building

```
        upstream/video-shotcraft              data/cinematic/
        (pinned git SHA, read-only)           (authored, committed, ours -- ADR 0007)
                    |                                    |
        platform/ingest/run.py              platform/catalog/schema.sql
          (pure function of the tree)       (same rules, own file: no merge conflict)
                    |                                    |
                    +-----------------+------------------+
                                      |
                    platform/db/shotcraft.db  <---- the single source of truth
                                      |
        +-----------------+---------+---------+------------------+
        |                 |                   |                  |
    wiki/ (LLM)      site/ (i18n)     platform/query.py      research/
    llms.txt         locales/*.json     CLI for agents      competitors,
    llms-full.txt    <locale>/*.html   card/param/rule     opportunities,
    cards/*.md       hreflang+sitemap  technique/optimize  licensing audit
    techniques/*.md  queries           queries
    domains/*.md (10)
```

Two corpora, one DB. `upstream/` answers *how a shot moves*; `data/cinematic/`
answers *what to shoot*. They are consecutive stages of one pipeline and meet in
`technique_motion`, which is a **declared** relation, never a name match.
                    upstream/video-shotcraft        (pinned git SHA, read-only)
                              |
                    platform/ingest/run.py         (pure function of the tree)
                              |
                   platform/db/shotcraft.db  <---- the single source of truth
                              |
        +---------------------+---------------------+---------------------+
        |                     |                     |                     |
    wiki/ (LLM)          site/ (i18n)          platform/query.py     research/
    llms.txt             locales/*.json         CLI for agents       competitors,
    llms-full.txt        <locale>/*.html       card/param/rule      opportunities,
    cards/*.md           hreflang + sitemap    queries              licensing audit
    domains/*.md
```

Everything downstream reads the DB. Nothing downstream reads markdown directly.
That is the whole architectural bet: **one parse, many consumers.**

## 3. The data layer

`platform/ingest/schema.sql` — 24 tables, 4 FTS5 indexes, run idempotently.
`platform/catalog/schema.sql` — 9 more tables and a 5th FTS5 index, for the
cinematic corpus (ADR 0007). Applied **after** the upstream schema: two FKs cross
the boundary on purpose (`source_file_id`, `style_id`) so a catalog row is
traceable to its authored byte and a motion pairing points at a real style.

Three decisions inside it worth calling out:

**Prose is stored twice.** Upstream keeps `能量: 中高（能量来自"跳变"的顿挫而非速度）`
as free text. The parenthesised rationale is the discriminative signal, so we keep
the verbatim string *and* normalize the ordinal into `energy_level` (rank 1–8).
A future filter on `rank` must not require throwing the prose away.

**Translations are rows, not columns.** 942 distinct `(ns, key)` pairs do not
belong in `shot_card`. `translation(locale_id, ns, key, text, method, status)`
scales to the 4,266 rows a full nine-locale set implies at `zh`'s coverage
(474 distinct keys × 9). Today it holds 1,298 rows across 3 built locales, and the
gap between those two numbers is the honest measure of how much is still English:

| namespace | distinct keys |
|---|---|
| `card` | 416 |
| `style` | 214 |
| `summary` | 199 |
| `ui` | 74 |
| `showcase` | 18 |
| `page` | 11 |
| `category` | 10 |

`card` carries 416 keys for 157 cards because upstream ships a name *and* a
description per card in some namespaces and a name only in others — which is why
`ru` has 157 translated card titles and 0 translated descriptions.

**The card↔style link comes from the directory, not from `library.json`.** We
found a real upstream data bug: `crash-zoom-punch` advertises one style key while
`demos/camera/crash-zoom-punch/` holds two components, and 31 gallery style keys
in total have no matching demo. `style.card_id` is resolved from the demo
directory (authoritative); `library.json` is matched and any divergence is kept
visible in `gallery_style` rather than silently dropped.

### What the ingest extracts that upstream never exposes

| data | count | why it matters |
|---|---|---|
| `card_param` (参数表) | 1,057 rows | the tuned values and the pass/fail thresholds in "how to tune" |
| `card_pitfall` (已知坑) | 792 rows, 3 marked 命门 | failure modes with rule citations (R1, Q8, P4…) |
| `motion_param` | 1,897 occurrences, 13 kinds | every `Easing.bezier`, `spring({config})`, `seg()`, `interpolate()` range, `exp()` envelope, extracted from the TSX |
| `easing_curve` | 50 distinct curves | ranks the house style: `bezier(0.3,0,0.2,1)` is the de-facto default |
| `card_search` | 157 blobs | one searchable blob per card pooled across **all** locales |

That last table is why the search works in Russian: the cards are written in
Chinese, so a latin FTS over the raw card text returns nothing. `card_search`
pools every locale's description plus parameters, pitfalls and style keys.

## 4. Search, and why it needs a cascade

Three constraints, discovered by testing rather than by reading docs:

1. `unicode61` treats a whole Chinese phrase as **one token**, so `MATCH '转场'`
   can never match inside `…转场…`.
2. `trigram` fixes substring matching for any script but requires a query of at
   least **3 characters** — so 2-character CJK still fails.
3. FTS5 must be matched **by table name**; `alias MATCH` raises
   `no such column`, so hit resolution goes through a CTE.

`platform/query.py` therefore cascades: `unicode61` → `trigram` (≥3 chars) →
`LIKE`. Verified working on `转场`, `弹簧`, `overshoot`, `spring`, `cut`, `crash-zoom`.

## 5. The site problem, stated precisely

Upstream's i18n is three independent inline mechanisms with no shared layer:

1. `gallery/translations.js` → `window.GALLERY_I18N` (`ui` zh/en + four flat
   maps of 157/157/214/214 entries)
2. `gallery/index.html` → its own inline `L10N`, 11 keys, `data-l10n`, `innerHTML`
3. `gallery/showcase.js` → its own `SHOWCASE_L10N`, 19 keys, `data-i18n`

The locale lives in `localStorage`. Consequences:

- **No indexable per-language URL.** No `/ru/library.html`, therefore no
  `hreflang`, therefore the SEO play is impossible as-is.
- **Every new language touches three HTML/JS files** plus a 371-entry dictionary.
- `build-seo.py` parses `cardsEn` by *string slicing* — any key containing `},`
  silently truncates the map. Adding locales multiplies that fragility.

Full design in [ADR-0004](adr/0004-i18n-architecture.md).

## 6. Licensing, stated as constraints

| subject | licence | commercial | blocks |
|---|---|---|---|
| core | Apache-2.0 | free | no |
| **Remotion** | Remotion License | free for individuals/small companies | **yes — price it in** |
| Mixkit audio | Mixkit Free | free | no |
| **video-talkcraft** | PolyForm Noncommercial | **requires authorisation** | **yes — read only** |
| 6 untraceable audio files | unknown | unknown | **yes — replace** |

Remotion is the real gate, not the code. Every client deliverable either assumes
the client's own licence or carries the cost.

## 7. Monorepo layout

```
shotcraft/
├── upstream/video-shotcraft/   pinned clone, never edited
├── platform/
│   ├── ingest/                 schema.sql + run.py + parsing.py + motion.py
│   ├── db/shotcraft.db         generated, reproducible from the clone
│   ├── wiki/build_wiki.py      DB -> wiki/
│   ├── mirror_site.py          live site + mp4 release -> upstream/site-mirror/
│   └── query.py                agent CLI over the DB
├── wiki/                       generated LLM wiki
├── site/                       our fork of the gallery, i18n rebuild
├── docs/                       adr/ architecture/ research/ monetization/
├── specs/                      SDD: vision, feature list, specs
└── scripts/                    one-shot maintenance scripts
```

`upstream/` is git-ignored; `platform/db/` and `wiki/` are committed as
artefacts (they are the deliverable) but regenerate in one command.

## 8. Build order

Dependency order, not preference order:

1. **ingest + schema** — done. Nothing else can be built without it.
2. **wiki** — done. Proves the schema is sufficient and gives agents a spec.
3. **i18n extraction** — the site rebuild. Highest visible value, blocks the SEO
   model.
4. **translation pipeline** — machine + review loop, coverage gate in CI.
5. **micro-SaaS / service site** — only after 1–4, because it consumes the same
   indexes.

## 9. Verification

| claim | how it is proven |
|---|---|
| the DB reflects upstream | `python platform/ingest/run.py` → 157 cards, 218 styles, 0 unexpected category dirs; every warning is a real upstream inconsistency, not a parse bug |
| the wiki is current | `python platform/wiki/build_wiki.py` is deterministic from the DB; a stale wiki is a stale DB |
| search works in every locale | the six queries in §4 |
| the site mirrors completely | `python platform/mirror_site.py --media` exits non-zero on any missing preview, the same check `deploy-pages.yml` performs |
| a feature is done | only `verifier` may set `passes: true` in `specs/feature-list.json` |