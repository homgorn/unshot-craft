# "Two-Shot Prompt for AI Image & Video"

`two-shot` · Camera Work · level basic

Reference video: `media/two-shot.mp4`

## Prompt (verbatim, `[Subject]` intact)

```
Two-shot of [Subject] framed together, their bodies creating complementary angles, the space between them charged with everything said and unsaid, shot on a 50mm Summilux at f/1.4 with gentle background blur, Kodak Portra 400 color rendition with soft warm midtones, the quiet eloquence of two figures in shared space
```

A shot framing exactly two subjects, showing their spatial and emotional relationship, essential for establishing dynamics between characters in conversation, confrontation, or intimacy. Billy Wilder was a master of the two-shot, using it in "The Apartment" and "Some Like It Hot" to capture the chemistry of his actors. Before Midnight director Richard Linklater builds entire films from two-shots of couples walking and talking, and Wong Kar-wai uses cramped two-shots in "In the Mood for Love" to convey forbidden intimacy within claustrophobic spaces.

**When to use.** Use a two-shot when the relationship between two people matters more than either individual performance alone. Shared framing exposes attraction, alliance, rivalry, distance, and changes in who controls the space. It works for conversation, walking dialogue, confrontation, and silent intimacy. Move to singles when isolation becomes the point, or to over-the-shoulder coverage when the exchange nee…

**Directing the AI.** Frame exactly two subjects with both faces and body angles legible. Use their spacing, height, orientation, and shared eyeline to express the relationship before dialogue begins. A normal lens and gentle background separation keep the scene intimate without erasing context. Leave the gap between them visible; it carries emotional weight. For video, choreograph who closes, crosses, or withdraws from that gap while keeping both figures inside the composition through the beat.

**Common mistakes.**
- Treating both figures as independent portraits, with no eyeline, gesture, or spatial tension connecting them.
- Cropping one subject at an awkward edge, making the second person feel accidental rather than compositionally equal.
- Using background blur so heavy that the shared environment no longer contributes to their relationship.

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
python platform/query.py technique-motions two-shot
```

## Sources

- 50+ Types of Camera Shots, Angles, and Techniques

## Related techniques

- [('three-shot', 'three-shot')](('three-shot', 'three-shot').md)
- [('over-the-shoulder', 'over-the-shoulder')](('over-the-shoulder', 'over-the-shoulder').md)
- [('medium-shot', 'medium-shot')](('medium-shot', 'medium-shot').md)
- [('aerial-shot', 'aerial-shot')](('aerial-shot', 'aerial-shot').md)
- [('birds-eye-view', 'birds-eye-view')](('birds-eye-view', 'birds-eye-view').md)
- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('dutch-angle', 'dutch-angle')](('dutch-angle', 'dutch-angle').md)
- [('dolly-shot', 'dolly-shot')](('dolly-shot', 'dolly-shot').md)
- [('establishing-shot', 'establishing-shot')](('establishing-shot', 'establishing-shot').md)
