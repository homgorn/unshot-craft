# Target architecture — Astro on Cloudflare

- Status: **proposal.** `site/` is empty. Nothing here is implemented.
- Date: 2026-10-01
- Companion: [README.md](README.md) §5 (the i18n problem), [ADR 0004](../adr/0004-i18n-architecture.md),
  [0002-style-identity-cost.md](0002-style-identity-cost.md)

## Why this document exists

`docs/architecture/README.md` §5 states the site problem precisely (three inline L10N
mechanisms, no indexable per-language URL, a 371-entry hand-maintained dictionary).
This document answers the question README leaves open: **given that problem, what do
we actually build?**

## The decision

**Astro static output on Cloudflare Pages. Video and posters on R2. Zero JavaScript
by default.**

```
platform/db/shotcraft.db
   │
   ├─ export ─► site/src/data/*.json        generated, committed, no runtime DB
   │
   ├─ build ─► site/dist/                   Astro static output
   │            /                            landing, 4×4 motion wall
   │            /[locale]/                   category overview, locale-prefixed
   │            /[locale]/cards/[slug]/      one page per card, per locale
   │            /[locale]/params/[key]/      parameter index  ← the moat (README §1)
   │            /[locale]/domains/[slug]/    cross-cutting essays
   │            /sitemap.xml, /llms.txt, /api/openapi.json
   │            islands only: style switcher, search box
   │
   └─ media ─► R2 bucket, custom domain
                /media/preview/<style-key>.mp4      214
                /media/poster/<style-key>.jpg       64
```

### Why Astro

- **The content is already a database.** Astro's content collections want Markdown
  frontmatter. We do not want Markdown — we want the 1,057 `card_param` rows and the
  27 `rule` rows as queryable data. Astro is used here as a **template engine over a
  generated JSON export**, not as a content-collection CMS. That is a deliberate
  mismatch with Astro's default idiom, and it is the right one: it keeps
  "the wiki/site are projections" (README §2) literally true.
- **It removes JavaScript rather than relocating it.** Upstream ships `app.js`,
  `showcase.js` and `translations.js` to render 157 cards that are Markdown with a
  video. Astro renders them at build time. Result: a card page is HTML + one `<video>`.
- **Two islands, not an SPA.** A style switcher (57 multi-style cards) and instant
  search need client code. Nothing else does. Filter-and-URL-state is plain links,
  so every filtered view is shareable and crawlable for free.

### Why Cloudflare Pages, not Workers

All 1,413 locale×card pages are known at build time from the database. There is no
per-request computation, so SSR would add a Worker and a latency floor to buy
nothing. Pages gives preview deploys per PR and cache rules for free.

**Take a Worker only when the monetization layer needs it** — auth, or gating paid
content. That is a Part-4 concern and it is the one thing that would invalidate this
decision. Everything in `docs/monetization/brainstorm.md` can ship on static output.

### Why R2, and not the GitHub release

Upstream keeps its previews in a `gallery-media` release precisely because git is the
wrong place for video. That reasoning is right and worth inheriting — but a release
asset store is a download API with a CLI, not a CDN with cache headers. R2 gives:

- **zero egress cost**, which matters at 214 videos and a multi-locale page count;
- **one origin with `site/`**, so a page and its video share a cache policy;
- **real content-hashed URLs**, which lets us delete the `?v=<epoch-ms>` cache-buster
  that upstream currently hand-manages inside every `library.json` URL.

```r2
/media/preview/<style-key>.mp4   immutable, Cache-Control: public, max-age=31536000
/media/poster/<style-key>.jpg   immutable, same
```

`<style-key>` is the upstream key — see
[0002-style-identity-cost.md](0002-style-identity-cost.md) for why the key must be
fixed and pinned before this URL contract is safe.

### What replaces the three L10N mechanisms

Per [ADR 0004](../adr/0004-i18n-architecture.md), all three collapse into DB rows:

| upstream today | becomes |
|---|---|
| `translations.js` `ui.zh`/`ui.en` (75 keys each) | `translation(ns='ui', …)` |
| `cardsZh`/`cardsEn` (157 each) | `translation(ns='card', key=<slug>)` |
| `stylesZh`/`stylesEn` (214 each) | `translation(ns='style', key=<style-key>)` |
| `index.html` inline `L10N` (11 keys) | `translation(ns='page', …)` |
| `showcase.js` `SHOWCASE_L10N` (19 keys) | `translation(ns='showcase', …)` |
| `workbench/src/i18n.ts` | out of scope — the workbench is a separate app and, per ADR 0005, encumbered |

`site/src/i18n/<locale>.ts` is **generated** from those rows at build time. The
`data-l10n` / `data-i18n` attribute walk disappears entirely, because there is no
longer a post-load phase to walk the DOM.

Two-tier lookup survives, because upstream genuinely needs both (ADR 0004 §4):
`t(key)` for chrome must exist in every shipped locale; `tx(text)` for content labels
looks up, else renders verbatim.

### hreflang, which is the actual point

```html
<link rel="alternate" hreflang="en" href="https://…/en/cards/card-stack/">
<link rel="alternate" hreflang="zh-CN" href="https://…/zh/cards/card-stack/">
<link rel="alternate" hreflang="ru" href="https://…/ru/cards/card-stack/">
<link rel="alternate" hreflang="x-default" href="https://…/en/cards/card-stack/">
```

Generated from `locale.bcp47`, which already has `html_lang` for the `zh`/`ja`/`ko`
cases where the BCP-47 tag and the HTML `lang` differ. `locale.status` gates emission:
a `pending` locale gets no `hreflang` entry, so we never advertise a page we have not
finished. That is the mechanism that prevents advertising `es` because the machine
translation ran.

## Build and deploy

```
python platform/ingest/run.py        # upstream -> db
python platform/wiki/build_wiki.py   # db -> wiki/
node site/build.mjs                  # db -> site/src/data/*.json   (generated)
npm --prefix site run build          # site -> site/dist
wrangler pages deploy site/dist
```

`site/src/data/*.json` and `wiki/` are committed artefacts, per ADR 0001: a reviewer
must be able to read the index without running anything, and a diff must never show
generated output without its cause.

## Sequencing against README §8

README's build order is: ingest → wiki → i18n extraction → translation pipeline →
SaaS. This document does not reorder it; it fills in what "i18n extraction" produces.
The one addition worth making explicit:

> **Part 3 needs a decision on the card-page template before the translation
> pipeline starts.** Machine-translating 1,413 pages and then changing the template
> means re-reviewing all of them. Build one locale's page, get the template right,
> then translate.

## Risks

| risk | mitigation |
|---|---|
| Scaled-content abuse on machine-translated pages (brainstorm Tier 1) | human review of the top 40 cards per locale, real editorial on landings, and `locale.status` gating hreflang — the last is structural, the first two are not |
| Astro used against its content-collection idiom | documented above; the JSON export is generated and gitignored-from-hand-editing by convention |
| Media cost before there is revenue | R2 egress is zero; storage at 214 previews is trivial. The real cost is Remotion, not bandwidth — see `docs/monetization/` |
| R2 before the key is fixed | blocked on [0002-style-identity-cost.md](0002-style-identity-cost.md). Do not bake the URL contract until `style.identity.lost` is 0 |