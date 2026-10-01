# "Split Screen Prompt for AI Image & Video"

`split-screen` · Editing · level intermediate

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Split screen dividing the frame with [Subject] visible in both halves simultaneously, one side warm-toned and the other cool-toned, the vertical divide becoming the physical and emotional distance, the De Palma technique of making the audience omniscient observers of parallel realities occupying the same frame
```

The frame is divided into two or more sections, each showing a different angle, location, or timeline simultaneously, showing parallel action, phone conversations, or multiple perspectives at once. Brian De Palma made split screen his signature, using it in "Carrie," "Dressed to Kill," and "Snake Eyes" to create impossible simultaneity. Ang Lee used complex multi-panel split screens in "Hulk" to emulate comic book layouts. Denis Villeneuve employed split screen in "Enemy" to visualize duality, and the technique has experienced a revival in television through shows like "24" where real-time pa…

**When to use.** Split screen is effective when the audience needs simultaneous access to separate locations, angles, timelines, or perspectives. Use it for phone calls, parallel action, surveillance, comparison, duality, or events whose timing matters more than spatial unity. Each panel needs a clear function and compatible visual hierarchy. The method becomes exhausting when every panel contains equal motion an…

**Directing the AI.** Divide the canvas into two or more clean panels with explicit proportions and boundaries. Assign each panel a location, palette, camera angle, and action, then synchronize moments that should connect across the divide. Keep identities and environments stable within their own sections. Control attention by varying motion, contrast, or duration so only one panel dominates at a time. Prevent limbs, faces, and objects from bleeding across boundaries unless a deliberate transition unites the spaces.

**Common mistakes.**
- Filling every panel with equally intense movement, forcing the viewer to miss essential actions happening at the same time.
- Changing panel sizes and borders without narrative purpose, making the layout feel unstable rather than intentionally dynamic.
- Allowing character features or backgrounds to drift between panels, weakening the distinction between separate locations or perspectives.

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
| declared | `scanline-assemble-flyin` | effects | 138 | `scanline-assemble-flyin` |

```
python platform/query.py technique-motions split-screen
```

## Sources

- What Is Film Editing?

## Related techniques

- [('cross-cutting', 'cross-cutting')](('cross-cutting', 'cross-cutting').md)
- [('parallel-storylines', 'parallel-storylines')](('parallel-storylines', 'parallel-storylines').md)
- [('two-shot', 'two-shot')](('two-shot', 'two-shot').md)
- [('jump-cut', 'jump-cut')](('jump-cut', 'jump-cut').md)
- [('dissolve', 'dissolve')](('dissolve', 'dissolve').md)
- [('fade-in-out', 'fade-in-out')](('fade-in-out', 'fade-in-out').md)
- [('montage', 'montage')](('montage', 'montage').md)
- [('smash-cut', 'smash-cut')](('smash-cut', 'smash-cut').md)
- [('long-take', 'long-take')](('long-take', 'long-take').md)
