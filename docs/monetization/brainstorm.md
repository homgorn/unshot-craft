# Brainstorm: how this actually makes money

## The asset, stated honestly

| what | size | is it ours? |
|---|---|---|
| Apache-2.0 skill: 157 cards, 218 tuned TSX demos | ~4.6 MB of code | **no** — anyone can fork |
| 154 licensed audio assets | 35 MB | no |
| 10.1k stars / 899 forks | — | no, and not the point |
| **9-locale index + search** | ours | **yes** |
| **1,057 extracted parameters, 1,897 motion params** | ours | **yes** — nobody indexes this |
| **A studio that ships films** | ours | **yes** |
| **Licence/compliance clarity for Remotion** | ours | **yes** — and it's a real blocker |

**The core is free. Therefore nothing we sell can be the code.** Every viable
model sells one of three things: a *rendered outcome*, a *service nobody else
wants to do*, or *support the free thing does not include*.

---

## Tier 0 — start here, this week

### 1. Agency: "a launch film before your funding announcement"

**Why this is first:** a hands-on third-party run reports ~35 minutes of hands-on
time for a 36-second promo, and upstream ships a validated 36.2 s / 10-shot
template. That is a unit-economics story, not a tool story.

- Sell the deadline, not the repo. The buyer is a founder whose Series A deck
  needs a video in 48 hours.
- Price against the alternative, which is an agency quote of €2–8k.
- The library is what lets us quote 48 hours instead of two weeks.
- **Risk:** it is trading time for money and does not scale. It buys us case
  studies and cash. Cap it.

### 2. Brand kits (paid presets) — S effort, 3–5 weeks to first revenue

The core already ships **9 visual themes** (`template/THEMES.md`) and 149 SFX.
Selling pre-skins that drop into the same schema is margin on work already done.

- Ship: 10–15 brand kits (palette + type + texture + SFX set), each ~$29–99.
- Distribution: the site, plus a `npx`-style install that layers over the skill.
- **Why it works:** the runtime, the cards and the acceptance rules are free and
  already adopted. We are selling taste, and taste is the one thing a repo cannot
  ship.
- **Watch:** Apache-2.0 means anyone can resell a theme pack. Our moat is volume
  and curation speed, not exclusivity.

---

## Tier 1 — the SEO engine

### 3. The localized library hub → service lead-gen

**The thesis:** upstream ships a library site with two locales and English-only
card copy. The keyword space is English-dominant; the audience is global. For
"product promo video", "motion design shot library", "video-shotcraft
alternative", RU/ES/DE/FR/PT/KO/JA pages are almost empty.

- **Traffic → lead → film.** The library page is the proof-of-work; the CTA is
  "have us make yours".
- **9 locales × 157 cards = 1,413 indexable pages.** Each one is a real page
  with a real video, not a thin doorway page — this is what makes it survive a
  quality update.
- **Second revenue line:** the same pages earn display/affiliate revenue and
  backlinks, so a page that does not convert still pays rent.
- **Prerequisite:** ADR-0004. Without locale-prefixed URLs and hreflang, this
  does not exist. That is why i18n is priority 3 in the build order and not
  "nice to have".
- **Risk:** Google may treat machine-translated 157-card pages as scaled content
  abuse. Mitigation: human review of the top 40 cards per locale, real
  editorial on the landing pages, and no page that is only a translation.

### 4. The wiki as a lead magnet with a twist

`wiki/llms.txt` + `llms-full.txt` + a searchable index is the kind of artifact
that gets cited by AI assistants — and AI assistants are becoming a referral
channel. Cheap to host, compounding, and it doubles as the asset that makes the
micro-SaaS credible.

- Publish under our brand, link upstream prominently (credibility + good faith).
- Monetize indirectly: it is the top of funnel for the service and the SaaS.

---

## Tier 2 — product, needs validation first

### 5. Micro-SaaS: hosted shot preview

**The pain is documented, not invented.** The README itself lists three headless
Linux walls for anyone rendering locally: the concurrency cap, the removal of
old headless mode, and the blocked CDN. Installation is `ln -s` into
`~/.claude/skills`.

- **Free tier:** upload screenshots, get one shot preview.
- **Paid:** render the film, get the MP4, per-shot parameter editing.
- **The real product is the escaping of Node + Chrome + Remotion licensing
  decisions from the client's CI.** That is a platform problem we can own.
- **Hard prerequisite we must not forget:** Remotion needs a paid licence for
  companies. A hosted service must price that in per render, or the client buys
  it. Get this right *before* building, not after the first enterprise customer.

### 6. B2B licence: branded skill + acceptance report

Apache-2.0 means the code cannot be locked up — so the defensible B2B product is
what is **not in the repo**:

1. A branded skill pinned to the client's own design system (their fonts, their
   tokens, their product screenshots), so a release note becomes a video.
2. CI that renders the promo on every PR — this is upstream's own `pr-checks.yml`
   pattern extended to a deliverable.
3. An acceptance report per release with frame-numbered evidence — a real
   artefact from `references/final-review.md`, sold as a process.
4. **Remotion licence navigation.** Companies get stuck here; being the party who
   already knows the answer is worth a line item.

- Price as an annual platform fee + onboarding. This is the only model that
  scales without trading time for money.

---

## What I would NOT do

- **Sell the fork.** Apache-2.0 means a competitor can undercut us with the same
  code. We would be selling a commodity at a premium.
- **Chase upstream stars.** 10.1k and counting, plus a fast release cadence. A
  fork chases forever and loses.
- **Touch `video-talkcraft` commercially.** PolyForm Noncommercial. Reading and
  porting techniques is fine — upstream already ported 19 cards. Shipping is not.
- **Build a full editor.** The upstream workbench already exists and is
  Apache-2.0. We would be rebuilding a CapCut clone. If we enter this space at
  all, it is a hosted thin client over *their* timeline model, never a fork of it.
- **Ad revenue as the primary plan.** Display ads on a niche B2B-intent keyword
  pay pennies. Ads here are a bonus on a page that already exists, not a business.

---

## Sequence

```
week 0-1   Agency first offer.  2 films, free or cheap, to get case studies + real timings.
           In parallel: i18n extraction (ADR-0004) — the SEO asset needs it.
week 2-4   3 brand kits shipped.  Measure: do people buy them without a sales call?
week 3-8   RU + DE + ES library pages live, hreflang correct. Measure impressions, not just rank.
week 8-12  Decide on SaaS from inbound: are people asking to *render*, or to *hire*?
           Those are different products. The inbound message tells you which.
```

## The one number that decides everything

**Does inbound say "render this for me" or "do this for me"?**

- "Do this for me" → the service model is the business. The SaaS is a feature
  that makes delivery faster, not the company.
- "Render this for me" → the SaaS is the business, and the service was a
  customer-acquisition channel that happened to pay for the first year.

Getting this wrong is the expensive mistake: building a SaaS when the market
wants an agency burns a year. Run the agency first, at small volume, and let the
inbound messages decide.