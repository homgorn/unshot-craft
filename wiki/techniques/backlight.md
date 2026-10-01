# "Backlight Prompt for AI Image & Video"

`backlight` · Lighting · level basic

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Backlit [Subject] with brilliant rim of white-gold light tracing every contour, hair transformed into a luminous halo of individually backlit strands, atmospheric dust and particles lit up like a galaxy of floating stars, god rays streaming past the figure, shot on a Cooke S4 with gentle halation on the overexposed highlights, the ethereal separation of backlight turning form into something divine
```

Light positioned behind the subject, creating a rim of light around their edges that separates the subject from the background and adds a halo-like, ethereal quality. Emmanuel Lubezki is the modern master of backlighting, using natural backlight in "The Revenant" and "The Tree of Life" to create an almost divine luminosity around his subjects. Vittorio Storaro's backlighting in "The Last Emperor" gives Pu Yi a godlike glow, and Janusz Kamiński's aggressive backlighting in "Schindler's List" and "Saving Private Ryan" — sometimes called the "Kamiński look" — adds an otherworldly haze to traumat…

**When to use.** Backlight is right when a subject must separate from a dark or visually busy background, or when the scene needs an ethereal halo. It performs especially well with hair, smoke, dust, rain, translucent fabric, and atmospheric haze. Use it for arrivals, memory fragments, spiritual imagery, or silhouettes with readable edges. Because the source faces the lens, decide whether the front remains dark o…

**Directing the AI.** Position the strongest source behind the subject and slightly above frame level. Describe a white-gold rim tracing shoulders, hair, and profile while particles in the air catch narrow beams. Let highlights bloom gently, but keep edge shape intact rather than washing the whole frame. State whether the face stays silhouetted or receives restrained frontal detail. In motion, maintain convincing occlusion: the rim should disappear on edges blocked from the source and brighten as the subject turns t…

**Common mistakes.**
- Applying an even glowing outline around every edge, including surfaces the rear source could not physically reach.
- Overexposing the background and rim together until the subject loses its silhouette instead of gaining clear separation.
- Ignoring atmosphere and surface response, which turns potentially luminous light into a thin digital-looking stroke around the figure.

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

**Declared, not inferred.** These come from an explicit `styles:` list in `data/cinematic/<slug>.md`, authored in `platform/catalog/pairings.py`. Nothing here is matched by name similarity.

| kind | shot card | category | frames | style |
|---|---|---|---|---|
| declared | `spotlight-hero-card` | opening | 220 | `spotlight-hero-card` |

```
python platform/query.py technique-motions backlight
```

## Sources

- Film Lighting

## Related techniques

- [('silhouette', 'silhouette')](('silhouette', 'silhouette').md)
- [('edge-light', 'edge-light')](('edge-light', 'edge-light').md)
- [('lens-flare', 'lens-flare')](('lens-flare', 'lens-flare').md)
- [('three-point-lighting', 'three-point-lighting')](('three-point-lighting', 'three-point-lighting').md)
- [('key-light', 'key-light')](('key-light', 'key-light').md)
- [('high-key-lighting', 'high-key-lighting')](('high-key-lighting', 'high-key-lighting').md)
- [('low-key-lighting', 'low-key-lighting')](('low-key-lighting', 'low-key-lighting').md)
- [('chiaroscuro', 'chiaroscuro')](('chiaroscuro', 'chiaroscuro').md)
- [('rembrandt-lighting', 'rembrandt-lighting')](('rembrandt-lighting', 'rembrandt-lighting').md)
