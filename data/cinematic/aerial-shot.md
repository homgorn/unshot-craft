---
slug: aerial-shot
title: "Aerial Shot Prompt for AI Image & Video"
category: camera-work
level: intermediate
image: "https://vvsvs.pro/img/cinematique/aerial-shot.webp"
source_url: https://vvsvs.pro/cinematique/aerial-shot
upstream_file: cinematique-catalog.json
upstream_sha256: 03443b1c573aec3c6b13c0ada9f219b7d52c54919ca6bd4374cbec84fd129853
styles: [overhead-camera-moves, crane-rise-reveal]
video: media/aerial-shot.mp4
---

Sweeping aerial shot of [Subject] seen from 300 feet above, captured at golden hour with warm amber light painting one side of the terrain while the other falls into deep violet shadow, volumetric god rays piercing through scattered cumulus clouds, shot on ARRI Alexa 65 with Hasselblad glass, 8K resolution, Kodak Vision3 250D color science, subtle atmospheric haze layering depth into the landscape

## Lede

A shot captured from high above the ground, typically using a drone or helicopter, providing a sweeping view of landscapes, cityscapes, or large-scale action. The aerial perspective conveys omniscience, freedom, or the terrifying scale of nature. David Lean pioneered epic aerial work in "Lawrence of Arabia," while Ridley Scott used helicopter shots to establish the grandeur of ancient Rome in "Gladiator." More recently, Denis Villeneuve employed haunting aerial compositions in "Sicario" to reveal the eerie geometry of border landscapes.

## When to use

Choose an aerial shot when geography matters as much as the subject. It can introduce a city, expose the geometry of a border or road network, track large-scale action, or reduce a person to a vulnerable mark inside the landscape. The height creates emotional distance, so use it for omniscience, freedom, grandeur, or environmental threat rather than intimate character beats.

## Directing the AI

Place the camera roughly 300 feet above the subject and describe a broad downward view rather than a straight top-down angle. Keep a recognizable focal point inside the terrain, then build depth with foreground landforms, distant layers, atmospheric haze, and scattered clouds. Let warm golden-hour light strike one side of the landscape while deep violet shadow holds the other. For motion, specify a slow, stable glide that preserves scale and horizon orientation.

## Common mistakes

- Setting the camera high without defining its angle, leaving the result confused between an aerial view and an overhead diagram.
- Filling every part of the landscape with equal detail, so the subject disappears without a deliberate scale relationship.
- Requesting fast drone movement when the scene needs grandeur, which turns a measured reveal into restless travel footage.

## Sources

- 50+ Types of Camera Shots, Angles, and Techniques

## Cross-tool

| tool | params | version | tested |
|---|---|---|---|
| mj61 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| runway_gen3 | `motion_brush: smooth_pan \| aspect_ratio: 16:9 \| duration: 5 \| resolution: 1080p` | gen-3-alpha | no |
| veo2 | `resolution: 1080p \| aspect_ratio: 16:9 \| duration: 5 \| cinematic_style: true` | veo-2 | no |
| kling15 | `camera_motion: pan_right \| resolution: 1080p \| duration: 5 \| style: cinematic` | kling-1.5 | no |
| luma | `aspect_ratio: 16_9 \| duration: 5 \| resolution: 1080p \| style: cinematic` | dream-machine | no |
| pika15 | `aspect_ratio: 16:9 \| style: cinematic \| duration: 5 \| motion: smooth_pan` | pika-1.5 | no |
| sora | `style: cinematic \| resolution: 1080p \| aspect_ratio: 16:9 \| duration: 5 \| motion: smooth_pan` | sora-1 | no |

## Related

- [extreme-long-shot](extreme-long-shot.md)
- [crane-shot](crane-shot.md)
- [establishing-shot](establishing-shot.md)
- [birds-eye-view](birds-eye-view.md)
- [close-up](close-up.md)
- [dutch-angle](dutch-angle.md)
- [dolly-shot](dolly-shot.md)
- [extreme-close-up](extreme-close-up.md)
- [eye-level-shot](eye-level-shot.md)

