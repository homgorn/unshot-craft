# "Vertigo Effect Prompt for AI Image & Video"

`vertigo-effect` · Camera Work · level advanced

Reference video: `media/vertigo-effect.mp4`

## Prompt (verbatim, `[Subject]` intact)

```
Vertigo effect dolly zoom on [Subject] locked in frame while the background warps and telescopes away in a nauseating spatial contradiction, the zoom and dolly counter-movement perfectly synchronized, desaturated palette with sickly yellow-green undertones, shot on anamorphic glass, Hitchcock's visual language of psychological vertigo made manifest
```

Also called a dolly zoom — the camera dollies in while zooming out (or vice versa), causing the background to warp while the subject stays the same size, creating a visceral sense of disorientation. Invented by cameraman Irmin Roberts for Alfred Hitchcock's "Vertigo" (1958) to visualize James Stewart's acrophobia, the technique was later used to devastating effect by Steven Spielberg in "Jaws" — the moment Chief Brody sees the shark attack from the beach. Peter Jackson employed it in "The Lord of the Rings" when Frodo senses the Ringwraiths approaching, and Sam Raimi made it a horror staple i…

**When to use.** Deploy the vertigo effect at a moment of shock, dread, realization, or altered perception. The subject stays the same size while the world behind them telescopes, making stable space feel suddenly impossible. It works when psychology and environment must collide in one mechanical move. Because the distortion is conspicuous, use it sparingly and motivate it with a precise emotional turn rather tha…

**Directing the AI.** Lock the subject's size and central position throughout the shot. Move the camera physically inward while zooming outward, or reverse both actions, with perfect counter-synchronization. The foreground face should remain stable as background distance stretches or compresses visibly along strong depth lines. Use a desaturated palette with sickly yellow-green undertones and restrained anamorphic texture. State the move's duration and emotional trigger; do not ask for a normal push-in with incident…

**Common mistakes.**
- Allowing the subject to grow during the move, which turns the setup into an ordinary zoom or dolly approach.
- Choosing a flat background with no depth lines, leaving little visible space for the contradiction to warp.
- Using the effect repeatedly, so a powerful psychological rupture becomes a predictable transition between ordinary shots.

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
| declared | `steep-tilt-glide` | camera | 120 | `steep-tilt-glide` |

```
python platform/query.py technique-motions vertigo-effect
```

## Sources

- 50+ Types of Camera Shots, Angles, and Techniques

## Related techniques

- [('dolly-shot', 'dolly-shot')](('dolly-shot', 'dolly-shot').md)
- [('push-in', 'push-in')](('push-in', 'push-in').md)
- [('lens-distortion', 'lens-distortion')](('lens-distortion', 'lens-distortion').md)
- [('aerial-shot', 'aerial-shot')](('aerial-shot', 'aerial-shot').md)
- [('birds-eye-view', 'birds-eye-view')](('birds-eye-view', 'birds-eye-view').md)
- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('dutch-angle', 'dutch-angle')](('dutch-angle', 'dutch-angle').md)
- [('establishing-shot', 'establishing-shot')](('establishing-shot', 'establishing-shot').md)
- [('extreme-close-up', 'extreme-close-up')](('extreme-close-up', 'extreme-close-up').md)
