# "Overhead Shot Prompt for AI Image & Video"

`overhead-shot` · Camera Work · level intermediate

Reference video: `media/overhead-shot.mp4`

## Prompt (verbatim, `[Subject]` intact)

```
Overhead shot looking straight down on [Subject], the flat geometric arrangement rendered as graphic composition, natural north-light creating soft even illumination with no harsh shadows, shot on medium format with a 55mm lens, clinical sharpness of top-down perspective, Wes Anderson-level compositional precision
```

Camera positioned directly above the scene looking straight down, similar to bird's eye but typically closer, often used for tabletop scenes, maps, or choreographed action. Wes Anderson uses overhead shots of hands and objects obsessively in films like "The Grand Budapest Hotel" and "The French Dispatch," turning tabletop arrangements into graphic design. Martin Scorsese employed the technique in "Goodfellas" for the famous cooking-in-prison scene, looking down on razor-thin garlic slices. Spike Jonze and David Fincher both use close overhead angles to transform mundane actions into visually…

**When to use.** Choose an overhead shot for close top-down views of hands, food, maps, tools, documents, bodies, or choreographed action. It converts ordinary activity into graphic arrangement while keeping more intimacy than a broad bird's eye view. The technique works for procedures, clues, rituals, and visual comedy. Use it only when the placement and movement of objects carries meaning, not as automatic deco…

**Directing the AI.** Mount the viewpoint directly above the working surface and point straight down, with no horizon or angled wall visible. Arrange hands and objects as a clean graphic composition, using soft north-window illumination to avoid harsh competing shadows. Keep the surface sharp from corner to corner and use a medium-format sense of detail. For video, specify precise hand paths and object changes while the camera remains locked, so movement activates the composition rather than destabilizing it.

**Common mistakes.**
- Tilting the camera enough to reveal side faces, changing the graphic top-down view into an ordinary high angle.
- Scattering props without deliberate spacing, which makes the surface look messy rather than designed for overhead reading.
- Using strong shadows that overlap critical objects and obscure the procedural or narrative information in the arrangement.

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
python platform/query.py technique-motions overhead-shot
```

## Sources

- 50+ Types of Camera Shots, Angles, and Techniques

## Related techniques

- [('birds-eye-view', 'birds-eye-view')](('birds-eye-view', 'birds-eye-view').md)
- [('insert-shot', 'insert-shot')](('insert-shot', 'insert-shot').md)
- [('repetition-and-pattern', 'repetition-and-pattern')](('repetition-and-pattern', 'repetition-and-pattern').md)
- [('aerial-shot', 'aerial-shot')](('aerial-shot', 'aerial-shot').md)
- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('dutch-angle', 'dutch-angle')](('dutch-angle', 'dutch-angle').md)
- [('dolly-shot', 'dolly-shot')](('dolly-shot', 'dolly-shot').md)
- [('establishing-shot', 'establishing-shot')](('establishing-shot', 'establishing-shot').md)
- [('extreme-close-up', 'extreme-close-up')](('extreme-close-up', 'extreme-close-up').md)
