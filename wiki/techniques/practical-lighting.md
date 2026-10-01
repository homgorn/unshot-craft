# "Practical Lighting Prompt for AI Image & Video"

`practical-lighting` · Lighting · level intermediate

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Practical lighting on [Subject] illuminated only by visible sources within the frame, each practical creating its own color world, the interplay of multiple color temperatures producing a rich layered chromatic atmosphere, no hidden movie lights, shot wide open at T1.3 on a Zeiss Super Speed to drink in every photon, the visual language of Christopher Doyle
```

Using visible light sources within the scene — lamps, candles, neon signs, TV screens — as the actual illumination, creating naturalistic, motivated lighting with rich atmosphere. Stanley Kubrick famously lit "Barry Lyndon" using only candles and natural window light, requiring specially modified NASA lenses. Wong Kar-wai and Christopher Doyle use neon signs and fluorescent tubes as practical sources in "Chungking Express" and "In the Mood for Love," turning Hong Kong's light pollution into visual poetry. Roger Deakins uses practicals masterfully in "Blade Runner 2049," letting in-scene holog…

**When to use.** Choose practical lighting when the sources should belong visibly to the world of the scene. Lamps, candles, televisions, fluorescent tubes, and neon signs can motivate color, direction, and atmosphere while making an interior feel lived-in. It works for naturalism and stylization alike. The visible fixtures must actually affect nearby surfaces; decorative bulbs that cast no corresponding light br…

**Directing the AI.** Name every visible source and assign it a local pool of illumination, color temperature, falloff, and affected surfaces. A warm lamp can shape one face while a cool television colors the shadow side and distant neon adds another layer. Keep brightness physically plausible and let areas between sources remain darker. Use a fast-lens look to retain low-light texture. For video, preserve each fixture's position and chromatic influence as characters move through the room.

**Common mistakes.**
- Showing visible lamps that cast no matching light or shadow, making them look like decorative props.
- Giving every practical equal brightness and reach, flattening the layered pools that create believable atmosphere.
- Adding an unexplained frontal beauty light that contradicts the claim that visible in-scene sources provide illumination.

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
| declared | `icon-field-colorize` | opening | 45 | `icon-field-colorize` |

```
python platform/query.py technique-motions practical-lighting
```

## Sources

- Film Lighting

## Related techniques

- [('motivated-lighting', 'motivated-lighting')](('motivated-lighting', 'motivated-lighting').md)
- [('available-light', 'available-light')](('available-light', 'available-light').md)
- [('color-temperature', 'color-temperature')](('color-temperature', 'color-temperature').md)
- [('three-point-lighting', 'three-point-lighting')](('three-point-lighting', 'three-point-lighting').md)
- [('key-light', 'key-light')](('key-light', 'key-light').md)
- [('high-key-lighting', 'high-key-lighting')](('high-key-lighting', 'high-key-lighting').md)
- [('low-key-lighting', 'low-key-lighting')](('low-key-lighting', 'low-key-lighting').md)
- [('chiaroscuro', 'chiaroscuro')](('chiaroscuro', 'chiaroscuro').md)
- [('rembrandt-lighting', 'rembrandt-lighting')](('rembrandt-lighting', 'rembrandt-lighting').md)
