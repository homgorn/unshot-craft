# "Rule of Thirds Prompt for AI Image & Video"

`rule-of-thirds` · Composition · level basic

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Rule of thirds composition with [Subject] positioned at the upper-right power point intersection, eyes precisely on the top horizontal third line, the remaining two-thirds of the frame filled with negative space creating natural visual flow, the composition dynamically balanced despite being asymmetrical, shot on a 50mm lens at T2.8, overcast daylight providing even naturalistic illumination
```

Dividing the frame into a 3x3 grid and placing key elements along the lines or at their intersections, creating naturally balanced, dynamic compositions that feel more alive than dead-center framing. While most directors use the rule instinctively, Roger Deakins and the Coen Brothers apply it with mathematical precision in films like "Fargo" and "No Country for Old Men." Emmanuel Lubezki frequently places subjects at the right-third intersection in Terrence Malick's films, leaving vast spaces of sky or landscape to fill the remaining two-thirds. The rule derives from classical painting compos…

**When to use.** Use the rule of thirds when a centered frame feels static but the composition still needs immediate clarity. It suits portraits, landscapes, interviews, and moving subjects because it creates space for gaze, direction, or environment. Place the focal point at an intersection and use the remaining area intentionally. The grid is a starting structure, not a decoration; break it when confrontation,…

**Directing the AI.** Divide the frame mentally into a three-by-three grid. Place the subject's primary focal point, often the eyes or face, on one power-point intersection and align the horizon or dominant architecture with a third line. Give the open two-thirds a purpose through landscape, gaze direction, or approaching action. Keep secondary elements from competing with the focal point. For video, preserve useful lead room as the subject moves rather than forcing them mechanically onto one grid point in every fra…

**Common mistakes.**
- Placing the subject near a third line while leaving the remaining space empty of meaning or directional purpose.
- Aligning every object to the grid, creating a visibly calculated frame instead of a naturally balanced composition.
- Using the rule during direct confrontation or formal symmetry, where off-center placement weakens the intended psychological force.

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
| declared | `space-camera-moves` | camera | 150 | `drone-dive-landing` |
| declared | `space-camera-moves` | camera | 150 | `exploded-view` |
| declared | `spotlight-hero-card` | opening | 220 | `spotlight-hero-card` |

```
python platform/query.py technique-motions rule-of-thirds
```

## Sources

- Rules of Shot Composition in Film

## Related techniques

- [('balancing-elements', 'balancing-elements')](('balancing-elements', 'balancing-elements').md)
- [('negative-space', 'negative-space')](('negative-space', 'negative-space').md)
- [('lead-room', 'lead-room')](('lead-room', 'lead-room').md)
- [('symmetry', 'symmetry')](('symmetry', 'symmetry').md)
- [('leading-lines', 'leading-lines')](('leading-lines', 'leading-lines').md)
- [('framing-within-frame', 'framing-within-frame')](('framing-within-frame', 'framing-within-frame').md)
- [('shallow-focus', 'shallow-focus')](('shallow-focus', 'shallow-focus').md)
- [('deep-focus', 'deep-focus')](('deep-focus', 'deep-focus').md)
- [('mise-en-scene', 'mise-en-scene')](('mise-en-scene', 'mise-en-scene').md)
