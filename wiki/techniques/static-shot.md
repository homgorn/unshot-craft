# "Static Shot Prompt for AI Image & Video"

`static-shot` · Camera Work · level basic

Reference video: `media/static-shot.mp4`

## Prompt (verbatim, `[Subject]` intact)

```
Perfectly static locked-off shot of [Subject], the camera absolutely motionless on a heavy tripod, every element placed with obsessive precision, the stillness of the camera making the frame feel like a living painting, shot on ARRI Alexa with a 40mm Zeiss Master Prime at T5.6 for maximum sharpness edge to edge, Wes Anderson palette, the deadpan humor of perfect order
```

A completely locked-off shot with no camera movement, forcing the composition to do all the work — the deliberate stillness can create contemplation, comedy through staging, or unsettling tension. Yasujiro Ozu built an entire cinematic philosophy around the static shot, his "pillow shots" of empty rooms and corridors in "Tokyo Story" becoming meditations on impermanence. Wes Anderson's rigorously static, symmetrical compositions in "The Grand Budapest Hotel" turn every frame into a diorama. Roy Andersson constructs elaborate single-frame tableaux vivants in "Songs from the Second Floor," and…

**When to use.** Choose a static shot when stillness should make viewers study composition, duration, and behavior inside the frame. It suits deadpan comedy, domestic routine, architectural order, contemplation, and tension created by waiting. With no camera movement to manufacture emphasis, blocking and timing become exposed. Use it when the frame can evolve internally; otherwise locked-off footage may simply fe…

**Directing the AI.** Lock the camera to a heavy tripod and prohibit pan, tilt, zoom, drift, or stabilization sway. Arrange every object and figure with precise spacing, strong verticals, and enough depth for movement within the composition. Use edge-to-edge clarity and a controlled palette so small changes register. For video, choreograph entrances, exits, gestures, or background events while the frame remains absolutely fixed. The visual tension must come from what changes inside the boundary.

**Common mistakes.**
- Adding subtle automated push or handheld drift, which breaks the formal stillness even when movement is barely visible.
- Treating locked camera as permission for weak composition, leaving no internal lines, depth, or staged action to inspect.
- Centering every subject mechanically when asymmetry or offscreen pressure would create stronger tension within the fixed frame.

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
python platform/query.py technique-motions static-shot
```

## Sources

- 50+ Types of Camera Shots, Angles, and Techniques

## Related techniques

- [('symmetry', 'symmetry')](('symmetry', 'symmetry').md)
- [('slow-cinema', 'slow-cinema')](('slow-cinema', 'slow-cinema').md)
- [('master-shot', 'master-shot')](('master-shot', 'master-shot').md)
- [('aerial-shot', 'aerial-shot')](('aerial-shot', 'aerial-shot').md)
- [('birds-eye-view', 'birds-eye-view')](('birds-eye-view', 'birds-eye-view').md)
- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('dutch-angle', 'dutch-angle')](('dutch-angle', 'dutch-angle').md)
- [('dolly-shot', 'dolly-shot')](('dolly-shot', 'dolly-shot').md)
- [('establishing-shot', 'establishing-shot')](('establishing-shot', 'establishing-shot').md)
