# "German Expressionism Prompt for AI Image & Video"

`german-expressionism` · Film Genres · level advanced

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
German Expressionism with [Subject] in deliberately distorted architecture, buildings leaning at impossible angles, shadows painted in sharp angular patterns that defy actual light sources, extreme contrast between blinding white and absolute black with no midtones, the Caligari aesthetic of a world bent by psychological torment, monochrome with exaggerated theatrical lighting
```

An early 20th-century movement using distorted sets, extreme shadows, and exaggerated angles to externalize inner psychological states — the visual DNA of modern horror and Tim Burton. Robert Wiene's "The Cabinet of Dr. Caligari" (1920) established the movement with painted shadows and impossible architecture. F.W. Murnau's "Nosferatu" and Fritz Lang's "Metropolis" expanded the vocabulary. When these filmmakers fled Nazi Germany, they brought Expressionism to Hollywood, directly influencing film noir. Tim Burton's "Batman," "Edward Scissorhands," and "Batman Returns" are modern Expressionism,…

**When to use.** Use German Expressionism when the environment should externalize fear, paranoia, grief, or mental fracture. Distorted walls, impossible streets, and painted shadows make psychology physical rather than realistic. It fits horror, nightmare, theatrical fantasy, and moments when subjective truth matters more than natural space. Commit across set, light, angle, and performance; one crooked doorway in…

**Directing the AI.** Build a monochrome set with leaning buildings, jagged doorways, slanted floors, and forced angles that cannot exist naturally. Remove most midtones, dividing the frame into blinding white and absolute black. Paint hard triangular shadows across surfaces without matching realistic light sources. Tilt the camera and exaggerate the subject's posture to echo the architecture. Keep every distortion graphic and intentional, as though the character's psychological torment designed the entire physical…

**Common mistakes.**
- Keeping realistic architecture while adding random tilted framing, producing a weak imitation of the style.
- Using soft naturalistic shadows, which contradict the painted graphic darkness of Expressionist space.
- Adding many unrelated horror props instead of letting distorted geometry and contrast carry the psychological threat.

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
python platform/query.py technique-motions german-expressionism
```

## Sources

- Genres: Where to Draw the Line?

## Related techniques

- [('dutch-angle', 'dutch-angle')](('dutch-angle', 'dutch-angle').md)
- [('chiaroscuro', 'chiaroscuro')](('chiaroscuro', 'chiaroscuro').md)
- [('film-noir', 'film-noir')](('film-noir', 'film-noir').md)
- [('cinema-verite', 'cinema-verite')](('cinema-verite', 'cinema-verite').md)
- [('french-new-wave', 'french-new-wave')](('french-new-wave', 'french-new-wave').md)
- [('surrealism', 'surrealism')](('surrealism', 'surrealism').md)
- [('found-footage', 'found-footage')](('found-footage', 'found-footage').md)
- [('spaghetti-western', 'spaghetti-western')](('spaghetti-western', 'spaghetti-western').md)
- [('italian-neorealism', 'italian-neorealism')](('italian-neorealism', 'italian-neorealism').md)
