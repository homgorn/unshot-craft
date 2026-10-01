# "Dissolve Prompt for AI Image & Video"

`dissolve` · Editing · level basic

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Dissolve transition with two overlapping images of [Subject], both simultaneously visible for a long four-second overlap, the soft double-exposure quality of two temporalities occupying one image, warm sepia tones mixing with saturated color, the nostalgic ache of time-dissolving cinema
```

One image gradually fades out as the next fades in, both visible simultaneously during the transition, suggesting the passage of time, a dream state, or a thematic connection. Ingmar Bergman used dissolves as emotional bridges in "Wild Strawberries," where the overlap between present and memory becomes the film's central visual metaphor. Terrence Malick uses extended dissolves in "The Tree of Life" to blend cosmic and domestic imagery. Stanley Kubrick's dissolve from the star gate sequence to the neoclassical bedroom in "2001" is one of cinema's most disorienting transitions. Wong Kar-wai lay…

**When to use.** A dissolve fits transitions where two images should coexist before one replaces the other. Use it for memory, elapsed time, dreams, emotional association, or visual comparison across places and periods. Longer overlaps feel fluid and contemplative; shorter ones work as gentle passage. Choose images whose shapes, tones, or meanings interact during the blend. If the overlap contains unrelated clutt…

**Directing the AI.** Select an outgoing and incoming shot with compatible focal areas or deliberately contrasting meanings. Fade the first image down while the second rises over a defined duration, allowing both to remain visible through the middle. Align faces, horizons, objects, or light shapes when their overlap should create a third meaning. Keep exposure controlled so the center does not become washed out. Preserve each shot's continuity before and after the transition, and avoid morphing identities during the…

**Common mistakes.**
- Dissolving between equally busy images, creating a cluttered middle where neither subject nor thematic connection remains readable.
- Letting faces or objects deform into each other, turning a layered transition into an unintended morphing effect.
- Using the same dissolve length for every transition, regardless of whether the story calls for tenderness, passage, or disorientation.

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
| declared | `shot-transitions` | transition | — | `black-card-transition` |
| declared | `shot-transitions` | transition | — | `dark-tunnel-transition` |
| declared | `shot-transitions` | transition | — | `focus-handoff-transition` |
| declared | `shot-transitions` | transition | — | `mask-wipe-real` |
| declared | `shot-transitions` | transition | — | `portal-wipe-v2` |
| declared | `shot-transitions` | transition | — | `whip-brake-real` |
| declared | `shot-transitions` | transition | — | `whip-pan-real` |

```
python platform/query.py technique-motions dissolve
```

## Sources

- What Is Film Editing?

## Related techniques

- [('fade-in-out', 'fade-in-out')](('fade-in-out', 'fade-in-out').md)
- [('morphing', 'morphing')](('morphing', 'morphing').md)
- [('flashback', 'flashback')](('flashback', 'flashback').md)
- [('cross-cutting', 'cross-cutting')](('cross-cutting', 'cross-cutting').md)
- [('jump-cut', 'jump-cut')](('jump-cut', 'jump-cut').md)
- [('montage', 'montage')](('montage', 'montage').md)
- [('smash-cut', 'smash-cut')](('smash-cut', 'smash-cut').md)
- [('long-take', 'long-take')](('long-take', 'long-take').md)
- [('freeze-frame', 'freeze-frame')](('freeze-frame', 'freeze-frame').md)
