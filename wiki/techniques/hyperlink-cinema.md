# "Hyperlink Cinema Prompt for AI Image & Video"

`hyperlink-cinema` · Film Genres · level advanced

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Hyperlink cinema visualization with [Subject] shown across multiple disconnected lives in the same moment, each in their own lighting world and emotional register yet sharing the same space, the invisible connections not yet apparent but waiting to be revealed, the Robert Altman and Paul Thomas Anderson structure of simultaneous parallel stories, the whole greater than the sum because these lives will eventually collide
```

A narrative style weaving multiple storylines that initially seem unconnected but gradually reveal hidden links — "Crash," "Babel," "Magnolia" — the interconnected web of human experience. Robert Altman pioneered the form with "Nashville" and "Short Cuts." Paul Thomas Anderson's "Magnolia" weaves nine storylines that converge in a biblical climax. Alejandro González Iñárritu's "Amores Perros" and "Babel" extended the form across cultures and continents. Paul Haggis's "Crash" won the Best Picture Oscar using the structure. The form reflects a philosophical worldview — that all human lives are…

**When to use.** Use hyperlink cinema when several apparently separate stories can reveal a larger web of cause, coincidence, or shared consequence. Unlike simple parallel action, the pleasure comes from discovering hidden links between lives that initially seem unrelated. Give each thread an independent emotional engine and plant connective objects, spaces, or events early. The convergence should change how prio…

**Directing the AI.** Create distinct visual worlds for each character through location, palette, light, and framing rhythm. Repeat one ordinary object, route, broadcast, weather event, or background figure across threads without emphasizing the connection too early. Cross-cut at matching gestures or consequences, gradually tightening temporal proximity. When lives collide, bring visual elements from their separate worlds into one composition. Preserve causality so the final network feels uncovered rather than manuf…

**Common mistakes.**
- Revealing every connection immediately, removing the gradual recognition that gives the structure its narrative pleasure.
- Giving secondary threads no independent stakes, making them feel like machinery for the central character's plot.
- Using coincidence alone at convergence without planted objects, spaces, causes, or consequences linking earlier scenes.

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
| declared | `glitch-cycle` | typography | 168 | `glitch-cycle` |

```
python platform/query.py technique-motions hyperlink-cinema
```

## Sources

- Genres: Where to Draw the Line?

## Related techniques

- [('parallel-storylines', 'parallel-storylines')](('parallel-storylines', 'parallel-storylines').md)
- [('cross-cutting', 'cross-cutting')](('cross-cutting', 'cross-cutting').md)
- [('motif', 'motif')](('motif', 'motif').md)
- [('film-noir', 'film-noir')](('film-noir', 'film-noir').md)
- [('german-expressionism', 'german-expressionism')](('german-expressionism', 'german-expressionism').md)
- [('cinema-verite', 'cinema-verite')](('cinema-verite', 'cinema-verite').md)
- [('french-new-wave', 'french-new-wave')](('french-new-wave', 'french-new-wave').md)
- [('surrealism', 'surrealism')](('surrealism', 'surrealism').md)
- [('found-footage', 'found-footage')](('found-footage', 'found-footage').md)
