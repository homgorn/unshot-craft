# Motion grammar

This is the part of video-shotcraft that exists **only** as literals inside `demos/**/*.tsx`: the tuned curves, springs and timing windows. Nothing upstream indexes it. We extracted 1607 parameter occurrences across 218 demos.

## Two demo families

- **Family A (51 demos)** — the Motion lab. Normalized progress `t ∈ [0,1]` derived from `useCurrentFrame()` only, a 480×270 `DesignStage` design space, and a shared easing table `E`. Lengthening a clip *slows* the animation instead of truncating it.
- **Family B (167 demos)** — frame-driven. `interpolate(frame, [frames], [values], {easing, clamp})` plus Remotion's `spring({frame, fps, config})`. Absolute frame math.

Both are deterministic by rule 9 of SKILL.md: no `Date.now()`, no unseeded `Math.random()`.

## The house easing curve

50 distinct bezier curves are used. The dominant one is the de-facto house style — reach for it first when writing a new shot:

| curve | styles using it | overshoot |
|---|---|---|
| `bezier(0.3,0,0.2,1)` | 12 | no |
| `bezier(0.4,0,0.3,1)` | 5 | no |
| `bezier(0.5,0.05,0.6,1)` | 4 | no |
| `bezier(0.2,0.75,0.3,1)` | 4 | no |
| `bezier(0.4,0,0.2,1)` | 3 | no |
| `bezier(0.4,0,0.6,1)` | 3 | no |
| `bezier(0.55,0,0.7,1)` | 2 | no |
| `bezier(0.35,0,0.25,1)` | 2 | no |
| `bezier(0.16,1,0.3,1)` | 2 | no |
| `bezier(0.35,0,0.2,1)` | 2 | no |
| `bezier(0.4,0,0.4,1)` | 2 | no |
| `bezier(0.4,0,0.5,1)` | 2 | no |
| `bezier(0.25,0.8,0.25,1)` | 2 | no |
| `bezier(0.3,0.1,0.3,1)` | 2 | no |
| `bezier(0.35,0,0.3,1)` | 2 | no |
| `bezier(0.45,0,0.25,1)` | 1 | no |
| `bezier(0.3,0.12,0.72,0.9)` | 1 | no |
| `bezier(0.2,0.75,0.25,1)` | 1 | no |
| `bezier(0.5,0,0.25,1)` | 1 | no |
| `bezier(0.22,1,0.36,1)` | 1 | no |

Overshoot curves (`y1 > 1`) are the ones that produce the springy settle; the repo treats them as a cost, not a default — a shot gets **one** overshoot beat, not a bouncing loop.

## Spring configs observed

| style | damping | stiffness | mass | frames |
|---|---|---|---|---|
| `autolayout-gap-dial` | 9.0 | 80.0 | 1.1 | — |
| `autolayout-gap-dial` | 14.0 | 130.0 | — | — |
| `brand-frame-snap` | 16.0 | 110.0 | 1.0 | — |
| `cloner-depth-echo` | 11.0 | 200.0 | 0.7 | 18 |
| `cloner-depth-echo` | 14.0 | 160.0 | 0.8 | 16 |
| `cursor-cast-ensemble` | 15.0 | 90.0 | 0.9 | — |
| `diagram-cascade-build` | 11.0 | 170.0 | — | — |
| `icon-flip-bloom-logo` | 13.0 | 140.0 | 0.8 | — |
| `icon-flip-bloom-logo` | 11.0 | 130.0 | 0.9 | — |
| `input-morphs-into-logo` | 13.0 | 90.0 | 0.9 | — |
| `input-morphs-into-logo` | 12.0 | 110.0 | 0.85 | — |
| `orbit-ring-title-open` | 12.0 | — | — | — |
| `orbit-ring-title-open` | 13.0 | — | 0.7 | — |
| `orbit-ring-title-open` | 14.0 | — | — | — |
| `panel-to-canvas-materialize` | 10.0 | 260.0 | — | — |
| `panel-to-canvas-materialize` | 16.0 | 60.0 | — | 34 |
| `popup-book-rise` | 11.0 | 130.0 | 0.9 | — |
| `segmented-thumb-hero` | 14.0 | 120.0 | 0.9 | — |
| `segmented-thumb-hero` | 10.0 | 220.0 | 0.6 | — |
| `skeleton-reveal` | 16.0 | 160.0 | 0.7 | — |
| `timeline-travel` | 11.0 | 160.0 | 0.9 | 26 |
| `ui-strip-away-outro` | 12.0 | 220.0 | — | — |
| `ui-strip-away-outro` | 14.0 | 90.0 | — | — |
| `unit-dot-swarm-regroup-v-2` | 11.5 | 150.0 | 0.8 | — |

Modal cluster: damping 9–16, stiffness 60–260, mass 0.6–1.1. `damping ≤ 10` with `stiffness ≥ 200` reads as a hard mechanical snap; `damping ≥ 15` with `stiffness ≈ 90` reads as a heavy object settling.

## Timing envelope

Durations across all demos: min 10f, max 3980f, mean 137f, 100 demos with no discoverable constant.

The hard holds that must survive translation into any new film:

- brand wordmark settle ≥ 1s (30f) — rule R1
- batch motion tail 0.5s (15f) still — rule R3
- opening hero action arc ≥ 3s — rule R3
- beat-sync cut error ≤ 3 frames after render, measured against the extracted audio track

## Parameter kinds found

| kind | count | what it is |
|---|---|---|
| `interpolate` | 758 | `interpolate(input, inputRange, outputRange, opts)` — the frame-driven workhorse |
| `easing_fn` | 259 | `Easing.in/out/inOut(Easing.base)` |
| `segment` | 199 | `seg(t, t0, t1, E.x)` — the family-A equivalent of interpolate |
| `sin` | 110 | `Math.sin(...)` oscillation |
| `bezier` | 84 | `Easing.bezier(x1,y1,x2,y2)` |
| `constant` | 75 | exported duration/frame constants |
| `color` | 59 | named palette constants such as `BG`, `ACCENT` |
| `spring` | 24 | Remotion `spring({frame, fps, config})` |
| `easing_const` | 18 | a module-scope easing constant, resolved before use |
| `exp_decay` | 13 | `Math.exp(...)` shake/decay envelopes |
| `motion_blur` | 8 | `<CameraMotionBlur shutterAngle samples>` |