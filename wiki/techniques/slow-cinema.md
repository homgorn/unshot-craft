# "Slow Cinema Prompt for AI Image & Video"

`slow-cinema` · Film Genres · level advanced

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Slow cinema with [Subject] in a single unbroken composition, the camera absolutely still observing with infinite patience, the only movement gradual shifting of natural light, duration itself becoming the subject, natural overcast daylight providing soft even illumination, the Tarkovsky-Bela Tarr discipline of trusting that observation is enough, that the passage of real time is cinema's most radical subject
```

A contemporary movement embracing extremely long takes, minimal dialogue, and patient observation that challenges the viewer to slow down, observe, and find meaning in duration itself. Andrei Tarkovsky is the spiritual father of slow cinema, with his meditative long takes in "Stalker" and "Mirror" establishing duration as a cinematic tool. Béla Tarr's "Sátántangó" (seven hours of long takes) and "The Turin Horse" are the movement's most extreme expressions. Apichatpong Weerasethakul's Palme d'Or-winning "Uncle Boonmee Who Can Recall His Past Lives" and Chantal Akerman's "Jeanne Dielman" repre…

**When to use.** Use slow cinema when duration itself reveals behavior, labor, landscape, grief, routine, or waiting. A long unbroken view can make tiny changes matter because the audience has time to notice them. It suits contemplative stories and actions normally compressed by editing. Choose a frame with evolving light, weather, posture, or background life; stillness should contain attention, not simply withho…

**Directing the AI.** Lock the camera in one carefully balanced composition and observe the subject through a complete action or interval without cutting. Keep dialogue sparse and movement gradual. Let natural overcast light shift, a distant figure cross, steam disappear, or posture change over real time. Avoid push-ins, coverage, and music cues that instruct emotion. Preserve ambient sound and depth. The frame must remain visually exact enough that small changes become legible rewards for patience.

**Common mistakes.**
- Holding an empty composition with no evolving light, behavior, sound, or environmental detail to observe.
- Adding frequent reframing or coverage cuts, which removes the sustained duration defining the approach.
- Using slow pacing as automatic seriousness without giving the audience specific visual activity worth attending to.

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
| declared | `space-camera-moves` | camera | 150 | `drone-dive-landing` |
| declared | `space-camera-moves` | camera | 150 | `exploded-view` |

```
python platform/query.py technique-motions slow-cinema
```

## Sources

- Genres: Where to Draw the Line?

## Related techniques

- [('long-take', 'long-take')](('long-take', 'long-take').md)
- [('static-shot', 'static-shot')](('static-shot', 'static-shot').md)
- [('italian-neorealism', 'italian-neorealism')](('italian-neorealism', 'italian-neorealism').md)
- [('film-noir', 'film-noir')](('film-noir', 'film-noir').md)
- [('german-expressionism', 'german-expressionism')](('german-expressionism', 'german-expressionism').md)
- [('cinema-verite', 'cinema-verite')](('cinema-verite', 'cinema-verite').md)
- [('french-new-wave', 'french-new-wave')](('french-new-wave', 'french-new-wave').md)
- [('surrealism', 'surrealism')](('surrealism', 'surrealism').md)
- [('found-footage', 'found-footage')](('found-footage', 'found-footage').md)
