# "Head-On Shot Prompt for AI Image & Video"

`head-on-shot` · Camera Work · level intermediate

Reference video: `media/head-on-shot.mp4`

## Prompt (verbatim, `[Subject]` intact)

```
Head-on shot of [Subject] moving directly toward the camera with perfect bilateral symmetry, the camera holding its ground as the figure grows larger in frame, shot on anamorphic 40mm Panavision C-series glass with slight barrel distortion adding menace, teal shadows and amber highlights, the confrontational energy of direct approach
```

A shot where the subject moves or faces directly toward the camera, creating a confrontational, powerful feeling as the subject approaches or stares directly at the viewer. Stanley Kubrick mastered the head-on shot with his famous "Kubrick stare" — characters like Alex in "A Clockwork Orange" and Jack Torrance in "The Shining" glaring directly into the lens with menacing intensity. Spike Lee's double-dolly head-on shots place characters in direct communion with the audience, while Wes Anderson uses symmetrical head-on framing as a core visual signature in every film.

**When to use.** Use a head-on shot when a character must confront the audience or advance with undeniable force. Direct eye contact can signal menace, confidence, accusation, or eerie calm, while forward movement steadily increases pressure. Symmetry makes the approach feel controlled and inevitable. Save this angle for decisive entrances, threats, revelations, or stylized portraiture; repeated use can turn conf…

**Directing the AI.** Center the subject on the lens axis and establish perfect bilateral balance around them. Have the camera hold position while the figure faces or walks directly toward it, growing from a smaller frame to a dominant one. Use a moderately wide anamorphic perspective with slight barrel distortion, teal shadows, and amber highlights to add pressure. Keep lateral drift near zero. The gaze, shoulders, and direction of travel should all point straight into the camera.

**Common mistakes.**
- Letting the subject approach diagonally, which changes the shot from direct confrontation into ordinary tracking coverage.
- Breaking symmetry with accidental background clutter that distracts from the figure's controlled movement toward the lens.
- Using a cheerful wide-angle distortion when the intended emotion depends on menace, authority, or focused intensity.

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
| declared | `basic-3d-scene` | camera | 180 | `basic-3d-scene` |

```
python platform/query.py technique-motions head-on-shot
```

## Sources

- 50+ Types of Camera Shots, Angles, and Techniques

## Related techniques

- [('centered-composition', 'centered-composition')](('centered-composition', 'centered-composition').md)
- [('push-in', 'push-in')](('push-in', 'push-in').md)
- [('low-angle-shot', 'low-angle-shot')](('low-angle-shot', 'low-angle-shot').md)
- [('aerial-shot', 'aerial-shot')](('aerial-shot', 'aerial-shot').md)
- [('birds-eye-view', 'birds-eye-view')](('birds-eye-view', 'birds-eye-view').md)
- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('dutch-angle', 'dutch-angle')](('dutch-angle', 'dutch-angle').md)
- [('dolly-shot', 'dolly-shot')](('dolly-shot', 'dolly-shot').md)
- [('establishing-shot', 'establishing-shot')](('establishing-shot', 'establishing-shot').md)
