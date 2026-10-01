# "Mise-en-Scène Prompt for AI Image & Video"

`mise-en-scene` · Composition · level advanced

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Meticulously arranged mise-en-scene with [Subject] positioned within an environment where every element tells a story, every prop researched and placed with production designer precision, the apparent normalcy concealing visible fault lines, shot on 35mm with a 32mm lens to capture the full space as a narrative environment, the Sirkian melodrama of a world where set design is psychology
```

The total arrangement of everything visible in the frame — set design, props, costumes, lighting, actor positioning — where every element is a deliberate storytelling choice. The concept originates from French theater and was elevated to an art form by directors like Max Ophüls in "The Earrings of Madame de..." and Jean Renoir in "The Rules of the Game." Kubrick's obsessive mise-en-scène in "2001" and "Eyes Wide Shut" treats every prop and color as narrative text. Wes Anderson's mise-en-scène is so controlled it becomes the primary vehicle of storytelling, while Bong Joon-ho's "Parasite" uses…

**When to use.** Mise-en-scène is the right lens when the entire visible world must communicate character, class, history, or conflict before anyone speaks. Use it for controlled interiors, symbolic environments, ensemble blocking, and frames where props or architecture carry plot. It is especially valuable when building a repeatable visual world across scenes. Every object needs a reason to exist, but the arrang…

**Directing the AI.** Define the environment, period cues, palette, costume, props, lighting logic, and actor positions as one connected system. Assign each major object a relationship to the subject or story, then remove anything that does not support that relationship. Use depth and blocking to expose status or tension. Keep wear, spacing, and material detail consistent with the setting. For video, preserve object locations and costume continuity while allowing performers to interact naturally with the designed sp…

**Common mistakes.**
- Listing attractive props without connecting them to character, conflict, or setting, creating decoration instead of visual storytelling.
- Overloading every surface with symbolic objects, leaving the audience no hierarchy and the performers no believable living space.
- Changing furniture, costume details, or practical-light positions across shots, breaking the coherence of the designed world.

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
| declared | `space-camera-moves` | camera | 150 | `drone-dive-landing` |
| declared | `space-camera-moves` | camera | 150 | `exploded-view` |

```
python platform/query.py technique-motions mise-en-scene
```

## Sources

- Rules of Shot Composition in Film

## Related techniques

- [('foreground-interest', 'foreground-interest')](('foreground-interest', 'foreground-interest').md)
- [('color-temperature', 'color-temperature')](('color-temperature', 'color-temperature').md)
- [('motif', 'motif')](('motif', 'motif').md)
- [('rule-of-thirds', 'rule-of-thirds')](('rule-of-thirds', 'rule-of-thirds').md)
- [('symmetry', 'symmetry')](('symmetry', 'symmetry').md)
- [('leading-lines', 'leading-lines')](('leading-lines', 'leading-lines').md)
- [('framing-within-frame', 'framing-within-frame')](('framing-within-frame', 'framing-within-frame').md)
- [('negative-space', 'negative-space')](('negative-space', 'negative-space').md)
- [('shallow-focus', 'shallow-focus')](('shallow-focus', 'shallow-focus').md)
