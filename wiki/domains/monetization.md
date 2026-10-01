# Monetization

Five models, ranked by time to first dollar rather than by ceiling. The evidence column is in `platform/db/shotcraft.db#/opportunity` and every number is traceable.

| key | model | effort | first revenue | status |
|---|---|---|---|---|
| `enterprise-license` | license | M | 2-3 months | idea |
| `render-farm-saas` | saas | L | 3-4 months | idea |
| `brand-pack-marketplace` | marketplace | S | 3-5 weeks | idea |
| `localized-library-hub` | ads + service lead-gen | M | 6-8 weeks | idea |
| `agency-film-in-a-day` | service | S | immediately | idea |

## B2B: branded skill + support SLA  (`enterprise-license`)

Upstream is Apache-2.0, so the code cannot be locked up. The defensible B2B product is the part that is NOT in the repo: a branded skill pinned to the client's design system, CI that renders on every PR, and an acceptance report per release.

- **model**: license · **effort**: M · **first revenue**: 2-3 months
- **depends on**: ["F020", "F040"]
- **evidence**: core_license=Apache-2.0, remotion_commercial=requires licence for companies, existing_ci=pr-checks.yml (tsc + vitest + smoke render)


## Hosted render + shot-preview micro-SaaS  (`render-farm-saas`)

The repo explicitly does not ship a hosted renderer; it documents three headless-Linux wall (concurrency cap, chrome-headless-shell, blocked CDN). A hosted 'render this shot with your product screenshots' API converts a documented pain point into a paid action.

- **model**: saas · **effort**: L · **first revenue**: 3-4 months
- **depends on**: ["F020", "F021"]
- **evidence**: render_blockers_documented=3, install_step=ln -s into ~/.claude/skills or ~/.codex/skills, free_tier=single-shot preview


## Paid brand kits (themes, palettes, SFX packs)  (`brand-pack-marketplace`)

The Apache-2.0 core already ships 9 visual themes (template/THEMES.md) and 149 SFX. Selling pre-skins that drop into the same schema is pure margin: the runtime, the cards and the acceptance rules are already paid for by the community.

- **model**: marketplace · **effort**: S · **first revenue**: 3-5 weeks
- **depends on**: ["F030"]
- **evidence**: themes_upstream=9, sfx_upstream=149, core_license=Apache-2.0


## 9-locale shot library hub (the site itself)  (`localized-library-hub`)

Upstream ships a library site with exactly two locales and English-only card copy. RU/ES/DE/FR/PT/KO/JA pages for 'product promo video' + 'motion design shot library' intent have almost no competition: the keyword space is English-dominant while the audience is global. Every page is a proof-of-work asset that also serves as a lead magnet.

- **model**: ads + service lead-gen · **effort**: M · **first revenue**: 6-8 weeks
- **depends on**: ["F010", "F011", "F012"]
- **evidence**: upstream_locales=2, target_locales=9, cards=157, styles=214, stars=10100, forks=899, source_sites=['enterprise-dna', 'moclaw', 'bigprompthub', 'onei.ai']


## Agency: 36-second film in a day  (`agency-film-in-a-day`)

A hands-on third-party run reports 35 minutes hands-on for a 36-second promo, and the template is a validated 36.2s / 10-shot cut. That is a unit-economics story, not a tool story: sell the outcome (a launch film before the funding announcement), not the repo.

- **model**: service · **effort**: S · **first revenue**: immediately
- **depends on**: []
- **evidence**: hands_on_minutes_reported=35, output_seconds=36, shots=10, source=moclaw.ai hands-on report

## What we are not doing

- **Not selling the core.** Apache-2.0 means anyone can sell a fork; our advantage has to be something a fork cannot copy — a rendered film, a supported pipeline, or a language nobody else bothered to translate.
- **Not competing on stars.** Upstream has 10.1k and a fast-moving release cadence. A fork chases upstream forever and loses.
- **Not touching video-talkcraft commercially.** PolyForm Noncommercial. Reading is fine; shipping is not.
