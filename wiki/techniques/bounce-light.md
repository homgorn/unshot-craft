# "Bounce Light Prompt for AI Image & Video"

`bounce-light` · Lighting · level intermediate

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Bounce light wrapping gently around [Subject], light reflected off a nearby surface creating soft warm illumination with no discernible directional shadow, the walls themselves becoming luminous secondary sources, shot on Alexa with Cooke S7 lenses for gentle roll-off into highlights, the naturalistic invisible lighting that Sven Nykvist spent a lifetime perfecting, light that serves the subject without announcing itself
```

Light reflected off a surface — wall, ceiling, or reflector — before hitting the subject, creating a soft, indirect illumination with a natural quality. Sven Nykvist perfected bounce lighting for Ingmar Bergman, often bouncing light off white ceilings and walls in "Cries and Whispers" to create his celebrated naturalistic look. Roger Deakins frequently bounces light off muslin and bead board to create his subtle, invisible lighting in films like "Fargo" and "A Beautiful Mind." The technique is fundamental to modern naturalistic cinematography, where visible movie lights would break the illusi…

**When to use.** Use bounce light for interiors and portraits that should feel naturally illuminated without an obvious movie source. It is ideal when direct light looks harsh, creates unwanted shadows, or breaks the location's realism. Bouncing can turn a wall, ceiling, or reflector into a large source that wraps faces and objects. Choose the reflecting surface carefully because its position, color, and size wil…

**Directing the AI.** Name the original source and the surface it strikes before reaching the subject. Ask for a broad return from a nearby pale wall or ceiling, with gentle wrap and no hard directional shadow. The bounce should inherit a subtle warmth or color cast from that surface, not appear perfectly neutral by default. Preserve a believable falloff across the room. For moving scenes, keep the indirect source anchored to the architecture so faces brighten and dim according to their distance from it.

**Common mistakes.**
- Describing soft light without identifying a reflecting surface, leaving the illumination direction arbitrary and spatially unconvincing.
- Bouncing from a strongly colored wall while asking for neutral skin, creating a contradiction in the scene's light behavior.
- Making every corner equally bright, which removes the natural falloff that gives indirect illumination its believable spatial depth.

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
python platform/query.py technique-motions bounce-light
```

## Sources

- Film Lighting

## Related techniques

- [('soft-light', 'soft-light')](('soft-light', 'soft-light').md)
- [('available-light', 'available-light')](('available-light', 'available-light').md)
- [('motivated-lighting', 'motivated-lighting')](('motivated-lighting', 'motivated-lighting').md)
- [('three-point-lighting', 'three-point-lighting')](('three-point-lighting', 'three-point-lighting').md)
- [('key-light', 'key-light')](('key-light', 'key-light').md)
- [('high-key-lighting', 'high-key-lighting')](('high-key-lighting', 'high-key-lighting').md)
- [('low-key-lighting', 'low-key-lighting')](('low-key-lighting', 'low-key-lighting').md)
- [('chiaroscuro', 'chiaroscuro')](('chiaroscuro', 'chiaroscuro').md)
- [('rembrandt-lighting', 'rembrandt-lighting')](('rembrandt-lighting', 'rembrandt-lighting').md)
