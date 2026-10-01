# "Framing Within Frame Prompt for AI Image & Video"

`framing-within-frame` · Composition · level intermediate

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Frame within a frame with [Subject] seen through a dark silhouette of an architectural opening, the framing device adding layers of depth and the voyeuristic feeling of observing from a hidden vantage, shot on a 35mm lens with exposure balanced for the subject making the surrounding frame go completely dark, the John Ford doorway composition that transforms a simple element into a metaphor for belonging and exclusion
```

Using elements within the scene — doorways, windows, arches, branches — to create a secondary frame around the subject, adding depth, drawing focus, and suggesting entrapment or voyeurism. John Ford used doorway framing iconically in "The Searchers" — the final shot of John Wayne framed in a cabin door is one of cinema's most analyzed compositions. Hitchcock used frame-within-frame throughout "Rear Window" with the apartment windows functioning as individual movie screens. Wes Anderson frequently frames characters through windows, doors, and proscenium arches to create his dollhouse aesthetic…

**When to use.** Use framing within frame when the environment should control how the audience sees a subject. A doorway can suggest exclusion, a window can create voyeurism, and an arch can add formal depth. The technique is valuable for surveillance, isolation, discovery, and layered location work. Choose a framing object that belongs to the scene and keep it subordinate. If the inner frame becomes more decorat…

**Directing the AI.** Place the camera behind or beyond a real foreground opening, then position the subject inside its boundaries. Let the outer frame fall darker, softer, or partially silhouetted so attention passes through it into the scene. Keep enough irregularity to preserve physical depth rather than making a graphic border. Align the inner opening with the subject's action or isolation. In video, allow the frame to reveal, conceal, or tighten through camera movement without clipping the focal action accident…

**Common mistakes.**
- Adding a decorative border with no physical relationship to the location, which reads as graphic design rather than staging.
- Letting the doorway, window, or branches cut through the subject's face and obscure essential expression without purpose.
- Exposing foreground and subject equally, flattening the depth layers that make the secondary frame visually useful.

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
| declared | `spotlight-hero-card` | opening | 220 | `spotlight-hero-card` |

```
python platform/query.py technique-motions framing-within-frame
```

## Sources

- Rules of Shot Composition in Film

## Related techniques

- [('foreground-interest', 'foreground-interest')](('foreground-interest', 'foreground-interest').md)
- [('figure-ground', 'figure-ground')](('figure-ground', 'figure-ground').md)
- [('negative-space', 'negative-space')](('negative-space', 'negative-space').md)
- [('rule-of-thirds', 'rule-of-thirds')](('rule-of-thirds', 'rule-of-thirds').md)
- [('symmetry', 'symmetry')](('symmetry', 'symmetry').md)
- [('leading-lines', 'leading-lines')](('leading-lines', 'leading-lines').md)
- [('shallow-focus', 'shallow-focus')](('shallow-focus', 'shallow-focus').md)
- [('deep-focus', 'deep-focus')](('deep-focus', 'deep-focus').md)
- [('mise-en-scene', 'mise-en-scene')](('mise-en-scene', 'mise-en-scene').md)
