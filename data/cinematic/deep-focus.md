---
slug: deep-focus
title: "Deep Focus Prompt for AI Image & Video"
category: composition
level: intermediate
image: "https://vvsvs.pro/img/cinematique/deep-focus.webp"
source_url: https://vvsvs.pro/cinematique/deep-focus
upstream_file: cinematique-catalog.json
upstream_sha256: 03443b1c573aec3c6b13c0ada9f219b7d52c54919ca6bd4374cbec84fd129853
styles: [space-camera-moves]
---

Deep focus composition with [Subject] visible across multiple planes simultaneously, all razor-sharp from two feet to thirty feet, the viewer free to explore any layer, requiring a small aperture of f/11 and powerful invisible lighting, shot on a 21mm wide lens to maximize depth of field, the Citizen Kane democratic composition where every inch of the frame rewards examination

## Lede

Everything in the frame — foreground, middle ground, and background — is in sharp focus simultaneously, allowing the viewer to explore the entire image and discover relationships between planes. Orson Welles and Gregg Toland made deep focus the defining visual innovation of "Citizen Kane" (1941), composing shots where action in the foreground, middle ground, and background all demanded simultaneous attention. William Wyler used deep focus in "The Best Years of Our Lives" to create some of cinema's most layered compositions. Jean Renoir's deep-focus staging in "Rules of the Game" lets multiple storylines play out in a single frame. The technique gives audiences agency — André Bazin argued it was more democratic than montage.

## When to use

Deep focus belongs in scenes where multiple planes carry simultaneous story information. Use it for ensemble staging, architecture, power relationships, reveals within one shot, or moments when the audience should choose where to look. Sharp foreground and background action can create tension without cutting. The technique demands deliberate arrangement across depth; if every plane is equally detailed but narratively empty, the result becomes busy rather than layered.

## Directing the AI

Stage distinct elements in foreground, middle ground, and background, then keep all three planes acceptably sharp. Use a wider perspective, strong depth cues, and enough even illumination to preserve texture throughout the space. Give each plane a different narrative function and prevent overlapping silhouettes from merging. Maintain atmospheric perspective without turning the distance soft. For video, coordinate action across layers so attention can shift through movement and timing, not through an artificial blur change.

## Common mistakes

- Keeping everything sharp without staging meaningful relationships across depth, producing detail density instead of dramatic complexity.
- Stacking figures directly behind one another, causing silhouettes to merge even though every plane remains technically focused.
- Adding heavy background haze or blur that contradicts the requirement for readable distant action and spatial information.

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

- [depth-of-field](depth-of-field.md)
- [foreground-interest](foreground-interest.md)
- [mise-en-scene](mise-en-scene.md)
- [rule-of-thirds](rule-of-thirds.md)
- [symmetry](symmetry.md)
- [leading-lines](leading-lines.md)
- [framing-within-frame](framing-within-frame.md)
- [negative-space](negative-space.md)
- [shallow-focus](shallow-focus.md)

