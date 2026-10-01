---
slug: found-footage
title: "Found Footage Prompt for AI Image & Video"
category: genres
level: basic
image: "https://vvsvs.pro/img/cinematique/found-footage.webp"
source_url: https://vvsvs.pro/cinematique/found-footage
upstream_file: cinematique-catalog.json
upstream_sha256: 03443b1c573aec3c6b13c0ada9f219b7d52c54919ca6bd4374cbec84fd129853
styles: [graze-face-tour]
---

Found footage shot of [Subject] through a consumer-grade camera in night vision mode, the entire image in distinctive green-tinged infrared, the framing chaotic and uncontrolled, the footage corrupted with digital artifacts and compression blocks, timestamp running in the corner, the Blair Witch principle that what you cannot clearly see is infinitely more terrifying, the aesthetic of authenticity as horror's most effective weapon

## Lede

A style presenting the film as discovered amateur or surveillance recordings — "The Blair Witch Project," "Paranormal Activity," the conceit that what you're watching is "real" raw footage. Ruggero Deodato's "Cannibal Holocaust" (1980) invented the format, so convincingly that the director was charged with murder before proving the actors were alive. "The Blair Witch Project" (1999) made found footage a cultural phenomenon and a marketing revolution. "Cloverfield" brought the style to blockbuster scale, and "Paranormal Activity" proved it could be extraordinarily profitable. The format exploits our associations between low production quality and authenticity.

## When to use

Use found footage when the recording itself is part of the story: evidence, a recovered diary, surveillance, or a final document of danger. It is especially effective for horror because limited framing and imperfect visibility force the audience to search the image. Define who holds the camera and why they keep filming. Without that motivation, chaotic footage feels like an effect rather than discovered material.

## Directing the AI

Choose a specific recording source and keep its limitations consistent: consumer camera, night vision, surveillance angle, or phone-like handheld footage. Add reactive framing, delayed pans, autofocus hunting, compression blocks, and a stable timestamp without obscuring essential action. In darkness, reveal partial shapes at the edge rather than a fully lit threat. Let the operator's breath, movement, and fear affect the image. Preserve continuous geography so uncertainty comes from visibility, not incoherence.

## Common mistakes

- Changing recording formats and artifact styles between shots without a story reason for the source change.
- Showing the threat clearly in centered light, removing the uncertainty that makes limited footage frightening.
- Ignoring the camera operator's motive, so continued filming during danger feels implausible and mechanically convenient.

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

- [cinema-verite](cinema-verite.md)
- [handheld-shot](handheld-shot.md)
- [cosmic-horror](cosmic-horror.md)
- [film-noir](film-noir.md)
- [german-expressionism](german-expressionism.md)
- [french-new-wave](french-new-wave.md)
- [surrealism](surrealism.md)
- [spaghetti-western](spaghetti-western.md)
- [italian-neorealism](italian-neorealism.md)

