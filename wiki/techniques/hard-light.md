# "Hard Light Prompt for AI Image & Video"

`hard-light` · Lighting · level basic

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Hard light from a bare overhead source casting razor-sharp shadows on [Subject], defined shadow edges so crisp they look cut with a knife, every surface texture amplified by the raking illumination, shot on Kodak Double-X black and white stock for maximum contrast, a 35mm Zeiss Planar lens, the graphic severity of film noir where light itself becomes an instrument of pressure
```

Light from a small or distant source that creates sharp, well-defined shadows, adding texture, drama, and graphic quality that can be harsh and unflattering or strikingly bold. Film noir cinematographers like John Alton and Nicholas Musuraca built entire visual worlds from hard light, creating the razor-sharp shadows of venetian blinds and fedora brims. David Fincher and Darius Khondji used hard light sources in "Se7en" to create the grimy, punishing atmosphere of a city drowning in sin. The direct sunlight in Sergio Leone's Westerns functions as nature's hard light, carving faces into dramat…

**When to use.** Use hard light when sharp shadows and exposed texture should create pressure, heat, severity, or graphic style. A small source can carve faces, project window patterns, define dust, or make architecture feel unforgiving. It suits noir, Westerns, interrogation, and harsh daylight. Because it reveals every surface irregularity, choose it deliberately for skin and products rather than assuming stron…

**Directing the AI.** Place a small bare or distant source at a defined angle and demand crisp, clearly shaped shadow edges. Let raking light reveal pores, fabric, dust, walls, and metal while keeping the contrast strong. A monochrome or restrained palette can make the geometry more forceful. Name any projected shape, such as blinds, and align it with the source. Avoid broad diffusion, ambient fill, or several competing directions that would soften the graphic result.

**Common mistakes.**
- Adding large diffusion to the source, softening the edges until the defining hard-shadow quality disappears.
- Using several hard lights from unrelated angles, producing crossed shadows that make the scene visually incoherent.
- Ignoring how raking light reveals skin and surface flaws, creating harsh detail where the subject needed restraint.

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
| declared | `fracture` | opening | 156 | `fracture` |

```
python platform/query.py technique-motions hard-light
```

## Sources

- Film Lighting

## Related techniques

- [('soft-light', 'soft-light')](('soft-light', 'soft-light').md)
- [('low-key-lighting', 'low-key-lighting')](('low-key-lighting', 'low-key-lighting').md)
- [('gobo-lighting', 'gobo-lighting')](('gobo-lighting', 'gobo-lighting').md)
- [('three-point-lighting', 'three-point-lighting')](('three-point-lighting', 'three-point-lighting').md)
- [('key-light', 'key-light')](('key-light', 'key-light').md)
- [('high-key-lighting', 'high-key-lighting')](('high-key-lighting', 'high-key-lighting').md)
- [('chiaroscuro', 'chiaroscuro')](('chiaroscuro', 'chiaroscuro').md)
- [('rembrandt-lighting', 'rembrandt-lighting')](('rembrandt-lighting', 'rembrandt-lighting').md)
- [('silhouette', 'silhouette')](('silhouette', 'silhouette').md)
