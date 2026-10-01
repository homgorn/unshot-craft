# "Blue Hour Prompt for AI Image & Video"

`blue-hour` · Lighting · level intermediate

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Blue hour twilight twenty minutes after sunset enveloping [Subject], the sky a luminous deep cobalt blue glowing from within, warm amber artificial light sources contrasting with the pervasive blue atmosphere, shot on Alexa at high ISO with Cooke S4 glass rendering practical lights as soft warm glows, the contemplative melancholy of Michael Mann's visual language
```

The cool, diffused light just before sunrise or after sunset when the sky turns deep blue, creating a melancholic, contemplative, or mysterious atmosphere. Michael Mann is the master of blue hour photography, using the transitional twilight extensively in "Heat," "Collateral," and "Miami Vice" to create his signature cool urban melancholy. Janusz Kamiński shot the D-Day sequence in "Saving Private Ryan" during overcast blue-hour conditions for authenticity, and Wong Kar-wai's "Fallen Angels" uses Hong Kong's blue hour as an emotional blanket over its lonely characters.

**When to use.** Use blue hour for transitional scenes that need cool calm, loneliness, anticipation, or mystery without full darkness. The luminous sky keeps exterior detail visible while windows, streetlights, and vehicles begin to glow warm. It suits city arrivals, departures, reflective portraits, and quiet suspense. Keep it distinct from night by preserving cobalt ambient light and from sunset by removing di…

**Directing the AI.** Set the moment roughly twenty minutes after sunset or before sunrise, when the sky is deep cobalt but still luminous. Let cool ambient light wrap buildings and faces while warm amber practicals punctuate windows, signs, or vehicles. Use high sensitivity with soft halation around those sources, preserving detail in both sky and shadow. For video, hold the narrow twilight state consistently; do not let the sky flicker between daylight, sunset orange, and black night.

**Common mistakes.**
- Making the sky completely black, which turns the scene into night and removes blue hour's luminous transition.
- Adding direct orange sunlight even though the sun has already dropped below the horizon in the intended setup.
- Coloring skin and every object uniformly blue, instead of balancing cool ambience with selective warm practical sources.

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
| declared | `letterspace-materialize` | opening | 15 | `letterspace-materialize` |

```
python platform/query.py technique-motions blue-hour
```

## Sources

- Film Lighting

## Related techniques

- [('golden-hour', 'golden-hour')](('golden-hour', 'golden-hour').md)
- [('practical-lighting', 'practical-lighting')](('practical-lighting', 'practical-lighting').md)
- [('color-temperature', 'color-temperature')](('color-temperature', 'color-temperature').md)
- [('three-point-lighting', 'three-point-lighting')](('three-point-lighting', 'three-point-lighting').md)
- [('key-light', 'key-light')](('key-light', 'key-light').md)
- [('high-key-lighting', 'high-key-lighting')](('high-key-lighting', 'high-key-lighting').md)
- [('low-key-lighting', 'low-key-lighting')](('low-key-lighting', 'low-key-lighting').md)
- [('chiaroscuro', 'chiaroscuro')](('chiaroscuro', 'chiaroscuro').md)
- [('rembrandt-lighting', 'rembrandt-lighting')](('rembrandt-lighting', 'rembrandt-lighting').md)
