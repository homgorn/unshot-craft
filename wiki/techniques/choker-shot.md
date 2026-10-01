# "Choker Shot Prompt for AI Image & Video"

`choker-shot` · Camera Work · level intermediate

Reference video: `media/choker-shot.mp4`

## Prompt (verbatim, `[Subject]` intact)

```
Choker shot framing [Subject] from hairline to chin with zero background visible, the skin filling the entire screen like a landscape, harsh toplight creating deep shadow in the eye sockets while illuminating the planes of cheekbone and brow, shot on a 100mm macro lens at T2.8, high-contrast monochromatic color treatment, Bergman-level psychological claustrophobia
```

A very tight shot framing the face from forehead to chin, eliminating nearly all background, more claustrophobic than a standard close-up and often used for moments of extreme emotion. Ingmar Bergman used the choker shot relentlessly in "Persona" and "Cries and Whispers," trapping his actors' faces in frames that feel like emotional prisons. Darren Aronofsky adopted this approach in "Black Swan," keeping Natalie Portman's face in suffocating proximity, and Steve McQueen uses sustained choker shots in "Hunger" and "Shame" to force viewers into uncomfortable intimacy with his characters' pain.

**When to use.** Use a choker shot when a face must become a confined emotional space. Framing from forehead to chin removes almost all context and lets tiny shifts in eyes, mouth, and skin tension feel enormous. It suits panic, shame, obsession, confrontation, and sustained discomfort. Because the closeness is aggressive, save it for peaks or deliberate formal systems rather than ordinary dialogue coverage.

**Directing the AI.** Fill the frame with the face from hairline to chin and remove all visible background. Use a longer or macro portrait perspective to keep features controlled, then shape the planes with hard toplight and deep eye-socket shadow. Preserve pores, moisture, and micro-expression rather than cosmetic smoothness. For video, hold the subject inside this narrow boundary with only breath, blinking, or minute focus drift; large head movement should feel constrained by the frame.

**Common mistakes.**
- Leaving background visible around the head, giving the viewer spatial relief that the choker shot should deny.
- Moving too close with a wide lens, distorting the nose and cheeks into unintended caricature.
- Using the framing for neutral exposition, where its psychological pressure overwhelms the actual dramatic importance.

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
python platform/query.py technique-motions choker-shot
```

## Sources

- 50+ Types of Camera Shots, Angles, and Techniques

## Related techniques

- [('extreme-close-up', 'extreme-close-up')](('extreme-close-up', 'extreme-close-up').md)
- [('medium-close-up', 'medium-close-up')](('medium-close-up', 'medium-close-up').md)
- [('low-key-lighting', 'low-key-lighting')](('low-key-lighting', 'low-key-lighting').md)
- [('aerial-shot', 'aerial-shot')](('aerial-shot', 'aerial-shot').md)
- [('birds-eye-view', 'birds-eye-view')](('birds-eye-view', 'birds-eye-view').md)
- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('dutch-angle', 'dutch-angle')](('dutch-angle', 'dutch-angle').md)
- [('dolly-shot', 'dolly-shot')](('dolly-shot', 'dolly-shot').md)
- [('establishing-shot', 'establishing-shot')](('establishing-shot', 'establishing-shot').md)
