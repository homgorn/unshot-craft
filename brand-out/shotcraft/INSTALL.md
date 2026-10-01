# shotcraft studio v1.0.0

House brand for the shotcraft studio. Layered over the upstream Remotion template without editing it.

## Install

```
python platform/brand_kit.py install shotcraft
```

Writes `brand-out/shotcraft/`. Nothing under `upstream/` is read for writing or modified.

## Use

Point the Remotion render at the overlay:

```
remotion render src/index.ts out.mp4 --public-dir brand-out/shotcraft
```

and import `tokens.css` before the template's stylesheet, `overlay.css` after it.

## Uninstall

```
python platform/brand_kit.py uninstall shotcraft
```

## What this deliberately does not set

Motion parameters are NOT a brand concern. They live in the shot-card corpus and are compiled into a brief per shot. A kit that tried to set them here would fork the corpus.
