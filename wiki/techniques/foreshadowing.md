# "Foreshadowing Prompt for AI Image & Video"

`foreshadowing` · Narrative · level intermediate

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
Foreshadowing detail hiding in plain sight around [Subject], a seemingly ordinary detail barely visible that the viewer will only recognize as prophetic on a second viewing, every element appearing innocent on first viewing but loaded with ominous meaning in retrospect, warm amber domestic lighting that makes the scene feel safe even as visual clues whisper that safety is temporary
```

Planting subtle hints of events to come — a cracked mirror, a line of dialogue, a color choice — details that seem innocuous on first viewing but become devastating on rewatch. Stanley Kubrick embedded foreshadowing details so densely in "The Shining" that the documentary "Room 237" is dedicated entirely to analyzing them. M. Night Shyamalan structures "The Sixth Sense" so that every scene contains foreshadowing of the twist ending. The Coen Brothers plant narrative seeds early — the wood chipper glimpsed in the first act of "Fargo" becomes the instrument of horror in the third. Denis Villene…

**When to use.** Use foreshadowing when a later reveal should feel earned rather than arbitrary. Plant a prop, shape, color, gesture, or line whose first meaning is ordinary and whose second meaning appears only after the outcome. It is ideal for mystery, tragedy, twists, and mounting dread. The clue must be visible enough to register unconsciously, yet integrated naturally enough that first-time viewers do not s…

**Directing the AI.** Compose a safe, ordinary scene around the main subject, then place one consequential detail near the edge of attention. Match its scale, light, and material to the environment so it belongs there. Avoid isolating it with a spotlight or explicit close-up. Repeat its shape, color, or position later if the pattern matters. On rewatch, the clue should look deliberate; on first viewing, it should remain plausible background information rather than a warning label.

**Common mistakes.**
- Centering and spotlighting the clue so aggressively that the future reveal becomes obvious on first viewing.
- Planting a detail with no later payoff, teaching the audience to distrust the story's visual information.
- Using an unrelated ominous object instead of a clue that connects specifically to the eventual event.

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
| declared | `assemble-then-type-flyin` | effects | 156 | `assemble-then-type-flyin` |

```
python platform/query.py technique-motions foreshadowing
```

## Sources

- How to Make a Short Film: An Introduction to Filmmaking

## Related techniques

- [('motif', 'motif')](('motif', 'motif').md)
- [('symbolism', 'symbolism')](('symbolism', 'symbolism').md)
- [('flashforward', 'flashforward')](('flashforward', 'flashforward').md)
- [('flashback', 'flashback')](('flashback', 'flashback').md)
- [('breaking-fourth-wall', 'breaking-fourth-wall')](('breaking-fourth-wall', 'breaking-fourth-wall').md)
- [('in-medias-res', 'in-medias-res')](('in-medias-res', 'in-medias-res').md)
- [('cliffhanger', 'cliffhanger')](('cliffhanger', 'cliffhanger').md)
- [('non-linear-narrative', 'non-linear-narrative')](('non-linear-narrative', 'non-linear-narrative').md)
- [('parallel-storylines', 'parallel-storylines')](('parallel-storylines', 'parallel-storylines').md)
