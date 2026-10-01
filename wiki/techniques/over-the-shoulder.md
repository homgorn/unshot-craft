# "Over-the-Shoulder Prompt for AI Image & Video"

`over-the-shoulder` · Camera Work · level basic

Reference video: `media/over-the-shoulder.mp4`

## Prompt (verbatim, `[Subject]` intact)

```
Over-the-shoulder shot with the near figure's shoulder and jaw soft and dark in the foreground, [Subject] sharply in focus in the mid-ground, the spatial depth between the two figures loaded with tension, shot on a 65mm lens at T2 creating a narrow depth of field, rich chiaroscuro lighting with deep umber shadows and warm golden highlights
```

Shot framed from behind one character, looking past their shoulder at another, the standard coverage for dialogue that creates spatial relationships and a sense of being within the conversation. The shot/reverse-shot pattern using over-the-shoulder angles became the backbone of Hollywood dialogue coverage through the classical studio era. David Fincher meticulously calibrates the exact angle and depth of his OTS shots in "The Social Network" and "Zodiac" to control psychological tension. Wong Kar-wai subverts the technique in "In the Mood for Love," using tight over-the-shoulder framings to s…

**When to use.** Use over-the-shoulder framing to place the audience inside a conversation while preserving who faces whom. The near shoulder creates depth and makes the listener's presence felt even when attention rests on the speaker. It suits dialogue, interrogation, seduction, negotiation, and withheld reactions. Choose cleaner singles when isolation matters more; use a two-shot when both performances deserve…

**Directing the AI.** Place one character's shoulder, jaw, and back of head as a soft dark foreground shape occupying a controlled edge of frame. Hold the other character sharp in the mid-ground with their gaze aimed just beside the lens. Use a narrow depth of field and chiaroscuro to load the gap between them with tension. Keep screen direction consistent across reverse coverage. The foreground figure must remain recognizable without blocking the speaker's face or hands.

**Common mistakes.**
- Letting the foreground head cover the speaker's expression, turning spatial context into a large visual obstruction.
- Breaking eyeline direction between paired shots, which makes both characters appear to face the same side.
- Rendering both planes equally sharp when the scene needs focus to privilege the person currently carrying the beat.

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

```
python platform/query.py technique-motions over-the-shoulder
```

## Sources

- 50+ Types of Camera Shots, Angles, and Techniques

## Related techniques

- [('two-shot', 'two-shot')](('two-shot', 'two-shot').md)
- [('medium-close-up', 'medium-close-up')](('medium-close-up', 'medium-close-up').md)
- [('reaction-shot', 'reaction-shot')](('reaction-shot', 'reaction-shot').md)
- [('aerial-shot', 'aerial-shot')](('aerial-shot', 'aerial-shot').md)
- [('birds-eye-view', 'birds-eye-view')](('birds-eye-view', 'birds-eye-view').md)
- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('dutch-angle', 'dutch-angle')](('dutch-angle', 'dutch-angle').md)
- [('dolly-shot', 'dolly-shot')](('dolly-shot', 'dolly-shot').md)
- [('establishing-shot', 'establishing-shot')](('establishing-shot', 'establishing-shot').md)
