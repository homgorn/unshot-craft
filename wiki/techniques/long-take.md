# "Long Take Prompt for AI Image & Video"

`long-take` · Editing · level advanced

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Long unbroken take following [Subject] in real time through continuous space, the single take creating immersive experience where the viewer is trapped in real-time, shot on Steadicam with an ARRI Alexa Mini and 21mm Zeiss lens, the shifting light creating a natural color temperature journey, the unbroken continuity refusing to let the viewer escape into a cut
```

An extended shot that runs significantly longer than conventional cuts, building real-time tension, showcasing performance, and immersing the viewer in unbroken space and time. Alfonso Cuarón and Emmanuel Lubezki pushed the long take to new extremes in "Children of Men" with the legendary six-minute car ambush, and later in "Gravity" and "Roma." Alejandro González Iñárritu's "Birdman" is constructed as one apparent continuous take. Andrei Tarkovsky's long takes in "Stalker" and "Mirror" unfold with hypnotic patience, while Béla Tarr's "Sátántangó" contains takes lasting over ten minutes. The…

**When to use.** A long take works when real-time duration, spatial continuity, or performance tension should trap the audience inside the event. Use it for entrances, conversations that shift power, journeys through complex space, action with readable geography, or patient observation. The shot must evolve internally through blocking, camera movement, focus, and revelation. Length alone is not the achievement; e…

**Directing the AI.** Plan one uninterrupted route with a clear starting frame, several blocking beats, and a decisive endpoint. Move the camera only when subject action or a reveal motivates it, preserving stable geography and consistent screen direction. Coordinate focus, exposure, and background activity as the shot enters new zones. Let performers cross foreground and background without identity drift. Avoid hidden jumps, resets, or impossible object changes. Build tension through real-time timing and changing p…

**Common mistakes.**
- Letting the camera wander without new blocking, information, or pressure, confusing duration with meaningful immersion.
- Changing doors, props, extras, or subject identity mid-shot, breaking the continuous space the technique depends on.
- Hiding obvious cuts behind every passing object, reducing an unbroken performance into a stitched visual trick.

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
| declared | `crane-rise-reveal` | opening | 20 | `crane-rise-reveal` |

```
python platform/query.py technique-motions long-take
```

## Sources

- What Is Film Editing?

## Related techniques

- [('one-er', 'one-er')](('one-er', 'one-er').md)
- [('steadicam', 'steadicam')](('steadicam', 'steadicam').md)
- [('tracking-shot', 'tracking-shot')](('tracking-shot', 'tracking-shot').md)
- [('cross-cutting', 'cross-cutting')](('cross-cutting', 'cross-cutting').md)
- [('jump-cut', 'jump-cut')](('jump-cut', 'jump-cut').md)
- [('dissolve', 'dissolve')](('dissolve', 'dissolve').md)
- [('fade-in-out', 'fade-in-out')](('fade-in-out', 'fade-in-out').md)
- [('montage', 'montage')](('montage', 'montage').md)
- [('smash-cut', 'smash-cut')](('smash-cut', 'smash-cut').md)
