---
slug: forced-perspective
title: "Forced Perspective Prompt for AI Image & Video"
category: visual-effects
level: intermediate
image: "https://vvsvs.pro/img/cinematique/forced-perspective.webp"
source_url: https://vvsvs.pro/cinematique/forced-perspective
upstream_file: cinematique-catalog.json
upstream_sha256: 03443b1c573aec3c6b13c0ada9f219b7d52c54919ca6bd4374cbec84fd129853
---

Forced perspective illusion with [Subject] appearing impossibly large or small through precise camera alignment and placement, the depth of field deep enough that both near and far elements appear sharp, the lighting matching between foreground and background, the Peter Jackson technique of making the impossible look real without digital manipulation, just physics and precise alignment

## Lede

Using the relationship between camera position and object placement to create optical illusions of size — Hobbits appear small next to Gandalf through precise staging rather than CGI. Peter Jackson used forced perspective extensively in "The Lord of the Rings," building oversized and undersized duplicate sets and using precise camera alignment to make Elijah Wood appear four feet shorter than Ian McKellen in the same frame. Jean-Pierre Jeunet used forced perspective for whimsical effect in "Amélie." The technique dates back to the earliest days of cinema and architecture — Egyptian temples and Baroque churches used the same principle to appear larger than they are.

## When to use

Use forced perspective when characters or objects must appear impossibly large or small while sharing one believable frame. It suits fantasy scale, whimsical comedy, giant-object illusions, and practical-looking visual tricks. The technique works from a precise viewpoint, so it is strongest in composed shots with controlled blocking. Avoid wide camera movement unless the alignment and depth relationship can remain locked throughout.

## Directing the AI

Place the larger-looking subject close to camera and the smaller-looking subject farther away on the same sightline. Use deep focus so both planes remain sharp, then match light direction, color temperature, shadow softness, and eye lines across the distance. Hide scale references that expose the separation. Keep the camera fixed at the alignment point. For interaction, choreograph gestures to meet visually in the frame even though the subjects occupy different depths.

## Common mistakes

- Allowing shallow focus to reveal that the apparently adjacent subjects sit on widely separated depth planes.
- Including familiar scale references between subjects, exposing the distance trick before the illusion can work.
- Moving the camera away from the designed viewpoint, causing edges, eye lines, and apparent contact to separate.

## Sources

- Inventing Worlds and Characters: Effects

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

- [deep-focus](deep-focus.md)
- [worms-eye-view](worms-eye-view.md)
- [mise-en-scene](mise-en-scene.md)
- [color-grading](color-grading.md)
- [desaturation](desaturation.md)
- [sepia-tone](sepia-tone.md)
- [film-grain](film-grain.md)
- [bokeh](bokeh.md)
- [lens-distortion](lens-distortion.md)

