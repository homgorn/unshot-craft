# "Cosmic Horror Prompt for AI Image & Video"

`cosmic-horror` · Film Genres · level advanced

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Cosmic horror atmosphere with [Subject] dwarfed by something vast and incomprehensible at the edge of the frame, non-Euclidean geometry subtly wrong in the architecture, the Annihilation shimmer distorting organic forms, scale that makes the human figure irrelevant, deep shadow concealing shapes that should not exist, cold clinical lighting that reveals too much, the terror of understanding how small you are
```

A visual approach to the unknowable and incomprehensible — vast entities beyond human understanding, non-Euclidean geometry, and the terror of insignificance in an indifferent universe. Inspired by H.P. Lovecraft's literary work, the visual language was refined by John Carpenter's "The Thing" (1982) with its shapeshifting alien horror. Annihilation (2018) by Alex Garland brought cosmic horror to modern cinema with its shimmer-distorted landscapes. The genre's visual challenge is depicting what cannot be comprehended — using scale, distortion, and wrongness to suggest the incomprehensible.

**When to use.** Use cosmic horror when fear should come from incomprehensible scale, unstable reality, or the discovery that human concerns mean nothing to the larger universe. It suits alien landscapes, impossible architecture, transformations, and encounters that resist full interpretation. Show enough structure to imply a vast intelligence or force, but preserve uncertainty. A fully explained creature becomes…

**Directing the AI.** Frame the human subject as a tiny, readable figure against an immense structure or entity partly concealed at the edge of vision. Bend architecture into subtly non-Euclidean relationships, repeat forms at impossible scales, and distort organic matter with a restrained shimmer. Use cold clinical light to reveal disturbing detail while deep shadow withholds the whole. Keep perspective internally wrong but visually coherent. The image should make scale undeniable and comprehension impossible.

**Common mistakes.**
- Centering and fully lighting the entity, reducing incomprehensible presence to a conventional creature reveal.
- Using random tentacles without impossible scale, wrong geometry, or any challenge to human understanding.
- Making the human figure invisible, which removes the scale reference needed to communicate insignificance.

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
| declared | `fracture` | opening | 156 | `fracture` |

```
python platform/query.py technique-motions cosmic-horror
```

## Sources

- Genres: Where to Draw the Line?

## Related techniques

- [('surrealism', 'surrealism')](('surrealism', 'surrealism').md)
- [('negative-space', 'negative-space')](('negative-space', 'negative-space').md)
- [('found-footage', 'found-footage')](('found-footage', 'found-footage').md)
- [('film-noir', 'film-noir')](('film-noir', 'film-noir').md)
- [('german-expressionism', 'german-expressionism')](('german-expressionism', 'german-expressionism').md)
- [('cinema-verite', 'cinema-verite')](('cinema-verite', 'cinema-verite').md)
- [('french-new-wave', 'french-new-wave')](('french-new-wave', 'french-new-wave').md)
- [('spaghetti-western', 'spaghetti-western')](('spaghetti-western', 'spaghetti-western').md)
- [('italian-neorealism', 'italian-neorealism')](('italian-neorealism', 'italian-neorealism').md)
