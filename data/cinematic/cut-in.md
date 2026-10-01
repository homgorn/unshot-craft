---
slug: cut-in
title: "Cut-In Prompt for AI Image & Video"
category: editing
level: basic
image: "https://vvsvs.pro/img/cinematique/cut-in.webp"
source_url: https://vvsvs.pro/cinematique/cut-in
upstream_file: cinematique-catalog.json
upstream_sha256: 03443b1c573aec3c6b13c0ada9f219b7d52c54919ca6bd4374cbec84fd129853
styles: [circle-match-iris]
---

Cut-in to a tight close-up of [Subject] revealing a telling detail, shot on a 100mm macro lens at T2, the directorial decision to abandon the wider view and find the truth hiding in a specific detail

## Lede

A cut to a closer shot of something already visible in the wider frame — zooming in on hands, a prop, or a facial detail — focusing attention on a specific element within the scene. Sergio Leone's films are built on the rhythm of wide shots cutting in to extreme close-ups of eyes and gun hands. Quentin Tarantino uses stylized cut-ins to food, drinks, and bare feet as signature moments. David Fincher cuts in to hands and screens and text messages with forensic precision in "The Social Network" and "Gone Girl." The cut-in is the editor's way of saying "look at this" — directing attention from the general to the specific.

## When to use

Use a cut-in when an element already present in the master view deserves sudden emphasis. Hands tightening around a glass, a hidden message on a screen, or a flicker in someone's eye can redirect the scene without changing location. It works best when the audience first understands the wider geography, then needs one precise fact, gesture, or object to read the moment correctly.

## Directing the AI

Compose a clear wider view where the detail is visible, then cut to a much tighter angle on that same element. Preserve hand position, object orientation, wardrobe, light direction, and screen direction across the edit. Use shallow depth of field and exact focus to make the detail dominant. Time the cut at the instant the information becomes consequential. Return wide only after the close view has changed the audience's understanding of the action.

## Common mistakes

- Introducing a detail that was absent from the wider shot, breaking continuity and visual credibility.
- Using nearly identical framing for both shots, so the editorial emphasis feels weak and indecisive.
- Cutting closer without a narrative reason, turning a precise attention cue into empty visual punctuation.

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

- [insert-shot](insert-shot.md)
- [extreme-close-up](extreme-close-up.md)
- [rack-focus](rack-focus.md)
- [cross-cutting](cross-cutting.md)
- [jump-cut](jump-cut.md)
- [dissolve](dissolve.md)
- [fade-in-out](fade-in-out.md)
- [montage](montage.md)
- [smash-cut](smash-cut.md)

