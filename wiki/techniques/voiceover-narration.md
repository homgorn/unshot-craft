# "Voiceover Narration Prompt for AI Image & Video"

`voiceover-narration` · Narrative · level basic

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Scene designed to accompany voiceover narration with [Subject] in a contemplative visual, the imagery deliberately quiet and reflective to create space for an unseen narrator's voice, the visual mood introspective and open-ended, soft desaturated color palette, the Malick-Scorsese understanding that the right contemplative image paired with words creates something greater than either alone
```

A character's voice speaking over the visuals, providing internal thoughts, context, or commentary that can create intimacy, irony, or an essay-like quality depending on tone. Martin Scorsese uses voiceover as a vital narrative engine — Henry Hill's running commentary in "Goodfellas" is inseparable from the film's identity. Terrence Malick's whispered, philosophical voiceovers in "The Thin Red Line" and "The Tree of Life" create an interior poetry. Billy Wilder used voiceover to brilliant ironic effect in "Sunset Boulevard," narrated by a dead man. Wong Kar-wai's voiceovers in "In the Mood fo…

**When to use.** Use voiceover narration when the audience needs access to thought, memory, commentary, or a perspective the visible action cannot supply. Pairing words and images can create intimacy, contradiction, or essay-like reflection. The voice should add a second layer, not describe what viewers already see. Leave room in pacing and composition for language to land, especially when the images are emotiona…

**Directing the AI.** Build a restrained visual scene around the subject: contemplative action, open negative space, soft desaturated color, and slow, readable movement. Keep cuts sparse enough for spoken ideas to breathe. Pair literal words with complementary or contradictory imagery rather than direct illustration. Maintain environmental sound and visual detail so the image does not become wallpaper. Place the subject off-center or looking beyond frame, creating psychological space for an unseen voice while preser…

**Common mistakes.**
- Describing visible actions word for word, reducing narration to redundant accessibility rather than added perspective.
- Cutting images faster than the spoken thought can land, forcing sound and picture to compete.
- Using vague contemplative visuals with no relationship to the narrator's specific memory, irony, or argument.

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
| declared | `typing-code-block` | typography | 138 | `typing-code-block` |

```
python platform/query.py technique-motions voiceover-narration
```

## Sources

- How to Make a Short Film: An Introduction to Filmmaking

## Related techniques

- [('frame-narrative', 'frame-narrative')](('frame-narrative', 'frame-narrative').md)
- [('breaking-fourth-wall', 'breaking-fourth-wall')](('breaking-fourth-wall', 'breaking-fourth-wall').md)
- [('negative-space', 'negative-space')](('negative-space', 'negative-space').md)
- [('flashback', 'flashback')](('flashback', 'flashback').md)
- [('foreshadowing', 'foreshadowing')](('foreshadowing', 'foreshadowing').md)
- [('in-medias-res', 'in-medias-res')](('in-medias-res', 'in-medias-res').md)
- [('cliffhanger', 'cliffhanger')](('cliffhanger', 'cliffhanger').md)
- [('flashforward', 'flashforward')](('flashforward', 'flashforward').md)
- [('non-linear-narrative', 'non-linear-narrative')](('non-linear-narrative', 'non-linear-narrative').md)
