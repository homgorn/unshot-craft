# "Cutaway Prompt for AI Image & Video"

`cutaway` · Editing · level basic

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Cutaway to [Subject] isolated in tight framing, the mundane object suddenly loaded with meaning by its context, shot on a 100mm macro lens with the background softly blurred, warm tungsten light, the Hitchcock principle that showing the ticking clock is more suspenseful than showing the argument
```

A brief cut to something outside the main action — a clock on the wall, a nervous hand, a landscape outside — adding context, creating pacing, or building parallel meaning. Yasujiro Ozu's famous "pillow shots" are extended cutaways to empty spaces, clotheslines, and chimneys that provide contemplative breathing room between scenes in "Tokyo Story." Hitchcock uses cutaways to ticking bombs and dripping faucets to build suspense. The Coen Brothers cut away to environmental details — a wood chipper, a wind-blown tumbleweed — that become darkly comedic commentary. Terrence Malick's cutaways to na…

**When to use.** Use a cutaway when the main action needs a breath, a clue, or a pressure point outside the immediate exchange. A clock can tighten suspense, an idle hand can expose anxiety, and an empty room can let emotion settle. It is especially useful between dialogue beats, during transitions, or whenever the environment should comment on the characters without speaking for them.

**Directing the AI.** First establish the main scene, then isolate one nearby object or environmental detail in tight framing. Keep its lighting, time of day, and production design consistent with the wider action. Reduce background information with shallow focus, but make the chosen detail unmistakable. Hold long enough for the audience to register its meaning, then return to the action. The cutaway should alter how the surrounding scene feels, not behave like decorative coverage.

**Common mistakes.**
- Choosing a random object with no emotional, narrative, or rhythmic connection to the surrounding scene.
- Changing the light or setting so sharply that the cutaway feels borrowed from another sequence.
- Holding on the detail after its meaning is clear, draining tension instead of sharpening it.

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
| declared | `circle-match-iris` | transition | 30 | `circle-match-iris` |

```
python platform/query.py technique-motions cutaway
```

## Sources

- What Is Film Editing?

## Related techniques

- [('insert-shot', 'insert-shot')](('insert-shot', 'insert-shot').md)
- [('reaction-shot', 'reaction-shot')](('reaction-shot', 'reaction-shot').md)
- [('foreshadowing', 'foreshadowing')](('foreshadowing', 'foreshadowing').md)
- [('cross-cutting', 'cross-cutting')](('cross-cutting', 'cross-cutting').md)
- [('jump-cut', 'jump-cut')](('jump-cut', 'jump-cut').md)
- [('dissolve', 'dissolve')](('dissolve', 'dissolve').md)
- [('fade-in-out', 'fade-in-out')](('fade-in-out', 'fade-in-out').md)
- [('montage', 'montage')](('montage', 'montage').md)
- [('smash-cut', 'smash-cut')](('smash-cut', 'smash-cut').md)
