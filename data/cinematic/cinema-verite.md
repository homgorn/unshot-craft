---
slug: cinema-verite
title: "Cinéma Vérité Prompt for AI Image & Video"
category: genres
level: intermediate
image: "https://vvsvs.pro/img/cinematique/cinema-verite.webp"
source_url: https://vvsvs.pro/cinematique/cinema-verite
upstream_file: cinematique-catalog.json
upstream_sha256: 03443b1c573aec3c6b13c0ada9f219b7d52c54919ca6bd4374cbec84fd129853
styles: [graze-face-tour]
---

Cinema verite documentary moment with [Subject], handheld camera following the action, natural available light providing uncontrolled illumination, the framing imperfect and reactive, occasional focus hunting, the raw audio of the environment, the entire aesthetic committed to the principle that imperfection is authenticity, Super 16mm film grain, the Jean Rouch principle that the camera's presence provokes truth

## Lede

A documentary approach using handheld cameras, natural lighting, and unscripted moments to capture truth — the camera is acknowledged as present, truth provoked rather than merely observed. Jean Rouch and Edgar Morin coined the term with "Chronicle of a Summer" (1961), where the filmmakers actively engage with their subjects. The American equivalent, "direct cinema" (Frederick Wiseman, the Maysles Brothers), takes a more observational approach. The Dardenne Brothers' fiction films apply cinéma vérité techniques to narrative cinema. Paul Greengrass brings cinéma vérité energy to mainstream thrillers like "United 93" and the "Bourne" trilogy, making Hollywood action feel like documentary.

## When to use

Use cinéma vérité when truth should emerge through interaction rather than polished observation. It suits interviews in motion, social encounters, street scenes, political situations, and fiction that needs documentary pressure. Let the camera's presence affect behavior instead of pretending it is invisible. The style requires responsive imperfections tied to unfolding action; random shake, damaged sound, or poor exposure without human consequence only imitates low production quality.

## Directing the AI

Follow the subject with a handheld camera at human distance, reacting late to gestures and occasionally correcting framing or focus. Use only available light, allowing mixed color and uneven exposure where the location creates it. Keep ambient sound, interruptions, and glances toward the camera. Let the operator shift position when events change rather than anticipating every move. Preserve faces and essential action; authenticity comes from responsive observation, not from making the footage unreadable.

## Common mistakes

- Adding constant violent shake, which feels performed and prevents the audience from observing actual behavior.
- Polishing every composition and focus pull, removing the reactive uncertainty that gives the approach its tension.
- Treating technical damage as authenticity while subjects remain posed, scripted, and untouched by the camera.

## Sources

- Genres: Where to Draw the Line?

## Cross-tool

| tool | params | version | tested |
|---|---|---|---|
| mj61 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| runway_gen3 | `motion_brush: smooth_slow_pan \| aspect_ratio: 16:9 \| duration: 5 \| resolution: 1080p` | gen-3-alpha | no |
| veo2 | `resolution: 1080p \| aspect_ratio: 16:9 \| duration: 5 \| cinematic_style: true` | veo-2 | no |
| kling15 | `camera_motion: slow_pan \| resolution: 1080p \| duration: 5 \| style: cinematic` | kling-1.5 | no |
| luma | `aspect_ratio: 16_9 \| duration: 5 \| resolution: 1080p \| style: cinematic` | dream-machine | no |
| pika15 | `aspect_ratio: 16:9 \| style: cinematic \| duration: 5 \| motion: slow_pan` | pika-1.5 | no |
| sora | `style: cinematic \| resolution: 1080p \| aspect_ratio: 16:9 \| duration: 5 \| motion: slow_pan` | sora-1 | no |

## Related

- [handheld-shot](handheld-shot.md)
- [available-light](available-light.md)
- [found-footage](found-footage.md)
- [film-noir](film-noir.md)
- [german-expressionism](german-expressionism.md)
- [french-new-wave](french-new-wave.md)
- [surrealism](surrealism.md)
- [spaghetti-western](spaghetti-western.md)
- [italian-neorealism](italian-neorealism.md)

