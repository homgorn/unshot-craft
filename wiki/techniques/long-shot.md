# "Long Shot Prompt for AI Image & Video"

`long-shot` · Camera Work · level basic

Reference video: `media/long-shot.mp4`

## Prompt (verbatim, `[Subject]` intact)

```
Long shot of [Subject] with the full figure visible from head to foot, the scale of the environment dwarfing the human figure while the figure's posture radiates quiet authority, shot on 65mm large format with a 50mm lens, rich Technicolor-inspired warm palette, the mythic framing of classic cinema
```

Shows the subject's full body within their environment, balancing character and setting while establishing spatial relationships and keeping the subject identifiable. John Ford used the long shot to place his characters within the monumental landscapes of Monument Valley in "The Searchers," making John Wayne both heroic and dwarfed by nature. Akira Kurosawa's long shots in "Seven Samurai" choreograph entire battle sequences with balletic spatial clarity, and Andrea Arnold employs long shots in "American Honey" to embed her characters in the vast, indifferent American landscape.

**When to use.** Choose a long shot when the audience needs the subject's full body and enough environment to understand movement, distance, or social position. It suits entrances, confrontations, dance, travel, and action blocking where posture tells part of the story. The person remains identifiable, unlike an extreme long shot. Move closer when facial nuance outweighs gesture, or wider when the landscape must…

**Directing the AI.** Frame the subject from head to foot with intentional space above, below, and along their direction of movement. Let the environment remain substantial but subordinate to readable posture and silhouette. Use a natural perspective with deep enough focus to describe the setting, warm earth tones, and one clear line linking character to landscape. For video, preserve the full body through the action rather than cropping feet as the person approaches.

**Common mistakes.**
- Cropping the feet or head during movement, which quietly converts the intended framing into an awkward medium-long view.
- Allowing the landscape to dwarf the figure so completely that the result becomes an extreme long shot.
- Using shallow focus that erases the environmental relationship the wider framing was chosen to establish.

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
python platform/query.py technique-motions long-shot
```

## Sources

- 50+ Types of Camera Shots, Angles, and Techniques

## Related techniques

- [('extreme-long-shot', 'extreme-long-shot')](('extreme-long-shot', 'extreme-long-shot').md)
- [('cowboy-shot', 'cowboy-shot')](('cowboy-shot', 'cowboy-shot').md)
- [('deep-focus', 'deep-focus')](('deep-focus', 'deep-focus').md)
- [('aerial-shot', 'aerial-shot')](('aerial-shot', 'aerial-shot').md)
- [('birds-eye-view', 'birds-eye-view')](('birds-eye-view', 'birds-eye-view').md)
- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('dutch-angle', 'dutch-angle')](('dutch-angle', 'dutch-angle').md)
- [('dolly-shot', 'dolly-shot')](('dolly-shot', 'dolly-shot').md)
- [('establishing-shot', 'establishing-shot')](('establishing-shot', 'establishing-shot').md)
