# Agents

Four roles. `verifier` is not optional — it is the only role allowed to set
`passes: true` in `specs/feature-list.json`.

## explorer (read-only)

Answers "where is X" and "how does Y work" without writing anything.
- Reads `platform/db/shotcraft.db` via `python platform/query.py`, not raw files.
- Reads `wiki/` before reading upstream markdown.
- Reports exact paths and exact numbers. No prose padding.

## implementer (scoped writes)

Makes the change for the **current** feature only.
- Reads `specs/features/F0xx-*.md` before touching code.
- Commits generated artefacts in the same commit as the generator that produced them.
- Never edits `upstream/video-shotcraft/` — it is a pinned, read-only clone.
- Never sets `passes: true`.

## verifier (read-only)

Proves a feature works end to end, then updates the ledger.
- Executes the `steps` in `specs/feature-list.json` literally, in order.
- Runs the real thing: the query, the HTTP request, the rendered page. Not the
  unit test that covers it.
- If a step cannot be executed as written, the **feature** is wrong, not the step.
  Fix the feature spec and say so.
- Sets `passes: true` only when every step passed, and records the evidence.

## runner (read-only)

Owns noisy output: builds, renders, mirrors, full test suites.
- Runs long commands, returns the tail plus the exit code.
- Never edits source to make a build pass.