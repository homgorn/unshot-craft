# "Dolly Shot Prompt for AI Image & Video"

`dolly-shot` · Camera Work · level intermediate

Reference video: `media/dolly-shot.mp4`

## Prompt (verbatim, `[Subject]` intact)

```
Smooth dolly shot gliding toward [Subject], the camera at eye level moving with buttery precision on dolly track, parallax effect separating foreground elements from the mid-ground subject from far-ground details, shot on 35mm with Panavision Primo lenses, rich blacks and saturated warm tones, the elegant motion of precision dolly track work
```

A smooth camera movement where the entire camera physically moves toward, away from, or alongside the subject on a wheeled platform or track, creating an immersive sense of movement through space. Orson Welles used dolly shots to navigate the deep-focus interiors of "Citizen Kane," while Spike Lee invented his signature double-dolly shot — mounting both actor and camera on the same platform — to create a floating, surreal glide seen in "Do the Right Thing" and "25th Hour." Martin Scorsese's famous Copacabana shot in "Goodfellas" tracks Henry Hill through the back entrance of a nightclub in on…

**When to use.** Use a dolly-in when a realization, threat, or emotional detail needs to become unavoidable. Dolly out when context should overwhelm the subject or create emotional distance. Move alongside a character when the audience should travel with them rather than simply observe them.

**Directing the AI.** Describe physical camera travel, direction, speed, subject lock, and foreground-to-background separation. "Dolly toward" is more useful than "cinematic movement." Give the model visible layers for parallax — a foreground obstruction, the subject in the middle distance, and a readable background — so the move changes spatial relationships instead of behaving like a digital zoom.

**Common mistakes.**
- Calling for a dolly and a zoom at the same time without intentionally asking for a dolly zoom.
- Describing camera movement without foreground or background layers, leaving no parallax for the model to express.
- Stacking "smooth," "dynamic," "epic," and multiple conflicting camera directions instead of specifying one controlled move.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` | `camera_motion: pan_right | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: smooth_pan` | pika-1.5 | no |
| `runway_gen3` | `motion_brush: smooth_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: smooth_pan` | sora-1 | no |
| `veo2` | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

## Motion pairings

**Declared, not inferred.** These come from an explicit `styles:` list in `data/cinematic/<slug>.md`, authored in `platform/catalog/pairings.py`. Nothing here is matched by name similarity.

| kind | shot card | category | frames | style |
|---|---|---|---|---|
| declared | `crash-zoom-punch` | camera | 11 | `crash-impact-real` |
| declared | `crash-zoom-punch` | camera | 11 | `crash-zoom-real` |
| declared | `tension-camera-moves` | camera | 150 | `bullet-time-freeze-orbit` |
| declared | `tension-camera-moves` | camera | 150 | `dutch-roll-to-level` |
| declared | `tension-camera-moves` | camera | 150 | `pull-back-isolation` |
| declared | `tension-camera-moves` | camera | 150 | `slow-push-in` |

```
python platform/query.py technique-motions dolly-shot
```

## Sources

- The Dolly Shot: How To Create Powerful Shots With Simple Movement

## Related techniques

- [('tracking-shot', 'tracking-shot')](('tracking-shot', 'tracking-shot').md)
- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('dutch-angle', 'dutch-angle')](('dutch-angle', 'dutch-angle').md)
- [('aerial-shot', 'aerial-shot')](('aerial-shot', 'aerial-shot').md)
- [('birds-eye-view', 'birds-eye-view')](('birds-eye-view', 'birds-eye-view').md)
- [('establishing-shot', 'establishing-shot')](('establishing-shot', 'establishing-shot').md)
- [('extreme-close-up', 'extreme-close-up')](('extreme-close-up', 'extreme-close-up').md)
- [('extreme-long-shot', 'extreme-long-shot')](('extreme-long-shot', 'extreme-long-shot').md)
- [('eye-level-shot', 'eye-level-shot')](('eye-level-shot', 'eye-level-shot').md)
