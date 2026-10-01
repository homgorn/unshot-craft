---
slug: kicker-light
title: "Kicker Light Prompt for AI Image & Video"
category: lighting
level: intermediate
image: "https://vvsvs.pro/img/cinematique/kicker-light.webp"
source_url: https://vvsvs.pro/cinematique/kicker-light
upstream_file: cinematique-catalog.json
upstream_sha256: 03443b1c573aec3c6b13c0ada9f219b7d52c54919ca6bd4374cbec84fd129853
styles: [spotlight-hero-card]
---

Kicker light accent on [Subject], a focused beam from behind and to the side catching just the edge of a cheekbone, the rim of an ear, and the curve of a shoulder in a thin bright line against darkness, the subtlety of the kicker creating depth and three-dimensionality, shot with a 135mm telephoto at T2, warm 3000K color temperature suggesting a tungsten practical source

## Lede

A light placed behind and to the side of a subject, adding an accent edge of light that is more targeted than a backlight, providing a touch of separation and dimensionality. The kicker light is a staple of professional cinematography that often goes unnoticed by audiences despite being visible in nearly every well-lit film. Darius Khondji uses precise kicker lights in David Fincher's "Se7en" to trace characters against dark backgrounds without revealing the full backlight. Robert Elswit employs subtle kickers in Paul Thomas Anderson's "There Will Be Blood" to add depth to candlelit and oil-lamp scenes where full backlighting would be unmotivated.

## When to use

Reach for a kicker light when the subject almost separates from the background but a full backlight would feel excessive or unmotivated. A narrow accent can define one cheekbone, ear, shoulder, or costume edge while preserving a dark overall image. It works in restrained portraits, candlelit rooms, thrillers, and night scenes. The kicker should be noticed through improved depth, not through a broad halo that announces the lighting setup.

## Directing the AI

Set a focused source behind and to one side of the subject, aimed across rather than directly toward the camera. Limit its reach to a thin accent on the near cheekbone, ear rim, hair edge, or shoulder curve. Match its color to a plausible lamp, fire, or practical source in the scene. Keep the face's front exposure unchanged. During movement, let the accent appear and disappear naturally as contours rotate through the beam instead of sticking to the same screen-space edge.

## Common mistakes

- Expanding the accent around the whole silhouette, which turns a targeted kicker into an indiscriminate backlight.
- Brightening the kicker beyond the scene's practical sources, making the edge feel detached from the surrounding exposure.
- Keeping the accent fixed on one screen edge while the subject turns, breaking the physical direction of the light.

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

- [edge-light](edge-light.md)
- [backlight](backlight.md)
- [three-point-lighting](three-point-lighting.md)
- [key-light](key-light.md)
- [high-key-lighting](high-key-lighting.md)
- [low-key-lighting](low-key-lighting.md)
- [chiaroscuro](chiaroscuro.md)
- [rembrandt-lighting](rembrandt-lighting.md)
- [silhouette](silhouette.md)

