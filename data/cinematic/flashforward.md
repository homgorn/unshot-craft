---
slug: flashforward
title: "Flashforward Prompt for AI Image & Video"
category: narrative
level: intermediate
image: "https://vvsvs.pro/img/cinematique/flashforward.webp"
source_url: https://vvsvs.pro/cinematique/flashforward
upstream_file: cinematique-catalog.json
upstream_sha256: 03443b1c573aec3c6b13c0ada9f219b7d52c54919ca6bd4374cbec84fd129853
styles: [shot-transitions]
---

Flashforward showing [Subject] in a future state, the visual treatment cooler and more desaturated than present-day scenes, the camera positioned in the same angle as earlier shots to make the change more devastating by comparison, the flashforward creating dramatic irony as the audience now carries knowledge of this future while watching the present unfold

## Lede

A scene that jumps ahead to show future events before returning to the present timeline, creating dramatic irony, dread, or anticipation by revealing a destination before the journey. Nicolas Roeg used flashforwards brilliantly in "Don't Look Now," where glimpses of the future create a web of dread throughout the film. "Breaking Bad" famously opens seasons with enigmatic flashforwards — the machine gun in the trunk, the burning teddy bear — that recontextualize everything that follows. Denis Villeneuve's "Arrival" builds its entire narrative twist on what the audience assumes are flashbacks but are actually flashforwards, fundamentally altering the audience's understanding of time and memory.

## When to use

Use a flashforward when knowing the destination will make the journey more charged. Show a future injury, altered relationship, ruined place, or unexplained object, then return to the present while the audience carries that knowledge. It is effective for dread and dramatic irony, especially when the future image raises a precise question. Do not reveal so much that the intervening story loses uncertainty or possibility.

## Directing the AI

Repeat a present-day camera angle in the future so changes become immediately comparable. Shift the future toward cooler, restrained color, altered light, and visible consequences while preserving recognizable architecture, wardrobe cues, or props. Keep the glimpse concise and focus on one unanswered change. Transition back through a visual match or sharp temporal cut. The audience should recognize that time advanced, understand what changed, and still need to discover why it happened.

## Common mistakes

- Changing every visual element at once, so the future no longer connects clearly to the present timeline.
- Showing the complete chain of events, removing the dramatic question that should energize the present story.
- Treating the future as a generic dream with no stable detail the audience can remember or track.

## Sources

- How to Make a Short Film: An Introduction to Filmmaking

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

- [flashback](flashback.md)
- [foreshadowing](foreshadowing.md)
- [non-linear-narrative](non-linear-narrative.md)
- [breaking-fourth-wall](breaking-fourth-wall.md)
- [in-medias-res](in-medias-res.md)
- [cliffhanger](cliffhanger.md)
- [parallel-storylines](parallel-storylines.md)
- [frame-narrative](frame-narrative.md)
- [voiceover-narration](voiceover-narration.md)

