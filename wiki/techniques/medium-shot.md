# "Medium Shot Prompt for AI Image & Video"

`medium-shot` · Camera Work · level basic

Reference video: `media/medium-shot.mp4`

## Prompt (verbatim, `[Subject]` intact)

```
Medium shot of [Subject] framed from the waist up, the perfect conversational distance that reveals both facial expression and the eloquent language of hands, shot on a 50mm lens at T2.8, Kodak Vision3 200T with rich warm midtones
```

Frames the subject from roughly the waist up, the workhorse of dialogue scenes — close enough to read expressions but wide enough to capture body language and gestures. Howard Hawks built his entire directorial style around the medium shot in films like "His Girl Friday" and "The Big Sleep," trusting the perfect middle distance to convey rapid-fire dialogue and physical chemistry. Aaron Sorkin's walk-and-talk scenes in "The West Wing" rely on moving medium shots, and Sofia Coppola uses static medium shots in "Lost in Translation" to capture the quiet body language of disconnection.

**When to use.** The medium shot is the default when dialogue and physical behavior need equal attention. Waist-up framing keeps expressions readable while preserving hands, shoulders, posture, and some environmental context. Use it for conversations, walk-and-talks, demonstrations, and quiet character beats that do not need close-up intensity. Its familiarity is useful, but a scene built only from medium shots c…

**Directing the AI.** Frame the subject from roughly the waist upward and leave room for hands to enter naturally. Use a normal perspective around 50mm, moderate depth of field, and warm midtones that keep skin and clothing dimensional. Place enough background detail to locate the scene without competing with the performance. For video, allow gestures and small body shifts to remain inside frame; avoid automated cropping that tightens toward the face whenever the subject speaks.

**Common mistakes.**
- Cropping at the chest and losing the hands, which makes the frame behave more like a medium close-up.
- Leaving excessive empty space around one person, weakening the practical balance between expression and environment.
- Using shallow focus so extreme that every gesture crossing the narrow plane becomes distracting and soft.

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
| declared | `space-camera-moves` | camera | 150 | `drone-dive-landing` |
| declared | `space-camera-moves` | camera | 150 | `exploded-view` |
| declared | `spotlight-hero-card` | opening | 220 | `spotlight-hero-card` |

```
python platform/query.py technique-motions medium-shot
```

## Sources

- 50+ Types of Camera Shots, Angles, and Techniques

## Related techniques

- [('medium-close-up', 'medium-close-up')](('medium-close-up', 'medium-close-up').md)
- [('two-shot', 'two-shot')](('two-shot', 'two-shot').md)
- [('eye-level-shot', 'eye-level-shot')](('eye-level-shot', 'eye-level-shot').md)
- [('aerial-shot', 'aerial-shot')](('aerial-shot', 'aerial-shot').md)
- [('birds-eye-view', 'birds-eye-view')](('birds-eye-view', 'birds-eye-view').md)
- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('dutch-angle', 'dutch-angle')](('dutch-angle', 'dutch-angle').md)
- [('dolly-shot', 'dolly-shot')](('dolly-shot', 'dolly-shot').md)
- [('establishing-shot', 'establishing-shot')](('establishing-shot', 'establishing-shot').md)
