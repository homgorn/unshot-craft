# "Flashback Prompt for AI Image & Video"

`flashback` · Narrative · level basic

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Flashback scene with [Subject] rendered in slightly overexposed warm-shifted tones, the image softer than present-day as if viewed through the imperfect lens of recollection, the color palette pushed toward amber and gold, lens flares and halation giving the image dreamy luminous quality, Kodak Vision3 50D pushed and cross-processed for vintage nostalgic look, the Malick-Lubezki language of memory as golden light
```

A scene that takes the audience back to an earlier point in time, revealing backstory, providing context for present behavior, or recontextualizing what we thought we knew. "Citizen Kane" is structured entirely around flashbacks as reporters investigate Charles Foster Kane's life. Francis Ford Coppola's "The Godfather Part II" masterfully interweaves flashbacks of young Vito Corleone with the present-day story of his son Michael. Christopher Nolan uses fragmented flashbacks as a structural principle in "Memento," where the reversed chronology makes every flashback a revelation. Terrence Malic…

**When to use.** Use a flashback when past experience must explain present behavior, reveal missing context, or challenge what the audience assumed. It works best when the return to the past has a specific dramatic purpose rather than serving as an information dump. Sensory fragments can express unreliable or emotional memory, while a fuller scene can deliver concrete backstory. Give the audience a clear temporal…

**Directing the AI.** Distinguish the remembered scene with a controlled visual system: warmer amber light, softer contrast, slight overexposure, gentle halation, or selective grain. Keep faces and important actions readable beneath the treatment. Build the transition around a matching object, sound cue, gesture, or composition that links present and past. Let imperfections suggest recollection, but maintain spatial continuity within the memory. Return to the present on an image that shows why this past moment matte…

**Common mistakes.**
- Using warm color alone without a narrative anchor, making the flashback resemble a random grade change.
- Explaining backstory the present scene already communicates, which stalls momentum instead of deepening character.
- Softening every detail until actions and faces become vague, sacrificing comprehension for a generic dream look.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` | `camera_motion: pan_right | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: smooth_pan` | pika-1.5 | no |
| `runway_gen3` | `motion_brush: smooth_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: smooth_pan` | sora-1 | no |
| `veo2` | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

## Motion pairings

**Declared, not inferred.** These come from an explicit `styles:` list in `data/cinematic/<slug>.md`, authored in `platform/catalog/pairings.py`. Nothing here is matched by name similarity.

| kind | shot card | category | frames | style |
|---|---|---|---|---|
| declared | `shot-transitions` | transition | — | `black-card-transition` |
| declared | `shot-transitions` | transition | — | `dark-tunnel-transition` |
| declared | `shot-transitions` | transition | — | `focus-handoff-transition` |
| declared | `shot-transitions` | transition | — | `mask-wipe-real` |
| declared | `shot-transitions` | transition | — | `portal-wipe-v2` |
| declared | `shot-transitions` | transition | — | `whip-brake-real` |
| declared | `shot-transitions` | transition | — | `whip-pan-real` |

```
python platform/query.py technique-motions flashback
```

## Sources

- How to Make a Short Film: An Introduction to Filmmaking

## Related techniques

- [('flashforward', 'flashforward')](('flashforward', 'flashforward').md)
- [('dissolve', 'dissolve')](('dissolve', 'dissolve').md)
- [('voiceover-narration', 'voiceover-narration')](('voiceover-narration', 'voiceover-narration').md)
- [('foreshadowing', 'foreshadowing')](('foreshadowing', 'foreshadowing').md)
- [('breaking-fourth-wall', 'breaking-fourth-wall')](('breaking-fourth-wall', 'breaking-fourth-wall').md)
- [('in-medias-res', 'in-medias-res')](('in-medias-res', 'in-medias-res').md)
- [('cliffhanger', 'cliffhanger')](('cliffhanger', 'cliffhanger').md)
- [('non-linear-narrative', 'non-linear-narrative')](('non-linear-narrative', 'non-linear-narrative').md)
- [('parallel-storylines', 'parallel-storylines')](('parallel-storylines', 'parallel-storylines').md)
