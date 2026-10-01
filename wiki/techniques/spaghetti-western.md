# "Spaghetti Western Prompt for AI Image & Video"

`spaghetti-western` · Film Genres · level intermediate

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Spaghetti Western standoff with [Subject], the camera alternating between extreme close-ups of squinting eyes and ultra-wide shots revealing vast empty space, dust devils spiraling through the frame, golden hour desert light casting long shadows, shot on Techniscope 2-perf 35mm for gritty widescreen, the Ennio Morricone tension of silence stretched to breaking point
```

Italian-produced Westerns characterized by extreme close-ups, sweeping wide shots, Morricone-style scores, morally gray antiheroes, and a stylized, operatic approach to violence. Sergio Leone defined the genre with his Dollars trilogy starring Clint Eastwood and reached its apex with "Once Upon a Time in the West" — a film built entirely from looks, silences, and Ennio Morricone's score. Leone's visual grammar of extreme close-up eyes cutting to extreme wide shots became one of cinema's most imitated styles. Sergio Corbucci's "Django" and "The Great Silence" pushed the genre toward nihilism.…

**When to use.** Use the Spaghetti Western style for standoffs, revenge, outlaw myth, and confrontations where waiting carries as much force as violence. Its rhythm depends on the collision between extreme close-ups and vast wides, turning eyes, hands, and empty distance into equal dramatic players. It suits morally gray characters and stylized danger. Do not rush the payoff; stretched silence is part of the visu…

**Directing the AI.** Establish an immense desert wide shot with the subject reduced against empty terrain, dust devils, and long golden-hour shadows. Cut to extreme close-ups of narrowed eyes, weathered skin, boots, and a hand hovering near a weapon. Keep the horizon broad and the color warm, with gritty widescreen texture. Alternate scale slowly, letting tiny gestures carry threat. Hold the final silence until tension peaks, then resolve with one sudden, readable action.

**Common mistakes.**
- Keeping every shot at medium distance, losing the genre's defining collision between faces and vast space.
- Cutting rapidly throughout the standoff, denying silence and duration the chance to build operatic tension.
- Using clean modern surfaces and clothing, which weakens the dusty, weathered physical world around the confrontation.

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
python platform/query.py technique-motions spaghetti-western
```

## Sources

- Genres: Where to Draw the Line?

## Related techniques

- [('cowboy-shot', 'cowboy-shot')](('cowboy-shot', 'cowboy-shot').md)
- [('extreme-close-up', 'extreme-close-up')](('extreme-close-up', 'extreme-close-up').md)
- [('acid-western', 'acid-western')](('acid-western', 'acid-western').md)
- [('film-noir', 'film-noir')](('film-noir', 'film-noir').md)
- [('german-expressionism', 'german-expressionism')](('german-expressionism', 'german-expressionism').md)
- [('cinema-verite', 'cinema-verite')](('cinema-verite', 'cinema-verite').md)
- [('french-new-wave', 'french-new-wave')](('french-new-wave', 'french-new-wave').md)
- [('surrealism', 'surrealism')](('surrealism', 'surrealism').md)
- [('found-footage', 'found-footage')](('found-footage', 'found-footage').md)
