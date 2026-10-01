---
slug: close-up
title: "Close-Up Prompt for AI Image & Video"
category: camera-work
level: basic
image: "https://vvsvs.pro/img/cinematique/close-up.webp"
source_url: https://vvsvs.pro/cinematique/close-up
upstream_file: cinematique-catalog.json
upstream_sha256: 03443b1c573aec3c6b13c0ada9f219b7d52c54919ca6bd4374cbec84fd129853
styles: [spotlight-hero-card]
video: media/close-up.mp4
---

Tight close-up of [Subject] filling the entire frame, every pore and texture rendered in sharp detail, shallow depth of field with background dissolving into creamy bokeh, warm sidelight from a single source, shot on Cooke S4 75mm at T2, Kodak Vision3 500T color science

## Lede

A tightly framed shot that fills the screen with a subject's face or a specific detail, revealing emotions, textures, and subtle details invisible in wider shots. Carl Theodor Dreyer's "The Passion of Joan of Arc" (1928) is built almost entirely from devastating close-ups of Renée Falconetti's face, widely considered the greatest performance ever captured on film. Sergio Leone elevated the close-up to operatic intensity in his Westerns, while Jonathan Demme's direct-to-camera close-ups in "The Silence of the Lambs" created unbearable intimacy with Hannibal Lecter.

## When to use

Use a close-up when a face, gesture, or object carries the meaning of the scene. It removes environmental information and asks the audience to read micro-expression, texture, and hesitation. Save it for information that genuinely deserves intimacy; constant close-ups flatten the visual hierarchy.

## Directing the AI

Specify the crop, focal length, focus plane, eye line, and one motivated light source. If the face must remain consistent, describe the identity before the shot language and keep lens distortion controlled with portrait-range focal lengths. For video, ask for restrained movement — a breath, blink, or minute push-in — rather than a second competing action.

## Common mistakes

- Using a very wide lens close to the face when you do not want exaggerated facial distortion.
- Adding so much environment and action that the result stops reading as a close-up.
- Demanding sharp eyes, sharp background, heavy bokeh, and extreme shallow focus simultaneously.

## Sources

- Close-Up Shots: Examples of Camera Movement and Angles

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

- [dolly-shot](dolly-shot.md)
- [dutch-angle](dutch-angle.md)
- [rembrandt-lighting](rembrandt-lighting.md)
- [aerial-shot](aerial-shot.md)
- [birds-eye-view](birds-eye-view.md)
- [establishing-shot](establishing-shot.md)
- [extreme-close-up](extreme-close-up.md)
- [extreme-long-shot](extreme-long-shot.md)
- [eye-level-shot](eye-level-shot.md)

