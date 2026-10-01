# "In Medias Res Prompt for AI Image & Video"

`in-medias-res` · Narrative · level basic

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
In medias res with [Subject] dropped without context into the middle of intense action already in progress, no exposition or setup, no explanation, the audience thrown into adrenaline and forced to piece together the story from fragments, handheld camera energy and desaturated color grade, the Tarantino-Nolan principle that starting in the middle makes the audience lean forward
```

Beginning the story in the middle of the action rather than from the chronological start, hooking the audience immediately and creating mystery about how we got here. The technique dates to Homer's Odyssey and has been a staple of cinema since film noir. Quentin Tarantino opens "Reservoir Dogs" in the aftermath of a heist gone wrong, and Christopher Nolan begins "The Dark Knight" mid-robbery. The Coen Brothers drop viewers into the middle of violent chaos in "No Country for Old Men." Sam Mendes opens "American Beauty" with Kevin Spacey narrating from beyond the grave, and Danny Boyle begins "…

**When to use.** Use in medias res when the opening needs immediate pressure, movement, or mystery. Start after the plan has failed, during the chase, or at the instant a relationship breaks, then let context emerge through behavior and consequences. It suits stories where discovery is part of the pleasure. Even without exposition, viewers need a concrete objective, threat, or question to orient their attention i…

**Directing the AI.** Open on action already underway: the subject running, hiding, arguing, escaping, or recovering from an unseen event. Use reactive handheld framing, compressed background information, and visible consequences such as damage, breathlessness, or scattered objects. Withhold names and explanations, but make the immediate stakes legible through direction of movement and character focus. Seed two or three contextual fragments that can be understood later. Do not pause the scene to explain how everyone…

**Common mistakes.**
- Withholding every point of orientation, turning deliberate mystery into a scene with no readable objective.
- Stopping the action for immediate exposition, which cancels the momentum created by the opening plunge.
- Staging generic chaos without specific consequences that hint at the unseen events preceding the scene.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

## Motion pairings

**Declared, not inferred.** These come from an explicit `styles:` list in `data/cinematic/<slug>.md`, authored in `platform/catalog/pairings.py`. Nothing here is matched by name similarity.

| kind | shot card | category | frames | style |
|---|---|---|---|---|
| declared | `beat-cut-moves` | rhythm | 49 | `beat-cut-accelerando` |
| declared | `beat-cut-moves` | rhythm | 49 | `paparazzi-flash` |

```
python platform/query.py technique-motions in-medias-res
```

## Sources

- How to Make a Short Film: An Introduction to Filmmaking

## Related techniques

- [('smash-cut', 'smash-cut')](('smash-cut', 'smash-cut').md)
- [('cliffhanger', 'cliffhanger')](('cliffhanger', 'cliffhanger').md)
- [('non-linear-narrative', 'non-linear-narrative')](('non-linear-narrative', 'non-linear-narrative').md)
- [('flashback', 'flashback')](('flashback', 'flashback').md)
- [('foreshadowing', 'foreshadowing')](('foreshadowing', 'foreshadowing').md)
- [('breaking-fourth-wall', 'breaking-fourth-wall')](('breaking-fourth-wall', 'breaking-fourth-wall').md)
- [('flashforward', 'flashforward')](('flashforward', 'flashforward').md)
- [('parallel-storylines', 'parallel-storylines')](('parallel-storylines', 'parallel-storylines').md)
- [('frame-narrative', 'frame-narrative')](('frame-narrative', 'frame-narrative').md)
