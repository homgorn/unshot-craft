# "Steadicam Prompt for AI Image & Video"

`steadicam` · Camera Work · level advanced

Reference video: `media/steadicam.mp4`

## Prompt (verbatim, `[Subject]` intact)

```
Steadicam tracking shot floating smoothly behind [Subject] through shifting environments, the preternatural smoothness creating a floating predatory presence, shot on Arriflex 35BL with Zeiss Standard Speed lenses, the shifting light temperatures from warm tungsten through cool fluorescent creating a living color journey
```

A stabilized camera rig worn by the operator that produces smooth, floating movement while following subjects through complex environments, combining the fluidity of dolly work with the freedom of handheld. Invented by Garrett Brown, the Steadicam was first showcased in "Rocky" (1976) running up the Philadelphia Museum steps, then immortalized by Stanley Kubrick in "The Shining" — the relentless tracking shots through the Overlook Hotel's corridors remain the technique's definitive achievement. Martin Scorsese's Copacabana shot in "Goodfellas" and Paul Thomas Anderson's opening sequence in "B…

**When to use.** Use Steadicam movement when a character must travel through complex space without the vibration of handheld or the track-bound feel of a dolly. It suits corridor journeys, entrances, crowd navigation, and scenes where the camera becomes a calm companion or predator. The floating continuity can build immersion and anticipation. Avoid it when instability, abrupt impact, or absolute tripod stillness…

**Directing the AI.** Have the camera float behind, beside, or ahead of the subject at a constant human walking distance. Describe smooth turns, level horizons, gentle acceleration, and deliberate passage through doorways or changing environments. Let practical color temperatures shift naturally as the route moves from warm tungsten into cool fluorescent light. Keep footstep bounce suppressed but not robotic. Define the complete path and endpoint so the motion feels choreographed rather than like aimless gimbal foot…

**Common mistakes.**
- Making the move perfectly frictionless, which can feel disembodied instead of like a skilled operator moving through space.
- Failing to define the route, causing doors, walls, and extras to change unpredictably during the generated movement.
- Adding handheld jolts for excitement, undermining the smooth floating continuity that distinguishes Steadicam work.

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
python platform/query.py technique-motions steadicam
```

## Sources

- 50+ Types of Camera Shots, Angles, and Techniques

## Related techniques

- [('tracking-shot', 'tracking-shot')](('tracking-shot', 'tracking-shot').md)
- [('one-er', 'one-er')](('one-er', 'one-er').md)
- [('handheld-shot', 'handheld-shot')](('handheld-shot', 'handheld-shot').md)
- [('aerial-shot', 'aerial-shot')](('aerial-shot', 'aerial-shot').md)
- [('birds-eye-view', 'birds-eye-view')](('birds-eye-view', 'birds-eye-view').md)
- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('dutch-angle', 'dutch-angle')](('dutch-angle', 'dutch-angle').md)
- [('dolly-shot', 'dolly-shot')](('dolly-shot', 'dolly-shot').md)
- [('establishing-shot', 'establishing-shot')](('establishing-shot', 'establishing-shot').md)
