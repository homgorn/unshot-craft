---
slug: slow-dolly-in
title: Slow dolly-in on a locked subject
category: camera-work
level: basic
image: https://vincentwei1021.github.io/video-shotcraft/assets/brand/logo-mark.svg
styles: [crane-rise-reveal, dolly-zoom-real, camera-flyover]
---

Cinematic shot of [Subject], slow steady dolly-in from a medium wide to a medium
close over about eight seconds, subject held at the same screen position, background
parallax sliding outward, 50mm on a dolly, locked horizon, no handheld shake.

## Lede

A dolly-in changes the relationship between subject and background rather than
magnifying the frame. Everything behind the subject shifts in scale at a different
rate, so the move reads as travelling into the scene, not zooming at it.

## When to use

When you want to add weight to a statement, or move the viewer from context into
detail without cutting. It is the default move for an opening line and for a reveal.

## Directing the AI

Give the duration, the start and end framing, and the parallax explicitly. "Slow
dolly-in over eight seconds from medium wide to medium close, background
parallax" distinguishes it from a zoom, which the model will otherwise choose.

## Common mistakes

- Producing a zoom: background stays static, so the move reads as a flat scale-up.
- Too fast. Under four seconds reads as a push, not a drift.
- Handheld micro-shake, which reads as "amateur" rather than "cinematic".

## Sources

- [Dolly shot — Wikipedia](https://en.wikipedia.org/wiki/Dolly_zoom)
- [Tracking shot — Wikipedia](https://en.wikipedia.org/wiki/Tracking_shot)

## Cross-tool

| tool | params | version | tested |
| --- | --- | --- | --- |
| mj61 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | yes |
| kling15 | `camera_control=forward, camera_speed=slow` | kling-1.5 | no |
| veo2 |  | veo-2 | no |

## Related

- [crane-rise-reveal](../wiki/cards/crane-rise-reveal.md)
- [tension-camera-moves](../wiki/cards/tension-camera-moves.md)