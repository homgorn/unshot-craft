---
slug: fade-in-out
title: "Fade In/Out Prompt for AI Image & Video"
category: editing
level: basic
image: "https://vvsvs.pro/img/cinematique/fade-in-out.webp"
source_url: https://vvsvs.pro/cinematique/fade-in-out
upstream_file: cinematique-catalog.json
upstream_sha256: 03443b1c573aec3c6b13c0ada9f219b7d52c54919ca6bd4374cbec84fd129853
styles: [chip-grid-single-select-blackout]
---

Fade to black from [Subject], the image gradually losing luminance over six seconds as the figure becomes shadow and the shadow becomes part of the darkness, the fade so gradual that the exact moment of disappearance is unidentifiable, the emotional weight of permanent conclusion, the visual equivalent of a long exhale

## Lede

The image gradually appears from or disappears to black (or white) — fade to black signals an ending or major time passage while fade from black signals a new beginning or chapter. The Coen Brothers use long, slow fades to black as chapter markers in "No Country for Old Men," each fade feeling like a door closing permanently. Kubrick's fade to white at the end of "2001" suggests transcendence. Martin Scorsese uses the fade to black at the end of "Goodfellas" and "The Irishman" with devastating finality. The pace of the fade itself communicates meaning — a quick fade feels like a curtain dropping while a slow fade feels like consciousness dimming.

## When to use

Fade in or out when the story needs a clear boundary rather than a direct visual connection between shots. A fade to black can close a chapter, suggest long passage, or let consciousness recede; a fade from black can establish a beginning or return. The duration carries meaning. Use a fast fade for decisive closure and a slow one for exhaustion, grief, or gradual disappearance.

## Directing the AI

Choose whether the image enters from black, leaves into black, or uses white for a distinctly brighter transition. Set an exact duration and preserve the shot's composition while luminance changes evenly. For a slow fade, let details disappear in tonal order until the subject merges with darkness; for a fade in, reverse that emergence cleanly. Keep the final black or white hold long enough to register. Do not change subject shape or camera position during the transition unless separately directed.

## Common mistakes

- Treating a fade as a default scene change, weakening the strong sense of chapter, ending, or passage it communicates.
- Changing exposure unevenly across objects, making the transition look like lighting failure rather than the entire image receding.
- Cutting away before full black has time to register, reducing the emotional closure and structural pause.

## Sources

- What Is Film Editing?

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

- [dissolve](dissolve.md)
- [iris-transition](iris-transition.md)
- [flashback](flashback.md)
- [cross-cutting](cross-cutting.md)
- [jump-cut](jump-cut.md)
- [montage](montage.md)
- [smash-cut](smash-cut.md)
- [long-take](long-take.md)
- [freeze-frame](freeze-frame.md)

