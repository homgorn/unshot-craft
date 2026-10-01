# "Negative Space Prompt for AI Image & Video"

`negative-space` · Composition · level intermediate

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Negative space composition with [Subject] occupying the extreme lower corner of the frame, the remaining ninety percent a vast expanse of emptiness, the scale relationship between the tiny figure and the overwhelming void creating a visceral feeling of isolation, shot on medium format with a 55mm lens at f/8 for clinical sharpness across the entire frame, the minimalist language of Antonioni where emptiness speaks louder than dialogue
```

Leaving large areas of the frame empty, with the subject occupying a small portion, creating breathing room, isolation, contemplation, or emphasizing the weight of absence. Michelangelo Antonioni was the master of negative space in films like "L'Avventura" and "Red Desert," where vast empty landscapes and blank walls dwarf his characters. Sofia Coppola uses negative space in "Lost in Translation" to visualize loneliness in Tokyo hotel rooms. Robert Bresson's austere compositions feature deliberate emptiness, and Chloé Zhao's "Nomadland" places Frances McDormand as a small figure against enorm…

**When to use.** Negative space works when what surrounds the subject should feel as important as the subject itself. Use it for solitude, anticipation, emotional distance, oppressive architecture, vast landscape, or room for text and motion. A small figure against emptiness can carry enormous weight, but the void still needs shape, tone, and direction. Empty space is not leftover space; it should sharpen the ide…

**Directing the AI.** Push the subject toward a corner or edge and reserve most of the frame for a controlled expanse of sky, wall, darkness, or landscape. Keep the empty field simple but not dead, using subtle texture, gradient, or atmospheric depth. Make the scale contrast unmistakable and prevent small background objects from filling the void. For video, hold the emptiness long enough to register, or let movement enter it deliberately rather than constantly recentering the subject.

**Common mistakes.**
- Leaving random unused space around a normally framed subject, which feels accidental rather than emotionally or compositionally charged.
- Filling the supposed void with detailed props, texture, and secondary figures until it no longer reads as absence.
- Centering the subject during motion, removing the asymmetry and expectation created by a large open field.

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
python platform/query.py technique-motions negative-space
```

## Sources

- Rules of Shot Composition in Film

## Related techniques

- [('extreme-long-shot', 'extreme-long-shot')](('extreme-long-shot', 'extreme-long-shot').md)
- [('visual-weight', 'visual-weight')](('visual-weight', 'visual-weight').md)
- [('rule-of-thirds', 'rule-of-thirds')](('rule-of-thirds', 'rule-of-thirds').md)
- [('symmetry', 'symmetry')](('symmetry', 'symmetry').md)
- [('leading-lines', 'leading-lines')](('leading-lines', 'leading-lines').md)
- [('framing-within-frame', 'framing-within-frame')](('framing-within-frame', 'framing-within-frame').md)
- [('shallow-focus', 'shallow-focus')](('shallow-focus', 'shallow-focus').md)
- [('deep-focus', 'deep-focus')](('deep-focus', 'deep-focus').md)
- [('mise-en-scene', 'mise-en-scene')](('mise-en-scene', 'mise-en-scene').md)
