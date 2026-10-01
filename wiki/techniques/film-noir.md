# "Film Noir Prompt for AI Image & Video"

`film-noir` · Film Genres · level intermediate

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Film noir aesthetic with [Subject] in high-contrast black and white, deep blacks and silvery highlights, venetian blind shadow patterns, neon signs reflected in rain puddles, shot on Kodak Double-X black and white stock with hard lighting creating razor shadows, the John Alton visual language of moral ambiguity expressed through the war between light and darkness
```

A genre defined by high-contrast black-and-white photography, urban settings, morally ambiguous characters, femme fatales, and a pervasive sense of cynicism and doom. Born from German Expressionist emigrés and American hardboiled fiction, film noir flowered in the 1940s and 50s with Billy Wilder's "Double Indemnity," Orson Welles's "Touch of Evil," and John Huston's "The Maltese Falcon." Cinematographers like John Alton and Nicholas Musuraca defined the visual language of shadows, rain, and venetian blinds. The genre was revived as neo-noir by Roman Polanski's "Chinatown," the Coen Brothers'…

**When to use.** Use film noir for crime, betrayal, investigation, fatal attraction, or any story built on compromised choices and approaching doom. Its visual language turns light into moral pressure: characters are divided by shadow, streets become traps, and interiors conceal more than they reveal. The genre is strongest when cinematography and character conflict agree. Venetian blinds alone cannot create noir…

**Directing the AI.** Work in high-contrast black and white with deep blacks, silvery highlights, and limited midtones. Place the subject in an urban interior or rain-dark street, then rake hard light through blinds, doorways, or smoke to create sharp patterned shadows. Use low or oblique angles and leave portions of faces concealed. Add wet reflections and restrained practical neon translated into tonal brightness. Compose every light source as pressure, surveillance, or temptation.

**Common mistakes.**
- Adding venetian-blind shadows to a bright neutral scene without noir conflict, danger, or moral ambiguity.
- Crushing every dark area to featureless black, erasing the location and the subject's readable silhouette.
- Using soft flattering portrait light, which removes the hard visual conflict central to noir imagery.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` | `camera_motion: pan_right | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: smooth_pan` | pika-1.5 | no |
| `runway_gen3` | `motion_brush: smooth_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: smooth_pan` | sora-1 | no |
| `veo2` | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

## Motion pairings

**Declared, not inferred.** These come from an explicit `styles:` list in `data/cinematic/<slug>.md`, authored in `platform/catalog/pairings.py`. Nothing here is matched by name similarity.

| kind | shot card | category | frames | style |
|---|---|---|---|---|
| declared | `brand-ink-open` | opening | 83 | `brand-ink-open` |
| declared | `fracture` | opening | 156 | `fracture` |

```
python platform/query.py technique-motions film-noir
```

## Sources

- Genres: Where to Draw the Line?

## Related techniques

- [('low-key-lighting', 'low-key-lighting')](('low-key-lighting', 'low-key-lighting').md)
- [('chiaroscuro', 'chiaroscuro')](('chiaroscuro', 'chiaroscuro').md)
- [('noir-tech', 'noir-tech')](('noir-tech', 'noir-tech').md)
- [('german-expressionism', 'german-expressionism')](('german-expressionism', 'german-expressionism').md)
- [('cinema-verite', 'cinema-verite')](('cinema-verite', 'cinema-verite').md)
- [('french-new-wave', 'french-new-wave')](('french-new-wave', 'french-new-wave').md)
- [('surrealism', 'surrealism')](('surrealism', 'surrealism').md)
- [('found-footage', 'found-footage')](('found-footage', 'found-footage').md)
- [('spaghetti-western', 'spaghetti-western')](('spaghetti-western', 'spaghetti-western').md)
