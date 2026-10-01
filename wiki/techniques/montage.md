# "Montage Prompt for AI Image & Video"

`montage` · Editing · level basic

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Montage sequence compressing time around [Subject], each shot shorter than the last as momentum accelerates, the editing rhythm itself building like a crescendo, culminating in a final sustained shot of completion, the cinematic time machine that compresses months into two minutes of escalating visual rhythm
```

A sequence of short shots edited together to compress time, convey information, or build emotional momentum — from training sequences to falling-in-love sequences, montage is cinema's time machine. Sergei Eisenstein theorized montage as cinema's unique art form in the 1920s, and his Odessa Steps sequence in "Battleship Potemkin" remains the most studied montage in film history. Rocky Balboa's training montage set to "Gonna Fly Now" defined the modern montage for a generation. Martin Scorsese uses montage in "Goodfellas" to compress years of criminal excess into exhilarating minutes, and Edgar…

**When to use.** Montage is built for change that matters but does not need to unfold in real time. Use it for training, travel, construction, research, falling in love, decline, or any process with visible milestones. Each shot should advance the state, not repeat the same information. Rhythm can accelerate toward completion or slow at setbacks. The sequence needs a clear beginning condition, meaningful progress…

**Directing the AI.** Define the process and list a sequence of distinct visual milestones. Start with longer shots that establish the task, then tighten duration as competence, urgency, or accumulation grows. Use repeated actions, matched framing, or recurring objects to show measurable change. Vary shot scale while preserving subject and environment continuity. Build toward one sustained payoff image rather than stopping randomly. Let music or action rhythm guide cuts, but ensure every beat remains legible without…

**Common mistakes.**
- Repeating attractive shots that show no new milestone, making the sequence energetic but narratively static.
- Accelerating cuts before the process is established, so the audience cannot understand what activity or change is being compressed.
- Ending on another brief fragment instead of a clear payoff that confirms completion, failure, or transformation.

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
python platform/query.py technique-motions montage
```

## Sources

- What Is Film Editing?

## Related techniques

- [('cross-cutting', 'cross-cutting')](('cross-cutting', 'cross-cutting').md)
- [('time-lapse', 'time-lapse')](('time-lapse', 'time-lapse').md)
- [('fast-motion', 'fast-motion')](('fast-motion', 'fast-motion').md)
- [('jump-cut', 'jump-cut')](('jump-cut', 'jump-cut').md)
- [('dissolve', 'dissolve')](('dissolve', 'dissolve').md)
- [('fade-in-out', 'fade-in-out')](('fade-in-out', 'fade-in-out').md)
- [('smash-cut', 'smash-cut')](('smash-cut', 'smash-cut').md)
- [('long-take', 'long-take')](('long-take', 'long-take').md)
- [('freeze-frame', 'freeze-frame')](('freeze-frame', 'freeze-frame').md)
