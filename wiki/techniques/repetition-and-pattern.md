# "Repetition and Pattern Prompt for AI Image & Video"

`repetition-and-pattern` · Composition · level intermediate

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Repetition and pattern composition with [Subject] as the single disruption in an otherwise uniform array, hundreds of repeated elements creating mesmerizing regularity with one anomaly immediately drawing the eye, the visual principle that the human eye is hardwired to detect anomalies in regular patterns, shot on a 50mm lens at f/4 with the full pattern sharp edge to edge, warm ambient lighting
```

Using recurring visual elements — shapes, colors, objects — to create rhythm and unity in the frame, where breaking a pattern draws immediate attention to the disruption. Kubrick's symmetrical corridors in "The Shining" use pattern repetition to create hypnotic unease, and any break in the pattern (the twins at the end of a hallway) becomes terrifying. Wes Anderson builds frames from repeated elements — rows of identical doors, matching uniforms, symmetrical windows. Zhang Yimou uses massive pattern compositions of soldiers, lanterns, and fabric in "Hero" and "House of Flying Daggers" where a…

**When to use.** Repetition and pattern works when order, scale, routine, conformity, or obsession should dominate the frame. Rows of windows, uniforms, doors, lights, or bodies create rhythm that the eye reads quickly. One anomaly then gains immediate narrative force. Use the technique for architecture, crowds, ritual, comedy, or unease. The repeated units need consistent shape and spacing; if variation is alrea…

**Directing the AI.** Build a clear array of recurring shapes, colors, objects, or figures with consistent spacing and orientation. Choose one subject as the only meaningful break through color, pose, absence, or direction. Keep the full pattern readable across the frame and give the anomaly enough contrast to register without becoming unrelated. For video, establish the regular rhythm before introducing disruption, then preserve continuity in the repeated units as the camera moves through or across them.

**Common mistakes.**
- Varying color, size, and spacing across every repeated unit, leaving no stable pattern for the audience to recognize.
- Introducing several anomalies at once, which divides attention and weakens the narrative force of the intended disruption.
- Cropping the array so tightly that repetition cannot accumulate into rhythm or communicate a larger ordered system.

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
| declared | `icon-field-colorize` | opening | 45 | `icon-field-colorize` |

```
python platform/query.py technique-motions repetition-and-pattern
```

## Sources

- Rules of Shot Composition in Film

## Related techniques

- [('symmetry', 'symmetry')](('symmetry', 'symmetry').md)
- [('motif', 'motif')](('motif', 'motif').md)
- [('leading-lines', 'leading-lines')](('leading-lines', 'leading-lines').md)
- [('rule-of-thirds', 'rule-of-thirds')](('rule-of-thirds', 'rule-of-thirds').md)
- [('framing-within-frame', 'framing-within-frame')](('framing-within-frame', 'framing-within-frame').md)
- [('negative-space', 'negative-space')](('negative-space', 'negative-space').md)
- [('shallow-focus', 'shallow-focus')](('shallow-focus', 'shallow-focus').md)
- [('deep-focus', 'deep-focus')](('deep-focus', 'deep-focus').md)
- [('mise-en-scene', 'mise-en-scene')](('mise-en-scene', 'mise-en-scene').md)
