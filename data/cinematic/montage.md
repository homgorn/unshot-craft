---
slug: montage
title: "Montage Prompt for AI Image & Video"
category: editing
level: basic
image: "https://vvsvs.pro/img/cinematique/montage.webp"
source_url: https://vvsvs.pro/cinematique/montage
upstream_file: cinematique-catalog.json
upstream_sha256: 03443b1c573aec3c6b13c0ada9f219b7d52c54919ca6bd4374cbec84fd129853
styles: [beat-cut-moves]
---

Montage sequence compressing time around [Subject], each shot shorter than the last as momentum accelerates, the editing rhythm itself building like a crescendo, culminating in a final sustained shot of completion, the cinematic time machine that compresses months into two minutes of escalating visual rhythm

## Lede

A sequence of short shots edited together to compress time, convey information, or build emotional momentum — from training sequences to falling-in-love sequences, montage is cinema's time machine. Sergei Eisenstein theorized montage as cinema's unique art form in the 1920s, and his Odessa Steps sequence in "Battleship Potemkin" remains the most studied montage in film history. Rocky Balboa's training montage set to "Gonna Fly Now" defined the modern montage for a generation. Martin Scorsese uses montage in "Goodfellas" to compress years of criminal excess into exhilarating minutes, and Edgar Wright creates kinetic comic montages in the Cornetto trilogy.

## When to use

Montage is built for change that matters but does not need to unfold in real time. Use it for training, travel, construction, research, falling in love, decline, or any process with visible milestones. Each shot should advance the state, not repeat the same information. Rhythm can accelerate toward completion or slow at setbacks. The sequence needs a clear beginning condition, meaningful progression, and a final image that proves what changed.

## Directing the AI

Define the process and list a sequence of distinct visual milestones. Start with longer shots that establish the task, then tighten duration as competence, urgency, or accumulation grows. Use repeated actions, matched framing, or recurring objects to show measurable change. Vary shot scale while preserving subject and environment continuity. Build toward one sustained payoff image rather than stopping randomly. Let music or action rhythm guide cuts, but ensure every beat remains legible without sound.

## Common mistakes

- Repeating attractive shots that show no new milestone, making the sequence energetic but narratively static.
- Accelerating cuts before the process is established, so the audience cannot understand what activity or change is being compressed.
- Ending on another brief fragment instead of a clear payoff that confirms completion, failure, or transformation.

## Sources

- What Is Film Editing?

## Cross-tool

| tool | params | version | tested |
|---|---|---|---|
| mj61 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| runway_gen3 | `motion_brush: smooth_pan \| aspect_ratio: 16:9 \| duration: 5 \| resolution: 1080p` | gen-3-alpha | no |
| veo2 | `resolution: 1080p \| aspect_ratio: 16:9 \| duration: 5 \| cinematic_style: true` | veo-2 | no |
| kling15 | `camera_motion: pan_right \| resolution: 1080p \| duration: 5 \| style: cinematic` | kling-1.5 | no |
| luma | `aspect_ratio: 16_9 \| duration: 5 \| resolution: 1080p \| style: cinematic` | dream-machine | no |
| pika15 | `aspect_ratio: 16:9 \| style: cinematic \| duration: 5 \| motion: smooth_pan` | pika-1.5 | no |
| sora | `style: cinematic \| resolution: 1080p \| aspect_ratio: 16:9 \| duration: 5 \| motion: smooth_pan` | sora-1 | no |

## Related

- [cross-cutting](cross-cutting.md)
- [time-lapse](time-lapse.md)
- [fast-motion](fast-motion.md)
- [jump-cut](jump-cut.md)
- [dissolve](dissolve.md)
- [fade-in-out](fade-in-out.md)
- [smash-cut](smash-cut.md)
- [long-take](long-take.md)
- [freeze-frame](freeze-frame.md)

