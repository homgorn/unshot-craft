# "Triangular Composition Prompt for AI Image & Video"

`triangular-composition` · Composition · level intermediate

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Triangular composition with [Subject] arranged to form a triangle within the frame, the apex drawing the eye first then naturally guiding it down along the diagonal lines to the base, shot on a 50mm lens at eye level, the classical compositional structure that Da Vinci and Kurosawa both understood as the geometry of power and stability
```

Arranging key elements to form a triangle within the frame, creating a stable, hierarchical structure that naturally guides the eye between three points of interest. Renaissance painters like Leonardo da Vinci used triangular composition as a foundation — the Mona Lisa and The Last Supper are both built on triangular structures. Akira Kurosawa arranges his samurai in triangular formations for stability and power in "Seven Samurai." Steven Spielberg uses triangular staging in his group dialogue scenes, and Kubrick's symmetrical compositions often embed triangular sub-structures that give the f…

**When to use.** Triangular composition works when three people, objects, or visual anchors need a stable relationship and clear hierarchy. It suits group dialogue, leadership tableaux, family scenes, and moments where an apex should dominate two supporting points. The eye naturally moves around the triangle, making dense blocking easier to read. Use variation in height and spacing; a perfectly equilateral arrang…

**Directing the AI.** Choose the dominant subject as the apex and place two secondary anchors lower and farther apart to form the base. Use gaze, shoulders, furniture, or architectural lines to reinforce the triangle without drawing it literally. Keep each point visually distinct and prevent overlapping heads. Adjust height and width to control stability: a broad base feels grounded, while a narrow steep form feels more hierarchical. In video, preserve the relationship through blocking as speakers shift attention.

**Common mistakes.**
- Placing three figures on one horizontal line, which removes the apex and collapses the intended hierarchy.
- Drawing obvious triangular props around the group, making the underlying compositional structure feel literal and forced.
- Overlapping the lower anchors behind the dominant subject, so the three points cannot be read as separate positions.

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
python platform/query.py technique-motions triangular-composition
```

## Sources

- Rules of Shot Composition in Film

## Related techniques

- [('three-shot', 'three-shot')](('three-shot', 'three-shot').md)
- [('balancing-elements', 'balancing-elements')](('balancing-elements', 'balancing-elements').md)
- [('visual-weight', 'visual-weight')](('visual-weight', 'visual-weight').md)
- [('rule-of-thirds', 'rule-of-thirds')](('rule-of-thirds', 'rule-of-thirds').md)
- [('symmetry', 'symmetry')](('symmetry', 'symmetry').md)
- [('leading-lines', 'leading-lines')](('leading-lines', 'leading-lines').md)
- [('framing-within-frame', 'framing-within-frame')](('framing-within-frame', 'framing-within-frame').md)
- [('negative-space', 'negative-space')](('negative-space', 'negative-space').md)
- [('shallow-focus', 'shallow-focus')](('shallow-focus', 'shallow-focus').md)
