# "Lens Distortion Prompt for AI Image & Video"

`lens-distortion` · Visual Effects & Promptable FX · level intermediate

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Lens distortion from a vintage anamorphic lens visible across [Subject], barrel distortion curving straight lines at frame edges into subtle arcs, oval-shaped bokeh, horizontal flare streaks, the edges softer and more swirled than the sharp center, chromatic aberration creating slight color fringing, the accumulated imperfections giving the image character that clinical modern lenses deliberately avoid
```

Optical aberrations from specific lenses that bend, stretch, or warp the image — wide-angle barrel distortion, anamorphic oval bokeh, or vintage lens flaring — each lens has a personality. Emmanuel Lubezki exploits wide-angle distortion in his work with Terrence Malick, using ultra-wide lenses that bend the edges of reality. Roger Deakins prefers Arri/Zeiss Master Primes for their clinical precision, while Robert Richardson often chooses older, imperfect glass for its character. The anamorphic distortion of Panavision C-series and E-series lenses — their signature flares, edge softness, and o…

**When to use.** Use lens distortion when optical imperfection should add personality, unease, intimacy, or period texture. Wide barrel distortion can make nearby faces confrontational, while anamorphic softness, oval bokeh, and horizontal flare can create expansive cinematic space. Match the aberration to a clear lens character and framing purpose. Distortion is less useful when architecture, products, or visual…

**Directing the AI.** Keep the central subject relatively sharp while curving straight lines near frame edges into subtle arcs. Add edge softness, mild chromatic fringing, oval background bokeh, and restrained horizontal flare from actual bright sources. Let perspective stretch objects closest to the lens, not distant forms at random. Preserve one coherent optical center across the shot. The imperfections should share a lens logic, with stronger aberration toward the perimeter and cleaner rendering near the middle.

**Common mistakes.**
- Warping the center and edges equally, making the image feel digitally melted rather than optically distorted.
- Adding flare without a bright source, which breaks the physical logic of the implied lens.
- Stacking barrel distortion, fringing, softness, and bokeh so heavily that the subject loses visual authority.

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

- [('bokeh', 'bokeh')](('bokeh', 'bokeh').md)
- [('lens-flare', 'lens-flare')](('lens-flare', 'lens-flare').md)
- [('dutch-angle', 'dutch-angle')](('dutch-angle', 'dutch-angle').md)
- [('color-grading', 'color-grading')](('color-grading', 'color-grading').md)
- [('desaturation', 'desaturation')](('desaturation', 'desaturation').md)
- [('sepia-tone', 'sepia-tone')](('sepia-tone', 'sepia-tone').md)
- [('film-grain', 'film-grain')](('film-grain', 'film-grain').md)
- [('forced-perspective', 'forced-perspective')](('forced-perspective', 'forced-perspective').md)
- [('morphing', 'morphing')](('morphing', 'morphing').md)
