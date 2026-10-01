# "Chiaroscuro Prompt for AI Image & Video"

`chiaroscuro` · Lighting · level advanced

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Chiaroscuro lighting on [Subject] with a single candle or flame as the only source, warm amber light painting face and hands while everything beyond arm's reach vanishes into absolute blackness, the contrast ratio approaching infinity, shot to emulate oil painting with a fast 50mm lens wide open, the Caravaggio-meets-Gordon Willis treatment of light as a moral force that reveals and conceals in equal measure
```

An extreme contrast between light and dark, inspired by Renaissance painting, creating deeply sculpted, painterly images with rich shadows and selective illumination. Directly descended from Caravaggio's revolutionary use of tenebrism in paintings like "The Calling of Saint Matthew," chiaroscuro entered cinema through German Expressionism and was perfected by Gordon Willis in "The Godfather" — his overhead toplight leaving Brando's eye sockets in impenetrable shadow became one of the most imitated looks in film history. Vittorio Storaro brought painterly chiaroscuro to "Apocalypse Now," and B…

**When to use.** Choose chiaroscuro when light and darkness should feel symbolic as well as descriptive. A face emerging from blackness can express divided motives, secrecy, spiritual weight, danger, or revelation. The painterly contrast works for intimate portraits, historical interiors, crime, and solemn drama. It demands selective control: if every surface receives dramatic light, the frame loses the tension b…

**Directing the AI.** Use one candle, flame, or narrow warm source to paint the subject's face and hands while everything beyond immediate reach falls toward absolute black. Shape the light across planes rather than outlining the entire body. Let one eye or side of the face disappear if the emotional idea supports concealment. Preserve rich amber gradation in lit skin and fabric. Keep secondary sources absent or extremely weak so darkness remains a compositional mass.

**Common mistakes.**
- Lighting the background for visual interest, reducing the black field that gives selective illumination its painterly force.
- Using equal split lighting with no tonal gradation, producing a simple half-lit portrait instead of sculpted chiaroscuro.
- Adding several colored sources that fragment the moral clarity of one dominant relationship between light and dark.

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
python platform/query.py technique-motions chiaroscuro
```

## Sources

- Film Lighting

## Related techniques

- [('low-key-lighting', 'low-key-lighting')](('low-key-lighting', 'low-key-lighting').md)
- [('rembrandt-lighting', 'rembrandt-lighting')](('rembrandt-lighting', 'rembrandt-lighting').md)
- [('film-noir', 'film-noir')](('film-noir', 'film-noir').md)
- [('three-point-lighting', 'three-point-lighting')](('three-point-lighting', 'three-point-lighting').md)
- [('key-light', 'key-light')](('key-light', 'key-light').md)
- [('high-key-lighting', 'high-key-lighting')](('high-key-lighting', 'high-key-lighting').md)
- [('silhouette', 'silhouette')](('silhouette', 'silhouette').md)
- [('golden-hour', 'golden-hour')](('golden-hour', 'golden-hour').md)
- [('blue-hour', 'blue-hour')](('blue-hour', 'blue-hour').md)
