# "Establishing Shot Prompt for AI Image & Video"

`establishing-shot` · Camera Work · level basic

Reference video: `media/establishing-shot.mp4`

## Prompt (verbatim, `[Subject]` intact)

```
Wide establishing shot of [Subject] at blue hour, deep indigo sky with the last traces of sunset, a few warm lights glowing from within, atmospheric haze softening the distance, shot on ARRI Alexa with Zeiss Master Primes, desaturated cool palette with selective warm accents, architectural precision meets cinematic storytelling
```

A wide shot typically used at the beginning of a scene to set the context, showing the location, time of day, and spatial relationships before cutting to closer action. Stanley Kubrick's establishing shots in "The Shining" — the Overlook Hotel dwarfed by mountains — immediately communicated isolation and foreboding. Ridley Scott's opening of "Blade Runner" established a dystopian Los Angeles with a single, unforgettable wide shot of industrial hellscape. David Fincher meticulously crafts establishing shots that embed narrative information into every architectural detail.

**When to use.** Open with an establishing shot when viewers need to understand where the scene happens, what time or weather shapes it, and how the key spaces connect. A strong version can also seed isolation, danger, wealth, or decay through architecture and scale. Use it before tighter coverage or after a major location change. Do not spend it on a setting the audience already reads clearly.

**Directing the AI.** Frame the location wide enough to show its dominant architecture, surrounding terrain, access points, and one small sign of life. Set the scene at blue hour with a deep indigo sky, faint sunset residue, warm interior lights, and haze softening the distance. Keep the composition legible rather than merely expansive. If generating video, begin still or with a restrained drift, allowing the viewer to map the place before any cut or character movement claims attention.

**Common mistakes.**
- Showing a beautiful location without the landmarks or spatial relationships needed to orient the next scene.
- Making the principal character too large in frame, turning contextual coverage into a conventional long shot.
- Packing the image with unrelated atmosphere cues that obscure the intended time, geography, or narrative tone.

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
| declared | `depth-layer-moves` | camera | 150 | `dolly-zoom-real` |
| declared | `depth-layer-moves` | camera | 150 | `multiplane-real` |
| declared | `space-camera-moves` | camera | 150 | `drone-dive-landing` |
| declared | `space-camera-moves` | camera | 150 | `exploded-view` |

```
python platform/query.py technique-motions establishing-shot
```

## Sources

- 50+ Types of Camera Shots, Angles, and Techniques

## Related techniques

- [('aerial-shot', 'aerial-shot')](('aerial-shot', 'aerial-shot').md)
- [('master-shot', 'master-shot')](('master-shot', 'master-shot').md)
- [('extreme-long-shot', 'extreme-long-shot')](('extreme-long-shot', 'extreme-long-shot').md)
- [('birds-eye-view', 'birds-eye-view')](('birds-eye-view', 'birds-eye-view').md)
- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('dutch-angle', 'dutch-angle')](('dutch-angle', 'dutch-angle').md)
- [('dolly-shot', 'dolly-shot')](('dolly-shot', 'dolly-shot').md)
- [('extreme-close-up', 'extreme-close-up')](('extreme-close-up', 'extreme-close-up').md)
- [('eye-level-shot', 'eye-level-shot')](('eye-level-shot', 'eye-level-shot').md)
