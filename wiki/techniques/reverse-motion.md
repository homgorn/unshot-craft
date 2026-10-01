# "Reverse Motion Prompt for AI Image & Video"

`reverse-motion` · Editing · level basic

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Reverse motion of [Subject] with the uncanny wrongness of reversed physics where entropy runs backward, fragments finding their original positions as if remembering where they belonged, shot originally on high-speed Phantom camera for smooth motion when reversed, the David Lynch surrealism of a world where time moves the wrong way
```

Footage played backwards, creating surreal, uncanny, or magical effects where broken things reassemble, fallen objects rise, and the familiar becomes alien. Jean Cocteau used reverse motion to create magical effects in "Orpheus" and "Beauty and the Beast" without any optical trickery. David Lynch employs reversed footage in "Twin Peaks" for the Red Room sequences, where actors learned their dialogue backwards so that when played in reverse, the speech sounds almost but not quite right — deeply uncanny. Christopher Nolan used extensive reverse motion in "Tenet" where entire action sequences pl…

**When to use.** Use reverse motion when ordinary physics should feel wrong: shattered material rebuilding, spilled liquid climbing upward, smoke returning to a source, or a fallen figure rising. It can signal magic, temporal disruption, surrealism, or unease. Choose actions with a clear irreversible direction in real life, because their reversal reads instantly. Subtle everyday movement may simply look awkward r…

**Directing the AI.** Begin from the completed aftermath, then choreograph every fragment, droplet, or particle traveling backward along a coherent path toward its original form. Keep trajectories smooth and collisions physically traceable, even though causality is reversed. Use steady framing and even illumination so the temporal wrongness remains the dominant effect. Preserve the subject's identity through the motion. Finish on a clean restored state that makes the reversal unmistakable.

**Common mistakes.**
- Reversing an action with no obvious directional logic, leaving the audience unsure whether anything unusual happened.
- Allowing fragments to appear from nowhere instead of retracing believable paths toward the restored object.
- Adding unrelated warping and color effects that distract from the simple uncanny power of backward physics.

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
| declared | `crash-zoom-punch` | camera | 11 | `crash-impact-real` |
| declared | `crash-zoom-punch` | camera | 11 | `crash-zoom-real` |

```
python platform/query.py technique-motions reverse-motion
```

## Sources

- What Is Film Editing?

## Related techniques

- [('morphing', 'morphing')](('morphing', 'morphing').md)
- [('time-lapse', 'time-lapse')](('time-lapse', 'time-lapse').md)
- [('surrealism', 'surrealism')](('surrealism', 'surrealism').md)
- [('cross-cutting', 'cross-cutting')](('cross-cutting', 'cross-cutting').md)
- [('jump-cut', 'jump-cut')](('jump-cut', 'jump-cut').md)
- [('dissolve', 'dissolve')](('dissolve', 'dissolve').md)
- [('fade-in-out', 'fade-in-out')](('fade-in-out', 'fade-in-out').md)
- [('montage', 'montage')](('montage', 'montage').md)
- [('smash-cut', 'smash-cut')](('smash-cut', 'smash-cut').md)
