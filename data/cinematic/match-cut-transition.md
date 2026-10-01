---
slug: match-cut-transition
title: Match cut on a shared silhouette
category: editing
level: intermediate
image: https://vincentwei1021.github.io/video-shotcraft/assets/brand/logo-mark.svg
styles: [circle-match-iris, color-block-step-wipe, invisible-cut]
---

Cinematic match cut: [Subject] in the first frame and a different scene in the
second frame share the same silhouette and screen position, hard cut on the shape,
no dissolve, matched camera height and focal length across both frames.

## Lede

A match cut hides the edit by making the second frame arrive already aligned with
the first. The viewer perceives continuity because the silhouette lands where the
previous silhouette was, and never registers the cut itself.

## When to use

Transitions between a product and the problem it solves, between a UI state and a
physical object, and anywhere a hard cut would otherwise feel like a mistake.

## Directing the AI

Name both frames and the shared property. "Same silhouette, same screen position,
same camera height" is the specification; "smooth transition" gets you a dissolve,
which is the opposite of the intent.

## Common mistakes

- Getting a dissolve or a whip pan: say "hard cut, no transition effect".
- Mismatched camera height, which breaks the alignment the cut depends on.
- Silhouettes that are merely similar rather than identical in position.

## Sources

- [Match cut — Wikipedia](https://en.wikipedia.org/wiki/Match_cut)
- [Graphic match — Wikipedia](https://en.wikipedia.org/wiki/Graphic_match)

## Cross-tool

| tool | params | version | tested |
| --- | --- | --- | --- |
| mj61 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | yes |
| runway_gen3 | `ratio=16:9` | gen-3-alpha | no |

## Related

- [circle-match-iris](../wiki/cards/circle-match-iris.md)
- [shot-transitions](../wiki/cards/shot-transitions.md)