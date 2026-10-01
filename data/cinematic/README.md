# `data/cinematic/` — the cinematic-technique catalog (source)

This directory is **source**, not generated. See `docs/adr/0007-cinematic-catalog-layer.md`.

It answers a question the shot-card corpus cannot: **what to shoot**. The upstream
corpus knows how a shot moves — easing curves, springs, timing windows, render
parameters. It has no opinion on focal length, key direction or colour science,
because upstream renders design-system demos, not films.

Together they are consecutive stages of one pipeline:

```
cinematic catalog                     shot-card corpus
what to shoot   ─────────────────────►  how it moves
camera, light, composition,           easing, spring, timing,
editing rhythm, genre                   render duration
                │                                  │
                └──────────► Remotion ◄────────────┘
```

## The file format

One file per technique, kebab-case slug as the filename. The slug is the join key
against `shot_card.name` and `style.key`.

```
---
slug: kicker-light              # the join key, ASCII kebab-case
title: Three-quarter backlight kicker
category: lighting               # one of 7 controlled values, or ingest fails
level: basic                     # basic | intermediate | advanced
image: <url>                     # reference still
video: <url>                     # optional: 0 of 14 currently have one
styles: [spotlight-sweep, ...]   # optional, explicit shot-card handoffs
---

<the prompt, verbatim, with [Subject] intact as a slot>

## Lede            one paragraph: what the technique actually is
## When to use     when to reach for it, and when not to
## Directing the AI  the specific clauses that make the prompt work
## Common mistakes  failure modes an AI actually produces
## Sources         film / technique citations
## Cross-tool      one row per tool; an empty cell is NULL, never a guess
## Related         links to sibling techniques and to shot cards
```

## Three rules that are not stylistic

1. **`[Subject]` is a slot, never expanded.** The prompt is stored verbatim. An
   expanded prompt reads exactly like an authored one, and an agent handed it will
   paste it to a client as though the studio wrote it.
2. **An absent cross-tool cell is `null`, not a default.** A tool parameter nobody
   has run is an untested claim, and a plausible string in that cell is a claim we
   cannot defend to a client. `tested: no` in the table is the honest state.
3. **`category` is a controlled vocabulary.** A value outside the seven fails the
   ingest rather than landing in `other`, which is what makes
   `query.py technique --category lighting` a filter instead of a guess.

## Current state

**14 techniques across all 7 categories.** This is a seed corpus, not the finished
catalog: the techniques here are the ones we can defend from real cinematography
practice today. `platform/doctor.py` reports the count and the unfilled-cell count
rather than a target, so nobody can mistake a partial corpus for a complete one.

The gap is curation, and it is deliberately visible. Two consequences:

- `docs/adr/0007` and `specs/features/F070` originally described a 150-technique
  corpus with a 117/150 filled matrix. That corpus has not been written. Both
  documents have been corrected to state what exists.
- The cross-tool matrix here is sparse by design: only `mj61` cells are marked
  tested, because only those were actually run. The rest are recorded as untested
  parameters or left `null`.

Growing it is mechanical once the pattern exists: add a file, re-run
`python platform/ingest/run.py`. Do not backfill the matrix by inference.