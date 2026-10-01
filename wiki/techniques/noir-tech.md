# "Tech Noir Prompt for AI Image & Video"

`noir-tech` · Film Genres · level intermediate

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Tech noir scene with [Subject] in a rain-soaked neon-lit dystopia, the hard shadows and moral ambiguity of classic noir transplanted into a high-tech future, reflections of holographic advertisements in wet pavement, the loneliness of Blade Runner, anamorphic lens flares streaking through rain, cold blue and hot orange competing in every frame, smoke and vapor caught in shafts of artificial light
```

A hybrid genre fusing film noir aesthetics with science fiction — rain-soaked neon cities, morally ambiguous protagonists navigating high-tech dystopias, and the existential dread of noir transplanted into a technological future. Ridley Scott's "Blade Runner" (1982) defined the genre, combining Raymond Chandler-style detective narrative with a cyberpunk cityscape. James Cameron coined the term as the name of a nightclub in "The Terminator." Alex Proyas's "Dark City" and Denis Villeneuve's "Blade Runner 2049" expanded the visual language. The genre asks noir's eternal question — what does it m…

**When to use.** Use Tech Noir for detective stories, fugitives, artificial identities, surveillance, and moral compromise inside advanced technological worlds. The genre works when noir loneliness and hard shadow remain central beneath futuristic surfaces. Rain, holographic advertising, and machines should intensify alienation rather than advertise spectacle. Give the protagonist a compromised choice or unstable…

**Directing the AI.** Place the subject alone in a rain-soaked night street or shadowed high-tech interior. Mix cold blue environmental light with hot amber practicals, allowing both to streak across wet pavement and reflective glass. Add smoke, vapor, surveillance surfaces, and restrained holographic advertisements. Use hard side light, deep negative space, and anamorphic flare motivated by bright sources. Keep technology worn and embedded in daily life while the character remains morally and visually isolated.

**Common mistakes.**
- Filling the frame with neon signs while omitting noir shadow, loneliness, and morally compromised character stakes.
- Presenting technology as clean spectacle, which loses the worn dystopian pressure central to the hybrid genre.
- Using evenly bright cyberpunk color, leaving no darkness for surveillance, concealment, or existential dread.

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
| declared | `brand-ink-open` | opening | 83 | `brand-ink-open` |
| declared | `fracture` | opening | 156 | `fracture` |

```
python platform/query.py technique-motions noir-tech
```

## Sources

- Genres: Where to Draw the Line?

## Related techniques

- [('film-noir', 'film-noir')](('film-noir', 'film-noir').md)
- [('color-grading', 'color-grading')](('color-grading', 'color-grading').md)
- [('lens-distortion', 'lens-distortion')](('lens-distortion', 'lens-distortion').md)
- [('german-expressionism', 'german-expressionism')](('german-expressionism', 'german-expressionism').md)
- [('cinema-verite', 'cinema-verite')](('cinema-verite', 'cinema-verite').md)
- [('french-new-wave', 'french-new-wave')](('french-new-wave', 'french-new-wave').md)
- [('surrealism', 'surrealism')](('surrealism', 'surrealism').md)
- [('found-footage', 'found-footage')](('found-footage', 'found-footage').md)
- [('spaghetti-western', 'spaghetti-western')](('spaghetti-western', 'spaghetti-western').md)
