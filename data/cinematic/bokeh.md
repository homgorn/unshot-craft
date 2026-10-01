---
slug: bokeh
title: "Bokeh Prompt for AI Image & Video"
category: visual-effects
level: basic
image: "https://vvsvs.pro/img/cinematique/bokeh.webp"
source_url: https://vvsvs.pro/cinematique/bokeh
upstream_file: cinematique-catalog.json
upstream_sha256: 03443b1c573aec3c6b13c0ada9f219b7d52c54919ca6bd4374cbec84fd129853
---

Beautiful bokeh behind [Subject], hundreds of out-of-focus light sources transformed into soft luminous orbs of color, each perfectly round from the wide-open aperture of a fast 85mm lens, the distinctive creamy rendering of a Zeiss or Leica lens where the out-of-focus transition is butter-smooth, the visual magic of shallow depth of field turning the background into an impressionist painting of light

## Lede

The aesthetic quality of out-of-focus areas, particularly light sources that become soft, circular orbs — beautiful bokeh creates a dreamy, luminous background that elevates any subject. The term comes from the Japanese word for "blur," and the quality of bokeh varies dramatically between lens designs. Anamorphic lenses produce distinctive oval bokeh, seen in J.J. Abrams' "Star Trek" and Ridley Scott's "Blade Runner." Wong Kar-wai and Christopher Doyle exploit bokeh as a primary aesthetic element in "In the Mood for Love." The rise of large-sensor cameras has made cinematic bokeh accessible to independent filmmakers, and the distinctive bokeh of vintage lenses has driven a renaissance in legacy glass from Helios, Canon K35, and Cooke Speed Panchro.

## When to use

Use bokeh when the subject needs separation from a busy environment or when background lights should become emotional atmosphere rather than information. It suits portraits, romantic scenes, night streets, and intimate details. Strong bokeh depends on depth staging: the subject, lens plane, and distant lights need clear separation. Avoid it when the audience must read the location, background action, or spatial relationships in detail.

## Directing the AI

Place the subject sharply in the foreground and move practical lights well behind them. Use shallow depth of field with smooth focus falloff, turning distant points into soft circular or oval orbs without losing their color. Keep the eyes or chosen detail critically sharp. Avoid cutting bokeh shapes through the subject's silhouette. Build varied orb sizes from multiple distances and retain a few recognizable environmental cues so the background feels optical, not abstract decoration.

## Common mistakes

- Blurring the subject along with the background, leaving no stable focal plane for the viewer.
- Filling every empty area with identical glowing circles, which reads as an overlay rather than optical depth.
- Using bokeh when background geography matters, hiding information the audience needs to understand the scene.

## Sources

- Inventing Worlds and Characters: Effects

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

- [shallow-focus](shallow-focus.md)
- [depth-of-field](depth-of-field.md)
- [lens-distortion](lens-distortion.md)
- [color-grading](color-grading.md)
- [desaturation](desaturation.md)
- [sepia-tone](sepia-tone.md)
- [film-grain](film-grain.md)
- [forced-perspective](forced-perspective.md)
- [morphing](morphing.md)

