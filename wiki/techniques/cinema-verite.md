# "Cinéma Vérité Prompt for AI Image & Video"

`cinema-verite` · Film Genres · level intermediate

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Cinema verite documentary moment with [Subject], handheld camera following the action, natural available light providing uncontrolled illumination, the framing imperfect and reactive, occasional focus hunting, the raw audio of the environment, the entire aesthetic committed to the principle that imperfection is authenticity, Super 16mm film grain, the Jean Rouch principle that the camera's presence provokes truth
```

A documentary approach using handheld cameras, natural lighting, and unscripted moments to capture truth — the camera is acknowledged as present, truth provoked rather than merely observed. Jean Rouch and Edgar Morin coined the term with "Chronicle of a Summer" (1961), where the filmmakers actively engage with their subjects. The American equivalent, "direct cinema" (Frederick Wiseman, the Maysles Brothers), takes a more observational approach. The Dardenne Brothers' fiction films apply cinéma vérité techniques to narrative cinema. Paul Greengrass brings cinéma vérité energy to mainstream thr…

**When to use.** Use cinéma vérité when truth should emerge through interaction rather than polished observation. It suits interviews in motion, social encounters, street scenes, political situations, and fiction that needs documentary pressure. Let the camera's presence affect behavior instead of pretending it is invisible. The style requires responsive imperfections tied to unfolding action; random shake, damag…

**Directing the AI.** Follow the subject with a handheld camera at human distance, reacting late to gestures and occasionally correcting framing or focus. Use only available light, allowing mixed color and uneven exposure where the location creates it. Keep ambient sound, interruptions, and glances toward the camera. Let the operator shift position when events change rather than anticipating every move. Preserve faces and essential action; authenticity comes from responsive observation, not from making the footage u…

**Common mistakes.**
- Adding constant violent shake, which feels performed and prevents the audience from observing actual behavior.
- Polishing every composition and focus pull, removing the reactive uncertainty that gives the approach its tension.
- Treating technical damage as authenticity while subjects remain posed, scripted, and untouched by the camera.

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
python platform/query.py technique-motions cinema-verite
```

## Sources

- Genres: Where to Draw the Line?

## Related techniques

- [('handheld-shot', 'handheld-shot')](('handheld-shot', 'handheld-shot').md)
- [('available-light', 'available-light')](('available-light', 'available-light').md)
- [('found-footage', 'found-footage')](('found-footage', 'found-footage').md)
- [('film-noir', 'film-noir')](('film-noir', 'film-noir').md)
- [('german-expressionism', 'german-expressionism')](('german-expressionism', 'german-expressionism').md)
- [('french-new-wave', 'french-new-wave')](('french-new-wave', 'french-new-wave').md)
- [('surrealism', 'surrealism')](('surrealism', 'surrealism').md)
- [('spaghetti-western', 'spaghetti-western')](('spaghetti-western', 'spaghetti-western').md)
- [('italian-neorealism', 'italian-neorealism')](('italian-neorealism', 'italian-neorealism').md)
