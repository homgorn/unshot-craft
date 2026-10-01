---
slug: low-key-single-source
title: Low-key single-source chiaroscuro
category: lighting
level: advanced
image: https://vincentwei1021.github.io/video-shotcraft/assets/brand/logo-mark.svg
styles: [light-play-moves, halation-bloom]
---

Chiaroscuro portrait of [Subject] lit by a single low hard source from camera-right,
most of the frame falling into black, one narrow highlight along the brow and cheek,
deep unlit background, no fill, 50mm, film grain, Rembrandt lighting.

## Lede

One source, no fill, and the parts of the face it misses are allowed to stay dark.
That is the whole technique: chiaroscuro is a subtraction problem, not a lighting
problem. Most prompts fail it by asking for "dramatic moody lighting" and getting
even, ambient darkness instead.

## When to use

Brand work that wants gravity, historical or period framing, and any shot where you
want the viewer to complete the missing information.

## Directing the AI

Name the single source, its position relative to the camera, and the absence of
fill. "No fill light, unlit side falls to black" is the clause that does the work.
Add a specific shape for the shadow — "a small triangle of light under the far eye"
— because "half the face is dark" gets you generic half-light.

## Common mistakes

- Adding ambient or bounce the prompt did not ask for; the shadow fills in.
- Losing the shape: the light spills so wide there is no defined terminator.
- Over-grading to black, which costs the subject any readable form.

## Sources

- [Chiaroscuro — Wikipedia](https://en.wikipedia.org/wiki/Chiaroscuro)
- [Rembrandt lighting — Wikipedia](https://en.wikipedia.org/wiki/Rembrandt_lighting)

## Cross-tool

| tool | params | version | tested |
| --- | --- | --- | --- |
| mj61 | `--ar 16:9 --v 6.1 --style raw --cw 100` | v6.1 | yes |
| runway_gen3 | `ratio=16:9, seed=fixed` | gen-3-alpha | no |
| kling15 | `negative_prompt=flat lighting, fill light` | kling-1.5 | no |

## Related

- [kicker-light](kicker-light.md)
- [light-play-moves](../wiki/cards/light-play-moves.md)