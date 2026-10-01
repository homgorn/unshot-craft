# "Reaction Shot Prompt for AI Image & Video"

`reaction-shot` · Editing · level basic

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Reaction shot close-up of [Subject] capturing the exact moment of emotional impact, the eyes widening, jaw muscles clenching, every micro-expression playing across the face in three seconds, soft directional light illuminating every subtle muscular change, shot on an 85mm lens with eyes along the upper third, the Spielberg technique of making the audience feel an event through its reflection on a human face
```

A cut to a character's facial response to an event, dialogue, or revelation — often more powerful than showing the action itself, as it lets the audience experience the emotional impact. Spielberg understands this deeply: in "Schindler's List," we often see Oskar Schindler's face reacting to horror rather than the horror itself, and the reaction is more devastating. Hitchcock said "the size of the close-up on a reaction shot should be directly proportional to the importance of the information." The Kuleshov Effect proves that the same neutral face takes on entirely different meanings based on…

**When to use.** Use a reaction shot when the audience should experience an event through its effect on a person rather than through spectacle alone. It is crucial for revelations, fear, grief, comedy, attraction, and shifts in power. The size and duration should match the importance of the information. Hold long enough for micro-expressions to unfold, but avoid explaining the feeling with exaggerated performance…

**Directing the AI.** Establish what the character sees or hears, then cut to a close view at the first instant of impact. Keep eye line consistent with the preceding shot and frame the eyes clearly. Direct a sequence of small physical changes: focus shift, tightened jaw, held breath, widened eyes, or a delayed blink. Let the response develop for several beats before cutting away. Preserve facial identity and lighting continuity, and avoid adding unrelated camera movement that competes with the performance.

**Common mistakes.**
- Showing the reaction before the triggering information, confusing cause and effect unless deliberate anticipation is the point.
- Pushing every facial feature into extreme expression, replacing specific emotional discovery with broad, unreadable melodrama.
- Breaking eye line or lighting continuity, making the close-up feel detached from the event and surrounding space.

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
| declared | `impact-feedback` | effects | — | `anime-impact` |
| declared | `impact-feedback` | effects | — | `hit-counter` |

```
python platform/query.py technique-motions reaction-shot
```

## Sources

- What Is Film Editing?

## Related techniques

- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('extreme-close-up', 'extreme-close-up')](('extreme-close-up', 'extreme-close-up').md)
- [('cutaway', 'cutaway')](('cutaway', 'cutaway').md)
- [('cross-cutting', 'cross-cutting')](('cross-cutting', 'cross-cutting').md)
- [('jump-cut', 'jump-cut')](('jump-cut', 'jump-cut').md)
- [('dissolve', 'dissolve')](('dissolve', 'dissolve').md)
- [('fade-in-out', 'fade-in-out')](('fade-in-out', 'fade-in-out').md)
- [('montage', 'montage')](('montage', 'montage').md)
- [('smash-cut', 'smash-cut')](('smash-cut', 'smash-cut').md)
