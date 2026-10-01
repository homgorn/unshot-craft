---
slug: analogue-texture
title: Analogue film texture, restrained
category: visual-style
level: basic
image: https://vincentwei1021.github.io/video-shotcraft/assets/brand/logo-mark.svg
styles: [grain-dissolve, riso-print-hits]
---

Cinematic still of [Subject] shot on 35mm film, fine organic grain visible in the
shadows, slight halation around highlights, gently lifted blacks, muted filmic
colour, restrained contrast, no heavy vignette, 50mm.

## Lede

Analogue texture is a *shadow* property first: grain lives in the low end, and
highlights bloom rather than clip. Adding visible grain over a clean digital render
reads as a filter; adding grain into the shadows of a real tonal curve reads as film.

## When to use

Brand work that wants warmth and imperfection, and as a counterweight to a corpus
that otherwise trends toward clean gradient UI motion.

## Directing the AI

"Grain visible in the shadows, halation around highlights" does the work. "Film
grain" on its own gets an even digital noise overlay across the whole frame.

## Common mistakes

- Uniform noise over the whole frame rather than concentrated in the shadows.
- Crushed blacks, which kills the grain along with the detail.
- Heavy vignette, which is a different look entirely (analogue lens falloff).

## Sources

- [Film grain — Wikipedia](https://en.wikipedia.org/wiki/Film_grain)
- [Halation — Wikipedia](https://en.wikipedia.org/wiki/Halation)

## Cross-tool

| tool | params | version | tested |
| --- | --- | --- | --- |
| mj61 | `--ar 16:9 --v 6.1 --style raw --cw 50 --s 250` | v6.1 | yes |
| pika15 |  | pika-1.5 | no |

## Related

- [riso-print-hits](../wiki/cards/riso-print-hits.md)
- [grain-dissolve](../wiki/cards/grain-dissolve.md)