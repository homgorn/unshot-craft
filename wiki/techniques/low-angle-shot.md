# "Low Angle Shot Prompt for AI Image & Video"

`low-angle-shot` · Camera Work · level basic

Reference video: `media/low-angle-shot.mp4`

## Prompt (verbatim, `[Subject]` intact)

```
Low angle shot looking up at [Subject] from below, the camera positioned at ground level shooting upward through converging vertical lines, shot on Cooke S4 18mm wide-angle lens exaggerating the height distortion, high-contrast Kodak Double-X black and white aesthetic, Citizen Kane grandeur
```

Camera positioned below the subject, looking up, making the subject appear dominant, powerful, heroic, or imposing. Orson Welles used low angles obsessively in "Citizen Kane," famously requiring trenches cut into studio floors to achieve extreme upward perspectives on Charles Foster Kane, visually encoding his megalomania into every frame. Quentin Tarantino's iconic trunk shots — looking up at characters from inside a car trunk — are a playful variation, and Christopher Nolan used low angles throughout "The Dark Knight" to make Batman a towering mythic figure against Gotham's skyline.

**When to use.** Use a low angle to make a person, structure, or object command the frame. The upward view can express authority, threat, heroism, arrogance, or awe depending on performance and light. It also lets architecture converge behind the subject, increasing apparent height. Choose it for power shifts and monumental introductions. Avoid using it automatically for every hero, since dominance without narrat…

**Directing the AI.** Lower the camera beneath the subject's eye line and point upward through converging walls, columns, or skyline. A wide lens can stretch height, but keep the face and body recognizable rather than grotesquely warped. Give the subject a firm stance and place open sky or strong architecture behind them. High-contrast monochrome treatment can reinforce authority. In motion, advance carefully or hold position; random tilt changes weaken the stable power relationship.

**Common mistakes.**
- Placing the lens only slightly below eye level, producing a neutral portrait with no meaningful upward pressure.
- Using an ultra-wide lens too close to the face, creating comic distortion instead of deliberate dominance.
- Ignoring the background, even though converging architecture or open sky is central to the angle's sense of scale.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` | **null** | kling-1.5 | no |
| `luma` | **null** | dream-machine | no |
| `mj61` | **null** | v6.1 | no |
| `pika15` | **null** | pika-1.5 | no |
| `runway_gen3` | **null** | gen-3-alpha | no |
| `sora` | **null** | sora-1 | no |
| `veo2` | **null** | veo-2 | no |

## Motion pairings

**Declared, not inferred.** These come from an explicit `styles:` list in `data/cinematic/<slug>.md`, authored in `platform/catalog/pairings.py`. Nothing here is matched by name similarity.

| kind | shot card | category | frames | style |
|---|---|---|---|---|
| declared | `steep-tilt-glide` | camera | 120 | `steep-tilt-glide` |

```
python platform/query.py technique-motions low-angle-shot
```

## Sources

- 50+ Types of Camera Shots, Angles, and Techniques

## Related techniques

- [('worms-eye-view', 'worms-eye-view')](('worms-eye-view', 'worms-eye-view').md)
- [('high-angle-shot', 'high-angle-shot')](('high-angle-shot', 'high-angle-shot').md)
- [('leading-lines', 'leading-lines')](('leading-lines', 'leading-lines').md)
- [('aerial-shot', 'aerial-shot')](('aerial-shot', 'aerial-shot').md)
- [('birds-eye-view', 'birds-eye-view')](('birds-eye-view', 'birds-eye-view').md)
- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('dutch-angle', 'dutch-angle')](('dutch-angle', 'dutch-angle').md)
- [('dolly-shot', 'dolly-shot')](('dolly-shot', 'dolly-shot').md)
- [('establishing-shot', 'establishing-shot')](('establishing-shot', 'establishing-shot').md)
