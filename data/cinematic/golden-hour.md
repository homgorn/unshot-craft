---
slug: golden-hour
title: "Golden Hour Prompt for AI Image & Video"
category: lighting
level: basic
image: "https://vvsvs.pro/img/cinematique/golden-hour.webp"
source_url: https://vvsvs.pro/cinematique/golden-hour
upstream_file: cinematique-catalog.json
upstream_sha256: 03443b1c573aec3c6b13c0ada9f219b7d52c54919ca6bd4374cbec84fd129853
styles: [letterspace-materialize]
---

Golden hour light thirty minutes before sunset bathing [Subject] in warm amber backlight, impossibly long shadows, lens flares streaking horizontally, the entire world turned to liquid gold and honey, shot on Kodak Vision3 50D for maximum color saturation in daylight, an 85mm lens compressing the background into a dense golden tapestry, the fleeting magic that Malick and Lubezki lived for

## Lede

The warm, soft, directional light that occurs shortly after sunrise or before sunset, casting long shadows and bathing everything in a warm amber glow that flatters skin and landscapes. Terrence Malick is the supreme poet of golden hour — "Days of Heaven," shot almost entirely in magic hour by Néstor Almendros and Haskell Wexler, remains the gold standard. Emmanuel Lubezki captured breathtaking golden hour light in "The Revenant" and "The New World" using only natural illumination. Ridley Scott's golden hour battle sequences in "Gladiator" lend warmth to violence, and Sofia Coppola bathes "The Virgin Suicides" in nostalgic golden light.

## When to use

Choose golden hour when warmth, tenderness, nostalgia, freedom, or natural grandeur should shape the scene. The low sun flatters faces, stretches shadows, and gives landscapes dimensional color. It suits romantic passages, journeys, memory, and violence made visually contradictory by beautiful light. The window is specific, so keep sun direction consistent across shots and avoid mixing it with a high midday sky.

## Directing the AI

Set the scene about thirty minutes before sunset or shortly after sunrise, with the sun low behind or beside the subject. Use warm amber backlight, long directional shadows, light haze, and restrained horizontal flare. Let an 85mm perspective compress the glowing background while preserving readable skin edges. Keep the sky and shadow side cooler for contrast. For video, maintain one sun position and let movement pass through stable shafts rather than changing time mid-shot.

## Common mistakes

- Pairing long sunset shadows with a sun placed high overhead, creating contradictory lighting geometry.
- Flooding every surface with uniform orange color, losing the cooler shadows that make warm light feel believable.
- Adding heavy lens flare across faces and focal details, turning atmospheric warmth into an optical obstruction.

## Sources

- Film Lighting

## Cross-tool

| tool | params | version | tested |
|---|---|---|---|
| mj61 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| runway_gen3 | `motion_brush: smooth_slow_pan \| aspect_ratio: 16:9 \| duration: 5 \| resolution: 1080p` | gen-3-alpha | no |
| veo2 | `resolution: 1080p \| aspect_ratio: 16:9 \| duration: 5 \| cinematic_style: true` | veo-2 | no |
| kling15 | `camera_motion: slow_pan \| resolution: 1080p \| duration: 5 \| style: cinematic` | kling-1.5 | no |
| luma | `aspect_ratio: 16_9 \| duration: 5 \| resolution: 1080p \| style: cinematic` | dream-machine | no |
| pika15 | `aspect_ratio: 16:9 \| style: cinematic \| duration: 5 \| motion: slow_pan` | pika-1.5 | no |
| sora | `style: cinematic \| resolution: 1080p \| aspect_ratio: 16:9 \| duration: 5 \| motion: slow_pan` | sora-1 | no |

## Related

- [blue-hour](blue-hour.md)
- [backlight](backlight.md)
- [lens-flare](lens-flare.md)
- [three-point-lighting](three-point-lighting.md)
- [key-light](key-light.md)
- [high-key-lighting](high-key-lighting.md)
- [low-key-lighting](low-key-lighting.md)
- [chiaroscuro](chiaroscuro.md)
- [rembrandt-lighting](rembrandt-lighting.md)

