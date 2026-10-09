# ADR-0008 — TypeSafe judgments are advisory, never gates

**Status:** accepted · **Date:** 2026-10-09

## Context

The `typesafe-ai` skill is installed project-local (`.agents/skills/`,
`skills-lock.json`). It offers cheap semantic judgments (Choice / Noul /
Score from System One models) for tasks this repo does with fragile code:
claim checking, translation QA, search rerank, skill routing, guardrails.
Full analysis: `docs/research/typesafe-ai.md`.

The temptation is to wire a judgment into a gate — e.g. "translation Score ≥
X or the build fails". That would break the property every gate in
`scripts\init.ps1` relies on: **a gate is a command that returns non-zero and
stops the pipeline, deterministically.** A probabilistic judgment sometimes
passes a defect and sometimes fails green work. Rule 9 of AGENTS.md already
records how a green suite can certify a broken page; a nondeterministic gate
makes that failure mode load-bearing.

## Decision

1. **TypeSafe output is an advisory signal.** It prepares ranked candidates,
   scores and flags for a human or the verifier. It never returns the exit
   code of a gate, never edits `shotcraft.db` / `wiki/` / `prompts/`, and
   never sets `passes`.
2. **Questions and thresholds live in one constants file** per integration,
   reviewed with eyes (upstream's own principle). Cookbook numbers are
   examples to calibrate against, not norms to copy.
3. **Secrets:** only the name `TYPESAFE_API_KEY` is committed (`.env.example`).
   Values live in `.env` (gitignored) or real environment variables, which win
   over the file per `platform/_env.py`.
4. **Data sent to the API is public-corpus only** (upstream Apache-2.0 text,
   MIT catalog, our generated pages) until a DPA review says otherwise. No
   credentials, no private user data in `state`.
5. **The installed copy is third-party** (`.agents/skills/typesafe-ai/`): never
   hand-edit it; updates replace the whole directory (`npx skills update`).
   Project adaptation lives in `docs/research/typesafe-ai.md`, not in the
   installed files.

## Consequences

**Good**

- We get a cheap semantic reviewer without weakening a single gate.
- Calibration is explicit: thresholds are constants with provenance, not vibes.

**Bad**

- Integrations cost API calls and need an account/key before they run.
- Every TypeSafe-assisted claim still needs a deterministic verifier
  (`docs_freshness.py` CLAIMS discipline applies).

## Alternatives rejected

- **TypeSafe as a gate.** Rejected: nondeterminism in, false confidence out.
- **Global install (`-g`).** Rejected: the skill is pinned per project in
  `skills-lock.json` so every clone resolves the same version.
- **Recording this in the DB/wiki.** Rejected: both are generated artifacts
  (AGENTS.md rules 2–3); a tool decision belongs in docs, not in the corpus.
