---
slug: low-key-lighting
title: "Low-Key Lighting Prompt for AI Image & Video"
category: lighting
level: intermediate
image: "https://vvsvs.pro/img/cinematique/low-key-lighting.webp"
source_url: https://vvsvs.pro/cinematique/low-key-lighting
upstream_file: cinematique-catalog.json
upstream_sha256: 03443b1c573aec3c6b13c0ada9f219b7d52c54919ca6bd4374cbec84fd129853
styles: [brand-ink-open, spotlight-hero-card]
---

Low-key lighting on [Subject] with deep impenetrable shadows claiming eighty percent of the frame, only a single source illuminating a small area, the contrast ratio pushed to 8:1 between highlights and shadows, shot on Kodak Double-X black and white stock with a 40mm Baltar lens, the inky blacks and silver highlights of classic film noir, John Alton-level mastery of darkness as an active compositional element

## Lede

A dramatic lighting style dominated by deep shadows and high contrast where only select areas are illuminated, creating mystery, tension, and a noir-like atmosphere. John Alton literally wrote the book — "Painting with Light" — and defined low-key noir cinematography in films like "The Big Combo" and "T-Men." Gordon Willis pushed low-key to its extreme in "The Godfather," with Marlon Brando's eyes often invisible in shadow. Bradford Young's low-key work in "Arrival" and "Selma" brought a moody, naturalistic darkness to modern cinema, and Robert Richardson uses low-key lighting in Tarantino's "The Hateful Eight" to make a single-room Western feel like a horror film.

## When to use

Use low-key lighting when darkness should occupy the frame as an active dramatic force. It suits mystery, crime, horror, secrecy, moral ambiguity, and intimate scenes where only selected information is revealed. Strong contrast can direct attention with remarkable precision. The goal is not merely to make everything dim; retain a readable highlight structure so faces, objects, and silhouettes emerge exactly where the story needs them.

## Directing the AI

Let roughly eighty percent of the frame fall into deep shadow and assign one controlled source to the essential face, hand, or object. Push the contrast toward an 8:1 relationship while preserving texture in chosen highlights and allowing other areas to vanish. Use inky blacks, silver or warm highlights, and negative fill to prevent ambient spill. Keep the beam motivated and narrowly shaped. For motion, ensure the subject passes through planned islands of light.

## Common mistakes

- Underexposing the entire image evenly, which creates muddy darkness without the selective highlight structure low key requires.
- Opening shadows with excessive fill, weakening mystery and turning the setup into ordinary balanced lighting.
- Crushing every black area identically, leaving no separation between subject, wardrobe, and background where readability matters.

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

- [chiaroscuro](chiaroscuro.md)
- [film-noir](film-noir.md)
- [hard-light](hard-light.md)
- [three-point-lighting](three-point-lighting.md)
- [key-light](key-light.md)
- [high-key-lighting](high-key-lighting.md)
- [rembrandt-lighting](rembrandt-lighting.md)
- [silhouette](silhouette.md)
- [golden-hour](golden-hour.md)

