---
slug: single-take-reveal
title: Single-take reveal with one motivated move
category: editing
level: advanced
image: https://vincentwei1021.github.io/video-shotcraft/assets/brand/logo-mark.svg
styles: [crane-rise-reveal, scanline-assemble-flyin]
---

One continuous take on [Subject], beginning tight on a small detail and craning up
and back to reveal the full scene, no cuts, single continuous camera motion, focus
pull from the detail to the far plane as the move finishes, 35mm.

## Lede

A single-take reveal earns attention by withholding. Nothing is hidden by a cut, so
the viewer learns the scale of the thing by experiencing the move rather than being
told it in a second shot.

## When to use

Product scale reveals, environment establishing shots, and any moment where a cut
would spend the reveal too early.

## Directing the AI

"Continuous single take, no cuts" has to be explicit — models add cuts freely. Name
the start and end of the move and the focus behaviour; the focus pull is what tells
the viewer the move has landed.

## Common mistakes

- A cut sneaking in mid-move.
- Moving without a focus change, so the reveal has no punctuation.
- Rising too fast to read the detail you started on.

## Sources

- [Single-take — Wikipedia](https://en.wikipedia.org/wiki/Continuous_shot)
- [Crane shot — Wikipedia](https://en.wikipedia.org/wiki/Crane_shot)

## Cross-tool

| tool | params | version | tested |
| --- | --- | --- | --- |
| kling15 | `camera_control=crane_up` | kling-1.5 | no |
| veo2 |  | veo-2 | no |
| pika15 |  | pika-1.5 | no |

## Related

- [crane-rise-reveal](../wiki/cards/crane-rise-reveal.md)