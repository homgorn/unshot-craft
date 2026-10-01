---
slug: orbit-reveal
title: Orbit around a stationary subject
category: camera-work
level: intermediate
image: https://vincentwei1021.github.io/video-shotcraft/assets/brand/logo-mark.svg
styles: [basic3-d-scene, cube-navigation, graze-face-tour]
---

Cinematic orbit shot circling [Subject] once at constant radius and speed, subject
stays perfectly still and centred while the background rotates behind it, 85mm,
even key light so the falloff does not betray the move, no dolly zoom.

## Lede

An orbit is the cheapest way to show that an object has depth: because the subject
is static and only the background moves, every edge that reveals a new face proves
the object is three-dimensional rather than a flat render.

## When to use

Product reveals, character introductions that need scale, and any moment where you
want to say "look at all of this" without cutting.

## Directing the AI

Say "orbit" and then forbid the two failure modes explicitly: no subject rotation,
no zoom. Constant radius and constant speed are what stop it reading as a handheld
wobble.

## Common mistakes

- The subject rotates with the camera, which destroys the parallax proof.
- Speed easing, so the move breathes at the wrong moment.
- Falling off a wide lens, which stretches the background as it turns.

## Sources

- [Orbit shot — Wikipedia](https://en.wikipedia.org/wiki/Orbit_shot)
- [Parallax — Wikipedia](https://en.wikipedia.org/wiki/Parallax)

## Cross-tool

| tool | params | version | tested |
| --- | --- | --- | --- |
| mj61 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | yes |
| kling15 | `camera_control=orbit` | kling-1.5 | no |
| pika15 |  | pika-1.5 | no |

## Related

- [basic-3d-scene](../wiki/cards/basic-3d-scene.md)