# "Silhouette Prompt for AI Image & Video"

`silhouette` · Lighting · level basic

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
[Subject] reduced to a pure dark silhouette against an intensely bright backlight source, all surface detail eliminated leaving only iconic form and outline, strong rim light tracing edges, high contrast, Kodak Double-X black and white stock
```

Subject appears as a dark shape against a bright background, with all surface detail eliminated, reducing characters to pure form and creating iconic, mythic, or anonymous images. David Lean created one of cinema's most recognizable silhouettes with Peter O'Toole against the desert sun in "Lawrence of Arabia." Steven Spielberg's E.T. bicycle silhouette against the moon became one of the most iconic images in film history. Terrence Malick uses human silhouettes against twilight skies throughout "The Thin Red Line" and "Days of Heaven" to reduce characters to archetypal figures against an indif…

**When to use.** Use a silhouette when identity should give way to shape, gesture, or archetype. It can make a figure mythic, anonymous, romantic, threatening, or small against a bright world. The outline must communicate the action because interior detail disappears. Choose distinctive profiles and separated limbs. Avoid silhouettes for moments that depend on facial performance, costume texture, or subtle inform…

**Directing the AI.** Place the strongest light source directly behind the subject and expose for the bright sky, doorway, moon, or screen. Reduce the figure to near-black with no visible facial or surface detail. Separate arms, legs, props, and profile so the outline reads instantly, then add only a thin edge trace if needed. Keep the background simple and luminous. In video, choreograph lateral movement that preserves the silhouette instead of merging body parts together.

**Common mistakes.**
- Lifting shadow detail inside the figure, weakening the graphic reduction that makes a silhouette instantly recognizable.
- Overlapping limbs and props against the torso, creating an unreadable dark mass instead of expressive outline.
- Using a cluttered bright background whose shapes compete with the subject's edge and destroy figure-ground clarity.

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
| declared | `brand-ink-open` | opening | 83 | `brand-ink-open` |

```
python platform/query.py technique-motions silhouette
```

## Sources

- Film Lighting

## Related techniques

- [('backlight', 'backlight')](('backlight', 'backlight').md)
- [('figure-ground', 'figure-ground')](('figure-ground', 'figure-ground').md)
- [('golden-hour', 'golden-hour')](('golden-hour', 'golden-hour').md)
- [('three-point-lighting', 'three-point-lighting')](('three-point-lighting', 'three-point-lighting').md)
- [('key-light', 'key-light')](('key-light', 'key-light').md)
- [('high-key-lighting', 'high-key-lighting')](('high-key-lighting', 'high-key-lighting').md)
- [('low-key-lighting', 'low-key-lighting')](('low-key-lighting', 'low-key-lighting').md)
- [('chiaroscuro', 'chiaroscuro')](('chiaroscuro', 'chiaroscuro').md)
- [('rembrandt-lighting', 'rembrandt-lighting')](('rembrandt-lighting', 'rembrandt-lighting').md)
