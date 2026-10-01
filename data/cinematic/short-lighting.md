---
slug: short-lighting
title: "Short Lighting Prompt for AI Image & Video"
category: lighting
level: intermediate
image: "https://vvsvs.pro/img/cinematique/short-lighting.webp"
source_url: https://vvsvs.pro/cinematique/short-lighting
upstream_file: cinematique-catalog.json
upstream_sha256: 03443b1c573aec3c6b13c0ada9f219b7d52c54919ca6bd4374cbec84fd129853
styles: [spotlight-hero-card]
---

Short lighting on [Subject] with the key hitting the narrow far side, putting the broader camera-facing side in shadow, the small bright area creating an accent surrounded by darkness, shot on a fast 85mm lens at T1.4 with the background falling to black, film noir portrait psychology where what is hidden matters more than what is shown

## Lede

The side of the face turned away from the camera receives the key light, putting the broader visible area in shadow, creating a slimming, more dramatic and moody portrait. Short lighting is preferred for dramatic and thriller genres where mystery and tension serve the story. Gordon Willis frequently used short lighting patterns in his collaborations with Woody Allen and Francis Ford Coppola. Film noir cinematographers defaulted to short lighting to create the shadowy, secretive faces of morally ambiguous characters. Roger Deakins uses short lighting in "Prisoners" to maintain a persistent sense of concealment and dread.

## When to use

Short lighting fits portraits that need mystery, tension, a slimmer face shape, or a sense that the character is withholding information. It works naturally in thrillers, noir, interrogations, and dramatic dialogue. The small far-side highlight becomes an accent surrounded by a larger field of shadow. Use it when concealment carries meaning, but protect enough eye and skin detail to keep the emotion intentional rather than simply underexposed.

## Directing the AI

Angle the subject away from camera and place the key on the narrow face plane turned farther from the lens. Keep the broad camera-facing cheek in shadow, with the bright far cheek acting as a controlled accent. Use minimal fill and let the background fall darker if the scene supports it. Preserve a catchlight or slight eye detail where needed. During movement, make the light pattern respond to head rotation instead of remaining frozen across the same facial regions.

## Common mistakes

- Illuminating the broad near cheek, which reverses the intended pattern and removes the slimming field of shadow.
- Crushing the entire camera-facing side to featureless black, losing the controlled detail that keeps the portrait readable.
- Letting the narrow highlight spread across the nose and front plane, weakening the concentrated dramatic accent.

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

- [side-lighting](side-lighting.md)
- [low-key-lighting](low-key-lighting.md)
- [rembrandt-lighting](rembrandt-lighting.md)
- [three-point-lighting](three-point-lighting.md)
- [key-light](key-light.md)
- [high-key-lighting](high-key-lighting.md)
- [chiaroscuro](chiaroscuro.md)
- [silhouette](silhouette.md)
- [golden-hour](golden-hour.md)

