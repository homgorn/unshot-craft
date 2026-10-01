# "Extreme Close-Up Prompt for AI Image & Video"

`extreme-close-up` · Camera Work · level basic

Reference video: `media/extreme-close-up.mp4`

## Prompt (verbatim, `[Subject]` intact)

```
Extreme macro close-up of [Subject] filling the entire frame, every microscopic detail rendered with clinical precision, ring light creating a circular catchlight, razor-thin depth of field at f/2.8 on a 100mm macro lens, Fujifilm Velvia-inspired saturated color science, the forensic intimacy of extreme proximity
```

An intensely tight shot focusing on a very specific detail — an eye, a hand trembling, a drop of sweat — amplifying significance and forcing the viewer into intimate proximity with the subject. Sergio Leone built the climax of "The Good, the Bad and the Ugly" almost entirely from extreme close-ups of eyes during the three-way standoff, creating unbearable tension through the intimacy of a glance. Darren Aronofsky used macro close-ups of dilating pupils and needle punctures in "Requiem for a Dream" to physicalize addiction. David Lynch frequently employs extreme close-ups of mundane objects to…

**When to use.** Cut to an extreme close-up when one tiny detail must carry the scene: a pupil changing, a finger tightening, sweat forming, or a needle touching skin. The frame forces attention and turns physical texture into emotion. Use it to intensify suspense, reveal evidence, or make an ordinary object uncanny. Its power drops quickly when every beat receives the same microscopic treatment.

**Directing the AI.** Name the exact fragment that fills the frame and exclude the wider face or body. Ask for macro-scale detail, a 100mm macro perspective, razor-thin depth of field, and one precise focus plane. A circular catchlight or controlled ring light can reveal surface structure without flattening the subject. Keep background information abstract or absent. In video, limit motion to a tremor, blink, bead of moisture, or minute focus adjustment so proximity remains the event.

**Common mistakes.**
- Prompting a generic close-up instead of naming the exact eye, fingertip, wound, or object detail that fills frame.
- Demanding sharpness everywhere, which removes the selective attention and optical intimacy of true macro framing.
- Adding a busy background that reintroduces context and breaks the suffocating proximity of the chosen detail.

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
| declared | `spotlight-hero-card` | opening | 220 | `spotlight-hero-card` |

```
python platform/query.py technique-motions extreme-close-up
```

## Sources

- 50+ Types of Camera Shots, Angles, and Techniques

## Related techniques

- [('choker-shot', 'choker-shot')](('choker-shot', 'choker-shot').md)
- [('insert-shot', 'insert-shot')](('insert-shot', 'insert-shot').md)
- [('shallow-focus', 'shallow-focus')](('shallow-focus', 'shallow-focus').md)
- [('aerial-shot', 'aerial-shot')](('aerial-shot', 'aerial-shot').md)
- [('birds-eye-view', 'birds-eye-view')](('birds-eye-view', 'birds-eye-view').md)
- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('dutch-angle', 'dutch-angle')](('dutch-angle', 'dutch-angle').md)
- [('dolly-shot', 'dolly-shot')](('dolly-shot', 'dolly-shot').md)
- [('establishing-shot', 'establishing-shot')](('establishing-shot', 'establishing-shot').md)
