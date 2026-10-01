# "Cliffhanger Prompt for AI Image & Video"

`cliffhanger` · Narrative · level basic

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Cliffhanger moment frozen at peak suspense with [Subject], the image capturing the exact instant before resolution, the viewer's need for closure weaponized into desperate anticipation, dramatic sidelighting creating hard shadows that emphasize physical strain, the visual language of unresolved tension that demands continuation
```

Ending a scene, episode, or act at a moment of peak suspense, leaving the outcome unresolved and exploiting the human need for closure to keep audiences desperate for more. The term comes from Thomas Hardy's serialized novel "A Pair of Blue Eyes," where a character literally hangs from a cliff. "The Empire Strikes Back" ends on one of cinema's greatest cliffhangers — Han frozen in carbonite, Luke maimed and shattered by Vader's revelation. Television perfected the cliffhanger with "Dallas" 's "Who shot J.R.?" and "Breaking Bad"'s mid-season endings. Christopher Nolan ends "Inception" on a phi…

**When to use.** Use a cliffhanger at an act, episode, or scene break when the unresolved outcome can pull the audience forward. The best version stops after the stakes are understood but before the decisive action, answer, or consequence arrives. It works for physical danger, revelations, choices, and emotional confrontations. Avoid using it on minor information; the interruption must leave a genuine narrative p…

**Directing the AI.** Build toward one irreversible beat, then frame the exact instant before impact, response, escape, or revelation. Use hard side light, compressed space, strained posture, and a clear eyeline toward the unresolved threat. Let the final image contain the question visually without explaining it in text. Cut away before movement completes, not before the audience understands what may happen. Preserve enough detail for the next scene to resume from the same physical and emotional position.

**Common mistakes.**
- Ending before the stakes are visible, creating simple interruption rather than suspenseful unresolved pressure.
- Resolving the dangerous action inside the final frame, then pretending the aftermath is still a cliffhanger.
- Using cliffhangers repeatedly without satisfying prior questions, which converts anticipation into audience distrust.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

## Motion pairings

**Declared, not inferred.** These come from an explicit `styles:` list in `data/cinematic/<slug>.md`, authored in `platform/catalog/pairings.py`. Nothing here is matched by name similarity.

| kind | shot card | category | frames | style |
|---|---|---|---|---|
| declared | `montage-rhythm-moves` | rhythm | 129 | `domino-cascade` |
| declared | `montage-rhythm-moves` | rhythm | 129 | `drop-blackout-slam` |
| declared | `montage-rhythm-moves` | rhythm | 129 | `wright-triple-cut` |

```
python platform/query.py technique-motions cliffhanger
```

## Sources

- How to Make a Short Film: An Introduction to Filmmaking

## Related techniques

- [('freeze-frame', 'freeze-frame')](('freeze-frame', 'freeze-frame').md)
- [('foreshadowing', 'foreshadowing')](('foreshadowing', 'foreshadowing').md)
- [('in-medias-res', 'in-medias-res')](('in-medias-res', 'in-medias-res').md)
- [('flashback', 'flashback')](('flashback', 'flashback').md)
- [('breaking-fourth-wall', 'breaking-fourth-wall')](('breaking-fourth-wall', 'breaking-fourth-wall').md)
- [('flashforward', 'flashforward')](('flashforward', 'flashforward').md)
- [('non-linear-narrative', 'non-linear-narrative')](('non-linear-narrative', 'non-linear-narrative').md)
- [('parallel-storylines', 'parallel-storylines')](('parallel-storylines', 'parallel-storylines').md)
- [('frame-narrative', 'frame-narrative')](('frame-narrative', 'frame-narrative').md)
