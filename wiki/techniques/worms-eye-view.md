# "Worm's Eye View Prompt for AI Image & Video"

`worms-eye-view` · Camera Work · level intermediate

Reference video: `media/worms-eye-view.mp4`

## Prompt (verbatim, `[Subject]` intact)

```
Worm's eye view from ground level looking straight up at [Subject], the perspective so extreme that vertical elements seem to lean inward and threaten to collapse, shot from a camera placed directly on the ground with a 14mm ultra-wide rectilinear lens pointed straight up, the barrel distortion adding to the vertiginous effect, the overwhelming scale from the perspective of the smallest creature
```

Camera placed at ground level looking straight up, the most extreme low angle, making everything tower above and creating a sense of awe, intimidation, or childlike wonder. Orson Welles was famous for his low-angle work in "Citizen Kane" and "The Trial," often requiring sets to be built with ceilings — unusual for the era. Terry Gilliam employs worm's eye views in "Brazil" and "12 Monkeys" to make bureaucratic architecture oppressive. Denis Villeneuve used ground-level upward shots in "Arrival" when the characters first approach the alien ship, capturing the vertigo of encountering something…

**When to use.** Choose a worm's eye view when the camera should occupy the smallest possible position beneath something immense. Looking almost straight up can make a building, creature, vehicle, or person feel oppressive, astonishing, or childishly wondrous. It is more extreme than a normal low angle and strongly abstracts space. Use it for encounters with scale; avoid it when facial readability or ordinary geo…

**Directing the AI.** Place the lens directly on the ground and aim nearly straight upward. Use an ultra-wide rectilinear perspective so vertical structures surge inward toward the sky while remaining recognizably architectural. Include a small ground-edge reference for scale and position the subject above or around the lens, not merely in front of it. Control barrel distortion rather than letting it dominate. In video, use a slow tilt or passing overhead movement, preserving the grounded viewpoint.

**Common mistakes.**
- Positioning the camera around waist height, which produces an ordinary low angle without the creature-level viewpoint.
- Aiming forward instead of upward, losing the collapsing verticals and overhead dominance central to the technique.
- Letting ultra-wide distortion bend every line randomly, turning controlled vertigo into an unreadable fisheye effect.

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
python platform/query.py technique-motions worms-eye-view
```

## Sources

- 50+ Types of Camera Shots, Angles, and Techniques

## Related techniques

- [('low-angle-shot', 'low-angle-shot')](('low-angle-shot', 'low-angle-shot').md)
- [('leading-lines', 'leading-lines')](('leading-lines', 'leading-lines').md)
- [('german-expressionism', 'german-expressionism')](('german-expressionism', 'german-expressionism').md)
- [('aerial-shot', 'aerial-shot')](('aerial-shot', 'aerial-shot').md)
- [('birds-eye-view', 'birds-eye-view')](('birds-eye-view', 'birds-eye-view').md)
- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('dutch-angle', 'dutch-angle')](('dutch-angle', 'dutch-angle').md)
- [('dolly-shot', 'dolly-shot')](('dolly-shot', 'dolly-shot').md)
- [('establishing-shot', 'establishing-shot')](('establishing-shot', 'establishing-shot').md)
