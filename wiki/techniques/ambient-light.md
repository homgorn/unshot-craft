# "Ambient Light Prompt for AI Image & Video"

`ambient-light` · Lighting · level basic

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Ambient light only on [Subject], the existing institutional or natural illumination providing the sole source, no dramatic shadows or cinematic enhancement, the honest unmanipulated light of a real place at a real time, shot on a fast lens wide open to handle the lower light levels, documentary naturalism where the space itself determines the visual mood
```

The existing, non-directional light present in an environment before any additional lighting is added, the base layer of illumination that sets the overall brightness and mood. Frederick Wiseman's documentaries like "Titicut Follies" and "High School" rely entirely on ambient light to maintain observational authenticity. The Dardenne brothers shoot their fiction films in ambient conditions to preserve documentary realism. Understanding and working with ambient light — the blue fill of an overcast sky, the warm glow of an office space, the green tint of a forest canopy — is the foundation upon…

**When to use.** Choose ambient light when the location's existing brightness and color should define the scene before any dramatic intervention. It suits documentary observation, institutional spaces, overcast exteriors, offices, forests, and other environments with broad non-directional illumination. Ambient light can make a frame feel immediate and unperformed, but it also exposes the space's natural tint and…

**Directing the AI.** Describe the environment as the source: cool overcast sky, warm office ceiling glow, or green light filtered through a canopy. Keep illumination broad and low in directionality, with restrained contrast and no unexplained rim or spotlight. Allow slight color contamination and uneven exposure where the real space would produce it. Maintain readable detail without turning the scene glossy. For video, let subjects move through the existing brightness pattern rather than carrying a perfectly shaped…

**Common mistakes.**
- Adding dramatic key and rim lights while calling the result ambient, which contradicts the technique's environmental base layer.
- Neutralizing every location tint, removing the blue, green, or warm cast that makes the existing light specific.
- Making ambient illumination perfectly uniform, even where walls, ceilings, windows, or foliage should create visible variation.

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
| declared | `brand-ink-open` | opening | 83 | `brand-ink-open` |

```
python platform/query.py technique-motions ambient-light
```

## Sources

- Film Lighting

## Related techniques

- [('available-light', 'available-light')](('available-light', 'available-light').md)
- [('practical-lighting', 'practical-lighting')](('practical-lighting', 'practical-lighting').md)
- [('cinema-verite', 'cinema-verite')](('cinema-verite', 'cinema-verite').md)
- [('three-point-lighting', 'three-point-lighting')](('three-point-lighting', 'three-point-lighting').md)
- [('key-light', 'key-light')](('key-light', 'key-light').md)
- [('high-key-lighting', 'high-key-lighting')](('high-key-lighting', 'high-key-lighting').md)
- [('low-key-lighting', 'low-key-lighting')](('low-key-lighting', 'low-key-lighting').md)
- [('chiaroscuro', 'chiaroscuro')](('chiaroscuro', 'chiaroscuro').md)
- [('rembrandt-lighting', 'rembrandt-lighting')](('rembrandt-lighting', 'rembrandt-lighting').md)
