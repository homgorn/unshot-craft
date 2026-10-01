# "Eye-Level Shot Prompt for AI Image & Video"

`eye-level-shot` · Camera Work · level basic

Reference video: `media/eye-level-shot.mp4`

## Prompt (verbatim, `[Subject]` intact)

```
Eye-level shot of [Subject] with the camera positioned exactly at their eye height creating a direct and equal relationship with the viewer, natural available light providing gentle directional illumination, no dramatic angles or manipulation, shot on 16mm film stock with gentle grain, naturalistic color palette, intimate documentary stillness
```

A neutral shot taken at the subject's eye height, the most natural and common camera angle, creating a sense of equality and objectivity between viewer and subject. Yasujiro Ozu famously placed his camera at a low eye-level (the "tatami shot") in films like "Tokyo Story," creating an intimate, respectful perspective that defined Japanese domestic cinema. The Dardenne brothers use persistent eye-level handheld work in "Rosetta" and "The Child" to maintain unflinching equality with their working-class subjects, never looking down on or up at them.

**When to use.** Choose eye level when the camera should meet a person without glorifying, diminishing, or judging them. It is the dependable angle for interviews, domestic scenes, observational drama, and direct exchanges where performance matters more than visual manipulation. Because it feels normal, it can also make unusual behavior more disturbing. Use another angle only when power, vulnerability, or spatial…

**Directing the AI.** Position the lens exactly at the subject's eye height and keep verticals neutral. Frame the person with a natural conversational distance, available directional light, gentle 16mm-style grain, and an unforced color palette. Avoid heroic upward lines or downward compression. Let posture, gaze, and small facial shifts carry the frame. In video, use minimal handheld breathing or a locked camera rather than conspicuous movement, preserving the equal relationship between viewer and subject.

**Common mistakes.**
- Placing the camera at chest or forehead height while calling it eye level, subtly changing the power relationship.
- Adding dramatic lens distortion or canted framing that contradicts the angle's neutral, observational purpose.
- Treating neutrality as visual emptiness instead of using gaze, posture, and available light to hold attention.

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
python platform/query.py technique-motions eye-level-shot
```

## Sources

- 50+ Types of Camera Shots, Angles, and Techniques

## Related techniques

- [('medium-shot', 'medium-shot')](('medium-shot', 'medium-shot').md)
- [('cinema-verite', 'cinema-verite')](('cinema-verite', 'cinema-verite').md)
- [('available-light', 'available-light')](('available-light', 'available-light').md)
- [('aerial-shot', 'aerial-shot')](('aerial-shot', 'aerial-shot').md)
- [('birds-eye-view', 'birds-eye-view')](('birds-eye-view', 'birds-eye-view').md)
- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('dutch-angle', 'dutch-angle')](('dutch-angle', 'dutch-angle').md)
- [('dolly-shot', 'dolly-shot')](('dolly-shot', 'dolly-shot').md)
- [('establishing-shot', 'establishing-shot')](('establishing-shot', 'establishing-shot').md)
