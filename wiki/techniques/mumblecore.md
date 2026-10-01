# "Mumblecore Prompt for AI Image & Video"

`mumblecore` · Film Genres · level basic

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Mumblecore scene with [Subject] shot on what appears to be a consumer DSLR with available window light, the dialogue clearly improvised with interrupted sentences and awkward pauses, the framing functional rather than composed, the sound ambient and slightly echoey, the Bujalski-Swanberg aesthetic where lack of budget becomes the honesty of the image, naturalistic window light
```

Ultra-low-budget indie filmmaking focused on naturalistic dialogue, improvisation, and the awkwardness of young adult relationships — micro-budget intimacy as aesthetic. Andrew Bujalski's "Funny Ha Ha" (2002) is considered mumblecore's founding film, followed by the Duplass Brothers' "The Puffy Chair," Joe Swanberg's "Hannah Takes the Stairs," and Greta Gerwig's early acting work in the movement. The aesthetic defined by its limitations — consumer cameras, available light, non-professional audio — turned zero-budget necessity into a deliberate creative philosophy. Many mumblecore alumni went…

**When to use.** Use mumblecore for low-stakes situations carrying high emotional discomfort: uncertain relationships, stalled adulthood, shared apartments, and conversations where people interrupt, retreat, or say the wrong thing. Its modest visual scale keeps attention on behavior and pauses. The style suits small casts and real spaces. Avoid adding polished coverage or dramatic plot machinery that overwhelms t…

**Directing the AI.** Stage two or three people in a real apartment, kitchen, car, or neighborhood space with available window light and functional framing. Keep the camera handheld but calm, adjusting late when someone shifts position. Let dialogue overlap, sentences trail off, and pauses remain visible in posture and eye lines. Retain room echo and ambient sound. Avoid glamour lighting and perfect shot-reverse-shot symmetry. The scene should feel discovered around the performers, not engineered before them.

**Common mistakes.**
- Writing polished speeches for every character, removing the interruption, hesitation, and uncertainty central to the style.
- Using aggressive handheld shake during quiet conversation, which competes with subtle behavior rather than observing it.
- Lighting the room like a prestige drama, erasing the practical intimacy of available windows and fixtures.

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
| declared | `letterspace-materialize` | opening | 15 | `letterspace-materialize` |

```
python platform/query.py technique-motions mumblecore
```

## Sources

- Genres: Where to Draw the Line?

## Related techniques

- [('dogme-95', 'dogme-95')](('dogme-95', 'dogme-95').md)
- [('cinema-verite', 'cinema-verite')](('cinema-verite', 'cinema-verite').md)
- [('two-shot', 'two-shot')](('two-shot', 'two-shot').md)
- [('film-noir', 'film-noir')](('film-noir', 'film-noir').md)
- [('german-expressionism', 'german-expressionism')](('german-expressionism', 'german-expressionism').md)
- [('french-new-wave', 'french-new-wave')](('french-new-wave', 'french-new-wave').md)
- [('surrealism', 'surrealism')](('surrealism', 'surrealism').md)
- [('found-footage', 'found-footage')](('found-footage', 'found-footage').md)
- [('spaghetti-western', 'spaghetti-western')](('spaghetti-western', 'spaghetti-western').md)
