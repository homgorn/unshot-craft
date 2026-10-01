# "Insert Shot Prompt for AI Image & Video"

`insert-shot` · Camera Work · level basic

Reference video: `media/insert-shot.mp4`

## Prompt (verbatim, `[Subject]` intact)

```
Insert shot of [Subject] isolated in tight framing, warm lamplight casting a golden glow while the surrounding space falls into shadow, shot with a macro lens at f/2 creating razor-thin focus, Kodak 5219 500T film stock warmth, the weight of consequence concentrated in a single object
```

A close-up cut to a specific detail within a scene — a ticking clock, a letter, a weapon being drawn — directing audience attention to a crucial narrative element. Hitchcock was the supreme master of the insert shot, using close-ups of keys, glasses of milk, and scissors in films like "Dial M for Murder" and "Notorious" to build unbearable suspense from ordinary objects. Quentin Tarantino uses stylized insert shots of food, weapons, and car details as a rhythmic signature, while Edgar Wright employs rapid-fire inserts for comedic punctuation in "Shaun of the Dead" and "Hot Fuzz."

**When to use.** Use an insert when the audience must notice a detail that changes how the scene is understood. A key turning, clock ticking, letter opening, weapon clearing a holster, or hand hesitating can carry plot and tension in a compact frame. The object should already belong to the scene. Insert shots are strongest as punctuation; too many make the sequence feel mechanically illustrated.

**Directing the AI.** Identify one object or action and frame it tightly enough that nothing competes for attention. Light it with a motivated warm lamp or practical source while the surrounding area falls into shadow. Use macro-like proximity, a narrow focus plane, and tactile material detail to give the object consequence. For video, define the exact event within the insert, such as a second hand advancing or a thumb releasing a safety, then cut away promptly.

**Common mistakes.**
- Choosing an object with no later consequence, training viewers to search for meaning that the sequence never pays off.
- Including too much of the surrounding scene, so attention remains divided instead of landing on the narrative detail.
- Rendering the insert in a mismatched lighting style that disconnects it from the space established around it.

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
python platform/query.py technique-motions insert-shot
```

## Sources

- 50+ Types of Camera Shots, Angles, and Techniques

## Related techniques

- [('cut-in', 'cut-in')](('cut-in', 'cut-in').md)
- [('cutaway', 'cutaway')](('cutaway', 'cutaway').md)
- [('extreme-close-up', 'extreme-close-up')](('extreme-close-up', 'extreme-close-up').md)
- [('aerial-shot', 'aerial-shot')](('aerial-shot', 'aerial-shot').md)
- [('birds-eye-view', 'birds-eye-view')](('birds-eye-view', 'birds-eye-view').md)
- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('dutch-angle', 'dutch-angle')](('dutch-angle', 'dutch-angle').md)
- [('dolly-shot', 'dolly-shot')](('dolly-shot', 'dolly-shot').md)
- [('establishing-shot', 'establishing-shot')](('establishing-shot', 'establishing-shot').md)
