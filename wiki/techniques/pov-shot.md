# "P.O.V. Shot Prompt for AI Image & Video"

`pov-shot` · Camera Work · level intermediate

Reference video: `media/pov-shot.mp4`

## Prompt (verbatim, `[Subject]` intact)

```
First-person POV shot through the eyes of [Subject], shallow depth of field mimicking unfocused human vision, subtle lens breathing as focus racks, shot on a wide 14mm rectilinear lens to approximate human field of view, the immersive subjectivity of seeing exactly what the character sees
```

Shows the scene exactly as a character sees it, placing the viewer inside their subjective experience and creating powerful identification and immersion. Hitchcock was the master of POV, using subjective shots in "Rear Window" to lock the audience into James Stewart's voyeuristic gaze, and in "Vertigo" to plunge viewers into the protagonist's acrophobia. Gaspar Noé built "Enter the Void" entirely from a first-person perspective, including the afterlife. The "Peep Show" technique was also used to devastating effect by Kathryn Bigelow in "Strange Days" and Jonathan Glazer in "Under the Skin."

**When to use.** Choose a point-of-view shot when viewers must share a character's act of looking rather than merely observe them. It can intensify discovery, fear, desire, surveillance, confusion, or physical danger. The shot works best when paired with a clear owner of the gaze and a meaningful target. Without that setup, first-person framing can feel like an unmotivated camera trick or generic game footage.

**Directing the AI.** State whose eyes define the camera and what they are looking toward. Keep the viewpoint at that character's height, with natural head movement, subtle focus breathing, and peripheral softness rather than a visible third-person body. A wide rectilinear perspective can suggest human field of view without fisheye distortion. For video, synchronize gaze shifts with sound or action cues and let focus settle imperfectly, as human attention does, before the important detail becomes clear.

**Common mistakes.**
- Showing the observing character in the same frame, which breaks the claim that the image is their exact view.
- Adding exaggerated fisheye curvature that reads as an action camera rather than ordinary subjective vision.
- Using random head sway without a target, making the viewpoint nauseating instead of emotionally identified with a character.

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
| declared | `graze-face-tour` | camera | 150 | `graze-face-tour` |

```
python platform/query.py technique-motions pov-shot
```

## Sources

- 50+ Types of Camera Shots, Angles, and Techniques

## Related techniques

- [('reaction-shot', 'reaction-shot')](('reaction-shot', 'reaction-shot').md)
- [('head-on-shot', 'head-on-shot')](('head-on-shot', 'head-on-shot').md)
- [('found-footage', 'found-footage')](('found-footage', 'found-footage').md)
- [('aerial-shot', 'aerial-shot')](('aerial-shot', 'aerial-shot').md)
- [('birds-eye-view', 'birds-eye-view')](('birds-eye-view', 'birds-eye-view').md)
- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('dutch-angle', 'dutch-angle')](('dutch-angle', 'dutch-angle').md)
- [('dolly-shot', 'dolly-shot')](('dolly-shot', 'dolly-shot').md)
- [('establishing-shot', 'establishing-shot')](('establishing-shot', 'establishing-shot').md)
