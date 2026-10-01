# Monetization architecture

- Status: decision memo, nothing shipped
- Date: 2026-10-01
- Evidence base: `license_registry`, `opportunity`, `actor`, `source_channel` in `platform/db/shotcraft.db`
- Depends on: [ADR 0005 — upstream policy](../adr/0005-upstream-policy.md), [SDD 0001 §7](../architecture/0001-platform.md)

---

## 1. The constraint that decides everything

**The core is Apache-2.0 and has 10.1k stars and 899 forks.** This has one
dominant consequence:

> You cannot monetise access to the code, because anyone can `git clone` it and
> anyone can fork it. Any model that depends on the code remaining scarce is
> dead on arrival — and it would be a bad business even if it worked.

So the question is never "how do we charge for the skill". It is:

> **What do we own that the repository does not contain?**

Five things qualify, and only these five:

1. **The index** — 157 cards × 9 locales, parsed and cross-linked. Upstream ships
   this as a hand-maintained 214-entry JSON index in two locales.
2. **The rendered corpus** — 214 previews. Upstream keeps them in a GitHub release
   because git is the wrong place for video.
3. **The localisation** — 7 locales that do not exist upstream, in the languages
   the audience actually reads.
4. **The hosted rendering path** — upstream explicitly documents *not* shipping one,
   along with the wall it hit on headless Linux.
5. **Provenance and compliance work** — licence audit, attribution, acceptance
   evidence. Nobody upstream does this.

Everything else — the cards, the demos, the template, the methodology — is free to
everyone, forever, and we should say so out loud. It is the funnel, not the product.

## 2. The legal gate, stated plainly

From our own `license_registry` (6 rows, 3 blocking):

| Subject | SPDX | Commercial | Blocking |
|---|---|---|---|
| video-shotcraft core | Apache-2.0 | free | no — but NOTICE/copyright must travel with redistribution |
| Mixkit SFX + BGM | Mixkit Free License | free | no |
| Shot-recipe provenance (48 cards) | Apache-2.0, techniques re-implemented | free | no — but no endorsement may be implied |
| **Remotion (render engine)** | Remotion License | **restricted** | **yes** |
| **video-talkcraft (sibling skill)** | PolyForm Noncommercial 1.0.0 | **requires licence** | **yes** |
| **6 audio files, 无法反查** | unknown | **unknown** | **yes** |

Three consequences, in order of urgency:

**2a. The workbench may be encumbered, and it is the biggest asset.** Upstream's
`workbench/` states it was ported from `video-talkcraft/workbench`, and that project
is PolyForm Noncommercial. A derived work sitting inside an Apache-2.0 repository
does not launder the restriction — PolyForm NC requires a licence for commercial use
of the software, and a port of it is a derivative work of it. *This needs an actual
opinion, not a judgement call by us.* Until it is resolved:

> **`workbench/` does not ship in anything we sell, and we do not market it as ours.**

If the answer is "yes it's encumbered", the choice is binary: obtain a licence from
that author (a conversation, not a purchase), or replace the workbench. We should
not discover this during a sales call.

**2b. Remotion gates anything that renders for money.** The Remotion licence is free
for individuals and small companies; companies may need a paid licence. Two different
products are affected differently:

- **Hosted render farm** — we would render on our own infrastructure using Remotion
  in a commercial service. This is the most exposed possible use. Highest risk,
  and the licence cost may exceed the margin.
- **Agency service** — we render for a client. Same question, smaller surface, and
  answerable per-client by client size.

Everything that does *not* render is untouched by this. That is the tell for
sequencing.

**2c. Six audio files cannot ship in a paid delivery.** `assets/audio/ATTRIBUTION.md`
records them as untraceable to a source URL. The `audio_asset` table currently marks
all 154 as `commercial_ok=1`, which contradicts the registry — that is a data defect
(`doctor.py: license.audio_consistency`) *and* a real exposure. Replace or
re-license them before the first invoice.

## 3. Re-ranking the five logged opportunities

`opportunity` has five rows, all `status='idea'`, none validated. My ranking differs
from the table's implicit order, and the reason is the gate in §2 — not ambition.

| Rank | Opportunity | Why here |
|---|---|---|
| **1** | `localized-library-hub` | **No licence gate at all.** We do not render, so Remotion never enters the picture. The pipeline is already ~80% built: index exists, wiki exists, 9 locales seeded. It is also the only one whose output *is* the moat — an index nobody else will build. |
| **2** | `agency-film-in-a-day` | Fastest cash, and it validates demand before we build anything. **Gated:** needs a Remotion position before the first large-company client, and it consumes the most founder time per pound. Run it as cash-flow, not as the company. |
| **3** | `enterprise-license` | The right shape — Apache-2.0 forces us to sell the non-repo part (branded skill, per-PR render CI, acceptance report). 2–3 months to be credible. It also *needs* a hosted renderer internally, so it inherits the Remotion gate. |
| **4** | `brand-pack-marketplace` | Cheap to build, but **redistributing Mixkit audio in a paid pack is its own licence question**, so scope it to themes and palettes only (upstream already ships 9 themes — see `template/THEMES.md`). Small revenue, small risk, small effort. |
| **5** | `render-farm-saas` | Largest theoretical upside, **highest licence exposure**, and 3–4 months. Do not start it. Revisit only once §2b is answered, because a licence cost above the margin kills it outright. |

**Recommendation:** build #1, use #2 for cash, hold #3 as the destination, take #4
only if it is a weekend. Do not start #5.

## 4. Monetizing the hub honestly

The temptation with 10.1k stars is to monetise attention. Resist most of it.

**Ads are near-worthless here.** The audience is developers and motion designers
who block ad networks, and the RPM on that traffic is pennies. If ads are in the
plan they should be expected to contribute noise, not revenue.

**The real model is lead generation into a service.** The hub's job is to be the
answer to "how do I animate my product page", and to be findable in seven languages
where the competition is English-only and thin. Each page is a proof-of-work asset:

```
   organic traffic (7 locales, long-tail: "product promo video" + "motion design")
        │
        ├─► card page  ──► "want this in your product? we do this in a day"
        ├─► param page ──► "your easing curves are off-brand"  ← the real hook
        └─► licence page ─► "you may use this commercially, here is why"
        │
        ▼
   agency service  ──►  enterprise licence (branded skill + CI + SLA)
```

Two observations worth acting on:

- **The parameter tables are the moat, not the cards.** 1,057 extracted rows across
  157 cards, each with a "调节手感" pass/fail note. That is *tuning knowledge*, it is
  what a card's prose cannot express, and it is exactly what an agent — or a
  designer — cannot get elsewhere. Rank and index pages by parameter, not by card
  name. (`param_fts` being empty is therefore not a minor bug; it is blocking the
  most differentiated surface we have.)
- **The licence page is a revenue asset.** We can state plainly that the core is
  Apache-2.0, that the 48-card batch contains no third-party footage or brand
  assets, and what the audio situation is. Competitors selling "premium" motion
  libraries cannot make that claim. Transparency here is a differentiator, and it is
  already written down in `ATTRIBUTION.md`.

## 5. What "validated" means before we spend anything

None of the five opportunities is validated, and the table says so honestly. Cheap
tests, in order:

1. **Hub demand** — publish RU + one more locale, instrument it, and check whether
   non-English long-tail actually converts. Cost: one build step, which Part 3
   already delivers. Kill criterion: no measurable non-English traffic in 8 weeks.
2. **Service demand** — sell the 36-second film once, publicly, at a real price.
   Cost: one day. Kill criterion: no inbound after three public posts.
3. **Remotion position** — a written answer from Remotion on company-tier use for a
   service. Cost: an email. **This gates 2, 3 and 5, so it goes first, today.**
4. **Workbench licence position** — a written answer from the `video-talkcraft`
   author. Cost: an email. **This gates any enterprise offering, so it goes first,
   today.**

Tests 3 and 4 cost an email each and unblock three of five opportunities. They are
the highest-leverage actions available and neither requires code.

## 6. What not to do

- **Do not lock up the cards.** Apache-2.0 forbids it, 10.1k stars make
  circumvention trivial, and it converts a friendly audience into adversaries.
- **Do not sell an "enterprise edition" of the repository.** It is Apache-2.0. The
  product is the service around it.
- **Do not rebrand upstream as ours without attribution.** ADR 0005 covers this;
  the audience follows the author and misattribution costs the audience we need.
- **Do not start the render farm** until §2b is answered in writing.
- **Do not build a SaaS around the wiki before `doctor.py` is green.** Selling
  access to an index that loses three card identities means a customer's agent
  quietly gets wrong answers and blames us.