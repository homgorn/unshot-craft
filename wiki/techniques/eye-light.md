# "Eye Light Prompt for AI Image & Video"

`eye-light` · Lighting · level intermediate

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Eye light close-up of [Subject] with brilliant catchlights sparkling in the irises, a dedicated small source just above the camera creating twin points of reflected light that bring the entire face to life, the subtle difference between eyes with and without this light is the difference between a living portrait and a death mask, shot in close-up on a 100mm macro lens at T2.8, warm golden skin tones, the tiny technical detail that separates professional cinematography from amateur work
```

A small, dedicated light source positioned to create a catchlight — a bright reflection in the subject's eyes — that brings eyes to life and creates a vital connection with the viewer. The eye light has been an essential tool since Hollywood's Golden Age, when cinematographers like Lee Garmes used tiny "inky" lights to add sparkle to Marlene Dietrich's eyes. Eyes without catchlights appear dead on screen — a fact horror filmmakers exploit deliberately. Steven Spielberg's cinematographers are known for precise eye lights; Janusz Kamiński's eye lights in "Schindler's List" are often the only br…

**When to use.** Eye light matters in close portraits where the audience must connect with a character's gaze. Use it when the broader lighting leaves the eyes dull, dark, or emotionally absent, especially in dramatic close-ups and reaction shots. A small catchlight can restore presence without changing the rest of the face. Remove it deliberately only when lifelessness, concealment, or horror is the point; other…

**Directing the AI.** Place a small dedicated source just above and near the camera axis. Ask for compact, matching catchlights in both visible irises, positioned consistently with the source and shaped by its aperture. Keep the reflections bright but not larger than the pupils, and preserve natural iris texture around them. The eye light should not lift the entire face. For video, lock the reflections to the curved eyes as the head turns; they should shift subtly, never float or remain fixed in screen space.

**Common mistakes.**
- Making catchlights huge or perfectly decorative, so the eyes resemble glossy illustrations rather than reflections from a small source.
- Placing different catchlight shapes or directions in each eye, breaking the shared geometry of the lighting setup.
- Brightening the entire face to create eye sparkle, which changes the scene instead of adding one precise reflection.

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
python platform/query.py technique-motions eye-light
```

## Sources

- Film Lighting

## Related techniques

- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('extreme-close-up', 'extreme-close-up')](('extreme-close-up', 'extreme-close-up').md)
- [('reaction-shot', 'reaction-shot')](('reaction-shot', 'reaction-shot').md)
- [('three-point-lighting', 'three-point-lighting')](('three-point-lighting', 'three-point-lighting').md)
- [('key-light', 'key-light')](('key-light', 'key-light').md)
- [('high-key-lighting', 'high-key-lighting')](('high-key-lighting', 'high-key-lighting').md)
- [('low-key-lighting', 'low-key-lighting')](('low-key-lighting', 'low-key-lighting').md)
- [('chiaroscuro', 'chiaroscuro')](('chiaroscuro', 'chiaroscuro').md)
- [('rembrandt-lighting', 'rembrandt-lighting')](('rembrandt-lighting', 'rembrandt-lighting').md)
