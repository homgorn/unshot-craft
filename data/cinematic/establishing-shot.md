---
slug: establishing-shot
title: "Establishing Shot Prompt for AI Image & Video"
category: camera-work
level: basic
image: "https://vvsvs.pro/img/cinematique/establishing-shot.webp"
source_url: https://vvsvs.pro/cinematique/establishing-shot
upstream_file: cinematique-catalog.json
upstream_sha256: 03443b1c573aec3c6b13c0ada9f219b7d52c54919ca6bd4374cbec84fd129853
styles: [depth-layer-moves, space-camera-moves]
video: media/establishing-shot.mp4
---

Wide establishing shot of [Subject] at blue hour, deep indigo sky with the last traces of sunset, a few warm lights glowing from within, atmospheric haze softening the distance, shot on ARRI Alexa with Zeiss Master Primes, desaturated cool palette with selective warm accents, architectural precision meets cinematic storytelling

## Lede

A wide shot typically used at the beginning of a scene to set the context, showing the location, time of day, and spatial relationships before cutting to closer action. Stanley Kubrick's establishing shots in "The Shining" — the Overlook Hotel dwarfed by mountains — immediately communicated isolation and foreboding. Ridley Scott's opening of "Blade Runner" established a dystopian Los Angeles with a single, unforgettable wide shot of industrial hellscape. David Fincher meticulously crafts establishing shots that embed narrative information into every architectural detail.

## When to use

Open with an establishing shot when viewers need to understand where the scene happens, what time or weather shapes it, and how the key spaces connect. A strong version can also seed isolation, danger, wealth, or decay through architecture and scale. Use it before tighter coverage or after a major location change. Do not spend it on a setting the audience already reads clearly.

## Directing the AI

Frame the location wide enough to show its dominant architecture, surrounding terrain, access points, and one small sign of life. Set the scene at blue hour with a deep indigo sky, faint sunset residue, warm interior lights, and haze softening the distance. Keep the composition legible rather than merely expansive. If generating video, begin still or with a restrained drift, allowing the viewer to map the place before any cut or character movement claims attention.

## Common mistakes

- Showing a beautiful location without the landmarks or spatial relationships needed to orient the next scene.
- Making the principal character too large in frame, turning contextual coverage into a conventional long shot.
- Packing the image with unrelated atmosphere cues that obscure the intended time, geography, or narrative tone.

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

- [aerial-shot](aerial-shot.md)
- [master-shot](master-shot.md)
- [extreme-long-shot](extreme-long-shot.md)
- [birds-eye-view](birds-eye-view.md)
- [close-up](close-up.md)
- [dutch-angle](dutch-angle.md)
- [dolly-shot](dolly-shot.md)
- [extreme-close-up](extreme-close-up.md)
- [eye-level-shot](eye-level-shot.md)

