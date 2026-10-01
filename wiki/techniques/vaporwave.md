# "Vaporwave Aesthetic Prompt for AI Image & Video"

`vaporwave` · Film Genres · level basic

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Vaporwave aesthetic with [Subject] bathed in neon pink and cyan gradient lighting, retro digital artifacts and scan lines overlaid, reflective chrome and glass surfaces, the nostalgic melancholy of a 1990s shopping mall at closing time, VHS color bleeding and tracking errors, palm trees and marble columns, the beauty of obsolete technology, everything slightly too saturated and slightly too perfect
```

A visual style born from internet culture that repurposes 1980s and 90s commercial aesthetics — glitch art, neon pink and cyan gradients, retro computer interfaces, marble busts, Japanese text, and VHS degradation — into a nostalgic critique of consumer capitalism. While originating as a music genre, the visual language has been widely adopted in film, advertising, and AI generation. Nicolas Winding Refn's neon-soaked aesthetics in "The Neon Demon" share DNA with vaporwave. The style is simultaneously ironic and sincere — mourning a future that never arrived.

**When to use.** Use vaporwave when the image should feel nostalgic for a commercial future that never arrived. It suits empty malls, obsolete technology, artificial leisure spaces, retro interfaces, and scenes balancing irony with sincere melancholy. The style is strongest when recognizable 1980s or 1990s consumer imagery feels abandoned or looped. Avoid treating it as a random neon collage; the emotional center…

**Directing the AI.** Bathe the subject in a pink-to-cyan gradient and place them among reflective chrome, glass, marble columns, palms, or an empty shopping-mall interior. Add scan lines, mild VHS color bleed, tracking errors, and retro interface fragments without covering the composition. Keep surfaces slightly too polished and colors slightly too saturated. Leave generous empty space and late-night stillness so obsolete commercial imagery reads as melancholy rather than energetic cyberpunk spectacle.

**Common mistakes.**
- Combining every retro icon at once, turning a coherent nostalgic world into an internet sticker collage.
- Using dark aggressive cyberpunk lighting, which loses vaporwave's pastel commercial emptiness and wistful artificial calm.
- Applying severe VHS damage until architecture, text, and the central subject can no longer be read.

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
| declared | `gradient-transition` | transition | 180 | `gradient-transition` |

```
python platform/query.py technique-motions vaporwave
```

## Sources

- Genres: Where to Draw the Line?

## Related techniques

- [('color-grading', 'color-grading')](('color-grading', 'color-grading').md)
- [('film-grain', 'film-grain')](('film-grain', 'film-grain').md)
- [('noir-tech', 'noir-tech')](('noir-tech', 'noir-tech').md)
- [('film-noir', 'film-noir')](('film-noir', 'film-noir').md)
- [('german-expressionism', 'german-expressionism')](('german-expressionism', 'german-expressionism').md)
- [('cinema-verite', 'cinema-verite')](('cinema-verite', 'cinema-verite').md)
- [('french-new-wave', 'french-new-wave')](('french-new-wave', 'french-new-wave').md)
- [('surrealism', 'surrealism')](('surrealism', 'surrealism').md)
- [('found-footage', 'found-footage')](('found-footage', 'found-footage').md)
