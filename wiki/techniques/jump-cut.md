# "Jump Cut Prompt for AI Image & Video"

`jump-cut` · Editing · level basic

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Jump cut sequence of [Subject] with the background and position shifting abruptly between cuts while the camera angle remains essentially the same, the jarring temporal discontinuity making time feel broken and reassembled, each cut a tiny violence against smooth continuity, shot on handheld 16mm with rough grain and blown-out highlights, the French New Wave rebellion against invisible editing
```

A cut between two sequential shots of the same subject from a similar angle, creating a jarring jump in time — once considered a mistake, now used intentionally for energy, anxiety, or time compression. Jean-Luc Godard made the jump cut famous in "Breathless" (1960), using it partly out of necessity to trim a too-long film and partly as a deliberate rejection of smooth Hollywood continuity. The technique became a signature of the French New Wave and has since been adopted by filmmakers from Guy Ritchie to Gus Van Sant. Darren Aronofsky uses rapid-fire jump cuts in "Requiem for a Dream" to con…

**When to use.** Use a jump cut when smooth continuity would hide the anxiety, speed, boredom, or fragmentation inside a moment. It can compress repeated action, expose missing time, or make a performance feel unstable. Keep camera angle and subject similar enough that the temporal jump reads clearly. The cut should feel intentionally abrupt, not like failed coverage. It works especially well in restless portrait…

**Directing the AI.** Lock a similar camera angle and framing across several sequential moments, then remove the connecting motion between them. Let the subject's pose, background position, or object state jump forward while the setup remains recognizably the same. Keep each discontinuity sharp, with no dissolve or smoothing. Vary interval length to shape rhythm without losing the pattern. Maintain identity, wardrobe, and location details so the audience reads broken time rather than unrelated replacement shots.

**Common mistakes.**
- Changing angle, lens, and location together, which reads as a conventional cut instead of a temporal jump.
- Smoothing the discontinuity with motion interpolation or dissolves, removing the jolt that gives the technique its character.
- Allowing the subject's identity or wardrobe to drift between cuts, turning intentional fragmentation into continuity failure.

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
| declared | `beat-cut-moves` | rhythm | 49 | `beat-cut-accelerando` |
| declared | `beat-cut-moves` | rhythm | 49 | `paparazzi-flash` |

```
python platform/query.py technique-motions jump-cut
```

## Sources

- What Is Film Editing?

## Related techniques

- [('french-new-wave', 'french-new-wave')](('french-new-wave', 'french-new-wave').md)
- [('montage', 'montage')](('montage', 'montage').md)
- [('fast-motion', 'fast-motion')](('fast-motion', 'fast-motion').md)
- [('cross-cutting', 'cross-cutting')](('cross-cutting', 'cross-cutting').md)
- [('dissolve', 'dissolve')](('dissolve', 'dissolve').md)
- [('fade-in-out', 'fade-in-out')](('fade-in-out', 'fade-in-out').md)
- [('smash-cut', 'smash-cut')](('smash-cut', 'smash-cut').md)
- [('long-take', 'long-take')](('long-take', 'long-take').md)
- [('freeze-frame', 'freeze-frame')](('freeze-frame', 'freeze-frame').md)
