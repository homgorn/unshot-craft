# ADR proposal — the measurable cost of rule 5 (style identity)

- Status: **decision memo, not a decision.** `docs/architecture/README.md` and
  AGENTS.md hard rule 5 stand. This document prices the rule so it can be kept or
  changed deliberately rather than by accident.
- Date: 2026-10-01 · upstream SHA `5ddbf521038b0a7accfb6dc1e0a9eb29c67277ab`
- Verify: `python platform/doctor.py` → checks `style.*`, `media.*`

## The rule

AGENTS.md hard rule 5:

> Card↔style links come from the demo directory, not from `gallery/api/library.json`.
> Upstream's file is lossy (31 keys have no matching demo). Divergences go in
> `gallery_style`, not into the bin.

**The premise is correct and the architecture README §3 explains it well:**
upstream `library.json` really is lossy. `crash-zoom-punch` advertises 1 style key
while `demos/camera/crash-zoom-punch/` holds 2 components; `shot-transitions`
advertises 6 while its directory holds 7.

**What the memo adds is the other half of the truth:** the demo directory is lossy
too, in a different place, and the two losses do not overlap.

## Two identities, two loss modes

One style ("式") has two candidate identifiers:

| source | rule | count | example |
|---|---|---|---|
| `library.json` → `styles[].key` | hand-authored by the author | **214** | `whip-pan`, `crash-zoom-punch`, `basic-3d-scene` |
| `kebab(<Comp>.tsx)` | derived from our filename scan | **218** | `whip-pan-real`, `crash-zoom-real`, `basic-3-dscene` |

They disagree on **34 keys**, spanning **20 of 157 cards**. Neither is complete, and
that is the real finding — it is not "upstream is lossy and we are right":

- upstream loses where a card has **more demos than advertised keys**
  (`crash-zoom-punch`: 2 demos, 1 key);
- we lose where a demo's **filename differs from the advertised key**
  (`WhipPanReal.tsx` ↔ `whip-pan`).

## Measured consequences

`python platform/doctor.py`, all numbers reproducible:

| check | result | meaning |
|---|---|---|
| `style.identity.lost` | **211/214** | 3 upstream keys match neither authority and are **gone** |
| `style.divergence_recorded` | 31 + 38 | 31 upstream keys in `gallery_style`; 38 demo-derived keys with no upstream counterpart |
| `media.upstream_reachable` | **214/214 PASS** | every upstream preview *is* fetchable, via `gallery_style.media_url` |
| `media.coverage` | **35 styles have no media row at all** | their derived key matches no upstream `.mp4` |
| `style.kebab_casing` | **7 keys** | `3D` → `3-D`; matches no upstream key either |
| `media.poster_orphans` | 3 | `basic-3d-scene.jpg`, `carousel-3d.jpg`, `terminal-3d.jpg` on disk, unreferenced |

**Correction to an earlier reading of mine:** previews are *not* unreachable. Because
`gallery_style` carries `media_url` copied verbatim from upstream, all 214 are
fetchable. The real cost is narrower and different:

> **35 styles carry no preview in our index at all**, and **3 cards lose their
> identity entirely**.

### The 3 lost keys are a `kebab()` bug, not a rule-5 consequence

`motion.py:kebab()` inserts a hyphen on *both* sides of a digit boundary:

```python
s = re.sub(r"([A-Za-z])(\d)", r"\1-\2", stem)   # Basic3DScene  -> Basic-3DScene
s = re.sub(r"(\d)([A-Za-z])", r"\1-\2", s)      # Basic-3DScene -> Basic-3-DScene
```

`Basic3DScene → basic-3-dscene`. Upstream says `basic-3d-scene`. The fuzzy `norm()`
fallback also fails, because `norm()` strips hyphens — so it cannot repair a rule
that invented one. Same for `Terminal3D → terminal-3-d` and `Carousel3D → carousel-3-d`.

**This one should be fixed regardless of the rule-5 decision**, because a key that
matches nothing is wrong under either authority. Cheapest correct rule: make the
digit boundary asymmetric — split between letters and digit-groups, never inside a
letter-digit run:

```
Basic3DScene   -> basic-3d-scene      Terminal3D -> terminal-3d
ChartV2        -> chart-v2            OscilloscopeStreamV2 -> oscilloscope-stream-v2
```

## The recommendation

Keep rule 5. It is the right default — the demo directory is the only source that
survives an upstream `library.json` rewrite, and upstream demonstrably rewrites it by
hand. But change **what the key means**, without changing **where the link comes from**:

```
style.key                     ← kebab(<Comp>.tsx), fixed rule      (unchanged source)
style.gallery_style_key       ← upstream key when one matches       (already exists)

gallery_style                 ← upstream keys with no demo match    (already exists)
```

and add the one column that makes the loss legible instead of silent:

```
style.media_status           ← ok | no-upstream-preview | key-lost
```

Cost: one regex fix, one new column, one backfill. Benefit: the 35 media-less styles
and the 3 lost keys become **visible facts with names**, which is what
`platform/query.py` and the site need in order to not invent a video URL that 404s.

Rejected alternative, for the record: **make `library.json` the authority for style
identity.** It would fix the 34 key collisions and recover the 3 lost keys, but it
re-introduces the exact failure rule 5 was written to prevent — a hand-authored
upstream file silently deciding which of our 218 demos is real. `shot-transitions`
would drop a demo every time the author forgets to list one. The hybrid above gets
the alignment without giving up the authority.

## What is a defect under any reading

Three items in this area need fixing and are not up for decision:

1. `style.kebab_casing` — 7 keys match nothing (`platform/doctor.py` FAIL).
2. `style.identity.lost` — 3 upstream keys unrecoverable (FAIL).
3. `media.coverage` — 35 styles with no preview and no marker saying so (FAIL).

`media.upstream_reachable` passing at 214/214 means no consumer is currently being
handed a broken URL. That is the good news: rule 5 is costing us *completeness*, not
correctness. Nothing we have published is wrong; things are merely missing.