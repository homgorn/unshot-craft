# "One-er (Oner) Prompt for AI Image & Video"

`one-er` · Camera Work · level advanced

Reference video: `media/one-er.mp4`

## Prompt (verbatim, `[Subject]` intact)

```
Long unbroken single take following [Subject] through shifting environments, the entire journey unbroken for minutes of choreographed spatial continuity, shot on Steadicam with an ARRI Alexa Mini and Cooke S4 21mm lens, the shifting light temperatures creating a living color journey through the space
```

An entire scene captured in a single unbroken take with no cuts, demanding precise choreography of actors, camera, and crew while creating real-time tension and immersive spatial continuity. Alfonso Cuarón and Emmanuel Lubezki pushed the oner to its limits in "Children of Men" with a six-minute car ambush shot, and Alejandro González Iñárritu structured the entirety of "Birdman" as one apparent continuous take. Alexander Sokurov actually achieved a true single-take feature film with "Russian Ark," 96 unbroken minutes wandering through the Hermitage Museum. Sam Mendes' "1917" used hidden cuts…

**When to use.** Use a oner when real-time continuity should create immersion, pressure, or virtuoso flow. It can follow characters through connected rooms, preserve an escalating performance, or make viewers discover action as the camera does. The scene needs choreography strong enough to justify the absence of cuts. Choose conventional coverage when time must compress, geography can be fragmented, or the genera…

**Directing the AI.** Describe one unbroken route from the opening composition to the final position, including each doorway, turn, actor crossing, focus change, and lighting transition. Keep the lens moderately wide and the movement Steadicam-smooth so space remains readable. Assign timed actions that motivate the camera's attention without implying cuts. Carry persistent wardrobe, props, and screen direction through every beat. If hidden transitions are intended, identify the exact occlusion instead of allowing ar…

**Common mistakes.**
- Writing only long continuous take without mapping the route, leaving the scene vulnerable to spatial jumps and changed details.
- Packing unrelated events into the move, so choreography feels like a demonstration rather than one developing dramatic beat.
- Using abrupt focal-length changes or impossible camera teleportation that function as cuts despite continuous-shot language.

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
| declared | `fracture` | opening | 156 | `fracture` |

```
python platform/query.py technique-motions one-er
```

## Sources

- 50+ Types of Camera Shots, Angles, and Techniques

## Related techniques

- [('long-take', 'long-take')](('long-take', 'long-take').md)
- [('steadicam', 'steadicam')](('steadicam', 'steadicam').md)
- [('master-shot', 'master-shot')](('master-shot', 'master-shot').md)
- [('aerial-shot', 'aerial-shot')](('aerial-shot', 'aerial-shot').md)
- [('birds-eye-view', 'birds-eye-view')](('birds-eye-view', 'birds-eye-view').md)
- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('dutch-angle', 'dutch-angle')](('dutch-angle', 'dutch-angle').md)
- [('dolly-shot', 'dolly-shot')](('dolly-shot', 'dolly-shot').md)
- [('establishing-shot', 'establishing-shot')](('establishing-shot', 'establishing-shot').md)
