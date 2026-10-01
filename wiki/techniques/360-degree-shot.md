# "360-Degree Shot Prompt for AI Image & Video"

`360-degree-shot` · Camera Work · level advanced

Reference video: `media/360-degree-shot.mp4`

## Prompt (verbatim, `[Subject]` intact)

```
360-degree orbiting shot circling [Subject], the camera revolving slowly as the background becomes a continuous ribbon of light, the centripetal energy of the rotation making the world feel like it is spinning around the subject as its axis, shot on anamorphic 50mm with oval bokeh, warm tungsten tones on skin against cool ambient light, the romantic vertigo of circular motion
```

The camera orbits completely around the subject, creating a sense of circling energy, romantic intensity, or the feeling of time and space collapsing around a central moment. Brian De Palma used the 360-degree orbit in "Carlito's Way" as Carlito and Gail dance, the world spinning away until only they exist. The Wachowskis' "bullet time" in "The Matrix" took the orbital shot to a new technological dimension. Michael Bay, for all his excess, executes dynamic 360-degree hero shots that became action cinema clichés. Sam Mendes uses a slow orbit in "American Beauty" around Kevin Spacey's dinner ta…

**When to use.** Use a full orbit when the world should seem to spin around one emotional center. It can heighten romance, heroism, panic, reunion, or a moment when normal space falls away. The circular move also reveals every side of an environment while keeping one subject central. Reserve it for major beats; an orbit without changing emotional or spatial information quickly becomes a familiar spectacle.

**Directing the AI.** Keep the subject fixed near the axis while the camera travels through one complete, level circle around them. Maintain consistent distance, focus, and body scale as the background becomes a continuous ribbon of parallax and light. Use an anamorphic perspective with oval bokeh, warm skin, and cooler ambient surroundings. Choreograph the subject's gaze or embrace through the orbit, and define a clean return to the original angle rather than an endless rotational loop.

**Common mistakes.**
- Rotating the background without changing viewpoint, which looks like a spinning plate rather than a physical camera orbit.
- Changing radius throughout the move, causing the subject to lurch in scale and weakening the central-axis effect.
- Completing several circles with no evolving action, turning emotional emphasis into repetitive visual display.

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
| declared | `orbit-ring-title-open` | opening | 130 | `orbit-ring-title-open` |

```
python platform/query.py technique-motions 360-degree-shot
```

## Sources

- 50+ Types of Camera Shots, Angles, and Techniques

## Related techniques

- [('tracking-shot', 'tracking-shot')](('tracking-shot', 'tracking-shot').md)
- [('vertigo-effect', 'vertigo-effect')](('vertigo-effect', 'vertigo-effect').md)
- [('two-shot', 'two-shot')](('two-shot', 'two-shot').md)
- [('aerial-shot', 'aerial-shot')](('aerial-shot', 'aerial-shot').md)
- [('birds-eye-view', 'birds-eye-view')](('birds-eye-view', 'birds-eye-view').md)
- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('dutch-angle', 'dutch-angle')](('dutch-angle', 'dutch-angle').md)
- [('dolly-shot', 'dolly-shot')](('dolly-shot', 'dolly-shot').md)
- [('establishing-shot', 'establishing-shot')](('establishing-shot', 'establishing-shot').md)
