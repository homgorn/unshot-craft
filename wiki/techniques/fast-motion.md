# "Fast Motion Prompt for AI Image & Video"

`fast-motion` · Editing · level basic

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Fast motion sequence of [Subject] accelerated to four times normal speed, the slight jerkiness of undercranked footage adding comedic effect, every movement purposeful but absurdly accelerated, the Buster Keaton energy of a body moving faster than physics allows, warm light consistent but shadows racing across surfaces
```

Footage played back faster than it was captured, compressing real-time action to create comedy, frenetic energy, or an accelerated sense of unstoppable momentum. Buster Keaton and Charlie Chaplin used undercranking to create the frenetic comedy of the silent era. Stanley Kubrick used fast motion for the threesome scene in "A Clockwork Orange" set to William Tell's Overture. Guy Ritchie employs speed ramping and fast motion in "Snatch" and "Lock, Stock and Two Smoking Barrels" as a signature stylistic device. Wes Anderson uses deadpan fast motion in montage sequences throughout "The Royal Tene…

**When to use.** Use fast motion for compressed routines, frantic escapes, mechanical work, comic physicality, or bursts of momentum that would drag at normal speed. It is strongest when the audience already understands the action and can enjoy its accelerated rhythm. Use it selectively inside a sequence; sustained speed can flatten emphasis, while a short burst can make an ordinary movement feel absurd, efficien…

**Directing the AI.** Stage the action in a readable wide or medium frame, then specify playback at roughly four times normal speed. Keep movement paths simple, purposeful, and continuous so acceleration remains legible. Let bodies and props carry a slight undercranked jerkiness when comedy is wanted, but preserve stable backgrounds and consistent light. Use racing shadows only if time itself is passing. End on a clear action beat rather than cutting during visual confusion.

**Common mistakes.**
- Accelerating complicated blocking until characters overlap, props teleport, and the audience can no longer follow cause and effect.
- Using fast motion for emotionally delicate acting, where facial nuance and hesitation need real duration to register.
- Mixing rapid playback with uncontrolled camera shake, producing visual noise instead of comic or kinetic rhythm.

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
python platform/query.py technique-motions fast-motion
```

## Sources

- What Is Film Editing?

## Related techniques

- [('slow-motion', 'slow-motion')](('slow-motion', 'slow-motion').md)
- [('montage', 'montage')](('montage', 'montage').md)
- [('jump-cut', 'jump-cut')](('jump-cut', 'jump-cut').md)
- [('cross-cutting', 'cross-cutting')](('cross-cutting', 'cross-cutting').md)
- [('dissolve', 'dissolve')](('dissolve', 'dissolve').md)
- [('fade-in-out', 'fade-in-out')](('fade-in-out', 'fade-in-out').md)
- [('smash-cut', 'smash-cut')](('smash-cut', 'smash-cut').md)
- [('long-take', 'long-take')](('long-take', 'long-take').md)
- [('freeze-frame', 'freeze-frame')](('freeze-frame', 'freeze-frame').md)
