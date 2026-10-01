# "Cross Lighting Prompt for AI Image & Video"

`cross-lighting` · Lighting · level intermediate

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Cross-lighting from two opposing sources on [Subject], a warm tungsten source from one side casting amber highlights while a cool blue-white source from the other paints steel tones, the two competing colors meeting in a narrow strip of mixed light, each surface independently sculpted by the dual sources, shot on 35mm Kodak Vision3 500T to handle the mixed color temperatures with richness, a 50mm lens capturing the sculptural dimensionality
```

Two light sources positioned on opposite sides of the subject, creating a complex interplay of highlights and shadows that sculpt form from multiple directions. Ridley Scott used cross-lighting extensively in "Blade Runner" to create the layered, multi-source atmosphere of a neon-drenched dystopia. Michael Mann employs cross-lighting in his nighttime cityscapes, with competing sources from streetlights, car headlights, and building illumination. The technique is also central to fashion and music video cinematography, where Bradford Young and Linus Sandgren create rich, multi-dimensional looks…

**When to use.** Choose cross lighting when one source cannot explain the layered energy of a night exterior, stage, fashion frame, or neon interior. Opposing sources can carve different surfaces and separate a subject from several directions at once. The technique is especially useful when warm and cool environments collide. It demands control: each source needs a believable origin, and their overlap should crea…

**Directing the AI.** Place two sources on opposite sides of the subject. Give one a warm amber character and the other a cooler blue-white tone, then specify which planes each source catches. Keep a narrow transition where the colors meet rather than blending everything into uniform purple. Let the sources cast shadows away from their own directions, with neither behaving like frontal fill. In video, lock both lights to motivated positions and track how their influence changes as the subject crosses between them.

**Common mistakes.**
- Blending the opposing colors across the entire subject, producing a muddy wash instead of two clearly directed sources.
- Giving both lights equal frontal coverage, which flattens form and defeats the sculptural purpose of cross lighting.
- Ignoring separate shadow directions, making the warm and cool highlights feel decorative rather than physically present in the space.

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
| declared | `spotlight-hero-card` | opening | 220 | `spotlight-hero-card` |

```
python platform/query.py technique-motions cross-lighting
```

## Sources

- Film Lighting

## Related techniques

- [('color-temperature', 'color-temperature')](('color-temperature', 'color-temperature').md)
- [('side-lighting', 'side-lighting')](('side-lighting', 'side-lighting').md)
- [('practical-lighting', 'practical-lighting')](('practical-lighting', 'practical-lighting').md)
- [('three-point-lighting', 'three-point-lighting')](('three-point-lighting', 'three-point-lighting').md)
- [('key-light', 'key-light')](('key-light', 'key-light').md)
- [('high-key-lighting', 'high-key-lighting')](('high-key-lighting', 'high-key-lighting').md)
- [('low-key-lighting', 'low-key-lighting')](('low-key-lighting', 'low-key-lighting').md)
- [('chiaroscuro', 'chiaroscuro')](('chiaroscuro', 'chiaroscuro').md)
- [('rembrandt-lighting', 'rembrandt-lighting')](('rembrandt-lighting', 'rembrandt-lighting').md)
