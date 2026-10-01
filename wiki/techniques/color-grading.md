# "Color Grading Prompt for AI Image & Video"

`color-grading` · Visual Effects & Promptable FX · level intermediate

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Heavily color-graded scene with [Subject] rendered in a distinct teal-and-orange complementary palette, shadows pushed deep into cyan-teal while skin tones and practicals isolated to deep amber-orange, the aggressive color manipulation where post-production color becomes a dominant creative force equal to the original photography, the final act of authorship in the filmmaking pipeline
```

The process of altering and enhancing color in post-production to create a specific mood, era, or visual identity — the final paintbrush of cinema, transforming raw footage into visual art. The Coen Brothers' "O Brother, Where Art Thou?" (2000) was the first major film to be entirely digitally color graded, creating its sepia-toned Depression-era look. David Fincher works obsessively with colorist Stephen Nakamura to achieve the sickly green-yellow palette of "Se7en" and the cold precision of "Zodiac." Steven Soderbergh used radical color grading in "Traffic" — amber for Mexico, blue for the…

**When to use.** Use color grading when a scene needs a unified emotional identity, a distinct period, or a visual boundary between storylines and locations. It can cool a procedural world, warm a memory, or create controlled contrast between shadows and practical lights. Establish the grade as part of the project's visual grammar, not a filter added independently to every shot. Continuity matters more than satur…

**Directing the AI.** Define the palette by assigning hue families to shadows, midtones, skin, highlights, and practical sources. For a teal-and-amber look, push dark regions toward cyan while keeping faces and lamps warm, then protect neutral whites from contamination. Maintain exposure detail in both ends of the range. Apply the same color relationships across changing locations. Specify restrained saturation and consistent black levels so the grade feels authored rather than pasted over the photography.

**Common mistakes.**
- Pushing every surface toward two colors, erasing natural material differences and believable skin variation.
- Changing black levels and white balance between adjacent shots, breaking the continuity of the visual world.
- Using saturation as a substitute for mood without controlling contrast, exposure, or the hierarchy of hues.

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

**None declared.** No entry in `platform/catalog/pairings.py` maps this technique to a shot card, so this page does not claim one. Pairing is authored, never guessed — a wrong pairing hands a client a duration and an easing and looks researched.

## Sources

- Inventing Worlds and Characters: Effects

## Related techniques

- [('color-temperature', 'color-temperature')](('color-temperature', 'color-temperature').md)
- [('desaturation', 'desaturation')](('desaturation', 'desaturation').md)
- [('sepia-tone', 'sepia-tone')](('sepia-tone', 'sepia-tone').md)
- [('film-grain', 'film-grain')](('film-grain', 'film-grain').md)
- [('bokeh', 'bokeh')](('bokeh', 'bokeh').md)
- [('forced-perspective', 'forced-perspective')](('forced-perspective', 'forced-perspective').md)
- [('lens-distortion', 'lens-distortion')](('lens-distortion', 'lens-distortion').md)
- [('morphing', 'morphing')](('morphing', 'morphing').md)
