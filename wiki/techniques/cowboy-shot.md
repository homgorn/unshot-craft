# "Cowboy Shot Prompt for AI Image & Video"

`cowboy-shot` · Camera Work · level basic

Reference video: `media/cowboy-shot.mp4`

## Prompt (verbatim, `[Subject]` intact)

```
Cowboy shot of [Subject] framed from mid-thigh up, hands hanging loose at their sides, the figure's posture radiating coiled readiness beneath apparent calm, shot on Techniscope 2-perf 35mm for a gritty widescreen look, warm dusty color palette of ochre and leather brown
```

Frames the subject from roughly mid-thigh up, named after Western films where the frame needed to include a gunslinger's holstered weapon, conveying casual authority. Sergio Leone codified this framing in his Dollars trilogy, making the cowboy shot synonymous with Clint Eastwood's laconic gunfighter stance. Tarantino pays homage to the cowboy shot throughout "Kill Bill" and "Django Unchained," and it has migrated beyond Westerns — John Woo uses the same mid-thigh framing for his dual-pistol action heroes in "Hard Boiled" and "The Killer."

**When to use.** Use the cowboy shot when a character's hands, hips, stance, or carried weapon matters alongside the face. Mid-thigh framing conveys readiness and casual authority without losing expression. It fits Western tension, action entrances, fashion, and any moment built around what someone might reach for. Choose a medium shot for more conversational ease, or a full long shot when footwork and environmen…

**Directing the AI.** Crop the figure at mid-thigh, keeping both hands visible and enough headroom for a stable silhouette. Ask for a relaxed but ready posture, with weight distribution and wardrobe details doing as much work as expression. Use a gritty widescreen texture, warm ochre and leather tones, and a natural perspective that does not stretch the legs. In video, hold the framing through hand movement rather than automatically pushing closer to the face.

**Common mistakes.**
- Cropping at the waist, which removes the holster zone and turns the image into a standard medium shot.
- Hiding both hands behind props or frame edges, losing the latent action that gives the composition tension.
- Using an exaggerated low angle by default, piling obvious dominance onto framing that already carries authority.

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
python platform/query.py technique-motions cowboy-shot
```

## Sources

- 50+ Types of Camera Shots, Angles, and Techniques

## Related techniques

- [('medium-shot', 'medium-shot')](('medium-shot', 'medium-shot').md)
- [('long-shot', 'long-shot')](('long-shot', 'long-shot').md)
- [('spaghetti-western', 'spaghetti-western')](('spaghetti-western', 'spaghetti-western').md)
- [('aerial-shot', 'aerial-shot')](('aerial-shot', 'aerial-shot').md)
- [('birds-eye-view', 'birds-eye-view')](('birds-eye-view', 'birds-eye-view').md)
- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('dutch-angle', 'dutch-angle')](('dutch-angle', 'dutch-angle').md)
- [('dolly-shot', 'dolly-shot')](('dolly-shot', 'dolly-shot').md)
- [('establishing-shot', 'establishing-shot')](('establishing-shot', 'establishing-shot').md)
