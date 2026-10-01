# 0007 — The cinematic-technique catalog is a second corpus, ingested into the same DB

- Status: accepted
- Date: 2026-09-28

## Context

We have one corpus today: 157 shot recipe cards from `upstream/video-shotcraft`,
covering **motion** — easing curves, springs, timing windows, render parameters.

A second corpus is proposed: **cinematic prompting techniques**
(Camera Work, Lighting, Composition, Editing, Narrative, Visual Style, Film
Styles), each with a production-ready prompt template, a `when to use` rationale,
a `directing the AI` note, a `common mistakes` list, film citations, a reference
image, and — the part that matters commercially — a **cross-tool parameter
matrix**: the same technique expressed for Midjourney v6.1, Runway Gen-3,
Google Veo 2, Kling 1.5, Luma Dream Machine, Pika 1.5 and Sora.

> **Correction, 2026-10-01.** This ADR originally described a *150-technique*
> catalog with a 117/150 filled matrix. That corpus was never authored. What
> exists today is a **seed corpus of 20 techniques across all 7 categories**,
> with a deliberately sparse matrix: 45 listed cells, 23 carrying a parameter,
> **16 actually tested**, 22 empty. The architecture below is unchanged; only the
> scale claim was wrong, and it is corrected here rather than left standing.

The two corpora are not competitors. They are **consecutive stages of one
pipeline**:

```
cinematique (this catalog)          shotcraft (upstream corpus)
─────────────────────────          ─────────────────────────────
WHAT to shoot                       HOW it moves
camera, light, composition,        easing, spring, timing,
editing rhythm, genre              render duration
         │                                    │
         └──────────────► Remotion ◄───────────┘
                    (motion execution + render)
```

A prompt without motion is a still. A motion curve without a shot decision is
decoration. The reference videos the catalog lacks are exactly the gap `F060`
(Remotion render) is blocked on.

- **Current scale: 20 techniques.** The catalog is a seed, not a library: the
  subset we can defend from real cinematography practice today. Growing it is
  mechanical — add a file, re-run the ingest — and the growth stays visible in
  `doctor.py` rather than implied by a target number.

## Decision

Ingest the cinematic catalog **into the same SQLite DB**, as its own numbered
schema section, and compile it to briefs **with the same compiler discipline** as
the shot cards.

Concretely:

1. `data/cinematic/` is **source** — hand-curated, versioned, committed. It is the
   only place the catalog is authored.
2. `platform/ingest/catalog.py` reads `data/cinematic/` and writes schema
   section 10: `cinematic_technique`, `ai_tool`, `technique_param`,
   `technique_tool_param`, `technique_related`, `technique_source`.
3. The cross-tool matrix is a **join table** (`technique_tool_param`), not a
   column — the same way `card_variant` already models card↔style.
4. A second compiler, `platform/catalog/build_briefs.py`, emits
   `prompts/catalog/generated/<slug>.json` under schema `cinematic.brief/1`,
   mirroring `shotcraft.brief/1`.
5. A tenth wiki domain, `wiki/domains/cinematic-techniques.md`, is generated like
   the other nine.

### Why one DB and not a second one

`docs/architecture/README.md` already states the bet: *"Everything downstream
reads the DB. Nothing downstream reads markdown directly. That is the whole
architectural bet: one parse, many consumers."*

Two databases means two parses, two FTS cascades, two sets of invariants, and an
N×M join that must be maintained by hand in application code. The join we
actually need — *"which shot cards can realize this cinematic technique, and with
which parameters?"* — is one `JOIN` in SQL and nothing anywhere else.

The two corpora share a second property that settles it: **both are keyed by a
kebab-case slug that is also its filename, and both are rendered into briefs by
the same shape of compiler.** The join keys already exist.

### Why `data/` and not `upstream/`

`upstream/` is read-only and git-ignored, because it is someone else's repo and
we pin a SHA. The cinematic catalog is **ours** — we curated it, we own the
cross-tool matrix, and we will version it ourselves. It therefore belongs under
version control as source, which is exactly what `data/` is for. This ADR gives
`data/` its job: `data/cinematic/README.md` states the file format and the three
rules, and the test is the same as everywhere else — delete any generated tree,
re-run its builder, get it back; but delete `data/cinematic/` and it does **not**
come back, because it was never generated.

### The verbatim rule applies here too

Schema preamble rule 4 says upstream prose is stored twice — verbatim plus
normalized — and *"never let the normalized value replace the verbatim column."*
The catalog's `prompt_template` is verbatim source text with a `[Subject]`
placeholder. That is a **slot**, not a template to expand. Storing the verbatim
string and keeping `[Subject]` intact is the difference between a re-runnable
ingest and a corrupted corpus.

## Consequences

**Good**

- One place to ask "how do I shoot a three-quarter backlight with a slow dolly
  in?" — `JOIN cinematic_technique ↔ shot_card`.
- The 150 briefs inherit the `generated` / `reference` split, so the
  machine-filler problem in F050's copy slots is solved the same way here.
- The wiki gains a domain an LLM can query without touching the filesystem.
- `platform/doctor.py` gains a `catalog.*` invariant family for free.

**Bad**

- `schema.sql` grows. Section 10 therefore lives in
  `platform/catalog/schema.sql` rather than in the upstream schema file: a
  150-line append from a different workstream in a file someone else edits is a
  merge conflict waiting to happen. `run.py` applies both, in that order.
- Ingest becomes non-idempotent-by-single-source: two inputs (`upstream/` clone +
  `data/cinematic/`) instead of one. `run.py` must handle a missing
  `data/cinematic/` gracefully rather than failing.
- `platform/query.py` gains a second namespace (`technique`, `optimize`), and
  every existing command must keep working unchanged.

**Neutral**

- The 22 empty cross-tool cells stay empty. Per `prompts/README.md`, an absent
  value is `null` and is reported, not estimated. A tool parameter we have not
  tested is `null`, not a plausible string. Of the 23 cells that *do* carry a
  parameter, only the 16 Midjourney ones have actually been run — the `tested`
  column carries that distinction per cell, and `query.py optimize` prints it
  rather than presenting an untested string as an authored one.

## Alternatives rejected

**Keep the catalog in its own repo and sync.** Rejected: the join is the product.
Two repos means the interesting question — *"which motion cards serve technique
X"* — is unanswerable without a build step, and the answer is the reason we are
doing this.

**Flatten the cross-tool matrix into JSON on the technique row.** Rejected: it
makes the matrix unfilterable. "All techniques with a tested Kling parameter"
would be a full scan plus a parse in application code, in a corpus we already
know how to put in FTS5.

**Generate briefs straight from the CSV without a schema.** Rejected: it breaks
ADR 0002. If the catalog is not in the DB, the wiki cannot be generated, the API
cannot serve it, and `doctor.py` cannot check it.

**Fill the matrix gaps by inference.** Rejected outright, and recorded here so nobody
re-litigates it: `duration_frames` is `null` for 5 upstream technique cards
because the corpus does not state one, and that is *"the correct value, not a gap
to fill by estimating."* Same rule here — and the same rule applies to growing the
corpus itself: 20 real techniques beat 150 plausible ones, because a reviewer has
to be able to tell which is which.

## See also

- `AGENTS.md` hard rules (upstream read-only, DB generated, prose stored twice)
- ADR 0002 (SQLite + FTS5 as the single index) · ADR 0003 (generated, never
  hand-written) · ADR 0006 (SDD loop with a verifier-owned gate)
- `specs/features/F070-cinematic-catalog-ingest.md` (ingest),
  `F071` (brief compiler), `F072` (wiki domain), `F073` (cross-tool optimizer)
- `docs/monetization/0002-blocking-issues.md` — `F060` render stays blocked on
  the Remotion licence question; this layer does not unblock it
