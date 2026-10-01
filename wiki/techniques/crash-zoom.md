# "Crash Zoom Prompt for AI Image & Video"

`crash-zoom` · Camera Work · level intermediate

Reference video: `media/crash-zoom.mp4`

## Prompt (verbatim, `[Subject]` intact)

```
Crash zoom snapping from a wide shot to an extreme close-up of [Subject] in half a second, the blur of the rapid zoom creating concentric radial streaks, shot on a vintage Angenieux 25-250mm zoom cranked at maximum speed, 35mm film grain adding grit to the motion blur, Shaw Brothers visual energy channeled through a modern lens
```

A sudden, rapid zoom into a subject for dramatic emphasis, often used for comedic punchlines, horror reveals, or martial arts impact moments. The crash zoom is a staple of Hong Kong martial arts cinema, used by directors like Lau Kar-leung and Chang Cheh in Shaw Brothers productions to punctuate kung fu strikes. Quentin Tarantino pays homage to this in "Kill Bill," and Edgar Wright uses crash zooms for comedic shock in his Cornetto trilogy. Sam Raimi made the crash zoom a horror signature — the camera hurtling toward a screaming face in the "Evil Dead" films became one of the genre's most rec…

**When to use.** Use a crash zoom to punch into a revelation, reaction, weapon, strike, or comic surprise with deliberate visual aggression. Unlike a push-in, it changes framing through a rapid lens move and should feel abrupt. The technique fits martial arts, horror, action, and stylized comedy. Save it for hard accents; repeated snaps reduce every moment to the same volume and exhaust the viewer.

**Directing the AI.** Begin on a readable wide or medium composition, then snap the zoom to an extreme close-up in roughly half a second. Keep the target centered enough to land sharply after a brief burst of concentric radial streaking. Add gritty film texture without smearing the final frame. Define the exact trigger, such as a blow or sudden look, and hold on the destination. Do not move the camera through space; the lens change is the mechanical event.

**Common mistakes.**
- Physically rushing the camera forward, which creates parallax and changes the move into a rapid dolly shot.
- Failing to identify the landing detail, causing the zoom to end between subjects or on an unreadable crop.
- Extending the blur across the held close-up, removing the crisp punctuation that makes the snap satisfying.

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
| declared | `crash-zoom-punch` | camera | 11 | `crash-impact-real` |
| declared | `crash-zoom-punch` | camera | 11 | `crash-zoom-real` |

```
python platform/query.py technique-motions crash-zoom
```

## Sources

- 50+ Types of Camera Shots, Angles, and Techniques

## Related techniques

- [('whip-pan', 'whip-pan')](('whip-pan', 'whip-pan').md)
- [('extreme-close-up', 'extreme-close-up')](('extreme-close-up', 'extreme-close-up').md)
- [('smash-cut', 'smash-cut')](('smash-cut', 'smash-cut').md)
- [('aerial-shot', 'aerial-shot')](('aerial-shot', 'aerial-shot').md)
- [('birds-eye-view', 'birds-eye-view')](('birds-eye-view', 'birds-eye-view').md)
- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('dutch-angle', 'dutch-angle')](('dutch-angle', 'dutch-angle').md)
- [('dolly-shot', 'dolly-shot')](('dolly-shot', 'dolly-shot').md)
- [('establishing-shot', 'establishing-shot')](('establishing-shot', 'establishing-shot').md)
