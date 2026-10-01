# Cinematic techniques

A second corpus: **20 techniques** that answer *what to shoot*, complementing the 157 shot cards that answer *how it moves*. Same DB, same join keys, same generated-from-the-DB rule (ADR 0007).

| stage | corpus | answers |
|---|---|---|
| 1 | `data/cinematic/` | **what to shoot** — camera, light, composition, editing rhythm, genre |
| 2 | `references/shots/` | **how it moves** — easing, spring, timing, render duration |
| 3 | Remotion | motion execution and render |

## Two rules that are not stylistic

1. **`[Subject]` is a slot and is never expanded.** The prompts below are verbatim. An expanded prompt reads exactly like an authored one, and an agent handed it will paste it to a client as though the studio wrote it.
2. **An absent cross-tool cell is `null`, never a default.** Of 45 listed cells, 23 carry a parameter, 16 have actually been run against the model version, and 22 are empty because nobody has tested them. A plausible string in an untested cell is a claim we cannot defend to a client.

`data/cinematic/` is **source**, not generated: authored, committed, reviewed in a diff. See `data/cinematic/README.md`. Reference stills are linked; 0/20 techniques have a reference video.

## Camera Work  (`camera-work`, 3)

| technique | level | motions | tested tools | prompt |
|---|---|---|---|---|
| [orbit-reveal](#orbit-reveal) | intermediate | 3 | mj61 | Cinematic orbit shot circling [Subject] once at constant radius and speed, subject stays… |
| [product-macro-detail](#product-macro-detail) | intermediate | 3 | mj61 | Extreme macro detail of [Subject] filling the frame, texture visible, focus racking from… |
| [slow-dolly-in](#slow-dolly-in) | basic | 3 | mj61 | Cinematic shot of [Subject], slow steady dolly-in from a medium wide to a medium close ov… |

## Lighting  (`lighting`, 3)

| technique | level | motions | tested tools | prompt |
|---|---|---|---|---|
| [butterfly-key](#butterfly-key) | basic | 0 | mj61 | Studio portrait of [Subject] under a butterfly key: the main light raised high and tilted… |
| [kicker-light](#kicker-light) | basic | 2 | mj61 | Cinematic portrait of [Subject], three-quarter backlight, deep shadows on the near side,… |
| [low-key-single-source](#low-key-single-source) | advanced | 1 | mj61 | Chiaroscuro portrait of [Subject] lit by a single low hard source from camera-right, most… |

## Composition  (`composition`, 3)

| technique | level | motions | tested tools | prompt |
|---|---|---|---|---|
| [centered-symmetry](#centered-symmetry) | basic | 2 | mj61 | Perfectly symmetrical product shot of [Subject] dead centre on the vertical axis, mirrore… |
| [negative-space-frame](#negative-space-frame) | basic | 2 | mj61 | Cinematic frame of [Subject] small and placed low-right, the upper two thirds left as cle… |
| [rule-of-thirds-subject](#rule-of-thirds-subject) | basic | 2 | mj61 | Cinematic composition of [Subject] placed on the left third, looking into open negative s… |

## Editing  (`editing`, 3)

| technique | level | motions | tested tools | prompt |
|---|---|---|---|---|
| [hard-cut-on-beat](#hard-cut-on-beat) | basic | 3 | none | Fast-cut montage on [Subject], every cut landing exactly on a drum transient, six to twel… |
| [match-cut-transition](#match-cut-transition) | intermediate | 4 | mj61 | Cinematic match cut: [Subject] in the first frame and a different scene in the second fra… |
| [single-take-reveal](#single-take-reveal) | advanced | 2 | none | One continuous take on [Subject], beginning tight on a small detail and craning up and ba… |

## Narrative  (`narrative`, 2)

| technique | level | motions | tested tools | prompt |
|---|---|---|---|---|
| [problem-to-solution-beat](#problem-to-solution-beat) | basic | 2 | mj61 | Two-beat product story: the first frame shows [Subject] mid-friction, the second frame sh… |
| [silent-observation-beat](#silent-observation-beat) | advanced | 2 | none | Documentary-style beat of [Subject] observed in use with no presenter, no voiceover, natu… |

## Visual Style  (`visual-style`, 3)

| technique | level | motions | tested tools | prompt |
|---|---|---|---|---|
| [analogue-texture](#analogue-texture) | basic | 2 | mj61 | Cinematic still of [Subject] shot on 35mm film, fine organic grain visible in the shadows… |
| [cold-blue-tech](#cold-blue-tech) | basic | 2 | mj61 | Cold blue technical frame of [Subject], cool desaturated palette, blue-grey metal, soft g… |
| [restrained-motion-graphics](#restrained-motion-graphics) | basic | 3 | mj61 | Clean product motion frame showing [Subject] as a crisp UI surface on a flat dark ground,… |

## Film Genres  (`genres`, 3)

| technique | level | motions | tested tools | prompt |
|---|---|---|---|---|
| [documentary-naturalism](#documentary-naturalism) | basic | 2 | none | Documentary shot of [Subject] in its real environment, available window light only, handh… |
| [high-key-white-studio](#high-key-white-studio) | basic | 2 | mj61 | High-key studio product photograph of [Subject] on a seamless white sweep, soft overhead… |
| [retro-analogue-comedy](#retro-analogue-comedy) | intermediate | 1 | mj61 | Retro 1970s comedy scene with [Subject] shot on vintage 16mm, slightly soft focus, visibl… |

## Techniques in full

### orbit-reveal

**Orbit around a stationary subject** · `camera-work` · level intermediate

```
Cinematic orbit shot circling [Subject] once at constant radius and speed, subject
stays perfectly still and centred while the background rotates behind it, 85mm,
even key light so the falloff does not betray the move, no dolly zoom.
```

An orbit is the cheapest way to show that an object has depth: because the subject is static and only the background moves, every edge that reveals a new face proves the object is three-dimensional rather than a flat render.

**When to use.** Product reveals, character introductions that need scale, and any moment where you want to say "look at all of this" without cutting.

**Directing the AI.** Say "orbit" and then forbid the two failure modes explicitly: no subject rotation, no zoom. Constant radius and constant speed are what stop it reading as a handheld wobble.

**Common mistakes.**
- The subject rotates with the camera, which destroys the parallax proof.
- Speed easing, so the move breathes at the wrong moment.
- Falling off a wide lens, which stretches the background as it turns.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_control=orbit` | kling-1.5 | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | yes |
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |

**Shot cards that can carry it.** `basic-3d-scene`, 180f, `cube-navigation`, 180f, `graze-face-tour`, 150f

**Sources.** [Orbit shot — Wikipedia](https://en.wikipedia.org/wiki/Orbit_shot), [Parallax — Wikipedia](https://en.wikipedia.org/wiki/Parallax)


### product-macro-detail

**Macro detail with a rack focus** · `camera-work` · level intermediate

```
Extreme macro detail of [Subject] filling the frame, texture visible, focus racking
from the near surface to the far plane mid-shot, shallow depth of field, controlled
key light skimming across the surface, 100mm macro, no camera movement.
```

At macro distances depth of field becomes a few millimetres, so a focus pull is the only move available. That constraint is useful: it turns attention into a physical act the viewer can follow, rather than a cut that asks them to notice a difference.

**When to use.** Material and texture proof, hardware close-ups, and detail shots that hand off to a wider frame.

**Directing the AI.** "Focus racks from the near surface to the far plane" plus "shallow depth of field" is the mechanism. Pair it with a declared motion-card handoff so the rack lands on a cut, which is what turns the pull into a transition.

**Common mistakes.**
- Too much depth of field, so the rack has nothing to travel through.
- Adding camera movement to a technique that is entirely about focus.
- Racking too fast to read either plane.

| tool | params | version | tested |
|---|---|---|---|
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | yes |
| `runway_gen3` Runway Gen-3 Alpha | **null** | gen-3-alpha | no |

**Shot cards that can carry it.** `dolly-zoom-real` (depth-layer-moves), 150f, `focus-handoff-transition` (shot-transitions), `spotlight-hero-card`, 220f

**Sources.** [Rack focus — Wikipedia](https://en.wikipedia.org/wiki/Focus_pulling), [Macro photography — Wikipedia](https://en.wikipedia.org/wiki/Macro_photography)


### slow-dolly-in

**Slow dolly-in on a locked subject** · `camera-work` · level basic

```
Cinematic shot of [Subject], slow steady dolly-in from a medium wide to a medium
close over about eight seconds, subject held at the same screen position, background
parallax sliding outward, 50mm on a dolly, locked horizon, no handheld shake.
```

A dolly-in changes the relationship between subject and background rather than magnifying the frame. Everything behind the subject shifts in scale at a different rate, so the move reads as travelling into the scene, not zooming at it.

**When to use.** When you want to add weight to a statement, or move the viewer from context into detail without cutting. It is the default move for an opening line and for a reveal.

**Directing the AI.** Give the duration, the start and end framing, and the parallax explicitly. "Slow dolly-in over eight seconds from medium wide to medium close, background parallax" distinguishes it from a zoom, which the model will otherwise choose.

**Common mistakes.**
- Producing a zoom: background stays static, so the move reads as a flat scale-up.
- Too fast. Under four seconds reads as a push, not a drift.
- Handheld micro-shake, which reads as "amateur" rather than "cinematic".

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_control=forward, camera_speed=slow` | kling-1.5 | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | yes |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `bullet-time-freeze-orbit` (tension-camera-moves), 150f, `crane-rise-reveal`, 20f, `dolly-zoom-real` (depth-layer-moves), 150f

**Sources.** [Dolly shot — Wikipedia](https://en.wikipedia.org/wiki/Dolly_zoom), [Tracking shot — Wikipedia](https://en.wikipedia.org/wiki/Tracking_shot)


### butterfly-key

**Butterfly key with under-light bounce** · `lighting` · level basic

```
Studio portrait of [Subject] under a butterfly key: the main light raised high and
tilted down so its shadow falls under the nose, a low reflector bouncing fill back
under the chin, black background, glamour lighting, 85mm, crisp catchlights.
```

Moving the key above the subject's eye line and tilting it down puts the nose shadow under the nose rather than to one side. That single geometric change flattens the face symmetrically, which is why fashion and beauty lighting has used it for a century.

**When to use.** Beauty and cosmetics work, skincare texture shots, any frontal hero image where symmetry is the point. Not for interviews: the symmetrical shadow reads as artificial in conversation.

**Directing the AI.** Say "high key light tilted down, nose shadow falls beneath the nose, low bounce reflector under the chin". The bounce is what keeps it from going harsh — without it the under-chin area goes black and the face reads as a mask.

**Common mistakes.**
- The shadow lands to the side, so the AI placed the key at eye level. Name the
- Omitting the bounce and getting a harsh, dark underside.
- Flash-on-the-lens look: a frontal catchlight instead of two angled ones.

| tool | params | version | tested |
|---|---|---|---|
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | yes |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Sources.** [Butterfly lighting — Wikipedia](https://en.wikipedia.org/wiki/Butterfly_lighting), [Paramount lighting — Wikipedia](https://en.wikipedia.org/wiki/Paramount_lighting)


### kicker-light

**Three-quarter backlight kicker** · `lighting` · level basic

```
Cinematic portrait of [Subject], three-quarter backlight, deep shadows on the near
side, a soft key picking out the cheekbone and shoulder line, subtle rim separating
the figure from a dark background, shallow depth of field, 35mm, anamorphic flare.
```

A hard backlight placed behind and roughly 40 degrees off the subject's axis does two jobs at once: it draws a bright edge along the near cheek and shoulder, and it lets the whole front of the figure fall into shadow. That contrast is what makes a dark portrait read as lit rather than underexposed.

**When to use.** Use it when the subject needs weight and separation but the environment should stay quiet: product heroes on dark backgrounds, interview subjects against a dim room, any shot where the silhouette is doing the storytelling.

**Directing the AI.** State the key direction and the falloff explicitly. "Backlit" alone gets you a window behind the subject; "backlight from camera-left at roughly 40 degrees, front falls to shadow, rim highlights the near cheek and shoulder" gets you the shot. Naming which side of the face is dark is the single highest-leverage clause.

**Common mistakes.**
- Filling the shadows. An AI that "balances the exposure" kills the contrast that
- Rimming both sides, which flattens into a halo rather than an edge.
- No background separation, so the rim merges into a bright wall.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_control=true` | kling-1.5 | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | yes |

**Shot cards that can carry it.** `corner-spotlight-reveal` (spotlight-sweep-moves), 135f, `spotlight-hero-card`, 220f

**Sources.** [Rim lighting — Wikipedia](https://en.wikipedia.org/wiki/Rim_light), [Three-point lighting — Wikipedia](https://en.wikipedia.org/wiki/Three-point_lighting)


### low-key-single-source

**Low-key single-source chiaroscuro** · `lighting` · level advanced

```
Chiaroscuro portrait of [Subject] lit by a single low hard source from camera-right,
most of the frame falling into black, one narrow highlight along the brow and cheek,
deep unlit background, no fill, 50mm, film grain, Rembrandt lighting.
```

One source, no fill, and the parts of the face it misses are allowed to stay dark. That is the whole technique: chiaroscuro is a subtraction problem, not a lighting problem. Most prompts fail it by asking for "dramatic moody lighting" and getting even, ambient darkness instead.

**When to use.** Brand work that wants gravity, historical or period framing, and any shot where you want the viewer to complete the missing information.

**Directing the AI.** Name the single source, its position relative to the camera, and the absence of fill. "No fill light, unlit side falls to black" is the clause that does the work. Add a specific shape for the shadow — "a small triangle of light under the far eye" — because "half the face is dark" gets you generic half-light.

**Common mistakes.**
- Adding ambient or bounce the prompt did not ask for; the shadow fills in.
- Losing the shape: the light spills so wide there is no defined terminator.
- Over-grading to black, which costs the subject any readable form.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `negative_prompt=flat lighting, fill light` | kling-1.5 | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 100` | v6.1 | yes |
| `runway_gen3` Runway Gen-3 Alpha | `ratio=16:9, seed=fixed` | gen-3-alpha | no |

**Shot cards that can carry it.** `halation-bloom` (light-play-moves), 159f

**Sources.** [Chiaroscuro — Wikipedia](https://en.wikipedia.org/wiki/Chiaroscuro), [Rembrandt lighting — Wikipedia](https://en.wikipedia.org/wiki/Rembrandt_lighting)


### centered-symmetry

**Centred symmetry for hero objects** · `composition` · level basic

```
Perfectly symmetrical product shot of [Subject] dead centre on the vertical axis,
mirrored surroundings, frontal even lighting, orthographic feel, 100mm, clean
seamless background, no perspective skew.
```

Symmetry is the composition for objects whose shape is the message. When the frame is bisected and both halves match, the eye has nothing to resolve, and the object reads as an icon rather than a photograph.

**When to use.** Brand marks, product hero shots on flat backgrounds, and UI states where symmetry signals precision. Avoid for anything with narrative, because symmetry has no direction for the eye to travel.

**Directing the AI.** "Perfectly symmetrical, dead centre, mirrored background" — the mirroring clause is what makes it work, since the model will happily produce a centred object in an asymmetric room.

**Common mistakes.**
- Near-symmetry: the axis is off by a few pixels, which the eye reads as sloppiness.
- Perspective distortion from a wide lens, breaking the mirror.
- Even lighting across a textured object, which flattens it.

| tool | params | version | tested |
|---|---|---|---|
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 100` | v6.1 | yes |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `brand-frame-snap`, 130f, `circle-match-iris`, 30f

**Sources.** [Symmetry in cinematography — Wikipedia](https://en.wikipedia.org/wiki/Symmetry_in_film), [Centered composition — Wikipedia](https://en.wikipedia.org/wiki/Rule_of_thirds)


### negative-space-frame

**Negative-space frame for a headline** · `composition` · level basic

```
Cinematic frame of [Subject] small and placed low-right, the upper two thirds left
as clean empty wall, even soft light, no clutter, muted palette, 35mm, ample
headroom for a headline.
```

A frame with real empty space is a layout that has already reserved its own copy area. Photographing with the composition you intend to typeset into is the difference between a design that feels designed and one that feels assembled.

**When to use.** Landing page heroes, social cards, and any shot that will carry a headline. Pair it with the motion card that later demotes the title into a section label.

**Directing the AI.** Give a proportion, not a vibe: "upper two thirds empty wall". "Lots of negative space" produces an empty frame with the subject dead centre.

**Common mistakes.**
- Empty space that is not clean, so a headline lands on texture.
- Subject placed on the third line but cropped by the frame edge.
- Light falloff in the copy area, which makes text unreadable over it.

| tool | params | version | tested |
|---|---|---|---|
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | yes |

**Shot cards that can carry it.** `lead-word-zoom-assemble`, 84f, `title-demote-to-label`, 92f

**Sources.** [Negative space — Wikipedia](https://en.wikipedia.org/wiki/Negative_space), [Rule of thirds — Wikipedia](https://en.wikipedia.org/wiki/Rule_of_thirds)


### rule-of-thirds-subject

**Off-centre subject with negative space** · `composition` · level basic

```
Cinematic composition of [Subject] placed on the left third, looking into open
negative space on the right, eye line on the upper horizontal, background uncluttered
and darker than the subject, 35mm, rule of thirds.
```

A subject on a third line, looking into the space it occupies, is a frame that already reads as a frame before anything happens in it. The negative space is not empty: it is the room the shot is going to move into.

**When to use.** Establishing shots, copy-led layouts, and any frame where you will later place text or a product UI. The space you leave is the space you will need.

**Directing the AI.** Say which third and which direction the subject looks. "Off-centre, negative space on the right" is enough; "rule of thirds" alone gets you a centred subject, because that is the model's default reading of a plain product shot.

**Common mistakes.**
- Centring everything, because "cinematic composition" biases toward symmetry.
- Filling the negative space with objects, which leaves nowhere to breathe.
- Horizon tangent to the subject's head, a classic tangency error.

| tool | params | version | tested |
|---|---|---|---|
| `luma` Luma Dream Machine | **null** | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | yes |

**Shot cards that can carry it.** `lead-word-zoom-assemble`, 84f, `title-demote-to-label`, 92f

**Sources.** [Rule of thirds — Wikipedia](https://en.wikipedia.org/wiki/Rule_of_thirds), [Negative space — Wikipedia](https://en.wikipedia.org/wiki/Negative_space)


### hard-cut-on-beat

**Hard cut on the beat** · `editing` · level basic

```
Fast-cut montage on [Subject], every cut landing exactly on a drum transient, six to
twelve frames per shot, no dissolves, hard audio transient on each cut, 24fps
shutter, high contrast.
```

A cut on a transient reads as intentional because the ear and the eye arrive at the same instant. A cut a few frames late reads as a mistake, and no amount of good footage will fix the timing.

**When to use.** Trailers, product hype reels, and the opening thirty seconds of a launch film. This is the technique the upstream `music-beat-sync.md` methodology exists to support, including its hard rule: measure real BPM first, then verify cut error is under three frames against the rendered audio.

**Directing the AI.** "Every cut lands exactly on the drum hit" plus a frame budget. Generate against a known track rather than "to the music", which is the difference between a measurable edit and a hopeful one.

**Common mistakes.**
- Cuts on the wrong transient — snare where the kick is.
- Varying shot length below the readability floor, which becomes flicker.
- Dissolves sneaking in, which smear the audio-image lock the technique needs.

| tool | params | version | tested |
|---|---|---|---|
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |
| `runway_gen3` Runway Gen-3 Alpha | **null** | gen-3-alpha | no |

**Shot cards that can carry it.** `beat-cut-accelerando` (beat-cut-moves), 49f, `jump-cut-punch-in` (rhythm-interrupt-moves), 135f, `strobe-black-frames` (rhythm-interrupt-moves), 135f

**Sources.** [Jump cut — Wikipedia](https://en.wikipedia.org/wiki/Jump_cut), [Montage — Wikipedia](https://en.wikipedia.org/wiki/Montage)


### match-cut-transition

**Match cut on a shared silhouette** · `editing` · level intermediate

```
Cinematic match cut: [Subject] in the first frame and a different scene in the
second frame share the same silhouette and screen position, hard cut on the shape,
no dissolve, matched camera height and focal length across both frames.
```

A match cut hides the edit by making the second frame arrive already aligned with the first. The viewer perceives continuity because the silhouette lands where the previous silhouette was, and never registers the cut itself.

**When to use.** Transitions between a product and the problem it solves, between a UI state and a physical object, and anywhere a hard cut would otherwise feel like a mistake.

**Directing the AI.** Name both frames and the shared property. "Same silhouette, same screen position, same camera height" is the specification; "smooth transition" gets you a dissolve, which is the opposite of the intent.

**Common mistakes.**
- Getting a dissolve or a whip pan: say "hard cut, no transition effect".
- Mismatched camera height, which breaks the alignment the cut depends on.
- Silhouettes that are merely similar rather than identical in position.

| tool | params | version | tested |
|---|---|---|---|
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | yes |
| `runway_gen3` Runway Gen-3 Alpha | `ratio=16:9` | gen-3-alpha | no |

**Shot cards that can carry it.** `black-card-transition` (shot-transitions), `circle-match-iris`, 30f, `color-block-step-wipe`, 44f, `invisible-cut` (transition-hidden-cut)

**Sources.** [Match cut — Wikipedia](https://en.wikipedia.org/wiki/Match_cut), [Graphic match — Wikipedia](https://en.wikipedia.org/wiki/Graphic_match)


### single-take-reveal

**Single-take reveal with one motivated move** · `editing` · level advanced

```
One continuous take on [Subject], beginning tight on a small detail and craning up
and back to reveal the full scene, no cuts, single continuous camera motion, focus
pull from the detail to the far plane as the move finishes, 35mm.
```

A single-take reveal earns attention by withholding. Nothing is hidden by a cut, so the viewer learns the scale of the thing by experiencing the move rather than being told it in a second shot.

**When to use.** Product scale reveals, environment establishing shots, and any moment where a cut would spend the reveal too early.

**Directing the AI.** "Continuous single take, no cuts" has to be explicit — models add cuts freely. Name the start and end of the move and the focus behaviour; the focus pull is what tells the viewer the move has landed.

**Common mistakes.**
- A cut sneaking in mid-move.
- Moving without a focus change, so the reveal has no punctuation.
- Rising too fast to read the detail you started on.

| tool | params | version | tested |
|---|---|---|---|
| `kling15` Kling 1.5 | `camera_control=crane_up` | kling-1.5 | no |
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `crane-rise-reveal`, 20f, `scanline-assemble-flyin`, 138f

**Sources.** [Single-take — Wikipedia](https://en.wikipedia.org/wiki/Continuous_shot), [Crane shot — Wikipedia](https://en.wikipedia.org/wiki/Crane_shot)


### problem-to-solution-beat

**Problem-to-solution two-beat structure** · `narrative` · level basic

```
Two-beat product story: the first frame shows [Subject] mid-friction, the second
frame shows the same subject resolved and calm, matched framing and lighting across
both beats so only the state changes, 50mm, no text.
```

The most durable product structure is a state change, not a feature list. Two frames, matched everything except the thing that is now solved. Because the camera language does not change, the viewer reads the difference as a change in the world rather than a change in the edit.

**When to use.** Launch films, paid social, and anywhere a viewer has about eight seconds of attention. It is also the structure the upstream 36.2s template is built on.

**Directing the AI.** Ask for the matched pair explicitly: "identical framing and lighting in both beats". Without that clause you get two different shots, and the comparison dies.

**Common mistakes.**
- Different lighting between beats, which makes it read as two products.
- Solving the problem with a hard cut to a logo instead of to the product.
- Adding on-screen text, which competes with the state change.

| tool | params | version | tested |
|---|---|---|---|
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | yes |
| `sora` OpenAI Sora | **null** | sora-1 | no |

**Shot cards that can carry it.** `counter-confetti`, 138f, `ui-strip-away-outro`, 130f

**Sources.** [Narrative structure — Wikipedia](https://en.wikipedia.org/wiki/Narrative_structure), [Problem–solution — Marketing examples](https://en.wikipedia.org/wiki/Problem%E2%80%93solution)


### silent-observation-beat

**Silent observation beat before the pitch** · `narrative` · level advanced

```
Documentary-style beat of [Subject] observed in use with no presenter, no voiceover,
natural ambient light only, long unbroken take, hands and screen in frame, 35mm,
shallow focus, observational framing.
```

Showing the tool in someone's hands, unscripted, borrows credibility that a presenter cannot manufacture. The absence of explanation is the technique: the viewer infers the use case, and an inference is more persuasive than a claim.

**When to use.** B2B and developer audiences, long-form landing pages, and anywhere a polished presenter shot would read as an ad.

**Directing the AI.** "No presenter, no voiceover, ambient light only" must all be said. The model defaults to a polished studio look with a talking head, which is the exact opposite of what is being asked.

**Common mistakes.**
- Drifting into a staged three-quarter hero angle mid-take.
- Adding ambient music cues that signal "commercial".
- Over-stabilising, which makes a handheld take look like a tripod.

| tool | params | version | tested |
|---|---|---|---|
| `luma` Luma Dream Machine | **null** | dream-machine | no |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `document-typewriter-reveal`, 110f, `typing-code-block`, 138f

**Sources.** [Observational cinema — Wikipedia](https://en.wikipedia.org/wiki/Observational_documentary), [Handheld shot — Wikipedia](https://en.wikipedia.org/wiki/Handheld_shot)


### analogue-texture

**Analogue film texture, restrained** · `visual-style` · level basic

```
Cinematic still of [Subject] shot on 35mm film, fine organic grain visible in the
shadows, slight halation around highlights, gently lifted blacks, muted filmic
colour, restrained contrast, no heavy vignette, 50mm.
```

Analogue texture is a *shadow* property first: grain lives in the low end, and highlights bloom rather than clip. Adding visible grain over a clean digital render reads as a filter; adding grain into the shadows of a real tonal curve reads as film.

**When to use.** Brand work that wants warmth and imperfection, and as a counterweight to a corpus that otherwise trends toward clean gradient UI motion.

**Directing the AI.** "Grain visible in the shadows, halation around highlights" does the work. "Film grain" on its own gets an even digital noise overlay across the whole frame.

**Common mistakes.**
- Uniform noise over the whole frame rather than concentrated in the shadows.
- Crushed blacks, which kills the grain along with the detail.
- Heavy vignette, which is a different look entirely (analogue lens falloff).

| tool | params | version | tested |
|---|---|---|---|
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50 --s 250` | v6.1 | yes |
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |

**Shot cards that can carry it.** `grain-dissolve`, 60f, `riso-beat-pump` (riso-print-hits), 120f

**Sources.** [Film grain — Wikipedia](https://en.wikipedia.org/wiki/Film_grain), [Halation — Wikipedia](https://en.wikipedia.org/wiki/Halation)


### cold-blue-tech

**Cold blue technical palette** · `visual-style` · level basic

```
Cold blue technical frame of [Subject], cool desaturated palette, blue-grey metal,
soft gradient background, precise specular highlights, minimal saturation, clean
industrial surfaces, 50mm, high micro-contrast.
```

A palette does work when every colour in it has the same temperature. The cold blue look survives scrutiny because nothing in the frame is warm enough to break it — the failure mode is one skin-tone or one warm prop in a supposedly cool scene.

**When to use.** Infrastructure and developer tooling, hardware, and enterprise work where "serious" is the register being aimed at.

**Directing the AI.** State the temperature constraint as a prohibition as well as a direction: "no warm tones". A palette described only positively will still admit a warm accent.

**Common mistakes.**
- One warm element surviving in the background.
- Over-saturating the blue until it reads as a filter rather than a material.
- Losing micro-contrast, which turns "precise" into "soft".

| tool | params | version | tested |
|---|---|---|---|
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 50` | v6.1 | yes |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `gradient-transition`, 180f, `neon-frame-forerun`, 18f

**Sources.** [Colour temperature — Wikipedia](https://en.wikipedia.org/wiki/Color_temperature), [Cinecolor — Wikipedia](https://en.wikipedia.org/wiki/Cinecolor)


### restrained-motion-graphics

**Restrained motion graphics for software** · `visual-style` · level basic

```
Clean product motion frame showing [Subject] as a crisp UI surface on a flat dark
ground, one element moving with a single ease, everything else perfectly still,
precise 8px spacing grid, one accent colour used once, no decorative glow, 60fps.
```

The restraint is the style. When exactly one element moves on an 8-pixel grid with a single ease, the movement reads as information; when four things move with decorative easing, the same movement reads as a template.

**When to use.** SaaS and developer tools, especially anything shipped alongside real UI. It also matches the upstream rule set directly: one motion idea per shot, holds after every key beat, no batch glows.

**Directing the AI.** "One element moving, everything else still, single ease" is the clause. Without "everything else still" you get every element animating, which is the failure this style exists to avoid.

**Common mistakes.**
- Batch entrances with per-item easing, which reads as busy rather than precise.
- Glow and bloom on UI elements, which makes flat design look dirty.
- Sub-pixel positions that make the grid read as sloppy.

| tool | params | version | tested |
|---|---|---|---|
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --cw 100` | v6.1 | yes |
| `sora` OpenAI Sora | **null** | sora-1 | no |

**Shot cards that can carry it.** `blur-slide`, 114f, `skeleton-reveal`, 172f, `typing-code-block`, 138f

**Sources.** [Material Design — motion](https://m3.material.io/styles/motion/overview), [Apple Human Interface Guidelines — motion](https://developer.apple.com/design/human-interface-guidelines/motion)


### documentary-naturalism

**Documentary naturalism** · `genres` · level basic

```
Documentary shot of [Subject] in its real environment, available window light only,
handheld but composed, muted natural colour, no stylisation, slight exposure
irregularity, 35mm, observational distance.
```

Naturalism is a constraint list: existing light, real locations, no styling, no clean-up. What it buys is belief. A viewer who suspects a set stops evaluating the content and starts evaluating the production.

**When to use.** Testimonials, case studies, and anything where credibility matters more than polish.

**Directing the AI.** "Available window light only, no stylisation, no colour grading" is the set of clauses. Leave any of them out and the model applies its default commercial-grade finish, which is exactly what the genre is avoiding.

**Common mistakes.**
- Styling the environment, which reads as a set.
- Perfect exposure, which reads as a still rather than a frame from a moving shot.
- Over-clean skin and walls, which is the fastest way to lose naturalism.

| tool | params | version | tested |
|---|---|---|---|
| `luma` Luma Dream Machine | **null** | dream-machine | no |
| `sora` OpenAI Sora | **null** | sora-1 | no |
| `veo2` Google Veo 2 | **null** | veo-2 | no |

**Shot cards that can carry it.** `row-embed`, 68f, `skeleton-reveal`, 172f

**Sources.** [Direct cinema — Wikipedia](https://en.wikipedia.org/wiki/Cinema_verite), [Available light — Wikipedia](https://en.wikipedia.org/wiki/Available_light)


### high-key-white-studio

**High-key white studio product shot** · `genres` · level basic

```
High-key studio product photograph of [Subject] on a seamless white sweep, soft
overhead key with a fill card, shadow falling softly beneath the object, colour
accurate, even exposure with no clipping, 100mm macro, commercial catalogue look.
```

High-key is an exposure discipline: keep every surface inside the range where the material is still readable. Clip the white background and the object stops looking like an object and starts looking like a shape cut out of paper.

**When to use.** Catalogue and e-commerce, marketplaces, and any frame where the viewer needs to judge the actual colour and material of the product.

**Directing the AI.** "Even exposure, no clipping, colour accurate" plus "soft shadow beneath". Without the clipping clause, white backgrounds blow out and take the product edge with them.

**Common mistakes.**
- Clipped highlights on a white object against white, which erases its silhouette.
- Hard multiple shadows from an unstated multi-light setup.
- Colour shifts from aggressive white balance.

| tool | params | version | tested |
|---|---|---|---|
| `luma` Luma Dream Machine | **null** | dream-machine | no |
| `mj61` Midjourney v6.1 | `--ar 1:1 --v 6.1 --style raw --cw 100` | v6.1 | yes |
| `sora` OpenAI Sora | **null** | sora-1 | no |

**Shot cards that can carry it.** `brand-frame-snap`, 130f, `product-card-progressive-assemble`, 150f

**Sources.** [High-key lighting — Wikipedia](https://en.wikipedia.org/wiki/High-key_lighting), [Product photography — Wikipedia](https://en.wikipedia.org/wiki/Product_photography)


### retro-analogue-comedy

**Retro analogue comedy framing** · `genres` · level intermediate

```
Retro 1970s comedy scene with [Subject] shot on vintage 16mm, slightly soft focus,
visible gate weave, warm amber cast, wide static framing with the subject small in
frame, deadpan timing, no camera movement.
```

Genre framing is mostly about how much frame you leave empty and how still the camera is. A 70s comedy shot is soft, warm, static and wide, and the stillness is what leaves room for the timing to do the work.

**When to use.** Humour, explainers that want warmth, and any brand that benefits from looking handmade rather than clinical.

**Directing the AI.** Name the stock and the framing: "vintage 16mm, warm amber, wide static framing, subject small in frame". "Retro" alone produces a costume-drama look, not a comedy one.

**Common mistakes.**
- Adding camera movement, which kills the deadpan timing the genre depends on.
- Pushing the subject too large, which loses the dead air the jokes land in.
- Over-sharpening, which reads as "old filter" instead of old film.

| tool | params | version | tested |
|---|---|---|---|
| `mj61` Midjourney v6.1 | `--ar 16:9 --v 6.1 --style raw --cw 100` | v6.1 | yes |
| `pika15` Pika 1.5 | **null** | pika-1.5 | no |

**Shot cards that can carry it.** `cel-flash-stomp`, 30f

**Sources.** [16mm film — Wikipedia](https://en.wikipedia.org/wiki/16_mm_film), [Slapstick — Wikipedia](https://en.wikipedia.org/wiki/Slapstick)
