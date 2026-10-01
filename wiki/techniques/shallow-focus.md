# "Shallow Focus Prompt for AI Image & Video"

`shallow-focus` · Composition · level basic

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Shallow focus portrait of [Subject] with only the face in razor-sharp focus while everything else dissolves into a tapestry of luminous color and bokeh, the depth of field so narrow that even the near ear goes soft, shot on a Zeiss Master Prime 85mm at T1.4 wide open, the large format sensor transforming the background into abstract painting, the Wong Kar-wai visual poetry of focus as desire
```

Using a very narrow depth of field so only the subject is sharp while everything else melts into soft blur, isolating the subject and creating an intimate, dreamy quality. Wong Kar-wai and Christopher Doyle use extremely shallow focus in "In the Mood for Love" and "Chungking Express" to create their signature romantic, ephemeral atmosphere. Terrence Malick's work with Emmanuel Lubezki frequently employs razor-thin focus planes in natural light. The rise of large-sensor digital cameras and fast cine lenses has made shallow focus more accessible than ever, but master cinematographers like Hoyte…

**When to use.** Shallow focus is useful when one face, eye, hand, or object must dominate a crowded or intimate frame. It can turn a literal environment into color and light, giving portraits a romantic, fragile, or subjective quality. The technique also helps hide distracting backgrounds. Use it with discipline: decide the exact focus plane and emotional reason for excluding information, especially when subject…

**Directing the AI.** Choose a single narrow focus plane and name what must remain sharp, such as the nearer eye or a hand-held object. Let the near ear, foreground, and background soften progressively rather than applying one uniform blur. Describe large soft bokeh shapes only where real highlights exist. Preserve clean edges at the focal plane. In video, hold focus on the chosen detail through subtle movement or specify a deliberate rack; do not let sharpness jump between unrelated surfaces.

**Common mistakes.**
- Blurring the background uniformly like a cutout mask, with no gradual transition through foreground, subject depth, and distance.
- Leaving both eyes equally sharp in a steeply angled close-up despite asking for an extremely narrow focus plane.
- Using shallow focus when several spatial relationships matter, hiding story information that the audience needs to compare.

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
| declared | `depth-layer-moves` | camera | 150 | `dolly-zoom-real` |
| declared | `depth-layer-moves` | camera | 150 | `multiplane-real` |

```
python platform/query.py technique-motions shallow-focus
```

## Sources

- Rules of Shot Composition in Film

## Related techniques

- [('depth-of-field', 'depth-of-field')](('depth-of-field', 'depth-of-field').md)
- [('bokeh', 'bokeh')](('bokeh', 'bokeh').md)
- [('rack-focus', 'rack-focus')](('rack-focus', 'rack-focus').md)
- [('rule-of-thirds', 'rule-of-thirds')](('rule-of-thirds', 'rule-of-thirds').md)
- [('symmetry', 'symmetry')](('symmetry', 'symmetry').md)
- [('leading-lines', 'leading-lines')](('leading-lines', 'leading-lines').md)
- [('framing-within-frame', 'framing-within-frame')](('framing-within-frame', 'framing-within-frame').md)
- [('negative-space', 'negative-space')](('negative-space', 'negative-space').md)
- [('deep-focus', 'deep-focus')](('deep-focus', 'deep-focus').md)
