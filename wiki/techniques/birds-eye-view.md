# "Bird's Eye View Prompt for AI Image & Video"

`birds-eye-view` · Camera Work · level intermediate

Reference video: `media/birds-eye-view.mp4`

## Prompt (verbatim, `[Subject]` intact)

```
Bird's eye view looking straight down on [Subject], the camera positioned directly overhead creating a flattened god-like perspective where depth is eliminated and everything becomes pattern and geometry, long shadows stretching from each element, shot on medium format digital with a 40mm equivalent lens, muted teal and gold color palette, forensic sharpness from edge to edge
```

A shot taken from directly overhead, looking straight down on the subject, creating a god-like perspective that can make subjects appear small and insignificant or reveal patterns invisible from ground level. Busby Berkeley pioneered the technique in 1930s musicals, choreographing dancers into kaleidoscopic geometric formations seen from directly above. Darren Aronofsky used it extensively in "Requiem for a Dream" to convey psychological detachment, and Wes Anderson frequently employs overhead shots of meticulously arranged objects as a signature compositional device.

**When to use.** Use a bird's eye view when the scene contains a pattern that ground-level framing would hide. Crowds, roads, bodies, tables, and architecture become readable as geometry from directly above. It also makes people appear controlled, observed, or insignificant. This angle works best when spatial design carries meaning; it is less useful when facial expression or normal depth must drive the moment.

**Directing the AI.** State that the camera looks straight down with its optical axis perpendicular to the ground. Remove the horizon and treat people, objects, roads, and shadows as flat graphic shapes. Arrange the main elements into a deliberate pattern with clean spacing and edge-to-edge sharpness. Use a restrained teal-and-gold palette and long directional shadows to preserve visual separation. For video, keep the camera locked or moving vertically so the top-down geometry does not drift into an oblique aerial a…

**Common mistakes.**
- Using the phrase from above without straight-down camera language, which often produces an ordinary high-angle perspective instead.
- Building a scene with no visible pattern, making the unusual viewpoint feel decorative rather than narratively motivated.
- Adding shallow focus across the frame, which weakens the forensic clarity and flattened geometry that define the view.

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
python platform/query.py technique-motions birds-eye-view
```

## Sources

- 50+ Types of Camera Shots, Angles, and Techniques

## Related techniques

- [('overhead-shot', 'overhead-shot')](('overhead-shot', 'overhead-shot').md)
- [('symmetry', 'symmetry')](('symmetry', 'symmetry').md)
- [('repetition-and-pattern', 'repetition-and-pattern')](('repetition-and-pattern', 'repetition-and-pattern').md)
- [('aerial-shot', 'aerial-shot')](('aerial-shot', 'aerial-shot').md)
- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('dutch-angle', 'dutch-angle')](('dutch-angle', 'dutch-angle').md)
- [('dolly-shot', 'dolly-shot')](('dolly-shot', 'dolly-shot').md)
- [('establishing-shot', 'establishing-shot')](('establishing-shot', 'establishing-shot').md)
- [('extreme-close-up', 'extreme-close-up')](('extreme-close-up', 'extreme-close-up').md)
