# "High-Key Lighting Prompt for AI Image & Video"

`high-key-lighting` · Lighting · level basic

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
High-key lighting flooding [Subject] in bright even illumination with barely a shadow to be found, the overall exposure pushed a third of a stop hot to create an airy blown-out feeling, shot on Alexa at 1280 ISO with Cooke S7 glass for gentle halation around the highlights, the dreamy overlit aesthetic of warmth without shadows, optimism without darkness
```

A bright, even lighting style with minimal shadows that creates an optimistic, clean, or ethereal atmosphere, common in comedies, commercials, and dream sequences. The classic Hollywood musical relied on high-key lighting — Vincente Minnelli's "An American in Paris" and "The Band Wagon" glow with uniform brightness. Kubrick used clinical high-key lighting in the space station sequences of "2001" to create sterile futurism, and Sofia Coppola bathes "Marie Antoinette" in high-key pastel light to capture the candy-colored excess of Versailles. The technique is also fundamental to the visual lang…

**When to use.** Choose high-key lighting for optimism, cleanliness, glamour, romantic ease, clinical futurism, or a dreamlike lack of darkness. It works in comedy, commercials, musicals, beauty work, and deliberately sterile interiors. The frame should remain shaped even with minimal shadow. Use low contrast intentionally; simply overexposing a normal setup will lose skin, fabric, and production detail rather th…

**Directing the AI.** Surround the subject with broad, diffused illumination and keep the fill level close to the key so shadows remain pale and soft. Lift the overall exposure slightly while protecting facial and fabric highlights from clipping. Use light backgrounds, gentle halation, creamy skin, and restrained pastel color. Preserve subtle edge separation through small tonal differences rather than hard rims. For video, maintain stable brightness across movement so the subject does not fall into accidental contra…

**Common mistakes.**
- Confusing high key with blown highlights, erasing skin texture and white surfaces instead of controlling contrast.
- Removing every trace of direction, which makes the subject look flat rather than softly and evenly modeled.
- Placing dark background elements behind the subject that contradict the intended bright, low-contrast visual field.

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
python platform/query.py technique-motions high-key-lighting
```

## Sources

- Film Lighting

## Related techniques

- [('soft-light', 'soft-light')](('soft-light', 'soft-light').md)
- [('fill-light', 'fill-light')](('fill-light', 'fill-light').md)
- [('broad-lighting', 'broad-lighting')](('broad-lighting', 'broad-lighting').md)
- [('three-point-lighting', 'three-point-lighting')](('three-point-lighting', 'three-point-lighting').md)
- [('key-light', 'key-light')](('key-light', 'key-light').md)
- [('low-key-lighting', 'low-key-lighting')](('low-key-lighting', 'low-key-lighting').md)
- [('chiaroscuro', 'chiaroscuro')](('chiaroscuro', 'chiaroscuro').md)
- [('rembrandt-lighting', 'rembrandt-lighting')](('rembrandt-lighting', 'rembrandt-lighting').md)
- [('silhouette', 'silhouette')](('silhouette', 'silhouette').md)
