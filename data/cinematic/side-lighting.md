---
slug: side-lighting
title: "Side Lighting Prompt for AI Image & Video"
category: lighting
level: intermediate
image: "https://vvsvs.pro/img/cinematique/side-lighting.webp"
source_url: https://vvsvs.pro/cinematique/side-lighting
upstream_file: cinematique-catalog.json
upstream_sha256: 03443b1c573aec3c6b13c0ada9f219b7d52c54919ca6bd4374cbec84fd129853
styles: [spotlight-hero-card]
---

Side lighting from a single source striking [Subject] at exactly 90 degrees, one half brilliantly illuminated while the other half vanishes into complete shadow creating a perfect vertical division, every texture on the lit side rendered in crystalline detail while the shadow side reveals nothing, shot on large format with an 80mm lens, the extreme dimensionality of single-source side light, the duality made visible

## Lede

Light striking the subject from a 90-degree angle, illuminating one half while leaving the other in shadow, splitting the face or figure to create strong dimensionality and visual tension. Vittorio Storaro used dramatic side lighting throughout "Apocalypse Now" to bisect characters between light and darkness, mirroring the moral duality at the film's core. Roger Deakins employs precise side lighting in "Prisoners" and "Sicario" to create sculptural depth. The technique is central to Conrad Hall's Oscar-winning cinematography in "American Beauty," where side light from venetian blinds creates the film's signature visual motif.

## When to use

Use side lighting when a face or figure needs strong dimensionality, moral tension, or a visible split between competing states. It suits confrontations, secretive portraits, and moments when one side of a character should remain unreadable. The technique also gives textured subjects more relief because light travels across the surface rather than flattening it. Avoid it when the scene needs openness, softness, or evenly legible expressions.

## Directing the AI

Place one dominant source exactly 90 degrees to the subject. Keep the camera-facing division clear: one half receives crisp illumination while the opposite half falls into deep shadow. Describe which facial plane, object edge, or body contour catches the light, and protect detail on that side. Hold fill to a minimum so the split remains graphic. For video, keep the source and subject positions consistent as they move, or let the division shift deliberately across the face.

## Common mistakes

- Adding frontal fill until both sides become equally readable, which removes the tension and sculptural split the setup needs.
- Placing the source too far forward, turning the result into ordinary three-quarter portrait lighting instead of true side light.
- Leaving the lit side featureless or clipped, so the frame loses the texture that should carry its dimensional detail.

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

- [low-key-lighting](low-key-lighting.md)
- [chiaroscuro](chiaroscuro.md)
- [short-lighting](short-lighting.md)
- [three-point-lighting](three-point-lighting.md)
- [key-light](key-light.md)
- [high-key-lighting](high-key-lighting.md)
- [rembrandt-lighting](rembrandt-lighting.md)
- [silhouette](silhouette.md)
- [golden-hour](golden-hour.md)

