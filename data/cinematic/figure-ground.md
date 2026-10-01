---
slug: figure-ground
title: "Figure-Ground Relationship Prompt for AI Image & Video"
category: composition
level: intermediate
image: "https://vvsvs.pro/img/cinematique/figure-ground.webp"
source_url: https://vvsvs.pro/cinematique/figure-ground
upstream_file: cinematique-catalog.json
upstream_sha256: 03443b1c573aec3c6b13c0ada9f219b7d52c54919ca6bd4374cbec84fd129853
styles: [brand-ink-open]
---

Strong figure-ground relationship with [Subject] separated from the background by extreme tonal and color contrast creating instant three-dimensional pop, the form isolated as cleanly as a paper cutout, shot on medium format with a 110mm lens at f/2.8 creating slight background softening that adds optical separation to the tonal separation, the fundamental perceptual principle that makes cinema readable

## Lede

The perceptual relationship between a subject (figure) and its background (ground) — strong figure-ground separation makes subjects pop, while ambiguous relationships create artistic tension. Film noir deliberately plays with figure-ground by merging characters into shadows, while Spielberg ensures crisp separation for visual clarity. Kubrick uses monochromatic figure-ground merging in "Full Metal Jacket" to show soldiers losing individuality. Roger Deakins creates separation through subtle lighting rather than color contrast, and cinematographer James Laxton uses luminous skin against dark backgrounds in "Moonlight" and "If Beale Street Could Talk" to celebrate Black skin tones.

## When to use

Figure-ground control matters whenever the subject risks disappearing into the background or should deliberately merge with it. Strong separation supports clarity, icon-like presence, and fast visual reading; ambiguity can create camouflage, loss of identity, or suspense. Use tonal, color, focus, edge, and lighting differences to decide the relationship. The goal is not always maximum pop. Choose whether the audience should find the figure instantly or work to locate it.

## Directing the AI

Define the figure and ground as separate tonal and color fields, then decide the strength of their boundary. For clean separation, use contrasting value, a restrained edge light, or slight background softening. For ambiguity, match selected contours and tones while preserving one clue that reveals the subject. Avoid accidental tangencies where edges merge unpredictably. In video, keep separation logic coherent as the figure moves across changing backgrounds, or let the merge happen at a planned narrative moment.

## Common mistakes

- Matching subject and background values by accident, causing important faces or gestures to disappear without narrative purpose.
- Outlining the entire figure with artificial brightness, producing separation that ignores the scene's actual light direction.
- Using maximum contrast on every edge, making the subject look pasted onto the environment rather than embedded within it.

## Sources

- Rules of Shot Composition in Film

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
- [contrast-composition](contrast-composition.md)
- [rule-of-thirds](rule-of-thirds.md)
- [symmetry](symmetry.md)
- [leading-lines](leading-lines.md)
- [framing-within-frame](framing-within-frame.md)
- [negative-space](negative-space.md)
- [shallow-focus](shallow-focus.md)

