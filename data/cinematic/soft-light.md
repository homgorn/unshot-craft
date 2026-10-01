---
slug: soft-light
title: "Soft Light Prompt for AI Image & Video"
category: lighting
level: basic
image: "https://vvsvs.pro/img/cinematique/soft-light.webp"
source_url: https://vvsvs.pro/cinematique/soft-light
upstream_file: cinematique-catalog.json
upstream_sha256: 03443b1c573aec3c6b13c0ada9f219b7d52c54919ca6bd4374cbec84fd129853
styles: [spotlight-hero-card]
---

Soft diffused light wrapping around [Subject] with barely perceptible shadow transitions, a massive window or diffusion source bending light gently around face and shoulders, skin rendered with luminous porcelain quality, shot on Cooke S7 lenses known for gentle rendering and subtle halation on highlights, Fujifilm Eterna color science with delicate pastel tonality, the Vermeer-like quality of undirected daylight

## Lede

Diffused light from a large source that wraps around the subject, creating gentle shadow transitions that are flattering for skin and create a dreamy or intimate quality. Sven Nykvist, Ingmar Bergman's cinematographer, was legendary for his soft, natural light in films like "Cries and Whispers" and "Fanny and Alexander," often bouncing light off white walls and ceilings. Emmanuel Lubezki creates ethereal soft light in Terrence Malick's "The Tree of Life" using large diffusion frames and natural overcast skies. Robert Richardson's soft light work in "The Aviator" recreated the luminous quality of Golden Age Hollywood glamour photography.

## When to use

Choose soft light when faces and materials need gentle modeling, intimacy, romance, or natural overcast calm. A large source wraps around features and creates gradual shadow transitions that are flattering without removing all shape. It suits close portraits, domestic scenes, beauty, and reflective drama. Soft does not mean flat: retain direction and controlled contrast so the subject remains dimensional and the source feels located.

## Directing the AI

Describe a very large window, bounced source, or diffusion frame close to the subject, placed slightly to one side. Ask for light that wraps around cheeks and shoulders with broad highlights and barely perceptible shadow edges. Keep skin luminous, pastel color delicate, and highlight halation subtle. Use negative fill on the far side if more shape is needed. Avoid hard rim lines and tiny catchlights that would contradict the broad source's apparent size.

## Common mistakes

- Filling both sides equally until the face loses direction, volume, and any sense of a located source.
- Adding crisp nose or jaw shadows that contradict the requested broad diffusion and gentle transitions.
- Smoothing texture into plastic skin, mistaking soft illumination for aggressive cosmetic post-processing.

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

- [hard-light](hard-light.md)
- [bounce-light](bounce-light.md)
- [high-key-lighting](high-key-lighting.md)
- [three-point-lighting](three-point-lighting.md)
- [key-light](key-light.md)
- [low-key-lighting](low-key-lighting.md)
- [chiaroscuro](chiaroscuro.md)
- [rembrandt-lighting](rembrandt-lighting.md)
- [silhouette](silhouette.md)

