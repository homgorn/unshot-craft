# "Push In Prompt for AI Image & Video"

`push-in` · Camera Work · level intermediate

Reference video: `media/push-in.mp4`

## Prompt (verbatim, `[Subject]` intact)

```
Imperceptibly slow push-in toward [Subject], the camera beginning in a medium shot and gradually closing to a medium close-up, the push-in so gradual viewers may not consciously register the camera moving yet feel the emotional walls closing in, shot on a 50mm Cooke Speed Panchro vintage lens with gentle focus breathing, Kodak 5219 warmth
```

A slow, deliberate camera movement toward the subject, physically closing distance to intensify focus and emotional weight, drawing the audience deeper into a moment or realization. Jonathan Demme's slow push-in to Clarice Starling's face during her final conversation with Hannibal Lecter in "Silence of the Lambs" is a masterclass in the technique. Kubrick used glacial push-ins toward Jack Nicholson in "The Shining" to build unbearable psychological pressure, and Paul Thomas Anderson employs the slow push-in as a recurring emotional punctuation mark throughout "There Will Be Blood" and "Phant…

**When to use.** Use a push-in when a realization, decision, threat, or confession grows more important while the shot continues. Physical camera movement narrows the viewer's world and can create pressure before they consciously notice why. It suits patient drama better than abrupt surprise. Define what changes during the move; pushing toward a static face without an emotional turn often feels like empty emphasi…

**Directing the AI.** Begin at a clear medium distance and move the camera slowly toward a medium close-up while keeping the lens perspective consistent. The background should shift through natural parallax, proving physical travel rather than a digital zoom. Use gentle vintage focus breathing and warm restrained color, but keep the subject's eyes steadily sharp. Time the approach to a specific thought or line, ending just as the emotional beat lands, then hold instead of continuing indefinitely.

**Common mistakes.**
- Changing focal length without camera travel, producing a zoom that lacks the spatial pressure of a true push-in.
- Moving too quickly for a quiet realization, announcing the emotion before the performance has time to develop.
- Starting already too tight, leaving no meaningful distance for the camera to close during the beat.

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
| declared | `tension-camera-moves` | camera | 150 | `bullet-time-freeze-orbit` |
| declared | `tension-camera-moves` | camera | 150 | `dutch-roll-to-level` |
| declared | `tension-camera-moves` | camera | 150 | `pull-back-isolation` |
| declared | `tension-camera-moves` | camera | 150 | `slow-push-in` |

```
python platform/query.py technique-motions push-in
```

## Sources

- 50+ Types of Camera Shots, Angles, and Techniques

## Related techniques

- [('dolly-shot', 'dolly-shot')](('dolly-shot', 'dolly-shot').md)
- [('medium-close-up', 'medium-close-up')](('medium-close-up', 'medium-close-up').md)
- [('vertigo-effect', 'vertigo-effect')](('vertigo-effect', 'vertigo-effect').md)
- [('aerial-shot', 'aerial-shot')](('aerial-shot', 'aerial-shot').md)
- [('birds-eye-view', 'birds-eye-view')](('birds-eye-view', 'birds-eye-view').md)
- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('dutch-angle', 'dutch-angle')](('dutch-angle', 'dutch-angle').md)
- [('establishing-shot', 'establishing-shot')](('establishing-shot', 'establishing-shot').md)
- [('extreme-close-up', 'extreme-close-up')](('extreme-close-up', 'extreme-close-up').md)
