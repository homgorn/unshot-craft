# `prompts/` — shot briefs

A **brief** is everything needed to execute one shot: cast, timing, parameters,
pitfalls, cited rules, style list. One per card.

```
prompts/
├── generated/       157 shot briefs — BUILD OUTPUT, never hand-edited
│   ├── <slug>.json
│   └── index.json
├── reference/       hand-authored shot briefs — SOURCE, the quality bar
└── catalog/         150 cinematic-technique briefs (ADR 0007, F071)
    ├── generated/   BUILD OUTPUT — schema cinematic.brief/1
    └── reference/   hand-authored — SOURCE
```

`catalog/` is a second corpus with the same discipline and a different subject:
`generated/` answers *how a shot moves*, `catalog/` answers *what to shoot*. The
join between them is `technique_motion`, declared in `data/cinematic/` and never
inferred. See `specs/features/F070-cinematic-catalog-ingest.md`.
prompts/
├── generated/     157 briefs — BUILD OUTPUT, never hand-edited
│   ├── <slug>.json
│   └── index.json
└── reference/     hand-authored briefs — SOURCE, the quality bar
```

`generated/` is a pure function of `platform/db/shotcraft.db`. Delete it and
`python platform/prompts/build_prompts.py` reproduces it byte-identically.
Same discipline as `wiki/` (ADR 0003).

## The rule: the brief is structure, the copy is a slot

`build_prompts.py` never invents prose. Every string it emits is either verbatim
upstream text or a literal marker, and every generated brief carries:

```json
"copy": {
  "status": "unfilled",
  "authored": false,
  "note": "Structure below is generated from the recipe. Copy is NOT. …",
  "slots": [ { "id": "headline", "max_chars": 40, "hint": "…", "status": "unfilled" } ]
}
```

**Why this is a hard rule and not a style preference.** A generated one-liner reads
exactly like an authored one. Hand it to an agent and it will quote it to a client as
though a human wrote it — and we would be selling machine filler as taste, in a
business whose entire pitch is that we have taste. The slot makes the gap impossible
to miss.

So the flow is: generate the structure → fill the slots by hand or by an agent →
the filled brief becomes a *reference* brief with `source.brief_kind: "hand"` and
`copy.authored: true`.

## `generated` vs `reference`

| | `generated/` | `reference/` |
|---|---|---|
| who writes it | `build_prompts.py` | a human or an agent |
| `source.brief_kind` | `"generated"` | `"hand"` |
| `copy.authored` | `false`, always | `true`, always |
| every slot filled | no | yes |
| purpose | coverage, agent-readable structure | the quality bar, and studio portfolio input |
| editable | never | yes — this is source |

`build_prompts.py --lint` and `platform/doctor.py` both enforce the right-hand column.
A file claiming to be hand-authored with an unfilled slot is an error, not a warning.

## Read `segments[]` before you render

`segments[]` comes from `motion_param`, which is scraped from the demo `.tsx` — so it
is authoritative where the prose is not. But it is not uniformly usable:

```json
{ "window": [0, 0.14], "ease": "E.outCubic", "concrete": true,  "raw": "seg(t, 0, 0.14, E.outCubic)" }
{ "window": null,       "from": "FLY_AT[i]", "to": "FLY_AT[i] + FLY",
  "concrete": false, "raw": "const f = seg(t, FLY_AT[i], FLY_AT[i] + FLY, E.inOutCubic)" }
```

`concrete: false` means the timing is expressed as a variable lookup. Resolve it
against the demo file or do not use it. Never hand `FLY_AT[i]` to a renderer as if it
were a number.

## Timing coverage is honestly partial

Over 1,349 motion-section bullets the corpus states timing in about five
incompatible notations, and the most common one is **frames** (`126f`), not
normalized units. Only 24 of 157 cards have a beat with a stated `[t0, t1]`; only 44
of 218 demos contain a literal `seg()` call.

> **A normalized timeline cannot be auto-derived.** The demos remain the
> authoritative implementation, and a real timeline is authored — which is what
> `reference/` is for.

`render.duration_frames` is `null` for 5 technique cards. That is the correct value,
not a gap to fill by estimating.

## Related

- Builder: `platform/prompts/build_prompts.py`
- Feature: `specs/features/F050-recipe-prompt-compiler.md` (compile), `F051` (reference briefs)
- Catalog builder: `platform/catalog/build_briefs.py` (F071)
- Catalog source: `data/cinematic/` — authoring contract in `data/README.md`
- Catalog features: `F070` ingest · `F071` compile · `F072` wiki · `F073` optimizer · `F074` motion pairing
- Blocked: `F060` (render to MP4) — needs the Remotion licence answer and the
  `video-talkcraft` PolyForm answer, see `docs/monetization/0002-blocking-issues.md`
- ADR 0003 (generated, never hand-edited) · ADR 0005 (upstream stays read-only)