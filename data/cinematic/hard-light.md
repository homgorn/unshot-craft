---
slug: hard-light
title: "Hard Light Prompt for AI Image & Video"
category: lighting
level: basic
image: "https://vvsvs.pro/img/cinematique/hard-light.webp"
source_url: https://vvsvs.pro/cinematique/hard-light
upstream_file: cinematique-catalog.json
upstream_sha256: 03443b1c573aec3c6b13c0ada9f219b7d52c54919ca6bd4374cbec84fd129853
styles: [fracture]
---

Hard light from a bare overhead source casting razor-sharp shadows on [Subject], defined shadow edges so crisp they look cut with a knife, every surface texture amplified by the raking illumination, shot on Kodak Double-X black and white stock for maximum contrast, a 35mm Zeiss Planar lens, the graphic severity of film noir where light itself becomes an instrument of pressure

## Lede

Light from a small or distant source that creates sharp, well-defined shadows, adding texture, drama, and graphic quality that can be harsh and unflattering or strikingly bold. Film noir cinematographers like John Alton and Nicholas Musuraca built entire visual worlds from hard light, creating the razor-sharp shadows of venetian blinds and fedora brims. David Fincher and Darius Khondji used hard light sources in "Se7en" to create the grimy, punishing atmosphere of a city drowning in sin. The direct sunlight in Sergio Leone's Westerns functions as nature's hard light, carving faces into dramatic relief.

## When to use

Use hard light when sharp shadows and exposed texture should create pressure, heat, severity, or graphic style. A small source can carve faces, project window patterns, define dust, or make architecture feel unforgiving. It suits noir, Westerns, interrogation, and harsh daylight. Because it reveals every surface irregularity, choose it deliberately for skin and products rather than assuming stronger contrast always looks more cinematic.

## Directing the AI

Place a small bare or distant source at a defined angle and demand crisp, clearly shaped shadow edges. Let raking light reveal pores, fabric, dust, walls, and metal while keeping the contrast strong. A monochrome or restrained palette can make the geometry more forceful. Name any projected shape, such as blinds, and align it with the source. Avoid broad diffusion, ambient fill, or several competing directions that would soften the graphic result.

## Common mistakes

- Adding large diffusion to the source, softening the edges until the defining hard-shadow quality disappears.
- Using several hard lights from unrelated angles, producing crossed shadows that make the scene visually incoherent.
- Ignoring how raking light reveals skin and surface flaws, creating harsh detail where the subject needed restraint.

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

- [soft-light](soft-light.md)
- [low-key-lighting](low-key-lighting.md)
- [gobo-lighting](gobo-lighting.md)
- [three-point-lighting](three-point-lighting.md)
- [key-light](key-light.md)
- [high-key-lighting](high-key-lighting.md)
- [chiaroscuro](chiaroscuro.md)
- [rembrandt-lighting](rembrandt-lighting.md)
- [silhouette](silhouette.md)

