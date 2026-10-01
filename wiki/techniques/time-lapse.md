# "Time-Lapse Prompt for AI Image & Video"

`time-lapse` · Editing · level intermediate

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Time-lapse of [Subject] compressed from hours into seconds, light cycling through the full spectrum of the day, shadows rotating like sundial hands, the entire rhythm of existence compressed into a single visual breath, shot on a locked-off camera with an intervalometer, the Koyaanisqatsi revelation that accelerating time reveals patterns invisible to human perception
```

Capturing frames at intervals much slower than playback speed, compressing hours, days, or months into seconds to reveal processes invisible to normal perception — clouds racing, cities pulsing. Ron Fricke's "Koyaanisqatsi" (with Philip Glass's score) turned time-lapse into transcendent art, showing the rhythms of nature and civilization accelerated into hypnotic visual music. Terrence Malick uses time-lapse in "The Tree of Life" for cosmic creation sequences. David Fincher employed time-lapse in "Fight Club" and "The Curious Case of Benjamin Button" for both practical and poetic purposes. Mo…

**When to use.** Use time-lapse when the story needs to show a process whose scale exceeds ordinary screen time: daylight crossing a room, clouds building, streets filling, or a structure changing. It can bridge hours, mark labor, reveal systems, or turn gradual transformation into visual rhythm. The technique works when change is the subject; it feels empty when nothing meaningful evolves within the locked compo…

**Directing the AI.** Lock the camera and define a clear start state, end state, and visible process between them. Keep permanent architecture and horizon lines stable while clouds, shadows, traffic, people, or growth accelerate through frame. Describe light cycling across a believable path, with shadows rotating consistently rather than flickering randomly. Maintain one composition throughout. Compress duration aggressively, but preserve enough intermediate stages for the transformation to read as a continuous patt…

**Common mistakes.**
- Moving the camera without purpose, which hides the gradual pattern that time compression is meant to reveal.
- Accelerating every element equally, making solid buildings wobble or permanent objects mutate with passing time.
- Providing no distinct beginning or ending state, so the sequence feels busy without communicating change.

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
| declared | `speed-ramp-freeze` | rhythm | 40 | `freeze-annotate-real` |
| declared | `speed-ramp-freeze` | rhythm | 40 | `speed-ramp-real` |

```
python platform/query.py technique-motions time-lapse
```

## Sources

- What Is Film Editing?

## Related techniques

- [('montage', 'montage')](('montage', 'montage').md)
- [('slow-motion', 'slow-motion')](('slow-motion', 'slow-motion').md)
- [('static-shot', 'static-shot')](('static-shot', 'static-shot').md)
- [('cross-cutting', 'cross-cutting')](('cross-cutting', 'cross-cutting').md)
- [('jump-cut', 'jump-cut')](('jump-cut', 'jump-cut').md)
- [('dissolve', 'dissolve')](('dissolve', 'dissolve').md)
- [('fade-in-out', 'fade-in-out')](('fade-in-out', 'fade-in-out').md)
- [('smash-cut', 'smash-cut')](('smash-cut', 'smash-cut').md)
- [('long-take', 'long-take')](('long-take', 'long-take').md)
