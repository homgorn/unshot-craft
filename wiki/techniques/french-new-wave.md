# "French New Wave Prompt for AI Image & Video"

`french-new-wave` · Film Genres · level intermediate

No reference video for this technique.

## Prompt (verbatim, `[Subject]` intact)

```
French New Wave scene with [Subject] shot handheld on what appears to be stolen moments, the camera following with improvisational looseness, harsh midday sun creating unflattering but honest illumination, the composition casual rather than composed, the visual rebellion against studio perfection, high-contrast black and white on grainy 16mm stock, the Raoul Coutard handheld aesthetic
```

A 1960s movement that broke every rule — jump cuts, handheld cameras, location shooting, fourth-wall breaks, and a rebellious rejection of polished studio filmmaking, treating cinema as conversation. Jean-Luc Godard's "Breathless" (1960) and François Truffaut's "The 400 Blows" (1959) launched the movement, joined by Agnès Varda, Jacques Rivette, Eric Rohmer, and Claude Chabrol. Cinematographer Raoul Coutard defined the visual style — handheld 16mm, natural light, real Parisian locations. The movement's influence is incalculable: Scorsese, Tarantino, Wes Anderson, Sofia Coppola, and Noah Baumb…

**When to use.** Use French New Wave style when the film should feel youthful, immediate, self-aware, and resistant to studio polish. It suits street romance, restless conversation, playful crime, and characters who seem to invent the movie as they live it. The style can combine handheld location work, jump cuts, direct address, and rough natural light. Choose rule-breaking that expresses attitude rather than col…

**Directing the AI.** Shoot on real streets in hard midday light with grainy high-contrast black and white or restrained natural color. Follow the subject handheld with loose reframing, occasional focus correction, and casual composition. Let jump cuts remove pieces of continuous action while preserving its emotional line. Permit a glance into lens or an abrupt pan when character energy demands it. Keep location sound and uncontrolled background life visible; the city should feel captured, not dressed.

**Common mistakes.**
- Combining every New Wave device in each shot, turning rebellion into a rigid checklist of effects.
- Using polished studio light and locked framing while relying on wardrobe alone to suggest the movement.
- Cutting continuity randomly, without preserving the character impulse that makes rough editing feel alive.

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
| declared | `shot-transitions` | transition | — | `black-card-transition` |
| declared | `shot-transitions` | transition | — | `dark-tunnel-transition` |
| declared | `shot-transitions` | transition | — | `focus-handoff-transition` |
| declared | `shot-transitions` | transition | — | `mask-wipe-real` |
| declared | `shot-transitions` | transition | — | `portal-wipe-v2` |
| declared | `shot-transitions` | transition | — | `whip-brake-real` |
| declared | `shot-transitions` | transition | — | `whip-pan-real` |

```
python platform/query.py technique-motions french-new-wave
```

## Sources

- Genres: Where to Draw the Line?

## Related techniques

- [('jump-cut', 'jump-cut')](('jump-cut', 'jump-cut').md)
- [('handheld-shot', 'handheld-shot')](('handheld-shot', 'handheld-shot').md)
- [('breaking-fourth-wall', 'breaking-fourth-wall')](('breaking-fourth-wall', 'breaking-fourth-wall').md)
- [('film-noir', 'film-noir')](('film-noir', 'film-noir').md)
- [('german-expressionism', 'german-expressionism')](('german-expressionism', 'german-expressionism').md)
- [('cinema-verite', 'cinema-verite')](('cinema-verite', 'cinema-verite').md)
- [('surrealism', 'surrealism')](('surrealism', 'surrealism').md)
- [('found-footage', 'found-footage')](('found-footage', 'found-footage').md)
- [('spaghetti-western', 'spaghetti-western')](('spaghetti-western', 'spaghetti-western').md)
