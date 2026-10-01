# Architecture of the upstream repo

video-shotcraft is four coupled layers plus a distribution layer. Every downstream product we build sits *beside* this, never inside it.

| layer | path | role |
|---|---|---|
| knowledge | `SKILL.md` + `references/` | the agent's entry point: 3 production modes, 9 hard rules, 157 cards, 27 aesthetic rules, the pipeline |
| implementation | `demos/**/*.tsx` + `assets/lib/` | the tuned truth: one TSX per motion style, plus reusable components (PageCam, ClipCard, DigitRoll, Caption, FlashCut) |
| runnable | `template/` + `workbench/` | the validated 36.2s Ink Press film (10 shots) and a CapCut-style browser timeline editor on port 5198 |
| distribution | `gallery/` | the static site: 157 cards, 214 previews, 2 locales, SEO prerender |
| delivery | `jianying-export/` | export the finished film as an editable CapCut CN draft |

## The join keys

- `name` (card slug) — identical across `references/shots/<cat>/<name>.md`, `gallery/source/<name>.md`, `library.json.cards[].name`, the demo directory, and the `library.html#<name>` deep link.
- `key` (style slug) — kebab-case of the demo TSX basename, equal to `media/<key>.mp4` and `media/poster/<key>.jpg`.

## Gallery build pipeline

```
references/shots/*.md ──sync-from-cards.py──> gallery/source/*.md + gallery/api/library.json
                             ──build-seo.py────> sitemap.xml, llms.txt, library.html prerender
             ──deploy-pages.yml───────> GitHub Pages (+ mp4s from the gallery-media release)
```

Note: **the mp4 previews are not in git.** They are downloaded from the `gallery-media` GitHub release at deploy time. A local checkout has zero previews; the 66 poster jpgs are in the tree. Any mirror of the site must fetch the release.

## Upstream i18n today

Three independent mechanisms, all inline, none shared:

1. `gallery/translations.js` → `window.GALLERY_I18N` with `ui` (zh/en) plus flat maps `cardsZh/cardsEn/stylesZh/stylesEn` (157 + 157 + 214 + 214 entries).
2. `gallery/index.html` → its own inline `L10N` object, 11 keys, applied via `data-l10n` and `innerHTML`.
3. `gallery/showcase.js` → its own `SHOWCASE_L10N`, 19 keys, `data-i18n`.

Locale lives in `localStorage`, not in the URL — so there is no indexable per-language URL, no `hreflang`, and no way for a crawler or a link to reach the Russian library. Fixing that is our first site change (ADR-0004).

## Repository composition (files indexed: 1139)

| role | files |
|---|---|
| `demo` | 248 |
| `site` | 238 |
| `card` | 157 |
| `asset` | 156 |
| `catalog` | 150 |
| `other` | 78 |
| `component` | 73 |
| `config` | 15 |
| `doc` | 10 |
| `reference` | 8 |
| `ci` | 3 |
| `sequence` | 2 |
| `license` | 1 |