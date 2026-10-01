# "Headroom Prompt for AI Image & Video"

`headroom` · Composition · level basic

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Proper headroom in a medium close-up of [Subject], eyes positioned along the upper-third line with a comfortable gap between the crown and the top of the frame, enough space to feel natural without wasting frame real estate, shot on a 85mm lens at T2.8, the invisible grammar of good camera operation
```

The space between the top of a subject's head and the top of the frame — too much feels disconnected, too little feels cramped, and proper headroom creates a natural, comfortable framing. Deliberately violating headroom conventions can be powerful: the Coen Brothers frequently cut off the top of heads or leave excessive headroom for comedic or unsettling effect in "A Serious Man" and "No Country for Old Men." Spike Jonze uses unconventional headroom in "Her" to create a feeling of emotional imbalance. Proper headroom is one of the first technical disciplines taught to camera operators and cin…

**When to use.** Headroom matters whenever a person occupies the frame, especially in interviews, dialogue, portraits, and moving coverage. A measured gap above the crown keeps the composition comfortable; too little pressure feels cramped, while too much space disconnects the face from the frame. Break the convention only when discomfort, comedy, or emotional imbalance needs to register. The correct amount also…

**Directing the AI.** Set the subject's eyes near the upper third and leave a controlled gap between the crown and top edge. Scale that gap to the shot size: tighter close-ups can crop hair deliberately, while medium shots need more breathing room. Keep the chin and shoulders balanced against the upper space. For video, maintain headroom as the subject stands, sits, or crosses frame by adjusting camera tilt smoothly; do not let the top edge bounce against the head.

**Common mistakes.**
- Leaving a large blank area above the head in a close portrait, making the subject appear to sink inside the frame.
- Clipping the crown by accident rather than using a confident, consistent close-up crop with clear visual intent.
- Allowing headroom to change wildly during movement, causing the camera to feel reactive instead of controlled.

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
python platform/query.py technique-motions headroom
```

## Sources

- Rules of Shot Composition in Film

## Related techniques

- [('medium-close-up', 'medium-close-up')](('medium-close-up', 'medium-close-up').md)
- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('rule-of-thirds', 'rule-of-thirds')](('rule-of-thirds', 'rule-of-thirds').md)
- [('symmetry', 'symmetry')](('symmetry', 'symmetry').md)
- [('leading-lines', 'leading-lines')](('leading-lines', 'leading-lines').md)
- [('framing-within-frame', 'framing-within-frame')](('framing-within-frame', 'framing-within-frame').md)
- [('negative-space', 'negative-space')](('negative-space', 'negative-space').md)
- [('shallow-focus', 'shallow-focus')](('shallow-focus', 'shallow-focus').md)
- [('deep-focus', 'deep-focus')](('deep-focus', 'deep-focus').md)
