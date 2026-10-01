"""Declared technique → shot-card pairings (F074).

This is the join the whole catalog layer exists for: *"I decided on a dolly
push — what motion parameters can realize it?"* It is a hand-authored table, not
a name-similarity heuristic, and that distinction is the feature.

Why a table and not a heuristic
-------------------------------
`dolly-shot` and `pull-out` share no tokens, yet both are push/pull camera
moves. String matching would pair them and also pair `close-up` with
`magnifier-zoom` purely on `up`, producing confident nonsense. A wrong pairing is
worse than a missing one, because it hands a client a specific duration and
easing and looks researched. So: an unmapped technique returns an empty list and
says so.

Why cards and not styles
------------------------
The join key is the shot card, not the style. A card is what a client buys (a
recipe with a cast, a parameter table and pitfalls); a style is one variant of
it. Pairing at the card level means one technique resolves to N shot cards, each
with its own duration and parameter table, and the styles come along for free.
`technique_motion.kind` records whether a pairing was `declared` (here) or
`curated` (a shot-card link inside a technique's own Related block).

Every entry below is defensible from real cinematography: the card performs the
move or holds the lighting pattern the technique describes. Nothing here is
"probably related".
"""

from __future__ import annotations

# technique slug -> list of shot-card names
PAIRINGS: dict[str, list[str]] = {

    # ---------------------------------------------------------------- camera
    "dolly-shot": ["tension-camera-moves", "crash-zoom-punch"],
    "push-in": ["tension-camera-moves"],
    "pull-out": ["space-camera-moves"],
    "tracking-shot": ["cursor-flyover", "space-camera-moves"],
    "crane-shot": ["crane-rise-reveal"],
    "aerial-shot": ["overhead-camera-moves", "crane-rise-reveal"],
    "overhead-shot": ["overhead-camera-moves"],
    "birds-eye-view": ["overhead-camera-moves"],
    "high-angle-shot": ["overhead-camera-moves"],
    "low-angle-shot": ["steep-tilt-glide"],
    "tilt-shot": ["steep-tilt-glide"],
    "worms-eye-view": ["steep-tilt-glide"],
    "dutch-angle": ["steep-tilt-glide", "fracture"],
    "close-up": ["spotlight-hero-card"],
    "extreme-close-up": ["spotlight-hero-card"],
    "medium-close-up": ["spotlight-hero-card"],
    "medium-shot": ["spotlight-hero-card", "space-camera-moves"],
    "long-shot": ["space-camera-moves"],
    "extreme-long-shot": ["space-camera-moves"],
    "establishing-shot": ["depth-layer-moves", "space-camera-moves"],
    "360-degree-shot": ["orbit-ring-title-open"],
    "crash-zoom": ["crash-zoom-punch"],
    "whip-pan": ["tension-camera-moves"],
    "pan-shot": ["space-camera-moves"],
    "handheld-shot": ["graze-face-tour"],
    "steadicam": ["graze-face-tour"],
    "rack-focus": ["depth-layer-moves"],
    "slow-motion": ["graze-face-tour"],
    "static-shot": ["basic-3d-scene"],
    "eye-level-shot": ["graze-face-tour"],
    "head-on-shot": ["basic-3d-scene"],
    "master-shot": ["space-camera-moves"],
    "three-shot": ["space-camera-moves"],
    "two-shot": ["space-camera-moves"],
    "over-the-shoulder": ["space-camera-moves"],
    "insert-shot": ["depth-layer-moves"],
    "choker-shot": ["spotlight-hero-card"],
    "cowboy-shot": ["spotlight-hero-card"],
    "pov-shot": ["graze-face-tour"],
    "one-er": ["fracture"],
    "vertigo-effect": ["crash-zoom-punch", "steep-tilt-glide"],

    # -------------------------------------------------------------- lighting
    "three-point-lighting": ["spotlight-hero-card"],
    "key-light": ["spotlight-hero-card"],
    "fill-light": ["spotlight-hero-card"],
    "backlight": ["spotlight-hero-card"],
    "kicker-light": ["spotlight-hero-card"],
    "edge-light": ["spotlight-hero-card"],
    "side-lighting": ["spotlight-hero-card"],
    "cross-lighting": ["spotlight-hero-card"],
    "rembrandt-lighting": ["spotlight-hero-card"],
    "high-key-lighting": ["spotlight-hero-card"],
    "bounce-light": ["spotlight-hero-card"],
    "low-key-lighting": ["brand-ink-open", "spotlight-hero-card"],
    "chiaroscuro": ["brand-ink-open"],
    "film-noir": ["brand-ink-open", "fracture"],
    "silhouette": ["brand-ink-open"],
    "ambient-light": ["brand-ink-open"],
    "soft-light": ["spotlight-hero-card"],
    "hard-light": ["fracture"],
    "available-light": ["letterspace-materialize"],
    "color-temperature": ["letterspace-materialize"],
    "blue-hour": ["letterspace-materialize"],
    "golden-hour": ["letterspace-materialize"],
    "practical-lighting": ["icon-field-colorize"],
    "motivated-lighting": ["icon-field-colorize"],
    "gobo-lighting": ["icon-field-colorize"],
    "dappled-light": ["icon-field-colorize"],
    "lens-flare": ["text-as-mask"],
    "short-lighting": ["spotlight-hero-card"],
    "broad-lighting": ["spotlight-hero-card"],
    "uplighting": ["fracture"],
    "eye-light": ["spotlight-hero-card"],

    # ---------------------------------------------------------- composition
    "rule-of-thirds": ["spotlight-hero-card", "space-camera-moves"],
    "negative-space": ["brand-ink-open", "spotlight-hero-card"],
    "headroom": ["spotlight-hero-card"],
    "lead-room": ["space-camera-moves"],
    "leading-lines": ["space-camera-moves"],
    "depth-of-field": ["depth-layer-moves"],
    "shallow-focus": ["depth-layer-moves"],
    "deep-focus": ["space-camera-moves"],
    "symmetry": ["orbit-ring-title-open"],
    "centered-composition": ["orbit-ring-title-open"],
    "framing-within-frame": ["spotlight-hero-card"],
    "figure-ground": ["brand-ink-open"],
    "contrast-composition": ["fracture"],
    "visual-weight": ["orbit-ring-title-open"],
    "repetition-and-pattern": ["icon-field-colorize"],
    "triangular-composition": ["spotlight-hero-card"],
    "diagonal-lines": ["steep-tilt-glide"],
    "mise-en-scene": ["space-camera-moves"],
    "golden-ratio": ["orbit-ring-title-open"],
    "balancing-elements": ["space-camera-moves"],
    "foreground-interest": ["depth-layer-moves"],

    # -------------------------------------------------------------- editing
    "iris-transition": ["circle-match-iris"],
    "dissolve": ["shot-transitions"],
    "wipe-transition": ["color-block-step-wipe"],
    "montage": ["beat-cut-moves"],
    "jump-cut": ["beat-cut-moves"],
    "fast-motion": ["speed-ramp-freeze"],
    "slow-motion": ["speed-ramp-freeze", "graze-face-tour"],
    "freeze-frame": ["montage-rhythm-moves"],
    "time-lapse": ["speed-ramp-freeze"],
    "smash-cut": ["impact-feedback"],
    "split-screen": ["scanline-assemble-flyin"],
    "long-take": ["crane-rise-reveal"],
    "cut-in": ["circle-match-iris"],
    "cutaway": ["circle-match-iris"],
    "reverse-motion": ["crash-zoom-punch"],
    "cross-cutting": ["beat-cut-moves"],
    "fade-in-out": ["chip-grid-single-select-blackout"],
    "reaction-shot": ["impact-feedback"],

    # -------------------------------------------------------------- genres
    "noir-tech": ["brand-ink-open", "fracture"],
    "vaporwave": ["gradient-transition"],
    "wuxia": ["cel-flash-stomp"],
    "cosmic-horror": ["fracture"],
    "slow-cinema": ["space-camera-moves"],
    "poetic-realism": ["letterspace-materialize"],
    "cinema-verite": ["graze-face-tour"],
    "found-footage": ["graze-face-tour"],
    "mockumentary": ["graze-face-tour"],
    "dogme-95": ["letterspace-materialize"],
    "italian-neorealism": ["letterspace-materialize"],
    "german-expressionism": ["fracture"],
    "giallo": ["fracture"],
    "surrealism": ["magician-card-flourish"],
    "french-new-wave": ["shot-transitions"],
    "acid-western": ["cel-flash-stomp"],
    "spaghetti-western": ["cel-flash-stomp"],
    "southern-gothic": ["brand-ink-open"],
    "hyperlink-cinema": ["glitch-cycle"],
    "mumblecore": ["letterspace-materialize"],

    # ------------------------------------------------------------ narrative
    "motif": ["icon-field-colorize"],
    "symbolism": ["text-as-mask"],
    "cliffhanger": ["montage-rhythm-moves"],
    "flashback": ["shot-transitions"],
    "flashforward": ["shot-transitions"],
    "in-medias-res": ["beat-cut-moves"],
    "non-linear-narrative": ["circle-match-iris"],
    "frame-narrative": ["stroke-segment-build"],
    "foreshadowing": ["assemble-then-type-flyin"],
    "voiceover-narration": ["typing-code-block"],
    "breaking-fourth-wall": ["cursor-flyover"],
    "parallel-storylines": ["split-flap-title"],
}


def cards_for(slug: str) -> list[str]:
    return PAIRINGS.get(slug, [])


def unmapped(slugs: list[str]) -> list[str]:
    return sorted(s for s in slugs if s not in PAIRINGS)