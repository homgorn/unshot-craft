# `data/` — authored source of truth

Everything under `data/` is **source**: written by a human or an agent, committed,
reviewed in a diff, changed on purpose.

Everything generated lives elsewhere and is reproducible:

| tree | produced by | editable |
|------|-------------|----------|
| `upstream/video-shotcraft/` | `git clone` (pinned SHA) | **never** |
| `data/cinematic/` | us | **yes — this is source** |
| `platform/db/shotcraft.db` | `platform/ingest/run.py` | never |
| `wiki/` | `platform/wiki/build_wiki.py` | never |
| `prompts/generated/` | `platform/prompts/build_prompts.py` | never |
| `prompts/catalog/generated/` | `platform/catalog/build_briefs.py` | never |
| `site/dist/` | `platform/site/build_site.py` | never |

The test: delete any generated tree, re-run its builder, get it back byte-identically.
If you cannot do that, the file is in the wrong place.

## `data/cinematic/` — the cinematic-technique catalog

150 techniques covering camera work, lighting, composition, editing, narrative,
visual style and film genres. Each is one markdown file, one technique, named for
its slug — the same `name`-is-the-filename discipline the shot cards use.

```
data/cinematic/
  README.md              this file's sibling: the authoring contract
  camera-work/
    aerial-shot.md
    close-up.md
    dolly-shot.md
  lighting/
    kicker-light.md
    three-point-lighting.md
  composition/
  editing/
  narrative/
  visual-style/
  genres/
```

### File format

YAML-ish frontmatter, then prose sections — the same shape as
`upstream/video-shotcraft/references/shots/<cat>/<name>.md`, so one parser reads
both corpora.

```markdown
---
slug: kicker-light
title: Kicker Light
category: lighting
level: intermediate
image: https://…/kicker-light.webp
video: null
styles: [kicker-flick, hair-rim]
---

## Prompt

Kicker light on [Subject], a hard backlight source placed low and behind the
subject, throwing a bright rim along the hair and shoulder line…

## When to use

## Directing the AI

## Common mistakes

1.
2.
3.

## Cross-tool

| tool | params | tested |
|------|--------|--------|
| mj61 | `--ar 16:9 --v 6.1 --style raw --cw 50` | yes |
| runway_gen3 | `motion_brush: … ` | yes |
| veo2 | | no |

## Sources

- [title](url)
```

### Three rules for authoring here

1. **`[Subject]` is a slot. Never expand it.** The ingest stores `## Prompt`
   verbatim. A prompt that has had its slot filled is a corrupted row, and
   `platform/doctor.py` fails the build on it — the same contract as
   `copy.slots[]` in `prompts/README.md`.
2. **An untested tool parameter is an empty cell, not a plausible default.**
   `doctor.py` prints `filled_cross_tool_cells`. Today it is **117 of 150**. Do not
   raise it by inventing strings; raise it by testing them.
3. **`styles:` is a declared relation, not a guess.** It lists shot cards from
   `upstream/` that can realize this technique. `F074` joins on it. A technique
   with no `styles:` has no motion pairing, and that is reported, not filled in by
   name similarity.

### Provenance

Every file's sha256 is recorded at ingest into `source_file`, so any DB row can be
traced back to the exact authored bytes, the same way upstream rows trace to an
upstream commit.
