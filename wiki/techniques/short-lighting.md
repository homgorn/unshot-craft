# "Short Lighting Prompt for AI Image & Video"

`short-lighting` · Lighting · level intermediate

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Short lighting on [Subject] with the key hitting the narrow far side, putting the broader camera-facing side in shadow, the small bright area creating an accent surrounded by darkness, shot on a fast 85mm lens at T1.4 with the background falling to black, film noir portrait psychology where what is hidden matters more than what is shown
```

The side of the face turned away from the camera receives the key light, putting the broader visible area in shadow, creating a slimming, more dramatic and moody portrait. Short lighting is preferred for dramatic and thriller genres where mystery and tension serve the story. Gordon Willis frequently used short lighting patterns in his collaborations with Woody Allen and Francis Ford Coppola. Film noir cinematographers defaulted to short lighting to create the shadowy, secretive faces of morally ambiguous characters. Roger Deakins uses short lighting in "Prisoners" to maintain a persistent sen…

**When to use.** Short lighting fits portraits that need mystery, tension, a slimmer face shape, or a sense that the character is withholding information. It works naturally in thrillers, noir, interrogations, and dramatic dialogue. The small far-side highlight becomes an accent surrounded by a larger field of shadow. Use it when concealment carries meaning, but protect enough eye and skin detail to keep the emot…

**Directing the AI.** Angle the subject away from camera and place the key on the narrow face plane turned farther from the lens. Keep the broad camera-facing cheek in shadow, with the bright far cheek acting as a controlled accent. Use minimal fill and let the background fall darker if the scene supports it. Preserve a catchlight or slight eye detail where needed. During movement, make the light pattern respond to head rotation instead of remaining frozen across the same facial regions.

**Common mistakes.**
- Illuminating the broad near cheek, which reverses the intended pattern and removes the slimming field of shadow.
- Crushing the entire camera-facing side to featureless black, losing the controlled detail that keeps the portrait readable.
- Letting the narrow highlight spread across the nose and front plane, weakening the concentrated dramatic accent.

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
python platform/query.py technique-motions short-lighting
```

## Sources

- Film Lighting

## Related techniques

- [('side-lighting', 'side-lighting')](('side-lighting', 'side-lighting').md)
- [('low-key-lighting', 'low-key-lighting')](('low-key-lighting', 'low-key-lighting').md)
- [('rembrandt-lighting', 'rembrandt-lighting')](('rembrandt-lighting', 'rembrandt-lighting').md)
- [('three-point-lighting', 'three-point-lighting')](('three-point-lighting', 'three-point-lighting').md)
- [('key-light', 'key-light')](('key-light', 'key-light').md)
- [('high-key-lighting', 'high-key-lighting')](('high-key-lighting', 'high-key-lighting').md)
- [('chiaroscuro', 'chiaroscuro')](('chiaroscuro', 'chiaroscuro').md)
- [('silhouette', 'silhouette')](('silhouette', 'silhouette').md)
- [('golden-hour', 'golden-hour')](('golden-hour', 'golden-hour').md)
