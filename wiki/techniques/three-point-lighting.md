# "Three-Point Lighting Prompt for AI Image & Video"

`three-point-lighting` · Lighting · level basic

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Classic three-point lighting on [Subject], the key light at 45 degrees creating defined shadow, a soft fill light gently opening the shadows, a warm-toned backlight rimming the edges with a thin golden halo, the balanced interplay sculpting the form into three dimensions, shot on medium format with an 80mm portrait lens at f/2.8, Kodak Portra color science with creamy skin tones and deep velvety blacks
```

The foundational lighting setup using three sources: a key light as the primary source, a fill light to soften shadows, and a backlight to separate the subject from the background. Developed during Hollywood's Golden Age by cinematographers like James Wong Howe and Gregg Toland, three-point lighting became the grammar of classical Hollywood cinema. It defined the glamorous look of stars from Garbo to Monroe and remains the starting point for all narrative lighting. Modern cinematographers like Roger Deakins and Janusz Kamiński build upon and deconstruct this foundation in every film they shoo…

**When to use.** Use three-point lighting when you need a flexible, readable foundation for portraits, interviews, dialogue, product work, or narrative coverage. The key establishes direction, fill controls contrast, and backlight separates the subject from the setting. It can look polished or dramatic depending on ratios. Treat it as a starting structure rather than a compulsory formula; some scenes are stronger…

**Directing the AI.** Place the key about 45 degrees to one side and above the subject, creating a clear modeled shadow. Add a softer, dimmer fill from the opposite side that opens detail without erasing shape. Position a warm backlight behind and above to trace shoulders and hair while avoiding lens flare. Describe the relative intensity and color of all three sources. Keep the background darker enough that separation remains visible without making the rim look pasted on.

**Common mistakes.**
- Making key and fill equally bright, which flattens the face and removes the setup's directional hierarchy.
- Using a backlight so strong that it creates a white cutout around hair and shoulders.
- Listing three lights without positions or ratios, leaving the resulting illumination arbitrary rather than intentionally structured.

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
python platform/query.py technique-motions three-point-lighting
```

## Sources

- Film Lighting

## Related techniques

- [('key-light', 'key-light')](('key-light', 'key-light').md)
- [('fill-light', 'fill-light')](('fill-light', 'fill-light').md)
- [('backlight', 'backlight')](('backlight', 'backlight').md)
- [('high-key-lighting', 'high-key-lighting')](('high-key-lighting', 'high-key-lighting').md)
- [('low-key-lighting', 'low-key-lighting')](('low-key-lighting', 'low-key-lighting').md)
- [('chiaroscuro', 'chiaroscuro')](('chiaroscuro', 'chiaroscuro').md)
- [('rembrandt-lighting', 'rembrandt-lighting')](('rembrandt-lighting', 'rembrandt-lighting').md)
- [('silhouette', 'silhouette')](('silhouette', 'silhouette').md)
- [('golden-hour', 'golden-hour')](('golden-hour', 'golden-hour').md)
