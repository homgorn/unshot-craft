# "Tracking Shot Prompt for AI Image & Video"

`tracking-shot` · Camera Work · level intermediate

Reference video: `media/tracking-shot.mp4`

## Prompt (verbatim, `[Subject]` intact)

```
Lateral tracking shot following [Subject] at shoulder height, the camera keeping perfect pace on a parallel track, smooth parallax separation between foreground, mid-ground, and background layers, shot on 35mm Kodak Vision3 250D with a 40mm Panavision Primo lens, the rhythmic steady accompaniment of a camera that walks with its subject
```

The camera moves alongside, behind, or in front of a moving subject, maintaining a consistent spatial relationship to create a sense of journey, pursuit, or accompaniment. Jean-Luc Godard's famous lateral tracking shot in "Weekend" follows a traffic jam for nearly ten unbroken minutes. Andrei Tarkovsky's tracking shots in "Stalker" move with hypnotic slowness through the Zone, while Alfonso Cuarón and cinematographer Emmanuel Lubezki perfected the extended tracking shot in "Children of Men," where the camera follows characters through chaotic war zones without cutting for minutes at a time.

**When to use.** Use a tracking shot when movement through a place is part of the story: pursuit, discovery, routine, escape, or procession. Unlike a pan, the camera changes position. The move can make the audience accompany a subject, expose an environment progressively, or hold tension without cutting.

**Directing the AI.** Define whether the camera leads, follows, or travels beside the subject; then state height, distance, speed, and what remains locked in frame. Give the model foreground objects to cross and background depth to reveal. For longer generations, keep the action simple and continuous so identity, direction, and geography have fewer chances to drift.

**Common mistakes.**
- Writing "tracking shot" without saying where the camera is in relation to the subject.
- Confusing a fixed-axis pan with physical travel through the scene.
- Combining a complex camera path with multiple character actions and environment changes in one short generation.

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
| declared | `cursor-flyover` | camera | 180 | `cursor-flyover` |
| declared | `space-camera-moves` | camera | 150 | `drone-dive-landing` |
| declared | `space-camera-moves` | camera | 150 | `exploded-view` |

```
python platform/query.py technique-motions tracking-shot
```

## Sources

- What is a Tracking Shot? Definition and Examples

## Related techniques

- [('dolly-shot', 'dolly-shot')](('dolly-shot', 'dolly-shot').md)
- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('dutch-angle', 'dutch-angle')](('dutch-angle', 'dutch-angle').md)
- [('aerial-shot', 'aerial-shot')](('aerial-shot', 'aerial-shot').md)
- [('birds-eye-view', 'birds-eye-view')](('birds-eye-view', 'birds-eye-view').md)
- [('establishing-shot', 'establishing-shot')](('establishing-shot', 'establishing-shot').md)
- [('extreme-close-up', 'extreme-close-up')](('extreme-close-up', 'extreme-close-up').md)
- [('extreme-long-shot', 'extreme-long-shot')](('extreme-long-shot', 'extreme-long-shot').md)
- [('eye-level-shot', 'eye-level-shot')](('eye-level-shot', 'eye-level-shot').md)
