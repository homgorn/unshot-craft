# ADR 0005 — Upstream is a pinned source, not a base

- Status: accepted (in force)
- Decided: 2026-10-01
- Supersedes: nothing

## Context

`video-shotcraft` is Apache-2.0, has ~10.1k stars and ~899 forks, and is actively
maintained by its author (Vincentwei1021). Its own `demos/README.md` and
`references/shots/ATTRIBUTION.md` make clear the motion techniques were researched
from publicly released promo films and open-source project pages, and **re-implemented
from scratch** — no original footage, screenshots, art or brand elements are
included, and the copy and palettes are neutral placeholders.

There is also a sibling project, `video-talkcraft` (~1.3k stars), licensed
**PolyForm Noncommercial 1.0.0**. Upstream's `workbench/` states it was ported
from `video-talkcraft/workbench`.

## Decision

1. **We are an independent downstream, not a contributor and not a fork owner.**
   We do not open PRs upstream and do not track its roadmap. We pin its SHA,
   ingest from the checkout, and publish under our own brand.
2. **Every ingested row is traceable.** `source_repo.head_sha` pins the exact
   revision; `source_file.sha256` records the exact bytes; `source_commit` records
   the commit. `ingest_run` records which SHA produced which build.
3. **The upstream checkout is read-only input.** No edits to
   `upstream/video-shotcraft/`. Anything we want to change upstream — the
   broken `generatedAt`/`revision` fields, the `library.json` ↔ `demos/` key
   drift, the hand-maintained 214-entry style index — is fixed **downstream** in
   our ingest, or filed upstream. It never becomes a silent local patch.
4. **Apache-2.0 obligations are honoured in our own distribution**: keep the
   copyright notice and LICENSE when redistributing the core. We do not imply
   endorsement by the upstream author.

## Rationale

- Apache-2.0 permits independent redistribution, so we do not need the author's
  consent to build on it — and he has no commercial licence to grant us anyway.
  A fork that competes on localisation and service does not need his roadmap.
- Pinning the SHA is what makes our index reproducible. Without it, "157 cards"
  is a claim that quietly changes.
- Keeping upstream pristine means our diff to it is always empty, so
  "what did we change?" has a trivially correct answer and upstream sync is a
  re-pin rather than a merge.

## Consequences

- We inherit upstream's data quality problems instead of fixing them in place.
  This is the cost, and it is why `doctor.py` exists: the defects are ours to
  detect (see ADR 0006).
- The `workbench/` lineage is a live legal question. `video-talkcraft` is
  PolyForm Noncommercial and upstream's workbench was ported from it. PolyForm
  Noncommercial permits use and modification for noncommercial purposes and
  requires a licence for "use or distribution of the Software for commercial
  purposes". A derived workbench inside an Apache-2.0 repository does not
  launder the restriction. **Consequence: `workbench/` must not ship in any
  commercial offering until this is resolved** — either by relicensing with
  permission, or by replacing it. This is tracked in `license_registry`
  (`video-talkcraft`, `blocking = 1`) and it is the highest-priority legal item
  in the product, ahead of any feature work.
- Same reasoning applies to the 6 audio files marked 无法反查 in
  `assets/audio/ATTRIBUTION.md`: they cannot ship in a paid delivery.

## Alternatives rejected

- **Contribute fixes upstream and wait.** Rejected as the primary path: it couples
  our index to someone else's release cadence, and the defects that matter most to
  us (style-key identity) are ones upstream has no reason to prioritise.
- **Fork and own the roadmap, publish changes.** Rejected: a visible fork that
  competes with the original, on a 10k-star project, buys nothing here. The
  defensible product is the part that is *not* in the repo.
- **Scrape the live site instead of cloning.** Rejected: it would make our index
  depend on an HTTP surface, and it loses the `.tsx` sources that carry the
  easing-curve and motion-parameter extraction.