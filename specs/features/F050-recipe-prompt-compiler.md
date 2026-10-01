# F050 — Recipe → prompt compiler

- Status: implemented, **not verified** (`passes: false`)
- Ledger entry: `specs/feature-list.json` → `F050`
- Builder: `platform/prompts/build_prompts.py`
- Output: `prompts/generated/<slug>.json` ×157 + `prompts/generated/index.json`

## What this is

Every one of the 157 shot cards compiles into a **brief**: the minimum a renderer
or an agent needs to execute that one shot, pre-joined from rows we already hold.

It exists because `vision.md` says we compete on *rendered outcomes*, and because
`brainstorm.md` Tier 0 sells a film "before your funding announcement". Both need a
machine-readable shot list. Today the only machine-readable shot list is
`library.json`, which upstream writes by hand for their gallery.

## The one design rule

> **The brief is structure. The copy is a slot.**

The compiler never invents prose. Every string it emits is either verbatim upstream
text (frontmatter, a `## 动效核心` bullet, a `## 参数表` cell, a `## 已知坑` line) or
a literal marker. `copy.authored` is `false` in all 157 generated briefs, by
construction, and the `copy.note` says so.

The reason is specific, not stylistic: a generated one-liner *looks* authored. Put it
in the brief and an agent will quote it to a client as though a human wrote it. We
would be selling machine filler as taste. The slot makes the gap impossible to
miss.

## What is actually derived

| field | source | notes |
|---|---|---|
| `render.duration_frames` | `shot_card.duration_frames` | 152/157; technique cards use `n/a` |
| `render.energy` + `energy_rationale` | `energy_level` + verbatim split | AGENTS.md rule 4: prose kept twice |
| `beats[]` | `card_section` where kind ∈ motion/phases/variants | one per bullet, `raw` verbatim |
| `beats[].frame_hints` | `126f` scraped from prose | 78/157 cards |
| `beats[].window` | `seg(t,a,b)` or `0.06-0.56` | only 24/157 — see the honest note |
| `segments[]` | `motion_param` where kind=`segment` | **authoritative**, from the `.tsx` |
| `parameters[]` | `card_param` | verbatim incl. `variant_letter` |
| `pitfalls[]` | `card_pitfall` | verbatim + `is_critical` + `rule_refs` |
| `rules[]` | `rule`, resolved from pitfall citations | |
| `styles[]` | `style` via `card_variant` | demo path, component, own duration |
| `tags[]` | `shot_card_tag` | includes cross-category tags |
| `source.card_sha256` | `source_file` | provenance to the byte |

## The negative result, which matters

**A normalized `[t0, t1]` timeline is not derivable from most cards.** Measured over
1,349 motion-section bullets:

| notation | bullets |
|---|---|
| `seg(t, a, b, E.x)` | 40 |
| `seg(` any form | 69 |
| `t=0.06–0.56` | 20 |
| bare `0.x–0.y` | 24 |
| **`Nf` frame counts** | **136** |
| `E.<ease>` | 40 |
| `outCubic`-family names | 90 |
| `spring(` | 10 |

So: five incompatible notations, the most common being **frames**, and only 44 of 218
demos contain a literal `seg()` call at all. Of the 199 segments we do extract, 119
carry literal numbers and 80 are symbolic (`from: "FLY_AT[i]"`), which is why each
segment has a `concrete: true|false` flag — a renderer must never be handed a variable
name where it expects a number.

**Consequence for F060:** we cannot auto-derive the timeline. The demos stay the
authoritative implementation. A real timeline is *authored*, which is exactly what
F051's reference briefs are for.

## Why `prompts/` is generated, not hand-written

Same rule as `wiki/` (ADR 0003): the tree is a pure function of the database. Delete
it, re-run, it returns byte-identically. Nobody edits `prompts/generated/` by hand;
`copy.slots` exist to be filled in a *derived* brief, and the authored result lives
in `prompts/reference/`, which is source.

## Verification

```powershell
python platform/prompts/build_prompts.py
python platform/prompts/build_prompts.py --lint     # F051, validates reference briefs
python platform/doctor.py                            # prompts.* checks
```

`doctor.py` fails if the tree is short relative to `shot_card`, if `index.json` is
missing, or if any hand-authored brief lies about being hand-authored.

## What is deliberately not here

- **No prose generation.** Discussed above.
- **No invented durations.** `duration_frames: null` is the honest value for the 5
  technique cards; it is not a defect to be filled in by estimation.
- **No scene description.** A brief says what the shot *is* and how it is timed. It
  does not say what the subject should be — that is the client's product, and it is
  the copy slot's job.