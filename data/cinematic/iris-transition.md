---
slug: iris-transition
title: "Iris Prompt for AI Image & Video"
category: editing
level: basic
image: "https://vvsvs.pro/img/cinematique/iris-transition.webp"
source_url: https://vvsvs.pro/cinematique/iris-transition
upstream_file: cinematique-catalog.json
upstream_sha256: 03443b1c573aec3c6b13c0ada9f219b7d52c54919ca6bd4374cbec84fd129853
styles: [circle-match-iris]
---

Iris transition closing concentrically around [Subject] at center frame, the circular black mask tightening from edges like a closing eye, the world progressively swallowed by darkness until only a small disc remains, the charming self-awareness of silent cinema technique, warm sepia-inflected tones suggesting aged film stock

## Lede

A circular aperture opens or closes on the frame, focusing attention on a specific point — an early cinema technique that has seen a modern revival for its charming, self-aware quality. D.W. Griffith and Buster Keaton used iris shots extensively in the silent era to direct attention and create transitions. The technique fell out of favor with the arrival of sound but has been revived by directors like the Coen Brothers in "The Hudsucker Proxy," Wes Anderson in "The Grand Budapest Hotel," and Martin Scorsese in "Hugo" as an affectionate nod to cinema's origins. The iris closing on a character's face is one of the most recognizable images from early film history.

## When to use

Use an iris when you want to end on a face, object, or gesture with unmistakable theatrical emphasis. It suits chapter endings, comic exits, storybook framing, and affectionate references to early cinema. Because the device announces itself, reserve it for sequences with formal playfulness or nostalgia. It is less effective in scenes that depend on seamless realism or emotional restraint.

## Directing the AI

Place the chosen subject precisely at the center or selected focal point. Close a circular black mask concentrically from the frame edges, keeping the remaining image stable as the visible disc shrinks. For an opening iris, reverse the movement and reveal the scene around the point of interest. Use warm, slightly aged color and restrained grain if nostalgia fits. Finish on full black or a fully open frame rather than stopping at an arbitrary aperture.

## Common mistakes

- Misplacing the subject so the closing circle drifts away from the intended emotional or comic focus.
- Combining the iris with excessive motion, making the audience chase the subject inside a shrinking frame.
- Applying aged color and grain so heavily that the transition becomes parody rather than affectionate reference.

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

- [wipe-transition](wipe-transition.md)
- [fade-in-out](fade-in-out.md)
- [centered-composition](centered-composition.md)
- [cross-cutting](cross-cutting.md)
- [jump-cut](jump-cut.md)
- [dissolve](dissolve.md)
- [montage](montage.md)
- [smash-cut](smash-cut.md)
- [long-take](long-take.md)

