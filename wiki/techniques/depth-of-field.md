# "Depth of Field Prompt for AI Image & Video"

`depth-of-field` · Composition · level basic

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Selective depth of field isolating [Subject] in a narrow focused slice, everything in front and behind melting into graduated blur, the cinematic depth of field that modern anamorphic and large-format cinematography has made the visual signature of prestige filmmaking, shot on a large format sensor with an 85mm lens at T1.3
```

The range of distance in a scene that appears acceptably sharp — manipulating depth of field controls what the viewer focuses on and how they perceive spatial depth. The creative use of depth of field defines entirely different cinematic schools: Gregg Toland's infinite depth in "Citizen Kane" versus the paper-thin focus of Wong Kar-wai's films. Robert Richardson uses depth of field as an emotional instrument in Oliver Stone's "JFK" and Tarantino's "The Hateful Eight." Modern large-format sensors on cameras like the ARRI Alexa 65 have given cinematographers like Hoyte van Hoytema and Linus Sa…

**When to use.** Depth of field is a core choice whenever the audience needs guidance about where to look and how much of the space matters. Narrow focus isolates emotion or detail; broad focus reveals relationships across the frame. Use it to control intimacy, suspense, information, and spatial depth. Decide before prompting whether the background is context, distraction, or active story. That decision should de…

**Directing the AI.** State the nearest and farthest distances that should appear sharp, then identify the exact focal subject. For selective depth, ask for progressive blur before and behind that plane; for broad depth, preserve readable detail through foreground, middle ground, and background. Match apparent focus behavior to perspective and distance. In video, specify whether focus stays locked, follows the subject, or transfers deliberately between planes. Keep the transition smooth and motivated by attention.

**Common mistakes.**
- Requesting cinematic depth of field without naming a focus plane, leaving sharpness arbitrary and unstable across the image.
- Applying equal blur to objects at different distances, which destroys the gradual spatial cues created by optical focus.
- Keeping the background soft when its action carries essential story information that should remain available to the viewer.

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
python platform/query.py technique-motions depth-of-field
```

## Sources

- Rules of Shot Composition in Film

## Related techniques

- [('shallow-focus', 'shallow-focus')](('shallow-focus', 'shallow-focus').md)
- [('deep-focus', 'deep-focus')](('deep-focus', 'deep-focus').md)
- [('rack-focus', 'rack-focus')](('rack-focus', 'rack-focus').md)
- [('rule-of-thirds', 'rule-of-thirds')](('rule-of-thirds', 'rule-of-thirds').md)
- [('symmetry', 'symmetry')](('symmetry', 'symmetry').md)
- [('leading-lines', 'leading-lines')](('leading-lines', 'leading-lines').md)
- [('framing-within-frame', 'framing-within-frame')](('framing-within-frame', 'framing-within-frame').md)
- [('negative-space', 'negative-space')](('negative-space', 'negative-space').md)
- [('mise-en-scene', 'mise-en-scene')](('mise-en-scene', 'mise-en-scene').md)
