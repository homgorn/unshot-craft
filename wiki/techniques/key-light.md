# "Key Light Prompt for AI Image & Video"

`key-light` · Lighting · level basic

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Strong directional key light from a single source illuminating [Subject], the light carving sharp shadows that define every contour, dust motes floating in the visible beam, the single-source authority establishing the entire mood, a Fresnel spotlight quality with defined beam edge, warm tungsten color temperature at 3200K against cool blue ambient shadow
```

The primary and brightest light source in a scene, whose position, intensity, and quality define the overall mood and establish the dominant direction of light and shadow. Gordon Willis, "the Prince of Darkness," used deliberately underexposed key lights in "The Godfather" to create the shadowy world of the Corleone family. Vittorio Storaro sculpted light as pure emotion in "Apocalypse Now" and "Last Tango in Paris." The placement and quality of the key light is the single most important creative decision in any lighting setup, shaping everything from film noir's harsh side-key to Lubezki's s…

**When to use.** Define the key light whenever one source must establish the scene's dominant visual logic. Its angle and hardness can make a face open, guarded, glamorous, threatening, or exhausted before secondary lights do anything. A clear key is vital in portraits and narrative scenes where viewers should understand where illumination comes from. It can stand alone or anchor a larger setup, but should never…

**Directing the AI.** Name the key as the brightest source and place it precisely relative to the subject, such as 45 degrees camera-left and slightly high. Describe whether its beam is hard or soft, where the nose and cheek shadows fall, and how rapidly illumination drops across the scene. A warm tungsten key against cooler ambient shadow creates readable color separation. Keep every secondary source dim enough that the key retains authority over form and mood.

**Common mistakes.**
- Calling several sources the key, which destroys the single dominant direction needed to sculpt the scene coherently.
- Specifying brightness without angle or quality, leaving facial shadows and material texture entirely uncontrolled.
- Allowing ambient illumination to overpower the key, making the stated primary source visually irrelevant.

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
python platform/query.py technique-motions key-light
```

## Sources

- Film Lighting

## Related techniques

- [('three-point-lighting', 'three-point-lighting')](('three-point-lighting', 'three-point-lighting').md)
- [('hard-light', 'hard-light')](('hard-light', 'hard-light').md)
- [('soft-light', 'soft-light')](('soft-light', 'soft-light').md)
- [('high-key-lighting', 'high-key-lighting')](('high-key-lighting', 'high-key-lighting').md)
- [('low-key-lighting', 'low-key-lighting')](('low-key-lighting', 'low-key-lighting').md)
- [('chiaroscuro', 'chiaroscuro')](('chiaroscuro', 'chiaroscuro').md)
- [('rembrandt-lighting', 'rembrandt-lighting')](('rembrandt-lighting', 'rembrandt-lighting').md)
- [('silhouette', 'silhouette')](('silhouette', 'silhouette').md)
- [('golden-hour', 'golden-hour')](('golden-hour', 'golden-hour').md)
