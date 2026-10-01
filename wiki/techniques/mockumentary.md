# "Mockumentary Prompt for AI Image & Video"

`mockumentary` · Film Genres · level basic

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Mockumentary talking head interview with [Subject] looking slightly off-camera to an unseen interviewer, standard documentary medium close-up with unflattering fluorescent lighting, the documentary format treating the setting with the visual gravity of a war correspondent's confession, handheld camera occasionally reframing to maintain the documentary illusion, the Christopher Guest understanding that absurd comedy requires deadpan documentary treatment
```

A fictional film presented in documentary style — talking head interviews, observational camera work, title cards — creating comedy through the contrast between the serious form and absurd content. Rob Reiner's "This Is Spinal Tap" (1984) established the mockumentary as a legitimate comedic form. Christopher Guest continued the tradition with "Waiting for Guffman," "Best in Show," and "A Mighty Wind." Ricky Gervais and Stephen Merchant's "The Office" (UK) made the mockumentary format a television staple, leading to the American version and eventually "Parks and Recreation" and "Modern Family.…

**When to use.** Use mockumentary when comedy depends on fictional characters treating absurd events with complete documentary seriousness. Talking-head interviews can contradict observed action, reveal vanity, or let a glance expose what dialogue will not. The format suits workplace, community, performance, and social satire. Keep the camera's behavior credible and restrained; if the filmmaking starts announcing…

**Directing the AI.** Frame the subject in a standard medium close-up, looking slightly off-camera toward an unseen interviewer. Use plain fluorescent or window light, a functional background, and minimal visual flattery. During observational scenes, let the handheld camera reframe late, zoom slightly toward revealing reactions, or catch a private glance into lens. Keep titles and composition sober. Treat every ridiculous statement with the visual gravity of serious testimony, never adding comic effects to explain t…

**Common mistakes.**
- Lighting and framing interviews like glossy commercials, weakening the contrast between serious form and absurd content.
- Adding comic zooms to every line, making the camera beg for laughs instead of observing behavior.
- Having characters perform obvious jokes for the lens rather than protecting their sincere documentary reality.

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
| declared | `graze-face-tour` | camera | 150 | `graze-face-tour` |

```
python platform/query.py technique-motions mockumentary
```

## Sources

- Genres: Where to Draw the Line?

## Related techniques

- [('reaction-shot', 'reaction-shot')](('reaction-shot', 'reaction-shot').md)
- [('breaking-fourth-wall', 'breaking-fourth-wall')](('breaking-fourth-wall', 'breaking-fourth-wall').md)
- [('cinema-verite', 'cinema-verite')](('cinema-verite', 'cinema-verite').md)
- [('film-noir', 'film-noir')](('film-noir', 'film-noir').md)
- [('german-expressionism', 'german-expressionism')](('german-expressionism', 'german-expressionism').md)
- [('french-new-wave', 'french-new-wave')](('french-new-wave', 'french-new-wave').md)
- [('surrealism', 'surrealism')](('surrealism', 'surrealism').md)
- [('found-footage', 'found-footage')](('found-footage', 'found-footage').md)
- [('spaghetti-western', 'spaghetti-western')](('spaghetti-western', 'spaghetti-western').md)
