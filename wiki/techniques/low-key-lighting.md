# "Low-Key Lighting Prompt for AI Image & Video"

`low-key-lighting` · Lighting · level intermediate

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Low-key lighting on [Subject] with deep impenetrable shadows claiming eighty percent of the frame, only a single source illuminating a small area, the contrast ratio pushed to 8:1 between highlights and shadows, shot on Kodak Double-X black and white stock with a 40mm Baltar lens, the inky blacks and silver highlights of classic film noir, John Alton-level mastery of darkness as an active compositional element
```

A dramatic lighting style dominated by deep shadows and high contrast where only select areas are illuminated, creating mystery, tension, and a noir-like atmosphere. John Alton literally wrote the book — "Painting with Light" — and defined low-key noir cinematography in films like "The Big Combo" and "T-Men." Gordon Willis pushed low-key to its extreme in "The Godfather," with Marlon Brando's eyes often invisible in shadow. Bradford Young's low-key work in "Arrival" and "Selma" brought a moody, naturalistic darkness to modern cinema, and Robert Richardson uses low-key lighting in Tarantino's…

**When to use.** Use low-key lighting when darkness should occupy the frame as an active dramatic force. It suits mystery, crime, horror, secrecy, moral ambiguity, and intimate scenes where only selected information is revealed. Strong contrast can direct attention with remarkable precision. The goal is not merely to make everything dim; retain a readable highlight structure so faces, objects, and silhouettes eme…

**Directing the AI.** Let roughly eighty percent of the frame fall into deep shadow and assign one controlled source to the essential face, hand, or object. Push the contrast toward an 8:1 relationship while preserving texture in chosen highlights and allowing other areas to vanish. Use inky blacks, silver or warm highlights, and negative fill to prevent ambient spill. Keep the beam motivated and narrowly shaped. For motion, ensure the subject passes through planned islands of light.

**Common mistakes.**
- Underexposing the entire image evenly, which creates muddy darkness without the selective highlight structure low key requires.
- Opening shadows with excessive fill, weakening mystery and turning the setup into ordinary balanced lighting.
- Crushing every black area identically, leaving no separation between subject, wardrobe, and background where readability matters.

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
| declared | `spotlight-hero-card` | opening | 220 | `spotlight-hero-card` |

```
python platform/query.py technique-motions low-key-lighting
```

## Sources

- Film Lighting

## Related techniques

- [('chiaroscuro', 'chiaroscuro')](('chiaroscuro', 'chiaroscuro').md)
- [('film-noir', 'film-noir')](('film-noir', 'film-noir').md)
- [('hard-light', 'hard-light')](('hard-light', 'hard-light').md)
- [('three-point-lighting', 'three-point-lighting')](('three-point-lighting', 'three-point-lighting').md)
- [('key-light', 'key-light')](('key-light', 'key-light').md)
- [('high-key-lighting', 'high-key-lighting')](('high-key-lighting', 'high-key-lighting').md)
- [('rembrandt-lighting', 'rembrandt-lighting')](('rembrandt-lighting', 'rembrandt-lighting').md)
- [('silhouette', 'silhouette')](('silhouette', 'silhouette').md)
- [('golden-hour', 'golden-hour')](('golden-hour', 'golden-hour').md)
