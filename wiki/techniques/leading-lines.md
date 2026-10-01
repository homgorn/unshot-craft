# "Leading Lines Prompt for AI Image & Video"

`leading-lines` · Composition · level basic

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Leading lines composition converging toward [Subject] at a distant vanishing point, every element in the frame designed to pull the eye irresistibly toward the focal point, morning fog softening the background and enhancing atmospheric perspective, shot on a 135mm telephoto to compress the distance and intensify convergence, desaturated cool palette, the visual magnetism of lines that refuse to let the eye wander
```

Using natural or architectural lines within the scene — roads, fences, corridors, shadows — to guide the viewer's eye toward the subject or deep into the frame. Kubrick's one-point-perspective corridors are pure leading-line compositions, while Vilmos Zsigmond used railroad tracks and highways as leading lines in "The Deer Hunter." Roger Deakins uses architectural lines in "Skyfall" — particularly in the Shanghai skyscraper sequence — to pull the eye through complex compositions. Christopher Doyle exploits the narrow corridors and alleyways of Hong Kong as natural leading lines in Wong Kar-wa…

**When to use.** Choose leading lines when the eye needs a clear route through a complex environment. Roads, fences, corridors, beams, shadows, and rows of objects can pull attention toward a distant subject or deeper into the frame. The technique is useful for journeys, reveals, architecture, and scale. Lines must lead somewhere relevant; if they terminate at empty space or compete with several focal points, the…

**Directing the AI.** Select one family of lines in the environment and aim their convergence toward the subject or intended vanishing point. Use camera height and lens perspective to strengthen the pull without bending every structure unnaturally. Let fog, distance, or tonal falloff simplify the far end of the frame. Keep the subject distinct where the lines meet. For video, reveal or intensify the convergence through forward movement, while maintaining a stable destination for the viewer's eye.

**Common mistakes.**
- Using strong converging lines that point away from the subject, sending attention toward an irrelevant edge or empty corner.
- Combining several conflicting line systems, leaving the eye trapped between architecture, shadows, and horizon with no destination.
- Warping straight structures excessively to force convergence, making the spatial design feel synthetic rather than observed.

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
python platform/query.py technique-motions leading-lines
```

## Sources

- Rules of Shot Composition in Film

## Related techniques

- [('symmetry', 'symmetry')](('symmetry', 'symmetry').md)
- [('foreground-interest', 'foreground-interest')](('foreground-interest', 'foreground-interest').md)
- [('deep-focus', 'deep-focus')](('deep-focus', 'deep-focus').md)
- [('rule-of-thirds', 'rule-of-thirds')](('rule-of-thirds', 'rule-of-thirds').md)
- [('framing-within-frame', 'framing-within-frame')](('framing-within-frame', 'framing-within-frame').md)
- [('negative-space', 'negative-space')](('negative-space', 'negative-space').md)
- [('shallow-focus', 'shallow-focus')](('shallow-focus', 'shallow-focus').md)
- [('mise-en-scene', 'mise-en-scene')](('mise-en-scene', 'mise-en-scene').md)
- [('golden-ratio', 'golden-ratio')](('golden-ratio', 'golden-ratio').md)
