# "Cross-Cutting Prompt for AI Image & Video"

`cross-cutting` · Editing · level intermediate

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Cross-cutting between two simultaneous scenes involving [Subject], the alternation between warm and cold tones accelerating in rhythm as both events build toward climax, the visual contrast intensifying the irony, each cut creating a collision of meaning that neither scene could generate alone, warm Kodak tones on one side against cold pushed processing on the other
```

Alternating between two or more scenes happening simultaneously in different locations, building tension by implying convergence and creating dramatic parallels between storylines. D.W. Griffith pioneered cross-cutting in "Intolerance" (1916), intercutting between four historical periods. Christopher Nolan elevated cross-cutting to structural principle in "Inception" and "Dunkirk," weaving three timelines with different tempos. Francis Ford Coppola's baptism sequence in "The Godfather" — cross-cutting between the church ceremony and the simultaneous murders — remains one of cinema's most powe…

**When to use.** Cross-cutting is the right structure when separate events happen at the same time and gain force by being compared. Use it for rescues, pursuits, rituals against violence, parallel decisions, or storylines moving toward collision. Each return should add information or tighten the temporal relationship. The technique fails when the scenes merely alternate without escalation, thematic contrast, or…

**Directing the AI.** Define two distinct locations, visual palettes, and actions occurring simultaneously. Begin with longer sections in each scene, then shorten the alternation as pressure rises. Match gestures, sounds, shapes, or emotional beats across cuts where a collision of meaning helps. Preserve wardrobe, geography, and action continuity within both strands. End at a shared climax, direct convergence, or purposeful separation. Do not let one storyline advance in time while the other appears frozen between r…

**Common mistakes.**
- Alternating locations at a fixed pace without raising stakes, shortening intervals, or revealing a stronger temporal connection.
- Losing continuity inside one strand, so objects, positions, or actions reset each time the edit returns there.
- Pairing scenes with no thematic or causal relationship, making the structure feel arbitrary rather than mutually intensifying.

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
| declared | `beat-cut-moves` | rhythm | 49 | `beat-cut-accelerando` |
| declared | `beat-cut-moves` | rhythm | 49 | `paparazzi-flash` |

```
python platform/query.py technique-motions cross-cutting
```

## Sources

- What Is Film Editing?

## Related techniques

- [('parallel-storylines', 'parallel-storylines')](('parallel-storylines', 'parallel-storylines').md)
- [('split-screen', 'split-screen')](('split-screen', 'split-screen').md)
- [('montage', 'montage')](('montage', 'montage').md)
- [('jump-cut', 'jump-cut')](('jump-cut', 'jump-cut').md)
- [('dissolve', 'dissolve')](('dissolve', 'dissolve').md)
- [('fade-in-out', 'fade-in-out')](('fade-in-out', 'fade-in-out').md)
- [('smash-cut', 'smash-cut')](('smash-cut', 'smash-cut').md)
- [('long-take', 'long-take')](('long-take', 'long-take').md)
- [('freeze-frame', 'freeze-frame')](('freeze-frame', 'freeze-frame').md)
