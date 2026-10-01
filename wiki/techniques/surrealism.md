# "Surrealism Prompt for AI Image & Video"

`surrealism` · Film Genres · level advanced

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Surrealist scene with [Subject] in a world where dream logic replaces physical reality, impossible elements presented with the matter-of-fact certainty of documentary, lighting impossibly motivated from sources that do not exist, the Bunuel-Lynch visual language where the subconscious mind's architecture is rendered as physical space, the unsettling beauty of a world where logic has been replaced by feeling
```

A movement drawing on dreams, the subconscious, and irrational imagery to create art that defies logic — melting clocks, impossible architecture, dream logic replacing narrative cause-and-effect. Luis Buñuel and Salvador Dalí created cinema's first surrealist film, "Un Chien Andalou" (1929), with its infamous eye-slicing opening. Buñuel continued making surrealist cinema for fifty years through "The Discreet Charm of the Bourgeoisie." David Lynch is surrealism's modern heir — "Eraserhead," "Mulholland Drive," and "Twin Peaks: The Return" operate on dream logic. Alejandro Jodorowsky's "El Topo…

**When to use.** Use surrealism when subconscious feeling, desire, dread, or contradiction matters more than literal cause and effect. It suits dreams, identity fractures, psychological transitions, and worlds where impossible events reveal emotional truth. Establish a visual rule that belongs to the scene's feeling, then treat it as ordinary. Random strangeness is not enough; the strongest surreal image is speci…

**Directing the AI.** Place the subject in a recognizable setting, then alter one governing reality: scale, gravity, architecture, identity, or time. Present the impossible element with neutral framing and documentary certainty rather than fantasy spectacle. Motivate light from sources that visibly cannot exist, but keep surfaces and shadows internally consistent. Repeat a shape or action to establish dream logic. Let emotion determine transitions, while preserving enough spatial continuity that the viewer can inhab…

**Common mistakes.**
- Filling the frame with unrelated strange objects, creating visual novelty without emotional or thematic logic.
- Lighting impossible events like spectacular fantasy, which weakens their calm and unsettling matter-of-fact quality.
- Changing the world's rules every moment, leaving no dream logic for the audience to follow.

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
| declared | `magician-card-flourish` | opening | 9 | `magician-card-flourish` |

```
python platform/query.py technique-motions surrealism
```

## Sources

- Genres: Where to Draw the Line?

## Related techniques

- [('morphing', 'morphing')](('morphing', 'morphing').md)
- [('reverse-motion', 'reverse-motion')](('reverse-motion', 'reverse-motion').md)
- [('symbolism', 'symbolism')](('symbolism', 'symbolism').md)
- [('film-noir', 'film-noir')](('film-noir', 'film-noir').md)
- [('german-expressionism', 'german-expressionism')](('german-expressionism', 'german-expressionism').md)
- [('cinema-verite', 'cinema-verite')](('cinema-verite', 'cinema-verite').md)
- [('french-new-wave', 'french-new-wave')](('french-new-wave', 'french-new-wave').md)
- [('found-footage', 'found-footage')](('found-footage', 'found-footage').md)
- [('spaghetti-western', 'spaghetti-western')](('spaghetti-western', 'spaghetti-western').md)
