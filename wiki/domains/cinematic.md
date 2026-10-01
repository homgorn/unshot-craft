# Cinematic techniques

A second corpus: **150 techniques** that answer *what to shoot*, complementing the 157 shot cards that answer *how it moves*. Same DB, same join keys, same generated-from-the-DB rule (ADR 0007).

| stage | corpus | answers |
|---|---|---|
| 1 | `data/cinematic/` | **what to shoot** — camera, light, composition, editing rhythm, genre |
| 2 | `references/shots/` | **how it moves** — easing, spring, timing, render duration |
| 3 | Remotion | motion execution and render |

## Two rules that are not stylistic

1. **`[Subject]` is a slot and is never expanded.** The prompts below are verbatim. An expanded prompt reads exactly like an authored one, and an agent handed it will paste it to a client as though the studio wrote it.
2. **An absent cross-tool cell is `null`, never a default.** Of 1050 listed cells, 791 carry a parameter, 0 have actually been run against the model version, and 259 are empty because nobody has tested them. A plausible string in an untested cell is a claim we cannot defend to a client.

**233 declared motion pairings across 142 of the 150 techniques.** Declared, never inferred: they come from an explicit `styles:` list in `data/cinematic/<slug>.md`, authored in `platform/catalog/pairings.py`. A technique with no entry returns an empty list and says so, because a wrong pairing hands a client a duration and an easing and looks researched.

`data/cinematic/` is **source**, not generated: authored, committed, reviewed in a diff. See `data/cinematic/README.md`. Reference stills are linked; 41/150 techniques have a reference video.

## Camera Work  (`camera-work`, 41)

| technique | level | motions | tested tools | prompt |
|---|---|---|---|---|
| [360-degree-shot](#360-degree-shot) | advanced | 1 | none | 360-degree orbiting shot circling [Subject], the camera revolving slowly as the backgroun… |
| [aerial-shot](#aerial-shot) | intermediate | 3 | none | Sweeping aerial shot of [Subject] seen from 300 feet above, captured at golden hour with… |
| [birds-eye-view](#birds-eye-view) | intermediate | 2 | none | Bird's eye view looking straight down on [Subject], the camera positioned directly overhe… |
| [choker-shot](#choker-shot) | intermediate | 1 | none | Choker shot framing [Subject] from hairline to chin with zero background visible, the ski… |
| [close-up](#close-up) | basic | 1 | none | Tight close-up of [Subject] filling the entire frame, every pore and texture rendered in… |
| [cowboy-shot](#cowboy-shot) | basic | 1 | none | Cowboy shot of [Subject] framed from mid-thigh up, hands hanging loose at their sides, th… |
| [crane-shot](#crane-shot) | advanced | 1 | none | Crane shot beginning tight on [Subject] then sweeping upward and backward in a majestic a… |
| [crash-zoom](#crash-zoom) | intermediate | 2 | none | Crash zoom snapping from a wide shot to an extreme close-up of [Subject] in half a second… |
| [dolly-shot](#dolly-shot) | intermediate | 6 | none | Smooth dolly shot gliding toward [Subject], the camera at eye level moving with buttery p… |
| [dutch-angle](#dutch-angle) | basic | 2 | none | [Subject] framed at a sharp 25-degree Dutch angle, vertical lines tilting diagonally acro… |
| [establishing-shot](#establishing-shot) | basic | 4 | none | Wide establishing shot of [Subject] at blue hour, deep indigo sky with the last traces of… |
| [extreme-close-up](#extreme-close-up) | basic | 1 | none | Extreme macro close-up of [Subject] filling the entire frame, every microscopic detail re… |
| [extreme-long-shot](#extreme-long-shot) | basic | 2 | none | Extreme long shot of [Subject] barely visible against a vast landscape stretching to the… |
| [eye-level-shot](#eye-level-shot) | basic | 1 | none | Eye-level shot of [Subject] with the camera positioned exactly at their eye height creati… |
| [handheld-shot](#handheld-shot) | basic | 1 | none | Handheld camera following [Subject], natural shake and breathing motion in the frame, mot… |
| [head-on-shot](#head-on-shot) | intermediate | 1 | none | Head-on shot of [Subject] moving directly toward the camera with perfect bilateral symmet… |
| [high-angle-shot](#high-angle-shot) | basic | 2 | none | High angle shot looking down on [Subject], the perspective making them appear impossibly… |
| [insert-shot](#insert-shot) | basic | 2 | none | Insert shot of [Subject] isolated in tight framing, warm lamplight casting a golden glow… |
| [long-shot](#long-shot) | basic | 2 | none | Long shot of [Subject] with the full figure visible from head to foot, the scale of the e… |
| [low-angle-shot](#low-angle-shot) | basic | 1 | none | Low angle shot looking up at [Subject] from below, the camera positioned at ground level… |
| [master-shot](#master-shot) | intermediate | 2 | none | Wide master shot of [Subject] with all elements visible simultaneously, every figure prec… |
| [medium-close-up](#medium-close-up) | basic | 1 | none | Medium close-up of [Subject] from the chest up, the intimate distance perfect for reading… |
| [medium-shot](#medium-shot) | basic | 3 | none | Medium shot of [Subject] framed from the waist up, the perfect conversational distance th… |
| [one-er](#one-er) | advanced | 1 | none | Long unbroken single take following [Subject] through shifting environments, the entire j… |
| [over-the-shoulder](#over-the-shoulder) | basic | 2 | none | Over-the-shoulder shot with the near figure's shoulder and jaw soft and dark in the foreg… |
| [overhead-shot](#overhead-shot) | intermediate | 2 | none | Overhead shot looking straight down on [Subject], the flat geometric arrangement rendered… |
| [pan-shot](#pan-shot) | basic | 2 | none | Slow panoramic pan revealing [Subject], the camera rotating smoothly on a fluid head, the… |
| [pov-shot](#pov-shot) | intermediate | 1 | none | First-person POV shot through the eyes of [Subject], shallow depth of field mimicking unf… |
| [pull-out](#pull-out) | intermediate | 2 | none | Pull-out shot beginning tight on [Subject] then slowly withdrawing to reveal the true sca… |
| [push-in](#push-in) | intermediate | 4 | none | Imperceptibly slow push-in toward [Subject], the camera beginning in a medium shot and gr… |
| [rack-focus](#rack-focus) | intermediate | 2 | none | Rack focus shot with [Subject] transitioning between sharp foreground detail and resolved… |
| [slow-motion](#slow-motion) | basic | 3 | none | Slow motion capture at 240fps of [Subject] suspended in a single stretched moment, dust p… |
| [static-shot](#static-shot) | basic | 1 | none | Perfectly static locked-off shot of [Subject], the camera absolutely motionless on a heav… |
| [steadicam](#steadicam) | advanced | 1 | none | Steadicam tracking shot floating smoothly behind [Subject] through shifting environments,… |
| [three-shot](#three-shot) | intermediate | 2 | none | Three-shot of [Subject] arranged in a triangular composition across the widescreen frame,… |
| [tilt-shot](#tilt-shot) | basic | 1 | none | Slow tilt shot beginning at the feet of [Subject] and climbing vertically up their body,… |
| [tracking-shot](#tracking-shot) | intermediate | 3 | none | Lateral tracking shot following [Subject] at shoulder height, the camera keeping perfect… |
| [two-shot](#two-shot) | basic | 2 | none | Two-shot of [Subject] framed together, their bodies creating complementary angles, the sp… |
| [vertigo-effect](#vertigo-effect) | advanced | 3 | none | Vertigo effect dolly zoom on [Subject] locked in frame while the background warps and tel… |
| [whip-pan](#whip-pan) | intermediate | 4 | none | Whip pan snapping to [Subject], heavy horizontal motion blur streaking the environment in… |
| [worms-eye-view](#worms-eye-view) | intermediate | 1 | none | Worm's eye view from ground level looking straight up at [Subject], the perspective so ex… |

## Lighting  (`lighting`, 30)

| technique | level | motions | tested tools | prompt |
|---|---|---|---|---|
| [ambient-light](#ambient-light) | basic | 1 | none | Ambient light only on [Subject], the existing institutional or natural illumination provi… |
| [available-light](#available-light) | intermediate | 1 | none | Available light on [Subject] with no additional movie lighting, illuminated purely by exi… |
| [backlight](#backlight) | basic | 1 | none | Backlit [Subject] with brilliant rim of white-gold light tracing every contour, hair tran… |
| [blue-hour](#blue-hour) | intermediate | 1 | none | Blue hour twilight twenty minutes after sunset enveloping [Subject], the sky a luminous d… |
| [bounce-light](#bounce-light) | intermediate | 1 | none | Bounce light wrapping gently around [Subject], light reflected off a nearby surface creat… |
| [broad-lighting](#broad-lighting) | basic | 1 | none | Broad lighting on [Subject] with the key illuminating the wider camera-facing side, creat… |
| [chiaroscuro](#chiaroscuro) | advanced | 1 | none | Chiaroscuro lighting on [Subject] with a single candle or flame as the only source, warm… |
| [color-temperature](#color-temperature) | intermediate | 1 | none | Mixed color temperatures on [Subject], the tension between warm 2700K tungsten sources ca… |
| [cross-lighting](#cross-lighting) | intermediate | 1 | none | Cross-lighting from two opposing sources on [Subject], a warm tungsten source from one si… |
| [dappled-light](#dappled-light) | intermediate | 1 | none | Dappled light filtering through a canopy onto [Subject], dozens of small bright spots and… |
| [edge-light](#edge-light) | intermediate | 1 | none | Edge light tracing the complete outline of [Subject] against darkness, a thin bright line… |
| [eye-light](#eye-light) | intermediate | 1 | none | Eye light close-up of [Subject] with brilliant catchlights sparkling in the irises, a ded… |
| [fill-light](#fill-light) | basic | 1 | none | Fill light softening the shadows on [Subject], a gentle secondary source creating a 4:1 c… |
| [gobo-lighting](#gobo-lighting) | advanced | 1 | none | Gobo lighting casting patterned shadows across [Subject], horizontal bars of light and da… |
| [golden-hour](#golden-hour) | basic | 1 | none | Golden hour light thirty minutes before sunset bathing [Subject] in warm amber backlight,… |
| [hard-light](#hard-light) | basic | 1 | none | Hard light from a bare overhead source casting razor-sharp shadows on [Subject], defined… |
| [high-key-lighting](#high-key-lighting) | basic | 1 | none | High-key lighting flooding [Subject] in bright even illumination with barely a shadow to… |
| [key-light](#key-light) | basic | 1 | none | Strong directional key light from a single source illuminating [Subject], the light carvi… |
| [kicker-light](#kicker-light) | intermediate | 1 | none | Kicker light accent on [Subject], a focused beam from behind and to the side catching jus… |
| [lens-flare](#lens-flare) | basic | 1 | none | Dramatic lens flare across [Subject], horizontal anamorphic flare streaks in cyan and mag… |
| [low-key-lighting](#low-key-lighting) | intermediate | 2 | none | Low-key lighting on [Subject] with deep impenetrable shadows claiming eighty percent of t… |
| [motivated-lighting](#motivated-lighting) | intermediate | 1 | none | Motivated lighting on [Subject] with every light source logically justified within the sc… |
| [practical-lighting](#practical-lighting) | intermediate | 1 | none | Practical lighting on [Subject] illuminated only by visible sources within the frame, eac… |
| [rembrandt-lighting](#rembrandt-lighting) | intermediate | 1 | none | Rembrandt lighting portrait of [Subject], the key light positioned high and at 45 degrees… |
| [short-lighting](#short-lighting) | intermediate | 1 | none | Short lighting on [Subject] with the key hitting the narrow far side, putting the broader… |
| [side-lighting](#side-lighting) | intermediate | 1 | none | Side lighting from a single source striking [Subject] at exactly 90 degrees, one half bri… |
| [silhouette](#silhouette) | basic | 1 | none | [Subject] reduced to a pure dark silhouette against an intensely bright backlight source,… |
| [soft-light](#soft-light) | basic | 1 | none | Soft diffused light wrapping around [Subject] with barely perceptible shadow transitions,… |
| [three-point-lighting](#three-point-lighting) | basic | 1 | none | Classic three-point lighting on [Subject], the key light at 45 degrees creating defined s… |
| [uplighting](#uplighting) | basic | 1 | none | Uplighting from below illuminating [Subject], the unnatural upward-casting light reversin… |

## Composition  (`composition`, 21)

| technique | level | motions | tested tools | prompt |
|---|---|---|---|---|
| [balancing-elements](#balancing-elements) | intermediate | 2 | none | Balanced composition with [Subject] on one third of the frame counterweighted by a visual… |
| [centered-composition](#centered-composition) | basic | 1 | none | Centered composition with [Subject] at the exact mathematical center, the space arranged… |
| [contrast-composition](#contrast-composition) | basic | 1 | none | High contrast composition with [Subject] as a tiny warm-colored element against a vast co… |
| [deep-focus](#deep-focus) | intermediate | 2 | none | Deep focus composition with [Subject] visible across multiple planes simultaneously, all… |
| [depth-of-field](#depth-of-field) | basic | 2 | none | Selective depth of field isolating [Subject] in a narrow focused slice, everything in fro… |
| [diagonal-lines](#diagonal-lines) | basic | 1 | none | Diagonal line composition with [Subject] surrounded by aggressive 45-degree angles, nothi… |
| [figure-ground](#figure-ground) | intermediate | 1 | none | Strong figure-ground relationship with [Subject] separated from the background by extreme… |
| [foreground-interest](#foreground-interest) | intermediate | 2 | none | Foreground interest composition with [Subject] in the mid-ground and blurred elements dom… |
| [framing-within-frame](#framing-within-frame) | intermediate | 1 | none | Frame within a frame with [Subject] seen through a dark silhouette of an architectural op… |
| [golden-ratio](#golden-ratio) | advanced | 1 | none | Golden ratio spiral composition with [Subject] placed along the logarithmic curve, every… |
| [headroom](#headroom) | basic | 1 | none | Proper headroom in a medium close-up of [Subject], eyes positioned along the upper-third… |
| [lead-room](#lead-room) | basic | 2 | none | Lead room composition with [Subject] positioned on one side of the frame with generous em… |
| [leading-lines](#leading-lines) | basic | 2 | none | Leading lines composition converging toward [Subject] at a distant vanishing point, every… |
| [mise-en-scene](#mise-en-scene) | advanced | 2 | none | Meticulously arranged mise-en-scene with [Subject] positioned within an environment where… |
| [negative-space](#negative-space) | intermediate | 2 | none | Negative space composition with [Subject] occupying the extreme lower corner of the frame… |
| [repetition-and-pattern](#repetition-and-pattern) | intermediate | 1 | none | Repetition and pattern composition with [Subject] as the single disruption in an otherwis… |
| [rule-of-thirds](#rule-of-thirds) | basic | 3 | none | Rule of thirds composition with [Subject] positioned at the upper-right power point inter… |
| [shallow-focus](#shallow-focus) | basic | 2 | none | Shallow focus portrait of [Subject] with only the face in razor-sharp focus while everyth… |
| [symmetry](#symmetry) | basic | 1 | none | Perfect bilateral symmetry with [Subject] standing at the exact center of the vanishing p… |
| [triangular-composition](#triangular-composition) | intermediate | 1 | none | Triangular composition with [Subject] arranged to form a triangle within the frame, the a… |
| [visual-weight](#visual-weight) | intermediate | 1 | none | Visual weight study with [Subject] as a small but vivid element carrying visual mass disp… |

## Editing  (`editing`, 17)

| technique | level | motions | tested tools | prompt |
|---|---|---|---|---|
| [cross-cutting](#cross-cutting) | intermediate | 2 | none | Cross-cutting between two simultaneous scenes involving [Subject], the alternation betwee… |
| [cut-in](#cut-in) | basic | 1 | none | Cut-in to a tight close-up of [Subject] revealing a telling detail, shot on a 100mm macro… |
| [cutaway](#cutaway) | basic | 1 | none | Cutaway to [Subject] isolated in tight framing, the mundane object suddenly loaded with m… |
| [dissolve](#dissolve) | basic | 7 | none | Dissolve transition with two overlapping images of [Subject], both simultaneously visible… |
| [fade-in-out](#fade-in-out) | basic | 1 | none | Fade to black from [Subject], the image gradually losing luminance over six seconds as th… |
| [fast-motion](#fast-motion) | basic | 2 | none | Fast motion sequence of [Subject] accelerated to four times normal speed, the slight jerk… |
| [freeze-frame](#freeze-frame) | basic | 3 | none | Freeze frame of [Subject] caught at the precise instant of peak emotional or physical exp… |
| [iris-transition](#iris-transition) | basic | 1 | none | Iris transition closing concentrically around [Subject] at center frame, the circular bla… |
| [jump-cut](#jump-cut) | basic | 2 | none | Jump cut sequence of [Subject] with the background and position shifting abruptly between… |
| [long-take](#long-take) | advanced | 1 | none | Long unbroken take following [Subject] in real time through continuous space, the single… |
| [montage](#montage) | basic | 2 | none | Montage sequence compressing time around [Subject], each shot shorter than the last as mo… |
| [reaction-shot](#reaction-shot) | basic | 2 | none | Reaction shot close-up of [Subject] capturing the exact moment of emotional impact, the e… |
| [reverse-motion](#reverse-motion) | basic | 2 | none | Reverse motion of [Subject] with the uncanny wrongness of reversed physics where entropy… |
| [smash-cut](#smash-cut) | basic | 2 | none | Smash cut from absolute serenity to total chaos involving [Subject], an instantaneous har… |
| [split-screen](#split-screen) | intermediate | 1 | none | Split screen dividing the frame with [Subject] visible in both halves simultaneously, one… |
| [time-lapse](#time-lapse) | intermediate | 2 | none | Time-lapse of [Subject] compressed from hours into seconds, light cycling through the ful… |
| [wipe-transition](#wipe-transition) | basic | 1 | none | Wipe transition with [Subject] in one scene being pushed off frame by an incoming scene s… |

## Narrative  (`narrative`, 12)

| technique | level | motions | tested tools | prompt |
|---|---|---|---|---|
| [breaking-fourth-wall](#breaking-fourth-wall) | intermediate | 1 | none | [Subject] suddenly turning to look directly into the camera lens with a knowing expressio… |
| [cliffhanger](#cliffhanger) | basic | 3 | none | Cliffhanger moment frozen at peak suspense with [Subject], the image capturing the exact… |
| [flashback](#flashback) | basic | 7 | none | Flashback scene with [Subject] rendered in slightly overexposed warm-shifted tones, the i… |
| [flashforward](#flashforward) | intermediate | 7 | none | Flashforward showing [Subject] in a future state, the visual treatment cooler and more de… |
| [foreshadowing](#foreshadowing) | intermediate | 1 | none | Foreshadowing detail hiding in plain sight around [Subject], a seemingly ordinary detail… |
| [frame-narrative](#frame-narrative) | intermediate | 1 | none | Frame narrative with [Subject] as the storyteller in warm amber lamplight, the image begi… |
| [in-medias-res](#in-medias-res) | basic | 2 | none | In medias res with [Subject] dropped without context into the middle of intense action al… |
| [motif](#motif) | intermediate | 1 | none | Recurring visual motif with [Subject] appearing for the nth time in the narrative, the vi… |
| [non-linear-narrative](#non-linear-narrative) | advanced | 1 | none | Non-linear narrative visualized with [Subject] existing simultaneously at different momen… |
| [parallel-storylines](#parallel-storylines) | advanced | 1 | none | Parallel storylines with [Subject] shown across multiple distinct visual quadrants happen… |
| [symbolism](#symbolism) | intermediate | 1 | none | Visual symbolism with [Subject] carrying abstract meaning beyond its literal form, the im… |
| [voiceover-narration](#voiceover-narration) | basic | 1 | none | Scene designed to accompany voiceover narration with [Subject] in a contemplative visual,… |

## Visual Effects & Promptable FX  (`visual-effects`, 8)

| technique | level | motions | tested tools | prompt |
|---|---|---|---|---|
| [bokeh](#bokeh) | basic | 0 | none | Beautiful bokeh behind [Subject], hundreds of out-of-focus light sources transformed into… |
| [color-grading](#color-grading) | intermediate | 0 | none | Heavily color-graded scene with [Subject] rendered in a distinct teal-and-orange compleme… |
| [desaturation](#desaturation) | basic | 0 | none | Desaturated scene with [Subject] approaching monochrome, all color drained to near-gray e… |
| [film-grain](#film-grain) | basic | 0 | none | Heavy film grain visible on [Subject], the organic random texture of high-speed 35mm film… |
| [forced-perspective](#forced-perspective) | intermediate | 0 | none | Forced perspective illusion with [Subject] appearing impossibly large or small through pr… |
| [lens-distortion](#lens-distortion) | intermediate | 0 | none | Lens distortion from a vintage anamorphic lens visible across [Subject], barrel distortio… |
| [morphing](#morphing) | advanced | 0 | none | [Subject] caught mid-transformation, the form dissolving into particles or liquid or ligh… |
| [sepia-tone](#sepia-tone) | basic | 0 | none | Sepia-toned treatment on [Subject], the warm brownish-yellow transforming the image into… |

## Film Genres  (`genres`, 21)

| technique | level | motions | tested tools | prompt |
|---|---|---|---|---|
| [acid-western](#acid-western) | advanced | 1 | none | Acid western with [Subject] in a vast surreal desert landscape, the familiar Western icon… |
| [cinema-verite](#cinema-verite) | intermediate | 1 | none | Cinema verite documentary moment with [Subject], handheld camera following the action, na… |
| [cosmic-horror](#cosmic-horror) | advanced | 1 | none | Cosmic horror atmosphere with [Subject] dwarfed by something vast and incomprehensible at… |
| [dogme-95](#dogme-95) | advanced | 1 | none | Dogme 95 aesthetic with [Subject] shot on a consumer camera with no additional lighting,… |
| [film-noir](#film-noir) | intermediate | 2 | none | Film noir aesthetic with [Subject] in high-contrast black and white, deep blacks and silv… |
| [found-footage](#found-footage) | basic | 1 | none | Found footage shot of [Subject] through a consumer-grade camera in night vision mode, the… |
| [french-new-wave](#french-new-wave) | intermediate | 7 | none | French New Wave scene with [Subject] shot handheld on what appears to be stolen moments,… |
| [german-expressionism](#german-expressionism) | advanced | 1 | none | German Expressionism with [Subject] in deliberately distorted architecture, buildings lea… |
| [giallo](#giallo) | advanced | 1 | none | Giallo-style scene with [Subject] drenched in vivid primary-color lighting, deep crimson… |
| [hyperlink-cinema](#hyperlink-cinema) | advanced | 1 | none | Hyperlink cinema visualization with [Subject] shown across multiple disconnected lives in… |
| [italian-neorealism](#italian-neorealism) | intermediate | 1 | none | Italian Neorealism with [Subject] on an actual working-class street, non-professional fac… |
| [mockumentary](#mockumentary) | basic | 1 | none | Mockumentary talking head interview with [Subject] looking slightly off-camera to an unse… |
| [mumblecore](#mumblecore) | basic | 1 | none | Mumblecore scene with [Subject] shot on what appears to be a consumer DSLR with available… |
| [noir-tech](#noir-tech) | intermediate | 2 | none | Tech noir scene with [Subject] in a rain-soaked neon-lit dystopia, the hard shadows and m… |
| [poetic-realism](#poetic-realism) | advanced | 1 | none | Poetic realism with [Subject] rendered in heartbreaking lyrical beauty, fog softening eve… |
| [slow-cinema](#slow-cinema) | advanced | 2 | none | Slow cinema with [Subject] in a single unbroken composition, the camera absolutely still… |
| [southern-gothic](#southern-gothic) | intermediate | 1 | none | Southern Gothic atmosphere with [Subject] amid crumbling architecture and encroaching nat… |
| [spaghetti-western](#spaghetti-western) | intermediate | 1 | none | Spaghetti Western standoff with [Subject], the camera alternating between extreme close-u… |
| [surrealism](#surrealism) | advanced | 1 | none | Surrealist scene with [Subject] in a world where dream logic replaces physical reality, i… |
| [vaporwave](#vaporwave) | basic | 1 | none | Vaporwave aesthetic with [Subject] bathed in neon pink and cyan gradient lighting, retro… |
| [wuxia](#wuxia) | advanced | 1 | none | Wuxia style with [Subject] in gravity-defying motion, robes and fabric trailing like call… |

## Techniques in full

### 360-degree-shot

**"360-Degree Shot Prompt for AI Image & Video"** · `camera-work` · level advanced

```
360-degree orbiting shot circling [Subject], the camera revolving slowly as the background becomes a continuous ribbon of light, the centripetal energy of the rotation making the world feel like it is spinning around the subject as its axis, shot on anamorphic 50mm with oval bokeh, warm tungsten tones on skin against cool ambient light, the romantic vertigo of circular motion
```

The camera orbits completely around the subject, creating a sense of circling energy, romantic intensity, or the feeling of time and space collapsing around a central moment. Brian De Palma used the 360-degree orbit in "Carlito's Way" as Carlito and Gail dance, the world spinning away until only they exist. The Wachowskis' "bullet time" in "The Matrix" took the orbital shot to a new technological…

**When to use.** Use a full orbit when the world should seem to spin around one emotional center. It can heighten romance, heroism, panic, reunion, or a moment when normal space falls away. The circular move also reveals every side of an environment while keeping one subject central. Reserve it for major beats; an…

**Directing the AI.** Keep the subject fixed near the axis while the camera travels through one complete, level circle around them. Maintain consistent distance, focus, and body scale as the background becomes a continuous ribbon of parallax and light. Use an anamorphic perspective with oval bokeh, warm skin, and cooler ambient surroundings. Choreograph the subject's gaze or embrace through the orbit, and define a cle…

**Common mistakes.**
- Rotating the background without changing viewpoint, which looks like a spinning plate rather than a physical camera orbit.
- Changing radius throughout the move, causing the subject to lurch in scale and weakening the central-axis effect.
- Completing several circles with no evolving action, turning emotional emphasis into repetitive visual display.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | **null** | kling-1.5 | no |
| `luma` Luma Dream Machine | **null** | dream-machine | no |
| `mj61` Midjourney v6.1 | **null** | v6.1 | no |
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | **null** | gen-3-alpha | no |
| `sora` OpenAI Sora | **null** | sora-1 | no |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `orbit-ring-title-open`, 130f

**Sources.** [50+ Types of Camera Shots, Angles, and Techniques](None)


### aerial-shot

**"Aerial Shot Prompt for AI Image & Video"** · `camera-work` · level intermediate

```
Sweeping aerial shot of [Subject] seen from 300 feet above, captured at golden hour with warm amber light painting one side of the terrain while the other falls into deep violet shadow, volumetric god rays piercing through scattered cumulus clouds, shot on ARRI Alexa 65 with Hasselblad glass, 8K resolution, Kodak Vision3 250D color science, subtle atmospheric haze layering depth into the landscape
```

A shot captured from high above the ground, typically using a drone or helicopter, providing a sweeping view of landscapes, cityscapes, or large-scale action. The aerial perspective conveys omniscience, freedom, or the terrifying scale of nature. David Lean pioneered epic aerial work in "Lawrence of Arabia," while Ridley Scott used helicopter shots to establish the grandeur of ancient Rome in "Gl…

**When to use.** Choose an aerial shot when geography matters as much as the subject. It can introduce a city, expose the geometry of a border or road network, track large-scale action, or reduce a person to a vulnerable mark inside the landscape. The height creates emotional distance, so use it for omniscience, fr…

**Directing the AI.** Place the camera roughly 300 feet above the subject and describe a broad downward view rather than a straight top-down angle. Keep a recognizable focal point inside the terrain, then build depth with foreground landforms, distant layers, atmospheric haze, and scattered clouds. Let warm golden-hour light strike one side of the landscape while deep violet shadow holds the other. For motion, specify…

**Common mistakes.**
- Setting the camera high without defining its angle, leaving the result confused between an aerial view and an overhead diagram.
- Filling every part of the landscape with equal detail, so the subject disappears without a deliberate scale relationship.
- Requesting fast drone movement when the scene needs grandeur, which turns a measured reveal into restless travel footage.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: pan_right | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: smooth_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: smooth_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `crane-rise-reveal`, 20f, `overhead-tabletop-drop` (overhead-camera-moves), 144f, `tilt-reveal` (overhead-camera-moves), 144f

**Sources.** [50+ Types of Camera Shots, Angles, and Techniques](None)


### birds-eye-view

**"Bird's Eye View Prompt for AI Image & Video"** · `camera-work` · level intermediate

```
Bird's eye view looking straight down on [Subject], the camera positioned directly overhead creating a flattened god-like perspective where depth is eliminated and everything becomes pattern and geometry, long shadows stretching from each element, shot on medium format digital with a 40mm equivalent lens, muted teal and gold color palette, forensic sharpness from edge to edge
```

A shot taken from directly overhead, looking straight down on the subject, creating a god-like perspective that can make subjects appear small and insignificant or reveal patterns invisible from ground level. Busby Berkeley pioneered the technique in 1930s musicals, choreographing dancers into kaleidoscopic geometric formations seen from directly above. Darren Aronofsky used it extensively in "Re…

**When to use.** Use a bird's eye view when the scene contains a pattern that ground-level framing would hide. Crowds, roads, bodies, tables, and architecture become readable as geometry from directly above. It also makes people appear controlled, observed, or insignificant. This angle works best when spatial desig…

**Directing the AI.** State that the camera looks straight down with its optical axis perpendicular to the ground. Remove the horizon and treat people, objects, roads, and shadows as flat graphic shapes. Arrange the main elements into a deliberate pattern with clean spacing and edge-to-edge sharpness. Use a restrained teal-and-gold palette and long directional shadows to preserve visual separation. For video, keep the…

**Common mistakes.**
- Using the phrase from above without straight-down camera language, which often produces an ordinary high-angle perspective instead.
- Building a scene with no visible pattern, making the unusual viewpoint feel decorative rather than narratively motivated.
- Adding shallow focus across the frame, which weakens the forensic clarity and flattened geometry that define the view.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | **null** | kling-1.5 | no |
| `luma` Luma Dream Machine | **null** | dream-machine | no |
| `mj61` Midjourney v6.1 | **null** | v6.1 | no |
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | **null** | gen-3-alpha | no |
| `sora` OpenAI Sora | **null** | sora-1 | no |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `overhead-tabletop-drop` (overhead-camera-moves), 144f, `tilt-reveal` (overhead-camera-moves), 144f

**Sources.** [50+ Types of Camera Shots, Angles, and Techniques](None)


### choker-shot

**"Choker Shot Prompt for AI Image & Video"** · `camera-work` · level intermediate

```
Choker shot framing [Subject] from hairline to chin with zero background visible, the skin filling the entire screen like a landscape, harsh toplight creating deep shadow in the eye sockets while illuminating the planes of cheekbone and brow, shot on a 100mm macro lens at T2.8, high-contrast monochromatic color treatment, Bergman-level psychological claustrophobia
```

A very tight shot framing the face from forehead to chin, eliminating nearly all background, more claustrophobic than a standard close-up and often used for moments of extreme emotion. Ingmar Bergman used the choker shot relentlessly in "Persona" and "Cries and Whispers," trapping his actors' faces in frames that feel like emotional prisons. Darren Aronofsky adopted this approach in "Black Swan,"…

**When to use.** Use a choker shot when a face must become a confined emotional space. Framing from forehead to chin removes almost all context and lets tiny shifts in eyes, mouth, and skin tension feel enormous. It suits panic, shame, obsession, confrontation, and sustained discomfort. Because the closeness is agg…

**Directing the AI.** Fill the frame with the face from hairline to chin and remove all visible background. Use a longer or macro portrait perspective to keep features controlled, then shape the planes with hard toplight and deep eye-socket shadow. Preserve pores, moisture, and micro-expression rather than cosmetic smoothness. For video, hold the subject inside this narrow boundary with only breath, blinking, or minut…

**Common mistakes.**
- Leaving background visible around the head, giving the viewer spatial relief that the choker shot should deny.
- Moving too close with a wide lens, distorting the nose and cheeks into unintended caricature.
- Using the framing for neutral exposition, where its psychological pressure overwhelms the actual dramatic importance.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | **null** | kling-1.5 | no |
| `luma` Luma Dream Machine | **null** | dream-machine | no |
| `mj61` Midjourney v6.1 | **null** | v6.1 | no |
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | **null** | gen-3-alpha | no |
| `sora` OpenAI Sora | **null** | sora-1 | no |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `spotlight-hero-card`, 220f

**Sources.** [50+ Types of Camera Shots, Angles, and Techniques](None)


### close-up

**"Close-Up Prompt for AI Image & Video"** · `camera-work` · level basic

```
Tight close-up of [Subject] filling the entire frame, every pore and texture rendered in sharp detail, shallow depth of field with background dissolving into creamy bokeh, warm sidelight from a single source, shot on Cooke S4 75mm at T2, Kodak Vision3 500T color science
```

A tightly framed shot that fills the screen with a subject's face or a specific detail, revealing emotions, textures, and subtle details invisible in wider shots. Carl Theodor Dreyer's "The Passion of Joan of Arc" (1928) is built almost entirely from devastating close-ups of Renée Falconetti's face, widely considered the greatest performance ever captured on film. Sergio Leone elevated the close-…

**When to use.** Use a close-up when a face, gesture, or object carries the meaning of the scene. It removes environmental information and asks the audience to read micro-expression, texture, and hesitation. Save it for information that genuinely deserves intimacy; constant close-ups flatten the visual hierarchy.

**Directing the AI.** Specify the crop, focal length, focus plane, eye line, and one motivated light source. If the face must remain consistent, describe the identity before the shot language and keep lens distortion controlled with portrait-range focal lengths. For video, ask for restrained movement — a breath, blink, or minute push-in — rather than a second competing action.

**Common mistakes.**
- Using a very wide lens close to the face when you do not want exaggerated facial distortion.
- Adding so much environment and action that the result stops reading as a close-up.
- Demanding sharp eyes, sharp background, heavy bokeh, and extreme shallow focus simultaneously.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: pan_right | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: smooth_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: smooth_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `spotlight-hero-card`, 220f

**Sources.** [Close-Up Shots: Examples of Camera Movement and Angles](None)


### cowboy-shot

**"Cowboy Shot Prompt for AI Image & Video"** · `camera-work` · level basic

```
Cowboy shot of [Subject] framed from mid-thigh up, hands hanging loose at their sides, the figure's posture radiating coiled readiness beneath apparent calm, shot on Techniscope 2-perf 35mm for a gritty widescreen look, warm dusty color palette of ochre and leather brown
```

Frames the subject from roughly mid-thigh up, named after Western films where the frame needed to include a gunslinger's holstered weapon, conveying casual authority. Sergio Leone codified this framing in his Dollars trilogy, making the cowboy shot synonymous with Clint Eastwood's laconic gunfighter stance. Tarantino pays homage to the cowboy shot throughout "Kill Bill" and "Django Unchained," an…

**When to use.** Use the cowboy shot when a character's hands, hips, stance, or carried weapon matters alongside the face. Mid-thigh framing conveys readiness and casual authority without losing expression. It fits Western tension, action entrances, fashion, and any moment built around what someone might reach for.…

**Directing the AI.** Crop the figure at mid-thigh, keeping both hands visible and enough headroom for a stable silhouette. Ask for a relaxed but ready posture, with weight distribution and wardrobe details doing as much work as expression. Use a gritty widescreen texture, warm ochre and leather tones, and a natural perspective that does not stretch the legs. In video, hold the framing through hand movement rather tha…

**Common mistakes.**
- Cropping at the waist, which removes the holster zone and turns the image into a standard medium shot.
- Hiding both hands behind props or frame edges, losing the latent action that gives the composition tension.
- Using an exaggerated low angle by default, piling obvious dominance onto framing that already carries authority.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | **null** | kling-1.5 | no |
| `luma` Luma Dream Machine | **null** | dream-machine | no |
| `mj61` Midjourney v6.1 | **null** | v6.1 | no |
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | **null** | gen-3-alpha | no |
| `sora` OpenAI Sora | **null** | sora-1 | no |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `spotlight-hero-card`, 220f

**Sources.** [50+ Types of Camera Shots, Angles, and Techniques](None)


### crane-shot

**"Crane Shot Prompt for AI Image & Video"** · `camera-work` · level advanced

```
Crane shot beginning tight on [Subject] then sweeping upward and backward in a majestic arc to reveal the true surrounding scale, the individual becoming one element among many in a seamless vertical revelation, shot on ARRI Alexa 65 with a 35mm Signature Prime, the mechanical grace of a Technocrane executing a precisely choreographed arc, golden hour light flooding horizontally
```

Camera mounted on a mechanical crane arm that sweeps upward, downward, or across a scene with majestic, controlled movement, often used for dramatic reveals or grand establishing moments. Orson Welles opened "Touch of Evil" with one of cinema's most famous crane shots — a continuous three-minute take following a car bomb through a Mexican border town. The final crane shot of "Gone with the Wind"…

**When to use.** Choose a crane shot when a scene needs a grand reveal that changes scale and perspective in one controlled movement. Rising from a person to a crowd, battlefield, building, or landscape can expose consequences beyond the intimate frame. Descending can isolate one figure from a larger world. The mov…

**Directing the AI.** Begin on a clearly framed subject, then sweep upward and backward along a smooth mechanical arc. Reveal new layers in sequence rather than exposing the full environment at once: nearby action, surrounding group, architecture, then horizon. Keep the subject's location traceable as scale expands. Use broad golden-hour light to bind the levels together and a wide lens that avoids severe distortion.…

**Common mistakes.**
- Revealing the whole setting in the first frame, leaving the crane movement without new visual information to uncover.
- Losing the original subject during ascent, which breaks the intended transition between individual and surrounding scale.
- Replacing the controlled arc with random airborne drift that reads as an aerial shot rather than crane movement.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | **null** | kling-1.5 | no |
| `luma` Luma Dream Machine | **null** | dream-machine | no |
| `mj61` Midjourney v6.1 | **null** | v6.1 | no |
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | **null** | gen-3-alpha | no |
| `sora` OpenAI Sora | **null** | sora-1 | no |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `crane-rise-reveal`, 20f

**Sources.** [50+ Types of Camera Shots, Angles, and Techniques](None)


### crash-zoom

**"Crash Zoom Prompt for AI Image & Video"** · `camera-work` · level intermediate

```
Crash zoom snapping from a wide shot to an extreme close-up of [Subject] in half a second, the blur of the rapid zoom creating concentric radial streaks, shot on a vintage Angenieux 25-250mm zoom cranked at maximum speed, 35mm film grain adding grit to the motion blur, Shaw Brothers visual energy channeled through a modern lens
```

A sudden, rapid zoom into a subject for dramatic emphasis, often used for comedic punchlines, horror reveals, or martial arts impact moments. The crash zoom is a staple of Hong Kong martial arts cinema, used by directors like Lau Kar-leung and Chang Cheh in Shaw Brothers productions to punctuate kung fu strikes. Quentin Tarantino pays homage to this in "Kill Bill," and Edgar Wright uses crash zoo…

**When to use.** Use a crash zoom to punch into a revelation, reaction, weapon, strike, or comic surprise with deliberate visual aggression. Unlike a push-in, it changes framing through a rapid lens move and should feel abrupt. The technique fits martial arts, horror, action, and stylized comedy. Save it for hard a…

**Directing the AI.** Begin on a readable wide or medium composition, then snap the zoom to an extreme close-up in roughly half a second. Keep the target centered enough to land sharply after a brief burst of concentric radial streaking. Add gritty film texture without smearing the final frame. Define the exact trigger, such as a blow or sudden look, and hold on the destination. Do not move the camera through space; t…

**Common mistakes.**
- Physically rushing the camera forward, which creates parallax and changes the move into a rapid dolly shot.
- Failing to identify the landing detail, causing the zoom to end between subjects or on an unreadable crop.
- Extending the blur across the held close-up, removing the crisp punctuation that makes the snap satisfying.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | **null** | kling-1.5 | no |
| `luma` Luma Dream Machine | **null** | dream-machine | no |
| `mj61` Midjourney v6.1 | **null** | v6.1 | no |
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | **null** | gen-3-alpha | no |
| `sora` OpenAI Sora | **null** | sora-1 | no |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `crash-impact-real` (crash-zoom-punch), 11f, `crash-zoom-real` (crash-zoom-punch), 11f

**Sources.** [50+ Types of Camera Shots, Angles, and Techniques](None)


### dolly-shot

**"Dolly Shot Prompt for AI Image & Video"** · `camera-work` · level intermediate

```
Smooth dolly shot gliding toward [Subject], the camera at eye level moving with buttery precision on dolly track, parallax effect separating foreground elements from the mid-ground subject from far-ground details, shot on 35mm with Panavision Primo lenses, rich blacks and saturated warm tones, the elegant motion of precision dolly track work
```

A smooth camera movement where the entire camera physically moves toward, away from, or alongside the subject on a wheeled platform or track, creating an immersive sense of movement through space. Orson Welles used dolly shots to navigate the deep-focus interiors of "Citizen Kane," while Spike Lee invented his signature double-dolly shot — mounting both actor and camera on the same platform — to…

**When to use.** Use a dolly-in when a realization, threat, or emotional detail needs to become unavoidable. Dolly out when context should overwhelm the subject or create emotional distance. Move alongside a character when the audience should travel with them rather than simply observe them.

**Directing the AI.** Describe physical camera travel, direction, speed, subject lock, and foreground-to-background separation. "Dolly toward" is more useful than "cinematic movement." Give the model visible layers for parallax — a foreground obstruction, the subject in the middle distance, and a readable background — so the move changes spatial relationships instead of behaving like a digital zoom.

**Common mistakes.**
- Calling for a dolly and a zoom at the same time without intentionally asking for a dolly zoom.
- Describing camera movement without foreground or background layers, leaving no parallax for the model to express.
- Stacking "smooth," "dynamic," "epic," and multiple conflicting camera directions instead of specifying one controlled move.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: pan_right | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: smooth_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: smooth_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `bullet-time-freeze-orbit` (tension-camera-moves), 150f, `crash-impact-real` (crash-zoom-punch), 11f, `crash-zoom-real` (crash-zoom-punch), 11f, `dutch-roll-to-level` (tension-camera-moves), 150f, `pull-back-isolation` (tension-camera-moves), 150f, `slow-push-in` (tension-camera-moves), 150f

**Sources.** [The Dolly Shot: How To Create Powerful Shots With Simple Movement](None)


### dutch-angle

**"Dutch Angle Prompt for AI Image & Video"** · `camera-work` · level basic

```
[Subject] framed at a sharp 25-degree Dutch angle, vertical lines tilting diagonally across the frame, long distorted shadows, overhead lighting casting fractured geometric patterns, 35mm film grain, Zeiss Super Speed 25mm, anamorphic edge distortion
```

A shot where the camera is tilted on its roll axis, creating a diagonal horizon line to convey unease, disorientation, tension, or a character's disturbed psychological state. Carol Reed made the Dutch angle iconic in "The Third Man" (1949), tilting nearly every frame in the Vienna sewers to mirror the moral corruption of Harry Lime. Tim Burton adopted it as a signature style in "Batman" and "Edw…

**When to use.** Use a Dutch angle when the world, character, or power relationship has slipped out of balance. The tilt should express a specific instability — paranoia, intoxication, danger, moral corruption — not simply make a frame look more cinematic.

**Directing the AI.** State the roll angle and preserve strong architectural or horizon lines so the tilt remains legible. Pair the canted frame with one emotional cause and a controlled lens choice. In video, keep the roll fixed unless the act of rotating the camera is itself the point; uncontrolled horizon drift reads as generation error rather than direction.

**Common mistakes.**
- Tilting a frame that has no strong vertical or horizontal references, making the technique visually disappear.
- Using the angle in every shot until disorientation becomes the visual baseline and loses meaning.
- Combining a Dutch angle with several unrelated distortions that obscure the intended psychological signal.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: pan_right | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: smooth_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: smooth_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `fracture`, 156f, `steep-tilt-glide`, 120f

**Sources.** [Location, location, location: Vienna and The Third Man](None)


### establishing-shot

**"Establishing Shot Prompt for AI Image & Video"** · `camera-work` · level basic

```
Wide establishing shot of [Subject] at blue hour, deep indigo sky with the last traces of sunset, a few warm lights glowing from within, atmospheric haze softening the distance, shot on ARRI Alexa with Zeiss Master Primes, desaturated cool palette with selective warm accents, architectural precision meets cinematic storytelling
```

A wide shot typically used at the beginning of a scene to set the context, showing the location, time of day, and spatial relationships before cutting to closer action. Stanley Kubrick's establishing shots in "The Shining" — the Overlook Hotel dwarfed by mountains — immediately communicated isolation and foreboding. Ridley Scott's opening of "Blade Runner" established a dystopian Los Angeles with…

**When to use.** Open with an establishing shot when viewers need to understand where the scene happens, what time or weather shapes it, and how the key spaces connect. A strong version can also seed isolation, danger, wealth, or decay through architecture and scale. Use it before tighter coverage or after a major…

**Directing the AI.** Frame the location wide enough to show its dominant architecture, surrounding terrain, access points, and one small sign of life. Set the scene at blue hour with a deep indigo sky, faint sunset residue, warm interior lights, and haze softening the distance. Keep the composition legible rather than merely expansive. If generating video, begin still or with a restrained drift, allowing the viewer t…

**Common mistakes.**
- Showing a beautiful location without the landmarks or spatial relationships needed to orient the next scene.
- Making the principal character too large in frame, turning contextual coverage into a conventional long shot.
- Packing the image with unrelated atmosphere cues that obscure the intended time, geography, or narrative tone.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: pan_right | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: smooth_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: smooth_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `dolly-zoom-real` (depth-layer-moves), 150f, `drone-dive-landing` (space-camera-moves), 150f, `exploded-view` (space-camera-moves), 150f, `multiplane-real` (depth-layer-moves), 150f

**Sources.** [50+ Types of Camera Shots, Angles, and Techniques](None)


### extreme-close-up

**"Extreme Close-Up Prompt for AI Image & Video"** · `camera-work` · level basic

```
Extreme macro close-up of [Subject] filling the entire frame, every microscopic detail rendered with clinical precision, ring light creating a circular catchlight, razor-thin depth of field at f/2.8 on a 100mm macro lens, Fujifilm Velvia-inspired saturated color science, the forensic intimacy of extreme proximity
```

An intensely tight shot focusing on a very specific detail — an eye, a hand trembling, a drop of sweat — amplifying significance and forcing the viewer into intimate proximity with the subject. Sergio Leone built the climax of "The Good, the Bad and the Ugly" almost entirely from extreme close-ups of eyes during the three-way standoff, creating unbearable tension through the intimacy of a glance.…

**When to use.** Cut to an extreme close-up when one tiny detail must carry the scene: a pupil changing, a finger tightening, sweat forming, or a needle touching skin. The frame forces attention and turns physical texture into emotion. Use it to intensify suspense, reveal evidence, or make an ordinary object uncann…

**Directing the AI.** Name the exact fragment that fills the frame and exclude the wider face or body. Ask for macro-scale detail, a 100mm macro perspective, razor-thin depth of field, and one precise focus plane. A circular catchlight or controlled ring light can reveal surface structure without flattening the subject. Keep background information abstract or absent. In video, limit motion to a tremor, blink, bead of…

**Common mistakes.**
- Prompting a generic close-up instead of naming the exact eye, fingertip, wound, or object detail that fills frame.
- Demanding sharpness everywhere, which removes the selective attention and optical intimacy of true macro framing.
- Adding a busy background that reintroduces context and breaks the suffocating proximity of the chosen detail.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | **null** | kling-1.5 | no |
| `luma` Luma Dream Machine | **null** | dream-machine | no |
| `mj61` Midjourney v6.1 | **null** | v6.1 | no |
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | **null** | gen-3-alpha | no |
| `sora` OpenAI Sora | **null** | sora-1 | no |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `spotlight-hero-card`, 220f

**Sources.** [50+ Types of Camera Shots, Angles, and Techniques](None)


### extreme-long-shot

**"Extreme Long Shot Prompt for AI Image & Video"** · `camera-work` · level basic

```
Extreme long shot of [Subject] barely visible against a vast landscape stretching to the horizon, a single long shadow the only vertical element in a perfectly horizontal world, sky gradient from pale white at the horizon to deep cerulean overhead, shot on large format 65mm film, infinite depth of field rendering everything sharp from feet to infinity, Lawrence of Arabia scale and desolation
```

A very wide shot where the subject appears small against a vast environment, emphasizing scale, isolation, or the overwhelming nature of the surroundings. David Lean defined the technique in "Lawrence of Arabia," where Peter O'Toole becomes a speck against infinite desert horizons, communicating both the grandeur and the punishing emptiness of the landscape. Terrence Malick uses extreme long shot…

**When to use.** Use an extreme long shot when the environment should overwhelm the person inside it. It suits desert crossings, isolated vehicles, battlefields, migration, wilderness, and moments when distance itself is the emotion. The subject may be tiny, but must remain compositionally discoverable. Choose this…

**Directing the AI.** Make the subject a small but intentional mark against a horizon-spanning environment. Describe a dominant horizontal composition, immense negative space, and one long shadow or contrasting color that lets the figure register. Keep detail sharp from near ground to distant horizon, with a pale-to-cerulean sky gradient reinforcing depth. For moving footage, use a nearly static frame or a very slow l…

**Common mistakes.**
- Making the subject so invisible that the frame reads only as landscape rather than a deliberate scale comparison.
- Using shallow depth of field, which collapses the vast environmental detail needed to communicate distance and isolation.
- Crowding the horizon with several competing focal points that weaken the lone figure's compositional importance.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | **null** | kling-1.5 | no |
| `luma` Luma Dream Machine | **null** | dream-machine | no |
| `mj61` Midjourney v6.1 | **null** | v6.1 | no |
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | **null** | gen-3-alpha | no |
| `sora` OpenAI Sora | **null** | sora-1 | no |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `drone-dive-landing` (space-camera-moves), 150f, `exploded-view` (space-camera-moves), 150f

**Sources.** [50+ Types of Camera Shots, Angles, and Techniques](None)


### eye-level-shot

**"Eye-Level Shot Prompt for AI Image & Video"** · `camera-work` · level basic

```
Eye-level shot of [Subject] with the camera positioned exactly at their eye height creating a direct and equal relationship with the viewer, natural available light providing gentle directional illumination, no dramatic angles or manipulation, shot on 16mm film stock with gentle grain, naturalistic color palette, intimate documentary stillness
```

A neutral shot taken at the subject's eye height, the most natural and common camera angle, creating a sense of equality and objectivity between viewer and subject. Yasujiro Ozu famously placed his camera at a low eye-level (the "tatami shot") in films like "Tokyo Story," creating an intimate, respectful perspective that defined Japanese domestic cinema. The Dardenne brothers use persistent eye-l…

**When to use.** Choose eye level when the camera should meet a person without glorifying, diminishing, or judging them. It is the dependable angle for interviews, domestic scenes, observational drama, and direct exchanges where performance matters more than visual manipulation. Because it feels normal, it can also…

**Directing the AI.** Position the lens exactly at the subject's eye height and keep verticals neutral. Frame the person with a natural conversational distance, available directional light, gentle 16mm-style grain, and an unforced color palette. Avoid heroic upward lines or downward compression. Let posture, gaze, and small facial shifts carry the frame. In video, use minimal handheld breathing or a locked camera rath…

**Common mistakes.**
- Placing the camera at chest or forehead height while calling it eye level, subtly changing the power relationship.
- Adding dramatic lens distortion or canted framing that contradicts the angle's neutral, observational purpose.
- Treating neutrality as visual emptiness instead of using gaze, posture, and available light to hold attention.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | **null** | kling-1.5 | no |
| `luma` Luma Dream Machine | **null** | dream-machine | no |
| `mj61` Midjourney v6.1 | **null** | v6.1 | no |
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | **null** | gen-3-alpha | no |
| `sora` OpenAI Sora | **null** | sora-1 | no |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `graze-face-tour`, 150f

**Sources.** [50+ Types of Camera Shots, Angles, and Techniques](None)


### handheld-shot

**"Handheld Shot Prompt for AI Image & Video"** · `camera-work` · level basic

```
Handheld camera following [Subject], natural shake and breathing motion in the frame, motion blur on fast-moving elements, the gritty texture of Super 16mm film pushed two stops in processing, desaturated color with blown-out highlights, the raw unfiltered energy of being inside the moment rather than observing it
```

Camera held by the operator without stabilization, resulting in natural shake and movement that creates raw immediacy, documentary realism, or frantic energy depending on context. John Cassavetes pioneered the emotional handheld style in "A Woman Under the Influence," where the camera's restlessness mirrors Gena Rowlands' unraveling psyche. Paul Greengrass brought visceral handheld energy to main…

**When to use.** Reach for handheld movement when the camera must feel physically present inside an unstable moment. It can follow a character through conflict, capture documentary spontaneity, mirror panic, or make polished spaces feel exposed. The shake should reflect operator behavior and subject movement, not r…

**Directing the AI.** Describe a shoulder-held operator following close behind or beside the subject, with subtle breathing drift, imperfect reframing, and heavier jolts only during sudden movement. Allow motion blur on fast gestures and occasional clipped highlights, supported by gritty Super 16 texture and restrained color. Keep the subject recoverable after each shake. For a still image, imply handheld capture thro…

**Common mistakes.**
- Requesting constant violent shake, which feels synthetic and makes the subject impossible to track through the scene.
- Combining handheld language with perfectly centered, mechanically smooth framing that cancels the intended operator presence.
- Applying equal blur to every surface instead of tying motion artifacts to camera and subject movement.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | **null** | kling-1.5 | no |
| `luma` Luma Dream Machine | **null** | dream-machine | no |
| `mj61` Midjourney v6.1 | **null** | v6.1 | no |
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | **null** | gen-3-alpha | no |
| `sora` OpenAI Sora | **null** | sora-1 | no |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `graze-face-tour`, 150f

**Sources.** [50+ Types of Camera Shots, Angles, and Techniques](None)


### head-on-shot

**"Head-On Shot Prompt for AI Image & Video"** · `camera-work` · level intermediate

```
Head-on shot of [Subject] moving directly toward the camera with perfect bilateral symmetry, the camera holding its ground as the figure grows larger in frame, shot on anamorphic 40mm Panavision C-series glass with slight barrel distortion adding menace, teal shadows and amber highlights, the confrontational energy of direct approach
```

A shot where the subject moves or faces directly toward the camera, creating a confrontational, powerful feeling as the subject approaches or stares directly at the viewer. Stanley Kubrick mastered the head-on shot with his famous "Kubrick stare" — characters like Alex in "A Clockwork Orange" and Jack Torrance in "The Shining" glaring directly into the lens with menacing intensity. Spike Lee's do…

**When to use.** Use a head-on shot when a character must confront the audience or advance with undeniable force. Direct eye contact can signal menace, confidence, accusation, or eerie calm, while forward movement steadily increases pressure. Symmetry makes the approach feel controlled and inevitable. Save this ang…

**Directing the AI.** Center the subject on the lens axis and establish perfect bilateral balance around them. Have the camera hold position while the figure faces or walks directly toward it, growing from a smaller frame to a dominant one. Use a moderately wide anamorphic perspective with slight barrel distortion, teal shadows, and amber highlights to add pressure. Keep lateral drift near zero. The gaze, shoulders, a…

**Common mistakes.**
- Letting the subject approach diagonally, which changes the shot from direct confrontation into ordinary tracking coverage.
- Breaking symmetry with accidental background clutter that distracts from the figure's controlled movement toward the lens.
- Using a cheerful wide-angle distortion when the intended emotion depends on menace, authority, or focused intensity.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | **null** | kling-1.5 | no |
| `luma` Luma Dream Machine | **null** | dream-machine | no |
| `mj61` Midjourney v6.1 | **null** | v6.1 | no |
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | **null** | gen-3-alpha | no |
| `sora` OpenAI Sora | **null** | sora-1 | no |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `basic-3d-scene`, 180f

**Sources.** [50+ Types of Camera Shots, Angles, and Techniques](None)


### high-angle-shot

**"High Angle Shot Prompt for AI Image & Video"** · `camera-work` · level basic

```
High angle shot looking down on [Subject], the perspective making them appear impossibly small and vulnerable, the camera positioned high above, shot on Arriflex with a 21mm wide lens to exaggerate spatial distortion, muted institutional color palette with a single color accent
```

Camera positioned above the subject, looking down, making the subject appear smaller, weaker, or more vulnerable while also providing a broader view of the scene layout. Alfred Hitchcock used high angles masterfully in "Psycho" and "Vertigo" to diminish characters and reveal their spatial entrapment. Orson Welles employed towering high angles in "The Trial" to crush Joseph K under oppressive bure…

**When to use.** A high angle is useful when the viewer should understand both a subject and the forces surrounding them. Looking down can make a person feel vulnerable, trapped, watched, or physically diminished while revealing exits, barriers, and crowd positions. It works for helplessness and tactical overview w…

**Directing the AI.** Raise the camera clearly above the subject and aim downward on a visible diagonal, preserving depth between foreground, person, and floor. Use a wide lens to expand the surrounding architecture and reduce the figure within it. Muted institutional colors with one controlled accent can isolate the subject. Show the boundaries, obstacles, or empty space responsible for the pressure. For video, hold…

**Common mistakes.**
- Pushing the camera directly overhead, which removes the diagonal depth and turns the setup into another technique.
- Isolating the subject against an empty floor without environmental elements that explain their vulnerability or confinement.
- Using extreme wide-angle distortion so aggressively that warped architecture becomes more important than the emotional hierarchy.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | **null** | kling-1.5 | no |
| `luma` Luma Dream Machine | **null** | dream-machine | no |
| `mj61` Midjourney v6.1 | **null** | v6.1 | no |
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | **null** | gen-3-alpha | no |
| `sora` OpenAI Sora | **null** | sora-1 | no |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `overhead-tabletop-drop` (overhead-camera-moves), 144f, `tilt-reveal` (overhead-camera-moves), 144f

**Sources.** [50+ Types of Camera Shots, Angles, and Techniques](None)


### insert-shot

**"Insert Shot Prompt for AI Image & Video"** · `camera-work` · level basic

```
Insert shot of [Subject] isolated in tight framing, warm lamplight casting a golden glow while the surrounding space falls into shadow, shot with a macro lens at f/2 creating razor-thin focus, Kodak 5219 500T film stock warmth, the weight of consequence concentrated in a single object
```

A close-up cut to a specific detail within a scene — a ticking clock, a letter, a weapon being drawn — directing audience attention to a crucial narrative element. Hitchcock was the supreme master of the insert shot, using close-ups of keys, glasses of milk, and scissors in films like "Dial M for Murder" and "Notorious" to build unbearable suspense from ordinary objects. Quentin Tarantino uses st…

**When to use.** Use an insert when the audience must notice a detail that changes how the scene is understood. A key turning, clock ticking, letter opening, weapon clearing a holster, or hand hesitating can carry plot and tension in a compact frame. The object should already belong to the scene. Insert shots are s…

**Directing the AI.** Identify one object or action and frame it tightly enough that nothing competes for attention. Light it with a motivated warm lamp or practical source while the surrounding area falls into shadow. Use macro-like proximity, a narrow focus plane, and tactile material detail to give the object consequence. For video, define the exact event within the insert, such as a second hand advancing or a thum…

**Common mistakes.**
- Choosing an object with no later consequence, training viewers to search for meaning that the sequence never pays off.
- Including too much of the surrounding scene, so attention remains divided instead of landing on the narrative detail.
- Rendering the insert in a mismatched lighting style that disconnects it from the space established around it.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | **null** | kling-1.5 | no |
| `luma` Luma Dream Machine | **null** | dream-machine | no |
| `mj61` Midjourney v6.1 | **null** | v6.1 | no |
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | **null** | gen-3-alpha | no |
| `sora` OpenAI Sora | **null** | sora-1 | no |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `dolly-zoom-real` (depth-layer-moves), 150f, `multiplane-real` (depth-layer-moves), 150f

**Sources.** [50+ Types of Camera Shots, Angles, and Techniques](None)


### long-shot

**"Long Shot Prompt for AI Image & Video"** · `camera-work` · level basic

```
Long shot of [Subject] with the full figure visible from head to foot, the scale of the environment dwarfing the human figure while the figure's posture radiates quiet authority, shot on 65mm large format with a 50mm lens, rich Technicolor-inspired warm palette, the mythic framing of classic cinema
```

Shows the subject's full body within their environment, balancing character and setting while establishing spatial relationships and keeping the subject identifiable. John Ford used the long shot to place his characters within the monumental landscapes of Monument Valley in "The Searchers," making John Wayne both heroic and dwarfed by nature. Akira Kurosawa's long shots in "Seven Samurai" choreog…

**When to use.** Choose a long shot when the audience needs the subject's full body and enough environment to understand movement, distance, or social position. It suits entrances, confrontations, dance, travel, and action blocking where posture tells part of the story. The person remains identifiable, unlike an ex…

**Directing the AI.** Frame the subject from head to foot with intentional space above, below, and along their direction of movement. Let the environment remain substantial but subordinate to readable posture and silhouette. Use a natural perspective with deep enough focus to describe the setting, warm earth tones, and one clear line linking character to landscape. For video, preserve the full body through the action…

**Common mistakes.**
- Cropping the feet or head during movement, which quietly converts the intended framing into an awkward medium-long view.
- Allowing the landscape to dwarf the figure so completely that the result becomes an extreme long shot.
- Using shallow focus that erases the environmental relationship the wider framing was chosen to establish.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | **null** | kling-1.5 | no |
| `luma` Luma Dream Machine | **null** | dream-machine | no |
| `mj61` Midjourney v6.1 | **null** | v6.1 | no |
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | **null** | gen-3-alpha | no |
| `sora` OpenAI Sora | **null** | sora-1 | no |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `drone-dive-landing` (space-camera-moves), 150f, `exploded-view` (space-camera-moves), 150f

**Sources.** [50+ Types of Camera Shots, Angles, and Techniques](None)


### low-angle-shot

**"Low Angle Shot Prompt for AI Image & Video"** · `camera-work` · level basic

```
Low angle shot looking up at [Subject] from below, the camera positioned at ground level shooting upward through converging vertical lines, shot on Cooke S4 18mm wide-angle lens exaggerating the height distortion, high-contrast Kodak Double-X black and white aesthetic, Citizen Kane grandeur
```

Camera positioned below the subject, looking up, making the subject appear dominant, powerful, heroic, or imposing. Orson Welles used low angles obsessively in "Citizen Kane," famously requiring trenches cut into studio floors to achieve extreme upward perspectives on Charles Foster Kane, visually encoding his megalomania into every frame. Quentin Tarantino's iconic trunk shots — looking up at ch…

**When to use.** Use a low angle to make a person, structure, or object command the frame. The upward view can express authority, threat, heroism, arrogance, or awe depending on performance and light. It also lets architecture converge behind the subject, increasing apparent height. Choose it for power shifts and m…

**Directing the AI.** Lower the camera beneath the subject's eye line and point upward through converging walls, columns, or skyline. A wide lens can stretch height, but keep the face and body recognizable rather than grotesquely warped. Give the subject a firm stance and place open sky or strong architecture behind them. High-contrast monochrome treatment can reinforce authority. In motion, advance carefully or hold…

**Common mistakes.**
- Placing the lens only slightly below eye level, producing a neutral portrait with no meaningful upward pressure.
- Using an ultra-wide lens too close to the face, creating comic distortion instead of deliberate dominance.
- Ignoring the background, even though converging architecture or open sky is central to the angle's sense of scale.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | **null** | kling-1.5 | no |
| `luma` Luma Dream Machine | **null** | dream-machine | no |
| `mj61` Midjourney v6.1 | **null** | v6.1 | no |
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | **null** | gen-3-alpha | no |
| `sora` OpenAI Sora | **null** | sora-1 | no |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `steep-tilt-glide`, 120f

**Sources.** [50+ Types of Camera Shots, Angles, and Techniques](None)


### master-shot

**"Master Shot Prompt for AI Image & Video"** · `camera-work` · level intermediate

```
Wide master shot of [Subject] with all elements visible simultaneously, every figure precisely blocked to create a composition of intersecting eyelines and subtle tensions, shot on 35mm with a 27mm lens from a tripod, classical Hollywood staging with Altman-esque layered naturalism
```

A continuous wide shot that captures the entire scene from start to finish, serving as the foundation over which closer coverage is layered in editing. Robert Altman was famous for shooting elaborate master shots with multiple overlapping conversations in films like "Nashville" and "Short Cuts," trusting the wide frame to let audiences discover the drama themselves. Sidney Lumet staged masterful…

**When to use.** Build a master shot when a scene depends on ensemble timing, spatial continuity, or the audience choosing where to look. It provides the full dramatic action in one wide composition and becomes a foundation for closer coverage. The format suits overlapping conversations, group conflict, and careful…

**Directing the AI.** Show the entire playing area and every essential figure at once. Block actors on distinct depth planes with intersecting eyelines, clear entrances, and enough separation to read alliances or friction. Use a stable tripod perspective and a moderately wide lens rather than an exaggerated panorama. Lighting should motivate attention inside the frame without hiding secondary action. For video, descri…

**Common mistakes.**
- Arranging every actor in a flat line, which records the cast but reveals nothing about hierarchy or tension.
- Framing so wide that gestures and eyelines become unreadable, defeating the purpose of sustained ensemble staging.
- Calling a short location reveal a master shot even though it does not contain the scene's complete dramatic action.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | **null** | kling-1.5 | no |
| `luma` Luma Dream Machine | **null** | dream-machine | no |
| `mj61` Midjourney v6.1 | **null** | v6.1 | no |
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | **null** | gen-3-alpha | no |
| `sora` OpenAI Sora | **null** | sora-1 | no |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `drone-dive-landing` (space-camera-moves), 150f, `exploded-view` (space-camera-moves), 150f

**Sources.** [50+ Types of Camera Shots, Angles, and Techniques](None)


### medium-close-up

**"Medium Close-Up Prompt for AI Image & Video"** · `camera-work` · level basic

```
Medium close-up of [Subject] from the chest up, the intimate distance perfect for reading micro-expressions while body language of tension remains visible in the shoulders and hands, shot on a 75mm Cooke S4 at T2, noir-inflected color palette of deep blues and intermittent warm accents
```

Frames the subject from the chest up, tighter than a medium shot but not as intimate as a close-up, ideal for emotional dialogue while retaining some body language context. This framing became the default for television drama and is the backbone of prestige TV from "The Sopranos" to "Breaking Bad." In cinema, Michael Mann favors the medium close-up in "Heat" and "Collateral" to maintain both the…

**When to use.** Choose a medium close-up when emotional dialogue needs intimacy without the pressure of a full close-up. Chest-up framing keeps micro-expressions legible while shoulders and upper-body tension remain available. It is strong for interviews, confession, restrained conflict, and reaction beats. Pull w…

**Directing the AI.** Frame from the chest upward, keeping the shoulders fully present and the eyes near the upper third. Use a slightly longer portrait perspective, moderate background blur, and controlled contrast that preserves skin detail. Let small changes in jaw, breath, and shoulder position carry the performance. Include only enough environment to anchor location. For video, avoid automatic zooming; hold the i…

**Common mistakes.**
- Cropping beneath the chin or above the shoulders, which turns the intended frame into a tight close-up.
- Leaving too much torso visible, weakening facial emphasis and drifting back toward a conventional medium shot.
- Smoothing skin and expression so aggressively that the subtle performance cues the framing exists to capture disappear.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | **null** | kling-1.5 | no |
| `luma` Luma Dream Machine | **null** | dream-machine | no |
| `mj61` Midjourney v6.1 | **null** | v6.1 | no |
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | **null** | gen-3-alpha | no |
| `sora` OpenAI Sora | **null** | sora-1 | no |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `spotlight-hero-card`, 220f

**Sources.** [50+ Types of Camera Shots, Angles, and Techniques](None)


### medium-shot

**"Medium Shot Prompt for AI Image & Video"** · `camera-work` · level basic

```
Medium shot of [Subject] framed from the waist up, the perfect conversational distance that reveals both facial expression and the eloquent language of hands, shot on a 50mm lens at T2.8, Kodak Vision3 200T with rich warm midtones
```

Frames the subject from roughly the waist up, the workhorse of dialogue scenes — close enough to read expressions but wide enough to capture body language and gestures. Howard Hawks built his entire directorial style around the medium shot in films like "His Girl Friday" and "The Big Sleep," trusting the perfect middle distance to convey rapid-fire dialogue and physical chemistry. Aaron Sorkin's…

**When to use.** The medium shot is the default when dialogue and physical behavior need equal attention. Waist-up framing keeps expressions readable while preserving hands, shoulders, posture, and some environmental context. Use it for conversations, walk-and-talks, demonstrations, and quiet character beats that d…

**Directing the AI.** Frame the subject from roughly the waist upward and leave room for hands to enter naturally. Use a normal perspective around 50mm, moderate depth of field, and warm midtones that keep skin and clothing dimensional. Place enough background detail to locate the scene without competing with the performance. For video, allow gestures and small body shifts to remain inside frame; avoid automated cropp…

**Common mistakes.**
- Cropping at the chest and losing the hands, which makes the frame behave more like a medium close-up.
- Leaving excessive empty space around one person, weakening the practical balance between expression and environment.
- Using shallow focus so extreme that every gesture crossing the narrow plane becomes distracting and soft.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | **null** | kling-1.5 | no |
| `luma` Luma Dream Machine | **null** | dream-machine | no |
| `mj61` Midjourney v6.1 | **null** | v6.1 | no |
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | **null** | gen-3-alpha | no |
| `sora` OpenAI Sora | **null** | sora-1 | no |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `drone-dive-landing` (space-camera-moves), 150f, `exploded-view` (space-camera-moves), 150f, `spotlight-hero-card`, 220f

**Sources.** [50+ Types of Camera Shots, Angles, and Techniques](None)


### one-er

**"One-er (Oner) Prompt for AI Image & Video"** · `camera-work` · level advanced

```
Long unbroken single take following [Subject] through shifting environments, the entire journey unbroken for minutes of choreographed spatial continuity, shot on Steadicam with an ARRI Alexa Mini and Cooke S4 21mm lens, the shifting light temperatures creating a living color journey through the space
```

An entire scene captured in a single unbroken take with no cuts, demanding precise choreography of actors, camera, and crew while creating real-time tension and immersive spatial continuity. Alfonso Cuarón and Emmanuel Lubezki pushed the oner to its limits in "Children of Men" with a six-minute car ambush shot, and Alejandro González Iñárritu structured the entirety of "Birdman" as one apparent c…

**When to use.** Use a oner when real-time continuity should create immersion, pressure, or virtuoso flow. It can follow characters through connected rooms, preserve an escalating performance, or make viewers discover action as the camera does. The scene needs choreography strong enough to justify the absence of cu…

**Directing the AI.** Describe one unbroken route from the opening composition to the final position, including each doorway, turn, actor crossing, focus change, and lighting transition. Keep the lens moderately wide and the movement Steadicam-smooth so space remains readable. Assign timed actions that motivate the camera's attention without implying cuts. Carry persistent wardrobe, props, and screen direction through…

**Common mistakes.**
- Writing only long continuous take without mapping the route, leaving the scene vulnerable to spatial jumps and changed details.
- Packing unrelated events into the move, so choreography feels like a demonstration rather than one developing dramatic beat.
- Using abrupt focal-length changes or impossible camera teleportation that function as cuts despite continuous-shot language.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | **null** | kling-1.5 | no |
| `luma` Luma Dream Machine | **null** | dream-machine | no |
| `mj61` Midjourney v6.1 | **null** | v6.1 | no |
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | **null** | gen-3-alpha | no |
| `sora` OpenAI Sora | **null** | sora-1 | no |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `fracture`, 156f

**Sources.** [50+ Types of Camera Shots, Angles, and Techniques](None)


### over-the-shoulder

**"Over-the-Shoulder Prompt for AI Image & Video"** · `camera-work` · level basic

```
Over-the-shoulder shot with the near figure's shoulder and jaw soft and dark in the foreground, [Subject] sharply in focus in the mid-ground, the spatial depth between the two figures loaded with tension, shot on a 65mm lens at T2 creating a narrow depth of field, rich chiaroscuro lighting with deep umber shadows and warm golden highlights
```

Shot framed from behind one character, looking past their shoulder at another, the standard coverage for dialogue that creates spatial relationships and a sense of being within the conversation. The shot/reverse-shot pattern using over-the-shoulder angles became the backbone of Hollywood dialogue coverage through the classical studio era. David Fincher meticulously calibrates the exact angle and…

**When to use.** Use over-the-shoulder framing to place the audience inside a conversation while preserving who faces whom. The near shoulder creates depth and makes the listener's presence felt even when attention rests on the speaker. It suits dialogue, interrogation, seduction, negotiation, and withheld reaction…

**Directing the AI.** Place one character's shoulder, jaw, and back of head as a soft dark foreground shape occupying a controlled edge of frame. Hold the other character sharp in the mid-ground with their gaze aimed just beside the lens. Use a narrow depth of field and chiaroscuro to load the gap between them with tension. Keep screen direction consistent across reverse coverage. The foreground figure must remain rec…

**Common mistakes.**
- Letting the foreground head cover the speaker's expression, turning spatial context into a large visual obstruction.
- Breaking eyeline direction between paired shots, which makes both characters appear to face the same side.
- Rendering both planes equally sharp when the scene needs focus to privilege the person currently carrying the beat.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | **null** | kling-1.5 | no |
| `luma` Luma Dream Machine | **null** | dream-machine | no |
| `mj61` Midjourney v6.1 | **null** | v6.1 | no |
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | **null** | gen-3-alpha | no |
| `sora` OpenAI Sora | **null** | sora-1 | no |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `drone-dive-landing` (space-camera-moves), 150f, `exploded-view` (space-camera-moves), 150f

**Sources.** [50+ Types of Camera Shots, Angles, and Techniques](None)


### overhead-shot

**"Overhead Shot Prompt for AI Image & Video"** · `camera-work` · level intermediate

```
Overhead shot looking straight down on [Subject], the flat geometric arrangement rendered as graphic composition, natural north-light creating soft even illumination with no harsh shadows, shot on medium format with a 55mm lens, clinical sharpness of top-down perspective, Wes Anderson-level compositional precision
```

Camera positioned directly above the scene looking straight down, similar to bird's eye but typically closer, often used for tabletop scenes, maps, or choreographed action. Wes Anderson uses overhead shots of hands and objects obsessively in films like "The Grand Budapest Hotel" and "The French Dispatch," turning tabletop arrangements into graphic design. Martin Scorsese employed the technique in…

**When to use.** Choose an overhead shot for close top-down views of hands, food, maps, tools, documents, bodies, or choreographed action. It converts ordinary activity into graphic arrangement while keeping more intimacy than a broad bird's eye view. The technique works for procedures, clues, rituals, and visual c…

**Directing the AI.** Mount the viewpoint directly above the working surface and point straight down, with no horizon or angled wall visible. Arrange hands and objects as a clean graphic composition, using soft north-window illumination to avoid harsh competing shadows. Keep the surface sharp from corner to corner and use a medium-format sense of detail. For video, specify precise hand paths and object changes while t…

**Common mistakes.**
- Tilting the camera enough to reveal side faces, changing the graphic top-down view into an ordinary high angle.
- Scattering props without deliberate spacing, which makes the surface look messy rather than designed for overhead reading.
- Using strong shadows that overlap critical objects and obscure the procedural or narrative information in the arrangement.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | **null** | kling-1.5 | no |
| `luma` Luma Dream Machine | **null** | dream-machine | no |
| `mj61` Midjourney v6.1 | **null** | v6.1 | no |
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | **null** | gen-3-alpha | no |
| `sora` OpenAI Sora | **null** | sora-1 | no |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `overhead-tabletop-drop` (overhead-camera-moves), 144f, `tilt-reveal` (overhead-camera-moves), 144f

**Sources.** [50+ Types of Camera Shots, Angles, and Techniques](None)


### pan-shot

**"Pan Shot Prompt for AI Image & Video"** · `camera-work` · level basic

```
Slow panoramic pan revealing [Subject], the camera rotating smoothly on a fluid head, the steady horizontal sweep connecting a wide expanse of visual information, shot on 35mm anamorphic with Panavision E-series glass, the ultra-wide field of view compressing the panorama into a layered ribbon of texture, cool teal shadows against warm highlight tones
```

A horizontal rotation of the camera on a fixed axis, sweeping left or right to reveal the breadth of a space, follow lateral movement, or connect subjects across a scene. John Ford's slow, reverent pans across Monument Valley in "The Searchers" established the landscape as a character. Jean Renoir pioneered fluid panning in "The Rules of the Game," and Paul Thomas Anderson uses methodical lateral…

**When to use.** Use a pan when attention must travel horizontally without relocating the camera. It can follow a person crossing frame, reveal a landscape, connect two subjects, or uncover new information waiting offscreen. The move creates a relationship between its starting and ending points, so both should matt…

**Directing the AI.** Fix the camera on one axis and describe a smooth left-to-right or right-to-left rotation. Name the opening subject, the visual path through the middle, and the exact endpoint that resolves the move. Use a fluid, measured speed with enough motion blur to feel continuous but not smeared. A wide anamorphic field can layer the panorama. Keep camera height and tilt unchanged, distinguishing rotation f…

**Common mistakes.**
- Failing to specify the start and end subjects, leaving the horizontal move without narrative direction or payoff.
- Combining a pan with forward travel and vertical drift until the motion no longer reads as fixed-axis rotation.
- Moving too quickly for the audience to inspect the landscape or understand the relationship being revealed.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | **null** | kling-1.5 | no |
| `luma` Luma Dream Machine | **null** | dream-machine | no |
| `mj61` Midjourney v6.1 | **null** | v6.1 | no |
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | **null** | gen-3-alpha | no |
| `sora` OpenAI Sora | **null** | sora-1 | no |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `drone-dive-landing` (space-camera-moves), 150f, `exploded-view` (space-camera-moves), 150f

**Sources.** [50+ Types of Camera Shots, Angles, and Techniques](None)


### pov-shot

**"P.O.V. Shot Prompt for AI Image & Video"** · `camera-work` · level intermediate

```
First-person POV shot through the eyes of [Subject], shallow depth of field mimicking unfocused human vision, subtle lens breathing as focus racks, shot on a wide 14mm rectilinear lens to approximate human field of view, the immersive subjectivity of seeing exactly what the character sees
```

Shows the scene exactly as a character sees it, placing the viewer inside their subjective experience and creating powerful identification and immersion. Hitchcock was the master of POV, using subjective shots in "Rear Window" to lock the audience into James Stewart's voyeuristic gaze, and in "Vertigo" to plunge viewers into the protagonist's acrophobia. Gaspar Noé built "Enter the Void" entirely…

**When to use.** Choose a point-of-view shot when viewers must share a character's act of looking rather than merely observe them. It can intensify discovery, fear, desire, surveillance, confusion, or physical danger. The shot works best when paired with a clear owner of the gaze and a meaningful target. Without th…

**Directing the AI.** State whose eyes define the camera and what they are looking toward. Keep the viewpoint at that character's height, with natural head movement, subtle focus breathing, and peripheral softness rather than a visible third-person body. A wide rectilinear perspective can suggest human field of view without fisheye distortion. For video, synchronize gaze shifts with sound or action cues and let focus…

**Common mistakes.**
- Showing the observing character in the same frame, which breaks the claim that the image is their exact view.
- Adding exaggerated fisheye curvature that reads as an action camera rather than ordinary subjective vision.
- Using random head sway without a target, making the viewpoint nauseating instead of emotionally identified with a character.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | **null** | kling-1.5 | no |
| `luma` Luma Dream Machine | **null** | dream-machine | no |
| `mj61` Midjourney v6.1 | **null** | v6.1 | no |
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | **null** | gen-3-alpha | no |
| `sora` OpenAI Sora | **null** | sora-1 | no |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `graze-face-tour`, 150f

**Sources.** [50+ Types of Camera Shots, Angles, and Techniques](None)


### pull-out

**"Pull Out Prompt for AI Image & Video"** · `camera-work` · level intermediate

```
Pull-out shot beginning tight on [Subject] then slowly withdrawing to reveal the true scale of their surroundings, the shot transitioning from intimacy to cosmic isolation in one continuous movement, shot on 24mm wide-angle lens mounted on a telescoping jib arm, the scale expanding to swallow the individual
```

The camera physically moves away from the subject, revealing more of the environment, often used to create a sense of isolation, revelation, or to transition from intimate to epic scale. The final pull-out of "The Truman Show" — revealing that Truman's entire world is a television set — is a defining use of the technique. Steven Spielberg's pull-out in "Schindler's List" from Oskar Schindler to r…

**When to use.** Choose a pull-out when new context should reframe an intimate moment. Moving away can reveal a crowd, set, landscape, aftermath, or barrier that changes the subject's meaning and makes them feel isolated. It works for endings, revelations, and transitions from personal to epic scale. The wider info…

**Directing the AI.** Start tightly enough to read the subject's expression, then move the camera physically backward in one continuous path. Let foreground objects enter and background architecture expand through visible parallax, gradually reducing the person inside the composition. Use a wide perspective only as space opens, not as a sudden lens jump. Specify the final revealed element and maintain the subject's sc…

**Common mistakes.**
- Revealing nothing consequential beyond the original frame, so the withdrawal changes size but not meaning.
- Shrinking the subject through a zoom alone, missing the foreground parallax that makes physical retreat convincing.
- Losing the subject behind newly revealed objects before the audience can compare them with the larger environment.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | **null** | kling-1.5 | no |
| `luma` Luma Dream Machine | **null** | dream-machine | no |
| `mj61` Midjourney v6.1 | **null** | v6.1 | no |
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | **null** | gen-3-alpha | no |
| `sora` OpenAI Sora | **null** | sora-1 | no |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `drone-dive-landing` (space-camera-moves), 150f, `exploded-view` (space-camera-moves), 150f

**Sources.** [50+ Types of Camera Shots, Angles, and Techniques](None)


### push-in

**"Push In Prompt for AI Image & Video"** · `camera-work` · level intermediate

```
Imperceptibly slow push-in toward [Subject], the camera beginning in a medium shot and gradually closing to a medium close-up, the push-in so gradual viewers may not consciously register the camera moving yet feel the emotional walls closing in, shot on a 50mm Cooke Speed Panchro vintage lens with gentle focus breathing, Kodak 5219 warmth
```

A slow, deliberate camera movement toward the subject, physically closing distance to intensify focus and emotional weight, drawing the audience deeper into a moment or realization. Jonathan Demme's slow push-in to Clarice Starling's face during her final conversation with Hannibal Lecter in "Silence of the Lambs" is a masterclass in the technique. Kubrick used glacial push-ins toward Jack Nichol…

**When to use.** Use a push-in when a realization, decision, threat, or confession grows more important while the shot continues. Physical camera movement narrows the viewer's world and can create pressure before they consciously notice why. It suits patient drama better than abrupt surprise. Define what changes du…

**Directing the AI.** Begin at a clear medium distance and move the camera slowly toward a medium close-up while keeping the lens perspective consistent. The background should shift through natural parallax, proving physical travel rather than a digital zoom. Use gentle vintage focus breathing and warm restrained color, but keep the subject's eyes steadily sharp. Time the approach to a specific thought or line, ending…

**Common mistakes.**
- Changing focal length without camera travel, producing a zoom that lacks the spatial pressure of a true push-in.
- Moving too quickly for a quiet realization, announcing the emotion before the performance has time to develop.
- Starting already too tight, leaving no meaningful distance for the camera to close during the beat.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | **null** | kling-1.5 | no |
| `luma` Luma Dream Machine | **null** | dream-machine | no |
| `mj61` Midjourney v6.1 | **null** | v6.1 | no |
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | **null** | gen-3-alpha | no |
| `sora` OpenAI Sora | **null** | sora-1 | no |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `bullet-time-freeze-orbit` (tension-camera-moves), 150f, `dutch-roll-to-level` (tension-camera-moves), 150f, `pull-back-isolation` (tension-camera-moves), 150f, `slow-push-in` (tension-camera-moves), 150f

**Sources.** [50+ Types of Camera Shots, Angles, and Techniques](None)


### rack-focus

**"Rack Focus Prompt for AI Image & Video"** · `camera-work` · level intermediate

```
Rack focus shot with [Subject] transitioning between sharp foreground detail and resolved background, the focus pull taking a full two seconds, layers of creamy circular bokeh in the defocused plane, shot on a vintage Canon K35 lens wide open at T1.4 for maximum separation between planes, the shallow depth of field turning focus itself into a storytelling instrument
```

A deliberate shift of focus from one subject to another within the same shot, redirecting audience attention without cutting and creating elegant visual transitions between foreground and background. Orson Welles and cinematographer Gregg Toland pioneered deep focus techniques in "Citizen Kane," but the deliberate rack focus became an expressive tool through the work of cinematographers like Vilm…

**When to use.** Use rack focus when two subjects share one composition but audience attention must transfer between them. A foreground clue can sharpen before a background reaction, or a speaking character can give way to someone listening behind them. The move preserves spatial continuity while changing narrative…

**Directing the AI.** Stage one subject close to the lens and another clearly separated in the background. Begin with only the first plane sharp, then pull focus smoothly over about two seconds until the second resolves and the first falls into creamy bokeh. Use a fast vintage lens and keep camera position fixed so focus itself performs the edit. Define the trigger for the shift, such as a sound, glance, or revealed o…

**Common mistakes.**
- Placing both subjects on nearly the same depth plane, leaving too little optical separation for a visible transition.
- Changing camera framing during the pull, which competes with focus and obscures where attention should land.
- Racking back and forth without narrative triggers, reducing an elegant redirection into distracting focus hunting.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | **null** | kling-1.5 | no |
| `luma` Luma Dream Machine | **null** | dream-machine | no |
| `mj61` Midjourney v6.1 | **null** | v6.1 | no |
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | **null** | gen-3-alpha | no |
| `sora` OpenAI Sora | **null** | sora-1 | no |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `dolly-zoom-real` (depth-layer-moves), 150f, `multiplane-real` (depth-layer-moves), 150f

**Sources.** [50+ Types of Camera Shots, Angles, and Techniques](None)


### slow-motion

**"Slow Motion Prompt for AI Image & Video"** · `camera-work` · level basic

```
Slow motion capture at 240fps of [Subject] suspended in a single stretched moment, dust particles hanging motionless in shafts of light, every fine detail frozen in crystalline clarity, shot on Phantom Flex4K high-speed camera with Zeiss Master Prime glass, time stretched until a single second becomes an eternity of beauty
```

Footage captured at a higher frame rate than playback speed, stretching time to reveal details invisible at normal speed and amplifying impact, beauty, or emotional weight of a moment. Sam Peckinpah revolutionized screen violence with the slow-motion bloodbath of "The Wild Bunch," making destruction simultaneously beautiful and horrifying. The Wachowskis' "bullet time" in "The Matrix" became a cu…

**When to use.** Apply slow motion when a brief action contains detail or emotional weight that normal speed would hide. Impacts, fabric movement, water, dust, a fall, or a tiny facial response can become readable and monumental. It can make violence beautiful, grief suspended, or athletic motion analytical. Reserv…

**Directing the AI.** Choose one action and describe it as high-frame-rate capture played back slowly, with a clear beginning, peak, and release. Ask for crisp micro-detail in particles, hair, fabric, or debris while allowing natural directional blur on the fastest edges. Keep the camera move simpler than the subject action. State the perceived duration so one second expands meaningfully rather than freezing. Lighting…

**Common mistakes.**
- Slowing an action with no hidden detail or emotional turning point, making the sequence feel padded rather than heightened.
- Removing all motion blur and producing a brittle sequence of frozen poses instead of continuous high-speed capture.
- Combining extreme slow motion with elaborate camera movement that distracts from the physical event being examined.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: pan_right | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: smooth_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: smooth_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `freeze-annotate-real` (speed-ramp-freeze), 40f, `graze-face-tour`, 150f, `speed-ramp-real` (speed-ramp-freeze), 40f

**Sources.** [50+ Types of Camera Shots, Angles, and Techniques](None)


### static-shot

**"Static Shot Prompt for AI Image & Video"** · `camera-work` · level basic

```
Perfectly static locked-off shot of [Subject], the camera absolutely motionless on a heavy tripod, every element placed with obsessive precision, the stillness of the camera making the frame feel like a living painting, shot on ARRI Alexa with a 40mm Zeiss Master Prime at T5.6 for maximum sharpness edge to edge, Wes Anderson palette, the deadpan humor of perfect order
```

A completely locked-off shot with no camera movement, forcing the composition to do all the work — the deliberate stillness can create contemplation, comedy through staging, or unsettling tension. Yasujiro Ozu built an entire cinematic philosophy around the static shot, his "pillow shots" of empty rooms and corridors in "Tokyo Story" becoming meditations on impermanence. Wes Anderson's rigorously…

**When to use.** Choose a static shot when stillness should make viewers study composition, duration, and behavior inside the frame. It suits deadpan comedy, domestic routine, architectural order, contemplation, and tension created by waiting. With no camera movement to manufacture emphasis, blocking and timing bec…

**Directing the AI.** Lock the camera to a heavy tripod and prohibit pan, tilt, zoom, drift, or stabilization sway. Arrange every object and figure with precise spacing, strong verticals, and enough depth for movement within the composition. Use edge-to-edge clarity and a controlled palette so small changes register. For video, choreograph entrances, exits, gestures, or background events while the frame remains absolu…

**Common mistakes.**
- Adding subtle automated push or handheld drift, which breaks the formal stillness even when movement is barely visible.
- Treating locked camera as permission for weak composition, leaving no internal lines, depth, or staged action to inspect.
- Centering every subject mechanically when asymmetry or offscreen pressure would create stronger tension within the fixed frame.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | **null** | kling-1.5 | no |
| `luma` Luma Dream Machine | **null** | dream-machine | no |
| `mj61` Midjourney v6.1 | **null** | v6.1 | no |
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | **null** | gen-3-alpha | no |
| `sora` OpenAI Sora | **null** | sora-1 | no |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `basic-3d-scene`, 180f

**Sources.** [50+ Types of Camera Shots, Angles, and Techniques](None)


### steadicam

**"Steadicam Prompt for AI Image & Video"** · `camera-work` · level advanced

```
Steadicam tracking shot floating smoothly behind [Subject] through shifting environments, the preternatural smoothness creating a floating predatory presence, shot on Arriflex 35BL with Zeiss Standard Speed lenses, the shifting light temperatures from warm tungsten through cool fluorescent creating a living color journey
```

A stabilized camera rig worn by the operator that produces smooth, floating movement while following subjects through complex environments, combining the fluidity of dolly work with the freedom of handheld. Invented by Garrett Brown, the Steadicam was first showcased in "Rocky" (1976) running up the Philadelphia Museum steps, then immortalized by Stanley Kubrick in "The Shining" — the relentless…

**When to use.** Use Steadicam movement when a character must travel through complex space without the vibration of handheld or the track-bound feel of a dolly. It suits corridor journeys, entrances, crowd navigation, and scenes where the camera becomes a calm companion or predator. The floating continuity can buil…

**Directing the AI.** Have the camera float behind, beside, or ahead of the subject at a constant human walking distance. Describe smooth turns, level horizons, gentle acceleration, and deliberate passage through doorways or changing environments. Let practical color temperatures shift naturally as the route moves from warm tungsten into cool fluorescent light. Keep footstep bounce suppressed but not robotic. Define t…

**Common mistakes.**
- Making the move perfectly frictionless, which can feel disembodied instead of like a skilled operator moving through space.
- Failing to define the route, causing doors, walls, and extras to change unpredictably during the generated movement.
- Adding handheld jolts for excitement, undermining the smooth floating continuity that distinguishes Steadicam work.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | **null** | kling-1.5 | no |
| `luma` Luma Dream Machine | **null** | dream-machine | no |
| `mj61` Midjourney v6.1 | **null** | v6.1 | no |
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | **null** | gen-3-alpha | no |
| `sora` OpenAI Sora | **null** | sora-1 | no |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `graze-face-tour`, 150f

**Sources.** [50+ Types of Camera Shots, Angles, and Techniques](None)


### three-shot

**"Three-Shot Prompt for AI Image & Video"** · `camera-work` · level intermediate

```
Three-shot of [Subject] arranged in a triangular composition across the widescreen frame, each occupying their own third, the triangular formation revealing tension between completely different energies colliding at a single point, shot on anamorphic 50mm with the wide frame emphasizing space between the three figures
```

A shot framing three subjects, often used to show group dynamics, alliances, or the odd-one-out tension within a trio. Sergio Leone perfected the three-shot in the climactic standoff of "The Good, the Bad and the Ugly," cycling between three armed men in a graveyard to create one of cinema's most iconic compositions. Akira Kurosawa uses triangular three-shots in "Rashomon" to stage conflicting te…

**When to use.** Choose a three-shot when the drama comes from a trio rather than three separate characters. Triangular placement can reveal two against one, a mediator caught between rivals, or unstable alliances that change inside the scene. It suits standoffs, negotiations, comedy, and family tension. Avoid lini…

**Directing the AI.** Place three subjects at distinct points of a triangle across the widescreen frame, varying depth or height to establish hierarchy. Give each person a readable eyeline and body orientation toward or away from the others. Keep the spaces between them clear so alliance and exclusion can shift through movement. Use an anamorphic field without crowding the edges. In video, specify the gesture or step…

**Common mistakes.**
- Arranging the trio in a flat shoulder-to-shoulder row, which hides alliances and makes the composition feel posed.
- Giving all three characters equal visual weight when the scene depends on one person being isolated or dominant.
- Allowing eyelines to point randomly, making the characters appear disconnected from the conversation or standoff.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | **null** | kling-1.5 | no |
| `luma` Luma Dream Machine | **null** | dream-machine | no |
| `mj61` Midjourney v6.1 | **null** | v6.1 | no |
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | **null** | gen-3-alpha | no |
| `sora` OpenAI Sora | **null** | sora-1 | no |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `drone-dive-landing` (space-camera-moves), 150f, `exploded-view` (space-camera-moves), 150f

**Sources.** [50+ Types of Camera Shots, Angles, and Techniques](None)


### tilt-shot

**"Tilt Shot Prompt for AI Image & Video"** · `camera-work` · level basic

```
Slow tilt shot beginning at the feet of [Subject] and climbing vertically up their body, the deliberate vertical scan building anticipation, each detail telling the character's story before the face is revealed, shot on 85mm telephoto compressing the vertical layers, Kodak Vision3 500T with cool overcast color rendition
```

A vertical rotation of the camera on a fixed axis, tilting up or down to reveal height, scan a character from feet to face, or follow vertical action. Hitchcock used the slow tilt masterfully in "Psycho," tilting up the facade of the Bates house to establish its Gothic menace. Spielberg opens "Jurassic Park" with a slow tilt up the Brachiosaurus that mirrors the characters' awe, and Christopher N…

**When to use.** Use a tilt when attention needs to travel vertically while the camera stays in place. A slow rise from boots to face can delay identity; a move up a facade can establish intimidating height; a downward tilt can reveal danger, evidence, or a body below. The start and finish should form a meaningful…

**Directing the AI.** Fix the camera on its support and specify a vertical rotation upward or downward with no lateral travel. Name the starting detail, the visual information encountered during the move, and the final reveal. A telephoto perspective can compress stacked details during a character scan, while steady speed builds anticipation. Keep horizontal framing stable and avoid roll. For video, let the tilt resol…

**Common mistakes.**
- Confusing tilt with raising the camera, which changes viewpoint and parallax instead of rotating on a fixed axis.
- Starting and ending on unrelated details, leaving the vertical scan with no dramatic logic or visual payoff.
- Tilting too fast for costume, architecture, or environmental clues to register before the final reveal.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | **null** | kling-1.5 | no |
| `luma` Luma Dream Machine | **null** | dream-machine | no |
| `mj61` Midjourney v6.1 | **null** | v6.1 | no |
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | **null** | gen-3-alpha | no |
| `sora` OpenAI Sora | **null** | sora-1 | no |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `steep-tilt-glide`, 120f

**Sources.** [50+ Types of Camera Shots, Angles, and Techniques](None)


### tracking-shot

**"Tracking Shot Prompt for AI Image & Video"** · `camera-work` · level intermediate

```
Lateral tracking shot following [Subject] at shoulder height, the camera keeping perfect pace on a parallel track, smooth parallax separation between foreground, mid-ground, and background layers, shot on 35mm Kodak Vision3 250D with a 40mm Panavision Primo lens, the rhythmic steady accompaniment of a camera that walks with its subject
```

The camera moves alongside, behind, or in front of a moving subject, maintaining a consistent spatial relationship to create a sense of journey, pursuit, or accompaniment. Jean-Luc Godard's famous lateral tracking shot in "Weekend" follows a traffic jam for nearly ten unbroken minutes. Andrei Tarkovsky's tracking shots in "Stalker" move with hypnotic slowness through the Zone, while Alfonso Cuaró…

**When to use.** Use a tracking shot when movement through a place is part of the story: pursuit, discovery, routine, escape, or procession. Unlike a pan, the camera changes position. The move can make the audience accompany a subject, expose an environment progressively, or hold tension without cutting.

**Directing the AI.** Define whether the camera leads, follows, or travels beside the subject; then state height, distance, speed, and what remains locked in frame. Give the model foreground objects to cross and background depth to reveal. For longer generations, keep the action simple and continuous so identity, direction, and geography have fewer chances to drift.

**Common mistakes.**
- Writing "tracking shot" without saying where the camera is in relation to the subject.
- Confusing a fixed-axis pan with physical travel through the scene.
- Combining a complex camera path with multiple character actions and environment changes in one short generation.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | **null** | kling-1.5 | no |
| `luma` Luma Dream Machine | **null** | dream-machine | no |
| `mj61` Midjourney v6.1 | **null** | v6.1 | no |
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | **null** | gen-3-alpha | no |
| `sora` OpenAI Sora | **null** | sora-1 | no |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `cursor-flyover`, 180f, `drone-dive-landing` (space-camera-moves), 150f, `exploded-view` (space-camera-moves), 150f

**Sources.** [What is a Tracking Shot? Definition and Examples](None)


### two-shot

**"Two-Shot Prompt for AI Image & Video"** · `camera-work` · level basic

```
Two-shot of [Subject] framed together, their bodies creating complementary angles, the space between them charged with everything said and unsaid, shot on a 50mm Summilux at f/1.4 with gentle background blur, Kodak Portra 400 color rendition with soft warm midtones, the quiet eloquence of two figures in shared space
```

A shot framing exactly two subjects, showing their spatial and emotional relationship, essential for establishing dynamics between characters in conversation, confrontation, or intimacy. Billy Wilder was a master of the two-shot, using it in "The Apartment" and "Some Like It Hot" to capture the chemistry of his actors. Before Midnight director Richard Linklater builds entire films from two-shots…

**When to use.** Use a two-shot when the relationship between two people matters more than either individual performance alone. Shared framing exposes attraction, alliance, rivalry, distance, and changes in who controls the space. It works for conversation, walking dialogue, confrontation, and silent intimacy. Move…

**Directing the AI.** Frame exactly two subjects with both faces and body angles legible. Use their spacing, height, orientation, and shared eyeline to express the relationship before dialogue begins. A normal lens and gentle background separation keep the scene intimate without erasing context. Leave the gap between them visible; it carries emotional weight. For video, choreograph who closes, crosses, or withdraws fr…

**Common mistakes.**
- Treating both figures as independent portraits, with no eyeline, gesture, or spatial tension connecting them.
- Cropping one subject at an awkward edge, making the second person feel accidental rather than compositionally equal.
- Using background blur so heavy that the shared environment no longer contributes to their relationship.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | **null** | kling-1.5 | no |
| `luma` Luma Dream Machine | **null** | dream-machine | no |
| `mj61` Midjourney v6.1 | **null** | v6.1 | no |
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | **null** | gen-3-alpha | no |
| `sora` OpenAI Sora | **null** | sora-1 | no |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `drone-dive-landing` (space-camera-moves), 150f, `exploded-view` (space-camera-moves), 150f

**Sources.** [50+ Types of Camera Shots, Angles, and Techniques](None)


### vertigo-effect

**"Vertigo Effect Prompt for AI Image & Video"** · `camera-work` · level advanced

```
Vertigo effect dolly zoom on [Subject] locked in frame while the background warps and telescopes away in a nauseating spatial contradiction, the zoom and dolly counter-movement perfectly synchronized, desaturated palette with sickly yellow-green undertones, shot on anamorphic glass, Hitchcock's visual language of psychological vertigo made manifest
```

Also called a dolly zoom — the camera dollies in while zooming out (or vice versa), causing the background to warp while the subject stays the same size, creating a visceral sense of disorientation. Invented by cameraman Irmin Roberts for Alfred Hitchcock's "Vertigo" (1958) to visualize James Stewart's acrophobia, the technique was later used to devastating effect by Steven Spielberg in "Jaws" —…

**When to use.** Deploy the vertigo effect at a moment of shock, dread, realization, or altered perception. The subject stays the same size while the world behind them telescopes, making stable space feel suddenly impossible. It works when psychology and environment must collide in one mechanical move. Because the…

**Directing the AI.** Lock the subject's size and central position throughout the shot. Move the camera physically inward while zooming outward, or reverse both actions, with perfect counter-synchronization. The foreground face should remain stable as background distance stretches or compresses visibly along strong depth lines. Use a desaturated palette with sickly yellow-green undertones and restrained anamorphic tex…

**Common mistakes.**
- Allowing the subject to grow during the move, which turns the setup into an ordinary zoom or dolly approach.
- Choosing a flat background with no depth lines, leaving little visible space for the contradiction to warp.
- Using the effect repeatedly, so a powerful psychological rupture becomes a predictable transition between ordinary shots.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | **null** | kling-1.5 | no |
| `luma` Luma Dream Machine | **null** | dream-machine | no |
| `mj61` Midjourney v6.1 | **null** | v6.1 | no |
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | **null** | gen-3-alpha | no |
| `sora` OpenAI Sora | **null** | sora-1 | no |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `crash-impact-real` (crash-zoom-punch), 11f, `crash-zoom-real` (crash-zoom-punch), 11f, `steep-tilt-glide`, 120f

**Sources.** [50+ Types of Camera Shots, Angles, and Techniques](None)


### whip-pan

**"Whip Pan Prompt for AI Image & Video"** · `camera-work` · level intermediate

```
Whip pan snapping to [Subject], heavy horizontal motion blur streaking the environment into abstract ribbons of color, the blur lasting just three frames before resolving into razor sharpness, shot on high-speed camera with a 35mm Zeiss Master Prime, raw visceral kinetic energy
```

An extremely fast horizontal pan that creates motion blur, used as a dynamic transition or to convey sudden surprise, rapid shifts of attention, or frenetic energy. Edgar Wright made the whip pan his comedic signature in "Shaun of the Dead," "Hot Fuzz," and "Baby Driver," using them as rapid-fire visual punchlines. Sam Raimi employed frantic whip pans in the "Evil Dead" trilogy to convey demonic…

**When to use.** Choose a whip pan for a sudden shift of attention, a visual punchline, an impact, or a high-energy transition between connected spaces. Its brief blur can hide a cut or compress the distance between subjects. The destination must justify the snap. Use it as punctuation inside controlled coverage; c…

**Directing the AI.** Define the sharp starting frame and an equally sharp landing frame on a second subject. Snap the camera horizontally between them, allowing only a few frames of heavy directional streaking before the image resolves. Keep blur aligned with the movement rather than radial or random. Match subject height and motion direction if the pan masks a transition. Hold briefly after landing. The move should…

**Common mistakes.**
- Leaving the endpoint vague, causing the camera to stop on empty space or a subject that never resolves sharply.
- Applying blur before and after the movement, which removes the crisp contrast that gives a whip pan impact.
- Using radial zoom streaks instead of horizontal motion blur, confusing the technique with a crash zoom.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: pan_right | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: smooth_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: smooth_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `bullet-time-freeze-orbit` (tension-camera-moves), 150f, `dutch-roll-to-level` (tension-camera-moves), 150f, `pull-back-isolation` (tension-camera-moves), 150f, `slow-push-in` (tension-camera-moves), 150f

**Sources.** [50+ Types of Camera Shots, Angles, and Techniques](None)


### worms-eye-view

**"Worm's Eye View Prompt for AI Image & Video"** · `camera-work` · level intermediate

```
Worm's eye view from ground level looking straight up at [Subject], the perspective so extreme that vertical elements seem to lean inward and threaten to collapse, shot from a camera placed directly on the ground with a 14mm ultra-wide rectilinear lens pointed straight up, the barrel distortion adding to the vertiginous effect, the overwhelming scale from the perspective of the smallest creature
```

Camera placed at ground level looking straight up, the most extreme low angle, making everything tower above and creating a sense of awe, intimidation, or childlike wonder. Orson Welles was famous for his low-angle work in "Citizen Kane" and "The Trial," often requiring sets to be built with ceilings — unusual for the era. Terry Gilliam employs worm's eye views in "Brazil" and "12 Monkeys" to mak…

**When to use.** Choose a worm's eye view when the camera should occupy the smallest possible position beneath something immense. Looking almost straight up can make a building, creature, vehicle, or person feel oppressive, astonishing, or childishly wondrous. It is more extreme than a normal low angle and strongly…

**Directing the AI.** Place the lens directly on the ground and aim nearly straight upward. Use an ultra-wide rectilinear perspective so vertical structures surge inward toward the sky while remaining recognizably architectural. Include a small ground-edge reference for scale and position the subject above or around the lens, not merely in front of it. Control barrel distortion rather than letting it dominate. In vide…

**Common mistakes.**
- Positioning the camera around waist height, which produces an ordinary low angle without the creature-level viewpoint.
- Aiming forward instead of upward, losing the collapsing verticals and overhead dominance central to the technique.
- Letting ultra-wide distortion bend every line randomly, turning controlled vertigo into an unreadable fisheye effect.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | **null** | kling-1.5 | no |
| `luma` Luma Dream Machine | **null** | dream-machine | no |
| `mj61` Midjourney v6.1 | **null** | v6.1 | no |
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | **null** | gen-3-alpha | no |
| `sora` OpenAI Sora | **null** | sora-1 | no |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `steep-tilt-glide`, 120f

**Sources.** [50+ Types of Camera Shots, Angles, and Techniques](None)


### ambient-light

**"Ambient Light Prompt for AI Image & Video"** · `lighting` · level basic

```
Ambient light only on [Subject], the existing institutional or natural illumination providing the sole source, no dramatic shadows or cinematic enhancement, the honest unmanipulated light of a real place at a real time, shot on a fast lens wide open to handle the lower light levels, documentary naturalism where the space itself determines the visual mood
```

The existing, non-directional light present in an environment before any additional lighting is added, the base layer of illumination that sets the overall brightness and mood. Frederick Wiseman's documentaries like "Titicut Follies" and "High School" rely entirely on ambient light to maintain observational authenticity. The Dardenne brothers shoot their fiction films in ambient conditions to pre…

**When to use.** Choose ambient light when the location's existing brightness and color should define the scene before any dramatic intervention. It suits documentary observation, institutional spaces, overcast exteriors, offices, forests, and other environments with broad non-directional illumination. Ambient ligh…

**Directing the AI.** Describe the environment as the source: cool overcast sky, warm office ceiling glow, or green light filtered through a canopy. Keep illumination broad and low in directionality, with restrained contrast and no unexplained rim or spotlight. Allow slight color contamination and uneven exposure where the real space would produce it. Maintain readable detail without turning the scene glossy. For vide…

**Common mistakes.**
- Adding dramatic key and rim lights while calling the result ambient, which contradicts the technique's environmental base layer.
- Neutralizing every location tint, removing the blue, green, or warm cast that makes the existing light specific.
- Making ambient illumination perfectly uniform, even where walls, ceilings, windows, or foliage should create visible variation.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `brand-ink-open`, 83f

**Sources.** [Film Lighting](None)


### available-light

**"Available Light Prompt for AI Image & Video"** · `lighting` · level intermediate

```
Available light on [Subject] with no additional movie lighting, illuminated purely by existing natural or practical sources, the honest imperfection of real light creating slightly uneven exposure, shot on an extremely fast lens at f/0.95 to capture the low ambient levels, the discipline of working with only what nature and architecture provide, Barry Lyndon austerity
```

Shooting with only the light naturally present in the location — no artificial movie lights added — creating an authentic, documentary quality that requires careful exposure management. Kubrick's "Barry Lyndon" is the most famous example, shot entirely by candlelight and window light using a modified NASA f/0.7 Zeiss lens. Emmanuel Lubezki committed to available light for Terrence Malick's "The N…

**When to use.** Available light is the disciplined choice when added movie lighting would disturb a location's truth, performance, or natural rhythm. Use it for documentary realism, candlelit rooms, window-lit interiors, and exterior scenes tied to a specific time of day. The look should retain slight exposure imb…

**Directing the AI.** List only sources that physically exist in the location, such as a window, candle, ceiling fixture, or open sky. Place the subject where those sources can reach them and accept controlled darkness elsewhere. Ask for a fast-lens feel, gentle highlight rolloff, and small exposure imperfections rather than polished studio balance. Do not introduce invisible fill. In video, keep brightness changes ti…

**Common mistakes.**
- Sneaking in a perfect frontal fill or rim that has no existing source, undermining the available-light constraint.
- Demanding clean exposure in every corner, which removes the honest limitations and hierarchy of the location's illumination.
- Ignoring the subject's position relative to windows or practicals, then compensating with impossible light that follows them.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `letterspace-materialize`, 15f

**Sources.** [Film Lighting](None)


### backlight

**"Backlight Prompt for AI Image & Video"** · `lighting` · level basic

```
Backlit [Subject] with brilliant rim of white-gold light tracing every contour, hair transformed into a luminous halo of individually backlit strands, atmospheric dust and particles lit up like a galaxy of floating stars, god rays streaming past the figure, shot on a Cooke S4 with gentle halation on the overexposed highlights, the ethereal separation of backlight turning form into something divine
```

Light positioned behind the subject, creating a rim of light around their edges that separates the subject from the background and adds a halo-like, ethereal quality. Emmanuel Lubezki is the modern master of backlighting, using natural backlight in "The Revenant" and "The Tree of Life" to create an almost divine luminosity around his subjects. Vittorio Storaro's backlighting in "The Last Emperor"…

**When to use.** Backlight is right when a subject must separate from a dark or visually busy background, or when the scene needs an ethereal halo. It performs especially well with hair, smoke, dust, rain, translucent fabric, and atmospheric haze. Use it for arrivals, memory fragments, spiritual imagery, or silhoue…

**Directing the AI.** Position the strongest source behind the subject and slightly above frame level. Describe a white-gold rim tracing shoulders, hair, and profile while particles in the air catch narrow beams. Let highlights bloom gently, but keep edge shape intact rather than washing the whole frame. State whether the face stays silhouetted or receives restrained frontal detail. In motion, maintain convincing occl…

**Common mistakes.**
- Applying an even glowing outline around every edge, including surfaces the rear source could not physically reach.
- Overexposing the background and rim together until the subject loses its silhouette instead of gaining clear separation.
- Ignoring atmosphere and surface response, which turns potentially luminous light into a thin digital-looking stroke around the figure.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `spotlight-hero-card`, 220f

**Sources.** [Film Lighting](None)


### blue-hour

**"Blue Hour Prompt for AI Image & Video"** · `lighting` · level intermediate

```
Blue hour twilight twenty minutes after sunset enveloping [Subject], the sky a luminous deep cobalt blue glowing from within, warm amber artificial light sources contrasting with the pervasive blue atmosphere, shot on Alexa at high ISO with Cooke S4 glass rendering practical lights as soft warm glows, the contemplative melancholy of Michael Mann's visual language
```

The cool, diffused light just before sunrise or after sunset when the sky turns deep blue, creating a melancholic, contemplative, or mysterious atmosphere. Michael Mann is the master of blue hour photography, using the transitional twilight extensively in "Heat," "Collateral," and "Miami Vice" to create his signature cool urban melancholy. Janusz Kamiński shot the D-Day sequence in "Saving Privat…

**When to use.** Use blue hour for transitional scenes that need cool calm, loneliness, anticipation, or mystery without full darkness. The luminous sky keeps exterior detail visible while windows, streetlights, and vehicles begin to glow warm. It suits city arrivals, departures, reflective portraits, and quiet sus…

**Directing the AI.** Set the moment roughly twenty minutes after sunset or before sunrise, when the sky is deep cobalt but still luminous. Let cool ambient light wrap buildings and faces while warm amber practicals punctuate windows, signs, or vehicles. Use high sensitivity with soft halation around those sources, preserving detail in both sky and shadow. For video, hold the narrow twilight state consistently; do not…

**Common mistakes.**
- Making the sky completely black, which turns the scene into night and removes blue hour's luminous transition.
- Adding direct orange sunlight even though the sun has already dropped below the horizon in the intended setup.
- Coloring skin and every object uniformly blue, instead of balancing cool ambience with selective warm practical sources.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `letterspace-materialize`, 15f

**Sources.** [Film Lighting](None)


### bounce-light

**"Bounce Light Prompt for AI Image & Video"** · `lighting` · level intermediate

```
Bounce light wrapping gently around [Subject], light reflected off a nearby surface creating soft warm illumination with no discernible directional shadow, the walls themselves becoming luminous secondary sources, shot on Alexa with Cooke S7 lenses for gentle roll-off into highlights, the naturalistic invisible lighting that Sven Nykvist spent a lifetime perfecting, light that serves the subject without announcing itself
```

Light reflected off a surface — wall, ceiling, or reflector — before hitting the subject, creating a soft, indirect illumination with a natural quality. Sven Nykvist perfected bounce lighting for Ingmar Bergman, often bouncing light off white ceilings and walls in "Cries and Whispers" to create his celebrated naturalistic look. Roger Deakins frequently bounces light off muslin and bead board to c…

**When to use.** Use bounce light for interiors and portraits that should feel naturally illuminated without an obvious movie source. It is ideal when direct light looks harsh, creates unwanted shadows, or breaks the location's realism. Bouncing can turn a wall, ceiling, or reflector into a large source that wraps…

**Directing the AI.** Name the original source and the surface it strikes before reaching the subject. Ask for a broad return from a nearby pale wall or ceiling, with gentle wrap and no hard directional shadow. The bounce should inherit a subtle warmth or color cast from that surface, not appear perfectly neutral by default. Preserve a believable falloff across the room. For moving scenes, keep the indirect source anc…

**Common mistakes.**
- Describing soft light without identifying a reflecting surface, leaving the illumination direction arbitrary and spatially unconvincing.
- Bouncing from a strongly colored wall while asking for neutral skin, creating a contradiction in the scene's light behavior.
- Making every corner equally bright, which removes the natural falloff that gives indirect illumination its believable spatial depth.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `spotlight-hero-card`, 220f

**Sources.** [Film Lighting](None)


### broad-lighting

**"Broad Lighting Prompt for AI Image & Video"** · `lighting` · level basic

```
Broad lighting on [Subject] with the key illuminating the wider camera-facing side, creating an open and warm appearance with minimal shadow visible, the widening effect making the face appear fuller and more inviting, a soft box key with matching soft fill creating low contrast, shot on an 85mm lens at f/4, the even clean illumination of a romantic comedy close-up, Kodak Portra-inspired warm skin rendition
```

The side of the face turned toward the camera receives the key light, widening the apparent face shape and creating a brighter, more open look. Broad lighting is commonly used in comedy and romantic genres where an open, welcoming quality is desired. Classic Hollywood glamour photographers like Clarence Sinclair Bull used broad lighting for approachable star portraits. In cinema, broad lighting i…

**When to use.** Use broad lighting when a portrait should feel open, warm, accessible, or gently flattering rather than secretive. It works well for comedy, romance, interviews, and dialogue where facial information needs to arrive without friction. Because the wider camera-facing side receives the key, the face a…

**Directing the AI.** Turn the subject slightly away from camera, then place the key so it illuminates the broader face plane still visible to the viewer. Use a large soft source and restrained fill, keeping only a narrow shadow on the far side. Maintain warm skin and open eyes without flattening every contour. The camera-facing cheek should carry the brightest area. Across video coverage, preserve the subject's turn…

**Common mistakes.**
- Lighting the narrow far cheek instead of the broad camera-facing plane, accidentally creating the opposite portrait pattern.
- Filling every facial shadow to the same value, turning an open look into flat, directionless illumination.
- Using broad lighting for a scene built on concealment, where its welcoming clarity works against the intended tension.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `spotlight-hero-card`, 220f

**Sources.** [Film Lighting](None)


### chiaroscuro

**"Chiaroscuro Prompt for AI Image & Video"** · `lighting` · level advanced

```
Chiaroscuro lighting on [Subject] with a single candle or flame as the only source, warm amber light painting face and hands while everything beyond arm's reach vanishes into absolute blackness, the contrast ratio approaching infinity, shot to emulate oil painting with a fast 50mm lens wide open, the Caravaggio-meets-Gordon Willis treatment of light as a moral force that reveals and conceals in equal measure
```

An extreme contrast between light and dark, inspired by Renaissance painting, creating deeply sculpted, painterly images with rich shadows and selective illumination. Directly descended from Caravaggio's revolutionary use of tenebrism in paintings like "The Calling of Saint Matthew," chiaroscuro entered cinema through German Expressionism and was perfected by Gordon Willis in "The Godfather" — hi…

**When to use.** Choose chiaroscuro when light and darkness should feel symbolic as well as descriptive. A face emerging from blackness can express divided motives, secrecy, spiritual weight, danger, or revelation. The painterly contrast works for intimate portraits, historical interiors, crime, and solemn drama. I…

**Directing the AI.** Use one candle, flame, or narrow warm source to paint the subject's face and hands while everything beyond immediate reach falls toward absolute black. Shape the light across planes rather than outlining the entire body. Let one eye or side of the face disappear if the emotional idea supports concealment. Preserve rich amber gradation in lit skin and fabric. Keep secondary sources absent or extre…

**Common mistakes.**
- Lighting the background for visual interest, reducing the black field that gives selective illumination its painterly force.
- Using equal split lighting with no tonal gradation, producing a simple half-lit portrait instead of sculpted chiaroscuro.
- Adding several colored sources that fragment the moral clarity of one dominant relationship between light and dark.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `brand-ink-open`, 83f

**Sources.** [Film Lighting](None)


### color-temperature

**"Color Temperature Prompt for AI Image & Video"** · `lighting` · level intermediate

```
Mixed color temperatures on [Subject], the tension between warm 2700K tungsten sources casting golden light and cool 6500K daylight-balanced sources washing in cold sterile tones, the two color worlds meeting on the subject's form, shot on Kodak Vision3 500T balanced for tungsten so warm sources read neutral while daylight goes intensely blue, the visual poetry of mixed color temperatures that maps emotional geography
```

The warmth or coolness of light measured in Kelvin — warm light (orange/amber) suggests comfort and intimacy while cool light (blue) suggests detachment, technology, or night. Steven Soderbergh is a master of deliberate color temperature manipulation, using amber for Mexico and blue-green for the US in "Traffic" to distinguish storylines. Emmanuel Lubezki plays warm and cool temperatures against…

**When to use.** Work with color temperature when emotional geography matters as much as brightness. Warm practicals can hold comfort, memory, or intimacy while cool ambient light suggests night, distance, or technology. Mixed temperatures are useful in doorways, vehicles, city interiors, and scenes where two world…

**Directing the AI.** Define at least two sources by position and color character: a warm tungsten-like lamp near the subject and cooler daylight or night ambience entering from elsewhere. State which side of the face, costume, and environment each one affects. Keep a visible transition between the color zones rather than washing the frame evenly. Neutral objects should reveal the contrast clearly. For video, maintain…

**Common mistakes.**
- Applying orange to skin and teal to every background by habit, without assigning either color to a real source.
- Blending warm and cool illumination into a uniform neutral wash, eliminating the emotional separation between the two zones.
- Changing color direction across adjacent shots, so the same window or lamp appears to migrate around the scene.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `letterspace-materialize`, 15f

**Sources.** [Film Lighting](None)


### cross-lighting

**"Cross Lighting Prompt for AI Image & Video"** · `lighting` · level intermediate

```
Cross-lighting from two opposing sources on [Subject], a warm tungsten source from one side casting amber highlights while a cool blue-white source from the other paints steel tones, the two competing colors meeting in a narrow strip of mixed light, each surface independently sculpted by the dual sources, shot on 35mm Kodak Vision3 500T to handle the mixed color temperatures with richness, a 50mm lens capturing the sculptural dimensionality
```

Two light sources positioned on opposite sides of the subject, creating a complex interplay of highlights and shadows that sculpt form from multiple directions. Ridley Scott used cross-lighting extensively in "Blade Runner" to create the layered, multi-source atmosphere of a neon-drenched dystopia. Michael Mann employs cross-lighting in his nighttime cityscapes, with competing sources from street…

**When to use.** Choose cross lighting when one source cannot explain the layered energy of a night exterior, stage, fashion frame, or neon interior. Opposing sources can carve different surfaces and separate a subject from several directions at once. The technique is especially useful when warm and cool environmen…

**Directing the AI.** Place two sources on opposite sides of the subject. Give one a warm amber character and the other a cooler blue-white tone, then specify which planes each source catches. Keep a narrow transition where the colors meet rather than blending everything into uniform purple. Let the sources cast shadows away from their own directions, with neither behaving like frontal fill. In video, lock both lights…

**Common mistakes.**
- Blending the opposing colors across the entire subject, producing a muddy wash instead of two clearly directed sources.
- Giving both lights equal frontal coverage, which flattens form and defeats the sculptural purpose of cross lighting.
- Ignoring separate shadow directions, making the warm and cool highlights feel decorative rather than physically present in the space.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `spotlight-hero-card`, 220f

**Sources.** [Film Lighting](None)


### dappled-light

**"Dappled Light Prompt for AI Image & Video"** · `lighting` · level intermediate

```
Dappled light filtering through a canopy onto [Subject], dozens of small bright spots and larger soft patches scattered across them in an ever-shifting mosaic, the interplay creating a natural pointillist painting on the surface, the overall light warm and green-shifted from passing through foliage, an 85mm lens at T1.4 turning the background into luminous green bokeh, Kodak Vision3 50D saturated daylight stock, the Malick-Lubezki prayer of natural light
```

Light filtered through trees, blinds, or other semi-transparent objects, creating a pattern of light and shadow across the subject that evokes natural environments and contemplation. Terrence Malick and Emmanuel Lubezki use dappled forest light as an almost religious motif throughout "The New World" and "The Tree of Life," where sunlight through leaves becomes a visual metaphor for divine presenc…

**When to use.** Dappled light works when the environment should leave a living pattern on the subject. Use it beneath foliage, near blinds, behind patterned screens, or anywhere a broken source can suggest contemplation, romance, instability, or a border between worlds. The shifting mosaic adds texture without ext…

**Directing the AI.** Place a hard or moderately focused source behind a specific filter, such as leaves or blinds. Ask for irregular bright patches and softer shadow areas that change size as they cross three-dimensional surfaces. If foliage is the filter, let the light carry a slight warm and green character. Keep the overall exposure coherent beneath the pattern. For video, animate the patches subtly with wind or s…

**Common mistakes.**
- Painting identical circular spots over the whole frame, which ignores the shape, distance, and depth of the filtering material.
- Keeping the projected pattern flat across curved faces and fabric, rather than letting it wrap and distort with form.
- Moving shadows rapidly without moving leaves, blinds, light, or subject, making the scene's illumination physically incoherent.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `icon-field-colorize`, 45f

**Sources.** [Film Lighting](None)


### edge-light

**"Edge Light Prompt for AI Image & Video"** · `lighting` · level intermediate

```
Edge light tracing the complete outline of [Subject] against darkness, a thin bright line following every contour from crown to fingertips, the face and front in complete shadow with no fill, only the bright edge visible, individual hair strands creating a fiber-optic halo effect, shot on a 135mm lens at T2 to compress the background into a seamless void, the cinematic elegance of defining a form by outline alone
```

A thin line of light that traces the outline of a subject, separating them from the background and creating a refined, cinematic look that adds depth and visual polish. Ridley Scott and his frequent cinematographer John Mathieson use edge lighting extensively in "Gladiator" and "Kingdom of Heaven" to make armored warriors pop against dark battle backgrounds. Roger Deakins uses hairline edge light…

**When to use.** Choose edge light when shape matters more than frontal detail, or when a dark subject needs refined separation from a dark background. It is effective for profiles, armor, fashion, music performance, smoke, and restrained sci-fi imagery. A thin contour can make the frame feel polished without expos…

**Directing the AI.** Position a narrow source behind the subject so it grazes the outer contour. Specify which edges catch light, from crown and hair strands to shoulder, arm, or object rim, while the front remains dark or minimally filled. Keep the line thin and brightest where the angle reflects toward camera. Avoid equal intensity around the whole body. In video, let the illuminated contour migrate with rotation,…

**Common mistakes.**
- Drawing a complete uniform outline around the subject, including edges hidden from or facing away from the source.
- Widening the edge until it spills across the face and torso, replacing elegant separation with broad backlighting.
- Using a background equally bright as the rim, which removes the contrast required for clean contour definition.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `spotlight-hero-card`, 220f

**Sources.** [Film Lighting](None)


### eye-light

**"Eye Light Prompt for AI Image & Video"** · `lighting` · level intermediate

```
Eye light close-up of [Subject] with brilliant catchlights sparkling in the irises, a dedicated small source just above the camera creating twin points of reflected light that bring the entire face to life, the subtle difference between eyes with and without this light is the difference between a living portrait and a death mask, shot in close-up on a 100mm macro lens at T2.8, warm golden skin tones, the tiny technical detail that separates professional cinematography from amateur work
```

A small, dedicated light source positioned to create a catchlight — a bright reflection in the subject's eyes — that brings eyes to life and creates a vital connection with the viewer. The eye light has been an essential tool since Hollywood's Golden Age, when cinematographers like Lee Garmes used tiny "inky" lights to add sparkle to Marlene Dietrich's eyes. Eyes without catchlights appear dead o…

**When to use.** Eye light matters in close portraits where the audience must connect with a character's gaze. Use it when the broader lighting leaves the eyes dull, dark, or emotionally absent, especially in dramatic close-ups and reaction shots. A small catchlight can restore presence without changing the rest of…

**Directing the AI.** Place a small dedicated source just above and near the camera axis. Ask for compact, matching catchlights in both visible irises, positioned consistently with the source and shaped by its aperture. Keep the reflections bright but not larger than the pupils, and preserve natural iris texture around them. The eye light should not lift the entire face. For video, lock the reflections to the curved e…

**Common mistakes.**
- Making catchlights huge or perfectly decorative, so the eyes resemble glossy illustrations rather than reflections from a small source.
- Placing different catchlight shapes or directions in each eye, breaking the shared geometry of the lighting setup.
- Brightening the entire face to create eye sparkle, which changes the scene instead of adding one precise reflection.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `spotlight-hero-card`, 220f

**Sources.** [Film Lighting](None)


### fill-light

**"Fill Light Prompt for AI Image & Video"** · `lighting` · level basic

```
Fill light softening the shadows on [Subject], a gentle secondary source creating a 4:1 contrast ratio, the shadow side retaining detail and color rather than falling to black, the fill large and diffused so it wraps without creating competing shadows, shot on 35mm Kodak Vision3 with a 65mm lens, the nuanced lighting ratio that separates professional from amateur cinematography
```

A secondary light used to soften or fill in shadows created by the key light, controlling the contrast ratio of the scene — more fill means softer, less fill means more dramatic. The fill light ratio is one of the most consequential creative decisions in cinematography. Gordon Willis deliberately withheld fill in "The Godfather," letting shadows go black, while Robert Richardson uses generous fil…

**When to use.** Bring in fill light when the key creates the right direction but the shadows hide too much story information. It is useful for dialogue, portraits, product work, and any scene where faces must remain dimensional yet readable. More fill creates a gentle, open image; less fill preserves danger and my…

**Directing the AI.** Establish the key light first, then add a broad, diffused secondary source near the camera side. Ask for soft shadow recovery without a second visible shadow or competing highlight. Define the desired contrast clearly: the shadow side should retain color, eye detail, and facial structure while staying darker than the key side. Keep the fill neutral unless the environment motivates a tint. Across…

**Common mistakes.**
- Raising fill until the face becomes flat and directionless, erasing the visual hierarchy established by the key light.
- Using a small hard fill source that casts its own sharp shadow and reveals the artificial lighting setup.
- Changing the fill ratio between adjacent shots, causing skin contrast and shadow detail to jump during the edit.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `spotlight-hero-card`, 220f

**Sources.** [Film Lighting](None)


### gobo-lighting

**"Gobo Lighting Prompt for AI Image & Video"** · `lighting` · level advanced

```
Gobo lighting casting patterned shadows across [Subject], horizontal bars of light and dark striping across the form at an angle, the shadow pattern breaking and wrapping as it crosses three-dimensional contours, projected by a single hard source through a template, Kodak Double-X black and white stock for maximum contrast between the light bars and shadow bars, the quintessential film noir visual texture
```

Light shaped by a template (gobo) placed in front of the source, casting patterned shadows — window frames, venetian blinds, branches — adding narrative texture without physical set pieces. Film noir cinematography relied heavily on gobo lighting; John Alton's venetian blind shadows in "The Big Combo" became the genre's visual shorthand. Dean Cundey used gobo patterns in John Carpenter's "Hallowe…

**When to use.** Gobo lighting is useful when a plain wall or simple set needs narrative texture without adding physical construction. Projected blinds can suggest confinement or secrecy; branches can make an interior feel exposed to the world outside. The technique belongs in noir, suspense, horror, and stylized d…

**Directing the AI.** Place a shaped template between one hard source and the subject. Define the pattern precisely, such as angled horizontal bars or broken branch shadows, and state where it lands. Let the projection wrap, widen, and break across face, clothing, furniture, and wall according to their depth. Keep light bars and shadow bars clearly separated. In video, hold the template spatially stable unless a belie…

**Common mistakes.**
- Overlaying a flat pattern across every surface at identical scale, ignoring distance and three-dimensional projection behavior.
- Using several unrelated templates together, turning focused narrative texture into visual noise with no readable source.
- Softening the source until the projected bars or branches lose definition and no longer function as shaped light.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `icon-field-colorize`, 45f

**Sources.** [Film Lighting](None)


### golden-hour

**"Golden Hour Prompt for AI Image & Video"** · `lighting` · level basic

```
Golden hour light thirty minutes before sunset bathing [Subject] in warm amber backlight, impossibly long shadows, lens flares streaking horizontally, the entire world turned to liquid gold and honey, shot on Kodak Vision3 50D for maximum color saturation in daylight, an 85mm lens compressing the background into a dense golden tapestry, the fleeting magic that Malick and Lubezki lived for
```

The warm, soft, directional light that occurs shortly after sunrise or before sunset, casting long shadows and bathing everything in a warm amber glow that flatters skin and landscapes. Terrence Malick is the supreme poet of golden hour — "Days of Heaven," shot almost entirely in magic hour by Néstor Almendros and Haskell Wexler, remains the gold standard. Emmanuel Lubezki captured breathtaking g…

**When to use.** Choose golden hour when warmth, tenderness, nostalgia, freedom, or natural grandeur should shape the scene. The low sun flatters faces, stretches shadows, and gives landscapes dimensional color. It suits romantic passages, journeys, memory, and violence made visually contradictory by beautiful ligh…

**Directing the AI.** Set the scene about thirty minutes before sunset or shortly after sunrise, with the sun low behind or beside the subject. Use warm amber backlight, long directional shadows, light haze, and restrained horizontal flare. Let an 85mm perspective compress the glowing background while preserving readable skin edges. Keep the sky and shadow side cooler for contrast. For video, maintain one sun position…

**Common mistakes.**
- Pairing long sunset shadows with a sun placed high overhead, creating contradictory lighting geometry.
- Flooding every surface with uniform orange color, losing the cooler shadows that make warm light feel believable.
- Adding heavy lens flare across faces and focal details, turning atmospheric warmth into an optical obstruction.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `letterspace-materialize`, 15f

**Sources.** [Film Lighting](None)


### hard-light

**"Hard Light Prompt for AI Image & Video"** · `lighting` · level basic

```
Hard light from a bare overhead source casting razor-sharp shadows on [Subject], defined shadow edges so crisp they look cut with a knife, every surface texture amplified by the raking illumination, shot on Kodak Double-X black and white stock for maximum contrast, a 35mm Zeiss Planar lens, the graphic severity of film noir where light itself becomes an instrument of pressure
```

Light from a small or distant source that creates sharp, well-defined shadows, adding texture, drama, and graphic quality that can be harsh and unflattering or strikingly bold. Film noir cinematographers like John Alton and Nicholas Musuraca built entire visual worlds from hard light, creating the razor-sharp shadows of venetian blinds and fedora brims. David Fincher and Darius Khondji used hard…

**When to use.** Use hard light when sharp shadows and exposed texture should create pressure, heat, severity, or graphic style. A small source can carve faces, project window patterns, define dust, or make architecture feel unforgiving. It suits noir, Westerns, interrogation, and harsh daylight. Because it reveals…

**Directing the AI.** Place a small bare or distant source at a defined angle and demand crisp, clearly shaped shadow edges. Let raking light reveal pores, fabric, dust, walls, and metal while keeping the contrast strong. A monochrome or restrained palette can make the geometry more forceful. Name any projected shape, such as blinds, and align it with the source. Avoid broad diffusion, ambient fill, or several competi…

**Common mistakes.**
- Adding large diffusion to the source, softening the edges until the defining hard-shadow quality disappears.
- Using several hard lights from unrelated angles, producing crossed shadows that make the scene visually incoherent.
- Ignoring how raking light reveals skin and surface flaws, creating harsh detail where the subject needed restraint.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `fracture`, 156f

**Sources.** [Film Lighting](None)


### high-key-lighting

**"High-Key Lighting Prompt for AI Image & Video"** · `lighting` · level basic

```
High-key lighting flooding [Subject] in bright even illumination with barely a shadow to be found, the overall exposure pushed a third of a stop hot to create an airy blown-out feeling, shot on Alexa at 1280 ISO with Cooke S7 glass for gentle halation around the highlights, the dreamy overlit aesthetic of warmth without shadows, optimism without darkness
```

A bright, even lighting style with minimal shadows that creates an optimistic, clean, or ethereal atmosphere, common in comedies, commercials, and dream sequences. The classic Hollywood musical relied on high-key lighting — Vincente Minnelli's "An American in Paris" and "The Band Wagon" glow with uniform brightness. Kubrick used clinical high-key lighting in the space station sequences of "2001"…

**When to use.** Choose high-key lighting for optimism, cleanliness, glamour, romantic ease, clinical futurism, or a dreamlike lack of darkness. It works in comedy, commercials, musicals, beauty work, and deliberately sterile interiors. The frame should remain shaped even with minimal shadow. Use low contrast inten…

**Directing the AI.** Surround the subject with broad, diffused illumination and keep the fill level close to the key so shadows remain pale and soft. Lift the overall exposure slightly while protecting facial and fabric highlights from clipping. Use light backgrounds, gentle halation, creamy skin, and restrained pastel color. Preserve subtle edge separation through small tonal differences rather than hard rims. For v…

**Common mistakes.**
- Confusing high key with blown highlights, erasing skin texture and white surfaces instead of controlling contrast.
- Removing every trace of direction, which makes the subject look flat rather than softly and evenly modeled.
- Placing dark background elements behind the subject that contradict the intended bright, low-contrast visual field.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `spotlight-hero-card`, 220f

**Sources.** [Film Lighting](None)


### key-light

**"Key Light Prompt for AI Image & Video"** · `lighting` · level basic

```
Strong directional key light from a single source illuminating [Subject], the light carving sharp shadows that define every contour, dust motes floating in the visible beam, the single-source authority establishing the entire mood, a Fresnel spotlight quality with defined beam edge, warm tungsten color temperature at 3200K against cool blue ambient shadow
```

The primary and brightest light source in a scene, whose position, intensity, and quality define the overall mood and establish the dominant direction of light and shadow. Gordon Willis, "the Prince of Darkness," used deliberately underexposed key lights in "The Godfather" to create the shadowy world of the Corleone family. Vittorio Storaro sculpted light as pure emotion in "Apocalypse Now" and "…

**When to use.** Define the key light whenever one source must establish the scene's dominant visual logic. Its angle and hardness can make a face open, guarded, glamorous, threatening, or exhausted before secondary lights do anything. A clear key is vital in portraits and narrative scenes where viewers should unde…

**Directing the AI.** Name the key as the brightest source and place it precisely relative to the subject, such as 45 degrees camera-left and slightly high. Describe whether its beam is hard or soft, where the nose and cheek shadows fall, and how rapidly illumination drops across the scene. A warm tungsten key against cooler ambient shadow creates readable color separation. Keep every secondary source dim enough that…

**Common mistakes.**
- Calling several sources the key, which destroys the single dominant direction needed to sculpt the scene coherently.
- Specifying brightness without angle or quality, leaving facial shadows and material texture entirely uncontrolled.
- Allowing ambient illumination to overpower the key, making the stated primary source visually irrelevant.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `spotlight-hero-card`, 220f

**Sources.** [Film Lighting](None)


### kicker-light

**"Kicker Light Prompt for AI Image & Video"** · `lighting` · level intermediate

```
Kicker light accent on [Subject], a focused beam from behind and to the side catching just the edge of a cheekbone, the rim of an ear, and the curve of a shoulder in a thin bright line against darkness, the subtlety of the kicker creating depth and three-dimensionality, shot with a 135mm telephoto at T2, warm 3000K color temperature suggesting a tungsten practical source
```

A light placed behind and to the side of a subject, adding an accent edge of light that is more targeted than a backlight, providing a touch of separation and dimensionality. The kicker light is a staple of professional cinematography that often goes unnoticed by audiences despite being visible in nearly every well-lit film. Darius Khondji uses precise kicker lights in David Fincher's "Se7en" to…

**When to use.** Reach for a kicker light when the subject almost separates from the background but a full backlight would feel excessive or unmotivated. A narrow accent can define one cheekbone, ear, shoulder, or costume edge while preserving a dark overall image. It works in restrained portraits, candlelit rooms,…

**Directing the AI.** Set a focused source behind and to one side of the subject, aimed across rather than directly toward the camera. Limit its reach to a thin accent on the near cheekbone, ear rim, hair edge, or shoulder curve. Match its color to a plausible lamp, fire, or practical source in the scene. Keep the face's front exposure unchanged. During movement, let the accent appear and disappear naturally as contou…

**Common mistakes.**
- Expanding the accent around the whole silhouette, which turns a targeted kicker into an indiscriminate backlight.
- Brightening the kicker beyond the scene's practical sources, making the edge feel detached from the surrounding exposure.
- Keeping the accent fixed on one screen edge while the subject turns, breaking the physical direction of the light.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `spotlight-hero-card`, 220f

**Sources.** [Film Lighting](None)


### lens-flare

**"Lens Flare Prompt for AI Image & Video"** · `lighting` · level basic

```
Dramatic lens flare across [Subject], horizontal anamorphic flare streaks in cyan and magenta stretching across the entire frame, secondary ghost flares bouncing between lens elements in geometric chains, shot on vintage anamorphic Panavision C-series lenses known for their aggressive but beautiful flare characteristics, the warm amber of sunrise fighting through cool blue coating artifacts
```

Light scattering through lens elements when a bright source hits the glass — once considered a flaw, now deliberately used to add energy, realism, or a dreamy sci-fi quality. J.J. Abrams made lens flare his polarizing signature, filling "Star Trek" (2009) with so many anamorphic flares that the technique became a meme. Before that, Janusz Kamiński used flares expressively in "Saving Private Ryan"…

**When to use.** Choose lens flare when a bright source should feel physically present inside the optics rather than merely lighting the set. It can energize action, make sunlight feel immediate, or push a scene toward dreamy science fiction. Use it as an event tied to camera angle and source position, not as surfa…

**Directing the AI.** Put a bright source at the edge of the frame or aimed toward the lens, then define the flare's path across the image. Specify a horizontal colored streak, a restrained chain of geometric ghosts, and a warm source fighting cooler coating artifacts. Keep the main face or action readable beneath the effect. For video, make the flare react to camera movement and disappear when the source is blocked;…

**Common mistakes.**
- Covering every frame with identical flare artifacts, which makes the effect feel composited rather than caused by a moving light source.
- Letting bright streaks cross the subject's eyes or essential action without a narrative reason, destroying clarity at the focal point.
- Mixing several unrelated flare shapes and colors until the optics no longer appear to belong to one coherent lens.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `text-as-mask`, 20f

**Sources.** [Film Lighting](None)


### low-key-lighting

**"Low-Key Lighting Prompt for AI Image & Video"** · `lighting` · level intermediate

```
Low-key lighting on [Subject] with deep impenetrable shadows claiming eighty percent of the frame, only a single source illuminating a small area, the contrast ratio pushed to 8:1 between highlights and shadows, shot on Kodak Double-X black and white stock with a 40mm Baltar lens, the inky blacks and silver highlights of classic film noir, John Alton-level mastery of darkness as an active compositional element
```

A dramatic lighting style dominated by deep shadows and high contrast where only select areas are illuminated, creating mystery, tension, and a noir-like atmosphere. John Alton literally wrote the book — "Painting with Light" — and defined low-key noir cinematography in films like "The Big Combo" and "T-Men." Gordon Willis pushed low-key to its extreme in "The Godfather," with Marlon Brando's eye…

**When to use.** Use low-key lighting when darkness should occupy the frame as an active dramatic force. It suits mystery, crime, horror, secrecy, moral ambiguity, and intimate scenes where only selected information is revealed. Strong contrast can direct attention with remarkable precision. The goal is not merely…

**Directing the AI.** Let roughly eighty percent of the frame fall into deep shadow and assign one controlled source to the essential face, hand, or object. Push the contrast toward an 8:1 relationship while preserving texture in chosen highlights and allowing other areas to vanish. Use inky blacks, silver or warm highlights, and negative fill to prevent ambient spill. Keep the beam motivated and narrowly shaped. For…

**Common mistakes.**
- Underexposing the entire image evenly, which creates muddy darkness without the selective highlight structure low key requires.
- Opening shadows with excessive fill, weakening mystery and turning the setup into ordinary balanced lighting.
- Crushing every black area identically, leaving no separation between subject, wardrobe, and background where readability matters.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `brand-ink-open`, 83f, `spotlight-hero-card`, 220f

**Sources.** [Film Lighting](None)


### motivated-lighting

**"Motivated Lighting Prompt for AI Image & Video"** · `lighting` · level intermediate

```
Motivated lighting on [Subject] with every light source logically justified within the scene, the shadows all pointing logically away from their respective visible sources, hidden augmentation maintaining the illusion of purely natural illumination, shot on 35mm with Panavision Primo lenses, the invisible craft of making elaborate lighting look like nature, Roger Deakins-level motivational rigor
```

Lighting that appears to come from a logical source within the story — a window, a fireplace, a streetlamp — even if augmented with movie lights, the effect looks naturally justified. Roger Deakins is the modern master of motivated lighting, meticulously justifying every light source in films like "Skyfall" and "1917." His work on the Coen Brothers' "No Country for Old Men" features exclusively m…

**When to use.** Motivated lighting belongs in any scene where cinematic control must remain invisible. Use it when windows, lamps, fires, streetlights, or headlights can justify the direction and color of every major source. It is particularly effective for realistic drama, period interiors, and location work wher…

**Directing the AI.** Identify every visible or implied source before describing the subject. A window should produce directional daylight and shadows that fall away from it; a lamp should create warmer, localized illumination with believable falloff. Add hidden augmentation only as an extension of those sources, never as a contradictory direction. Keep reflections, rims, and eye highlights consistent with the same lo…

**Common mistakes.**
- Adding a beautiful rim from the wrong direction when no window, lamp, or reflective surface can justify it.
- Giving several practical lamps equal influence across the room, ignoring distance, falloff, and obstruction between source and subject.
- Changing shadow direction between shots while visible sources remain fixed, exposing the construction behind supposedly natural illumination.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `icon-field-colorize`, 45f

**Sources.** [Film Lighting](None)


### practical-lighting

**"Practical Lighting Prompt for AI Image & Video"** · `lighting` · level intermediate

```
Practical lighting on [Subject] illuminated only by visible sources within the frame, each practical creating its own color world, the interplay of multiple color temperatures producing a rich layered chromatic atmosphere, no hidden movie lights, shot wide open at T1.3 on a Zeiss Super Speed to drink in every photon, the visual language of Christopher Doyle
```

Using visible light sources within the scene — lamps, candles, neon signs, TV screens — as the actual illumination, creating naturalistic, motivated lighting with rich atmosphere. Stanley Kubrick famously lit "Barry Lyndon" using only candles and natural window light, requiring specially modified NASA lenses. Wong Kar-wai and Christopher Doyle use neon signs and fluorescent tubes as practical sou…

**When to use.** Choose practical lighting when the sources should belong visibly to the world of the scene. Lamps, candles, televisions, fluorescent tubes, and neon signs can motivate color, direction, and atmosphere while making an interior feel lived-in. It works for naturalism and stylization alike. The visible…

**Directing the AI.** Name every visible source and assign it a local pool of illumination, color temperature, falloff, and affected surfaces. A warm lamp can shape one face while a cool television colors the shadow side and distant neon adds another layer. Keep brightness physically plausible and let areas between sources remain darker. Use a fast-lens look to retain low-light texture. For video, preserve each fixtur…

**Common mistakes.**
- Showing visible lamps that cast no matching light or shadow, making them look like decorative props.
- Giving every practical equal brightness and reach, flattening the layered pools that create believable atmosphere.
- Adding an unexplained frontal beauty light that contradicts the claim that visible in-scene sources provide illumination.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `icon-field-colorize`, 45f

**Sources.** [Film Lighting](None)


### rembrandt-lighting

**"Rembrandt Lighting Prompt for AI Image & Video"** · `lighting` · level intermediate

```
Rembrandt lighting portrait of [Subject], the key light positioned high and at 45 degrees creating the signature triangle of light on the shadow-side cheek, warm amber tones on the illuminated side transitioning to rich umber shadow on the other, shot on a 105mm portrait lens at f/2, the painterly quality that made Rembrandt's work immortal translated to photographic light
```

Named after the Dutch painter — light positioned to create a small triangle of light on the shadow side of the face, a classic portrait technique conveying depth and character. Rembrandt van Rijn developed this lighting naturally in his self-portraits, and Hollywood cinematographers adopted it as the gold standard for dramatic portraiture. Sven Nykvist, Ingmar Bergman's longtime cinematographer,…

**When to use.** Use Rembrandt lighting when a portrait needs dimensionality, restraint, and psychological weight. The small triangle of light on the shadow-side cheek keeps the face readable while preserving contrast, making the pattern useful for character portraits, interrogations, period scenes, and intimate dr…

**Directing the AI.** Name the pattern, then describe the mechanism: one key light about 45 degrees to the side and above eye level, the nose shadow connecting toward the cheek, and a small inverted triangle beneath the shadow-side eye. Control fill separately. Without those physical cues, models often return generic split lighting or a vague "painterly" portrait.

**Common mistakes.**
- Calling any half-lit face Rembrandt lighting without the defining triangle on the shadow-side cheek.
- Adding several equal-strength key lights that erase the directional pattern.
- Using "Rembrandt," "soft beauty light," "flat lighting," and "high key" together without resolving the contradiction.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `spotlight-hero-card`, 220f

**Sources.** [What Is Rembrandt Lighting and How To Use It](None)


### short-lighting

**"Short Lighting Prompt for AI Image & Video"** · `lighting` · level intermediate

```
Short lighting on [Subject] with the key hitting the narrow far side, putting the broader camera-facing side in shadow, the small bright area creating an accent surrounded by darkness, shot on a fast 85mm lens at T1.4 with the background falling to black, film noir portrait psychology where what is hidden matters more than what is shown
```

The side of the face turned away from the camera receives the key light, putting the broader visible area in shadow, creating a slimming, more dramatic and moody portrait. Short lighting is preferred for dramatic and thriller genres where mystery and tension serve the story. Gordon Willis frequently used short lighting patterns in his collaborations with Woody Allen and Francis Ford Coppola. Film…

**When to use.** Short lighting fits portraits that need mystery, tension, a slimmer face shape, or a sense that the character is withholding information. It works naturally in thrillers, noir, interrogations, and dramatic dialogue. The small far-side highlight becomes an accent surrounded by a larger field of shad…

**Directing the AI.** Angle the subject away from camera and place the key on the narrow face plane turned farther from the lens. Keep the broad camera-facing cheek in shadow, with the bright far cheek acting as a controlled accent. Use minimal fill and let the background fall darker if the scene supports it. Preserve a catchlight or slight eye detail where needed. During movement, make the light pattern respond to he…

**Common mistakes.**
- Illuminating the broad near cheek, which reverses the intended pattern and removes the slimming field of shadow.
- Crushing the entire camera-facing side to featureless black, losing the controlled detail that keeps the portrait readable.
- Letting the narrow highlight spread across the nose and front plane, weakening the concentrated dramatic accent.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `spotlight-hero-card`, 220f

**Sources.** [Film Lighting](None)


### side-lighting

**"Side Lighting Prompt for AI Image & Video"** · `lighting` · level intermediate

```
Side lighting from a single source striking [Subject] at exactly 90 degrees, one half brilliantly illuminated while the other half vanishes into complete shadow creating a perfect vertical division, every texture on the lit side rendered in crystalline detail while the shadow side reveals nothing, shot on large format with an 80mm lens, the extreme dimensionality of single-source side light, the duality made visible
```

Light striking the subject from a 90-degree angle, illuminating one half while leaving the other in shadow, splitting the face or figure to create strong dimensionality and visual tension. Vittorio Storaro used dramatic side lighting throughout "Apocalypse Now" to bisect characters between light and darkness, mirroring the moral duality at the film's core. Roger Deakins employs precise side light…

**When to use.** Use side lighting when a face or figure needs strong dimensionality, moral tension, or a visible split between competing states. It suits confrontations, secretive portraits, and moments when one side of a character should remain unreadable. The technique also gives textured subjects more relief be…

**Directing the AI.** Place one dominant source exactly 90 degrees to the subject. Keep the camera-facing division clear: one half receives crisp illumination while the opposite half falls into deep shadow. Describe which facial plane, object edge, or body contour catches the light, and protect detail on that side. Hold fill to a minimum so the split remains graphic. For video, keep the source and subject positions co…

**Common mistakes.**
- Adding frontal fill until both sides become equally readable, which removes the tension and sculptural split the setup needs.
- Placing the source too far forward, turning the result into ordinary three-quarter portrait lighting instead of true side light.
- Leaving the lit side featureless or clipped, so the frame loses the texture that should carry its dimensional detail.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `spotlight-hero-card`, 220f

**Sources.** [Film Lighting](None)


### silhouette

**"Silhouette Prompt for AI Image & Video"** · `lighting` · level basic

```
[Subject] reduced to a pure dark silhouette against an intensely bright backlight source, all surface detail eliminated leaving only iconic form and outline, strong rim light tracing edges, high contrast, Kodak Double-X black and white stock
```

Subject appears as a dark shape against a bright background, with all surface detail eliminated, reducing characters to pure form and creating iconic, mythic, or anonymous images. David Lean created one of cinema's most recognizable silhouettes with Peter O'Toole against the desert sun in "Lawrence of Arabia." Steven Spielberg's E.T. bicycle silhouette against the moon became one of the most icon…

**When to use.** Use a silhouette when identity should give way to shape, gesture, or archetype. It can make a figure mythic, anonymous, romantic, threatening, or small against a bright world. The outline must communicate the action because interior detail disappears. Choose distinctive profiles and separated limbs…

**Directing the AI.** Place the strongest light source directly behind the subject and expose for the bright sky, doorway, moon, or screen. Reduce the figure to near-black with no visible facial or surface detail. Separate arms, legs, props, and profile so the outline reads instantly, then add only a thin edge trace if needed. Keep the background simple and luminous. In video, choreograph lateral movement that preserv…

**Common mistakes.**
- Lifting shadow detail inside the figure, weakening the graphic reduction that makes a silhouette instantly recognizable.
- Overlapping limbs and props against the torso, creating an unreadable dark mass instead of expressive outline.
- Using a cluttered bright background whose shapes compete with the subject's edge and destroy figure-ground clarity.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `brand-ink-open`, 83f

**Sources.** [Film Lighting](None)


### soft-light

**"Soft Light Prompt for AI Image & Video"** · `lighting` · level basic

```
Soft diffused light wrapping around [Subject] with barely perceptible shadow transitions, a massive window or diffusion source bending light gently around face and shoulders, skin rendered with luminous porcelain quality, shot on Cooke S7 lenses known for gentle rendering and subtle halation on highlights, Fujifilm Eterna color science with delicate pastel tonality, the Vermeer-like quality of undirected daylight
```

Diffused light from a large source that wraps around the subject, creating gentle shadow transitions that are flattering for skin and create a dreamy or intimate quality. Sven Nykvist, Ingmar Bergman's cinematographer, was legendary for his soft, natural light in films like "Cries and Whispers" and "Fanny and Alexander," often bouncing light off white walls and ceilings. Emmanuel Lubezki creates…

**When to use.** Choose soft light when faces and materials need gentle modeling, intimacy, romance, or natural overcast calm. A large source wraps around features and creates gradual shadow transitions that are flattering without removing all shape. It suits close portraits, domestic scenes, beauty, and reflective…

**Directing the AI.** Describe a very large window, bounced source, or diffusion frame close to the subject, placed slightly to one side. Ask for light that wraps around cheeks and shoulders with broad highlights and barely perceptible shadow edges. Keep skin luminous, pastel color delicate, and highlight halation subtle. Use negative fill on the far side if more shape is needed. Avoid hard rim lines and tiny catchlig…

**Common mistakes.**
- Filling both sides equally until the face loses direction, volume, and any sense of a located source.
- Adding crisp nose or jaw shadows that contradict the requested broad diffusion and gentle transitions.
- Smoothing texture into plastic skin, mistaking soft illumination for aggressive cosmetic post-processing.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `spotlight-hero-card`, 220f

**Sources.** [Film Lighting](None)


### three-point-lighting

**"Three-Point Lighting Prompt for AI Image & Video"** · `lighting` · level basic

```
Classic three-point lighting on [Subject], the key light at 45 degrees creating defined shadow, a soft fill light gently opening the shadows, a warm-toned backlight rimming the edges with a thin golden halo, the balanced interplay sculpting the form into three dimensions, shot on medium format with an 80mm portrait lens at f/2.8, Kodak Portra color science with creamy skin tones and deep velvety blacks
```

The foundational lighting setup using three sources: a key light as the primary source, a fill light to soften shadows, and a backlight to separate the subject from the background. Developed during Hollywood's Golden Age by cinematographers like James Wong Howe and Gregg Toland, three-point lighting became the grammar of classical Hollywood cinema. It defined the glamorous look of stars from Garb…

**When to use.** Use three-point lighting when you need a flexible, readable foundation for portraits, interviews, dialogue, product work, or narrative coverage. The key establishes direction, fill controls contrast, and backlight separates the subject from the setting. It can look polished or dramatic depending on…

**Directing the AI.** Place the key about 45 degrees to one side and above the subject, creating a clear modeled shadow. Add a softer, dimmer fill from the opposite side that opens detail without erasing shape. Position a warm backlight behind and above to trace shoulders and hair while avoiding lens flare. Describe the relative intensity and color of all three sources. Keep the background darker enough that separatio…

**Common mistakes.**
- Making key and fill equally bright, which flattens the face and removes the setup's directional hierarchy.
- Using a backlight so strong that it creates a white cutout around hair and shoulders.
- Listing three lights without positions or ratios, leaving the resulting illumination arbitrary rather than intentionally structured.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `spotlight-hero-card`, 220f

**Sources.** [Film Lighting](None)


### uplighting

**"Uplighting Prompt for AI Image & Video"** · `lighting` · level basic

```
Uplighting from below illuminating [Subject], the unnatural upward-casting light reversing every shadow humans instinctively expect, shadows falling upward from the brow ridge creating deep black pools where the eyes should be, orange flickering firelight causing the shadows to dance, shot on a 50mm lens with the warm 2000K color temperature of open flame, the deep biological wrongness of light coming from below
```

Light cast upward from below the subject, unnatural to human experience, creating eerie, sinister, or supernatural effects — the classic "flashlight under the chin" horror look. James Whale used uplighting to terrifying effect in "Frankenstein" (1931) and "Bride of Frankenstein," casting Boris Karloff's face into monstrous relief. F.W. Murnau's "Nosferatu" employed underlighting to transform Max…

**When to use.** Use uplighting when illumination should feel instinctively wrong. A source below the face reverses familiar shadow patterns, turning ordinary features sinister, supernatural, theatrical, or childishly spooky. It works for horror, séances, firelit threats, and characters emerging from beneath a spac…

**Directing the AI.** Place the main source below the subject's chin or beneath the frame and angle it upward. Shadows should climb from brow, nose, and cheekbones, with eye sockets becoming dark pools above the lit planes. Use warm flickering firelight around 2000K when a flame motivates the effect, or a colder source for unnatural dread. Keep overhead fill minimal so normal shadow direction does not return. In video…

**Common mistakes.**
- Adding a stronger overhead key, which restores conventional facial shadows and cancels the unsettling reversal.
- Lighting the face evenly from below, missing the deep upward-cast shadows that make the setup biologically strange.
- Using uplighting in a neutral dialogue scene without motivation, making the visual tone feel accidentally theatrical.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `fracture`, 156f

**Sources.** [Film Lighting](None)


### balancing-elements

**"Balancing Elements Prompt for AI Image & Video"** · `composition` · level intermediate

```
Balanced composition with [Subject] on one third of the frame counterweighted by a visually striking element on the opposite side, the balance not symmetrical but felt, the eye moving comfortably between the two anchoring elements, shot on medium format with a 65mm lens at f/5.6, the compositional harmony of a frame where every element has been weighed and placed with the precision of a balance scale
```

Distributing visual weight across the frame so no single area feels too heavy or empty — a large subject on one side can be balanced by a smaller but visually striking element on the other. Akira Kurosawa was a master of compositional balance, carefully arranging actors and set pieces to create harmonious frames in "Ran" and "Kagemusha." Emmanuel Lubezki balances Malick's human subjects against n…

**When to use.** Balancing elements is useful when an asymmetrical frame feels lopsided even though the subject sits in the right place. A large muted figure can be counterweighted by a smaller bright object, strong line, or concentrated patch of contrast. Use the method in dialogue, landscape, still life, and envi…

**Directing the AI.** Place the primary subject on one side, then choose a secondary element on the opposite side with enough contrast, color, isolation, or shape to counter it. Keep the secondary element clearly less important while giving it sufficient visual mass. Test the spaces between both anchors and the frame edges. In video, preserve the balance as figures move by shifting camera position, blocking, or backgr…

**Common mistakes.**
- Matching both sides by size alone, ignoring how brightness, color, texture, and isolation change perceived visual mass.
- Making the counterweight as prominent as the subject, splitting attention between two equally demanding focal points.
- Correcting imbalance with an unrelated prop that has no place in the environment or connection to the scene.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `drone-dive-landing` (space-camera-moves), 150f, `exploded-view` (space-camera-moves), 150f

**Sources.** [Rules of Shot Composition in Film](None)


### centered-composition

**"Centered Composition Prompt for AI Image & Video"** · `composition` · level basic

```
Centered composition with [Subject] at the exact mathematical center, the space arranged in perfect bilateral symmetry around them, the deliberate center placement creating ritual importance and confrontational directness, shot on a 28mm lens from a locked tripod at center height, deep focus rendering every detail sharp, Wes Anderson planimetric aesthetic meets Kubrick one-point-perspective severity
```

Placing the subject dead center in the frame — when done deliberately, it creates a powerful, confrontational, or hypnotically ordered effect that requires confidence and intentionality. Wes Anderson builds his entire visual identity around centered subjects, creating his trademark "planimetric" compositions. Kubrick's centered one-point-perspective shots in "The Shining" and "Full Metal Jacket"…

**When to use.** Centered composition is powerful when the subject should confront the viewer, command ritual importance, or become the fixed axis of an ordered world. Use it for direct address, formal portraits, one-point perspective, deadpan comedy, and psychologically rigid spaces. It requires confidence because…

**Directing the AI.** Place the subject's central axis on the exact midpoint of the frame and align the camera with the environment's vanishing point. Arrange surrounding forms to reinforce that position through symmetry, converging lines, or balanced negative space. Keep lens height level and make any asymmetry deliberate. The subject may look directly into camera for confrontation or remain still within the ordered…

**Common mistakes.**
- Centering the subject while architecture and vanishing lines sit off-axis, making the composition feel carelessly misaligned.
- Using central placement in every shot, reducing a forceful choice to an unexamined visual habit with no escalation.
- Adding several equally bright side elements, which pull attention away from the exact axis the composition establishes.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `orbit-ring-title-open`, 130f

**Sources.** [Rules of Shot Composition in Film](None)


### contrast-composition

**"Contrast Prompt for AI Image & Video"** · `composition` · level basic

```
High contrast composition with [Subject] as a tiny warm-colored element against a vast cool-toned environment, every type of visual contrast at work simultaneously — warm against cool, small organic shape against massive geometry, soft texture against hard surface, movement against stillness, shot on large format 65mm with a 100mm telephoto compressing the background, Kodak Vision3 50D saturated daylight stock
```

Using opposing visual elements — light vs dark, large vs small, warm vs cool, sharp vs soft — to create visual interest, hierarchy, and dramatic tension within the frame. Akira Kurosawa was perhaps cinema's greatest practitioner of compositional contrast, pitting tiny samurai against massive rainstorms in "Seven Samurai" and fragile humans against erupting volcanoes of color in "Ran." David Lean…

**When to use.** Contrast is useful when a frame needs immediate hierarchy or when two forces should feel emotionally opposed. Pair warm with cool, small with large, soft with hard, organic with geometric, or motion with stillness. It can clarify the subject or turn the entire composition into conflict. Choose one…

**Directing the AI.** Select the dominant contrast first, such as a small warm figure against a vast cool structure. Reinforce it through scale, texture, and stillness only where those differences support the same idea. Keep the subject readable and prevent secondary colors or objects from creating rival conflicts. Describe both sides of the opposition concretely. For video, let the contrast persist through movement a…

**Common mistakes.**
- Stacking unrelated oppositions across color, scale, texture, and motion until the frame loses one dominant visual argument.
- Using strong tonal contrast without controlling the brightest area, allowing a background highlight to steal the subject's hierarchy.
- Choosing opposing colors as decoration while size, lighting, and staging communicate no actual tension between the elements.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `fracture`, 156f

**Sources.** [Rules of Shot Composition in Film](None)


### deep-focus

**"Deep Focus Prompt for AI Image & Video"** · `composition` · level intermediate

```
Deep focus composition with [Subject] visible across multiple planes simultaneously, all razor-sharp from two feet to thirty feet, the viewer free to explore any layer, requiring a small aperture of f/11 and powerful invisible lighting, shot on a 21mm wide lens to maximize depth of field, the Citizen Kane democratic composition where every inch of the frame rewards examination
```

Everything in the frame — foreground, middle ground, and background — is in sharp focus simultaneously, allowing the viewer to explore the entire image and discover relationships between planes. Orson Welles and Gregg Toland made deep focus the defining visual innovation of "Citizen Kane" (1941), composing shots where action in the foreground, middle ground, and background all demanded simultaneo…

**When to use.** Deep focus belongs in scenes where multiple planes carry simultaneous story information. Use it for ensemble staging, architecture, power relationships, reveals within one shot, or moments when the audience should choose where to look. Sharp foreground and background action can create tension witho…

**Directing the AI.** Stage distinct elements in foreground, middle ground, and background, then keep all three planes acceptably sharp. Use a wider perspective, strong depth cues, and enough even illumination to preserve texture throughout the space. Give each plane a different narrative function and prevent overlapping silhouettes from merging. Maintain atmospheric perspective without turning the distance soft. For…

**Common mistakes.**
- Keeping everything sharp without staging meaningful relationships across depth, producing detail density instead of dramatic complexity.
- Stacking figures directly behind one another, causing silhouettes to merge even though every plane remains technically focused.
- Adding heavy background haze or blur that contradicts the requirement for readable distant action and spatial information.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `drone-dive-landing` (space-camera-moves), 150f, `exploded-view` (space-camera-moves), 150f

**Sources.** [Rules of Shot Composition in Film](None)


### depth-of-field

**"Depth of Field Prompt for AI Image & Video"** · `composition` · level basic

```
Selective depth of field isolating [Subject] in a narrow focused slice, everything in front and behind melting into graduated blur, the cinematic depth of field that modern anamorphic and large-format cinematography has made the visual signature of prestige filmmaking, shot on a large format sensor with an 85mm lens at T1.3
```

The range of distance in a scene that appears acceptably sharp — manipulating depth of field controls what the viewer focuses on and how they perceive spatial depth. The creative use of depth of field defines entirely different cinematic schools: Gregg Toland's infinite depth in "Citizen Kane" versus the paper-thin focus of Wong Kar-wai's films. Robert Richardson uses depth of field as an emotion…

**When to use.** Depth of field is a core choice whenever the audience needs guidance about where to look and how much of the space matters. Narrow focus isolates emotion or detail; broad focus reveals relationships across the frame. Use it to control intimacy, suspense, information, and spatial depth. Decide befor…

**Directing the AI.** State the nearest and farthest distances that should appear sharp, then identify the exact focal subject. For selective depth, ask for progressive blur before and behind that plane; for broad depth, preserve readable detail through foreground, middle ground, and background. Match apparent focus behavior to perspective and distance. In video, specify whether focus stays locked, follows the subject…

**Common mistakes.**
- Requesting cinematic depth of field without naming a focus plane, leaving sharpness arbitrary and unstable across the image.
- Applying equal blur to objects at different distances, which destroys the gradual spatial cues created by optical focus.
- Keeping the background soft when its action carries essential story information that should remain available to the viewer.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `dolly-zoom-real` (depth-layer-moves), 150f, `multiplane-real` (depth-layer-moves), 150f

**Sources.** [Rules of Shot Composition in Film](None)


### diagonal-lines

**"Diagonal Lines Prompt for AI Image & Video"** · `composition` · level basic

```
Diagonal line composition with [Subject] surrounded by aggressive 45-degree angles, nothing horizontal or vertical in the entire composition, every line tilted and active, the deliberate absence of any stable reference creating dynamic instability and forward momentum, shot on a 24mm wide-angle with slight barrel distortion enhancing angular dynamism
```

Using diagonal elements in composition to create dynamic energy and movement, as diagonals feel inherently unstable and active compared to horizontal or vertical lines. Carol Reed filled "The Third Man" with diagonal compositions — tilted streets, canted angles, shadow lines cutting diagonally across walls — to visualize post-war Vienna's moral instability. Michael Bay uses aggressive diagonal co…

**When to use.** Diagonal lines suit action, pursuit, imbalance, conflict, and scenes that should resist calm horizontal or vertical order. Streets, shadows, rain, architecture, bodies, and camera angle can all create active slants through the frame. Use them to push the eye forward or make the world feel unstable.…

**Directing the AI.** Build the composition around one strong diagonal, roughly crossing from a lower corner toward the opposite upper area. Align architecture, shadow, rain, or body movement with that direction, then place the subject where the line delivers attention. Minimize stable horizontal references if instability is the goal. Use a second opposing diagonal only to create deliberate friction. For video, carry…

**Common mistakes.**
- Tilting every object in a different direction, creating visual confusion rather than one readable source of dynamic energy.
- Leaving a dominant horizon perfectly stable while minor props angle randomly, weakening the intended sense of instability.
- Using diagonals in a quiet formal scene where their kinetic pressure contradicts the emotional pace and staging.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `steep-tilt-glide`, 120f

**Sources.** [Rules of Shot Composition in Film](None)


### figure-ground

**"Figure-Ground Relationship Prompt for AI Image & Video"** · `composition` · level intermediate

```
Strong figure-ground relationship with [Subject] separated from the background by extreme tonal and color contrast creating instant three-dimensional pop, the form isolated as cleanly as a paper cutout, shot on medium format with a 110mm lens at f/2.8 creating slight background softening that adds optical separation to the tonal separation, the fundamental perceptual principle that makes cinema readable
```

The perceptual relationship between a subject (figure) and its background (ground) — strong figure-ground separation makes subjects pop, while ambiguous relationships create artistic tension. Film noir deliberately plays with figure-ground by merging characters into shadows, while Spielberg ensures crisp separation for visual clarity. Kubrick uses monochromatic figure-ground merging in "Full Meta…

**When to use.** Figure-ground control matters whenever the subject risks disappearing into the background or should deliberately merge with it. Strong separation supports clarity, icon-like presence, and fast visual reading; ambiguity can create camouflage, loss of identity, or suspense. Use tonal, color, focus, e…

**Directing the AI.** Define the figure and ground as separate tonal and color fields, then decide the strength of their boundary. For clean separation, use contrasting value, a restrained edge light, or slight background softening. For ambiguity, match selected contours and tones while preserving one clue that reveals the subject. Avoid accidental tangencies where edges merge unpredictably. In video, keep separation…

**Common mistakes.**
- Matching subject and background values by accident, causing important faces or gestures to disappear without narrative purpose.
- Outlining the entire figure with artificial brightness, producing separation that ignores the scene's actual light direction.
- Using maximum contrast on every edge, making the subject look pasted onto the environment rather than embedded within it.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `brand-ink-open`, 83f

**Sources.** [Rules of Shot Composition in Film](None)


### foreground-interest

**"Foreground Interest Prompt for AI Image & Video"** · `composition` · level intermediate

```
Foreground interest composition with [Subject] in the mid-ground and blurred elements dominating the immediate foreground, three distinct depth planes creating immersive physical space, the foreground elements partially obscuring the subject adding voyeuristic tension, shot on a 40mm lens at T2 creating visible focus separation between planes, Kodak 5219 500T with desaturated earth tones, the Spielberg technique of putting the viewer inside the world
```

Placing objects or elements in the immediate foreground to add depth and dimension, creating a layered image that draws the viewer through multiple planes of the composition. Steven Spielberg consistently uses foreground objects — a glass of water in "Jurassic Park," toys in "E.T." — to add depth and narrative context. Roger Deakins layers his compositions with foreground elements in "Skyfall" an…

**When to use.** Foreground interest helps when a scene feels flat, observed from outside, or short on spatial tension. Use nearby branches, glass, furniture, props, architecture, or partial figures to place the viewer inside the environment. It can add context, concealment, scale, or a voyeuristic edge while guidi…

**Directing the AI.** Place a large object very close to the camera, partially entering the frame, with the main subject in the middle ground and a readable background beyond. Decide whether the foreground stays soft, sharp, reflective, or silhouetted based on its role. Use overlap to establish depth without covering the subject's essential action. For video, let parallax separate the planes during camera movement; ne…

**Common mistakes.**
- Adding anonymous blurred blobs at the corners, with no recognizable connection to the location or the scene's meaning.
- Covering the subject's face or action with foreground objects that create obstruction without tension, context, or reveal.
- Moving all depth planes at the same screen speed, eliminating the parallax that makes foreground layering physically convincing.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `dolly-zoom-real` (depth-layer-moves), 150f, `multiplane-real` (depth-layer-moves), 150f

**Sources.** [Rules of Shot Composition in Film](None)


### framing-within-frame

**"Framing Within Frame Prompt for AI Image & Video"** · `composition` · level intermediate

```
Frame within a frame with [Subject] seen through a dark silhouette of an architectural opening, the framing device adding layers of depth and the voyeuristic feeling of observing from a hidden vantage, shot on a 35mm lens with exposure balanced for the subject making the surrounding frame go completely dark, the John Ford doorway composition that transforms a simple element into a metaphor for belonging and exclusion
```

Using elements within the scene — doorways, windows, arches, branches — to create a secondary frame around the subject, adding depth, drawing focus, and suggesting entrapment or voyeurism. John Ford used doorway framing iconically in "The Searchers" — the final shot of John Wayne framed in a cabin door is one of cinema's most analyzed compositions. Hitchcock used frame-within-frame throughout "Re…

**When to use.** Use framing within frame when the environment should control how the audience sees a subject. A doorway can suggest exclusion, a window can create voyeurism, and an arch can add formal depth. The technique is valuable for surveillance, isolation, discovery, and layered location work. Choose a frami…

**Directing the AI.** Place the camera behind or beyond a real foreground opening, then position the subject inside its boundaries. Let the outer frame fall darker, softer, or partially silhouetted so attention passes through it into the scene. Keep enough irregularity to preserve physical depth rather than making a graphic border. Align the inner opening with the subject's action or isolation. In video, allow the fra…

**Common mistakes.**
- Adding a decorative border with no physical relationship to the location, which reads as graphic design rather than staging.
- Letting the doorway, window, or branches cut through the subject's face and obscure essential expression without purpose.
- Exposing foreground and subject equally, flattening the depth layers that make the secondary frame visually useful.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `spotlight-hero-card`, 220f

**Sources.** [Rules of Shot Composition in Film](None)


### golden-ratio

**"Golden Ratio Prompt for AI Image & Video"** · `composition` · level advanced

```
Golden ratio spiral composition with [Subject] placed along the logarithmic curve, every major element sitting naturally along the mathematical spiral, the proportional harmony creating organic rightness that the eye follows without conscious awareness, shot on a 24mm wide-angle lens, the mathematical beauty that connects Fibonacci sequences to Renaissance painting to cinematic composition
```

Composing using the mathematical golden spiral (1.618:1) to place key elements along a naturally occurring logarithmic curve, creating compositions that feel organically harmonious. While debate exists about whether filmmakers consciously employ the golden ratio, analysis of work by Akira Kurosawa, Kubrick, and Spielberg reveals compositions that consistently align with the spiral. Vittorio Stora…

**When to use.** Use the golden ratio when a composition needs organic flow rather than the visible grid of thirds or the formality of symmetry. It suits landscapes, portraits in complex environments, still life, and layered action with a curved visual path. The spiral can connect a broad outer shape to a tight foc…

**Directing the AI.** Lay a logarithmic spiral across the frame and place the main subject near its tightest curl. Arrange larger environmental forms, secondary figures, or lines along the expanding arc so the eye travels inward naturally. Avoid drawing a literal spiral into the set unless the story requires one. Keep the focal point strongest through contrast and detail. For video, let camera or subject movement foll…

**Common mistakes.**
- Forcing every prop onto a visible spiral, making the composition feel diagrammed instead of naturally organized around attention.
- Using the golden ratio as a substitute for contrast, depth, and subject hierarchy, leaving the focal point weak.
- Confusing the technique with centered symmetry, which removes the expanding curved path that should guide the viewer.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `orbit-ring-title-open`, 130f

**Sources.** [Rules of Shot Composition in Film](None)


### headroom

**"Headroom Prompt for AI Image & Video"** · `composition` · level basic

```
Proper headroom in a medium close-up of [Subject], eyes positioned along the upper-third line with a comfortable gap between the crown and the top of the frame, enough space to feel natural without wasting frame real estate, shot on a 85mm lens at T2.8, the invisible grammar of good camera operation
```

The space between the top of a subject's head and the top of the frame — too much feels disconnected, too little feels cramped, and proper headroom creates a natural, comfortable framing. Deliberately violating headroom conventions can be powerful: the Coen Brothers frequently cut off the top of heads or leave excessive headroom for comedic or unsettling effect in "A Serious Man" and "No Country…

**When to use.** Headroom matters whenever a person occupies the frame, especially in interviews, dialogue, portraits, and moving coverage. A measured gap above the crown keeps the composition comfortable; too little pressure feels cramped, while too much space disconnects the face from the frame. Break the convent…

**Directing the AI.** Set the subject's eyes near the upper third and leave a controlled gap between the crown and top edge. Scale that gap to the shot size: tighter close-ups can crop hair deliberately, while medium shots need more breathing room. Keep the chin and shoulders balanced against the upper space. For video, maintain headroom as the subject stands, sits, or crosses frame by adjusting camera tilt smoothly;…

**Common mistakes.**
- Leaving a large blank area above the head in a close portrait, making the subject appear to sink inside the frame.
- Clipping the crown by accident rather than using a confident, consistent close-up crop with clear visual intent.
- Allowing headroom to change wildly during movement, causing the camera to feel reactive instead of controlled.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `spotlight-hero-card`, 220f

**Sources.** [Rules of Shot Composition in Film](None)


### lead-room

**"Lead Room Prompt for AI Image & Video"** · `composition` · level basic

```
Lead room composition with [Subject] positioned on one side of the frame with generous empty space in the direction of their gaze or movement, the open space suggesting possibility and destination, the satisfying rightness of proper lead room creating visual momentum, shot on a 50mm lens, the composition feeling natural and kinetically forward
```

Empty space in front of a moving subject or in the direction they're looking, giving the subject visual breathing room and implying destination or intent. Lead room is one of the fundamental principles of shot composition — violating it deliberately creates tension and unease, as the Coen Brothers and David Fincher sometimes do in thriller sequences. Denis Villeneuve uses generous lead room in "A…

**When to use.** Lead room is essential when a subject looks, walks, drives, or moves toward one side of the frame. Space ahead gives that action somewhere to go and lets the audience anticipate a destination, person, or threat. Use generous room for possibility and forward momentum. Remove it deliberately when the…

**Directing the AI.** Place the moving or looking subject on the side opposite their direction, leaving a larger open field ahead of the eyes or motion. Keep the destination readable through environment, light, or framing, even if nothing has entered yet. Reduce trailing space behind the subject without crowding them. For video, pan or track at a speed that preserves the open area. If tension requires breaking the rul…

**Common mistakes.**
- Leaving empty space behind a moving subject while compressing the area ahead, making the frame feel visually backward.
- Following body orientation instead of eye direction, which can create lead room on the wrong side of a glance.
- Recentering the subject continuously during a tracking shot, erasing the forward space that communicates destination and momentum.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `drone-dive-landing` (space-camera-moves), 150f, `exploded-view` (space-camera-moves), 150f

**Sources.** [Rules of Shot Composition in Film](None)


### leading-lines

**"Leading Lines Prompt for AI Image & Video"** · `composition` · level basic

```
Leading lines composition converging toward [Subject] at a distant vanishing point, every element in the frame designed to pull the eye irresistibly toward the focal point, morning fog softening the background and enhancing atmospheric perspective, shot on a 135mm telephoto to compress the distance and intensify convergence, desaturated cool palette, the visual magnetism of lines that refuse to let the eye wander
```

Using natural or architectural lines within the scene — roads, fences, corridors, shadows — to guide the viewer's eye toward the subject or deep into the frame. Kubrick's one-point-perspective corridors are pure leading-line compositions, while Vilmos Zsigmond used railroad tracks and highways as leading lines in "The Deer Hunter." Roger Deakins uses architectural lines in "Skyfall" — particularl…

**When to use.** Choose leading lines when the eye needs a clear route through a complex environment. Roads, fences, corridors, beams, shadows, and rows of objects can pull attention toward a distant subject or deeper into the frame. The technique is useful for journeys, reveals, architecture, and scale. Lines must…

**Directing the AI.** Select one family of lines in the environment and aim their convergence toward the subject or intended vanishing point. Use camera height and lens perspective to strengthen the pull without bending every structure unnaturally. Let fog, distance, or tonal falloff simplify the far end of the frame. Keep the subject distinct where the lines meet. For video, reveal or intensify the convergence throug…

**Common mistakes.**
- Using strong converging lines that point away from the subject, sending attention toward an irrelevant edge or empty corner.
- Combining several conflicting line systems, leaving the eye trapped between architecture, shadows, and horizon with no destination.
- Warping straight structures excessively to force convergence, making the spatial design feel synthetic rather than observed.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `drone-dive-landing` (space-camera-moves), 150f, `exploded-view` (space-camera-moves), 150f

**Sources.** [Rules of Shot Composition in Film](None)


### mise-en-scene

**"Mise-en-Scène Prompt for AI Image & Video"** · `composition` · level advanced

```
Meticulously arranged mise-en-scene with [Subject] positioned within an environment where every element tells a story, every prop researched and placed with production designer precision, the apparent normalcy concealing visible fault lines, shot on 35mm with a 32mm lens to capture the full space as a narrative environment, the Sirkian melodrama of a world where set design is psychology
```

The total arrangement of everything visible in the frame — set design, props, costumes, lighting, actor positioning — where every element is a deliberate storytelling choice. The concept originates from French theater and was elevated to an art form by directors like Max Ophüls in "The Earrings of Madame de..." and Jean Renoir in "The Rules of the Game." Kubrick's obsessive mise-en-scène in "2001…

**When to use.** Mise-en-scène is the right lens when the entire visible world must communicate character, class, history, or conflict before anyone speaks. Use it for controlled interiors, symbolic environments, ensemble blocking, and frames where props or architecture carry plot. It is especially valuable when bu…

**Directing the AI.** Define the environment, period cues, palette, costume, props, lighting logic, and actor positions as one connected system. Assign each major object a relationship to the subject or story, then remove anything that does not support that relationship. Use depth and blocking to expose status or tension. Keep wear, spacing, and material detail consistent with the setting. For video, preserve object l…

**Common mistakes.**
- Listing attractive props without connecting them to character, conflict, or setting, creating decoration instead of visual storytelling.
- Overloading every surface with symbolic objects, leaving the audience no hierarchy and the performers no believable living space.
- Changing furniture, costume details, or practical-light positions across shots, breaking the coherence of the designed world.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `drone-dive-landing` (space-camera-moves), 150f, `exploded-view` (space-camera-moves), 150f

**Sources.** [Rules of Shot Composition in Film](None)


### negative-space

**"Negative Space Prompt for AI Image & Video"** · `composition` · level intermediate

```
Negative space composition with [Subject] occupying the extreme lower corner of the frame, the remaining ninety percent a vast expanse of emptiness, the scale relationship between the tiny figure and the overwhelming void creating a visceral feeling of isolation, shot on medium format with a 55mm lens at f/8 for clinical sharpness across the entire frame, the minimalist language of Antonioni where emptiness speaks louder than dialogue
```

Leaving large areas of the frame empty, with the subject occupying a small portion, creating breathing room, isolation, contemplation, or emphasizing the weight of absence. Michelangelo Antonioni was the master of negative space in films like "L'Avventura" and "Red Desert," where vast empty landscapes and blank walls dwarf his characters. Sofia Coppola uses negative space in "Lost in Translation"…

**When to use.** Negative space works when what surrounds the subject should feel as important as the subject itself. Use it for solitude, anticipation, emotional distance, oppressive architecture, vast landscape, or room for text and motion. A small figure against emptiness can carry enormous weight, but the void…

**Directing the AI.** Push the subject toward a corner or edge and reserve most of the frame for a controlled expanse of sky, wall, darkness, or landscape. Keep the empty field simple but not dead, using subtle texture, gradient, or atmospheric depth. Make the scale contrast unmistakable and prevent small background objects from filling the void. For video, hold the emptiness long enough to register, or let movement e…

**Common mistakes.**
- Leaving random unused space around a normally framed subject, which feels accidental rather than emotionally or compositionally charged.
- Filling the supposed void with detailed props, texture, and secondary figures until it no longer reads as absence.
- Centering the subject during motion, removing the asymmetry and expectation created by a large open field.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `brand-ink-open`, 83f, `spotlight-hero-card`, 220f

**Sources.** [Rules of Shot Composition in Film](None)


### repetition-and-pattern

**"Repetition and Pattern Prompt for AI Image & Video"** · `composition` · level intermediate

```
Repetition and pattern composition with [Subject] as the single disruption in an otherwise uniform array, hundreds of repeated elements creating mesmerizing regularity with one anomaly immediately drawing the eye, the visual principle that the human eye is hardwired to detect anomalies in regular patterns, shot on a 50mm lens at f/4 with the full pattern sharp edge to edge, warm ambient lighting
```

Using recurring visual elements — shapes, colors, objects — to create rhythm and unity in the frame, where breaking a pattern draws immediate attention to the disruption. Kubrick's symmetrical corridors in "The Shining" use pattern repetition to create hypnotic unease, and any break in the pattern (the twins at the end of a hallway) becomes terrifying. Wes Anderson builds frames from repeated ele…

**When to use.** Repetition and pattern works when order, scale, routine, conformity, or obsession should dominate the frame. Rows of windows, uniforms, doors, lights, or bodies create rhythm that the eye reads quickly. One anomaly then gains immediate narrative force. Use the technique for architecture, crowds, ri…

**Directing the AI.** Build a clear array of recurring shapes, colors, objects, or figures with consistent spacing and orientation. Choose one subject as the only meaningful break through color, pose, absence, or direction. Keep the full pattern readable across the frame and give the anomaly enough contrast to register without becoming unrelated. For video, establish the regular rhythm before introducing disruption, t…

**Common mistakes.**
- Varying color, size, and spacing across every repeated unit, leaving no stable pattern for the audience to recognize.
- Introducing several anomalies at once, which divides attention and weakens the narrative force of the intended disruption.
- Cropping the array so tightly that repetition cannot accumulate into rhythm or communicate a larger ordered system.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `icon-field-colorize`, 45f

**Sources.** [Rules of Shot Composition in Film](None)


### rule-of-thirds

**"Rule of Thirds Prompt for AI Image & Video"** · `composition` · level basic

```
Rule of thirds composition with [Subject] positioned at the upper-right power point intersection, eyes precisely on the top horizontal third line, the remaining two-thirds of the frame filled with negative space creating natural visual flow, the composition dynamically balanced despite being asymmetrical, shot on a 50mm lens at T2.8, overcast daylight providing even naturalistic illumination
```

Dividing the frame into a 3x3 grid and placing key elements along the lines or at their intersections, creating naturally balanced, dynamic compositions that feel more alive than dead-center framing. While most directors use the rule instinctively, Roger Deakins and the Coen Brothers apply it with mathematical precision in films like "Fargo" and "No Country for Old Men." Emmanuel Lubezki frequent…

**When to use.** Use the rule of thirds when a centered frame feels static but the composition still needs immediate clarity. It suits portraits, landscapes, interviews, and moving subjects because it creates space for gaze, direction, or environment. Place the focal point at an intersection and use the remaining a…

**Directing the AI.** Divide the frame mentally into a three-by-three grid. Place the subject's primary focal point, often the eyes or face, on one power-point intersection and align the horizon or dominant architecture with a third line. Give the open two-thirds a purpose through landscape, gaze direction, or approaching action. Keep secondary elements from competing with the focal point. For video, preserve useful l…

**Common mistakes.**
- Placing the subject near a third line while leaving the remaining space empty of meaning or directional purpose.
- Aligning every object to the grid, creating a visibly calculated frame instead of a naturally balanced composition.
- Using the rule during direct confrontation or formal symmetry, where off-center placement weakens the intended psychological force.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: pan_right | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: smooth_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: smooth_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `drone-dive-landing` (space-camera-moves), 150f, `exploded-view` (space-camera-moves), 150f, `spotlight-hero-card`, 220f

**Sources.** [Rules of Shot Composition in Film](None)


### shallow-focus

**"Shallow Focus Prompt for AI Image & Video"** · `composition` · level basic

```
Shallow focus portrait of [Subject] with only the face in razor-sharp focus while everything else dissolves into a tapestry of luminous color and bokeh, the depth of field so narrow that even the near ear goes soft, shot on a Zeiss Master Prime 85mm at T1.4 wide open, the large format sensor transforming the background into abstract painting, the Wong Kar-wai visual poetry of focus as desire
```

Using a very narrow depth of field so only the subject is sharp while everything else melts into soft blur, isolating the subject and creating an intimate, dreamy quality. Wong Kar-wai and Christopher Doyle use extremely shallow focus in "In the Mood for Love" and "Chungking Express" to create their signature romantic, ephemeral atmosphere. Terrence Malick's work with Emmanuel Lubezki frequently…

**When to use.** Shallow focus is useful when one face, eye, hand, or object must dominate a crowded or intimate frame. It can turn a literal environment into color and light, giving portraits a romantic, fragile, or subjective quality. The technique also helps hide distracting backgrounds. Use it with discipline:…

**Directing the AI.** Choose a single narrow focus plane and name what must remain sharp, such as the nearer eye or a hand-held object. Let the near ear, foreground, and background soften progressively rather than applying one uniform blur. Describe large soft bokeh shapes only where real highlights exist. Preserve clean edges at the focal plane. In video, hold focus on the chosen detail through subtle movement or spe…

**Common mistakes.**
- Blurring the background uniformly like a cutout mask, with no gradual transition through foreground, subject depth, and distance.
- Leaving both eyes equally sharp in a steeply angled close-up despite asking for an extremely narrow focus plane.
- Using shallow focus when several spatial relationships matter, hiding story information that the audience needs to compare.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `dolly-zoom-real` (depth-layer-moves), 150f, `multiplane-real` (depth-layer-moves), 150f

**Sources.** [Rules of Shot Composition in Film](None)


### symmetry

**"Symmetry Prompt for AI Image & Video"** · `composition` · level basic

```
Perfect bilateral symmetry with [Subject] standing at the exact center of the vanishing point, matching elements receding into infinity on both sides, the symmetry so absolute it becomes psychologically oppressive rather than beautiful, shot on a wide 24mm lens from a locked-off tripod at exact center height, Kubrick one-point-perspective severity
```

A composition where both halves of the frame mirror each other, creating a sense of order, formality, perfection, or unsettling precision. Stanley Kubrick made symmetry his defining visual signature — the one-point-perspective corridor shots of "The Shining" and "A Clockwork Orange" remain the technique's most analyzed examples. Wes Anderson took symmetry to its whimsical extreme, making it the e…

**When to use.** Symmetry is strongest when order itself carries emotion. Use it for ritual, authority, control, artificial perfection, deadpan comedy, or an unsettling sense that the world has been arranged too precisely. Corridors, facades, tables, and grouped characters provide natural mirrored structure. The ef…

**Directing the AI.** Lock the camera on the exact center axis of the space and place the subject at the central vanishing point. Mirror major architectural forms, props, spacing, and light levels across the vertical divide. Keep lens height level so lines do not drift. Decide whether the symmetry feels playful, formal, or oppressive through scale and repetition. In video, use stable movement directly along the center…

**Common mistakes.**
- Setting the camera slightly off-axis, causing doorways, ceiling lines, and vanishing points to disagree across the frame.
- Mirroring broad shapes but ignoring light, color, and spacing, leaving the composition balanced only at first glance.
- Breaking symmetry with several unrelated objects, so no single disruption gains the attention or narrative weight it deserves.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: pan_right | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: smooth_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: smooth_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `orbit-ring-title-open`, 130f

**Sources.** [Rules of Shot Composition in Film](None)


### triangular-composition

**"Triangular Composition Prompt for AI Image & Video"** · `composition` · level intermediate

```
Triangular composition with [Subject] arranged to form a triangle within the frame, the apex drawing the eye first then naturally guiding it down along the diagonal lines to the base, shot on a 50mm lens at eye level, the classical compositional structure that Da Vinci and Kurosawa both understood as the geometry of power and stability
```

Arranging key elements to form a triangle within the frame, creating a stable, hierarchical structure that naturally guides the eye between three points of interest. Renaissance painters like Leonardo da Vinci used triangular composition as a foundation — the Mona Lisa and The Last Supper are both built on triangular structures. Akira Kurosawa arranges his samurai in triangular formations for sta…

**When to use.** Triangular composition works when three people, objects, or visual anchors need a stable relationship and clear hierarchy. It suits group dialogue, leadership tableaux, family scenes, and moments where an apex should dominate two supporting points. The eye naturally moves around the triangle, makin…

**Directing the AI.** Choose the dominant subject as the apex and place two secondary anchors lower and farther apart to form the base. Use gaze, shoulders, furniture, or architectural lines to reinforce the triangle without drawing it literally. Keep each point visually distinct and prevent overlapping heads. Adjust height and width to control stability: a broad base feels grounded, while a narrow steep form feels mo…

**Common mistakes.**
- Placing three figures on one horizontal line, which removes the apex and collapses the intended hierarchy.
- Drawing obvious triangular props around the group, making the underlying compositional structure feel literal and forced.
- Overlapping the lower anchors behind the dominant subject, so the three points cannot be read as separate positions.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `spotlight-hero-card`, 220f

**Sources.** [Rules of Shot Composition in Film](None)


### visual-weight

**"Visual Weight Prompt for AI Image & Video"** · `composition` · level intermediate

```
Visual weight study with [Subject] as a small but vivid element carrying visual mass disproportionate to its physical size through isolation, color saturation, and tonal contrast, the composition deliberately exploring how chromatic density creates perceived heaviness independent of actual size, shot on a 35mm lens at f/5.6 with clinical sharpness throughout
```

The perceived heaviness of elements in a composition based on size, color, contrast, texture, and isolation — understanding visual weight is key to creating balanced or deliberately unbalanced frames. Akira Kurosawa demonstrated extraordinary sensitivity to visual weight in "Ran," balancing armies against landscapes with painterly precision. Wes Anderson manipulates visual weight through color —…

**When to use.** Think in visual weight when a composition feels wrong despite correct spacing or grid placement. Brightness, saturated color, sharp detail, isolation, and faces can make a small element outweigh a much larger quiet form. The principle helps balance asymmetrical frames or create deliberate unease. U…

**Directing the AI.** Identify the primary visual mass, then control its size, brightness, color saturation, texture, and isolation. Counter it with another element whose combined qualities create the desired balance, even if its physical size differs. Keep low-priority areas quieter through reduced contrast and detail. Test the eye path from first glance to secondary anchor. For video, account for moving weight: a sm…

**Common mistakes.**
- Balancing objects by physical size alone while ignoring the disproportionate pull of faces, bright highlights, and saturated color.
- Giving every area equal contrast and texture, leaving the frame without a clear hierarchy of perceived importance.
- Adding a vivid counterweight near the edge, accidentally pulling the viewer out of the frame instead of across it.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `orbit-ring-title-open`, 130f

**Sources.** [Rules of Shot Composition in Film](None)


### cross-cutting

**"Cross-Cutting Prompt for AI Image & Video"** · `editing` · level intermediate

```
Cross-cutting between two simultaneous scenes involving [Subject], the alternation between warm and cold tones accelerating in rhythm as both events build toward climax, the visual contrast intensifying the irony, each cut creating a collision of meaning that neither scene could generate alone, warm Kodak tones on one side against cold pushed processing on the other
```

Alternating between two or more scenes happening simultaneously in different locations, building tension by implying convergence and creating dramatic parallels between storylines. D.W. Griffith pioneered cross-cutting in "Intolerance" (1916), intercutting between four historical periods. Christopher Nolan elevated cross-cutting to structural principle in "Inception" and "Dunkirk," weaving three…

**When to use.** Cross-cutting is the right structure when separate events happen at the same time and gain force by being compared. Use it for rescues, pursuits, rituals against violence, parallel decisions, or storylines moving toward collision. Each return should add information or tighten the temporal relations…

**Directing the AI.** Define two distinct locations, visual palettes, and actions occurring simultaneously. Begin with longer sections in each scene, then shorten the alternation as pressure rises. Match gestures, sounds, shapes, or emotional beats across cuts where a collision of meaning helps. Preserve wardrobe, geography, and action continuity within both strands. End at a shared climax, direct convergence, or purp…

**Common mistakes.**
- Alternating locations at a fixed pace without raising stakes, shortening intervals, or revealing a stronger temporal connection.
- Losing continuity inside one strand, so objects, positions, or actions reset each time the edit returns there.
- Pairing scenes with no thematic or causal relationship, making the structure feel arbitrary rather than mutually intensifying.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `beat-cut-accelerando` (beat-cut-moves), 49f, `paparazzi-flash` (beat-cut-moves), 49f

**Sources.** [What Is Film Editing?](None)


### cut-in

**"Cut-In Prompt for AI Image & Video"** · `editing` · level basic

```
Cut-in to a tight close-up of [Subject] revealing a telling detail, shot on a 100mm macro lens at T2, the directorial decision to abandon the wider view and find the truth hiding in a specific detail
```

A cut to a closer shot of something already visible in the wider frame — zooming in on hands, a prop, or a facial detail — focusing attention on a specific element within the scene. Sergio Leone's films are built on the rhythm of wide shots cutting in to extreme close-ups of eyes and gun hands. Quentin Tarantino uses stylized cut-ins to food, drinks, and bare feet as signature moments. David Finc…

**When to use.** Use a cut-in when an element already present in the master view deserves sudden emphasis. Hands tightening around a glass, a hidden message on a screen, or a flicker in someone's eye can redirect the scene without changing location. It works best when the audience first understands the wider geogra…

**Directing the AI.** Compose a clear wider view where the detail is visible, then cut to a much tighter angle on that same element. Preserve hand position, object orientation, wardrobe, light direction, and screen direction across the edit. Use shallow depth of field and exact focus to make the detail dominant. Time the cut at the instant the information becomes consequential. Return wide only after the close view ha…

**Common mistakes.**
- Introducing a detail that was absent from the wider shot, breaking continuity and visual credibility.
- Using nearly identical framing for both shots, so the editorial emphasis feels weak and indecisive.
- Cutting closer without a narrative reason, turning a precise attention cue into empty visual punctuation.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `circle-match-iris`, 30f

**Sources.** [What Is Film Editing?](None)


### cutaway

**"Cutaway Prompt for AI Image & Video"** · `editing` · level basic

```
Cutaway to [Subject] isolated in tight framing, the mundane object suddenly loaded with meaning by its context, shot on a 100mm macro lens with the background softly blurred, warm tungsten light, the Hitchcock principle that showing the ticking clock is more suspenseful than showing the argument
```

A brief cut to something outside the main action — a clock on the wall, a nervous hand, a landscape outside — adding context, creating pacing, or building parallel meaning. Yasujiro Ozu's famous "pillow shots" are extended cutaways to empty spaces, clotheslines, and chimneys that provide contemplative breathing room between scenes in "Tokyo Story." Hitchcock uses cutaways to ticking bombs and dri…

**When to use.** Use a cutaway when the main action needs a breath, a clue, or a pressure point outside the immediate exchange. A clock can tighten suspense, an idle hand can expose anxiety, and an empty room can let emotion settle. It is especially useful between dialogue beats, during transitions, or whenever the…

**Directing the AI.** First establish the main scene, then isolate one nearby object or environmental detail in tight framing. Keep its lighting, time of day, and production design consistent with the wider action. Reduce background information with shallow focus, but make the chosen detail unmistakable. Hold long enough for the audience to register its meaning, then return to the action. The cutaway should alter how…

**Common mistakes.**
- Choosing a random object with no emotional, narrative, or rhythmic connection to the surrounding scene.
- Changing the light or setting so sharply that the cutaway feels borrowed from another sequence.
- Holding on the detail after its meaning is clear, draining tension instead of sharpening it.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `circle-match-iris`, 30f

**Sources.** [What Is Film Editing?](None)


### dissolve

**"Dissolve Prompt for AI Image & Video"** · `editing` · level basic

```
Dissolve transition with two overlapping images of [Subject], both simultaneously visible for a long four-second overlap, the soft double-exposure quality of two temporalities occupying one image, warm sepia tones mixing with saturated color, the nostalgic ache of time-dissolving cinema
```

One image gradually fades out as the next fades in, both visible simultaneously during the transition, suggesting the passage of time, a dream state, or a thematic connection. Ingmar Bergman used dissolves as emotional bridges in "Wild Strawberries," where the overlap between present and memory becomes the film's central visual metaphor. Terrence Malick uses extended dissolves in "The Tree of Lif…

**When to use.** A dissolve fits transitions where two images should coexist before one replaces the other. Use it for memory, elapsed time, dreams, emotional association, or visual comparison across places and periods. Longer overlaps feel fluid and contemplative; shorter ones work as gentle passage. Choose images…

**Directing the AI.** Select an outgoing and incoming shot with compatible focal areas or deliberately contrasting meanings. Fade the first image down while the second rises over a defined duration, allowing both to remain visible through the middle. Align faces, horizons, objects, or light shapes when their overlap should create a third meaning. Keep exposure controlled so the center does not become washed out. Prese…

**Common mistakes.**
- Dissolving between equally busy images, creating a cluttered middle where neither subject nor thematic connection remains readable.
- Letting faces or objects deform into each other, turning a layered transition into an unintended morphing effect.
- Using the same dissolve length for every transition, regardless of whether the story calls for tenderness, passage, or disorientation.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: pan_right | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: smooth_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: smooth_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `black-card-transition` (shot-transitions), `dark-tunnel-transition` (shot-transitions), `focus-handoff-transition` (shot-transitions), `mask-wipe-real` (shot-transitions), `portal-wipe-v2` (shot-transitions), `whip-brake-real` (shot-transitions), `whip-pan-real` (shot-transitions)

**Sources.** [What Is Film Editing?](None)


### fade-in-out

**"Fade In/Out Prompt for AI Image & Video"** · `editing` · level basic

```
Fade to black from [Subject], the image gradually losing luminance over six seconds as the figure becomes shadow and the shadow becomes part of the darkness, the fade so gradual that the exact moment of disappearance is unidentifiable, the emotional weight of permanent conclusion, the visual equivalent of a long exhale
```

The image gradually appears from or disappears to black (or white) — fade to black signals an ending or major time passage while fade from black signals a new beginning or chapter. The Coen Brothers use long, slow fades to black as chapter markers in "No Country for Old Men," each fade feeling like a door closing permanently. Kubrick's fade to white at the end of "2001" suggests transcendence. Ma…

**When to use.** Fade in or out when the story needs a clear boundary rather than a direct visual connection between shots. A fade to black can close a chapter, suggest long passage, or let consciousness recede; a fade from black can establish a beginning or return. The duration carries meaning. Use a fast fade for…

**Directing the AI.** Choose whether the image enters from black, leaves into black, or uses white for a distinctly brighter transition. Set an exact duration and preserve the shot's composition while luminance changes evenly. For a slow fade, let details disappear in tonal order until the subject merges with darkness; for a fade in, reverse that emergence cleanly. Keep the final black or white hold long enough to reg…

**Common mistakes.**
- Treating a fade as a default scene change, weakening the strong sense of chapter, ending, or passage it communicates.
- Changing exposure unevenly across objects, making the transition look like lighting failure rather than the entire image receding.
- Cutting away before full black has time to register, reducing the emotional closure and structural pause.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `chip-grid-single-select-blackout`, 150f

**Sources.** [What Is Film Editing?](None)


### fast-motion

**"Fast Motion Prompt for AI Image & Video"** · `editing` · level basic

```
Fast motion sequence of [Subject] accelerated to four times normal speed, the slight jerkiness of undercranked footage adding comedic effect, every movement purposeful but absurdly accelerated, the Buster Keaton energy of a body moving faster than physics allows, warm light consistent but shadows racing across surfaces
```

Footage played back faster than it was captured, compressing real-time action to create comedy, frenetic energy, or an accelerated sense of unstoppable momentum. Buster Keaton and Charlie Chaplin used undercranking to create the frenetic comedy of the silent era. Stanley Kubrick used fast motion for the threesome scene in "A Clockwork Orange" set to William Tell's Overture. Guy Ritchie employs sp…

**When to use.** Use fast motion for compressed routines, frantic escapes, mechanical work, comic physicality, or bursts of momentum that would drag at normal speed. It is strongest when the audience already understands the action and can enjoy its accelerated rhythm. Use it selectively inside a sequence; sustained…

**Directing the AI.** Stage the action in a readable wide or medium frame, then specify playback at roughly four times normal speed. Keep movement paths simple, purposeful, and continuous so acceleration remains legible. Let bodies and props carry a slight undercranked jerkiness when comedy is wanted, but preserve stable backgrounds and consistent light. Use racing shadows only if time itself is passing. End on a clea…

**Common mistakes.**
- Accelerating complicated blocking until characters overlap, props teleport, and the audience can no longer follow cause and effect.
- Using fast motion for emotionally delicate acting, where facial nuance and hesitation need real duration to register.
- Mixing rapid playback with uncontrolled camera shake, producing visual noise instead of comic or kinetic rhythm.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | **null** | kling-1.5 | no |
| `luma` Luma Dream Machine | **null** | dream-machine | no |
| `mj61` Midjourney v6.1 | **null** | v6.1 | no |
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | **null** | gen-3-alpha | no |
| `sora` OpenAI Sora | **null** | sora-1 | no |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `freeze-annotate-real` (speed-ramp-freeze), 40f, `speed-ramp-real` (speed-ramp-freeze), 40f

**Sources.** [What Is Film Editing?](None)


### freeze-frame

**"Freeze Frame Prompt for AI Image & Video"** · `editing` · level basic

```
Freeze frame of [Subject] caught at the precise instant of peak emotional or physical expression, the film grain suddenly visible as motion stops, the abrupt silence of a world frozen in time, movement arrested as an editorial exclamation point, Kodak Tri-X black and white grain, the immortality of a single stolen instant
```

Action suddenly stops as a single frame is held on screen — the exclamation point of cinema, used for endings, revelations, or comic emphasis. François Truffaut's freeze frame ending of "The 400 Blows" — young Antoine Doinel reaching the sea and turning to look directly at the camera as the image freezes — is one of cinema's most iconic final images. Martin Scorsese uses the freeze frame througho…

**When to use.** Freeze frame belongs at an instant the audience should inspect, remember, or carry beyond normal time. Use it for endings, revelations, introductions, comic emphasis, or peak physical and emotional expression. The chosen image needs a strong silhouette and readable face or action because motion can…

**Directing the AI.** Build motion toward one precise peak, then hold that exact frame without interpolation, camera drift, or living background movement. Choose a moment with clear gesture, expression, and composition, not a transitional blur. Let texture or grain become visible once motion stops, and decide whether sound cuts, continues, or drops to silence. Hold long enough for the image to change meaning through d…

**Common mistakes.**
- Freezing on a motion-blurred transition frame where hands, face, or body position cannot carry a clear idea.
- Allowing hair, smoke, background figures, or camera movement to continue, turning the freeze into selective visual failure.
- Using multiple freezes without structural reason, reducing a decisive editorial gesture to a repetitive surface style.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `domino-cascade` (montage-rhythm-moves), 129f, `drop-blackout-slam` (montage-rhythm-moves), 129f, `wright-triple-cut` (montage-rhythm-moves), 129f

**Sources.** [What Is Film Editing?](None)


### iris-transition

**"Iris Prompt for AI Image & Video"** · `editing` · level basic

```
Iris transition closing concentrically around [Subject] at center frame, the circular black mask tightening from edges like a closing eye, the world progressively swallowed by darkness until only a small disc remains, the charming self-awareness of silent cinema technique, warm sepia-inflected tones suggesting aged film stock
```

A circular aperture opens or closes on the frame, focusing attention on a specific point — an early cinema technique that has seen a modern revival for its charming, self-aware quality. D.W. Griffith and Buster Keaton used iris shots extensively in the silent era to direct attention and create transitions. The technique fell out of favor with the arrival of sound but has been revived by directors…

**When to use.** Use an iris when you want to end on a face, object, or gesture with unmistakable theatrical emphasis. It suits chapter endings, comic exits, storybook framing, and affectionate references to early cinema. Because the device announces itself, reserve it for sequences with formal playfulness or nosta…

**Directing the AI.** Place the chosen subject precisely at the center or selected focal point. Close a circular black mask concentrically from the frame edges, keeping the remaining image stable as the visible disc shrinks. For an opening iris, reverse the movement and reveal the scene around the point of interest. Use warm, slightly aged color and restrained grain if nostalgia fits. Finish on full black or a fully o…

**Common mistakes.**
- Misplacing the subject so the closing circle drifts away from the intended emotional or comic focus.
- Combining the iris with excessive motion, making the audience chase the subject inside a shrinking frame.
- Applying aged color and grain so heavily that the transition becomes parody rather than affectionate reference.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `circle-match-iris`, 30f

**Sources.** [What Is Film Editing?](None)


### jump-cut

**"Jump Cut Prompt for AI Image & Video"** · `editing` · level basic

```
Jump cut sequence of [Subject] with the background and position shifting abruptly between cuts while the camera angle remains essentially the same, the jarring temporal discontinuity making time feel broken and reassembled, each cut a tiny violence against smooth continuity, shot on handheld 16mm with rough grain and blown-out highlights, the French New Wave rebellion against invisible editing
```

A cut between two sequential shots of the same subject from a similar angle, creating a jarring jump in time — once considered a mistake, now used intentionally for energy, anxiety, or time compression. Jean-Luc Godard made the jump cut famous in "Breathless" (1960), using it partly out of necessity to trim a too-long film and partly as a deliberate rejection of smooth Hollywood continuity. The t…

**When to use.** Use a jump cut when smooth continuity would hide the anxiety, speed, boredom, or fragmentation inside a moment. It can compress repeated action, expose missing time, or make a performance feel unstable. Keep camera angle and subject similar enough that the temporal jump reads clearly. The cut shoul…

**Directing the AI.** Lock a similar camera angle and framing across several sequential moments, then remove the connecting motion between them. Let the subject's pose, background position, or object state jump forward while the setup remains recognizably the same. Keep each discontinuity sharp, with no dissolve or smoothing. Vary interval length to shape rhythm without losing the pattern. Maintain identity, wardrobe,…

**Common mistakes.**
- Changing angle, lens, and location together, which reads as a conventional cut instead of a temporal jump.
- Smoothing the discontinuity with motion interpolation or dissolves, removing the jolt that gives the technique its character.
- Allowing the subject's identity or wardrobe to drift between cuts, turning intentional fragmentation into continuity failure.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: pan_right | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: smooth_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: smooth_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `beat-cut-accelerando` (beat-cut-moves), 49f, `paparazzi-flash` (beat-cut-moves), 49f

**Sources.** [What Is Film Editing?](None)


### long-take

**"Long Take Prompt for AI Image & Video"** · `editing` · level advanced

```
Long unbroken take following [Subject] in real time through continuous space, the single take creating immersive experience where the viewer is trapped in real-time, shot on Steadicam with an ARRI Alexa Mini and 21mm Zeiss lens, the shifting light creating a natural color temperature journey, the unbroken continuity refusing to let the viewer escape into a cut
```

An extended shot that runs significantly longer than conventional cuts, building real-time tension, showcasing performance, and immersing the viewer in unbroken space and time. Alfonso Cuarón and Emmanuel Lubezki pushed the long take to new extremes in "Children of Men" with the legendary six-minute car ambush, and later in "Gravity" and "Roma." Alejandro González Iñárritu's "Birdman" is construc…

**When to use.** A long take works when real-time duration, spatial continuity, or performance tension should trap the audience inside the event. Use it for entrances, conversations that shift power, journeys through complex space, action with readable geography, or patient observation. The shot must evolve interna…

**Directing the AI.** Plan one uninterrupted route with a clear starting frame, several blocking beats, and a decisive endpoint. Move the camera only when subject action or a reveal motivates it, preserving stable geography and consistent screen direction. Coordinate focus, exposure, and background activity as the shot enters new zones. Let performers cross foreground and background without identity drift. Avoid hidde…

**Common mistakes.**
- Letting the camera wander without new blocking, information, or pressure, confusing duration with meaningful immersion.
- Changing doors, props, extras, or subject identity mid-shot, breaking the continuous space the technique depends on.
- Hiding obvious cuts behind every passing object, reducing an unbroken performance into a stitched visual trick.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `crane-rise-reveal`, 20f

**Sources.** [What Is Film Editing?](None)


### montage

**"Montage Prompt for AI Image & Video"** · `editing` · level basic

```
Montage sequence compressing time around [Subject], each shot shorter than the last as momentum accelerates, the editing rhythm itself building like a crescendo, culminating in a final sustained shot of completion, the cinematic time machine that compresses months into two minutes of escalating visual rhythm
```

A sequence of short shots edited together to compress time, convey information, or build emotional momentum — from training sequences to falling-in-love sequences, montage is cinema's time machine. Sergei Eisenstein theorized montage as cinema's unique art form in the 1920s, and his Odessa Steps sequence in "Battleship Potemkin" remains the most studied montage in film history. Rocky Balboa's tra…

**When to use.** Montage is built for change that matters but does not need to unfold in real time. Use it for training, travel, construction, research, falling in love, decline, or any process with visible milestones. Each shot should advance the state, not repeat the same information. Rhythm can accelerate toward…

**Directing the AI.** Define the process and list a sequence of distinct visual milestones. Start with longer shots that establish the task, then tighten duration as competence, urgency, or accumulation grows. Use repeated actions, matched framing, or recurring objects to show measurable change. Vary shot scale while preserving subject and environment continuity. Build toward one sustained payoff image rather than sto…

**Common mistakes.**
- Repeating attractive shots that show no new milestone, making the sequence energetic but narratively static.
- Accelerating cuts before the process is established, so the audience cannot understand what activity or change is being compressed.
- Ending on another brief fragment instead of a clear payoff that confirms completion, failure, or transformation.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: pan_right | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: smooth_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: smooth_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `beat-cut-accelerando` (beat-cut-moves), 49f, `paparazzi-flash` (beat-cut-moves), 49f

**Sources.** [What Is Film Editing?](None)


### reaction-shot

**"Reaction Shot Prompt for AI Image & Video"** · `editing` · level basic

```
Reaction shot close-up of [Subject] capturing the exact moment of emotional impact, the eyes widening, jaw muscles clenching, every micro-expression playing across the face in three seconds, soft directional light illuminating every subtle muscular change, shot on an 85mm lens with eyes along the upper third, the Spielberg technique of making the audience feel an event through its reflection on a human face
```

A cut to a character's facial response to an event, dialogue, or revelation — often more powerful than showing the action itself, as it lets the audience experience the emotional impact. Spielberg understands this deeply: in "Schindler's List," we often see Oskar Schindler's face reacting to horror rather than the horror itself, and the reaction is more devastating. Hitchcock said "the size of th…

**When to use.** Use a reaction shot when the audience should experience an event through its effect on a person rather than through spectacle alone. It is crucial for revelations, fear, grief, comedy, attraction, and shifts in power. The size and duration should match the importance of the information. Hold long e…

**Directing the AI.** Establish what the character sees or hears, then cut to a close view at the first instant of impact. Keep eye line consistent with the preceding shot and frame the eyes clearly. Direct a sequence of small physical changes: focus shift, tightened jaw, held breath, widened eyes, or a delayed blink. Let the response develop for several beats before cutting away. Preserve facial identity and lighting…

**Common mistakes.**
- Showing the reaction before the triggering information, confusing cause and effect unless deliberate anticipation is the point.
- Pushing every facial feature into extreme expression, replacing specific emotional discovery with broad, unreadable melodrama.
- Breaking eye line or lighting continuity, making the close-up feel detached from the event and surrounding space.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `anime-impact` (impact-feedback), `hit-counter` (impact-feedback)

**Sources.** [What Is Film Editing?](None)


### reverse-motion

**"Reverse Motion Prompt for AI Image & Video"** · `editing` · level basic

```
Reverse motion of [Subject] with the uncanny wrongness of reversed physics where entropy runs backward, fragments finding their original positions as if remembering where they belonged, shot originally on high-speed Phantom camera for smooth motion when reversed, the David Lynch surrealism of a world where time moves the wrong way
```

Footage played backwards, creating surreal, uncanny, or magical effects where broken things reassemble, fallen objects rise, and the familiar becomes alien. Jean Cocteau used reverse motion to create magical effects in "Orpheus" and "Beauty and the Beast" without any optical trickery. David Lynch employs reversed footage in "Twin Peaks" for the Red Room sequences, where actors learned their dialo…

**When to use.** Use reverse motion when ordinary physics should feel wrong: shattered material rebuilding, spilled liquid climbing upward, smoke returning to a source, or a fallen figure rising. It can signal magic, temporal disruption, surrealism, or unease. Choose actions with a clear irreversible direction in r…

**Directing the AI.** Begin from the completed aftermath, then choreograph every fragment, droplet, or particle traveling backward along a coherent path toward its original form. Keep trajectories smooth and collisions physically traceable, even though causality is reversed. Use steady framing and even illumination so the temporal wrongness remains the dominant effect. Preserve the subject's identity through the motio…

**Common mistakes.**
- Reversing an action with no obvious directional logic, leaving the audience unsure whether anything unusual happened.
- Allowing fragments to appear from nowhere instead of retracing believable paths toward the restored object.
- Adding unrelated warping and color effects that distract from the simple uncanny power of backward physics.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | **null** | kling-1.5 | no |
| `luma` Luma Dream Machine | **null** | dream-machine | no |
| `mj61` Midjourney v6.1 | **null** | v6.1 | no |
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | **null** | gen-3-alpha | no |
| `sora` OpenAI Sora | **null** | sora-1 | no |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `crash-impact-real` (crash-zoom-punch), 11f, `crash-zoom-real` (crash-zoom-punch), 11f

**Sources.** [What Is Film Editing?](None)


### smash-cut

**"Smash Cut Prompt for AI Image & Video"** · `editing` · level basic

```
Smash cut from absolute serenity to total chaos involving [Subject], an instantaneous hard cut with no transition, no preparation, the tonal whiplash so extreme the viewer physically reacts, the editorial equivalent of a slap, the technique that weaponizes the cut itself as a storytelling instrument
```

An abrupt, jarring cut between two vastly different scenes — often from quiet to loud, calm to chaos, or a character saying "nothing could go wrong" to everything going wrong. Edgar Wright is the modern master of the smash cut, using it for comedic whiplash throughout "Shaun of the Dead" and "Hot Fuzz." Kubrick's smash cut from the bone to the satellite in "2001" is the most dramatic temporal sma…

**When to use.** Use a smash cut when the transition itself should trigger shock, comedy, dread, or a sudden change of scale and time. The strongest versions collide opposite states: quiet with noise, stillness with motion, confidence with failure, or intimacy with vastness. Build enough calm or expectation before…

**Directing the AI.** Construct two shots with sharply opposed tone, volume, motion, palette, or scale. Hold the first long enough to establish its state, then cut instantly at the most vulnerable or ironic beat. Use no dissolve, flash, or transitional smoothing. Make the opening frame of the second shot immediately legible and maximally different. Preserve intentional continuity only where a matched shape or phrase s…

**Common mistakes.**
- Adding a flash, blur, or speed ramp between scenes, cushioning the hard collision that should create the reaction.
- Cutting between scenes with similar motion and tone, leaving too little contrast for real editorial whiplash.
- Repeating smash cuts throughout a sequence, training the audience to expect them and draining their surprise.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `anime-impact` (impact-feedback), `hit-counter` (impact-feedback)

**Sources.** [What Is Film Editing?](None)


### split-screen

**"Split Screen Prompt for AI Image & Video"** · `editing` · level intermediate

```
Split screen dividing the frame with [Subject] visible in both halves simultaneously, one side warm-toned and the other cool-toned, the vertical divide becoming the physical and emotional distance, the De Palma technique of making the audience omniscient observers of parallel realities occupying the same frame
```

The frame is divided into two or more sections, each showing a different angle, location, or timeline simultaneously, showing parallel action, phone conversations, or multiple perspectives at once. Brian De Palma made split screen his signature, using it in "Carrie," "Dressed to Kill," and "Snake Eyes" to create impossible simultaneity. Ang Lee used complex multi-panel split screens in "Hulk" to…

**When to use.** Split screen is effective when the audience needs simultaneous access to separate locations, angles, timelines, or perspectives. Use it for phone calls, parallel action, surveillance, comparison, duality, or events whose timing matters more than spatial unity. Each panel needs a clear function and…

**Directing the AI.** Divide the canvas into two or more clean panels with explicit proportions and boundaries. Assign each panel a location, palette, camera angle, and action, then synchronize moments that should connect across the divide. Keep identities and environments stable within their own sections. Control attention by varying motion, contrast, or duration so only one panel dominates at a time. Prevent limbs,…

**Common mistakes.**
- Filling every panel with equally intense movement, forcing the viewer to miss essential actions happening at the same time.
- Changing panel sizes and borders without narrative purpose, making the layout feel unstable rather than intentionally dynamic.
- Allowing character features or backgrounds to drift between panels, weakening the distinction between separate locations or perspectives.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `scanline-assemble-flyin`, 138f

**Sources.** [What Is Film Editing?](None)


### time-lapse

**"Time-Lapse Prompt for AI Image & Video"** · `editing` · level intermediate

```
Time-lapse of [Subject] compressed from hours into seconds, light cycling through the full spectrum of the day, shadows rotating like sundial hands, the entire rhythm of existence compressed into a single visual breath, shot on a locked-off camera with an intervalometer, the Koyaanisqatsi revelation that accelerating time reveals patterns invisible to human perception
```

Capturing frames at intervals much slower than playback speed, compressing hours, days, or months into seconds to reveal processes invisible to normal perception — clouds racing, cities pulsing. Ron Fricke's "Koyaanisqatsi" (with Philip Glass's score) turned time-lapse into transcendent art, showing the rhythms of nature and civilization accelerated into hypnotic visual music. Terrence Malick use…

**When to use.** Use time-lapse when the story needs to show a process whose scale exceeds ordinary screen time: daylight crossing a room, clouds building, streets filling, or a structure changing. It can bridge hours, mark labor, reveal systems, or turn gradual transformation into visual rhythm. The technique work…

**Directing the AI.** Lock the camera and define a clear start state, end state, and visible process between them. Keep permanent architecture and horizon lines stable while clouds, shadows, traffic, people, or growth accelerate through frame. Describe light cycling across a believable path, with shadows rotating consistently rather than flickering randomly. Maintain one composition throughout. Compress duration aggre…

**Common mistakes.**
- Moving the camera without purpose, which hides the gradual pattern that time compression is meant to reveal.
- Accelerating every element equally, making solid buildings wobble or permanent objects mutate with passing time.
- Providing no distinct beginning or ending state, so the sequence feels busy without communicating change.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | **null** | kling-1.5 | no |
| `luma` Luma Dream Machine | **null** | dream-machine | no |
| `mj61` Midjourney v6.1 | **null** | v6.1 | no |
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | **null** | gen-3-alpha | no |
| `sora` OpenAI Sora | **null** | sora-1 | no |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `freeze-annotate-real` (speed-ramp-freeze), 40f, `speed-ramp-real` (speed-ramp-freeze), 40f

**Sources.** [What Is Film Editing?](None)


### wipe-transition

**"Wipe Prompt for AI Image & Video"** · `editing` · level basic

```
Wipe transition with [Subject] in one scene being pushed off frame by an incoming scene sliding in, the geometric wipe edge a clean vertical line, both scenes fully lit and composed as complete images on either side, the nostalgic energy of adventure serials, the self-aware playfulness of a transition that announces itself as a storytelling device
```

One shot pushes another off screen in a defined geometric pattern — a signature of Star Wars and classic serials that adds kinetic energy and a retro, adventurous feel. George Lucas adopted the wipe transition directly from Akira Kurosawa's "The Hidden Fortress" for "Star Wars," making it the saga's most recognizable editorial device. The wipe was common in 1930s and 40s adventure serials that Lu…

**When to use.** Use a wipe when the transition itself should be felt: a chapter change, geographic jump, comic beat, or deliberate nod to classic adventure serials. It carries more personality than a neutral cut and more momentum than a dissolve. Choose it for stylized worlds that can support visible editorial gra…

**Directing the AI.** Design two fully resolved shots with compatible visual weight on opposite sides of the transition. Move a clean vertical, horizontal, or shaped boundary steadily across frame until the incoming scene replaces the outgoing one. Keep the wipe edge crisp and the speed confident, without smearing subjects together. Coordinate directional movement so the new composition feels pushed into place. Let bo…

**Common mistakes.**
- Using a wipe inside an otherwise invisible edit style, making one transition feel accidentally theatrical.
- Leaving either scene undercomposed because the creator planned only the final frame, not the moving boundary.
- Adding blur or dissolve at the edge, which weakens the clean geometric character of the technique.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `color-block-step-wipe`, 44f

**Sources.** [What Is Film Editing?](None)


### breaking-fourth-wall

**"Breaking the Fourth Wall Prompt for AI Image & Video"** · `narrative` · level intermediate

```
[Subject] suddenly turning to look directly into the camera lens with a knowing expression, the other figures frozen in their activity unaware of the breach, the direct eye contact creating an instant conspiratorial bond with the viewer, the camera positioned exactly where an observer would be making the viewer complicit, the Fleabag-Ferris Bueller intimacy of a character who trusts the audience more than anyone in their own world
```

A character directly addresses or acknowledges the audience, shattering the illusion of the fictional world to create intimacy, comedy, or existential awareness. Groucho Marx was an early master, but the technique reached its dramatic potential when Ingmar Bergman had actors stare into the camera in "Persona" and "Summer with Monika." Ferris Bueller's conspiratorial monologues to the audience in…

**When to use.** Use breaking the fourth wall when the character should recruit the audience as confidant, witness, judge, or accomplice. A glance can land a joke; sustained address can expose a private truth or rupture the fictional world. Establish normal scene behavior first so the breach has force. The techniqu…

**Directing the AI.** Position the camera exactly where an observer would stand, at the character's eye level. Let the surrounding action continue or briefly freeze while the subject turns and fixes direct, unwavering eye contact on the lens. Keep the expression specific: conspiratorial, accusatory, amused, or exposed. Other characters should remain unaware unless the story demands a larger rupture. Hold the gaze long…

**Common mistakes.**
- Having every figure look into camera, which destroys the private bond between one character and the audience.
- Using a vague neutral expression when the direct gaze needs a precise comic or dramatic intention.
- Beginning with direct address before establishing the fictional space, leaving no illusion for the character to break.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `cursor-flyover`, 180f

**Sources.** [How to Make a Short Film: An Introduction to Filmmaking](None)


### cliffhanger

**"Cliffhanger Prompt for AI Image & Video"** · `narrative` · level basic

```
Cliffhanger moment frozen at peak suspense with [Subject], the image capturing the exact instant before resolution, the viewer's need for closure weaponized into desperate anticipation, dramatic sidelighting creating hard shadows that emphasize physical strain, the visual language of unresolved tension that demands continuation
```

Ending a scene, episode, or act at a moment of peak suspense, leaving the outcome unresolved and exploiting the human need for closure to keep audiences desperate for more. The term comes from Thomas Hardy's serialized novel "A Pair of Blue Eyes," where a character literally hangs from a cliff. "The Empire Strikes Back" ends on one of cinema's greatest cliffhangers — Han frozen in carbonite, Luke…

**When to use.** Use a cliffhanger at an act, episode, or scene break when the unresolved outcome can pull the audience forward. The best version stops after the stakes are understood but before the decisive action, answer, or consequence arrives. It works for physical danger, revelations, choices, and emotional co…

**Directing the AI.** Build toward one irreversible beat, then frame the exact instant before impact, response, escape, or revelation. Use hard side light, compressed space, strained posture, and a clear eyeline toward the unresolved threat. Let the final image contain the question visually without explaining it in text. Cut away before movement completes, not before the audience understands what may happen. Preserve…

**Common mistakes.**
- Ending before the stakes are visible, creating simple interruption rather than suspenseful unresolved pressure.
- Resolving the dangerous action inside the final frame, then pretending the aftermath is still a cliffhanger.
- Using cliffhangers repeatedly without satisfying prior questions, which converts anticipation into audience distrust.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `domino-cascade` (montage-rhythm-moves), 129f, `drop-blackout-slam` (montage-rhythm-moves), 129f, `wright-triple-cut` (montage-rhythm-moves), 129f

**Sources.** [How to Make a Short Film: An Introduction to Filmmaking](None)


### flashback

**"Flashback Prompt for AI Image & Video"** · `narrative` · level basic

```
Flashback scene with [Subject] rendered in slightly overexposed warm-shifted tones, the image softer than present-day as if viewed through the imperfect lens of recollection, the color palette pushed toward amber and gold, lens flares and halation giving the image dreamy luminous quality, Kodak Vision3 50D pushed and cross-processed for vintage nostalgic look, the Malick-Lubezki language of memory as golden light
```

A scene that takes the audience back to an earlier point in time, revealing backstory, providing context for present behavior, or recontextualizing what we thought we knew. "Citizen Kane" is structured entirely around flashbacks as reporters investigate Charles Foster Kane's life. Francis Ford Coppola's "The Godfather Part II" masterfully interweaves flashbacks of young Vito Corleone with the pre…

**When to use.** Use a flashback when past experience must explain present behavior, reveal missing context, or challenge what the audience assumed. It works best when the return to the past has a specific dramatic purpose rather than serving as an information dump. Sensory fragments can express unreliable or emoti…

**Directing the AI.** Distinguish the remembered scene with a controlled visual system: warmer amber light, softer contrast, slight overexposure, gentle halation, or selective grain. Keep faces and important actions readable beneath the treatment. Build the transition around a matching object, sound cue, gesture, or composition that links present and past. Let imperfections suggest recollection, but maintain spatial c…

**Common mistakes.**
- Using warm color alone without a narrative anchor, making the flashback resemble a random grade change.
- Explaining backstory the present scene already communicates, which stalls momentum instead of deepening character.
- Softening every detail until actions and faces become vague, sacrificing comprehension for a generic dream look.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: pan_right | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: smooth_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: smooth_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `black-card-transition` (shot-transitions), `dark-tunnel-transition` (shot-transitions), `focus-handoff-transition` (shot-transitions), `mask-wipe-real` (shot-transitions), `portal-wipe-v2` (shot-transitions), `whip-brake-real` (shot-transitions), `whip-pan-real` (shot-transitions)

**Sources.** [How to Make a Short Film: An Introduction to Filmmaking](None)


### flashforward

**"Flashforward Prompt for AI Image & Video"** · `narrative` · level intermediate

```
Flashforward showing [Subject] in a future state, the visual treatment cooler and more desaturated than present-day scenes, the camera positioned in the same angle as earlier shots to make the change more devastating by comparison, the flashforward creating dramatic irony as the audience now carries knowledge of this future while watching the present unfold
```

A scene that jumps ahead to show future events before returning to the present timeline, creating dramatic irony, dread, or anticipation by revealing a destination before the journey. Nicolas Roeg used flashforwards brilliantly in "Don't Look Now," where glimpses of the future create a web of dread throughout the film. "Breaking Bad" famously opens seasons with enigmatic flashforwards — the machi…

**When to use.** Use a flashforward when knowing the destination will make the journey more charged. Show a future injury, altered relationship, ruined place, or unexplained object, then return to the present while the audience carries that knowledge. It is effective for dread and dramatic irony, especially when th…

**Directing the AI.** Repeat a present-day camera angle in the future so changes become immediately comparable. Shift the future toward cooler, restrained color, altered light, and visible consequences while preserving recognizable architecture, wardrobe cues, or props. Keep the glimpse concise and focus on one unanswered change. Transition back through a visual match or sharp temporal cut. The audience should recogni…

**Common mistakes.**
- Changing every visual element at once, so the future no longer connects clearly to the present timeline.
- Showing the complete chain of events, removing the dramatic question that should energize the present story.
- Treating the future as a generic dream with no stable detail the audience can remember or track.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `black-card-transition` (shot-transitions), `dark-tunnel-transition` (shot-transitions), `focus-handoff-transition` (shot-transitions), `mask-wipe-real` (shot-transitions), `portal-wipe-v2` (shot-transitions), `whip-brake-real` (shot-transitions), `whip-pan-real` (shot-transitions)

**Sources.** [How to Make a Short Film: An Introduction to Filmmaking](None)


### foreshadowing

**"Foreshadowing Prompt for AI Image & Video"** · `narrative` · level intermediate

```
Foreshadowing detail hiding in plain sight around [Subject], a seemingly ordinary detail barely visible that the viewer will only recognize as prophetic on a second viewing, every element appearing innocent on first viewing but loaded with ominous meaning in retrospect, warm amber domestic lighting that makes the scene feel safe even as visual clues whisper that safety is temporary
```

Planting subtle hints of events to come — a cracked mirror, a line of dialogue, a color choice — details that seem innocuous on first viewing but become devastating on rewatch. Stanley Kubrick embedded foreshadowing details so densely in "The Shining" that the documentary "Room 237" is dedicated entirely to analyzing them. M. Night Shyamalan structures "The Sixth Sense" so that every scene contai…

**When to use.** Use foreshadowing when a later reveal should feel earned rather than arbitrary. Plant a prop, shape, color, gesture, or line whose first meaning is ordinary and whose second meaning appears only after the outcome. It is ideal for mystery, tragedy, twists, and mounting dread. The clue must be visibl…

**Directing the AI.** Compose a safe, ordinary scene around the main subject, then place one consequential detail near the edge of attention. Match its scale, light, and material to the environment so it belongs there. Avoid isolating it with a spotlight or explicit close-up. Repeat its shape, color, or position later if the pattern matters. On rewatch, the clue should look deliberate; on first viewing, it should rema…

**Common mistakes.**
- Centering and spotlighting the clue so aggressively that the future reveal becomes obvious on first viewing.
- Planting a detail with no later payoff, teaching the audience to distrust the story's visual information.
- Using an unrelated ominous object instead of a clue that connects specifically to the eventual event.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `assemble-then-type-flyin`, 156f

**Sources.** [How to Make a Short Film: An Introduction to Filmmaking](None)


### frame-narrative

**"Frame Narrative Prompt for AI Image & Video"** · `narrative` · level intermediate

```
Frame narrative with [Subject] as the storyteller in warm amber lamplight, the image beginning to dissolve into the story being told, two realities briefly coexisting in the dissolve, the warm domestic frame giving way to the adventure palette of the nested story, the nested structure raising questions about what is real and what has been embellished
```

A story-within-a-story structure — a character tells a tale, and we watch it unfold — creating layers of perspective, questions of reliability, and a satisfying nesting of narratives. Rob Reiner's "The Princess Bride" is a beloved frame narrative, with Peter Falk reading to Fred Savage while the fairy tale plays out. "Titanic" uses a frame narrative of elderly Rose recounting her experience to re…

**When to use.** Use a frame narrative when the act of telling matters as much as the tale. A narrator can filter events through memory, bias, affection, or invention, while the outer scene gives the audience a place to question and interpret the inner story. It suits recollection, legend, testimony, and storybook…

**Directing the AI.** Stage the storyteller in a stable, intimate frame with warm lamplight and a clear listener or storytelling object. Transition into the nested tale through a dissolve, matched gesture, page, photograph, or changing background. Give the inner story a broader palette and different spatial scale, but repeat one visual element from the frame to preserve authorship. When returning, reveal a reaction or…

**Common mistakes.**
- Abandoning the outer frame after the opening, making the storyteller structurally unnecessary to the narrative.
- Giving both narrative layers identical visual treatment, so the transition between teller and tale becomes muddy.
- Using the frame only for exposition instead of allowing perspective or reliability to affect the inner story.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `stroke-segment-build`, 150f

**Sources.** [How to Make a Short Film: An Introduction to Filmmaking](None)


### in-medias-res

**"In Medias Res Prompt for AI Image & Video"** · `narrative` · level basic

```
In medias res with [Subject] dropped without context into the middle of intense action already in progress, no exposition or setup, no explanation, the audience thrown into adrenaline and forced to piece together the story from fragments, handheld camera energy and desaturated color grade, the Tarantino-Nolan principle that starting in the middle makes the audience lean forward
```

Beginning the story in the middle of the action rather than from the chronological start, hooking the audience immediately and creating mystery about how we got here. The technique dates to Homer's Odyssey and has been a staple of cinema since film noir. Quentin Tarantino opens "Reservoir Dogs" in the aftermath of a heist gone wrong, and Christopher Nolan begins "The Dark Knight" mid-robbery. The…

**When to use.** Use in medias res when the opening needs immediate pressure, movement, or mystery. Start after the plan has failed, during the chase, or at the instant a relationship breaks, then let context emerge through behavior and consequences. It suits stories where discovery is part of the pleasure. Even wi…

**Directing the AI.** Open on action already underway: the subject running, hiding, arguing, escaping, or recovering from an unseen event. Use reactive handheld framing, compressed background information, and visible consequences such as damage, breathlessness, or scattered objects. Withhold names and explanations, but make the immediate stakes legible through direction of movement and character focus. Seed two or thr…

**Common mistakes.**
- Withholding every point of orientation, turning deliberate mystery into a scene with no readable objective.
- Stopping the action for immediate exposition, which cancels the momentum created by the opening plunge.
- Staging generic chaos without specific consequences that hint at the unseen events preceding the scene.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `beat-cut-accelerando` (beat-cut-moves), 49f, `paparazzi-flash` (beat-cut-moves), 49f

**Sources.** [How to Make a Short Film: An Introduction to Filmmaking](None)


### motif

**"Motif Prompt for AI Image & Video"** · `narrative` · level intermediate

```
Recurring visual motif with [Subject] appearing for the nth time in the narrative, the viewer now conditioned to feel a specific emotion at the sight, the seemingly mundane detail having accumulated devastating associative weight through repetition, the Coppola technique of training the audience to read a visual symbol through consistent placement, the motif's power residing in the accumulated pattern of meaning
```

A recurring visual, audio, or narrative element that accumulates meaning through repetition — oranges in "The Godfather," mirrors in "Black Swan," water in "The Shape of Water" — patterns that become the story's visual language. Francis Ford Coppola's oranges appear before every death in the Godfather trilogy, creating an association the viewer feels before consciously understanding it. Kubrick u…

**When to use.** Use a motif when a recurring object, color, sound, shape, or gesture can become the story's private vocabulary. Repeat it before related events, around one character, or at emotional turning points so association grows without explanation. A motif should remain recognizable while its context change…

**Directing the AI.** Choose one simple, unmistakable element and define its color, shape, material, and typical frame position. Introduce it in a neutral context, then repeat it across later scenes with consistent identity but changing emotional surroundings. Do not isolate it every time; sometimes let it sit naturally in production design. Increase its prominence only when the accumulated meaning should surface. Pre…

**Common mistakes.**
- Changing the motif's shape or color between scenes until viewers cannot recognize the repeated element.
- Explaining the motif in dialogue, removing the pleasure of association built through visual recurrence.
- Repeating the element in every scene, turning a meaningful pattern into obvious decoration and visual noise.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `icon-field-colorize`, 45f

**Sources.** [How to Make a Short Film: An Introduction to Filmmaking](None)


### non-linear-narrative

**"Non-Linear Narrative Prompt for AI Image & Video"** · `narrative` · level advanced

```
Non-linear narrative visualized with [Subject] existing simultaneously at different moments, each temporal fragment in its own distinct visual world with unique color science, the puzzle-like structure of Nolan and Tarantino made visual, the non-linear principle that chronology is a creative choice rather than an obligation
```

A story told out of chronological order — rearranging time to create mystery, thematic resonance, or a puzzle the audience assembles. Quentin Tarantino's "Pulp Fiction" made non-linear narrative a mainstream phenomenon, while Christopher Nolan's "Memento" pushed it to its logical extreme by running the entire film in reverse. Alejandro González Iñárritu's "21 Grams" fragments three timelines into…

**When to use.** Use a non-linear narrative when reordered time creates mystery, emotional contrast, or thematic resonance that chronology cannot provide. Place consequences before causes, revisit one event from different periods, or interleave temporal fragments that change one another's meaning. Every jump should…

**Directing the AI.** Define each time period with a distinct but related palette, lighting condition, costume state, and environmental detail. Repeat one subject or composition across periods to expose change. Arrange fragments around dramatic meaning rather than random chronology: consequence, cause, contradiction, revelation. Keep screen direction and identity consistent within each period. When moments overlap, sh…

**Common mistakes.**
- Reordering scenes arbitrarily without creating mystery, contrast, or a new relationship between cause and consequence.
- Giving every period identical styling, forcing viewers to guess when events occur from dialogue alone.
- Overloading each fragment with clues, making the structure feel like a puzzle interface instead of lived drama.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `circle-match-iris`, 30f

**Sources.** [How to Make a Short Film: An Introduction to Filmmaking](None)


### parallel-storylines

**"Parallel Storylines Prompt for AI Image & Video"** · `narrative` · level advanced

```
Parallel storylines with [Subject] shown across multiple distinct visual quadrants happening simultaneously, each in its own color world and emotional register yet connected by theme, the Altman-Anderson principle that the world is a symphony of simultaneous stories, the invisible threads connecting lives that share a time without knowing it
```

Multiple narrative threads running simultaneously, often converging at key moments, creating thematic parallels and enriching the story by showing how different characters experience the same world. Robert Altman pioneered the multi-storyline film with "Nashville" and "Short Cuts," weaving dozens of characters into tapestries of intersecting lives. Paul Thomas Anderson followed with "Magnolia," w…

**When to use.** Use parallel storylines when different characters, places, or times can illuminate the same theme from contrasting angles. The threads may share an event, echo one another, or converge physically at a climax. Give each storyline its own immediate desire and visual identity; none should exist merely…

**Directing the AI.** Assign each thread a distinct location, palette, light quality, framing rhythm, and recurring subject. Show simultaneous action through alternating shots or clearly divided compositions, keeping each world internally consistent. Link the threads with matched gestures, shapes, weather, or objects without pretending they occupy the same space. Increase the frequency of transitions as convergence ap…

**Common mistakes.**
- Giving one storyline all meaningful action while the others function only as decorative interruptions.
- Using identical locations and palettes, making simultaneous threads difficult to identify at a glance.
- Forcing convergence through coincidence without planting shared causes, spaces, objects, or thematic pressure beforehand.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `split-flap-flip` (split-flap-title), 140f

**Sources.** [How to Make a Short Film: An Introduction to Filmmaking](None)


### symbolism

**"Symbolism Prompt for AI Image & Video"** · `narrative` · level intermediate

```
Visual symbolism with [Subject] carrying abstract meaning beyond its literal form, the image precisely rendered to communicate truths that language cannot reach, the composition treating the symbol with the reverence of a monument — centered, solitary, given maximum visual space, the Tarkovsky understanding that a concrete image can channel the ineffable
```

Using concrete visual elements to represent abstract ideas or themes — a cage for imprisonment, water for rebirth, red for passion or danger — the visual poetry of cinema. Andrei Tarkovsky filled his films with water, fire, and earth symbolism in "Stalker," "Mirror," and "Nostalghia." Kubrick encoded "2001: A Space Odyssey" with evolutionary symbolism from the bone weapon to the star child. Guill…

**When to use.** Use symbolism when an abstract idea needs a physical image the audience can feel: enclosure for confinement, water for renewal, or a divided reflection for fractured identity. The chosen symbol should emerge from the story's world and character experience. It is most effective at turning points or…

**Directing the AI.** Choose one concrete subject whose form, behavior, or placement naturally echoes the theme. Give it clear visual space through centered framing, isolation, scale, or contrast, while retaining believable light and material. Connect it to the character through gaze, touch, or blocking rather than explanatory text. If the symbol recurs, alter its condition as the story changes. Let the literal object…

**Common mistakes.**
- Choosing a symbol through cliché alone, without connecting it to the character's specific conflict or world.
- Crowding the frame with competing metaphors, leaving no single image enough space to carry meaning.
- Lighting the symbol like a supernatural sign when it should remain a credible object in the scene.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `text-as-mask`, 20f

**Sources.** [How to Make a Short Film: An Introduction to Filmmaking](None)


### voiceover-narration

**"Voiceover Narration Prompt for AI Image & Video"** · `narrative` · level basic

```
Scene designed to accompany voiceover narration with [Subject] in a contemplative visual, the imagery deliberately quiet and reflective to create space for an unseen narrator's voice, the visual mood introspective and open-ended, soft desaturated color palette, the Malick-Scorsese understanding that the right contemplative image paired with words creates something greater than either alone
```

A character's voice speaking over the visuals, providing internal thoughts, context, or commentary that can create intimacy, irony, or an essay-like quality depending on tone. Martin Scorsese uses voiceover as a vital narrative engine — Henry Hill's running commentary in "Goodfellas" is inseparable from the film's identity. Terrence Malick's whispered, philosophical voiceovers in "The Thin Red Li…

**When to use.** Use voiceover narration when the audience needs access to thought, memory, commentary, or a perspective the visible action cannot supply. Pairing words and images can create intimacy, contradiction, or essay-like reflection. The voice should add a second layer, not describe what viewers already see…

**Directing the AI.** Build a restrained visual scene around the subject: contemplative action, open negative space, soft desaturated color, and slow, readable movement. Keep cuts sparse enough for spoken ideas to breathe. Pair literal words with complementary or contradictory imagery rather than direct illustration. Maintain environmental sound and visual detail so the image does not become wallpaper. Place the subje…

**Common mistakes.**
- Describing visible actions word for word, reducing narration to redundant accessibility rather than added perspective.
- Cutting images faster than the spoken thought can land, forcing sound and picture to compete.
- Using vague contemplative visuals with no relationship to the narrator's specific memory, irony, or argument.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `typing-code-block`, 138f

**Sources.** [How to Make a Short Film: An Introduction to Filmmaking](None)


### bokeh

**"Bokeh Prompt for AI Image & Video"** · `visual-effects` · level basic

```
Beautiful bokeh behind [Subject], hundreds of out-of-focus light sources transformed into soft luminous orbs of color, each perfectly round from the wide-open aperture of a fast 85mm lens, the distinctive creamy rendering of a Zeiss or Leica lens where the out-of-focus transition is butter-smooth, the visual magic of shallow depth of field turning the background into an impressionist painting of light
```

The aesthetic quality of out-of-focus areas, particularly light sources that become soft, circular orbs — beautiful bokeh creates a dreamy, luminous background that elevates any subject. The term comes from the Japanese word for "blur," and the quality of bokeh varies dramatically between lens designs. Anamorphic lenses produce distinctive oval bokeh, seen in J.J. Abrams' "Star Trek" and Ridley S…

**When to use.** Use bokeh when the subject needs separation from a busy environment or when background lights should become emotional atmosphere rather than information. It suits portraits, romantic scenes, night streets, and intimate details. Strong bokeh depends on depth staging: the subject, lens plane, and dis…

**Directing the AI.** Place the subject sharply in the foreground and move practical lights well behind them. Use shallow depth of field with smooth focus falloff, turning distant points into soft circular or oval orbs without losing their color. Keep the eyes or chosen detail critically sharp. Avoid cutting bokeh shapes through the subject's silhouette. Build varied orb sizes from multiple distances and retain a few…

**Common mistakes.**
- Blurring the subject along with the background, leaving no stable focal plane for the viewer.
- Filling every empty area with identical glowing circles, which reads as an overlay rather than optical depth.
- Using bokeh when background geography matters, hiding information the audience needs to understand the scene.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: pan_right | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: smooth_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: smooth_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Sources.** [Inventing Worlds and Characters: Effects](None)


### color-grading

**"Color Grading Prompt for AI Image & Video"** · `visual-effects` · level intermediate

```
Heavily color-graded scene with [Subject] rendered in a distinct teal-and-orange complementary palette, shadows pushed deep into cyan-teal while skin tones and practicals isolated to deep amber-orange, the aggressive color manipulation where post-production color becomes a dominant creative force equal to the original photography, the final act of authorship in the filmmaking pipeline
```

The process of altering and enhancing color in post-production to create a specific mood, era, or visual identity — the final paintbrush of cinema, transforming raw footage into visual art. The Coen Brothers' "O Brother, Where Art Thou?" (2000) was the first major film to be entirely digitally color graded, creating its sepia-toned Depression-era look. David Fincher works obsessively with coloris…

**When to use.** Use color grading when a scene needs a unified emotional identity, a distinct period, or a visual boundary between storylines and locations. It can cool a procedural world, warm a memory, or create controlled contrast between shadows and practical lights. Establish the grade as part of the project'…

**Directing the AI.** Define the palette by assigning hue families to shadows, midtones, skin, highlights, and practical sources. For a teal-and-amber look, push dark regions toward cyan while keeping faces and lamps warm, then protect neutral whites from contamination. Maintain exposure detail in both ends of the range. Apply the same color relationships across changing locations. Specify restrained saturation and co…

**Common mistakes.**
- Pushing every surface toward two colors, erasing natural material differences and believable skin variation.
- Changing black levels and white balance between adjacent shots, breaking the continuity of the visual world.
- Using saturation as a substitute for mood without controlling contrast, exposure, or the hierarchy of hues.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: pan_right | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: smooth_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: smooth_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Sources.** [Inventing Worlds and Characters: Effects](None)


### desaturation

**"Desaturation Prompt for AI Image & Video"** · `visual-effects` · level basic

```
Desaturated scene with [Subject] approaching monochrome, all color drained to near-gray except for a single vivid element, the Spielberg "Schindler's List" technique of selective color isolation, the surrounding gray rendering the world as bleak while the single color insists that something vital remains, heavy desaturation in grading leaving only one color channel active
```

Reducing color intensity in the image, moving toward grayscale to create a bleak, documentary, or dreamlike quality — partial desaturation can isolate a single color for dramatic effect. Steven Spielberg used near-total desaturation in "Schindler's List" with the famous exception of the girl's red coat, creating one of cinema's most iconic selective-color moments. Ridley Scott desaturated "Black…

**When to use.** Use desaturation for bleak realism, memory, documentary severity, graphic stylization, or a world emotionally drained of vitality. Partial desaturation can guide attention toward one remaining color, but that color needs narrative significance. The approach works when luminance, texture, and shape…

**Directing the AI.** Reduce saturation across the scene while preserving distinct values in skin, clothing, architecture, and background. Let most hues approach neutral gray rather than collapse into one muddy tone. If isolating a color, choose a single object and retain its vivid channel with clean edges and believable reflections. Support the treatment with directional light and strong tonal contrast. Keep the sele…

**Common mistakes.**
- Removing color without preserving value contrast, producing a flat gray image with no visual hierarchy.
- Leaving several unrelated colors vivid, weakening the narrative force of selective color isolation.
- Oversaturating the retained hue until it appears pasted on rather than present in the photographed world.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Sources.** [Inventing Worlds and Characters: Effects](None)


### film-grain

**"Film Grain Prompt for AI Image & Video"** · `visual-effects` · level basic

```
Heavy film grain visible on [Subject], the organic random texture of high-speed 35mm film stock pushed two stops in processing, each frame alive with dancing silver halide crystals, the grain coarser in shadows and finer in highlights, Kodak Vision3 500T texture that Tarantino and Nolan insist on preserving, the organic soul of celluloid in an increasingly digital world
```

The visible texture of chemical film stock — random variations in density and color that give analog footage its organic, tactile character, often added digitally for warmth and nostalgia. Christopher Nolan and Quentin Tarantino remain committed to shooting on actual film stock, preserving the authentic grain of celluloid. Steven Soderbergh shot "Traffic" on different film stocks to differentiate…

**When to use.** Use film grain when pristine digital surfaces feel too sterile for the story, or when a period, documentary, intimate, or nostalgic mood benefits from tactile imperfection. Grain can unify composited elements and give shadows physical texture. Choose its strength to match the scene's light and emot…

**Directing the AI.** Apply random, frame-varying texture across the image, with coarser grain in deep shadows and finer grain in exposed highlights. Let color density fluctuate subtly without crawling around edges or changing object shapes. Preserve facial features and text readability beneath the texture. Keep grain scale consistent with the apparent format and shot size. In motion, every frame should carry a fresh…

**Common mistakes.**
- Using a fixed noise layer across every frame, making the grain look pinned to the screen.
- Applying equal grain density to highlights and shadows, which removes the exposure-responsive character of film texture.
- Choosing particles so large that fine facial features and material detail become difficult to read.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Sources.** [Inventing Worlds and Characters: Effects](None)


### forced-perspective

**"Forced Perspective Prompt for AI Image & Video"** · `visual-effects` · level intermediate

```
Forced perspective illusion with [Subject] appearing impossibly large or small through precise camera alignment and placement, the depth of field deep enough that both near and far elements appear sharp, the lighting matching between foreground and background, the Peter Jackson technique of making the impossible look real without digital manipulation, just physics and precise alignment
```

Using the relationship between camera position and object placement to create optical illusions of size — Hobbits appear small next to Gandalf through precise staging rather than CGI. Peter Jackson used forced perspective extensively in "The Lord of the Rings," building oversized and undersized duplicate sets and using precise camera alignment to make Elijah Wood appear four feet shorter than Ian…

**When to use.** Use forced perspective when characters or objects must appear impossibly large or small while sharing one believable frame. It suits fantasy scale, whimsical comedy, giant-object illusions, and practical-looking visual tricks. The technique works from a precise viewpoint, so it is strongest in comp…

**Directing the AI.** Place the larger-looking subject close to camera and the smaller-looking subject farther away on the same sightline. Use deep focus so both planes remain sharp, then match light direction, color temperature, shadow softness, and eye lines across the distance. Hide scale references that expose the separation. Keep the camera fixed at the alignment point. For interaction, choreograph gestures to me…

**Common mistakes.**
- Allowing shallow focus to reveal that the apparently adjacent subjects sit on widely separated depth planes.
- Including familiar scale references between subjects, exposing the distance trick before the illusion can work.
- Moving the camera away from the designed viewpoint, causing edges, eye lines, and apparent contact to separate.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Sources.** [Inventing Worlds and Characters: Effects](None)


### lens-distortion

**"Lens Distortion Prompt for AI Image & Video"** · `visual-effects` · level intermediate

```
Lens distortion from a vintage anamorphic lens visible across [Subject], barrel distortion curving straight lines at frame edges into subtle arcs, oval-shaped bokeh, horizontal flare streaks, the edges softer and more swirled than the sharp center, chromatic aberration creating slight color fringing, the accumulated imperfections giving the image character that clinical modern lenses deliberately avoid
```

Optical aberrations from specific lenses that bend, stretch, or warp the image — wide-angle barrel distortion, anamorphic oval bokeh, or vintage lens flaring — each lens has a personality. Emmanuel Lubezki exploits wide-angle distortion in his work with Terrence Malick, using ultra-wide lenses that bend the edges of reality. Roger Deakins prefers Arri/Zeiss Master Primes for their clinical precis…

**When to use.** Use lens distortion when optical imperfection should add personality, unease, intimacy, or period texture. Wide barrel distortion can make nearby faces confrontational, while anamorphic softness, oval bokeh, and horizontal flare can create expansive cinematic space. Match the aberration to a clear…

**Directing the AI.** Keep the central subject relatively sharp while curving straight lines near frame edges into subtle arcs. Add edge softness, mild chromatic fringing, oval background bokeh, and restrained horizontal flare from actual bright sources. Let perspective stretch objects closest to the lens, not distant forms at random. Preserve one coherent optical center across the shot. The imperfections should share…

**Common mistakes.**
- Warping the center and edges equally, making the image feel digitally melted rather than optically distorted.
- Adding flare without a bright source, which breaks the physical logic of the implied lens.
- Stacking barrel distortion, fringing, softness, and bokeh so heavily that the subject loses visual authority.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Sources.** [Inventing Worlds and Characters: Effects](None)


### morphing

**"Morphing / Dissolve Effect Prompt for AI Image & Video"** · `visual-effects` · level advanced

```
[Subject] caught mid-transformation, the form dissolving into particles or liquid or light, features simultaneously present and absent in a liminal state between two identities, the mathematical smoothness of digital morphing applied to the human form, even lighting ensuring the transformation reads cleanly, the unsettling beauty of identity in flux and matter in transition
```

A digital transformation effect where one form smoothly dissolves, transmutes, or reshapes into another — character dissolving into particles, liquid metal transformation, ethereal dissolution, matter transmutation. Originally pioneered by ILM for the T-1000 in "Terminator 2," morphing has evolved from face-to-face blending into a rich vocabulary of transformation effects. In AI image and video g…

**When to use.** Use morphing when transformation itself is the dramatic event: a body changing identity, matter dissolving into particles, a face becoming another face, or an object reforming from liquid or light. It suits surreal, magical, technological, and body-horror moments. Define the source, destination, an…

**Directing the AI.** Show the subject midway between two defined forms, with landmarks from both identities visible in corresponding positions. Choose one transition behavior, such as particles, liquid, or light, and move it progressively across the body rather than everywhere at once. Keep the camera steady and illumination even so changing contours read cleanly. Preserve mass and directional flow. End with a stable…

**Common mistakes.**
- Mixing particles, smoke, liquid, and fire in one change, obscuring the transformation's governing visual rule.
- Losing facial or structural landmarks midway, so the source and destination no longer feel connected.
- Changing lighting and camera angle during the morph, making continuity errors compete with the intended transformation.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Sources.** [Inventing Worlds and Characters: Effects](None)


### sepia-tone

**"Sepia Tone Prompt for AI Image & Video"** · `visual-effects` · level basic

```
Sepia-toned treatment on [Subject], the warm brownish-yellow transforming the image into what appears to be an aged photographic plate, the entire color spectrum collapsed into variations of amber and umber, highlights tinged with pale gold and shadows falling to chocolate brown, visible grain and slight vignetting reinforcing the antique quality, the universal visual language that tells the audience "this was a long time ago"
```

A warm brownish-yellow color treatment that evokes aged photographs and historical periods, instantly signaling "the past" and adding a romantic, weathered quality. The sepia effect mimics the actual chemical toning process used on photographs from the 1860s through the early 1900s. The Coen Brothers used a digital sepia grade throughout "O Brother, Where Art Thou?" to evoke Depression-era Americ…

**When to use.** Use sepia tone when the image should immediately suggest history, memory, an old photograph, or romantic distance from the present. It fits archival inserts, period bookends, family recollection, and deliberately weathered visual worlds. The treatment is a strong shorthand, so pair it with period-a…

**Directing the AI.** Collapse the palette into amber, umber, pale gold, and chocolate brown while retaining a full range from highlight to shadow. Add fine visible grain, slight edge vignetting, and restrained softness consistent with an aged photographic plate. Keep faces and important objects separated by value, not color. Remove modern color accents that would puncture the treatment. Apply the same tonal curve acr…

**Common mistakes.**
- Applying a flat brown overlay that stains whites and blacks without creating a convincing tonal range.
- Keeping bright modern color accents in frame, which breaks the historical shorthand of the sepia treatment.
- Adding extreme scratches and damage until surface effects overwhelm faces, actions, and the intended emotional memory.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Sources.** [Inventing Worlds and Characters: Effects](None)


### acid-western

**"Acid Western Prompt for AI Image & Video"** · `genres` · level advanced

```
Acid western with [Subject] in a vast surreal desert landscape, the familiar Western iconography distorted through a psychedelic lens, oversaturated sky bleeding unnatural colors, dust and heat haze warping the horizon, Jodorowsky's mysticism meets Jarmusch's deadpan, a lone figure in an existential void that was once the frontier, 16mm film grain, the American myth turned hallucinatory
```

A psychedelic subversion of the Western genre that replaces manifest destiny optimism with hallucinatory existentialism. Alejandro Jodorowsky's "El Topo" (1970) invented the form — a mystical gunfighter journey through surreal desert landscapes. Jim Jarmusch's "Dead Man" (1995) deconstructed the genre with a dying accountant guided by a Native American named Nobody. The Coen Brothers' "No Country…

**When to use.** Use Acid Western style when frontier myths need to dissolve into hallucination, nihilism, absurdity, or metaphysical doubt. A lone rider, desert town, gunfighter, or ritual can remain recognizable while the landscape becomes an existential void. It suits journeys without comforting destiny and viol…

**Directing the AI.** Place a solitary subject in a vast desert with familiar Western clothing, weapons, or architecture, then corrupt the myth through oversaturated sky, unnatural horizon color, heat haze, and warped distance. Use gritty grain and long static observation rather than frantic effects. Let one surreal object or action appear without explanation. Keep the figure small against the land, with dread and abs…

**Common mistakes.**
- Removing all recognizable Western elements, leaving psychedelic desert imagery without a genre being subverted.
- Using cheerful kaleidoscopic effects, which misses the form's dread, deadpan absurdity, and existential emptiness.
- Packing the landscape with symbols and visions instead of letting one impossible intrusion disturb the familiar myth.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `cel-flash-stomp`, 30f

**Sources.** [Genres: Where to Draw the Line?](None)


### cinema-verite

**"Cinéma Vérité Prompt for AI Image & Video"** · `genres` · level intermediate

```
Cinema verite documentary moment with [Subject], handheld camera following the action, natural available light providing uncontrolled illumination, the framing imperfect and reactive, occasional focus hunting, the raw audio of the environment, the entire aesthetic committed to the principle that imperfection is authenticity, Super 16mm film grain, the Jean Rouch principle that the camera's presence provokes truth
```

A documentary approach using handheld cameras, natural lighting, and unscripted moments to capture truth — the camera is acknowledged as present, truth provoked rather than merely observed. Jean Rouch and Edgar Morin coined the term with "Chronicle of a Summer" (1961), where the filmmakers actively engage with their subjects. The American equivalent, "direct cinema" (Frederick Wiseman, the Maysle…

**When to use.** Use cinéma vérité when truth should emerge through interaction rather than polished observation. It suits interviews in motion, social encounters, street scenes, political situations, and fiction that needs documentary pressure. Let the camera's presence affect behavior instead of pretending it is…

**Directing the AI.** Follow the subject with a handheld camera at human distance, reacting late to gestures and occasionally correcting framing or focus. Use only available light, allowing mixed color and uneven exposure where the location creates it. Keep ambient sound, interruptions, and glances toward the camera. Let the operator shift position when events change rather than anticipating every move. Preserve faces…

**Common mistakes.**
- Adding constant violent shake, which feels performed and prevents the audience from observing actual behavior.
- Polishing every composition and focus pull, removing the reactive uncertainty that gives the approach its tension.
- Treating technical damage as authenticity while subjects remain posed, scripted, and untouched by the camera.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `graze-face-tour`, 150f

**Sources.** [Genres: Where to Draw the Line?](None)


### cosmic-horror

**"Cosmic Horror Prompt for AI Image & Video"** · `genres` · level advanced

```
Cosmic horror atmosphere with [Subject] dwarfed by something vast and incomprehensible at the edge of the frame, non-Euclidean geometry subtly wrong in the architecture, the Annihilation shimmer distorting organic forms, scale that makes the human figure irrelevant, deep shadow concealing shapes that should not exist, cold clinical lighting that reveals too much, the terror of understanding how small you are
```

A visual approach to the unknowable and incomprehensible — vast entities beyond human understanding, non-Euclidean geometry, and the terror of insignificance in an indifferent universe. Inspired by H.P. Lovecraft's literary work, the visual language was refined by John Carpenter's "The Thing" (1982) with its shapeshifting alien horror. Annihilation (2018) by Alex Garland brought cosmic horror to…

**When to use.** Use cosmic horror when fear should come from incomprehensible scale, unstable reality, or the discovery that human concerns mean nothing to the larger universe. It suits alien landscapes, impossible architecture, transformations, and encounters that resist full interpretation. Show enough structure…

**Directing the AI.** Frame the human subject as a tiny, readable figure against an immense structure or entity partly concealed at the edge of vision. Bend architecture into subtly non-Euclidean relationships, repeat forms at impossible scales, and distort organic matter with a restrained shimmer. Use cold clinical light to reveal disturbing detail while deep shadow withholds the whole. Keep perspective internally wr…

**Common mistakes.**
- Centering and fully lighting the entity, reducing incomprehensible presence to a conventional creature reveal.
- Using random tentacles without impossible scale, wrong geometry, or any challenge to human understanding.
- Making the human figure invisible, which removes the scale reference needed to communicate insignificance.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `fracture`, 156f

**Sources.** [Genres: Where to Draw the Line?](None)


### dogme-95

**"Dogme 95 Prompt for AI Image & Video"** · `genres` · level advanced

```
Dogme 95 aesthetic with [Subject] shot on a consumer camera with no additional lighting, harsh overhead fluorescent as the only illumination, color balance slightly off, handheld breathing movement, the radical commitment to zero artifice — no music, no effects, no genre, just human beings in real space, the Vinterberg-von Trier Vow of Chastity made visible
```

A 1995 Danish manifesto demanding handheld cameras, natural lighting, real locations, no genre conventions, and no directorial credit — a radical purity movement that stripped cinema to its bones. Lars von Trier and Thomas Vinterberg created the Dogme 95 "Vow of Chastity," and Vinterberg's "The Celebration" became the movement's masterpiece, using only available light and handheld consumer video…

**When to use.** Use Dogme 95 principles when performance and human conflict should survive without cinematic decoration. Real rooms, handheld cameras, available light, location sound, and present-tense action can expose discomfort that polished technique might soften. It fits family crises, confrontations, and int…

**Directing the AI.** Place the subject in a real interior or exterior and use only light already present, even when fluorescent color or window exposure is imperfect. Follow action handheld at close human distance, allowing breathing movement and reactive reframing. Keep natural room echo, interruptions, and practical objects. Remove added music, stylized transitions, artificial set dressing, and visual effects. Pres…

**Common mistakes.**
- Adding artificial grain, glitches, and damage, mistaking post-production distress for a commitment to real conditions.
- Using dramatic added light while claiming available-light realism, which breaks the technique's central visual discipline.
- Making the frame deliberately unreadable, when stripped-back filmmaking should expose performance rather than hide it.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `letterspace-materialize`, 15f

**Sources.** [Genres: Where to Draw the Line?](None)


### film-noir

**"Film Noir Prompt for AI Image & Video"** · `genres` · level intermediate

```
Film noir aesthetic with [Subject] in high-contrast black and white, deep blacks and silvery highlights, venetian blind shadow patterns, neon signs reflected in rain puddles, shot on Kodak Double-X black and white stock with hard lighting creating razor shadows, the John Alton visual language of moral ambiguity expressed through the war between light and darkness
```

A genre defined by high-contrast black-and-white photography, urban settings, morally ambiguous characters, femme fatales, and a pervasive sense of cynicism and doom. Born from German Expressionist emigrés and American hardboiled fiction, film noir flowered in the 1940s and 50s with Billy Wilder's "Double Indemnity," Orson Welles's "Touch of Evil," and John Huston's "The Maltese Falcon." Cinemato…

**When to use.** Use film noir for crime, betrayal, investigation, fatal attraction, or any story built on compromised choices and approaching doom. Its visual language turns light into moral pressure: characters are divided by shadow, streets become traps, and interiors conceal more than they reveal. The genre is…

**Directing the AI.** Work in high-contrast black and white with deep blacks, silvery highlights, and limited midtones. Place the subject in an urban interior or rain-dark street, then rake hard light through blinds, doorways, or smoke to create sharp patterned shadows. Use low or oblique angles and leave portions of faces concealed. Add wet reflections and restrained practical neon translated into tonal brightness. C…

**Common mistakes.**
- Adding venetian-blind shadows to a bright neutral scene without noir conflict, danger, or moral ambiguity.
- Crushing every dark area to featureless black, erasing the location and the subject's readable silhouette.
- Using soft flattering portrait light, which removes the hard visual conflict central to noir imagery.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: pan_right | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: smooth_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: smooth_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `brand-ink-open`, 83f, `fracture`, 156f

**Sources.** [Genres: Where to Draw the Line?](None)


### found-footage

**"Found Footage Prompt for AI Image & Video"** · `genres` · level basic

```
Found footage shot of [Subject] through a consumer-grade camera in night vision mode, the entire image in distinctive green-tinged infrared, the framing chaotic and uncontrolled, the footage corrupted with digital artifacts and compression blocks, timestamp running in the corner, the Blair Witch principle that what you cannot clearly see is infinitely more terrifying, the aesthetic of authenticity as horror's most effective weapon
```

A style presenting the film as discovered amateur or surveillance recordings — "The Blair Witch Project," "Paranormal Activity," the conceit that what you're watching is "real" raw footage. Ruggero Deodato's "Cannibal Holocaust" (1980) invented the format, so convincingly that the director was charged with murder before proving the actors were alive. "The Blair Witch Project" (1999) made found fo…

**When to use.** Use found footage when the recording itself is part of the story: evidence, a recovered diary, surveillance, or a final document of danger. It is especially effective for horror because limited framing and imperfect visibility force the audience to search the image. Define who holds the camera and…

**Directing the AI.** Choose a specific recording source and keep its limitations consistent: consumer camera, night vision, surveillance angle, or phone-like handheld footage. Add reactive framing, delayed pans, autofocus hunting, compression blocks, and a stable timestamp without obscuring essential action. In darkness, reveal partial shapes at the edge rather than a fully lit threat. Let the operator's breath, move…

**Common mistakes.**
- Changing recording formats and artifact styles between shots without a story reason for the source change.
- Showing the threat clearly in centered light, removing the uncertainty that makes limited footage frightening.
- Ignoring the camera operator's motive, so continued filming during danger feels implausible and mechanically convenient.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `graze-face-tour`, 150f

**Sources.** [Genres: Where to Draw the Line?](None)


### french-new-wave

**"French New Wave Prompt for AI Image & Video"** · `genres` · level intermediate

```
French New Wave scene with [Subject] shot handheld on what appears to be stolen moments, the camera following with improvisational looseness, harsh midday sun creating unflattering but honest illumination, the composition casual rather than composed, the visual rebellion against studio perfection, high-contrast black and white on grainy 16mm stock, the Raoul Coutard handheld aesthetic
```

A 1960s movement that broke every rule — jump cuts, handheld cameras, location shooting, fourth-wall breaks, and a rebellious rejection of polished studio filmmaking, treating cinema as conversation. Jean-Luc Godard's "Breathless" (1960) and François Truffaut's "The 400 Blows" (1959) launched the movement, joined by Agnès Varda, Jacques Rivette, Eric Rohmer, and Claude Chabrol. Cinematographer Ra…

**When to use.** Use French New Wave style when the film should feel youthful, immediate, self-aware, and resistant to studio polish. It suits street romance, restless conversation, playful crime, and characters who seem to invent the movie as they live it. The style can combine handheld location work, jump cuts, d…

**Directing the AI.** Shoot on real streets in hard midday light with grainy high-contrast black and white or restrained natural color. Follow the subject handheld with loose reframing, occasional focus correction, and casual composition. Let jump cuts remove pieces of continuous action while preserving its emotional line. Permit a glance into lens or an abrupt pan when character energy demands it. Keep location sound…

**Common mistakes.**
- Combining every New Wave device in each shot, turning rebellion into a rigid checklist of effects.
- Using polished studio light and locked framing while relying on wardrobe alone to suggest the movement.
- Cutting continuity randomly, without preserving the character impulse that makes rough editing feel alive.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `black-card-transition` (shot-transitions), `dark-tunnel-transition` (shot-transitions), `focus-handoff-transition` (shot-transitions), `mask-wipe-real` (shot-transitions), `portal-wipe-v2` (shot-transitions), `whip-brake-real` (shot-transitions), `whip-pan-real` (shot-transitions)

**Sources.** [Genres: Where to Draw the Line?](None)


### german-expressionism

**"German Expressionism Prompt for AI Image & Video"** · `genres` · level advanced

```
German Expressionism with [Subject] in deliberately distorted architecture, buildings leaning at impossible angles, shadows painted in sharp angular patterns that defy actual light sources, extreme contrast between blinding white and absolute black with no midtones, the Caligari aesthetic of a world bent by psychological torment, monochrome with exaggerated theatrical lighting
```

An early 20th-century movement using distorted sets, extreme shadows, and exaggerated angles to externalize inner psychological states — the visual DNA of modern horror and Tim Burton. Robert Wiene's "The Cabinet of Dr. Caligari" (1920) established the movement with painted shadows and impossible architecture. F.W. Murnau's "Nosferatu" and Fritz Lang's "Metropolis" expanded the vocabulary. When t…

**When to use.** Use German Expressionism when the environment should externalize fear, paranoia, grief, or mental fracture. Distorted walls, impossible streets, and painted shadows make psychology physical rather than realistic. It fits horror, nightmare, theatrical fantasy, and moments when subjective truth matte…

**Directing the AI.** Build a monochrome set with leaning buildings, jagged doorways, slanted floors, and forced angles that cannot exist naturally. Remove most midtones, dividing the frame into blinding white and absolute black. Paint hard triangular shadows across surfaces without matching realistic light sources. Tilt the camera and exaggerate the subject's posture to echo the architecture. Keep every distortion gr…

**Common mistakes.**
- Keeping realistic architecture while adding random tilted framing, producing a weak imitation of the style.
- Using soft naturalistic shadows, which contradict the painted graphic darkness of Expressionist space.
- Adding many unrelated horror props instead of letting distorted geometry and contrast carry the psychological threat.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `fracture`, 156f

**Sources.** [Genres: Where to Draw the Line?](None)


### giallo

**"Giallo Prompt for AI Image & Video"** · `genres` · level advanced

```
Giallo-style scene with [Subject] drenched in vivid primary-color lighting, deep crimson from unseen sources, a pool of intense blue creating color boundaries where red meets blue in deep violet, the composition more concerned with aesthetic beauty than narrative logic, every frame designed as a painting, the Dario Argento principle that terror can be beautiful, the saturated primary colors of "Suspiria"
```

Italian horror-thriller genre known for vivid color palettes, elaborate murder sequences, leather-gloved killers, and a heightened visual style that prioritizes aesthetic beauty over narrative logic. Mario Bava established the giallo with "Blood and Black Lace" (1964) and "Bay of Blood." Dario Argento perfected it with "Deep Red," "Suspiria," and "Tenebre," using vivid primary-color lighting and…

**When to use.** Use giallo for horror-thriller scenes where color, suspense, and elaborate visual staging matter more than strict realism. It suits stalking, gloved killers, labyrinthine interiors, clues, and moments where danger becomes a composed spectacle. The palette should carry psychological pressure through…

**Directing the AI.** Place the subject inside a dark interior divided by intense red and blue light from unseen or stylized sources, allowing their overlap to form deep violet. Use glossy surfaces, sharp silhouettes, elegant framing, and one threatening detail such as a leather-gloved hand at frame edge. Keep color saturation rich without losing facial form or object texture. Move the camera with controlled curiosity…

**Common mistakes.**
- Using random neon colors without establishing the disciplined red, blue, and violet architecture of the scene.
- Flattening shadows with broad fill light, removing the concealment that makes saturated color feel dangerous.
- Centering the threat immediately, leaving no elegant visual search or suspense inside the composition.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `fracture`, 156f

**Sources.** [Genres: Where to Draw the Line?](None)


### hyperlink-cinema

**"Hyperlink Cinema Prompt for AI Image & Video"** · `genres` · level advanced

```
Hyperlink cinema visualization with [Subject] shown across multiple disconnected lives in the same moment, each in their own lighting world and emotional register yet sharing the same space, the invisible connections not yet apparent but waiting to be revealed, the Robert Altman and Paul Thomas Anderson structure of simultaneous parallel stories, the whole greater than the sum because these lives will eventually collide
```

A narrative style weaving multiple storylines that initially seem unconnected but gradually reveal hidden links — "Crash," "Babel," "Magnolia" — the interconnected web of human experience. Robert Altman pioneered the form with "Nashville" and "Short Cuts." Paul Thomas Anderson's "Magnolia" weaves nine storylines that converge in a biblical climax. Alejandro González Iñárritu's "Amores Perros" and…

**When to use.** Use hyperlink cinema when several apparently separate stories can reveal a larger web of cause, coincidence, or shared consequence. Unlike simple parallel action, the pleasure comes from discovering hidden links between lives that initially seem unrelated. Give each thread an independent emotional…

**Directing the AI.** Create distinct visual worlds for each character through location, palette, light, and framing rhythm. Repeat one ordinary object, route, broadcast, weather event, or background figure across threads without emphasizing the connection too early. Cross-cut at matching gestures or consequences, gradually tightening temporal proximity. When lives collide, bring visual elements from their separate wo…

**Common mistakes.**
- Revealing every connection immediately, removing the gradual recognition that gives the structure its narrative pleasure.
- Giving secondary threads no independent stakes, making them feel like machinery for the central character's plot.
- Using coincidence alone at convergence without planted objects, spaces, causes, or consequences linking earlier scenes.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `glitch-cycle`, 168f

**Sources.** [Genres: Where to Draw the Line?](None)


### italian-neorealism

**"Italian Neorealism Prompt for AI Image & Video"** · `genres` · level intermediate

```
Italian Neorealism with [Subject] on an actual working-class street, non-professional faces and authentic clothing, the real architecture providing the set, the camera observing at a respectful distance, natural overcast light providing flat honest illumination, black and white photography capturing poverty with dignity, the De Sica principle that reality itself is more dramatic than anything a screenwriter could invent
```

Post-war Italian movement using non-professional actors, real locations, and stories of everyday working-class life — raw, honest, and deeply humanist cinema stripped to its moral essentials. Roberto Rossellini's "Rome, Open City" (1945) launched the movement from the rubble of war. Vittorio De Sica's "Bicycle Thieves" (1948) and "Umberto D." are the genre's masterpieces — devastating stories of…

**When to use.** Use Italian Neorealism for stories about work, poverty, family, survival, and ordinary moral choices shaped by material conditions. Real locations and unvarnished faces keep attention on human stakes rather than spectacle. The approach suits quiet observation and simple actions with serious consequ…

**Directing the AI.** Place the subject on an actual working street among worn architecture, everyday clothing, passing pedestrians, and functional objects. Use natural overcast light or plain daylight with black-and-white tonal detail. Keep the camera at a respectful medium distance, observing complete actions without dramatic angle changes. Favor unpolished faces and restrained gestures. Let background life continue…

**Common mistakes.**
- Beautifying poverty with glowing light and decorative ruin, turning material hardship into an aesthetic backdrop.
- Posing every background figure, which removes the independent street life essential to the observed reality.
- Forcing melodramatic expressions instead of trusting ordinary faces, restrained gestures, and concrete circumstances.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `letterspace-materialize`, 15f

**Sources.** [Genres: Where to Draw the Line?](None)


### mockumentary

**"Mockumentary Prompt for AI Image & Video"** · `genres` · level basic

```
Mockumentary talking head interview with [Subject] looking slightly off-camera to an unseen interviewer, standard documentary medium close-up with unflattering fluorescent lighting, the documentary format treating the setting with the visual gravity of a war correspondent's confession, handheld camera occasionally reframing to maintain the documentary illusion, the Christopher Guest understanding that absurd comedy requires deadpan documentary treatment
```

A fictional film presented in documentary style — talking head interviews, observational camera work, title cards — creating comedy through the contrast between the serious form and absurd content. Rob Reiner's "This Is Spinal Tap" (1984) established the mockumentary as a legitimate comedic form. Christopher Guest continued the tradition with "Waiting for Guffman," "Best in Show," and "A Mighty W…

**When to use.** Use mockumentary when comedy depends on fictional characters treating absurd events with complete documentary seriousness. Talking-head interviews can contradict observed action, reveal vanity, or let a glance expose what dialogue will not. The format suits workplace, community, performance, and so…

**Directing the AI.** Frame the subject in a standard medium close-up, looking slightly off-camera toward an unseen interviewer. Use plain fluorescent or window light, a functional background, and minimal visual flattery. During observational scenes, let the handheld camera reframe late, zoom slightly toward revealing reactions, or catch a private glance into lens. Keep titles and composition sober. Treat every ridicu…

**Common mistakes.**
- Lighting and framing interviews like glossy commercials, weakening the contrast between serious form and absurd content.
- Adding comic zooms to every line, making the camera beg for laughs instead of observing behavior.
- Having characters perform obvious jokes for the lens rather than protecting their sincere documentary reality.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `graze-face-tour`, 150f

**Sources.** [Genres: Where to Draw the Line?](None)


### mumblecore

**"Mumblecore Prompt for AI Image & Video"** · `genres` · level basic

```
Mumblecore scene with [Subject] shot on what appears to be a consumer DSLR with available window light, the dialogue clearly improvised with interrupted sentences and awkward pauses, the framing functional rather than composed, the sound ambient and slightly echoey, the Bujalski-Swanberg aesthetic where lack of budget becomes the honesty of the image, naturalistic window light
```

Ultra-low-budget indie filmmaking focused on naturalistic dialogue, improvisation, and the awkwardness of young adult relationships — micro-budget intimacy as aesthetic. Andrew Bujalski's "Funny Ha Ha" (2002) is considered mumblecore's founding film, followed by the Duplass Brothers' "The Puffy Chair," Joe Swanberg's "Hannah Takes the Stairs," and Greta Gerwig's early acting work in the movement.…

**When to use.** Use mumblecore for low-stakes situations carrying high emotional discomfort: uncertain relationships, stalled adulthood, shared apartments, and conversations where people interrupt, retreat, or say the wrong thing. Its modest visual scale keeps attention on behavior and pauses. The style suits smal…

**Directing the AI.** Stage two or three people in a real apartment, kitchen, car, or neighborhood space with available window light and functional framing. Keep the camera handheld but calm, adjusting late when someone shifts position. Let dialogue overlap, sentences trail off, and pauses remain visible in posture and eye lines. Retain room echo and ambient sound. Avoid glamour lighting and perfect shot-reverse-shot…

**Common mistakes.**
- Writing polished speeches for every character, removing the interruption, hesitation, and uncertainty central to the style.
- Using aggressive handheld shake during quiet conversation, which competes with subtle behavior rather than observing it.
- Lighting the room like a prestige drama, erasing the practical intimacy of available windows and fixtures.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `letterspace-materialize`, 15f

**Sources.** [Genres: Where to Draw the Line?](None)


### noir-tech

**"Tech Noir Prompt for AI Image & Video"** · `genres` · level intermediate

```
Tech noir scene with [Subject] in a rain-soaked neon-lit dystopia, the hard shadows and moral ambiguity of classic noir transplanted into a high-tech future, reflections of holographic advertisements in wet pavement, the loneliness of Blade Runner, anamorphic lens flares streaking through rain, cold blue and hot orange competing in every frame, smoke and vapor caught in shafts of artificial light
```

A hybrid genre fusing film noir aesthetics with science fiction — rain-soaked neon cities, morally ambiguous protagonists navigating high-tech dystopias, and the existential dread of noir transplanted into a technological future. Ridley Scott's "Blade Runner" (1982) defined the genre, combining Raymond Chandler-style detective narrative with a cyberpunk cityscape. James Cameron coined the term as…

**When to use.** Use Tech Noir for detective stories, fugitives, artificial identities, surveillance, and moral compromise inside advanced technological worlds. The genre works when noir loneliness and hard shadow remain central beneath futuristic surfaces. Rain, holographic advertising, and machines should intensi…

**Directing the AI.** Place the subject alone in a rain-soaked night street or shadowed high-tech interior. Mix cold blue environmental light with hot amber practicals, allowing both to streak across wet pavement and reflective glass. Add smoke, vapor, surveillance surfaces, and restrained holographic advertisements. Use hard side light, deep negative space, and anamorphic flare motivated by bright sources. Keep techn…

**Common mistakes.**
- Filling the frame with neon signs while omitting noir shadow, loneliness, and morally compromised character stakes.
- Presenting technology as clean spectacle, which loses the worn dystopian pressure central to the hybrid genre.
- Using evenly bright cyberpunk color, leaving no darkness for surveillance, concealment, or existential dread.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `brand-ink-open`, 83f, `fracture`, 156f

**Sources.** [Genres: Where to Draw the Line?](None)


### poetic-realism

**"Poetic Realism Prompt for AI Image & Video"** · `genres` · level advanced

```
Poetic realism with [Subject] rendered in heartbreaking lyrical beauty, fog softening every hard edge into dreamlike haze, the ordinary transformed into visual poetry by atmosphere, the Marcel Carne understanding that working-class life contains as much beauty and melancholy as any aristocratic drama, soft black and white with rich midtones, fog itself becoming the emotional texture of longing
```

A 1930s French movement blending realistic working-class settings with lyrical, dreamlike visual beauty — finding poetry in the mundane through fog-wrapped docks, rain on cobblestones, and melancholy love. Marcel Carné and cinematographer Eugène Schüfftan defined the style in "Port of Shadows" and "Children of Paradise," creating misty, romantically lit working-class worlds. Jean Renoir's "The Ru…

**When to use.** Use poetic realism for melancholy love, working-class lives, doomed encounters, and ordinary places charged with longing. The method keeps streets, docks, rooms, and labor recognizable while atmosphere lifts them beyond plain documentation. Fog, rain, reflections, and soft tonal light should deepen…

**Directing the AI.** Place the subject in a modest street, dock, café, or rented room with real signs of work and wear. Use soft black and white with rich midtones, wet cobblestones, diffused lamps, and fog that gently reduces distant contrast. Keep the figure grounded through tactile clothing and specific activity. Let rain or haze shape depth without hiding the setting. Compose lyricism through atmosphere and gestu…

**Common mistakes.**
- Using fog so densely that the working environment disappears and the image becomes generic romantic haze.
- Beautifying every surface until labor, wear, and social reality no longer anchor the lyrical treatment.
- Crushing the image into harsh noir contrast, losing the soft midtones that carry melancholy and tenderness.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `letterspace-materialize`, 15f

**Sources.** [Genres: Where to Draw the Line?](None)


### slow-cinema

**"Slow Cinema Prompt for AI Image & Video"** · `genres` · level advanced

```
Slow cinema with [Subject] in a single unbroken composition, the camera absolutely still observing with infinite patience, the only movement gradual shifting of natural light, duration itself becoming the subject, natural overcast daylight providing soft even illumination, the Tarkovsky-Bela Tarr discipline of trusting that observation is enough, that the passage of real time is cinema's most radical subject
```

A contemporary movement embracing extremely long takes, minimal dialogue, and patient observation that challenges the viewer to slow down, observe, and find meaning in duration itself. Andrei Tarkovsky is the spiritual father of slow cinema, with his meditative long takes in "Stalker" and "Mirror" establishing duration as a cinematic tool. Béla Tarr's "Sátántangó" (seven hours of long takes) and…

**When to use.** Use slow cinema when duration itself reveals behavior, labor, landscape, grief, routine, or waiting. A long unbroken view can make tiny changes matter because the audience has time to notice them. It suits contemplative stories and actions normally compressed by editing. Choose a frame with evolvin…

**Directing the AI.** Lock the camera in one carefully balanced composition and observe the subject through a complete action or interval without cutting. Keep dialogue sparse and movement gradual. Let natural overcast light shift, a distant figure cross, steam disappear, or posture change over real time. Avoid push-ins, coverage, and music cues that instruct emotion. Preserve ambient sound and depth. The frame must r…

**Common mistakes.**
- Holding an empty composition with no evolving light, behavior, sound, or environmental detail to observe.
- Adding frequent reframing or coverage cuts, which removes the sustained duration defining the approach.
- Using slow pacing as automatic seriousness without giving the audience specific visual activity worth attending to.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `drone-dive-landing` (space-camera-moves), 150f, `exploded-view` (space-camera-moves), 150f

**Sources.** [Genres: Where to Draw the Line?](None)


### southern-gothic

**"Southern Gothic Prompt for AI Image & Video"** · `genres` · level intermediate

```
Southern Gothic atmosphere with [Subject] amid crumbling architecture and encroaching nature, Spanish moss hanging like curtains, golden diffused light filtering through dirty windows, the beauty of decay, oppressive warmth visible in the thick humid air, Kodak Vision3 250D pushed warm, overexposed highlights bleeding into shadow, the weight of history in every peeling surface, Laughton's dreamlike menace
```

A genre steeped in decay, moral corruption, and the haunted atmosphere of the American South — crumbling plantation houses, Spanish moss, oppressive humidity, and characters burdened by dark histories. Charles Laughton's "The Night of the Hunter" (1955) created the definitive Southern Gothic visual language with its dreamlike river sequences. Terrence Malick's "Badlands" and David Gordon Green's…

**When to use.** Use Southern Gothic for family secrets, moral corruption, inherited violence, religious unease, and beauty entangled with decay in the American South. The setting should feel burdened by history rather than merely old. Crumbling houses, Spanish moss, oppressive heat, and polite surfaces can conceal…

**Directing the AI.** Place the subject inside or beside decaying Southern architecture overtaken by vines, damp wood, peeling paint, and hanging Spanish moss. Filter warm diffused light through dirty windows or thick foliage, allowing highlights to bleed softly into shadow. Make humid air visible through haze and stillness. Keep wardrobe restrained and posture controlled, with one unsettling historical trace in frame…

**Common mistakes.**
- Using a clean restored mansion with decorative moss, which removes the physical pressure of accumulated decay.
- Adding generic ghosts or gore instead of letting history, restraint, heat, and corruption create the menace.
- Romanticizing every ruined surface, making the setting picturesque rather than morally and emotionally burdened.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `brand-ink-open`, 83f

**Sources.** [Genres: Where to Draw the Line?](None)


### spaghetti-western

**"Spaghetti Western Prompt for AI Image & Video"** · `genres` · level intermediate

```
Spaghetti Western standoff with [Subject], the camera alternating between extreme close-ups of squinting eyes and ultra-wide shots revealing vast empty space, dust devils spiraling through the frame, golden hour desert light casting long shadows, shot on Techniscope 2-perf 35mm for gritty widescreen, the Ennio Morricone tension of silence stretched to breaking point
```

Italian-produced Westerns characterized by extreme close-ups, sweeping wide shots, Morricone-style scores, morally gray antiheroes, and a stylized, operatic approach to violence. Sergio Leone defined the genre with his Dollars trilogy starring Clint Eastwood and reached its apex with "Once Upon a Time in the West" — a film built entirely from looks, silences, and Ennio Morricone's score. Leone's…

**When to use.** Use the Spaghetti Western style for standoffs, revenge, outlaw myth, and confrontations where waiting carries as much force as violence. Its rhythm depends on the collision between extreme close-ups and vast wides, turning eyes, hands, and empty distance into equal dramatic players. It suits morall…

**Directing the AI.** Establish an immense desert wide shot with the subject reduced against empty terrain, dust devils, and long golden-hour shadows. Cut to extreme close-ups of narrowed eyes, weathered skin, boots, and a hand hovering near a weapon. Keep the horizon broad and the color warm, with gritty widescreen texture. Alternate scale slowly, letting tiny gestures carry threat. Hold the final silence until tensi…

**Common mistakes.**
- Keeping every shot at medium distance, losing the genre's defining collision between faces and vast space.
- Cutting rapidly throughout the standoff, denying silence and duration the chance to build operatic tension.
- Using clean modern surfaces and clothing, which weakens the dusty, weathered physical world around the confrontation.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `cel-flash-stomp`, 30f

**Sources.** [Genres: Where to Draw the Line?](None)


### surrealism

**"Surrealism Prompt for AI Image & Video"** · `genres` · level advanced

```
Surrealist scene with [Subject] in a world where dream logic replaces physical reality, impossible elements presented with the matter-of-fact certainty of documentary, lighting impossibly motivated from sources that do not exist, the Bunuel-Lynch visual language where the subconscious mind's architecture is rendered as physical space, the unsettling beauty of a world where logic has been replaced by feeling
```

A movement drawing on dreams, the subconscious, and irrational imagery to create art that defies logic — melting clocks, impossible architecture, dream logic replacing narrative cause-and-effect. Luis Buñuel and Salvador Dalí created cinema's first surrealist film, "Un Chien Andalou" (1929), with its infamous eye-slicing opening. Buñuel continued making surrealist cinema for fifty years through "…

**When to use.** Use surrealism when subconscious feeling, desire, dread, or contradiction matters more than literal cause and effect. It suits dreams, identity fractures, psychological transitions, and worlds where impossible events reveal emotional truth. Establish a visual rule that belongs to the scene's feelin…

**Directing the AI.** Place the subject in a recognizable setting, then alter one governing reality: scale, gravity, architecture, identity, or time. Present the impossible element with neutral framing and documentary certainty rather than fantasy spectacle. Motivate light from sources that visibly cannot exist, but keep surfaces and shadows internally consistent. Repeat a shape or action to establish dream logic. Let…

**Common mistakes.**
- Filling the frame with unrelated strange objects, creating visual novelty without emotional or thematic logic.
- Lighting impossible events like spectacular fantasy, which weakens their calm and unsettling matter-of-fact quality.
- Changing the world's rules every moment, leaving no dream logic for the audience to follow.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `magician-card-flourish`, 9f

**Sources.** [Genres: Where to Draw the Line?](None)


### vaporwave

**"Vaporwave Aesthetic Prompt for AI Image & Video"** · `genres` · level basic

```
Vaporwave aesthetic with [Subject] bathed in neon pink and cyan gradient lighting, retro digital artifacts and scan lines overlaid, reflective chrome and glass surfaces, the nostalgic melancholy of a 1990s shopping mall at closing time, VHS color bleeding and tracking errors, palm trees and marble columns, the beauty of obsolete technology, everything slightly too saturated and slightly too perfect
```

A visual style born from internet culture that repurposes 1980s and 90s commercial aesthetics — glitch art, neon pink and cyan gradients, retro computer interfaces, marble busts, Japanese text, and VHS degradation — into a nostalgic critique of consumer capitalism. While originating as a music genre, the visual language has been widely adopted in film, advertising, and AI generation. Nicolas Wind…

**When to use.** Use vaporwave when the image should feel nostalgic for a commercial future that never arrived. It suits empty malls, obsolete technology, artificial leisure spaces, retro interfaces, and scenes balancing irony with sincere melancholy. The style is strongest when recognizable 1980s or 1990s consumer…

**Directing the AI.** Bathe the subject in a pink-to-cyan gradient and place them among reflective chrome, glass, marble columns, palms, or an empty shopping-mall interior. Add scan lines, mild VHS color bleed, tracking errors, and retro interface fragments without covering the composition. Keep surfaces slightly too polished and colors slightly too saturated. Leave generous empty space and late-night stillness so obs…

**Common mistakes.**
- Combining every retro icon at once, turning a coherent nostalgic world into an internet sticker collage.
- Using dark aggressive cyberpunk lighting, which loses vaporwave's pastel commercial emptiness and wistful artificial calm.
- Applying severe VHS damage until architecture, text, and the central subject can no longer be read.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `gradient-transition`, 180f

**Sources.** [Genres: Where to Draw the Line?](None)


### wuxia

**"Wuxia Prompt for AI Image & Video"** · `genres` · level advanced

```
Wuxia style with [Subject] in gravity-defying motion, robes and fabric trailing like calligraphy strokes through the air, the fight-as-dance choreography of Ang Lee and Zhang Yimou, painterly natural landscape behind — bamboo forests or misty mountains, the action frozen at its most balletic moment, Kodak Vision3 250D warmth, the poetry of martial arts rendered as visual art
```

A Chinese genre centered on martial arts warriors bound by codes of honor, featuring gravity-defying combat choreography, flowing silk costumes, and painterly landscapes. Ang Lee's "Crouching Tiger, Hidden Dragon" (2000) introduced the genre to global audiences with its bamboo forest fight sequence. Zhang Yimou's "Hero" and "House of Flying Daggers" pushed the visual poetry further with color-cod…

**When to use.** Use wuxia for martial conflict shaped by honor, loyalty, restraint, and impossible physical grace. Combat becomes dance, while landscape and costume carry emotional meaning equal to the fighters. It suits duels in bamboo, misty mountains, courtyards, and color-coded chapters. Focus on one balletic…

**Directing the AI.** Freeze or track the subject at the most graceful point of a leap, turn, or suspended strike. Extend robes, sleeves, hair, and fabric along the motion path like calligraphy strokes. Place the action against bamboo, misty mountains, or another painterly natural setting with warm daylight and layered depth. Keep bodies anatomically readable and weapons aligned with gesture. Choreograph opponents as…

**Common mistakes.**
- Crowding the frame with many fighters, making the choreography read as battle noise instead of visual calligraphy.
- Using rigid clothing and poses, which removes the flowing motion that gives wuxia action its lyricism.
- Treating aerial movement as superhero flight without grounded gesture, landscape, or honor-bound dramatic tension.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_motion: slow_pan | resolution: 1080p | duration: 5 | style: cinematic` | kling-1.5 | no |
| `luma` Luma Dream Machine | `aspect_ratio: 16_9 | duration: 5 | resolution: 1080p | style: cinematic` | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | no |
| `pika15` Pika 1.5 | `aspect_ratio: 16:9 | style: cinematic | duration: 5 | motion: slow_pan` | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | `motion_brush: smooth_slow_pan | aspect_ratio: 16:9 | duration: 5 | resolution: 1080p` | gen-3-alpha | no |
| `sora` OpenAI Sora | `style: cinematic | resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | motion: slow_pan` | sora-1 | no |
| `veo2` Google Veo 2 | `resolution: 1080p | aspect_ratio: 16:9 | duration: 5 | cinematic_style: true` | veo-2 | no |

**Shot cards that can carry it.** `cel-flash-stomp`, 30f

**Sources.** [Genres: Where to Draw the Line?](None)


## Per-technique pages

One page per technique, 150 in total, so loading a single technique does not cost a 40 KB document:

| technique | category | level | video | pairings |
|---|---|---|---|---|
| [360-degree-shot](../techniques/360-degree-shot.md) | camera-work | advanced | yes | 1 |
| [aerial-shot](../techniques/aerial-shot.md) | camera-work | intermediate | yes | 3 |
| [birds-eye-view](../techniques/birds-eye-view.md) | camera-work | intermediate | yes | 2 |
| [choker-shot](../techniques/choker-shot.md) | camera-work | intermediate | yes | 1 |
| [close-up](../techniques/close-up.md) | camera-work | basic | yes | 1 |
| [cowboy-shot](../techniques/cowboy-shot.md) | camera-work | basic | yes | 1 |
| [crane-shot](../techniques/crane-shot.md) | camera-work | advanced | yes | 1 |
| [crash-zoom](../techniques/crash-zoom.md) | camera-work | intermediate | yes | 2 |
| [dolly-shot](../techniques/dolly-shot.md) | camera-work | intermediate | yes | 6 |
| [dutch-angle](../techniques/dutch-angle.md) | camera-work | basic | yes | 2 |
| [establishing-shot](../techniques/establishing-shot.md) | camera-work | basic | yes | 4 |
| [extreme-close-up](../techniques/extreme-close-up.md) | camera-work | basic | yes | 1 |
| [extreme-long-shot](../techniques/extreme-long-shot.md) | camera-work | basic | yes | 2 |
| [eye-level-shot](../techniques/eye-level-shot.md) | camera-work | basic | yes | 1 |
| [handheld-shot](../techniques/handheld-shot.md) | camera-work | basic | yes | 1 |
| [head-on-shot](../techniques/head-on-shot.md) | camera-work | intermediate | yes | 1 |
| [high-angle-shot](../techniques/high-angle-shot.md) | camera-work | basic | yes | 2 |
| [insert-shot](../techniques/insert-shot.md) | camera-work | basic | yes | 2 |
| [long-shot](../techniques/long-shot.md) | camera-work | basic | yes | 2 |
| [low-angle-shot](../techniques/low-angle-shot.md) | camera-work | basic | yes | 1 |
| [master-shot](../techniques/master-shot.md) | camera-work | intermediate | yes | 2 |
| [medium-close-up](../techniques/medium-close-up.md) | camera-work | basic | yes | 1 |
| [medium-shot](../techniques/medium-shot.md) | camera-work | basic | yes | 3 |
| [one-er](../techniques/one-er.md) | camera-work | advanced | yes | 1 |
| [over-the-shoulder](../techniques/over-the-shoulder.md) | camera-work | basic | yes | 2 |
| [overhead-shot](../techniques/overhead-shot.md) | camera-work | intermediate | yes | 2 |
| [pan-shot](../techniques/pan-shot.md) | camera-work | basic | yes | 2 |
| [pov-shot](../techniques/pov-shot.md) | camera-work | intermediate | yes | 1 |
| [pull-out](../techniques/pull-out.md) | camera-work | intermediate | yes | 2 |
| [push-in](../techniques/push-in.md) | camera-work | intermediate | yes | 4 |
| [rack-focus](../techniques/rack-focus.md) | camera-work | intermediate | yes | 2 |
| [slow-motion](../techniques/slow-motion.md) | camera-work | basic | yes | 3 |
| [static-shot](../techniques/static-shot.md) | camera-work | basic | yes | 1 |
| [steadicam](../techniques/steadicam.md) | camera-work | advanced | yes | 1 |
| [three-shot](../techniques/three-shot.md) | camera-work | intermediate | yes | 2 |
| [tilt-shot](../techniques/tilt-shot.md) | camera-work | basic | yes | 1 |
| [tracking-shot](../techniques/tracking-shot.md) | camera-work | intermediate | yes | 3 |
| [two-shot](../techniques/two-shot.md) | camera-work | basic | yes | 2 |
| [vertigo-effect](../techniques/vertigo-effect.md) | camera-work | advanced | yes | 3 |
| [whip-pan](../techniques/whip-pan.md) | camera-work | intermediate | yes | 4 |
| [worms-eye-view](../techniques/worms-eye-view.md) | camera-work | intermediate | yes | 1 |
| [ambient-light](../techniques/ambient-light.md) | lighting | basic | no | 1 |
| [available-light](../techniques/available-light.md) | lighting | intermediate | no | 1 |
| [backlight](../techniques/backlight.md) | lighting | basic | no | 1 |
| [blue-hour](../techniques/blue-hour.md) | lighting | intermediate | no | 1 |
| [bounce-light](../techniques/bounce-light.md) | lighting | intermediate | no | 1 |
| [broad-lighting](../techniques/broad-lighting.md) | lighting | basic | no | 1 |
| [chiaroscuro](../techniques/chiaroscuro.md) | lighting | advanced | no | 1 |
| [color-temperature](../techniques/color-temperature.md) | lighting | intermediate | no | 1 |
| [cross-lighting](../techniques/cross-lighting.md) | lighting | intermediate | no | 1 |
| [dappled-light](../techniques/dappled-light.md) | lighting | intermediate | no | 1 |
| [edge-light](../techniques/edge-light.md) | lighting | intermediate | no | 1 |
| [eye-light](../techniques/eye-light.md) | lighting | intermediate | no | 1 |
| [fill-light](../techniques/fill-light.md) | lighting | basic | no | 1 |
| [gobo-lighting](../techniques/gobo-lighting.md) | lighting | advanced | no | 1 |
| [golden-hour](../techniques/golden-hour.md) | lighting | basic | no | 1 |
| [hard-light](../techniques/hard-light.md) | lighting | basic | no | 1 |
| [high-key-lighting](../techniques/high-key-lighting.md) | lighting | basic | no | 1 |
| [key-light](../techniques/key-light.md) | lighting | basic | no | 1 |
| [kicker-light](../techniques/kicker-light.md) | lighting | intermediate | no | 1 |
| [lens-flare](../techniques/lens-flare.md) | lighting | basic | no | 1 |
| [low-key-lighting](../techniques/low-key-lighting.md) | lighting | intermediate | no | 2 |
| [motivated-lighting](../techniques/motivated-lighting.md) | lighting | intermediate | no | 1 |
| [practical-lighting](../techniques/practical-lighting.md) | lighting | intermediate | no | 1 |
| [rembrandt-lighting](../techniques/rembrandt-lighting.md) | lighting | intermediate | no | 1 |
| [short-lighting](../techniques/short-lighting.md) | lighting | intermediate | no | 1 |
| [side-lighting](../techniques/side-lighting.md) | lighting | intermediate | no | 1 |
| [silhouette](../techniques/silhouette.md) | lighting | basic | no | 1 |
| [soft-light](../techniques/soft-light.md) | lighting | basic | no | 1 |
| [three-point-lighting](../techniques/three-point-lighting.md) | lighting | basic | no | 1 |
| [uplighting](../techniques/uplighting.md) | lighting | basic | no | 1 |
| [balancing-elements](../techniques/balancing-elements.md) | composition | intermediate | no | 2 |
| [centered-composition](../techniques/centered-composition.md) | composition | basic | no | 1 |
| [contrast-composition](../techniques/contrast-composition.md) | composition | basic | no | 1 |
| [deep-focus](../techniques/deep-focus.md) | composition | intermediate | no | 2 |
| [depth-of-field](../techniques/depth-of-field.md) | composition | basic | no | 2 |
| [diagonal-lines](../techniques/diagonal-lines.md) | composition | basic | no | 1 |
| [figure-ground](../techniques/figure-ground.md) | composition | intermediate | no | 1 |
| [foreground-interest](../techniques/foreground-interest.md) | composition | intermediate | no | 2 |
| [framing-within-frame](../techniques/framing-within-frame.md) | composition | intermediate | no | 1 |
| [golden-ratio](../techniques/golden-ratio.md) | composition | advanced | no | 1 |
| [headroom](../techniques/headroom.md) | composition | basic | no | 1 |
| [lead-room](../techniques/lead-room.md) | composition | basic | no | 2 |
| [leading-lines](../techniques/leading-lines.md) | composition | basic | no | 2 |
| [mise-en-scene](../techniques/mise-en-scene.md) | composition | advanced | no | 2 |
| [negative-space](../techniques/negative-space.md) | composition | intermediate | no | 2 |
| [repetition-and-pattern](../techniques/repetition-and-pattern.md) | composition | intermediate | no | 1 |
| [rule-of-thirds](../techniques/rule-of-thirds.md) | composition | basic | no | 3 |
| [shallow-focus](../techniques/shallow-focus.md) | composition | basic | no | 2 |
| [symmetry](../techniques/symmetry.md) | composition | basic | no | 1 |
| [triangular-composition](../techniques/triangular-composition.md) | composition | intermediate | no | 1 |
| [visual-weight](../techniques/visual-weight.md) | composition | intermediate | no | 1 |
| [cross-cutting](../techniques/cross-cutting.md) | editing | intermediate | no | 2 |
| [cut-in](../techniques/cut-in.md) | editing | basic | no | 1 |
| [cutaway](../techniques/cutaway.md) | editing | basic | no | 1 |
| [dissolve](../techniques/dissolve.md) | editing | basic | no | 7 |
| [fade-in-out](../techniques/fade-in-out.md) | editing | basic | no | 1 |
| [fast-motion](../techniques/fast-motion.md) | editing | basic | no | 2 |
| [freeze-frame](../techniques/freeze-frame.md) | editing | basic | no | 3 |
| [iris-transition](../techniques/iris-transition.md) | editing | basic | no | 1 |
| [jump-cut](../techniques/jump-cut.md) | editing | basic | no | 2 |
| [long-take](../techniques/long-take.md) | editing | advanced | no | 1 |
| [montage](../techniques/montage.md) | editing | basic | no | 2 |
| [reaction-shot](../techniques/reaction-shot.md) | editing | basic | no | 2 |
| [reverse-motion](../techniques/reverse-motion.md) | editing | basic | no | 2 |
| [smash-cut](../techniques/smash-cut.md) | editing | basic | no | 2 |
| [split-screen](../techniques/split-screen.md) | editing | intermediate | no | 1 |
| [time-lapse](../techniques/time-lapse.md) | editing | intermediate | no | 2 |
| [wipe-transition](../techniques/wipe-transition.md) | editing | basic | no | 1 |
| [breaking-fourth-wall](../techniques/breaking-fourth-wall.md) | narrative | intermediate | no | 1 |
| [cliffhanger](../techniques/cliffhanger.md) | narrative | basic | no | 3 |
| [flashback](../techniques/flashback.md) | narrative | basic | no | 7 |
| [flashforward](../techniques/flashforward.md) | narrative | intermediate | no | 7 |
| [foreshadowing](../techniques/foreshadowing.md) | narrative | intermediate | no | 1 |
| [frame-narrative](../techniques/frame-narrative.md) | narrative | intermediate | no | 1 |
| [in-medias-res](../techniques/in-medias-res.md) | narrative | basic | no | 2 |
| [motif](../techniques/motif.md) | narrative | intermediate | no | 1 |
| [non-linear-narrative](../techniques/non-linear-narrative.md) | narrative | advanced | no | 1 |
| [parallel-storylines](../techniques/parallel-storylines.md) | narrative | advanced | no | 1 |
| [symbolism](../techniques/symbolism.md) | narrative | intermediate | no | 1 |
| [voiceover-narration](../techniques/voiceover-narration.md) | narrative | basic | no | 1 |
| [bokeh](../techniques/bokeh.md) | visual-effects | basic | no | 0 |
| [color-grading](../techniques/color-grading.md) | visual-effects | intermediate | no | 0 |
| [desaturation](../techniques/desaturation.md) | visual-effects | basic | no | 0 |
| [film-grain](../techniques/film-grain.md) | visual-effects | basic | no | 0 |
| [forced-perspective](../techniques/forced-perspective.md) | visual-effects | intermediate | no | 0 |
| [lens-distortion](../techniques/lens-distortion.md) | visual-effects | intermediate | no | 0 |
| [morphing](../techniques/morphing.md) | visual-effects | advanced | no | 0 |
| [sepia-tone](../techniques/sepia-tone.md) | visual-effects | basic | no | 0 |
| [acid-western](../techniques/acid-western.md) | genres | advanced | no | 1 |
| [cinema-verite](../techniques/cinema-verite.md) | genres | intermediate | no | 1 |
| [cosmic-horror](../techniques/cosmic-horror.md) | genres | advanced | no | 1 |
| [dogme-95](../techniques/dogme-95.md) | genres | advanced | no | 1 |
| [film-noir](../techniques/film-noir.md) | genres | intermediate | no | 2 |
| [found-footage](../techniques/found-footage.md) | genres | basic | no | 1 |
| [french-new-wave](../techniques/french-new-wave.md) | genres | intermediate | no | 7 |
| [german-expressionism](../techniques/german-expressionism.md) | genres | advanced | no | 1 |
| [giallo](../techniques/giallo.md) | genres | advanced | no | 1 |
| [hyperlink-cinema](../techniques/hyperlink-cinema.md) | genres | advanced | no | 1 |
| [italian-neorealism](../techniques/italian-neorealism.md) | genres | intermediate | no | 1 |
| [mockumentary](../techniques/mockumentary.md) | genres | basic | no | 1 |
| [mumblecore](../techniques/mumblecore.md) | genres | basic | no | 1 |
| [noir-tech](../techniques/noir-tech.md) | genres | intermediate | no | 2 |
| [poetic-realism](../techniques/poetic-realism.md) | genres | advanced | no | 1 |
| [slow-cinema](../techniques/slow-cinema.md) | genres | advanced | no | 2 |
| [southern-gothic](../techniques/southern-gothic.md) | genres | intermediate | no | 1 |
| [spaghetti-western](../techniques/spaghetti-western.md) | genres | intermediate | no | 1 |
| [surrealism](../techniques/surrealism.md) | genres | advanced | no | 1 |
| [vaporwave](../techniques/vaporwave.md) | genres | basic | no | 1 |
| [wuxia](../techniques/wuxia.md) | genres | advanced | no | 1 |
