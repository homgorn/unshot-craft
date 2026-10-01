---
slug: hard-cut-on-beat
title: Hard cut on the beat
category: editing
level: basic
image: https://vincentwei1021.github.io/video-shotcraft/assets/brand/logo-mark.svg
styles: [beat-cut-accelerando, strobe-black-frames, impact-feedback]
---

Fast-cut montage on [Subject], every cut landing exactly on a drum transient, six to
twelve frames per shot, no dissolves, hard audio transient on each cut, 24fps
shutter, high contrast.

## Lede

A cut on a transient reads as intentional because the ear and the eye arrive at the
same instant. A cut a few frames late reads as a mistake, and no amount of good
footage will fix the timing.

## When to use

Trailers, product hype reels, and the opening thirty seconds of a launch film. This
is the technique the upstream `music-beat-sync.md` methodology exists to support,
including its hard rule: measure real BPM first, then verify cut error is under
three frames against the rendered audio.

## Directing the AI

"Every cut lands exactly on the drum hit" plus a frame budget. Generate against a
known track rather than "to the music", which is the difference between a measurable
edit and a hopeful one.

## Common mistakes

- Cuts on the wrong transient — snare where the kick is.
- Varying shot length below the readability floor, which becomes flicker.
- Dissolves sneaking in, which smear the audio-image lock the technique needs.

## Sources

- [Jump cut — Wikipedia](https://en.wikipedia.org/wiki/Jump_cut)
- [Montage — Wikipedia](https://en.wikipedia.org/wiki/Montage)

## Cross-tool

| tool | params | version | tested |
| --- | --- | --- | --- |
| runway_gen3 |  | gen-3-alpha | no |
| pika15 |  | pika-1.5 | no |

## Related

- [beat-cut-moves](../wiki/cards/beat-cut-moves.md)
- [rhythm-interrupt-moves](../wiki/cards/rhythm-interrupt-moves.md)