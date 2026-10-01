# "Symmetry Prompt for AI Image & Video"

`symmetry` · Composition · level basic

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Perfect bilateral symmetry with [Subject] standing at the exact center of the vanishing point, matching elements receding into infinity on both sides, the symmetry so absolute it becomes psychologically oppressive rather than beautiful, shot on a wide 24mm lens from a locked-off tripod at exact center height, Kubrick one-point-perspective severity
```

A composition where both halves of the frame mirror each other, creating a sense of order, formality, perfection, or unsettling precision. Stanley Kubrick made symmetry his defining visual signature — the one-point-perspective corridor shots of "The Shining" and "A Clockwork Orange" remain the technique's most analyzed examples. Wes Anderson took symmetry to its whimsical extreme, making it the entire visual language of "The Grand Budapest Hotel" and "The French Dispatch." Denis Villeneuve uses cold, imposing symmetry in "Blade Runner 2049" and "Arrival" to convey alien or corporate power str…

**When to use.** Symmetry is strongest when order itself carries emotion. Use it for ritual, authority, control, artificial perfection, deadpan comedy, or an unsettling sense that the world has been arranged too precisely. Corridors, facades, tables, and grouped characters provide natural mirrored structure. The effect depends on exact camera position and balanced set elements. Avoid casual near-symmetry; small e…

**Directing the AI.** Lock the camera on the exact center axis of the space and place the subject at the central vanishing point. Mirror major architectural forms, props, spacing, and light levels across the vertical divide. Keep lens height level so lines do not drift. Decide whether the symmetry feels playful, formal, or oppressive through scale and repetition. In video, use stable movement directly along the center axis; lateral drift should either remain absent or become a clear rupture of the ordered frame.

**Common mistakes.**
- Setting the camera slightly off-axis, causing doorways, ceiling lines, and vanishing points to disagree across the frame.
- Mirroring broad shapes but ignoring light, color, and spacing, leaving the composition balanced only at first glance.
- Breaking symmetry with several unrelated objects, so no single disruption gains the attention or narrative weight it deserves.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` | `camera_motion: pan_right | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: smooth_pan` | pika-1.5 | no |
| `runway_gen3` | `motion_brush: smooth_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: smooth_pan` | sora-1 | no |
| `veo2` | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

## Motion pairings

**Declared, not inferred.** These come from an explicit `styles:` list in `data/cinematic/<slug>.md`, authored in `platform/catalog/pairings.py`. Nothing here is matched by name similarity.

| kind | shot card | category | frames | style |
|---|---|---|---|---|
| declared | `orbit-ring-title-open` | opening | 130 | `orbit-ring-title-open` |

```
python platform/query.py technique-motions symmetry
```

## Sources

- Rules of Shot Composition in Film

## Related techniques

- [('centered-composition', 'centered-composition')](('centered-composition', 'centered-composition').md)
- [('leading-lines', 'leading-lines')](('leading-lines', 'leading-lines').md)
- [('repetition-and-pattern', 'repetition-and-pattern')](('repetition-and-pattern', 'repetition-and-pattern').md)
- [('rule-of-thirds', 'rule-of-thirds')](('rule-of-thirds', 'rule-of-thirds').md)
- [('framing-within-frame', 'framing-within-frame')](('framing-within-frame', 'framing-within-frame').md)
- [('negative-space', 'negative-space')](('negative-space', 'negative-space').md)
- [('shallow-focus', 'shallow-focus')](('shallow-focus', 'shallow-focus').md)
- [('deep-focus', 'deep-focus')](('deep-focus', 'deep-focus').md)
- [('mise-en-scene', 'mise-en-scene')](('mise-en-scene', 'mise-en-scene').md)
