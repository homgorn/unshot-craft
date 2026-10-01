---
slug: giallo
title: "Giallo Prompt for AI Image & Video"
category: genres
level: advanced
image: "https://vvsvs.pro/img/cinematique/giallo.webp"
source_url: https://vvsvs.pro/cinematique/giallo
upstream_file: cinematique-catalog.json
upstream_sha256: 03443b1c573aec3c6b13c0ada9f219b7d52c54919ca6bd4374cbec84fd129853
styles: [fracture]
---

Giallo-style scene with [Subject] drenched in vivid primary-color lighting, deep crimson from unseen sources, a pool of intense blue creating color boundaries where red meets blue in deep violet, the composition more concerned with aesthetic beauty than narrative logic, every frame designed as a painting, the Dario Argento principle that terror can be beautiful, the saturated primary colors of "Suspiria"

## Lede

Italian horror-thriller genre known for vivid color palettes, elaborate murder sequences, leather-gloved killers, and a heightened visual style that prioritizes aesthetic beauty over narrative logic. Mario Bava established the giallo with "Blood and Black Lace" (1964) and "Bay of Blood." Dario Argento perfected it with "Deep Red," "Suspiria," and "Tenebre," using vivid primary-color lighting and elaborate set pieces that transform murder into grotesque art. Lucio Fulci pushed the genre to extremes with "The Beyond." The giallo's influence extends to Brian De Palma, Nicolas Winding Refn's "The Neon Demon," and the recent Suspiria remake by Luca Guadagnino.

## When to use

Use giallo for horror-thriller scenes where color, suspense, and elaborate visual staging matter more than strict realism. It suits stalking, gloved killers, labyrinthine interiors, clues, and moments where danger becomes a composed spectacle. The palette should carry psychological pressure through red, blue, and violet boundaries. Avoid using vivid light as mere decoration; every color zone should shape threat, concealment, or attention.

## Directing the AI

Place the subject inside a dark interior divided by intense red and blue light from unseen or stylized sources, allowing their overlap to form deep violet. Use glossy surfaces, sharp silhouettes, elegant framing, and one threatening detail such as a leather-gloved hand at frame edge. Keep color saturation rich without losing facial form or object texture. Move the camera with controlled curiosity, revealing danger through reflections, doorways, and partial views rather than immediate full exposure.

## Common mistakes

- Using random neon colors without establishing the disciplined red, blue, and violet architecture of the scene.
- Flattening shadows with broad fill light, removing the concealment that makes saturated color feel dangerous.
- Centering the threat immediately, leaving no elegant visual search or suspense inside the composition.

## Sources

- Genres: Where to Draw the Line?

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

- [color-grading](color-grading.md)
- [low-key-lighting](low-key-lighting.md)
- [film-noir](film-noir.md)
- [german-expressionism](german-expressionism.md)
- [cinema-verite](cinema-verite.md)
- [french-new-wave](french-new-wave.md)
- [surrealism](surrealism.md)
- [found-footage](found-footage.md)
- [spaghetti-western](spaghetti-western.md)

