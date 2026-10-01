# "Film Grain Prompt for AI Image & Video"

`film-grain` · Visual Effects & Promptable FX · level basic

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Heavy film grain visible on [Subject], the organic random texture of high-speed 35mm film stock pushed two stops in processing, each frame alive with dancing silver halide crystals, the grain coarser in shadows and finer in highlights, Kodak Vision3 500T texture that Tarantino and Nolan insist on preserving, the organic soul of celluloid in an increasingly digital world
```

The visible texture of chemical film stock — random variations in density and color that give analog footage its organic, tactile character, often added digitally for warmth and nostalgia. Christopher Nolan and Quentin Tarantino remain committed to shooting on actual film stock, preserving the authentic grain of celluloid. Steven Soderbergh shot "Traffic" on different film stocks to differentiate storylines. Modern digital films frequently add film grain in post-production — David Fincher, despite shooting digitally, adds carefully calibrated grain to every frame. The resurgence of film grain…

**When to use.** Use film grain when pristine digital surfaces feel too sterile for the story, or when a period, documentary, intimate, or nostalgic mood benefits from tactile imperfection. Grain can unify composited elements and give shadows physical texture. Choose its strength to match the scene's light and emotional register. Heavy grain suits low light or pushed material; delicate daylight scenes usually nee…

**Directing the AI.** Apply random, frame-varying texture across the image, with coarser grain in deep shadows and finer grain in exposed highlights. Let color density fluctuate subtly without crawling around edges or changing object shapes. Preserve facial features and text readability beneath the texture. Keep grain scale consistent with the apparent format and shot size. In motion, every frame should carry a fresh pattern so the surface feels alive rather than like a static overlay.

**Common mistakes.**
- Using a fixed noise layer across every frame, making the grain look pinned to the screen.
- Applying equal grain density to highlights and shadows, which removes the exposure-responsive character of film texture.
- Choosing particles so large that fine facial features and material detail become difficult to read.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

## Motion pairings

**None declared.** No entry in `platform/catalog/pairings.py` maps this technique to a shot card, so this page does not claim one. Pairing is authored, never guessed — a wrong pairing hands a client a duration and an easing and looks researched.

## Sources

- Inventing Worlds and Characters: Effects

## Related techniques

- [('sepia-tone', 'sepia-tone')](('sepia-tone', 'sepia-tone').md)
- [('desaturation', 'desaturation')](('desaturation', 'desaturation').md)
- [('cinema-verite', 'cinema-verite')](('cinema-verite', 'cinema-verite').md)
- [('color-grading', 'color-grading')](('color-grading', 'color-grading').md)
- [('bokeh', 'bokeh')](('bokeh', 'bokeh').md)
- [('forced-perspective', 'forced-perspective')](('forced-perspective', 'forced-perspective').md)
- [('lens-distortion', 'lens-distortion')](('lens-distortion', 'lens-distortion').md)
- [('morphing', 'morphing')](('morphing', 'morphing').md)
