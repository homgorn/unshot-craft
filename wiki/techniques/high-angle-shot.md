# "High Angle Shot Prompt for AI Image & Video"

`high-angle-shot` · Camera Work · level basic

Reference video: `media/high-angle-shot.mp4`

## Prompt (verbatim, `[Subject]` intact)

```
High angle shot looking down on [Subject], the perspective making them appear impossibly small and vulnerable, the camera positioned high above, shot on Arriflex with a 21mm wide lens to exaggerate spatial distortion, muted institutional color palette with a single color accent
```

Camera positioned above the subject, looking down, making the subject appear smaller, weaker, or more vulnerable while also providing a broader view of the scene layout. Alfred Hitchcock used high angles masterfully in "Psycho" and "Vertigo" to diminish characters and reveal their spatial entrapment. Orson Welles employed towering high angles in "The Trial" to crush Joseph K under oppressive bureaucratic architecture. More recently, Denis Villeneuve used high-angle compositions in "Prisoners" to convey the helplessness of parents searching for their missing children.

**When to use.** A high angle is useful when the viewer should understand both a subject and the forces surrounding them. Looking down can make a person feel vulnerable, trapped, watched, or physically diminished while revealing exits, barriers, and crowd positions. It works for helplessness and tactical overview without reaching the abstraction of a straight overhead view. Avoid assuming every downward angle aut…

**Directing the AI.** Raise the camera clearly above the subject and aim downward on a visible diagonal, preserving depth between foreground, person, and floor. Use a wide lens to expand the surrounding architecture and reduce the figure within it. Muted institutional colors with one controlled accent can isolate the subject. Show the boundaries, obstacles, or empty space responsible for the pressure. For video, hold or descend slowly rather than drifting into a fully vertical bird's eye composition.

**Common mistakes.**
- Pushing the camera directly overhead, which removes the diagonal depth and turns the setup into another technique.
- Isolating the subject against an empty floor without environmental elements that explain their vulnerability or confinement.
- Using extreme wide-angle distortion so aggressively that warped architecture becomes more important than the emotional hierarchy.

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
| declared | `overhead-camera-moves` | camera | 144 | `overhead-tabletop-drop` |
| declared | `overhead-camera-moves` | camera | 144 | `tilt-reveal` |

```
python platform/query.py technique-motions high-angle-shot
```

## Sources

- 50+ Types of Camera Shots, Angles, and Techniques

## Related techniques

- [('birds-eye-view', 'birds-eye-view')](('birds-eye-view', 'birds-eye-view').md)
- [('worms-eye-view', 'worms-eye-view')](('worms-eye-view', 'worms-eye-view').md)
- [('negative-space', 'negative-space')](('negative-space', 'negative-space').md)
- [('aerial-shot', 'aerial-shot')](('aerial-shot', 'aerial-shot').md)
- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('dutch-angle', 'dutch-angle')](('dutch-angle', 'dutch-angle').md)
- [('dolly-shot', 'dolly-shot')](('dolly-shot', 'dolly-shot').md)
- [('establishing-shot', 'establishing-shot')](('establishing-shot', 'establishing-shot').md)
- [('extreme-close-up', 'extreme-close-up')](('extreme-close-up', 'extreme-close-up').md)
