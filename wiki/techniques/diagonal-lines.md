# "Diagonal Lines Prompt for AI Image & Video"

`diagonal-lines` · Composition · level basic

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Diagonal line composition with [Subject] surrounded by aggressive 45-degree angles, nothing horizontal or vertical in the entire composition, every line tilted and active, the deliberate absence of any stable reference creating dynamic instability and forward momentum, shot on a 24mm wide-angle with slight barrel distortion enhancing angular dynamism
```

Using diagonal elements in composition to create dynamic energy and movement, as diagonals feel inherently unstable and active compared to horizontal or vertical lines. Carol Reed filled "The Third Man" with diagonal compositions — tilted streets, canted angles, shadow lines cutting diagonally across walls — to visualize post-war Vienna's moral instability. Michael Bay uses aggressive diagonal compositions in his action sequences to maximize kinetic energy. Christopher Nolan employs diagonal lines in "Inception" during the dream sequences where architecture literally tilts, and Ridley Scott u…

**When to use.** Diagonal lines suit action, pursuit, imbalance, conflict, and scenes that should resist calm horizontal or vertical order. Streets, shadows, rain, architecture, bodies, and camera angle can all create active slants through the frame. Use them to push the eye forward or make the world feel unstable. The technique loses force when every line tilts randomly; choose a dominant direction and let oppos…

**Directing the AI.** Build the composition around one strong diagonal, roughly crossing from a lower corner toward the opposite upper area. Align architecture, shadow, rain, or body movement with that direction, then place the subject where the line delivers attention. Minimize stable horizontal references if instability is the goal. Use a second opposing diagonal only to create deliberate friction. For video, carry movement along the chosen slant or reveal it through a controlled camera tilt, not arbitrary frame w…

**Common mistakes.**
- Tilting every object in a different direction, creating visual confusion rather than one readable source of dynamic energy.
- Leaving a dominant horizon perfectly stable while minor props angle randomly, weakening the intended sense of instability.
- Using diagonals in a quiet formal scene where their kinetic pressure contradicts the emotional pace and staging.

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
| declared | `steep-tilt-glide` | camera | 120 | `steep-tilt-glide` |

```
python platform/query.py technique-motions diagonal-lines
```

## Sources

- Rules of Shot Composition in Film

## Related techniques

- [('dutch-angle', 'dutch-angle')](('dutch-angle', 'dutch-angle').md)
- [('leading-lines', 'leading-lines')](('leading-lines', 'leading-lines').md)
- [('contrast-composition', 'contrast-composition')](('contrast-composition', 'contrast-composition').md)
- [('rule-of-thirds', 'rule-of-thirds')](('rule-of-thirds', 'rule-of-thirds').md)
- [('symmetry', 'symmetry')](('symmetry', 'symmetry').md)
- [('framing-within-frame', 'framing-within-frame')](('framing-within-frame', 'framing-within-frame').md)
- [('negative-space', 'negative-space')](('negative-space', 'negative-space').md)
- [('shallow-focus', 'shallow-focus')](('shallow-focus', 'shallow-focus').md)
- [('deep-focus', 'deep-focus')](('deep-focus', 'deep-focus').md)
