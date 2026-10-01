---
slug: dappled-light
title: "Dappled Light Prompt for AI Image & Video"
category: lighting
level: intermediate
image: "https://vvsvs.pro/img/cinematique/dappled-light.webp"
source_url: https://vvsvs.pro/cinematique/dappled-light
upstream_file: cinematique-catalog.json
upstream_sha256: 03443b1c573aec3c6b13c0ada9f219b7d52c54919ca6bd4374cbec84fd129853
styles: [icon-field-colorize]
---

Dappled light filtering through a canopy onto [Subject], dozens of small bright spots and larger soft patches scattered across them in an ever-shifting mosaic, the interplay creating a natural pointillist painting on the surface, the overall light warm and green-shifted from passing through foliage, an 85mm lens at T1.4 turning the background into luminous green bokeh, Kodak Vision3 50D saturated daylight stock, the Malick-Lubezki prayer of natural light

## Lede

Light filtered through trees, blinds, or other semi-transparent objects, creating a pattern of light and shadow across the subject that evokes natural environments and contemplation. Terrence Malick and Emmanuel Lubezki use dappled forest light as an almost religious motif throughout "The New World" and "The Tree of Life," where sunlight through leaves becomes a visual metaphor for divine presence. Akira Kurosawa used dappled light filtering through the forest canopy in "Rashomon" to create the famous unreliable visual atmosphere. Guillermo del Toro employs dappled light in "Pan's Labyrinth" to mark the boundary between the real and fantastical worlds.

## When to use

Dappled light works when the environment should leave a living pattern on the subject. Use it beneath foliage, near blinds, behind patterned screens, or anywhere a broken source can suggest contemplation, romance, instability, or a border between worlds. The shifting mosaic adds texture without extra objects in the frame. It is strongest when the filter has a clear physical presence and the pattern wraps convincingly across faces, clothing, walls, and ground.

## Directing the AI

Place a hard or moderately focused source behind a specific filter, such as leaves or blinds. Ask for irregular bright patches and softer shadow areas that change size as they cross three-dimensional surfaces. If foliage is the filter, let the light carry a slight warm and green character. Keep the overall exposure coherent beneath the pattern. For video, animate the patches subtly with wind or subject movement; avoid making every spot pulse independently or slide across stationary architecture.

## Common mistakes

- Painting identical circular spots over the whole frame, which ignores the shape, distance, and depth of the filtering material.
- Keeping the projected pattern flat across curved faces and fabric, rather than letting it wrap and distort with form.
- Moving shadows rapidly without moving leaves, blinds, light, or subject, making the scene's illumination physically incoherent.

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

- [gobo-lighting](gobo-lighting.md)
- [golden-hour](golden-hour.md)
- [hard-light](hard-light.md)
- [three-point-lighting](three-point-lighting.md)
- [key-light](key-light.md)
- [high-key-lighting](high-key-lighting.md)
- [low-key-lighting](low-key-lighting.md)
- [chiaroscuro](chiaroscuro.md)
- [rembrandt-lighting](rembrandt-lighting.md)

