# "Italian Neorealism Prompt for AI Image & Video"

`italian-neorealism` · Film Genres · level intermediate

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Italian Neorealism with [Subject] on an actual working-class street, non-professional faces and authentic clothing, the real architecture providing the set, the camera observing at a respectful distance, natural overcast light providing flat honest illumination, black and white photography capturing poverty with dignity, the De Sica principle that reality itself is more dramatic than anything a screenwriter could invent
```

Post-war Italian movement using non-professional actors, real locations, and stories of everyday working-class life — raw, honest, and deeply humanist cinema stripped to its moral essentials. Roberto Rossellini's "Rome, Open City" (1945) launched the movement from the rubble of war. Vittorio De Sica's "Bicycle Thieves" (1948) and "Umberto D." are the genre's masterpieces — devastating stories of ordinary people told with extraordinary simplicity. Luchino Visconti's "La Terra Trema" used actual Sicilian fishermen as actors. The movement's influence extends through the Dardenne Brothers, Ken Lo…

**When to use.** Use Italian Neorealism for stories about work, poverty, family, survival, and ordinary moral choices shaped by material conditions. Real locations and unvarnished faces keep attention on human stakes rather than spectacle. The approach suits quiet observation and simple actions with serious consequences. Avoid romanticizing hardship or turning working-class environments into picturesque decay; di…

**Directing the AI.** Place the subject on an actual working street among worn architecture, everyday clothing, passing pedestrians, and functional objects. Use natural overcast light or plain daylight with black-and-white tonal detail. Keep the camera at a respectful medium distance, observing complete actions without dramatic angle changes. Favor unpolished faces and restrained gestures. Let background life continue independently. Compose clearly, but avoid ornamental lighting or production design that makes hards…

**Common mistakes.**
- Beautifying poverty with glowing light and decorative ruin, turning material hardship into an aesthetic backdrop.
- Posing every background figure, which removes the independent street life essential to the observed reality.
- Forcing melodramatic expressions instead of trusting ordinary faces, restrained gestures, and concrete circumstances.

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
python platform/query.py technique-motions italian-neorealism
```

## Sources

- Genres: Where to Draw the Line?

## Related techniques

- [('cinema-verite', 'cinema-verite')](('cinema-verite', 'cinema-verite').md)
- [('available-light', 'available-light')](('available-light', 'available-light').md)
- [('slow-cinema', 'slow-cinema')](('slow-cinema', 'slow-cinema').md)
- [('film-noir', 'film-noir')](('film-noir', 'film-noir').md)
- [('german-expressionism', 'german-expressionism')](('german-expressionism', 'german-expressionism').md)
- [('french-new-wave', 'french-new-wave')](('french-new-wave', 'french-new-wave').md)
- [('surrealism', 'surrealism')](('surrealism', 'surrealism').md)
- [('found-footage', 'found-footage')](('found-footage', 'found-footage').md)
- [('spaghetti-western', 'spaghetti-western')](('spaghetti-western', 'spaghetti-western').md)
