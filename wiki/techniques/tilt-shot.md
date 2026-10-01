# "Tilt Shot Prompt for AI Image & Video"

`tilt-shot` · Camera Work · level basic

Reference video: `media/tilt-shot.mp4`

## Prompt (verbatim, `[Subject]` intact)

```
Slow tilt shot beginning at the feet of [Subject] and climbing vertically up their body, the deliberate vertical scan building anticipation, each detail telling the character's story before the face is revealed, shot on 85mm telephoto compressing the vertical layers, Kodak Vision3 500T with cool overcast color rendition
```

A vertical rotation of the camera on a fixed axis, tilting up or down to reveal height, scan a character from feet to face, or follow vertical action. Hitchcock used the slow tilt masterfully in "Psycho," tilting up the facade of the Bates house to establish its Gothic menace. Spielberg opens "Jurassic Park" with a slow tilt up the Brachiosaurus that mirrors the characters' awe, and Christopher Nolan employs precise tilts in "Inception" to disorient the viewer as architecture folds upon itself.

**When to use.** Use a tilt when attention needs to travel vertically while the camera stays in place. A slow rise from boots to face can delay identity; a move up a facade can establish intimidating height; a downward tilt can reveal danger, evidence, or a body below. The start and finish should form a meaningful relationship. Avoid tilting when physical camera elevation or a wider static frame communicates the…

**Directing the AI.** Fix the camera on its support and specify a vertical rotation upward or downward with no lateral travel. Name the starting detail, the visual information encountered during the move, and the final reveal. A telephoto perspective can compress stacked details during a character scan, while steady speed builds anticipation. Keep horizontal framing stable and avoid roll. For video, let the tilt resolve and hold briefly on the destination so the revealed face or object registers.

**Common mistakes.**
- Confusing tilt with raising the camera, which changes viewpoint and parallax instead of rotating on a fixed axis.
- Starting and ending on unrelated details, leaving the vertical scan with no dramatic logic or visual payoff.
- Tilting too fast for costume, architecture, or environmental clues to register before the final reveal.

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
python platform/query.py technique-motions tilt-shot
```

## Sources

- 50+ Types of Camera Shots, Angles, and Techniques

## Related techniques

- [('pan-shot', 'pan-shot')](('pan-shot', 'pan-shot').md)
- [('crane-shot', 'crane-shot')](('crane-shot', 'crane-shot').md)
- [('low-angle-shot', 'low-angle-shot')](('low-angle-shot', 'low-angle-shot').md)
- [('aerial-shot', 'aerial-shot')](('aerial-shot', 'aerial-shot').md)
- [('birds-eye-view', 'birds-eye-view')](('birds-eye-view', 'birds-eye-view').md)
- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('dutch-angle', 'dutch-angle')](('dutch-angle', 'dutch-angle').md)
- [('dolly-shot', 'dolly-shot')](('dolly-shot', 'dolly-shot').md)
- [('establishing-shot', 'establishing-shot')](('establishing-shot', 'establishing-shot').md)
