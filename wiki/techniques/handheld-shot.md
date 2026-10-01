# "Handheld Shot Prompt for AI Image & Video"

`handheld-shot` · Camera Work · level basic

Reference video: `media/handheld-shot.mp4`

## Prompt (verbatim, `[Subject]` intact)

```
Handheld camera following [Subject], natural shake and breathing motion in the frame, motion blur on fast-moving elements, the gritty texture of Super 16mm film pushed two stops in processing, desaturated color with blown-out highlights, the raw unfiltered energy of being inside the moment rather than observing it
```

Camera held by the operator without stabilization, resulting in natural shake and movement that creates raw immediacy, documentary realism, or frantic energy depending on context. John Cassavetes pioneered the emotional handheld style in "A Woman Under the Influence," where the camera's restlessness mirrors Gena Rowlands' unraveling psyche. Paul Greengrass brought visceral handheld energy to mainstream cinema with the "Bourne" trilogy, while the Dardenne brothers and Lars von Trier's Dogme 95 movement made handheld a philosophical commitment to unvarnished truth.

**When to use.** Reach for handheld movement when the camera must feel physically present inside an unstable moment. It can follow a character through conflict, capture documentary spontaneity, mirror panic, or make polished spaces feel exposed. The shake should reflect operator behavior and subject movement, not random vibration. Avoid it when spatial clarity, ceremonial scale, or controlled stillness matters mo…

**Directing the AI.** Describe a shoulder-held operator following close behind or beside the subject, with subtle breathing drift, imperfect reframing, and heavier jolts only during sudden movement. Allow motion blur on fast gestures and occasional clipped highlights, supported by gritty Super 16 texture and restrained color. Keep the subject recoverable after each shake. For a still image, imply handheld capture through slight motion smear and off-center timing rather than uniformly blurring the entire frame.

**Common mistakes.**
- Requesting constant violent shake, which feels synthetic and makes the subject impossible to track through the scene.
- Combining handheld language with perfectly centered, mechanically smooth framing that cancels the intended operator presence.
- Applying equal blur to every surface instead of tying motion artifacts to camera and subject movement.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` | **null** | kling-1.5 | no |
| `luma` | **null** | dream-machine | no |
| `mj61` | **null** | v6.1 | no |
| `pika15` | **null** | pika-1.5 | no |
| `runway_gen3` | **null** | gen-3-alpha | no |
| `sora` | **null** | sora-1 | no |
| `veo2` | **null** | veo-2 | no |

## Motion pairings

**Declared, not inferred.** These come from an explicit `styles:` list in `data/cinematic/<slug>.md`, authored in `platform/catalog/pairings.py`. Nothing here is matched by name similarity.

| kind | shot card | category | frames | style |
|---|---|---|---|---|
| declared | `graze-face-tour` | camera | 150 | `graze-face-tour` |

```
python platform/query.py technique-motions handheld-shot
```

## Sources

- 50+ Types of Camera Shots, Angles, and Techniques

## Related techniques

- [('found-footage', 'found-footage')](('found-footage', 'found-footage').md)
- [('cinema-verite', 'cinema-verite')](('cinema-verite', 'cinema-verite').md)
- [('steadicam', 'steadicam')](('steadicam', 'steadicam').md)
- [('aerial-shot', 'aerial-shot')](('aerial-shot', 'aerial-shot').md)
- [('birds-eye-view', 'birds-eye-view')](('birds-eye-view', 'birds-eye-view').md)
- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('dutch-angle', 'dutch-angle')](('dutch-angle', 'dutch-angle').md)
- [('dolly-shot', 'dolly-shot')](('dolly-shot', 'dolly-shot').md)
- [('establishing-shot', 'establishing-shot')](('establishing-shot', 'establishing-shot').md)
