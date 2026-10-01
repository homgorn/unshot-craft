# "Pan Shot Prompt for AI Image & Video"

`pan-shot` · Camera Work · level basic

Reference video: `media/pan-shot.mp4`

## Prompt (verbatim, `[Subject]` intact)

```
Slow panoramic pan revealing [Subject], the camera rotating smoothly on a fluid head, the steady horizontal sweep connecting a wide expanse of visual information, shot on 35mm anamorphic with Panavision E-series glass, the ultra-wide field of view compressing the panorama into a layered ribbon of texture, cool teal shadows against warm highlight tones
```

A horizontal rotation of the camera on a fixed axis, sweeping left or right to reveal the breadth of a space, follow lateral movement, or connect subjects across a scene. John Ford's slow, reverent pans across Monument Valley in "The Searchers" established the landscape as a character. Jean Renoir pioneered fluid panning in "The Rules of the Game," and Paul Thomas Anderson uses methodical lateral pans in "There Will Be Blood" to survey the oil fields with the deliberate gaze of a prospector scanning for fortune.

**When to use.** Use a pan when attention must travel horizontally without relocating the camera. It can follow a person crossing frame, reveal a landscape, connect two subjects, or uncover new information waiting offscreen. The move creates a relationship between its starting and ending points, so both should matter. Avoid panning simply because the frame feels static; motivated rotation is clearer and more pers…

**Directing the AI.** Fix the camera on one axis and describe a smooth left-to-right or right-to-left rotation. Name the opening subject, the visual path through the middle, and the exact endpoint that resolves the move. Use a fluid, measured speed with enough motion blur to feel continuous but not smeared. A wide anamorphic field can layer the panorama. Keep camera height and tilt unchanged, distinguishing rotation from a dolly, orbit, or handheld drift.

**Common mistakes.**
- Failing to specify the start and end subjects, leaving the horizontal move without narrative direction or payoff.
- Combining a pan with forward travel and vertical drift until the motion no longer reads as fixed-axis rotation.
- Moving too quickly for the audience to inspect the landscape or understand the relationship being revealed.

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
| declared | `space-camera-moves` | camera | 150 | `drone-dive-landing` |
| declared | `space-camera-moves` | camera | 150 | `exploded-view` |

```
python platform/query.py technique-motions pan-shot
```

## Sources

- 50+ Types of Camera Shots, Angles, and Techniques

## Related techniques

- [('whip-pan', 'whip-pan')](('whip-pan', 'whip-pan').md)
- [('tilt-shot', 'tilt-shot')](('tilt-shot', 'tilt-shot').md)
- [('tracking-shot', 'tracking-shot')](('tracking-shot', 'tracking-shot').md)
- [('aerial-shot', 'aerial-shot')](('aerial-shot', 'aerial-shot').md)
- [('birds-eye-view', 'birds-eye-view')](('birds-eye-view', 'birds-eye-view').md)
- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('dutch-angle', 'dutch-angle')](('dutch-angle', 'dutch-angle').md)
- [('dolly-shot', 'dolly-shot')](('dolly-shot', 'dolly-shot').md)
- [('establishing-shot', 'establishing-shot')](('establishing-shot', 'establishing-shot').md)
