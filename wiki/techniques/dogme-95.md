# "Dogme 95 Prompt for AI Image & Video"

`dogme-95` · Film Genres · level advanced

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Dogme 95 aesthetic with [Subject] shot on a consumer camera with no additional lighting, harsh overhead fluorescent as the only illumination, color balance slightly off, handheld breathing movement, the radical commitment to zero artifice — no music, no effects, no genre, just human beings in real space, the Vinterberg-von Trier Vow of Chastity made visible
```

A 1995 Danish manifesto demanding handheld cameras, natural lighting, real locations, no genre conventions, and no directorial credit — a radical purity movement that stripped cinema to its bones. Lars von Trier and Thomas Vinterberg created the Dogme 95 "Vow of Chastity," and Vinterberg's "The Celebration" became the movement's masterpiece, using only available light and handheld consumer video cameras. Von Trier's "The Idiots" and Harmony Korine's "Julien Donkey-Boy" also bore the Dogme certificate. Though the movement officially ended, its influence persists in mumblecore, in the work of t…

**When to use.** Use Dogme 95 principles when performance and human conflict should survive without cinematic decoration. Real rooms, handheld cameras, available light, location sound, and present-tense action can expose discomfort that polished technique might soften. It fits family crises, confrontations, and intimate social pressure. Apply the restrictions as a creative discipline, not as a distressed preset;…

**Directing the AI.** Place the subject in a real interior or exterior and use only light already present, even when fluorescent color or window exposure is imperfect. Follow action handheld at close human distance, allowing breathing movement and reactive reframing. Keep natural room echo, interruptions, and practical objects. Remove added music, stylized transitions, artificial set dressing, and visual effects. Preserve readable faces and actions while letting the location's limitations dictate the image rather th…

**Common mistakes.**
- Adding artificial grain, glitches, and damage, mistaking post-production distress for a commitment to real conditions.
- Using dramatic added light while claiming available-light realism, which breaks the technique's central visual discipline.
- Making the frame deliberately unreadable, when stripped-back filmmaking should expose performance rather than hide it.

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
python platform/query.py technique-motions dogme-95
```

## Sources

- Genres: Where to Draw the Line?

## Related techniques

- [('available-light', 'available-light')](('available-light', 'available-light').md)
- [('handheld-shot', 'handheld-shot')](('handheld-shot', 'handheld-shot').md)
- [('mumblecore', 'mumblecore')](('mumblecore', 'mumblecore').md)
- [('film-noir', 'film-noir')](('film-noir', 'film-noir').md)
- [('german-expressionism', 'german-expressionism')](('german-expressionism', 'german-expressionism').md)
- [('cinema-verite', 'cinema-verite')](('cinema-verite', 'cinema-verite').md)
- [('french-new-wave', 'french-new-wave')](('french-new-wave', 'french-new-wave').md)
- [('surrealism', 'surrealism')](('surrealism', 'surrealism').md)
- [('found-footage', 'found-footage')](('found-footage', 'found-footage').md)
