---
slug: depth-of-field
title: "Depth of Field Prompt for AI Image & Video"
category: composition
level: basic
image: "https://vvsvs.pro/img/cinematique/depth-of-field.webp"
source_url: https://vvsvs.pro/cinematique/depth-of-field
upstream_file: cinematique-catalog.json
upstream_sha256: 03443b1c573aec3c6b13c0ada9f219b7d52c54919ca6bd4374cbec84fd129853
styles: [depth-layer-moves]
---

Selective depth of field isolating [Subject] in a narrow focused slice, everything in front and behind melting into graduated blur, the cinematic depth of field that modern anamorphic and large-format cinematography has made the visual signature of prestige filmmaking, shot on a large format sensor with an 85mm lens at T1.3

## Lede

The range of distance in a scene that appears acceptably sharp — manipulating depth of field controls what the viewer focuses on and how they perceive spatial depth. The creative use of depth of field defines entirely different cinematic schools: Gregg Toland's infinite depth in "Citizen Kane" versus the paper-thin focus of Wong Kar-wai's films. Robert Richardson uses depth of field as an emotional instrument in Oliver Stone's "JFK" and Tarantino's "The Hateful Eight." Modern large-format sensors on cameras like the ARRI Alexa 65 have given cinematographers like Hoyte van Hoytema and Linus Sandgren even more control over focus separation.

## When to use

Depth of field is a core choice whenever the audience needs guidance about where to look and how much of the space matters. Narrow focus isolates emotion or detail; broad focus reveals relationships across the frame. Use it to control intimacy, suspense, information, and spatial depth. Decide before prompting whether the background is context, distraction, or active story. That decision should determine focus range, not a default preference for cinematic blur.

## Directing the AI

State the nearest and farthest distances that should appear sharp, then identify the exact focal subject. For selective depth, ask for progressive blur before and behind that plane; for broad depth, preserve readable detail through foreground, middle ground, and background. Match apparent focus behavior to perspective and distance. In video, specify whether focus stays locked, follows the subject, or transfers deliberately between planes. Keep the transition smooth and motivated by attention.

## Common mistakes

- Requesting cinematic depth of field without naming a focus plane, leaving sharpness arbitrary and unstable across the image.
- Applying equal blur to objects at different distances, which destroys the gradual spatial cues created by optical focus.
- Keeping the background soft when its action carries essential story information that should remain available to the viewer.

## Sources

- Rules of Shot Composition in Film

## Cross-tool

| tool | params | version | tested |
|---|---|---|---|
| mj61 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| runway_gen3 | `motion_brush: smooth_slow_pan \| aspect_ratio: 16:9 \| duration: 5 \| resolution: 1080p` | gen-3-alpha | no |
| veo2 | `resolution: 1080p \| aspect_ratio: 16:9 \| duration: 5 \| cinematic_style: true` | veo-2 | no |
| kling15 | `camera_motion: slow_pan \| resolution: 1080p \| duration: 5 \| style: cinematic` | kling-1.5 | no |
| luma | `aspect_ratio: 16_9 \| duration: 5 \| resolution: 1080p \| style: cinematic` | dream-machine | no |
| pika15 | `aspect_ratio: 16:9 \| style: cinematic \| duration: 5 \| motion: slow_pan` | pika-1.5 | no |
| sora | `style: cinematic \| resolution: 1080p \| aspect_ratio: 16:9 \| duration: 5 \| motion: slow_pan` | sora-1 | no |

## Related

- [shallow-focus](shallow-focus.md)
- [deep-focus](deep-focus.md)
- [rack-focus](rack-focus.md)
- [rule-of-thirds](rule-of-thirds.md)
- [symmetry](symmetry.md)
- [leading-lines](leading-lines.md)
- [framing-within-frame](framing-within-frame.md)
- [negative-space](negative-space.md)
- [mise-en-scene](mise-en-scene.md)

