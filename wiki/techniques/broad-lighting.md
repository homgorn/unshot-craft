# "Broad Lighting Prompt for AI Image & Video"

`broad-lighting` · Lighting · level basic

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Broad lighting on [Subject] with the key illuminating the wider camera-facing side, creating an open and warm appearance with minimal shadow visible, the widening effect making the face appear fuller and more inviting, a soft box key with matching soft fill creating low contrast, shot on an 85mm lens at f/4, the even clean illumination of a romantic comedy close-up, Kodak Portra-inspired warm skin rendition
```

The side of the face turned toward the camera receives the key light, widening the apparent face shape and creating a brighter, more open look. Broad lighting is commonly used in comedy and romantic genres where an open, welcoming quality is desired. Classic Hollywood glamour photographers like Clarence Sinclair Bull used broad lighting for approachable star portraits. In cinema, broad lighting is the default for high-key comedic scenes and sitcom-style dialogue. It works against the conventional wisdom of dramatic lighting, deliberately choosing the wider, flatter option for warmth and acces…

**When to use.** Use broad lighting when a portrait should feel open, warm, accessible, or gently flattering rather than secretive. It works well for comedy, romance, interviews, and dialogue where facial information needs to arrive without friction. Because the wider camera-facing side receives the key, the face appears fuller and brighter. Choose it deliberately for emotional ease, and avoid it when the charact…

**Directing the AI.** Turn the subject slightly away from camera, then place the key so it illuminates the broader face plane still visible to the viewer. Use a large soft source and restrained fill, keeping only a narrow shadow on the far side. Maintain warm skin and open eyes without flattening every contour. The camera-facing cheek should carry the brightest area. Across video coverage, preserve the subject's turn and key direction; reversing either one accidentally changes the portrait into short lighting.

**Common mistakes.**
- Lighting the narrow far cheek instead of the broad camera-facing plane, accidentally creating the opposite portrait pattern.
- Filling every facial shadow to the same value, turning an open look into flat, directionless illumination.
- Using broad lighting for a scene built on concealment, where its welcoming clarity works against the intended tension.

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
python platform/query.py technique-motions broad-lighting
```

## Sources

- Film Lighting

## Related techniques

- [('high-key-lighting', 'high-key-lighting')](('high-key-lighting', 'high-key-lighting').md)
- [('soft-light', 'soft-light')](('soft-light', 'soft-light').md)
- [('fill-light', 'fill-light')](('fill-light', 'fill-light').md)
- [('three-point-lighting', 'three-point-lighting')](('three-point-lighting', 'three-point-lighting').md)
- [('key-light', 'key-light')](('key-light', 'key-light').md)
- [('low-key-lighting', 'low-key-lighting')](('low-key-lighting', 'low-key-lighting').md)
- [('chiaroscuro', 'chiaroscuro')](('chiaroscuro', 'chiaroscuro').md)
- [('rembrandt-lighting', 'rembrandt-lighting')](('rembrandt-lighting', 'rembrandt-lighting').md)
- [('silhouette', 'silhouette')](('silhouette', 'silhouette').md)
