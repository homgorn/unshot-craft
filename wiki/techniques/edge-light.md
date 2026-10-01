# "Edge Light Prompt for AI Image & Video"

`edge-light` · Lighting · level intermediate

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Edge light tracing the complete outline of [Subject] against darkness, a thin bright line following every contour from crown to fingertips, the face and front in complete shadow with no fill, only the bright edge visible, individual hair strands creating a fiber-optic halo effect, shot on a 135mm lens at T2 to compress the background into a seamless void, the cinematic elegance of defining a form by outline alone
```

A thin line of light that traces the outline of a subject, separating them from the background and creating a refined, cinematic look that adds depth and visual polish. Ridley Scott and his frequent cinematographer John Mathieson use edge lighting extensively in "Gladiator" and "Kingdom of Heaven" to make armored warriors pop against dark battle backgrounds. Roger Deakins uses hairline edge lights in "Blade Runner 2049" where characters are often defined more by their luminous outlines than their illuminated faces. The technique is also fundamental to music video and commercial cinematography…

**When to use.** Choose edge light when shape matters more than frontal detail, or when a dark subject needs refined separation from a dark background. It is effective for profiles, armor, fashion, music performance, smoke, and restrained sci-fi imagery. A thin contour can make the frame feel polished without exposing the face. Use it to reveal silhouette and surface boundaries, not as a universal glow; the line…

**Directing the AI.** Position a narrow source behind the subject so it grazes the outer contour. Specify which edges catch light, from crown and hair strands to shoulder, arm, or object rim, while the front remains dark or minimally filled. Keep the line thin and brightest where the angle reflects toward camera. Avoid equal intensity around the whole body. In video, let the illuminated contour migrate with rotation, revealing different edges as geometry changes relative to the fixed source.

**Common mistakes.**
- Drawing a complete uniform outline around the subject, including edges hidden from or facing away from the source.
- Widening the edge until it spills across the face and torso, replacing elegant separation with broad backlighting.
- Using a background equally bright as the rim, which removes the contrast required for clean contour definition.

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
python platform/query.py technique-motions edge-light
```

## Sources

- Film Lighting

## Related techniques

- [('backlight', 'backlight')](('backlight', 'backlight').md)
- [('kicker-light', 'kicker-light')](('kicker-light', 'kicker-light').md)
- [('silhouette', 'silhouette')](('silhouette', 'silhouette').md)
- [('three-point-lighting', 'three-point-lighting')](('three-point-lighting', 'three-point-lighting').md)
- [('key-light', 'key-light')](('key-light', 'key-light').md)
- [('high-key-lighting', 'high-key-lighting')](('high-key-lighting', 'high-key-lighting').md)
- [('low-key-lighting', 'low-key-lighting')](('low-key-lighting', 'low-key-lighting').md)
- [('chiaroscuro', 'chiaroscuro')](('chiaroscuro', 'chiaroscuro').md)
- [('rembrandt-lighting', 'rembrandt-lighting')](('rembrandt-lighting', 'rembrandt-lighting').md)
