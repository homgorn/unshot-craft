---
slug: silhouette
title: "Silhouette Prompt for AI Image & Video"
category: lighting
level: basic
image: "https://vvsvs.pro/img/cinematique/silhouette.webp"
source_url: https://vvsvs.pro/cinematique/silhouette
upstream_file: cinematique-catalog.json
upstream_sha256: 03443b1c573aec3c6b13c0ada9f219b7d52c54919ca6bd4374cbec84fd129853
styles: [brand-ink-open]
---

[Subject] reduced to a pure dark silhouette against an intensely bright backlight source, all surface detail eliminated leaving only iconic form and outline, strong rim light tracing edges, high contrast, Kodak Double-X black and white stock

## Lede

Subject appears as a dark shape against a bright background, with all surface detail eliminated, reducing characters to pure form and creating iconic, mythic, or anonymous images. David Lean created one of cinema's most recognizable silhouettes with Peter O'Toole against the desert sun in "Lawrence of Arabia." Steven Spielberg's E.T. bicycle silhouette against the moon became one of the most iconic images in film history. Terrence Malick uses human silhouettes against twilight skies throughout "The Thin Red Line" and "Days of Heaven" to reduce characters to archetypal figures against an indifferent natural world.

## When to use

Use a silhouette when identity should give way to shape, gesture, or archetype. It can make a figure mythic, anonymous, romantic, threatening, or small against a bright world. The outline must communicate the action because interior detail disappears. Choose distinctive profiles and separated limbs. Avoid silhouettes for moments that depend on facial performance, costume texture, or subtle information inside the subject.

## Directing the AI

Place the strongest light source directly behind the subject and expose for the bright sky, doorway, moon, or screen. Reduce the figure to near-black with no visible facial or surface detail. Separate arms, legs, props, and profile so the outline reads instantly, then add only a thin edge trace if needed. Keep the background simple and luminous. In video, choreograph lateral movement that preserves the silhouette instead of merging body parts together.

## Common mistakes

- Lifting shadow detail inside the figure, weakening the graphic reduction that makes a silhouette instantly recognizable.
- Overlapping limbs and props against the torso, creating an unreadable dark mass instead of expressive outline.
- Using a cluttered bright background whose shapes compete with the subject's edge and destroy figure-ground clarity.

## Sources

- Film Lighting

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

- [backlight](backlight.md)
- [figure-ground](figure-ground.md)
- [golden-hour](golden-hour.md)
- [three-point-lighting](three-point-lighting.md)
- [key-light](key-light.md)
- [high-key-lighting](high-key-lighting.md)
- [low-key-lighting](low-key-lighting.md)
- [chiaroscuro](chiaroscuro.md)
- [rembrandt-lighting](rembrandt-lighting.md)

