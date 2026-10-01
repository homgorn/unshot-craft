---
slug: split-screen
title: "Split Screen Prompt for AI Image & Video"
category: editing
level: intermediate
image: "https://vvsvs.pro/img/cinematique/split-screen.webp"
source_url: https://vvsvs.pro/cinematique/split-screen
upstream_file: cinematique-catalog.json
upstream_sha256: 03443b1c573aec3c6b13c0ada9f219b7d52c54919ca6bd4374cbec84fd129853
styles: [scanline-assemble-flyin]
---

Split screen dividing the frame with [Subject] visible in both halves simultaneously, one side warm-toned and the other cool-toned, the vertical divide becoming the physical and emotional distance, the De Palma technique of making the audience omniscient observers of parallel realities occupying the same frame

## Lede

The frame is divided into two or more sections, each showing a different angle, location, or timeline simultaneously, showing parallel action, phone conversations, or multiple perspectives at once. Brian De Palma made split screen his signature, using it in "Carrie," "Dressed to Kill," and "Snake Eyes" to create impossible simultaneity. Ang Lee used complex multi-panel split screens in "Hulk" to emulate comic book layouts. Denis Villeneuve employed split screen in "Enemy" to visualize duality, and the technique has experienced a revival in television through shows like "24" where real-time parallel action demanded simultaneous visual presentation.

## When to use

Split screen is effective when the audience needs simultaneous access to separate locations, angles, timelines, or perspectives. Use it for phone calls, parallel action, surveillance, comparison, duality, or events whose timing matters more than spatial unity. Each panel needs a clear function and compatible visual hierarchy. The method becomes exhausting when every panel contains equal motion and detail, so decide where attention should move from moment to moment.

## Directing the AI

Divide the canvas into two or more clean panels with explicit proportions and boundaries. Assign each panel a location, palette, camera angle, and action, then synchronize moments that should connect across the divide. Keep identities and environments stable within their own sections. Control attention by varying motion, contrast, or duration so only one panel dominates at a time. Prevent limbs, faces, and objects from bleeding across boundaries unless a deliberate transition unites the spaces.

## Common mistakes

- Filling every panel with equally intense movement, forcing the viewer to miss essential actions happening at the same time.
- Changing panel sizes and borders without narrative purpose, making the layout feel unstable rather than intentionally dynamic.
- Allowing character features or backgrounds to drift between panels, weakening the distinction between separate locations or perspectives.

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

- [cross-cutting](cross-cutting.md)
- [parallel-storylines](parallel-storylines.md)
- [two-shot](two-shot.md)
- [jump-cut](jump-cut.md)
- [dissolve](dissolve.md)
- [fade-in-out](fade-in-out.md)
- [montage](montage.md)
- [smash-cut](smash-cut.md)
- [long-take](long-take.md)

