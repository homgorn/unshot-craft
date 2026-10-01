---
slug: dolly-shot
title: "Dolly Shot Prompt for AI Image & Video"
category: camera-work
level: intermediate
image: "https://vvsvs.pro/img/cinematique/dolly-shot.webp"
source_url: https://vvsvs.pro/cinematique/dolly-shot
upstream_file: cinematique-catalog.json
upstream_sha256: 03443b1c573aec3c6b13c0ada9f219b7d52c54919ca6bd4374cbec84fd129853
styles: [tension-camera-moves, crash-zoom-punch]
video: media/dolly-shot.mp4
---

Smooth dolly shot gliding toward [Subject], the camera at eye level moving with buttery precision on dolly track, parallax effect separating foreground elements from the mid-ground subject from far-ground details, shot on 35mm with Panavision Primo lenses, rich blacks and saturated warm tones, the elegant motion of precision dolly track work

## Lede

A smooth camera movement where the entire camera physically moves toward, away from, or alongside the subject on a wheeled platform or track, creating an immersive sense of movement through space. Orson Welles used dolly shots to navigate the deep-focus interiors of "Citizen Kane," while Spike Lee invented his signature double-dolly shot — mounting both actor and camera on the same platform — to create a floating, surreal glide seen in "Do the Right Thing" and "25th Hour." Martin Scorsese's famous Copacabana shot in "Goodfellas" tracks Henry Hill through the back entrance of a nightclub in one fluid dolly movement.

## When to use

Use a dolly-in when a realization, threat, or emotional detail needs to become unavoidable. Dolly out when context should overwhelm the subject or create emotional distance. Move alongside a character when the audience should travel with them rather than simply observe them.

## Directing the AI

Describe physical camera travel, direction, speed, subject lock, and foreground-to-background separation. "Dolly toward" is more useful than "cinematic movement." Give the model visible layers for parallax — a foreground obstruction, the subject in the middle distance, and a readable background — so the move changes spatial relationships instead of behaving like a digital zoom.

## Common mistakes

- Calling for a dolly and a zoom at the same time without intentionally asking for a dolly zoom.
- Describing camera movement without foreground or background layers, leaving no parallax for the model to express.
- Stacking "smooth," "dynamic," "epic," and multiple conflicting camera directions instead of specifying one controlled move.

## Sources

- The Dolly Shot: How To Create Powerful Shots With Simple Movement

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

- [tracking-shot](tracking-shot.md)
- [close-up](close-up.md)
- [dutch-angle](dutch-angle.md)
- [aerial-shot](aerial-shot.md)
- [birds-eye-view](birds-eye-view.md)
- [establishing-shot](establishing-shot.md)
- [extreme-close-up](extreme-close-up.md)
- [extreme-long-shot](extreme-long-shot.md)
- [eye-level-shot](eye-level-shot.md)

