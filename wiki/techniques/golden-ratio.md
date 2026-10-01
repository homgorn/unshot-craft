# "Golden Ratio Prompt for AI Image & Video"

`golden-ratio` · Composition · level advanced

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Golden ratio spiral composition with [Subject] placed along the logarithmic curve, every major element sitting naturally along the mathematical spiral, the proportional harmony creating organic rightness that the eye follows without conscious awareness, shot on a 24mm wide-angle lens, the mathematical beauty that connects Fibonacci sequences to Renaissance painting to cinematic composition
```

Composing using the mathematical golden spiral (1.618:1) to place key elements along a naturally occurring logarithmic curve, creating compositions that feel organically harmonious. While debate exists about whether filmmakers consciously employ the golden ratio, analysis of work by Akira Kurosawa, Kubrick, and Spielberg reveals compositions that consistently align with the spiral. Vittorio Storaro has explicitly discussed using the golden ratio in his compositions for "Apocalypse Now" and "The Last Emperor." Renaissance painters from Leonardo to Vermeer used the proportion extensively, and i…

**When to use.** Use the golden ratio when a composition needs organic flow rather than the visible grid of thirds or the formality of symmetry. It suits landscapes, portraits in complex environments, still life, and layered action with a curved visual path. The spiral can connect a broad outer shape to a tight focal point. Treat it as a planning guide, not mystical proof of quality; subject hierarchy and readabl…

**Directing the AI.** Lay a logarithmic spiral across the frame and place the main subject near its tightest curl. Arrange larger environmental forms, secondary figures, or lines along the expanding arc so the eye travels inward naturally. Avoid drawing a literal spiral into the set unless the story requires one. Keep the focal point strongest through contrast and detail. For video, let camera or subject movement follow the curved path while preserving the final visual landing point.

**Common mistakes.**
- Forcing every prop onto a visible spiral, making the composition feel diagrammed instead of naturally organized around attention.
- Using the golden ratio as a substitute for contrast, depth, and subject hierarchy, leaving the focal point weak.
- Confusing the technique with centered symmetry, which removes the expanding curved path that should guide the viewer.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

## Motion pairings

**Declared, not inferred.** These come from an explicit `styles:` list in `data/cinematic/<slug>.md`, authored in `platform/catalog/pairings.py`. Nothing here is matched by name similarity.

| kind | shot card | category | frames | style |
|---|---|---|---|---|
| declared | `orbit-ring-title-open` | opening | 130 | `orbit-ring-title-open` |

```
python platform/query.py technique-motions golden-ratio
```

## Sources

- Rules of Shot Composition in Film

## Related techniques

- [('rule-of-thirds', 'rule-of-thirds')](('rule-of-thirds', 'rule-of-thirds').md)
- [('leading-lines', 'leading-lines')](('leading-lines', 'leading-lines').md)
- [('balancing-elements', 'balancing-elements')](('balancing-elements', 'balancing-elements').md)
- [('symmetry', 'symmetry')](('symmetry', 'symmetry').md)
- [('framing-within-frame', 'framing-within-frame')](('framing-within-frame', 'framing-within-frame').md)
- [('negative-space', 'negative-space')](('negative-space', 'negative-space').md)
- [('shallow-focus', 'shallow-focus')](('shallow-focus', 'shallow-focus').md)
- [('deep-focus', 'deep-focus')](('deep-focus', 'deep-focus').md)
- [('mise-en-scene', 'mise-en-scene')](('mise-en-scene', 'mise-en-scene').md)
