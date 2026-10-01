# "Fade In/Out Prompt for AI Image & Video"

`fade-in-out` · Editing · level basic

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Fade to black from [Subject], the image gradually losing luminance over six seconds as the figure becomes shadow and the shadow becomes part of the darkness, the fade so gradual that the exact moment of disappearance is unidentifiable, the emotional weight of permanent conclusion, the visual equivalent of a long exhale
```

The image gradually appears from or disappears to black (or white) — fade to black signals an ending or major time passage while fade from black signals a new beginning or chapter. The Coen Brothers use long, slow fades to black as chapter markers in "No Country for Old Men," each fade feeling like a door closing permanently. Kubrick's fade to white at the end of "2001" suggests transcendence. Martin Scorsese uses the fade to black at the end of "Goodfellas" and "The Irishman" with devastating finality. The pace of the fade itself communicates meaning — a quick fade feels like a curtain dropp…

**When to use.** Fade in or out when the story needs a clear boundary rather than a direct visual connection between shots. A fade to black can close a chapter, suggest long passage, or let consciousness recede; a fade from black can establish a beginning or return. The duration carries meaning. Use a fast fade for decisive closure and a slow one for exhaustion, grief, or gradual disappearance.

**Directing the AI.** Choose whether the image enters from black, leaves into black, or uses white for a distinctly brighter transition. Set an exact duration and preserve the shot's composition while luminance changes evenly. For a slow fade, let details disappear in tonal order until the subject merges with darkness; for a fade in, reverse that emergence cleanly. Keep the final black or white hold long enough to register. Do not change subject shape or camera position during the transition unless separately direct…

**Common mistakes.**
- Treating a fade as a default scene change, weakening the strong sense of chapter, ending, or passage it communicates.
- Changing exposure unevenly across objects, making the transition look like lighting failure rather than the entire image receding.
- Cutting away before full black has time to register, reducing the emotional closure and structural pause.

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
| declared | `chip-grid-single-select-blackout` | interaction | 150 | `chip-grid-single-select-blackout` |

```
python platform/query.py technique-motions fade-in-out
```

## Sources

- What Is Film Editing?

## Related techniques

- [('dissolve', 'dissolve')](('dissolve', 'dissolve').md)
- [('iris-transition', 'iris-transition')](('iris-transition', 'iris-transition').md)
- [('flashback', 'flashback')](('flashback', 'flashback').md)
- [('cross-cutting', 'cross-cutting')](('cross-cutting', 'cross-cutting').md)
- [('jump-cut', 'jump-cut')](('jump-cut', 'jump-cut').md)
- [('montage', 'montage')](('montage', 'montage').md)
- [('smash-cut', 'smash-cut')](('smash-cut', 'smash-cut').md)
- [('long-take', 'long-take')](('long-take', 'long-take').md)
- [('freeze-frame', 'freeze-frame')](('freeze-frame', 'freeze-frame').md)
