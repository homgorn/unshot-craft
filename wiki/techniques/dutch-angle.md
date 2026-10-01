# "Dutch Angle Prompt for AI Image & Video"

`dutch-angle` · Camera Work · level basic

Reference video: `media/dutch-angle.mp4`

## Prompt (verbatim, `[Subject]` intact)

```
[Subject] framed at a sharp 25-degree Dutch angle, vertical lines tilting diagonally across the frame, long distorted shadows, overhead lighting casting fractured geometric patterns, 35mm film grain, Zeiss Super Speed 25mm, anamorphic edge distortion
```

A shot where the camera is tilted on its roll axis, creating a diagonal horizon line to convey unease, disorientation, tension, or a character's disturbed psychological state. Carol Reed made the Dutch angle iconic in "The Third Man" (1949), tilting nearly every frame in the Vienna sewers to mirror the moral corruption of Harry Lime. Tim Burton adopted it as a signature style in "Batman" and "Edward Scissorhands," while Kenneth Branagh used it relentlessly in "Thor" to evoke the comic-book panels of Jack Kirby.

**When to use.** Use a Dutch angle when the world, character, or power relationship has slipped out of balance. The tilt should express a specific instability — paranoia, intoxication, danger, moral corruption — not simply make a frame look more cinematic.

**Directing the AI.** State the roll angle and preserve strong architectural or horizon lines so the tilt remains legible. Pair the canted frame with one emotional cause and a controlled lens choice. In video, keep the roll fixed unless the act of rotating the camera is itself the point; uncontrolled horizon drift reads as generation error rather than direction.

**Common mistakes.**
- Tilting a frame that has no strong vertical or horizontal references, making the technique visually disappear.
- Using the angle in every shot until disorientation becomes the visual baseline and loses meaning.
- Combining a Dutch angle with several unrelated distortions that obscure the intended psychological signal.

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
| declared | `fracture` | opening | 156 | `fracture` |
| declared | `steep-tilt-glide` | camera | 120 | `steep-tilt-glide` |

```
python platform/query.py technique-motions dutch-angle
```

## Sources

- Location, location, location: Vienna and The Third Man

## Related techniques

- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('dolly-shot', 'dolly-shot')](('dolly-shot', 'dolly-shot').md)
- [('rembrandt-lighting', 'rembrandt-lighting')](('rembrandt-lighting', 'rembrandt-lighting').md)
- [('aerial-shot', 'aerial-shot')](('aerial-shot', 'aerial-shot').md)
- [('birds-eye-view', 'birds-eye-view')](('birds-eye-view', 'birds-eye-view').md)
- [('establishing-shot', 'establishing-shot')](('establishing-shot', 'establishing-shot').md)
- [('extreme-close-up', 'extreme-close-up')](('extreme-close-up', 'extreme-close-up').md)
- [('extreme-long-shot', 'extreme-long-shot')](('extreme-long-shot', 'extreme-long-shot').md)
- [('eye-level-shot', 'eye-level-shot')](('eye-level-shot', 'eye-level-shot').md)
