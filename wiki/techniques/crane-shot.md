# "Crane Shot Prompt for AI Image & Video"

`crane-shot` · Camera Work · level advanced

Reference video: `media/crane-shot.mp4`

## Prompt (verbatim, `[Subject]` intact)

```
Crane shot beginning tight on [Subject] then sweeping upward and backward in a majestic arc to reveal the true surrounding scale, the individual becoming one element among many in a seamless vertical revelation, shot on ARRI Alexa 65 with a 35mm Signature Prime, the mechanical grace of a Technocrane executing a precisely choreographed arc, golden hour light flooding horizontally
```

Camera mounted on a mechanical crane arm that sweeps upward, downward, or across a scene with majestic, controlled movement, often used for dramatic reveals or grand establishing moments. Orson Welles opened "Touch of Evil" with one of cinema's most famous crane shots — a continuous three-minute take following a car bomb through a Mexican border town. The final crane shot of "Gone with the Wind" pulling back to reveal hundreds of wounded soldiers remains one of Hollywood's most iconic images. Brian De Palma used elaborate crane work in "The Untouchables" for the Union Station staircase sequen…

**When to use.** Choose a crane shot when a scene needs a grand reveal that changes scale and perspective in one controlled movement. Rising from a person to a crowd, battlefield, building, or landscape can expose consequences beyond the intimate frame. Descending can isolate one figure from a larger world. The move suits openings, finales, and major transitions; it is excessive when a simple tilt or pull-out con…

**Directing the AI.** Begin on a clearly framed subject, then sweep upward and backward along a smooth mechanical arc. Reveal new layers in sequence rather than exposing the full environment at once: nearby action, surrounding group, architecture, then horizon. Keep the subject's location traceable as scale expands. Use broad golden-hour light to bind the levels together and a wide lens that avoids severe distortion. The path should feel engineered, stable, and continuous, never like free-floating aerial footage.

**Common mistakes.**
- Revealing the whole setting in the first frame, leaving the crane movement without new visual information to uncover.
- Losing the original subject during ascent, which breaks the intended transition between individual and surrounding scale.
- Replacing the controlled arc with random airborne drift that reads as an aerial shot rather than crane movement.

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
| declared | `crane-rise-reveal` | opening | 20 | `crane-rise-reveal` |

```
python platform/query.py technique-motions crane-shot
```

## Sources

- 50+ Types of Camera Shots, Angles, and Techniques

## Related techniques

- [('pull-out', 'pull-out')](('pull-out', 'pull-out').md)
- [('aerial-shot', 'aerial-shot')](('aerial-shot', 'aerial-shot').md)
- [('tilt-shot', 'tilt-shot')](('tilt-shot', 'tilt-shot').md)
- [('birds-eye-view', 'birds-eye-view')](('birds-eye-view', 'birds-eye-view').md)
- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('dutch-angle', 'dutch-angle')](('dutch-angle', 'dutch-angle').md)
- [('dolly-shot', 'dolly-shot')](('dolly-shot', 'dolly-shot').md)
- [('establishing-shot', 'establishing-shot')](('establishing-shot', 'establishing-shot').md)
- [('extreme-close-up', 'extreme-close-up')](('extreme-close-up', 'extreme-close-up').md)
