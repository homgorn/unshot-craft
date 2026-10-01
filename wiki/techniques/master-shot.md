# "Master Shot Prompt for AI Image & Video"

`master-shot` · Camera Work · level intermediate

Reference video: `media/master-shot.mp4`

## Prompt (verbatim, `[Subject]` intact)

```
Wide master shot of [Subject] with all elements visible simultaneously, every figure precisely blocked to create a composition of intersecting eyelines and subtle tensions, shot on 35mm with a 27mm lens from a tripod, classical Hollywood staging with Altman-esque layered naturalism
```

A continuous wide shot that captures the entire scene from start to finish, serving as the foundation over which closer coverage is layered in editing. Robert Altman was famous for shooting elaborate master shots with multiple overlapping conversations in films like "Nashville" and "Short Cuts," trusting the wide frame to let audiences discover the drama themselves. Sidney Lumet staged masterful master shots in "12 Angry Men," choreographing twelve actors within a single room with balletic precision. Mike Leigh builds entire scenes from master shots that allow his actors' improvisational perf…

**When to use.** Build a master shot when a scene depends on ensemble timing, spatial continuity, or the audience choosing where to look. It provides the full dramatic action in one wide composition and becomes a foundation for closer coverage. The format suits overlapping conversations, group conflict, and carefully blocked rooms. It is less effective when the setting cannot support layered action or when one fa…

**Directing the AI.** Show the entire playing area and every essential figure at once. Block actors on distinct depth planes with intersecting eyelines, clear entrances, and enough separation to read alliances or friction. Use a stable tripod perspective and a moderately wide lens rather than an exaggerated panorama. Lighting should motivate attention inside the frame without hiding secondary action. For video, describe the scene's full beginning-to-end choreography, not merely a wide opening before an automatic cut.

**Common mistakes.**
- Arranging every actor in a flat line, which records the cast but reveals nothing about hierarchy or tension.
- Framing so wide that gestures and eyelines become unreadable, defeating the purpose of sustained ensemble staging.
- Calling a short location reveal a master shot even though it does not contain the scene's complete dramatic action.

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
| declared | `space-camera-moves` | camera | 150 | `drone-dive-landing` |
| declared | `space-camera-moves` | camera | 150 | `exploded-view` |

```
python platform/query.py technique-motions master-shot
```

## Sources

- 50+ Types of Camera Shots, Angles, and Techniques

## Related techniques

- [('one-er', 'one-er')](('one-er', 'one-er').md)
- [('deep-focus', 'deep-focus')](('deep-focus', 'deep-focus').md)
- [('mise-en-scene', 'mise-en-scene')](('mise-en-scene', 'mise-en-scene').md)
- [('aerial-shot', 'aerial-shot')](('aerial-shot', 'aerial-shot').md)
- [('birds-eye-view', 'birds-eye-view')](('birds-eye-view', 'birds-eye-view').md)
- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('dutch-angle', 'dutch-angle')](('dutch-angle', 'dutch-angle').md)
- [('dolly-shot', 'dolly-shot')](('dolly-shot', 'dolly-shot').md)
- [('establishing-shot', 'establishing-shot')](('establishing-shot', 'establishing-shot').md)
