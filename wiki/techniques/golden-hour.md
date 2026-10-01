# "Golden Hour Prompt for AI Image & Video"

`golden-hour` · Lighting · level basic

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Golden hour light thirty minutes before sunset bathing [Subject] in warm amber backlight, impossibly long shadows, lens flares streaking horizontally, the entire world turned to liquid gold and honey, shot on Kodak Vision3 50D for maximum color saturation in daylight, an 85mm lens compressing the background into a dense golden tapestry, the fleeting magic that Malick and Lubezki lived for
```

The warm, soft, directional light that occurs shortly after sunrise or before sunset, casting long shadows and bathing everything in a warm amber glow that flatters skin and landscapes. Terrence Malick is the supreme poet of golden hour — "Days of Heaven," shot almost entirely in magic hour by Néstor Almendros and Haskell Wexler, remains the gold standard. Emmanuel Lubezki captured breathtaking golden hour light in "The Revenant" and "The New World" using only natural illumination. Ridley Scott's golden hour battle sequences in "Gladiator" lend warmth to violence, and Sofia Coppola bathes "Th…

**When to use.** Choose golden hour when warmth, tenderness, nostalgia, freedom, or natural grandeur should shape the scene. The low sun flatters faces, stretches shadows, and gives landscapes dimensional color. It suits romantic passages, journeys, memory, and violence made visually contradictory by beautiful light. The window is specific, so keep sun direction consistent across shots and avoid mixing it with a…

**Directing the AI.** Set the scene about thirty minutes before sunset or shortly after sunrise, with the sun low behind or beside the subject. Use warm amber backlight, long directional shadows, light haze, and restrained horizontal flare. Let an 85mm perspective compress the glowing background while preserving readable skin edges. Keep the sky and shadow side cooler for contrast. For video, maintain one sun position and let movement pass through stable shafts rather than changing time mid-shot.

**Common mistakes.**
- Pairing long sunset shadows with a sun placed high overhead, creating contradictory lighting geometry.
- Flooding every surface with uniform orange color, losing the cooler shadows that make warm light feel believable.
- Adding heavy lens flare across faces and focal details, turning atmospheric warmth into an optical obstruction.

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
python platform/query.py technique-motions golden-hour
```

## Sources

- Film Lighting

## Related techniques

- [('blue-hour', 'blue-hour')](('blue-hour', 'blue-hour').md)
- [('backlight', 'backlight')](('backlight', 'backlight').md)
- [('lens-flare', 'lens-flare')](('lens-flare', 'lens-flare').md)
- [('three-point-lighting', 'three-point-lighting')](('three-point-lighting', 'three-point-lighting').md)
- [('key-light', 'key-light')](('key-light', 'key-light').md)
- [('high-key-lighting', 'high-key-lighting')](('high-key-lighting', 'high-key-lighting').md)
- [('low-key-lighting', 'low-key-lighting')](('low-key-lighting', 'low-key-lighting').md)
- [('chiaroscuro', 'chiaroscuro')](('chiaroscuro', 'chiaroscuro').md)
- [('rembrandt-lighting', 'rembrandt-lighting')](('rembrandt-lighting', 'rembrandt-lighting').md)
