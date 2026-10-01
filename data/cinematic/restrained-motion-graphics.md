---
slug: restrained-motion-graphics
title: Restrained motion graphics for software
category: visual-style
level: basic
image: https://vincentwei1021.github.io/video-shotcraft/assets/brand/logo-mark.svg
styles: [blur-slide, skeleton-reveal, typing-code-block]
---

Clean product motion frame showing [Subject] as a crisp UI surface on a flat dark
ground, one element moving with a single ease, everything else perfectly still,
precise 8px spacing grid, one accent colour used once, no decorative glow, 60fps.

## Lede

The restraint is the style. When exactly one element moves on an 8-pixel grid with a
single ease, the movement reads as information; when four things move with
decorative easing, the same movement reads as a template.

## When to use

SaaS and developer tools, especially anything shipped alongside real UI. It also
matches the upstream rule set directly: one motion idea per shot, holds after every
key beat, no batch glows.

## Directing the AI

"One element moving, everything else still, single ease" is the clause. Without
"everything else still" you get every element animating, which is the failure this
style exists to avoid.

## Common mistakes

- Batch entrances with per-item easing, which reads as busy rather than precise.
- Glow and bloom on UI elements, which makes flat design look dirty.
- Sub-pixel positions that make the grid read as sloppy.

## Sources

- [Material Design — motion](https://m3.material.io/styles/motion/overview)
- [Apple Human Interface Guidelines — motion](https://developer.apple.com/design/human-interface-guidelines/motion)

## Cross-tool

| tool | params | version | tested |
| --- | --- | --- | --- |
| mj61 | `--ar 16:9 --v 6.1 --cw 100` | v6.1 | yes |
| sora |  | sora-1 | no |

## Related

- [blur-slide](../wiki/cards/blur-slide.md)
- [skeleton-reveal](../wiki/cards/skeleton-reveal.md)