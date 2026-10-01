---
slug: centered-symmetry
title: Centred symmetry for hero objects
category: composition
level: basic
image: https://vincentwei1021.github.io/video-shotcraft/assets/brand/logo-mark.svg
styles: [brand-frame-snap, circle-match-iris]
---

Perfectly symmetrical product shot of [Subject] dead centre on the vertical axis,
mirrored surroundings, frontal even lighting, orthographic feel, 100mm, clean
seamless background, no perspective skew.

## Lede

Symmetry is the composition for objects whose shape is the message. When the frame
is bisected and both halves match, the eye has nothing to resolve, and the object
reads as an icon rather than a photograph.

## When to use

Brand marks, product hero shots on flat backgrounds, and UI states where symmetry
signals precision. Avoid for anything with narrative, because symmetry has no
direction for the eye to travel.

## Directing the AI

"Perfectly symmetrical, dead centre, mirrored background" — the mirroring clause is
what makes it work, since the model will happily produce a centred object in an
asymmetric room.

## Common mistakes

- Near-symmetry: the axis is off by a few pixels, which the eye reads as sloppiness.
- Perspective distortion from a wide lens, breaking the mirror.
- Even lighting across a textured object, which flattens it.

## Sources

- [Symmetry in cinematography — Wikipedia](https://en.wikipedia.org/wiki/Symmetry_in_film)
- [Centered composition — Wikipedia](https://en.wikipedia.org/wiki/Rule_of_thirds)

## Cross-tool

| tool | params | version | tested |
| --- | --- | --- | --- |
| mj61 | `--ar 16:9 --v 6.1 --style raw --cw 100` | v6.1 | yes |
| veo2 |  | veo-2 | no |

## Related

- [brand-frame-snap](../wiki/cards/brand-frame-snap.md)