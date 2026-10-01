---
slug: uplighting
title: "Uplighting Prompt for AI Image & Video"
category: lighting
level: basic
image: "https://vvsvs.pro/img/cinematique/uplighting.webp"
source_url: https://vvsvs.pro/cinematique/uplighting
upstream_file: cinematique-catalog.json
upstream_sha256: 03443b1c573aec3c6b13c0ada9f219b7d52c54919ca6bd4374cbec84fd129853
styles: [fracture]
---

Uplighting from below illuminating [Subject], the unnatural upward-casting light reversing every shadow humans instinctively expect, shadows falling upward from the brow ridge creating deep black pools where the eyes should be, orange flickering firelight causing the shadows to dance, shot on a 50mm lens with the warm 2000K color temperature of open flame, the deep biological wrongness of light coming from below

## Lede

Light cast upward from below the subject, unnatural to human experience, creating eerie, sinister, or supernatural effects — the classic "flashlight under the chin" horror look. James Whale used uplighting to terrifying effect in "Frankenstein" (1931) and "Bride of Frankenstein," casting Boris Karloff's face into monstrous relief. F.W. Murnau's "Nosferatu" employed underlighting to transform Max Schreck into a figure of pure dread. Modern horror directors like Ari Aster use subtle uplighting in "Hereditary" during the séance sequences, and Jordan Peele employs it in "Us" when the tethered versions of characters emerge from below.

## When to use

Use uplighting when illumination should feel instinctively wrong. A source below the face reverses familiar shadow patterns, turning ordinary features sinister, supernatural, theatrical, or childishly spooky. It works for horror, séances, firelit threats, and characters emerging from beneath a space. Keep the motivation visible or plausible. Constant underlighting outside those contexts can feel campy and flatten the scene into a single genre signal.

## Directing the AI

Place the main source below the subject's chin or beneath the frame and angle it upward. Shadows should climb from brow, nose, and cheekbones, with eye sockets becoming dark pools above the lit planes. Use warm flickering firelight around 2000K when a flame motivates the effect, or a colder source for unnatural dread. Keep overhead fill minimal so normal shadow direction does not return. In video, vary flicker subtly without changing source position.

## Common mistakes

- Adding a stronger overhead key, which restores conventional facial shadows and cancels the unsettling reversal.
- Lighting the face evenly from below, missing the deep upward-cast shadows that make the setup biologically strange.
- Using uplighting in a neutral dialogue scene without motivation, making the visual tone feel accidentally theatrical.

## Sources

- Film Lighting

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

- [german-expressionism](german-expressionism.md)
- [hard-light](hard-light.md)
- [low-key-lighting](low-key-lighting.md)
- [three-point-lighting](three-point-lighting.md)
- [key-light](key-light.md)
- [high-key-lighting](high-key-lighting.md)
- [chiaroscuro](chiaroscuro.md)
- [rembrandt-lighting](rembrandt-lighting.md)
- [silhouette](silhouette.md)

