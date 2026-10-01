---
slug: kicker-light
title: Three-quarter backlight kicker
category: lighting
level: basic
image: https://vincentwei1021.github.io/video-shotcraft/assets/brand/logo-mark.svg
styles: [spotlight-sweep, spotlight-hero-card]
---

Cinematic portrait of [Subject], three-quarter backlight, deep shadows on the near
side, a soft key picking out the cheekbone and shoulder line, subtle rim separating
the figure from a dark background, shallow depth of field, 35mm, anamorphic flare.

## Lede

A hard backlight placed behind and roughly 40 degrees off the subject's axis does
two jobs at once: it draws a bright edge along the near cheek and shoulder, and it
lets the whole front of the figure fall into shadow. That contrast is what makes a
dark portrait read as lit rather than underexposed.

## When to use

Use it when the subject needs weight and separation but the environment should stay
quiet: product heroes on dark backgrounds, interview subjects against a dim room,
any shot where the silhouette is doing the storytelling.

## Directing the AI

State the key direction and the falloff explicitly. "Backlit" alone gets you a
window behind the subject; "backlight from camera-left at roughly 40 degrees, front
falls to shadow, rim highlights the near cheek and shoulder" gets you the shot.
Naming which side of the face is dark is the single highest-leverage clause.

## Common mistakes

- Filling the shadows. An AI that "balances the exposure" kills the contrast that
  the technique depends on — say "front falls into shadow" explicitly.
- Rimming both sides, which flattens into a halo rather than an edge.
- No background separation, so the rim merges into a bright wall.

## Sources

- [Rim lighting — Wikipedia](https://en.wikipedia.org/wiki/Rim_light)
- [Three-point lighting — Wikipedia](https://en.wikipedia.org/wiki/Three-point_lighting)

## Cross-tool

| tool | params | version | tested |
| --- | --- | --- | --- |
| mj61 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | yes |
| kling15 | `camera_control=true` | kling-1.5 | no |

## Related

- [spotlight-hero-card](../wiki/cards/spotlight-hero-card.md)
- [spotlight-sweep-moves](../wiki/cards/spotlight-sweep-moves.md)