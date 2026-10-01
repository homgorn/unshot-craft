# "Centered Composition Prompt for AI Image & Video"

`centered-composition` · Composition · level basic

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Centered composition with [Subject] at the exact mathematical center, the space arranged in perfect bilateral symmetry around them, the deliberate center placement creating ritual importance and confrontational directness, shot on a 28mm lens from a locked tripod at center height, deep focus rendering every detail sharp, Wes Anderson planimetric aesthetic meets Kubrick one-point-perspective severity
```

Placing the subject dead center in the frame — when done deliberately, it creates a powerful, confrontational, or hypnotically ordered effect that requires confidence and intentionality. Wes Anderson builds his entire visual identity around centered subjects, creating his trademark "planimetric" compositions. Kubrick's centered one-point-perspective shots in "The Shining" and "Full Metal Jacket" use the center position for maximum psychological impact. Jonathan Demme's centered close-ups in "Silence of the Lambs" break the conventional off-center framing of dialogue scenes to create confronta…

**When to use.** Centered composition is powerful when the subject should confront the viewer, command ritual importance, or become the fixed axis of an ordered world. Use it for direct address, formal portraits, one-point perspective, deadpan comedy, and psychologically rigid spaces. It requires confidence because the eye notices every imbalance around the center. Avoid default centering for convenience; the fra…

**Directing the AI.** Place the subject's central axis on the exact midpoint of the frame and align the camera with the environment's vanishing point. Arrange surrounding forms to reinforce that position through symmetry, converging lines, or balanced negative space. Keep lens height level and make any asymmetry deliberate. The subject may look directly into camera for confrontation or remain still within the ordered space. For video, use locked framing or movement straight toward the center axis without lateral dri…

**Common mistakes.**
- Centering the subject while architecture and vanishing lines sit off-axis, making the composition feel carelessly misaligned.
- Using central placement in every shot, reducing a forceful choice to an unexamined visual habit with no escalation.
- Adding several equally bright side elements, which pull attention away from the exact axis the composition establishes.

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
python platform/query.py technique-motions centered-composition
```

## Sources

- Rules of Shot Composition in Film

## Related techniques

- [('symmetry', 'symmetry')](('symmetry', 'symmetry').md)
- [('head-on-shot', 'head-on-shot')](('head-on-shot', 'head-on-shot').md)
- [('leading-lines', 'leading-lines')](('leading-lines', 'leading-lines').md)
- [('rule-of-thirds', 'rule-of-thirds')](('rule-of-thirds', 'rule-of-thirds').md)
- [('framing-within-frame', 'framing-within-frame')](('framing-within-frame', 'framing-within-frame').md)
- [('negative-space', 'negative-space')](('negative-space', 'negative-space').md)
- [('shallow-focus', 'shallow-focus')](('shallow-focus', 'shallow-focus').md)
- [('deep-focus', 'deep-focus')](('deep-focus', 'deep-focus').md)
- [('mise-en-scene', 'mise-en-scene')](('mise-en-scene', 'mise-en-scene').md)
