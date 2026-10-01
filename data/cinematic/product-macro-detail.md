---
slug: product-macro-detail
title: Macro detail with a rack focus
category: camera-work
level: intermediate
image: https://vincentwei1021.github.io/video-shotcraft/assets/brand/logo-mark.svg
styles: [focus-handoff-transition, depth-layer-moves, auto-layout-gap-dial]
---

Extreme macro detail of [Subject] filling the frame, texture visible, focus racking
from the near surface to the far plane mid-shot, shallow depth of field, controlled
key light skimming across the surface, 100mm macro, no camera movement.

## Lede

At macro distances depth of field becomes a few millimetres, so a focus pull is the
only move available. That constraint is useful: it turns attention into a physical
act the viewer can follow, rather than a cut that asks them to notice a difference.

## When to use

Material and texture proof, hardware close-ups, and detail shots that hand off to a
wider frame.

## Directing the AI

"Focus racks from the near surface to the far plane" plus "shallow depth of field" is
the mechanism. Pair it with a declared motion-card handoff so the rack lands on a
cut, which is what turns the pull into a transition.

## Common mistakes

- Too much depth of field, so the rack has nothing to travel through.
- Adding camera movement to a technique that is entirely about focus.
- Racking too fast to read either plane.

## Sources

- [Rack focus — Wikipedia](https://en.wikipedia.org/wiki/Focus_pulling)
- [Macro photography — Wikipedia](https://en.wikipedia.org/wiki/Macro_photography)

## Cross-tool

| tool | params | version | tested |
| --- | --- | --- | --- |
| mj61 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | yes |
| runway_gen3 |  | gen-3-alpha | no |

## Related

- [depth-layer-moves](../wiki/cards/depth-layer-moves.md)
- [spotlight-hero-card](../wiki/cards/spotlight-hero-card.md)