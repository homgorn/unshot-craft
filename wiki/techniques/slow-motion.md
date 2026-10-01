# "Slow Motion Prompt for AI Image & Video"

`slow-motion` · Camera Work · level basic

Reference video: `media/slow-motion.mp4`

## Prompt (verbatim, `[Subject]` intact)

```
Slow motion capture at 240fps of [Subject] suspended in a single stretched moment, dust particles hanging motionless in shafts of light, every fine detail frozen in crystalline clarity, shot on Phantom Flex4K high-speed camera with Zeiss Master Prime glass, time stretched until a single second becomes an eternity of beauty
```

Footage captured at a higher frame rate than playback speed, stretching time to reveal details invisible at normal speed and amplifying impact, beauty, or emotional weight of a moment. Sam Peckinpah revolutionized screen violence with the slow-motion bloodbath of "The Wild Bunch," making destruction simultaneously beautiful and horrifying. The Wachowskis' "bullet time" in "The Matrix" became a cultural phenomenon, while Zack Snyder made speed ramping — shifting between slow and normal motion — his signature in "300." Wong Kar-wai uses slow motion with step-printing in "In the Mood for Love" t…

**When to use.** Apply slow motion when a brief action contains detail or emotional weight that normal speed would hide. Impacts, fabric movement, water, dust, a fall, or a tiny facial response can become readable and monumental. It can make violence beautiful, grief suspended, or athletic motion analytical. Reserve it for selected beats; stretching routine movement without contrast often drains urgency instead o…

**Directing the AI.** Choose one action and describe it as high-frame-rate capture played back slowly, with a clear beginning, peak, and release. Ask for crisp micro-detail in particles, hair, fabric, or debris while allowing natural directional blur on the fastest edges. Keep the camera move simpler than the subject action. State the perceived duration so one second expands meaningfully rather than freezing. Lighting should be strong enough to define each suspended element against the background.

**Common mistakes.**
- Slowing an action with no hidden detail or emotional turning point, making the sequence feel padded rather than heightened.
- Removing all motion blur and producing a brittle sequence of frozen poses instead of continuous high-speed capture.
- Combining extreme slow motion with elaborate camera movement that distracts from the physical event being examined.

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
| declared | `graze-face-tour` | camera | 150 | `graze-face-tour` |
| declared | `speed-ramp-freeze` | rhythm | 40 | `freeze-annotate-real` |
| declared | `speed-ramp-freeze` | rhythm | 40 | `speed-ramp-real` |

```
python platform/query.py technique-motions slow-motion
```

## Sources

- 50+ Types of Camera Shots, Angles, and Techniques

## Related techniques

- [('freeze-frame', 'freeze-frame')](('freeze-frame', 'freeze-frame').md)
- [('fast-motion', 'fast-motion')](('fast-motion', 'fast-motion').md)
- [('time-lapse', 'time-lapse')](('time-lapse', 'time-lapse').md)
- [('aerial-shot', 'aerial-shot')](('aerial-shot', 'aerial-shot').md)
- [('birds-eye-view', 'birds-eye-view')](('birds-eye-view', 'birds-eye-view').md)
- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('dutch-angle', 'dutch-angle')](('dutch-angle', 'dutch-angle').md)
- [('dolly-shot', 'dolly-shot')](('dolly-shot', 'dolly-shot').md)
- [('establishing-shot', 'establishing-shot')](('establishing-shot', 'establishing-shot').md)
