---
slug: film-grain
title: "Film Grain Prompt for AI Image & Video"
category: visual-effects
level: basic
image: "https://vvsvs.pro/img/cinematique/film-grain.webp"
source_url: https://vvsvs.pro/cinematique/film-grain
upstream_file: cinematique-catalog.json
upstream_sha256: 03443b1c573aec3c6b13c0ada9f219b7d52c54919ca6bd4374cbec84fd129853
---

Heavy film grain visible on [Subject], the organic random texture of high-speed 35mm film stock pushed two stops in processing, each frame alive with dancing silver halide crystals, the grain coarser in shadows and finer in highlights, Kodak Vision3 500T texture that Tarantino and Nolan insist on preserving, the organic soul of celluloid in an increasingly digital world

## Lede

The visible texture of chemical film stock — random variations in density and color that give analog footage its organic, tactile character, often added digitally for warmth and nostalgia. Christopher Nolan and Quentin Tarantino remain committed to shooting on actual film stock, preserving the authentic grain of celluloid. Steven Soderbergh shot "Traffic" on different film stocks to differentiate storylines. Modern digital films frequently add film grain in post-production — David Fincher, despite shooting digitally, adds carefully calibrated grain to every frame. The resurgence of film grain aesthetics in photography and video reflects a cultural desire for the organic imperfection that digital capture eliminates.

## When to use

Use film grain when pristine digital surfaces feel too sterile for the story, or when a period, documentary, intimate, or nostalgic mood benefits from tactile imperfection. Grain can unify composited elements and give shadows physical texture. Choose its strength to match the scene's light and emotional register. Heavy grain suits low light or pushed material; delicate daylight scenes usually need a finer structure.

## Directing the AI

Apply random, frame-varying texture across the image, with coarser grain in deep shadows and finer grain in exposed highlights. Let color density fluctuate subtly without crawling around edges or changing object shapes. Preserve facial features and text readability beneath the texture. Keep grain scale consistent with the apparent format and shot size. In motion, every frame should carry a fresh pattern so the surface feels alive rather than like a static overlay.

## Common mistakes

- Using a fixed noise layer across every frame, making the grain look pinned to the screen.
- Applying equal grain density to highlights and shadows, which removes the exposure-responsive character of film texture.
- Choosing particles so large that fine facial features and material detail become difficult to read.

## Sources

- Inventing Worlds and Characters: Effects

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

- [sepia-tone](sepia-tone.md)
- [desaturation](desaturation.md)
- [cinema-verite](cinema-verite.md)
- [color-grading](color-grading.md)
- [bokeh](bokeh.md)
- [forced-perspective](forced-perspective.md)
- [lens-distortion](lens-distortion.md)
- [morphing](morphing.md)

