# "Rack Focus Prompt for AI Image & Video"

`rack-focus` · Camera Work · level intermediate

Reference video: `media/rack-focus.mp4`

## Prompt (verbatim, `[Subject]` intact)

```
Rack focus shot with [Subject] transitioning between sharp foreground detail and resolved background, the focus pull taking a full two seconds, layers of creamy circular bokeh in the defocused plane, shot on a vintage Canon K35 lens wide open at T1.4 for maximum separation between planes, the shallow depth of field turning focus itself into a storytelling instrument
```

A deliberate shift of focus from one subject to another within the same shot, redirecting audience attention without cutting and creating elegant visual transitions between foreground and background. Orson Welles and cinematographer Gregg Toland pioneered deep focus techniques in "Citizen Kane," but the deliberate rack focus became an expressive tool through the work of cinematographers like Vilmos Zsigmond in "The Deer Hunter." Robert Altman used rack focus as a narrative device in "The Player," shifting attention between overlapping conversations, and Roger Deakins employs subtle focus pull…

**When to use.** Use rack focus when two subjects share one composition but audience attention must transfer between them. A foreground clue can sharpen before a background reaction, or a speaking character can give way to someone listening behind them. The move preserves spatial continuity while changing narrative emphasis. It needs distinct depth planes and a reason to shift; otherwise focus hunting looks like…

**Directing the AI.** Stage one subject close to the lens and another clearly separated in the background. Begin with only the first plane sharp, then pull focus smoothly over about two seconds until the second resolves and the first falls into creamy bokeh. Use a fast vintage lens and keep camera position fixed so focus itself performs the edit. Define the trigger for the shift, such as a sound, glance, or revealed object, and avoid breathing that changes framing dramatically.

**Common mistakes.**
- Placing both subjects on nearly the same depth plane, leaving too little optical separation for a visible transition.
- Changing camera framing during the pull, which competes with focus and obscures where attention should land.
- Racking back and forth without narrative triggers, reducing an elegant redirection into distracting focus hunting.

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
| declared | `depth-layer-moves` | camera | 150 | `dolly-zoom-real` |
| declared | `depth-layer-moves` | camera | 150 | `multiplane-real` |

```
python platform/query.py technique-motions rack-focus
```

## Sources

- 50+ Types of Camera Shots, Angles, and Techniques

## Related techniques

- [('shallow-focus', 'shallow-focus')](('shallow-focus', 'shallow-focus').md)
- [('depth-of-field', 'depth-of-field')](('depth-of-field', 'depth-of-field').md)
- [('insert-shot', 'insert-shot')](('insert-shot', 'insert-shot').md)
- [('aerial-shot', 'aerial-shot')](('aerial-shot', 'aerial-shot').md)
- [('birds-eye-view', 'birds-eye-view')](('birds-eye-view', 'birds-eye-view').md)
- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('dutch-angle', 'dutch-angle')](('dutch-angle', 'dutch-angle').md)
- [('dolly-shot', 'dolly-shot')](('dolly-shot', 'dolly-shot').md)
- [('establishing-shot', 'establishing-shot')](('establishing-shot', 'establishing-shot').md)
