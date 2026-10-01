# "Smash Cut Prompt for AI Image & Video"

`smash-cut` · Editing · level basic

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Smash cut from absolute serenity to total chaos involving [Subject], an instantaneous hard cut with no transition, no preparation, the tonal whiplash so extreme the viewer physically reacts, the editorial equivalent of a slap, the technique that weaponizes the cut itself as a storytelling instrument
```

An abrupt, jarring cut between two vastly different scenes — often from quiet to loud, calm to chaos, or a character saying "nothing could go wrong" to everything going wrong. Edgar Wright is the modern master of the smash cut, using it for comedic whiplash throughout "Shaun of the Dead" and "Hot Fuzz." Kubrick's smash cut from the bone to the satellite in "2001" is the most dramatic temporal smash cut in cinema. The Coen Brothers use smash cuts for dark comedy in "Fargo" and "No Country for Old Men," and David Lynch uses them in "Mulholland Drive" to shatter the viewer's sense of narrative s…

**When to use.** Use a smash cut when the transition itself should trigger shock, comedy, dread, or a sudden change of scale and time. The strongest versions collide opposite states: quiet with noise, stillness with motion, confidence with failure, or intimacy with vastness. Build enough calm or expectation before the cut for the whiplash to land. Avoid using it repeatedly, because the audience quickly adapts and…

**Directing the AI.** Construct two shots with sharply opposed tone, volume, motion, palette, or scale. Hold the first long enough to establish its state, then cut instantly at the most vulnerable or ironic beat. Use no dissolve, flash, or transitional smoothing. Make the opening frame of the second shot immediately legible and maximally different. Preserve intentional continuity only where a matched shape or phrase sharpens the joke or shock. Let sound change on the exact same frame as picture.

**Common mistakes.**
- Adding a flash, blur, or speed ramp between scenes, cushioning the hard collision that should create the reaction.
- Cutting between scenes with similar motion and tone, leaving too little contrast for real editorial whiplash.
- Repeating smash cuts throughout a sequence, training the audience to expect them and draining their surprise.

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
| declared | `impact-feedback` | effects | — | `anime-impact` |
| declared | `impact-feedback` | effects | — | `hit-counter` |

```
python platform/query.py technique-motions smash-cut
```

## Sources

- What Is Film Editing?

## Related techniques

- [('jump-cut', 'jump-cut')](('jump-cut', 'jump-cut').md)
- [('whip-pan', 'whip-pan')](('whip-pan', 'whip-pan').md)
- [('contrast-composition', 'contrast-composition')](('contrast-composition', 'contrast-composition').md)
- [('cross-cutting', 'cross-cutting')](('cross-cutting', 'cross-cutting').md)
- [('dissolve', 'dissolve')](('dissolve', 'dissolve').md)
- [('fade-in-out', 'fade-in-out')](('fade-in-out', 'fade-in-out').md)
- [('montage', 'montage')](('montage', 'montage').md)
- [('long-take', 'long-take')](('long-take', 'long-take').md)
- [('freeze-frame', 'freeze-frame')](('freeze-frame', 'freeze-frame').md)
