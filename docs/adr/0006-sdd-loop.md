# ADR-0006 — SDD loop with a verifier-owned completion gate

**Status:** accepted · **Date:** 2026-10-01

## Context

This project will run across many sessions and many agents. The measured failure
modes of that setup are specific:

1. An agent runs out of context mid-feature and the next session starts with no
   record of what was in flight.
2. An agent sees existing work, declares victory, and ships at 60%.
3. An agent marks a feature `passes: true` because it wrote the code and the unit
   tests pass — never having opened the feature in a browser.

All three are structural, not motivational.

## Decision

Spec-driven development with three artifacts:

- `specs/vision.md` — what we are building and what we are explicitly not.
- `specs/feature-list.json` — the work ledger. Every feature is independently
  verifiable end to end by someone with no memory of the project.
- `specs/features/F0xx-*.md` — the spec for a feature, written *before* the code.

And two rules:

1. **Only the `verifier` sets `passes: true`.** Not the implementer, not the
   planner, not the user.
2. **A feature that cannot be verified end to end is not a feature.** If
   verification requires a human eyeballing a video, either build the machine
   gate that replaces that judgement or reclassify it as `quality`.

## Feature granularity

Test applied: *could a person who has never seen this project run the steps and
know it works?*

- "Library page renders in Russian with all 157 cards translated" — yes.
- "Auth module exists" — no.
- "Site is fast" — no. Rewrite as a measured threshold.

Categories: `functional`, `integration`, `quality`, `ops` — they need different
kinds of proof. An `ops` feature is proved by running the script; a `functional`
one by driving the UI.

## Roles

| role | job | writes |
|---|---|---|
| `explorer` | read-only mapping; answers "where is X" | no |
| `implementer` | makes the change for the current feature | scoped |
| `verifier` | proves the feature end to end, then sets `passes` | no |
| `runner` | owns noisy output (builds, renders, test suites) | no |

`verifier` is not optional. It is the entire mechanism.

## Consequences

**Good**

- A cold session reads `feature-list.json` and knows exactly where it stopped.
- `git revert` is a usable recovery tool, because the baseline commit is clean.
- "Done" is defined by evidence, not by the implementer's confidence.

**Bad**

- Slower per feature: verification is real work and sometimes finds that the
  feature is wrong.
- The feature list rots if it is not updated at the end of each session. That
  maintenance is itself an `ops` task, not an afterthought.

## Alternatives rejected

- **Free-form TODO.md.** Rejected by the measurement: markdown invites models to
  rewrite and truncate it. JSON does not.
- **Issue tracker as the ledger.** The tracker is the right place for *shared*
  work; this work is single-repo and agent-driven, so a tracked JSON file is one
  fewer network dependency and one fewer auth failure mode. Revisit if the team
  grows.