# "Contrast Prompt for AI Image & Video"

`contrast-composition` · Composition · level basic

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
High contrast composition with [Subject] as a tiny warm-colored element against a vast cool-toned environment, every type of visual contrast at work simultaneously — warm against cool, small organic shape against massive geometry, soft texture against hard surface, movement against stillness, shot on large format 65mm with a 100mm telephoto compressing the background, Kodak Vision3 50D saturated daylight stock
```

Using opposing visual elements — light vs dark, large vs small, warm vs cool, sharp vs soft — to create visual interest, hierarchy, and dramatic tension within the frame. Akira Kurosawa was perhaps cinema's greatest practitioner of compositional contrast, pitting tiny samurai against massive rainstorms in "Seven Samurai" and fragile humans against erupting volcanoes of color in "Ran." David Lean used scale contrast — small figures against enormous landscapes — as his signature in "Lawrence of Arabia" and "Doctor Zhivago." Christopher Nolan employs contrast between warm intimate interiors and…

**When to use.** Contrast is useful when a frame needs immediate hierarchy or when two forces should feel emotionally opposed. Pair warm with cool, small with large, soft with hard, organic with geometric, or motion with stillness. It can clarify the subject or turn the entire composition into conflict. Choose one primary opposition and support it with others carefully. If every property fights at once, the image…

**Directing the AI.** Select the dominant contrast first, such as a small warm figure against a vast cool structure. Reinforce it through scale, texture, and stillness only where those differences support the same idea. Keep the subject readable and prevent secondary colors or objects from creating rival conflicts. Describe both sides of the opposition concretely. For video, let the contrast persist through movement and cutting, or reveal one side after the other so the collision lands with intention.

**Common mistakes.**
- Stacking unrelated oppositions across color, scale, texture, and motion until the frame loses one dominant visual argument.
- Using strong tonal contrast without controlling the brightest area, allowing a background highlight to steal the subject's hierarchy.
- Choosing opposing colors as decoration while size, lighting, and staging communicate no actual tension between the elements.

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
| declared | `fracture` | opening | 156 | `fracture` |

```
python platform/query.py technique-motions contrast-composition
```

## Sources

- Rules of Shot Composition in Film

## Related techniques

- [('color-temperature', 'color-temperature')](('color-temperature', 'color-temperature').md)
- [('visual-weight', 'visual-weight')](('visual-weight', 'visual-weight').md)
- [('chiaroscuro', 'chiaroscuro')](('chiaroscuro', 'chiaroscuro').md)
- [('rule-of-thirds', 'rule-of-thirds')](('rule-of-thirds', 'rule-of-thirds').md)
- [('symmetry', 'symmetry')](('symmetry', 'symmetry').md)
- [('leading-lines', 'leading-lines')](('leading-lines', 'leading-lines').md)
- [('framing-within-frame', 'framing-within-frame')](('framing-within-frame', 'framing-within-frame').md)
- [('negative-space', 'negative-space')](('negative-space', 'negative-space').md)
- [('shallow-focus', 'shallow-focus')](('shallow-focus', 'shallow-focus').md)
