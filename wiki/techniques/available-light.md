# "Available Light Prompt for AI Image & Video"

`available-light` · Lighting · level intermediate

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Available light on [Subject] with no additional movie lighting, illuminated purely by existing natural or practical sources, the honest imperfection of real light creating slightly uneven exposure, shot on an extremely fast lens at f/0.95 to capture the low ambient levels, the discipline of working with only what nature and architecture provide, Barry Lyndon austerity
```

Shooting with only the light naturally present in the location — no artificial movie lights added — creating an authentic, documentary quality that requires careful exposure management. Kubrick's "Barry Lyndon" is the most famous example, shot entirely by candlelight and window light using a modified NASA f/0.7 Zeiss lens. Emmanuel Lubezki committed to available light for Terrence Malick's "The New World" and "The Tree of Life," as well as Iñárritu's "The Revenant," winning three consecutive Oscars for his mastery of natural illumination. Bradford Young's available-light work in "Arrival" cre…

**When to use.** Available light is the disciplined choice when added movie lighting would disturb a location's truth, performance, or natural rhythm. Use it for documentary realism, candlelit rooms, window-lit interiors, and exterior scenes tied to a specific time of day. The look should retain slight exposure imbalance and practical limitations. This method is less about making everything visible than choosing…

**Directing the AI.** List only sources that physically exist in the location, such as a window, candle, ceiling fixture, or open sky. Place the subject where those sources can reach them and accept controlled darkness elsewhere. Ask for a fast-lens feel, gentle highlight rolloff, and small exposure imperfections rather than polished studio balance. Do not introduce invisible fill. In video, keep brightness changes tied to real movement, passing clouds, flickering flame, or shifts between practical pools of light.

**Common mistakes.**
- Sneaking in a perfect frontal fill or rim that has no existing source, undermining the available-light constraint.
- Demanding clean exposure in every corner, which removes the honest limitations and hierarchy of the location's illumination.
- Ignoring the subject's position relative to windows or practicals, then compensating with impossible light that follows them.

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
| declared | `letterspace-materialize` | opening | 15 | `letterspace-materialize` |

```
python platform/query.py technique-motions available-light
```

## Sources

- Film Lighting

## Related techniques

- [('ambient-light', 'ambient-light')](('ambient-light', 'ambient-light').md)
- [('golden-hour', 'golden-hour')](('golden-hour', 'golden-hour').md)
- [('dogme-95', 'dogme-95')](('dogme-95', 'dogme-95').md)
- [('three-point-lighting', 'three-point-lighting')](('three-point-lighting', 'three-point-lighting').md)
- [('key-light', 'key-light')](('key-light', 'key-light').md)
- [('high-key-lighting', 'high-key-lighting')](('high-key-lighting', 'high-key-lighting').md)
- [('low-key-lighting', 'low-key-lighting')](('low-key-lighting', 'low-key-lighting').md)
- [('chiaroscuro', 'chiaroscuro')](('chiaroscuro', 'chiaroscuro').md)
- [('rembrandt-lighting', 'rembrandt-lighting')](('rembrandt-lighting', 'rembrandt-lighting').md)
