# "Whip Pan Prompt for AI Image & Video"

`whip-pan` · Camera Work · level intermediate

Reference video: `media/whip-pan.mp4`

## Prompt (verbatim, `[Subject]` intact)

```
Whip pan snapping to [Subject], heavy horizontal motion blur streaking the environment into abstract ribbons of color, the blur lasting just three frames before resolving into razor sharpness, shot on high-speed camera with a 35mm Zeiss Master Prime, raw visceral kinetic energy
```

An extremely fast horizontal pan that creates motion blur, used as a dynamic transition or to convey sudden surprise, rapid shifts of attention, or frenetic energy. Edgar Wright made the whip pan his comedic signature in "Shaun of the Dead," "Hot Fuzz," and "Baby Driver," using them as rapid-fire visual punchlines. Sam Raimi employed frantic whip pans in the "Evil Dead" trilogy to convey demonic energy, and Damien Chazelle used precise whip pans in "Whiplash" to match the violent tempo of jazz drumming. Paul Thomas Anderson uses them as elegant transitions between scenes in "Boogie Nights."

**When to use.** Choose a whip pan for a sudden shift of attention, a visual punchline, an impact, or a high-energy transition between connected spaces. Its brief blur can hide a cut or compress the distance between subjects. The destination must justify the snap. Use it as punctuation inside controlled coverage; constant whip pans make the scene noisy and erase the surprise that gives the move force.

**Directing the AI.** Define the sharp starting frame and an equally sharp landing frame on a second subject. Snap the camera horizontally between them, allowing only a few frames of heavy directional streaking before the image resolves. Keep blur aligned with the movement rather than radial or random. Match subject height and motion direction if the pan masks a transition. Hold briefly after landing. The move should read as one decisive operator reaction, not a continuous rapid scan.

**Common mistakes.**
- Leaving the endpoint vague, causing the camera to stop on empty space or a subject that never resolves sharply.
- Applying blur before and after the movement, which removes the crisp contrast that gives a whip pan impact.
- Using radial zoom streaks instead of horizontal motion blur, confusing the technique with a crash zoom.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` | `camera_motion: pan_right | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: smooth_pan` | pika-1.5 | no |
| `runway_gen3` | `motion_brush: smooth_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: smooth_pan` | sora-1 | no |
| `veo2` | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

## Motion pairings

**Declared, not inferred.** These come from an explicit `styles:` list in `data/cinematic/<slug>.md`, authored in `platform/catalog/pairings.py`. Nothing here is matched by name similarity.

| kind | shot card | category | frames | style |
|---|---|---|---|---|
| declared | `tension-camera-moves` | camera | 150 | `bullet-time-freeze-orbit` |
| declared | `tension-camera-moves` | camera | 150 | `dutch-roll-to-level` |
| declared | `tension-camera-moves` | camera | 150 | `pull-back-isolation` |
| declared | `tension-camera-moves` | camera | 150 | `slow-push-in` |

```
python platform/query.py technique-motions whip-pan
```

## Sources

- 50+ Types of Camera Shots, Angles, and Techniques

## Related techniques

- [('pan-shot', 'pan-shot')](('pan-shot', 'pan-shot').md)
- [('crash-zoom', 'crash-zoom')](('crash-zoom', 'crash-zoom').md)
- [('smash-cut', 'smash-cut')](('smash-cut', 'smash-cut').md)
- [('aerial-shot', 'aerial-shot')](('aerial-shot', 'aerial-shot').md)
- [('birds-eye-view', 'birds-eye-view')](('birds-eye-view', 'birds-eye-view').md)
- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('dutch-angle', 'dutch-angle')](('dutch-angle', 'dutch-angle').md)
- [('dolly-shot', 'dolly-shot')](('dolly-shot', 'dolly-shot').md)
- [('establishing-shot', 'establishing-shot')](('establishing-shot', 'establishing-shot').md)
