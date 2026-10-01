---
slug: gobo-lighting
title: "Gobo Lighting Prompt for AI Image & Video"
category: lighting
level: advanced
image: "https://vvsvs.pro/img/cinematique/gobo-lighting.webp"
source_url: https://vvsvs.pro/cinematique/gobo-lighting
upstream_file: cinematique-catalog.json
upstream_sha256: 03443b1c573aec3c6b13c0ada9f219b7d52c54919ca6bd4374cbec84fd129853
styles: [icon-field-colorize]
---

Gobo lighting casting patterned shadows across [Subject], horizontal bars of light and dark striping across the form at an angle, the shadow pattern breaking and wrapping as it crosses three-dimensional contours, projected by a single hard source through a template, Kodak Double-X black and white stock for maximum contrast between the light bars and shadow bars, the quintessential film noir visual texture

## Lede

Light shaped by a template (gobo) placed in front of the source, casting patterned shadows — window frames, venetian blinds, branches — adding narrative texture without physical set pieces. Film noir cinematography relied heavily on gobo lighting; John Alton's venetian blind shadows in "The Big Combo" became the genre's visual shorthand. Dean Cundey used gobo patterns in John Carpenter's "Halloween" to cast ominous branch shadows across interiors. Roger Deakins uses subtle gobo patterns in "Skyfall" to create the impression of light filtering through unseen architectural elements, adding visual complexity without visible source.

## When to use

Gobo lighting is useful when a plain wall or simple set needs narrative texture without adding physical construction. Projected blinds can suggest confinement or secrecy; branches can make an interior feel exposed to the world outside. The technique belongs in noir, suspense, horror, and stylized drama. Use one recognizable template and a motivated hard source. The pattern should clarify the scene's emotional geometry, not fill empty space with arbitrary stripes.

## Directing the AI

Place a shaped template between one hard source and the subject. Define the pattern precisely, such as angled horizontal bars or broken branch shadows, and state where it lands. Let the projection wrap, widen, and break across face, clothing, furniture, and wall according to their depth. Keep light bars and shadow bars clearly separated. In video, hold the template spatially stable unless a believable blind, branch, source, or camera movement causes the pattern to shift.

## Common mistakes

- Overlaying a flat pattern across every surface at identical scale, ignoring distance and three-dimensional projection behavior.
- Using several unrelated templates together, turning focused narrative texture into visual noise with no readable source.
- Softening the source until the projected bars or branches lose definition and no longer function as shaped light.

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
- [film-noir](film-noir.md)
- [chiaroscuro](chiaroscuro.md)
- [three-point-lighting](three-point-lighting.md)
- [key-light](key-light.md)
- [high-key-lighting](high-key-lighting.md)
- [low-key-lighting](low-key-lighting.md)
- [rembrandt-lighting](rembrandt-lighting.md)
- [silhouette](silhouette.md)

