---
slug: frame-narrative
title: "Frame Narrative Prompt for AI Image & Video"
category: narrative
level: intermediate
image: "https://vvsvs.pro/img/cinematique/frame-narrative.webp"
source_url: https://vvsvs.pro/cinematique/frame-narrative
upstream_file: cinematique-catalog.json
upstream_sha256: 03443b1c573aec3c6b13c0ada9f219b7d52c54919ca6bd4374cbec84fd129853
styles: [stroke-segment-build]
---

Frame narrative with [Subject] as the storyteller in warm amber lamplight, the image beginning to dissolve into the story being told, two realities briefly coexisting in the dissolve, the warm domestic frame giving way to the adventure palette of the nested story, the nested structure raising questions about what is real and what has been embellished

## Lede

A story-within-a-story structure — a character tells a tale, and we watch it unfold — creating layers of perspective, questions of reliability, and a satisfying nesting of narratives. Rob Reiner's "The Princess Bride" is a beloved frame narrative, with Peter Falk reading to Fred Savage while the fairy tale plays out. "Titanic" uses a frame narrative of elderly Rose recounting her experience to researchers. Wes Anderson employs nested frame narratives in "The Grand Budapest Hotel" — a girl reads a book by an author recounting a story told to him by Zero Moustafa. The frame narrative raises inherent questions of reliability since we see events filtered through a teller's perspective.

## When to use

Use a frame narrative when the act of telling matters as much as the tale. A narrator can filter events through memory, bias, affection, or invention, while the outer scene gives the audience a place to question and interpret the inner story. It suits recollection, legend, testimony, and storybook structures. Return to the frame at meaningful points so it shapes the nested narrative rather than merely introducing it.

## Directing the AI

Stage the storyteller in a stable, intimate frame with warm lamplight and a clear listener or storytelling object. Transition into the nested tale through a dissolve, matched gesture, page, photograph, or changing background. Give the inner story a broader palette and different spatial scale, but repeat one visual element from the frame to preserve authorship. When returning, reveal a reaction or altered detail that questions, confirms, or complicates what the audience just saw.

## Common mistakes

- Abandoning the outer frame after the opening, making the storyteller structurally unnecessary to the narrative.
- Giving both narrative layers identical visual treatment, so the transition between teller and tale becomes muddy.
- Using the frame only for exposition instead of allowing perspective or reliability to affect the inner story.

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

- [voiceover-narration](voiceover-narration.md)
- [flashback](flashback.md)
- [dissolve](dissolve.md)
- [foreshadowing](foreshadowing.md)
- [breaking-fourth-wall](breaking-fourth-wall.md)
- [in-medias-res](in-medias-res.md)
- [cliffhanger](cliffhanger.md)
- [flashforward](flashforward.md)
- [non-linear-narrative](non-linear-narrative.md)

