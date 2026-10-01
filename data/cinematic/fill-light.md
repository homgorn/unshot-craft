---
slug: fill-light
title: "Fill Light Prompt for AI Image & Video"
category: lighting
level: basic
image: "https://vvsvs.pro/img/cinematique/fill-light.webp"
source_url: https://vvsvs.pro/cinematique/fill-light
upstream_file: cinematique-catalog.json
upstream_sha256: 03443b1c573aec3c6b13c0ada9f219b7d52c54919ca6bd4374cbec84fd129853
styles: [spotlight-hero-card]
---

Fill light softening the shadows on [Subject], a gentle secondary source creating a 4:1 contrast ratio, the shadow side retaining detail and color rather than falling to black, the fill large and diffused so it wraps without creating competing shadows, shot on 35mm Kodak Vision3 with a 65mm lens, the nuanced lighting ratio that separates professional from amateur cinematography

## Lede

A secondary light used to soften or fill in shadows created by the key light, controlling the contrast ratio of the scene — more fill means softer, less fill means more dramatic. The fill light ratio is one of the most consequential creative decisions in cinematography. Gordon Willis deliberately withheld fill in "The Godfather," letting shadows go black, while Robert Richardson uses generous fill in Scorsese's "Hugo" to create a warm, inviting visual world. Roger Deakins is known for using minimal, precisely placed fill — often just a white card or bounce — to retain naturalism while keeping shadow detail alive in films like "No Country for Old Men."

## When to use

Bring in fill light when the key creates the right direction but the shadows hide too much story information. It is useful for dialogue, portraits, product work, and any scene where faces must remain dimensional yet readable. More fill creates a gentle, open image; less fill preserves danger and mystery. Treat the fill level as an emotional decision, especially when matching several shots within the same conversation or sequence.

## Directing the AI

Establish the key light first, then add a broad, diffused secondary source near the camera side. Ask for soft shadow recovery without a second visible shadow or competing highlight. Define the desired contrast clearly: the shadow side should retain color, eye detail, and facial structure while staying darker than the key side. Keep the fill neutral unless the environment motivates a tint. Across video shots, preserve the same key-to-fill relationship so contrast does not pulse between cuts.

## Common mistakes

- Raising fill until the face becomes flat and directionless, erasing the visual hierarchy established by the key light.
- Using a small hard fill source that casts its own sharp shadow and reveals the artificial lighting setup.
- Changing the fill ratio between adjacent shots, causing skin contrast and shadow detail to jump during the edit.

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

- [key-light](key-light.md)
- [three-point-lighting](three-point-lighting.md)
- [soft-light](soft-light.md)
- [high-key-lighting](high-key-lighting.md)
- [low-key-lighting](low-key-lighting.md)
- [chiaroscuro](chiaroscuro.md)
- [rembrandt-lighting](rembrandt-lighting.md)
- [silhouette](silhouette.md)
- [golden-hour](golden-hour.md)

