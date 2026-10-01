---
slug: lens-flare
title: "Lens Flare Prompt for AI Image & Video"
category: lighting
level: basic
image: "https://vvsvs.pro/img/cinematique/lens-flare.webp"
source_url: https://vvsvs.pro/cinematique/lens-flare
upstream_file: cinematique-catalog.json
upstream_sha256: 03443b1c573aec3c6b13c0ada9f219b7d52c54919ca6bd4374cbec84fd129853
styles: [text-as-mask]
---

Dramatic lens flare across [Subject], horizontal anamorphic flare streaks in cyan and magenta stretching across the entire frame, secondary ghost flares bouncing between lens elements in geometric chains, shot on vintage anamorphic Panavision C-series lenses known for their aggressive but beautiful flare characteristics, the warm amber of sunrise fighting through cool blue coating artifacts

## Lede

Light scattering through lens elements when a bright source hits the glass — once considered a flaw, now deliberately used to add energy, realism, or a dreamy sci-fi quality. J.J. Abrams made lens flare his polarizing signature, filling "Star Trek" (2009) with so many anamorphic flares that the technique became a meme. Before that, Janusz Kamiński used flares expressively in "Saving Private Ryan" and "Minority Report" as a visual language for memory and futurity. Michael Bay embraces flares for action energy, while cinematographer Hoyte van Hoytema uses controlled flares in Christopher Nolan's "Interstellar" to suggest cosmic light bleeding into human vision.

## When to use

Choose lens flare when a bright source should feel physically present inside the optics rather than merely lighting the set. It can energize action, make sunlight feel immediate, or push a scene toward dreamy science fiction. Use it as an event tied to camera angle and source position, not as surface decoration. The technique works best when the flare reinforces heat, scale, memory, glare, or a moment of visual overload.

## Directing the AI

Put a bright source at the edge of the frame or aimed toward the lens, then define the flare's path across the image. Specify a horizontal colored streak, a restrained chain of geometric ghosts, and a warm source fighting cooler coating artifacts. Keep the main face or action readable beneath the effect. For video, make the flare react to camera movement and disappear when the source is blocked; it should slide, bloom, and contract with changing alignment rather than remain pasted in place.

## Common mistakes

- Covering every frame with identical flare artifacts, which makes the effect feel composited rather than caused by a moving light source.
- Letting bright streaks cross the subject's eyes or essential action without a narrative reason, destroying clarity at the focal point.
- Mixing several unrelated flare shapes and colors until the optics no longer appear to belong to one coherent lens.

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

- [backlight](backlight.md)
- [golden-hour](golden-hour.md)
- [color-grading](color-grading.md)
- [three-point-lighting](three-point-lighting.md)
- [key-light](key-light.md)
- [high-key-lighting](high-key-lighting.md)
- [low-key-lighting](low-key-lighting.md)
- [chiaroscuro](chiaroscuro.md)
- [rembrandt-lighting](rembrandt-lighting.md)

