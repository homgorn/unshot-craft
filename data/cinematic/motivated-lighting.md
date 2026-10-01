---
slug: motivated-lighting
title: "Motivated Lighting Prompt for AI Image & Video"
category: lighting
level: intermediate
image: "https://vvsvs.pro/img/cinematique/motivated-lighting.webp"
source_url: https://vvsvs.pro/cinematique/motivated-lighting
upstream_file: cinematique-catalog.json
upstream_sha256: 03443b1c573aec3c6b13c0ada9f219b7d52c54919ca6bd4374cbec84fd129853
styles: [icon-field-colorize]
---

Motivated lighting on [Subject] with every light source logically justified within the scene, the shadows all pointing logically away from their respective visible sources, hidden augmentation maintaining the illusion of purely natural illumination, shot on 35mm with Panavision Primo lenses, the invisible craft of making elaborate lighting look like nature, Roger Deakins-level motivational rigor

## Lede

Lighting that appears to come from a logical source within the story — a window, a fireplace, a streetlamp — even if augmented with movie lights, the effect looks naturally justified. Roger Deakins is the modern master of motivated lighting, meticulously justifying every light source in films like "Skyfall" and "1917." His work on the Coen Brothers' "No Country for Old Men" features exclusively motivated lighting — every source can be traced to a window, lamp, or headlight in the scene. Kubrick's candlelit rooms in "Barry Lyndon" and Storaro's fire-motivated interiors in "Apocalypse Now" are landmark achievements in motivated practical lighting.

## When to use

Motivated lighting belongs in any scene where cinematic control must remain invisible. Use it when windows, lamps, fires, streetlights, or headlights can justify the direction and color of every major source. It is particularly effective for realistic drama, period interiors, and location work where unexplained beauty would break the world. The method also helps maintain continuity because each lighting decision can be traced back to stable objects in the environment.

## Directing the AI

Identify every visible or implied source before describing the subject. A window should produce directional daylight and shadows that fall away from it; a lamp should create warmer, localized illumination with believable falloff. Add hidden augmentation only as an extension of those sources, never as a contradictory direction. Keep reflections, rims, and eye highlights consistent with the same logic. In video, preserve source positions across coverage and let moving characters pass through distinct pools of justified light.

## Common mistakes

- Adding a beautiful rim from the wrong direction when no window, lamp, or reflective surface can justify it.
- Giving several practical lamps equal influence across the room, ignoring distance, falloff, and obstruction between source and subject.
- Changing shadow direction between shots while visible sources remain fixed, exposing the construction behind supposedly natural illumination.

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

- [practical-lighting](practical-lighting.md)
- [available-light](available-light.md)
- [ambient-light](ambient-light.md)
- [three-point-lighting](three-point-lighting.md)
- [key-light](key-light.md)
- [high-key-lighting](high-key-lighting.md)
- [low-key-lighting](low-key-lighting.md)
- [chiaroscuro](chiaroscuro.md)
- [rembrandt-lighting](rembrandt-lighting.md)

