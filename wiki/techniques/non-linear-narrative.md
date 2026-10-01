# "Non-Linear Narrative Prompt for AI Image & Video"

`non-linear-narrative` · Narrative · level advanced

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Non-linear narrative visualized with [Subject] existing simultaneously at different moments, each temporal fragment in its own distinct visual world with unique color science, the puzzle-like structure of Nolan and Tarantino made visual, the non-linear principle that chronology is a creative choice rather than an obligation
```

A story told out of chronological order — rearranging time to create mystery, thematic resonance, or a puzzle the audience assembles. Quentin Tarantino's "Pulp Fiction" made non-linear narrative a mainstream phenomenon, while Christopher Nolan's "Memento" pushed it to its logical extreme by running the entire film in reverse. Alejandro González Iñárritu's "21 Grams" fragments three timelines into a mosaic, and Denis Villeneuve's "Arrival" uses non-linear structure to redefine the audience's understanding of time itself. Gaspar Noé's "Irréversible" tells its story in reverse chronological orde…

**When to use.** Use a non-linear narrative when reordered time creates mystery, emotional contrast, or thematic resonance that chronology cannot provide. Place consequences before causes, revisit one event from different periods, or interleave temporal fragments that change one another's meaning. Every jump should contribute evidence. The structure demands strong anchors such as age, wardrobe, location, color, o…

**Directing the AI.** Define each time period with a distinct but related palette, lighting condition, costume state, and environmental detail. Repeat one subject or composition across periods to expose change. Arrange fragments around dramatic meaning rather than random chronology: consequence, cause, contradiction, revelation. Keep screen direction and identity consistent within each period. When moments overlap, show a clear visual bridge. The final sequence should reward reconstruction, with each temporal fragme…

**Common mistakes.**
- Reordering scenes arbitrarily without creating mystery, contrast, or a new relationship between cause and consequence.
- Giving every period identical styling, forcing viewers to guess when events occur from dialogue alone.
- Overloading each fragment with clues, making the structure feel like a puzzle interface instead of lived drama.

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
| declared | `circle-match-iris` | transition | 30 | `circle-match-iris` |

```
python platform/query.py technique-motions non-linear-narrative
```

## Sources

- How to Make a Short Film: An Introduction to Filmmaking

## Related techniques

- [('flashback', 'flashback')](('flashback', 'flashback').md)
- [('flashforward', 'flashforward')](('flashforward', 'flashforward').md)
- [('parallel-storylines', 'parallel-storylines')](('parallel-storylines', 'parallel-storylines').md)
- [('foreshadowing', 'foreshadowing')](('foreshadowing', 'foreshadowing').md)
- [('breaking-fourth-wall', 'breaking-fourth-wall')](('breaking-fourth-wall', 'breaking-fourth-wall').md)
- [('in-medias-res', 'in-medias-res')](('in-medias-res', 'in-medias-res').md)
- [('cliffhanger', 'cliffhanger')](('cliffhanger', 'cliffhanger').md)
- [('frame-narrative', 'frame-narrative')](('frame-narrative', 'frame-narrative').md)
- [('voiceover-narration', 'voiceover-narration')](('voiceover-narration', 'voiceover-narration').md)
