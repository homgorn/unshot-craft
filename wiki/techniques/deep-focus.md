# "Deep Focus Prompt for AI Image & Video"

`deep-focus` · Composition · level intermediate

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Deep focus composition with [Subject] visible across multiple planes simultaneously, all razor-sharp from two feet to thirty feet, the viewer free to explore any layer, requiring a small aperture of f/11 and powerful invisible lighting, shot on a 21mm wide lens to maximize depth of field, the Citizen Kane democratic composition where every inch of the frame rewards examination
```

Everything in the frame — foreground, middle ground, and background — is in sharp focus simultaneously, allowing the viewer to explore the entire image and discover relationships between planes. Orson Welles and Gregg Toland made deep focus the defining visual innovation of "Citizen Kane" (1941), composing shots where action in the foreground, middle ground, and background all demanded simultaneous attention. William Wyler used deep focus in "The Best Years of Our Lives" to create some of cinema's most layered compositions. Jean Renoir's deep-focus staging in "Rules of the Game" lets multiple…

**When to use.** Deep focus belongs in scenes where multiple planes carry simultaneous story information. Use it for ensemble staging, architecture, power relationships, reveals within one shot, or moments when the audience should choose where to look. Sharp foreground and background action can create tension without cutting. The technique demands deliberate arrangement across depth; if every plane is equally det…

**Directing the AI.** Stage distinct elements in foreground, middle ground, and background, then keep all three planes acceptably sharp. Use a wider perspective, strong depth cues, and enough even illumination to preserve texture throughout the space. Give each plane a different narrative function and prevent overlapping silhouettes from merging. Maintain atmospheric perspective without turning the distance soft. For video, coordinate action across layers so attention can shift through movement and timing, not throu…

**Common mistakes.**
- Keeping everything sharp without staging meaningful relationships across depth, producing detail density instead of dramatic complexity.
- Stacking figures directly behind one another, causing silhouettes to merge even though every plane remains technically focused.
- Adding heavy background haze or blur that contradicts the requirement for readable distant action and spatial information.

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
python platform/query.py technique-motions deep-focus
```

## Sources

- Rules of Shot Composition in Film

## Related techniques

- [('depth-of-field', 'depth-of-field')](('depth-of-field', 'depth-of-field').md)
- [('foreground-interest', 'foreground-interest')](('foreground-interest', 'foreground-interest').md)
- [('mise-en-scene', 'mise-en-scene')](('mise-en-scene', 'mise-en-scene').md)
- [('rule-of-thirds', 'rule-of-thirds')](('rule-of-thirds', 'rule-of-thirds').md)
- [('symmetry', 'symmetry')](('symmetry', 'symmetry').md)
- [('leading-lines', 'leading-lines')](('leading-lines', 'leading-lines').md)
- [('framing-within-frame', 'framing-within-frame')](('framing-within-frame', 'framing-within-frame').md)
- [('negative-space', 'negative-space')](('negative-space', 'negative-space').md)
- [('shallow-focus', 'shallow-focus')](('shallow-focus', 'shallow-focus').md)
