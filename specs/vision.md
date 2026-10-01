# Vision — shotcraft

## One line

Turn an open-source 10k-star motion-design agent skill into a localized,
searchable, commercially defensible platform: a 9-language index of cinematic
shot craft, and a studio that uses it to ship films fast.

## The problem we are solving

The upstream project is excellent and *stops at documentation*. It has 157 shot
recipe cards, 218 tuned Remotion demos and a validated 36.2 s template — but:

1. **The knowledge is unusable as data.** 1,057 tuned parameters, 792 pitfalls
   and every easing curve exist only as markdown or as TSX literals. An agent
   must read 157 files to answer "what shots fit a 15-frame high-energy beat?".
2. **The site is English- and Chinese-only**, with the language stored in
   `localStorage` — so there is no indexable Russian, Spanish or German page and
   no `hreflang`. The single largest untapped asset has no URL.
3. **Nobody indexed the motion grammar.** 50 distinct bezier curves, the modal
   spring config, the mandatory hold budgets. This is the part of the craft that
   transfers across products, and it is invisible.

## What we build, in order

1. **The index** (done) — SQLite + FTS5 over cards, parameters, pitfalls, motion
   parameters, methodology and licensing, plus an agent CLI.
2. **The wiki** (done) — generated from the index: `llms.txt`, `llms-full.txt`,
   9 domain documents, 157 card pages, an OpenAPI contract.
3. **The localized site** — 9 locales, locale-prefixed URLs, `hreflang`,
   generated per-locale dictionaries, a coverage gate.
4. **The business** — a service first (films), then brand kits, then a hosted
   renderer only if inbound asks for it.

## Explicit non-goals

- **Not a video editor.** The upstream workbench is Apache-2.0 and exists. We do
  not fork a CapCut clone.
- **Not a fork that ships the upstream skill.** We build beside it, under our own
  brand, with upstream pinned and credited.
- **Not commercial use of `video-talkcraft`.** PolyForm Noncommercial — read and
  port techniques, never ship.
- **Not competing on stars.** 10.1k and a fast release cadence. We compete on
  reach and on rendered outcomes.
- **Not a speculative platform.** The SaaS is gated on inbound evidence, not on
  our enthusiasm.

## Success criteria

| horizon | criterion | how it is measured |
|---|---|---|
| now | the index is complete and queryable | 157/157 cards, 218/218 styles, 6/6 search queries pass in 3 languages |
| next | a cold agent can answer a craft question correctly | ask 20 questions; ≥18 answered from `wiki/` alone with no upstream file access |
| next | the Russian library page is reachable | `/ru/library.html` returns 200, `hreflang` complete, 157 cards rendered |
| later | the service converts | inbound split between "render this" and "do this" |

## The bet

Apache-2.0 makes the code free. So we sell outcomes and support, and we build the
index that nobody else has. If the index is genuinely more useful than grep, the
site is genuinely more useful than the upstream gallery, and the studio is
genuinely faster than an agency — then the free code is the cheapest part of the
business.