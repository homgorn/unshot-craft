---
slug: backlight
title: "Backlight Prompt for AI Image & Video"
category: lighting
level: basic
image: "https://vvsvs.pro/img/cinematique/backlight.webp"
source_url: https://vvsvs.pro/cinematique/backlight
upstream_file: cinematique-catalog.json
upstream_sha256: 03443b1c573aec3c6b13c0ada9f219b7d52c54919ca6bd4374cbec84fd129853
styles: [spotlight-hero-card]
---

Backlit [Subject] with brilliant rim of white-gold light tracing every contour, hair transformed into a luminous halo of individually backlit strands, atmospheric dust and particles lit up like a galaxy of floating stars, god rays streaming past the figure, shot on a Cooke S4 with gentle halation on the overexposed highlights, the ethereal separation of backlight turning form into something divine

## Lede

Light positioned behind the subject, creating a rim of light around their edges that separates the subject from the background and adds a halo-like, ethereal quality. Emmanuel Lubezki is the modern master of backlighting, using natural backlight in "The Revenant" and "The Tree of Life" to create an almost divine luminosity around his subjects. Vittorio Storaro's backlighting in "The Last Emperor" gives Pu Yi a godlike glow, and Janusz Kamiński's aggressive backlighting in "Schindler's List" and "Saving Private Ryan" — sometimes called the "Kamiński look" — adds an otherworldly haze to traumatic events.

## When to use

Backlight is right when a subject must separate from a dark or visually busy background, or when the scene needs an ethereal halo. It performs especially well with hair, smoke, dust, rain, translucent fabric, and atmospheric haze. Use it for arrivals, memory fragments, spiritual imagery, or silhouettes with readable edges. Because the source faces the lens, decide whether the front remains dark or receives enough fill for expression.

## Directing the AI

Position the strongest source behind the subject and slightly above frame level. Describe a white-gold rim tracing shoulders, hair, and profile while particles in the air catch narrow beams. Let highlights bloom gently, but keep edge shape intact rather than washing the whole frame. State whether the face stays silhouetted or receives restrained frontal detail. In motion, maintain convincing occlusion: the rim should disappear on edges blocked from the source and brighten as the subject turns toward it.

## Common mistakes

- Applying an even glowing outline around every edge, including surfaces the rear source could not physically reach.
- Overexposing the background and rim together until the subject loses its silhouette instead of gaining clear separation.
- Ignoring atmosphere and surface response, which turns potentially luminous light into a thin digital-looking stroke around the figure.

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

- [silhouette](silhouette.md)
- [edge-light](edge-light.md)
- [lens-flare](lens-flare.md)
- [three-point-lighting](three-point-lighting.md)
- [key-light](key-light.md)
- [high-key-lighting](high-key-lighting.md)
- [low-key-lighting](low-key-lighting.md)
- [chiaroscuro](chiaroscuro.md)
- [rembrandt-lighting](rembrandt-lighting.md)

