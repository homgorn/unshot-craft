# "Wipe Prompt for AI Image & Video"

`wipe-transition` · Editing · level basic

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Wipe transition with [Subject] in one scene being pushed off frame by an incoming scene sliding in, the geometric wipe edge a clean vertical line, both scenes fully lit and composed as complete images on either side, the nostalgic energy of adventure serials, the self-aware playfulness of a transition that announces itself as a storytelling device
```

One shot pushes another off screen in a defined geometric pattern — a signature of Star Wars and classic serials that adds kinetic energy and a retro, adventurous feel. George Lucas adopted the wipe transition directly from Akira Kurosawa's "The Hidden Fortress" for "Star Wars," making it the saga's most recognizable editorial device. The wipe was common in 1930s and 40s adventure serials that Lucas and Spielberg loved as children. While largely absent from modern cinema, wipes occasionally appear as deliberate homage — Edgar Wright uses them in "Baby Driver," and Wes Anderson employs them in…

**When to use.** Use a wipe when the transition itself should be felt: a chapter change, geographic jump, comic beat, or deliberate nod to classic adventure serials. It carries more personality than a neutral cut and more momentum than a dissolve. Choose it for stylized worlds that can support visible editorial grammar; avoid it when realism or emotional invisibility matters more than playful movement.

**Directing the AI.** Design two fully resolved shots with compatible visual weight on opposite sides of the transition. Move a clean vertical, horizontal, or shaped boundary steadily across frame until the incoming scene replaces the outgoing one. Keep the wipe edge crisp and the speed confident, without smearing subjects together. Coordinate directional movement so the new composition feels pushed into place. Let both scenes remain legible during the handoff, even though each appears only partially.

**Common mistakes.**
- Using a wipe inside an otherwise invisible edit style, making one transition feel accidentally theatrical.
- Leaving either scene undercomposed because the creator planned only the final frame, not the moving boundary.
- Adding blur or dissolve at the edge, which weakens the clean geometric character of the technique.

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
| declared | `color-block-step-wipe` | transition | 44 | `color-block-step-wipe` |

```
python platform/query.py technique-motions wipe-transition
```

## Sources

- What Is Film Editing?

## Related techniques

- [('whip-pan', 'whip-pan')](('whip-pan', 'whip-pan').md)
- [('dissolve', 'dissolve')](('dissolve', 'dissolve').md)
- [('iris-transition', 'iris-transition')](('iris-transition', 'iris-transition').md)
- [('cross-cutting', 'cross-cutting')](('cross-cutting', 'cross-cutting').md)
- [('jump-cut', 'jump-cut')](('jump-cut', 'jump-cut').md)
- [('fade-in-out', 'fade-in-out')](('fade-in-out', 'fade-in-out').md)
- [('montage', 'montage')](('montage', 'montage').md)
- [('smash-cut', 'smash-cut')](('smash-cut', 'smash-cut').md)
- [('long-take', 'long-take')](('long-take', 'long-take').md)
