# "Pull Out Prompt for AI Image & Video"

`pull-out` · Camera Work · level intermediate

Reference video: `media/pull-out.mp4`

## Prompt (verbatim, `[Subject]` intact)

```
Pull-out shot beginning tight on [Subject] then slowly withdrawing to reveal the true scale of their surroundings, the shot transitioning from intimacy to cosmic isolation in one continuous movement, shot on 24mm wide-angle lens mounted on a telescoping jib arm, the scale expanding to swallow the individual
```

The camera physically moves away from the subject, revealing more of the environment, often used to create a sense of isolation, revelation, or to transition from intimate to epic scale. The final pull-out of "The Truman Show" — revealing that Truman's entire world is a television set — is a defining use of the technique. Steven Spielberg's pull-out in "Schindler's List" from Oskar Schindler to reveal the enormous line of saved workers is emotionally devastating. The famous opening of Robert Altman's "The Player" pulls out from an office window to reveal the entire studio lot in one continuou…

**When to use.** Choose a pull-out when new context should reframe an intimate moment. Moving away can reveal a crowd, set, landscape, aftermath, or barrier that changes the subject's meaning and makes them feel isolated. It works for endings, revelations, and transitions from personal to epic scale. The wider information must matter; withdrawing only to show more empty room rarely earns the emotional shift.

**Directing the AI.** Start tightly enough to read the subject's expression, then move the camera physically backward in one continuous path. Let foreground objects enter and background architecture expand through visible parallax, gradually reducing the person inside the composition. Use a wide perspective only as space opens, not as a sudden lens jump. Specify the final revealed element and maintain the subject's screen position so viewers can track them as the environment begins to swallow the frame.

**Common mistakes.**
- Revealing nothing consequential beyond the original frame, so the withdrawal changes size but not meaning.
- Shrinking the subject through a zoom alone, missing the foreground parallax that makes physical retreat convincing.
- Losing the subject behind newly revealed objects before the audience can compare them with the larger environment.

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
python platform/query.py technique-motions pull-out
```

## Sources

- 50+ Types of Camera Shots, Angles, and Techniques

## Related techniques

- [('crane-shot', 'crane-shot')](('crane-shot', 'crane-shot').md)
- [('extreme-long-shot', 'extreme-long-shot')](('extreme-long-shot', 'extreme-long-shot').md)
- [('dolly-shot', 'dolly-shot')](('dolly-shot', 'dolly-shot').md)
- [('aerial-shot', 'aerial-shot')](('aerial-shot', 'aerial-shot').md)
- [('birds-eye-view', 'birds-eye-view')](('birds-eye-view', 'birds-eye-view').md)
- [('close-up', 'close-up')](('close-up', 'close-up').md)
- [('dutch-angle', 'dutch-angle')](('dutch-angle', 'dutch-angle').md)
- [('establishing-shot', 'establishing-shot')](('establishing-shot', 'establishing-shot').md)
- [('extreme-close-up', 'extreme-close-up')](('extreme-close-up', 'extreme-close-up').md)
