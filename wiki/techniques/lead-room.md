# "Lead Room Prompt for AI Image & Video"

`lead-room` · Composition · level basic

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Lead room composition with [Subject] positioned on one side of the frame with generous empty space in the direction of their gaze or movement, the open space suggesting possibility and destination, the satisfying rightness of proper lead room creating visual momentum, shot on a 50mm lens, the composition feeling natural and kinetically forward
```

Empty space in front of a moving subject or in the direction they're looking, giving the subject visual breathing room and implying destination or intent. Lead room is one of the fundamental principles of shot composition — violating it deliberately creates tension and unease, as the Coen Brothers and David Fincher sometimes do in thriller sequences. Denis Villeneuve uses generous lead room in "Arrival" to suggest the vastness of the unknown that Amy Adams's character faces. Breaking the convention — placing a character at the leading edge of the frame with nothing ahead — immediately signals…

**When to use.** Lead room is essential when a subject looks, walks, drives, or moves toward one side of the frame. Space ahead gives that action somewhere to go and lets the audience anticipate a destination, person, or threat. Use generous room for possibility and forward momentum. Remove it deliberately when the character should feel blocked, pursued, or trapped against the edge. The technique must follow actu…

**Directing the AI.** Place the moving or looking subject on the side opposite their direction, leaving a larger open field ahead of the eyes or motion. Keep the destination readable through environment, light, or framing, even if nothing has entered yet. Reduce trailing space behind the subject without crowding them. For video, pan or track at a speed that preserves the open area. If tension requires breaking the rule, pin the subject near the leading edge and make the absence of room unmistakable.

**Common mistakes.**
- Leaving empty space behind a moving subject while compressing the area ahead, making the frame feel visually backward.
- Following body orientation instead of eye direction, which can create lead room on the wrong side of a glance.
- Recentering the subject continuously during a tracking shot, erasing the forward space that communicates destination and momentum.

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
| declared | `space-camera-moves` | camera | 150 | `drone-dive-landing` |
| declared | `space-camera-moves` | camera | 150 | `exploded-view` |

```
python platform/query.py technique-motions lead-room
```

## Sources

- Rules of Shot Composition in Film

## Related techniques

- [('tracking-shot', 'tracking-shot')](('tracking-shot', 'tracking-shot').md)
- [('pan-shot', 'pan-shot')](('pan-shot', 'pan-shot').md)
- [('rule-of-thirds', 'rule-of-thirds')](('rule-of-thirds', 'rule-of-thirds').md)
- [('symmetry', 'symmetry')](('symmetry', 'symmetry').md)
- [('leading-lines', 'leading-lines')](('leading-lines', 'leading-lines').md)
- [('framing-within-frame', 'framing-within-frame')](('framing-within-frame', 'framing-within-frame').md)
- [('negative-space', 'negative-space')](('negative-space', 'negative-space').md)
- [('shallow-focus', 'shallow-focus')](('shallow-focus', 'shallow-focus').md)
- [('deep-focus', 'deep-focus')](('deep-focus', 'deep-focus').md)
