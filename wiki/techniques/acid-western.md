# "Acid Western Prompt for AI Image & Video"

`acid-western` · Film Genres · level advanced

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Acid western with [Subject] in a vast surreal desert landscape, the familiar Western iconography distorted through a psychedelic lens, oversaturated sky bleeding unnatural colors, dust and heat haze warping the horizon, Jodorowsky's mysticism meets Jarmusch's deadpan, a lone figure in an existential void that was once the frontier, 16mm film grain, the American myth turned hallucinatory
```

A psychedelic subversion of the Western genre that replaces manifest destiny optimism with hallucinatory existentialism. Alejandro Jodorowsky's "El Topo" (1970) invented the form — a mystical gunfighter journey through surreal desert landscapes. Jim Jarmusch's "Dead Man" (1995) deconstructed the genre with a dying accountant guided by a Native American named Nobody. The Coen Brothers' "No Country for Old Men" carries acid western DNA in its nihilistic desert violence. The genre takes the Western's vast landscapes and fills them with dread, absurdity, and metaphysical questioning.

**When to use.** Use Acid Western style when frontier myths need to dissolve into hallucination, nihilism, absurdity, or metaphysical doubt. A lone rider, desert town, gunfighter, or ritual can remain recognizable while the landscape becomes an existential void. It suits journeys without comforting destiny and violence without heroic certainty. Keep enough Western iconography to establish the genre before distort…

**Directing the AI.** Place a solitary subject in a vast desert with familiar Western clothing, weapons, or architecture, then corrupt the myth through oversaturated sky, unnatural horizon color, heat haze, and warped distance. Use gritty grain and long static observation rather than frantic effects. Let one surreal object or action appear without explanation. Keep the figure small against the land, with dread and absurdity sharing the frame. The frontier should feel emptied of promised meaning.

**Common mistakes.**
- Removing all recognizable Western elements, leaving psychedelic desert imagery without a genre being subverted.
- Using cheerful kaleidoscopic effects, which misses the form's dread, deadpan absurdity, and existential emptiness.
- Packing the landscape with symbols and visions instead of letting one impossible intrusion disturb the familiar myth.

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
| declared | `cel-flash-stomp` | typography | 30 | `cel-flash-stomp` |

```
python platform/query.py technique-motions acid-western
```

## Sources

- Genres: Where to Draw the Line?

## Related techniques

- [('spaghetti-western', 'spaghetti-western')](('spaghetti-western', 'spaghetti-western').md)
- [('surrealism', 'surrealism')](('surrealism', 'surrealism').md)
- [('extreme-long-shot', 'extreme-long-shot')](('extreme-long-shot', 'extreme-long-shot').md)
- [('film-noir', 'film-noir')](('film-noir', 'film-noir').md)
- [('german-expressionism', 'german-expressionism')](('german-expressionism', 'german-expressionism').md)
- [('cinema-verite', 'cinema-verite')](('cinema-verite', 'cinema-verite').md)
- [('french-new-wave', 'french-new-wave')](('french-new-wave', 'french-new-wave').md)
- [('found-footage', 'found-footage')](('found-footage', 'found-footage').md)
- [('italian-neorealism', 'italian-neorealism')](('italian-neorealism', 'italian-neorealism').md)
