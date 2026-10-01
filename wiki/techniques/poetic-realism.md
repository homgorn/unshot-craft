# "Poetic Realism Prompt for AI Image & Video"

`poetic-realism` · Film Genres · level advanced

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Poetic realism with [Subject] rendered in heartbreaking lyrical beauty, fog softening every hard edge into dreamlike haze, the ordinary transformed into visual poetry by atmosphere, the Marcel Carne understanding that working-class life contains as much beauty and melancholy as any aristocratic drama, soft black and white with rich midtones, fog itself becoming the emotional texture of longing
```

A 1930s French movement blending realistic working-class settings with lyrical, dreamlike visual beauty — finding poetry in the mundane through fog-wrapped docks, rain on cobblestones, and melancholy love. Marcel Carné and cinematographer Eugène Schüfftan defined the style in "Port of Shadows" and "Children of Paradise," creating misty, romantically lit working-class worlds. Jean Renoir's "The Rules of the Game" carries the movement's humanism. Jean Vigo's "L'Atalante" is poetic realism at its most luminous. The movement directly influenced film noir and continues to echo in the work of Wong…

**When to use.** Use poetic realism for melancholy love, working-class lives, doomed encounters, and ordinary places charged with longing. The method keeps streets, docks, rooms, and labor recognizable while atmosphere lifts them beyond plain documentation. Fog, rain, reflections, and soft tonal light should deepen human feeling, not erase material reality. It is ideal when beauty and hardship need to coexist in…

**Directing the AI.** Place the subject in a modest street, dock, café, or rented room with real signs of work and wear. Use soft black and white with rich midtones, wet cobblestones, diffused lamps, and fog that gently reduces distant contrast. Keep the figure grounded through tactile clothing and specific activity. Let rain or haze shape depth without hiding the setting. Compose lyricism through atmosphere and gesture, avoiding glamorous polish or fantasy architecture.

**Common mistakes.**
- Using fog so densely that the working environment disappears and the image becomes generic romantic haze.
- Beautifying every surface until labor, wear, and social reality no longer anchor the lyrical treatment.
- Crushing the image into harsh noir contrast, losing the soft midtones that carry melancholy and tenderness.

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
python platform/query.py technique-motions poetic-realism
```

## Sources

- Genres: Where to Draw the Line?

## Related techniques

- [('soft-light', 'soft-light')](('soft-light', 'soft-light').md)
- [('italian-neorealism', 'italian-neorealism')](('italian-neorealism', 'italian-neorealism').md)
- [('film-noir', 'film-noir')](('film-noir', 'film-noir').md)
- [('german-expressionism', 'german-expressionism')](('german-expressionism', 'german-expressionism').md)
- [('cinema-verite', 'cinema-verite')](('cinema-verite', 'cinema-verite').md)
- [('french-new-wave', 'french-new-wave')](('french-new-wave', 'french-new-wave').md)
- [('surrealism', 'surrealism')](('surrealism', 'surrealism').md)
- [('found-footage', 'found-footage')](('found-footage', 'found-footage').md)
- [('spaghetti-western', 'spaghetti-western')](('spaghetti-western', 'spaghetti-western').md)
