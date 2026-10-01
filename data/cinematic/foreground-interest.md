---
slug: foreground-interest
title: "Foreground Interest Prompt for AI Image & Video"
category: composition
level: intermediate
image: "https://vvsvs.pro/img/cinematique/foreground-interest.webp"
source_url: https://vvsvs.pro/cinematique/foreground-interest
upstream_file: cinematique-catalog.json
upstream_sha256: 03443b1c573aec3c6b13c0ada9f219b7d52c54919ca6bd4374cbec84fd129853
styles: [depth-layer-moves]
---

Foreground interest composition with [Subject] in the mid-ground and blurred elements dominating the immediate foreground, three distinct depth planes creating immersive physical space, the foreground elements partially obscuring the subject adding voyeuristic tension, shot on a 40mm lens at T2 creating visible focus separation between planes, Kodak 5219 500T with desaturated earth tones, the Spielberg technique of putting the viewer inside the world

## Lede

Placing objects or elements in the immediate foreground to add depth and dimension, creating a layered image that draws the viewer through multiple planes of the composition. Steven Spielberg consistently uses foreground objects — a glass of water in "Jurassic Park," toys in "E.T." — to add depth and narrative context. Roger Deakins layers his compositions with foreground elements in "Skyfall" and "Blade Runner 2049" to create immersive three-dimensionality. Emmanuel Lubezki places branches, grass, and natural elements in the immediate foreground of nearly every exterior shot in Malick's films to create the feeling of being inside the environment rather than observing it.

## When to use

Foreground interest helps when a scene feels flat, observed from outside, or short on spatial tension. Use nearby branches, glass, furniture, props, architecture, or partial figures to place the viewer inside the environment. It can add context, concealment, scale, or a voyeuristic edge while guiding attention toward mid-ground action. The foreground object should belong to the location and support the scene; random blur at the frame edge is not enough.

## Directing the AI

Place a large object very close to the camera, partially entering the frame, with the main subject in the middle ground and a readable background beyond. Decide whether the foreground stays soft, sharp, reflective, or silhouetted based on its role. Use overlap to establish depth without covering the subject's essential action. For video, let parallax separate the planes during camera movement; nearby elements should travel faster across frame than distant ones.

## Common mistakes

- Adding anonymous blurred blobs at the corners, with no recognizable connection to the location or the scene's meaning.
- Covering the subject's face or action with foreground objects that create obstruction without tension, context, or reveal.
- Moving all depth planes at the same screen speed, eliminating the parallax that makes foreground layering physically convincing.

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

- [framing-within-frame](framing-within-frame.md)
- [depth-of-field](depth-of-field.md)
- [leading-lines](leading-lines.md)
- [rule-of-thirds](rule-of-thirds.md)
- [symmetry](symmetry.md)
- [negative-space](negative-space.md)
- [shallow-focus](shallow-focus.md)
- [deep-focus](deep-focus.md)
- [mise-en-scene](mise-en-scene.md)

