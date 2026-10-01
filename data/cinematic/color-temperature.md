---
slug: color-temperature
title: "Color Temperature Prompt for AI Image & Video"
category: lighting
level: intermediate
image: "https://vvsvs.pro/img/cinematique/color-temperature.webp"
source_url: https://vvsvs.pro/cinematique/color-temperature
upstream_file: cinematique-catalog.json
upstream_sha256: 03443b1c573aec3c6b13c0ada9f219b7d52c54919ca6bd4374cbec84fd129853
styles: [letterspace-materialize]
---

Mixed color temperatures on [Subject], the tension between warm 2700K tungsten sources casting golden light and cool 6500K daylight-balanced sources washing in cold sterile tones, the two color worlds meeting on the subject's form, shot on Kodak Vision3 500T balanced for tungsten so warm sources read neutral while daylight goes intensely blue, the visual poetry of mixed color temperatures that maps emotional geography

## Lede

The warmth or coolness of light measured in Kelvin — warm light (orange/amber) suggests comfort and intimacy while cool light (blue) suggests detachment, technology, or night. Steven Soderbergh is a master of deliberate color temperature manipulation, using amber for Mexico and blue-green for the US in "Traffic" to distinguish storylines. Emmanuel Lubezki plays warm and cool temperatures against each other in nearly every frame of "The Revenant." The contrast between warm practicals and cool ambient light is a fundamental tool of modern cinematography, used by Hoyte van Hoytema in "Interstellar" and Bradford Young in "Solo: A Star Wars Story."

## When to use

Work with color temperature when emotional geography matters as much as brightness. Warm practicals can hold comfort, memory, or intimacy while cool ambient light suggests night, distance, or technology. Mixed temperatures are useful in doorways, vehicles, city interiors, and scenes where two worlds meet on one subject. Establish the narrative role of each source first; otherwise amber and blue become an automatic cinematic palette with no connection to place or feeling.

## Directing the AI

Define at least two sources by position and color character: a warm tungsten-like lamp near the subject and cooler daylight or night ambience entering from elsewhere. State which side of the face, costume, and environment each one affects. Keep a visible transition between the color zones rather than washing the frame evenly. Neutral objects should reveal the contrast clearly. For video, maintain stable color logic as the camera turns and let subjects cross naturally between warm and cool pools.

## Common mistakes

- Applying orange to skin and teal to every background by habit, without assigning either color to a real source.
- Blending warm and cool illumination into a uniform neutral wash, eliminating the emotional separation between the two zones.
- Changing color direction across adjacent shots, so the same window or lamp appears to migrate around the scene.

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

- [color-grading](color-grading.md)
- [cross-lighting](cross-lighting.md)
- [practical-lighting](practical-lighting.md)
- [three-point-lighting](three-point-lighting.md)
- [key-light](key-light.md)
- [high-key-lighting](high-key-lighting.md)
- [low-key-lighting](low-key-lighting.md)
- [chiaroscuro](chiaroscuro.md)
- [rembrandt-lighting](rembrandt-lighting.md)

