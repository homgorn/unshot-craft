# "Medium Close-Up Prompt for AI Image & Video"

`medium-close-up` · Camera Work · level basic

Reference video: `media/medium-close-up.mp4`

## Prompt (verbatim, `[Subject]` intact)

```
Medium close-up of [Subject] from the chest up, the intimate distance perfect for reading micro-expressions while body language of tension remains visible in the shoulders and hands, shot on a 75mm Cooke S4 at T2, noir-inflected color palette of deep blues and intermittent warm accents
```

Frames the subject from the chest up, tighter than a medium shot but not as intimate as a close-up, ideal for emotional dialogue while retaining some body language context. This framing became the default for television drama and is the backbone of prestige TV from "The Sopranos" to "Breaking Bad." In cinema, Michael Mann favors the medium close-up in "Heat" and "Collateral" to maintain both the intensity of facial performance and the physical awareness of characters in dangerous environments. Jonathan Demme's slightly-off-center medium close-ups became his signature from "Silence of the Lamb…

**When to use.** Choose a medium close-up when emotional dialogue needs intimacy without the pressure of a full close-up. Chest-up framing keeps micro-expressions legible while shoulders and upper-body tension remain available. It is strong for interviews, confession, restrained conflict, and reaction beats. Pull wider when hands or spatial relations matter; move tighter when the face must become the entire drama…

**Directing the AI.** Frame from the chest upward, keeping the shoulders fully present and the eyes near the upper third. Use a slightly longer portrait perspective, moderate background blur, and controlled contrast that preserves skin detail. Let small changes in jaw, breath, and shoulder position carry the performance. Include only enough environment to anchor location. For video, avoid automatic zooming; hold the intimate distance and let the actor's micro-expressions create the variation.

**Common mistakes.**
- Cropping beneath the chin or above the shoulders, which turns the intended frame into a tight close-up.
- Leaving too much torso visible, weakening facial emphasis and drifting back toward a conventional medium shot.
- Smoothing skin and expression so aggressively that the subtle performance cues the framing exists to capture disappear.

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
python platform/query.py technique-motions medium-close-up
```

## Sources

- 50+ Types of Camera Shots, Angles, and Techniques

## Related techniques

- [('medium-shot', 'medium-shot')](('medium-shot', 'medium-shot').md)
- [('choker-shot', 'choker-shot')](('choker-shot', 'choker-shot').md)
- [('eye-light', 'eye-light')](('eye-light', 'eye-light').md)
- [('aerial-shot', 'aerial-shot')](('aerial-shot', 'aerial-shot').md)
- [('birds-eye-view', 'birds-eye-view')](('birds-eye-view', 'birds-eye-view').md)
- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('dutch-angle', 'dutch-angle')](('dutch-angle', 'dutch-angle').md)
- [('dolly-shot', 'dolly-shot')](('dolly-shot', 'dolly-shot').md)
- [('establishing-shot', 'establishing-shot')](('establishing-shot', 'establishing-shot').md)
