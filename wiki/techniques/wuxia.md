# "Wuxia Prompt for AI Image & Video"

`wuxia` · Film Genres · level advanced

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Wuxia style with [Subject] in gravity-defying motion, robes and fabric trailing like calligraphy strokes through the air, the fight-as-dance choreography of Ang Lee and Zhang Yimou, painterly natural landscape behind — bamboo forests or misty mountains, the action frozen at its most balletic moment, Kodak Vision3 250D warmth, the poetry of martial arts rendered as visual art
```

A Chinese genre centered on martial arts warriors bound by codes of honor, featuring gravity-defying combat choreography, flowing silk costumes, and painterly landscapes. Ang Lee's "Crouching Tiger, Hidden Dragon" (2000) introduced the genre to global audiences with its bamboo forest fight sequence. Zhang Yimou's "Hero" and "House of Flying Daggers" pushed the visual poetry further with color-coded narrative chapters and rain of arrows frozen in mid-air. King Hu's "A Touch of Zen" (1971) established the template of martial artists fighting in natural landscapes. The genre treats action as dan…

**When to use.** Use wuxia for martial conflict shaped by honor, loyalty, restraint, and impossible physical grace. Combat becomes dance, while landscape and costume carry emotional meaning equal to the fighters. It suits duels in bamboo, misty mountains, courtyards, and color-coded chapters. Focus on one balletic action and its moral tension; crowded chaotic fighting loses the calligraphic clarity that makes the…

**Directing the AI.** Freeze or track the subject at the most graceful point of a leap, turn, or suspended strike. Extend robes, sleeves, hair, and fabric along the motion path like calligraphy strokes. Place the action against bamboo, misty mountains, or another painterly natural setting with warm daylight and layered depth. Keep bodies anatomically readable and weapons aligned with gesture. Choreograph opponents as a balanced composition, treating gravity-defying movement as controlled dance rather than explosive…

**Common mistakes.**
- Crowding the frame with many fighters, making the choreography read as battle noise instead of visual calligraphy.
- Using rigid clothing and poses, which removes the flowing motion that gives wuxia action its lyricism.
- Treating aerial movement as superhero flight without grounded gesture, landscape, or honor-bound dramatic tension.

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
| declared | `cel-flash-stomp` | typography | 30 | `cel-flash-stomp` |

```
python platform/query.py technique-motions wuxia
```

## Sources

- Genres: Where to Draw the Line?

## Related techniques

- [('slow-motion', 'slow-motion')](('slow-motion', 'slow-motion').md)
- [('diagonal-lines', 'diagonal-lines')](('diagonal-lines', 'diagonal-lines').md)
- [('golden-hour', 'golden-hour')](('golden-hour', 'golden-hour').md)
- [('film-noir', 'film-noir')](('film-noir', 'film-noir').md)
- [('german-expressionism', 'german-expressionism')](('german-expressionism', 'german-expressionism').md)
- [('cinema-verite', 'cinema-verite')](('cinema-verite', 'cinema-verite').md)
- [('french-new-wave', 'french-new-wave')](('french-new-wave', 'french-new-wave').md)
- [('surrealism', 'surrealism')](('surrealism', 'surrealism').md)
- [('found-footage', 'found-footage')](('found-footage', 'found-footage').md)
