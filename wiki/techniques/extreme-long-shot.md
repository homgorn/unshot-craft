# "Extreme Long Shot Prompt for AI Image & Video"

`extreme-long-shot` · Camera Work · level basic

Reference video: `media/extreme-long-shot.mp4`

## Prompt (verbatim, `[Subject]` intact)

```
Extreme long shot of [Subject] barely visible against a vast landscape stretching to the horizon, a single long shadow the only vertical element in a perfectly horizontal world, sky gradient from pale white at the horizon to deep cerulean overhead, shot on large format 65mm film, infinite depth of field rendering everything sharp from feet to infinity, Lawrence of Arabia scale and desolation
```

A very wide shot where the subject appears small against a vast environment, emphasizing scale, isolation, or the overwhelming nature of the surroundings. David Lean defined the technique in "Lawrence of Arabia," where Peter O'Toole becomes a speck against infinite desert horizons, communicating both the grandeur and the punishing emptiness of the landscape. Terrence Malick uses extreme long shots in "The Thin Red Line" to dwarf soldiers against indifferent nature, and Chloé Zhao employed them throughout "Nomadland" to place Frances McDormand's van as a tiny vessel adrift in the American West.

**When to use.** Use an extreme long shot when the environment should overwhelm the person inside it. It suits desert crossings, isolated vehicles, battlefields, migration, wilderness, and moments when distance itself is the emotion. The subject may be tiny, but must remain compositionally discoverable. Choose this scale for grandeur, loneliness, or indifference; switch closer when gesture, identity, or dialogue…

**Directing the AI.** Make the subject a small but intentional mark against a horizon-spanning environment. Describe a dominant horizontal composition, immense negative space, and one long shadow or contrasting color that lets the figure register. Keep detail sharp from near ground to distant horizon, with a pale-to-cerulean sky gradient reinforcing depth. For moving footage, use a nearly static frame or a very slow lateral drift; rapid movement destroys the patient comparison between human scale and landscape.

**Common mistakes.**
- Making the subject so invisible that the frame reads only as landscape rather than a deliberate scale comparison.
- Using shallow depth of field, which collapses the vast environmental detail needed to communicate distance and isolation.
- Crowding the horizon with several competing focal points that weaken the lone figure's compositional importance.

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
python platform/query.py technique-motions extreme-long-shot
```

## Sources

- 50+ Types of Camera Shots, Angles, and Techniques

## Related techniques

- [('long-shot', 'long-shot')](('long-shot', 'long-shot').md)
- [('negative-space', 'negative-space')](('negative-space', 'negative-space').md)
- [('aerial-shot', 'aerial-shot')](('aerial-shot', 'aerial-shot').md)
- [('birds-eye-view', 'birds-eye-view')](('birds-eye-view', 'birds-eye-view').md)
- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('dutch-angle', 'dutch-angle')](('dutch-angle', 'dutch-angle').md)
- [('dolly-shot', 'dolly-shot')](('dolly-shot', 'dolly-shot').md)
- [('establishing-shot', 'establishing-shot')](('establishing-shot', 'establishing-shot').md)
- [('extreme-close-up', 'extreme-close-up')](('extreme-close-up', 'extreme-close-up').md)
