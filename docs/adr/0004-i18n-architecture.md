# ADR 0004 — Translations become rows; sites are generated per-locale from the DB

- Status: accepted (schema in force; Astro migration pending)
- Decided: 2026-10-01
- Supersedes: nothing

## Context

Upstream has **three independent** localisation mechanisms, none of them shared:

| Surface | Mechanism | Locales |
|---|---|---|
| `gallery/translations.js` | `window.GALLERY_I18N = { ui:{zh,en}, cardsZh, cardsEn, stylesZh, stylesEn }`; DOM attributes `data-i18n` | zh, en |
| `gallery/index.html` | inline `L10N` object; attributes `data-l10n`; sets `innerHTML` | zh, en |
| `gallery/showcase.js` | inline `SHOWCASE_L10N`; attributes `data-i18n` | zh, en |
| `workbench/src/i18n.ts` | `STRINGS` for chrome + `LABELS` for content; locales en/zh/ru | en, zh, ru |

Consequences we have to live with:

- Adding a locale means editing four files in three languages of programmer.
- `translations.js` holds **742 hand-maintained index entries** (157 zh + 157 en
  card names, 214 zh + 214 en style names) that must agree with the card set.
- `build-seo.py` parses the JS by string-slicing (`src.index('cardsEn')` up to the
  next `},`) because there is no JSON to read. A single key containing `},`
  silently truncates the map.
- Content keys and chrome keys are conflated: `workbench` needs "translate this
  *label if we happen to know it*, else show it verbatim", while chrome needs
  "this key must exist in every locale".

## Decision

1. **Translations are rows, not columns.** `translation(locale_id, ns, key, text,
   method, status)` with namespaces `ui | page | card | style | category | summary
   | showcase | meta`. Nine locales × ~400 strings is rows, never columns.
2. **`locale.status` tracks coverage honestly** (`source | partial | complete`)
   and `translation.status` tracks each string (`pending | translated |
   reviewed | stale`). A page may only claim a locale the database says is
   complete.
3. **Site pages are generated per locale from the DB**, locale-prefixed URLs
   (`/ru/cards/<slug>/`), with `hreflang` generated from `locale.bcp47`.
4. **Two translation tiers stay distinct**, because upstream needs both:
   - `t(key)` — chrome. Key must exist in every shipped locale; a missing key is a build error.
   - `tx(text)` — content (card names, schema labels, category names, track names).
     Look up, else render verbatim. Content is authored in its own language and
     never blocks a page.

## Rationale

- The keyword play requires URL-addressable locales. `hreflang` needs stable
  per-locale paths, which needs a generator, which needs the strings in the DB
  rather than in a JS bundle.
- Coverage is the metric that matters commercially, and a metric has to be
  queryable. "How many RU strings are missing?" must be a `SELECT`, not a diff.
- `method` and `status` on the row are what make machine translation safe: an
  agent can be told to fill only `status='pending'` rows, and a human can review
  only `method='machine'`.

## Consequences

- We stop shipping `translations.js` copies; we import them once into
  `translation` rows and record the import (the same treatment upstream's own
  scripts give their artifacts).
- **Key namespaces must not be mixed.** The current DB has `ru/card` holding 259
  rows against 157 cards, because upstream's `workbench/i18n/ru/*.json` are flat
  "Chinese source string → Russian" maps keyed by *label text*, not by slug.
  Slug keys and label-text keys are two different key spaces and must not share
  the `card` namespace. This is tracked as a defect in `doctor.py`
  (`search.*` / taxonomy family), not silently accepted.
- Machine translation must be marked `method='machine', status='translated'` and
  never `reviewed`, so the site can ship a "machine translated, may be rough"
  affordance rather than pretending otherwise.

## Alternatives rejected

- **Keep inline dictionaries, add locales by hand.** Rejected: four surfaces,
  no coverage metric, and the 742-entry index keeps drifting.
- **Astro i18n with JSON files per locale.** Not rejected — used as the *rendering*
  layer, reading strings from the DB export rather than from hand-written JSON.
  JSON files by hand are the thing we are removing.
- **Runtime translation lookup (client fetches strings).** Rejected: it moves
  latency and a failure mode onto every page view, for a benefit (changing copy
  without a deploy) that does not matter here.