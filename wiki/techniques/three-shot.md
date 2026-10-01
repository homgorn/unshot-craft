# "Three-Shot Prompt for AI Image & Video"

`three-shot` · Camera Work · level intermediate

Reference video: `media/three-shot.mp4`

## Prompt (verbatim, `[Subject]` intact)

```
Three-shot of [Subject] arranged in a triangular composition across the widescreen frame, each occupying their own third, the triangular formation revealing tension between completely different energies colliding at a single point, shot on anamorphic 50mm with the wide frame emphasizing space between the three figures
```

A shot framing three subjects, often used to show group dynamics, alliances, or the odd-one-out tension within a trio. Sergio Leone perfected the three-shot in the climactic standoff of "The Good, the Bad and the Ugly," cycling between three armed men in a graveyard to create one of cinema's most iconic compositions. Akira Kurosawa uses triangular three-shots in "Rashomon" to stage conflicting testimonies, and the Coen Brothers frequently compose three-shots in their ensemble comedies like "The Big Lebowski" to play dynamics of alliance and exclusion within a group.

**When to use.** Choose a three-shot when the drama comes from a trio rather than three separate characters. Triangular placement can reveal two against one, a mediator caught between rivals, or unstable alliances that change inside the scene. It suits standoffs, negotiations, comedy, and family tension. Avoid lining everyone up equally unless neutrality is intentional; the arrangement should make the group's emo…

**Directing the AI.** Place three subjects at distinct points of a triangle across the widescreen frame, varying depth or height to establish hierarchy. Give each person a readable eyeline and body orientation toward or away from the others. Keep the spaces between them clear so alliance and exclusion can shift through movement. Use an anamorphic field without crowding the edges. In video, specify the gesture or step that changes the triangle and redistributes visual weight.

**Common mistakes.**
- Arranging the trio in a flat shoulder-to-shoulder row, which hides alliances and makes the composition feel posed.
- Giving all three characters equal visual weight when the scene depends on one person being isolated or dominant.
- Allowing eyelines to point randomly, making the characters appear disconnected from the conversation or standoff.

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
python platform/query.py technique-motions three-shot
```

## Sources

- 50+ Types of Camera Shots, Angles, and Techniques

## Related techniques

- [('triangular-composition', 'triangular-composition')](('triangular-composition', 'triangular-composition').md)
- [('two-shot', 'two-shot')](('two-shot', 'two-shot').md)
- [('balancing-elements', 'balancing-elements')](('balancing-elements', 'balancing-elements').md)
- [('aerial-shot', 'aerial-shot')](('aerial-shot', 'aerial-shot').md)
- [('birds-eye-view', 'birds-eye-view')](('birds-eye-view', 'birds-eye-view').md)
- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('dutch-angle', 'dutch-angle')](('dutch-angle', 'dutch-angle').md)
- [('dolly-shot', 'dolly-shot')](('dolly-shot', 'dolly-shot').md)
- [('establishing-shot', 'establishing-shot')](('establishing-shot', 'establishing-shot').md)
