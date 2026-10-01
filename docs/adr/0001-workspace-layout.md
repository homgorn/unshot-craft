# ADR-0001 — Monorepo with a pinned, read-only upstream

**Status:** accepted · **Date:** 2026-10-01

## Context

We are forking a fast-moving 10.1k-star repository (157 cards and growing, 101
commits, media assets not in git) to localise its site, index its content and
build products on top of it.

## Decision

One git repository, `shotcraft/`, holding our work. Upstream is a clone inside
it at `upstream/video-shotcraft/`, **git-ignored and never edited**.

```
shotcraft/
├── upstream/video-shotcraft/   read-only clone, pinned SHA, ignored by git
├── platform/                   ingest, db, wiki generator, CLI, mirrorer
├── wiki/                       generated, committed
├── site/                       our fork of the gallery site
├── docs/                       adr, architecture, research, monetization
└── specs/                      SDD: vision, feature list, specs
```

## Rationale

**An editable vendor copy is a liability.** If we patched upstream files in
place, every upstream release becomes a merge conflict with unclear provenance,
and nobody can later answer "did we change their tuning, or only their site?".
Read-only makes that question unanswerable-by-construction.

**A pin beats a submodule here.** The upstream repo's media lives in a GitHub
release, not in git, and its `workbench/demosrc` is a symlink that does not
resolve on Windows. A submodule would inherit both problems. A plain clone plus
a recorded SHA in `source_repo.head_sha` gives the same reproducibility with
none of the tooling.

**`platform/db/` and `wiki/` are committed.** They are deliverables: a reviewer
should be able to read the index without running Python, and diff it when
upstream moves. The generator ships alongside, so "why does this row say that" is
always answerable.

## Conventions

- One commit per feature, referencing the `specs/feature-list.json` id.
- Generated artefacts are committed in the same commit as the generator change
  that produced them, so a diff never shows generated output without its cause.
- Upstream bumps are their own commit: re-run ingest, regenerate the wiki,
  review the diff of `wiki/index.json` stats, and record the new SHA.
- Nothing under `upstream/` is ever committed.

## Consequences

**Good**

- Upstream updates are a scripted, reviewable operation.
- "What is ours vs theirs" is answerable by path.
- The repo stays small: the 44 MB upstream clone and the mp4 release stay out of
  git history.

**Bad**

- No `git pull` for upstream content; there is a re-run step.
- The 44 MB clone plus ~214 mp4 previews must exist locally for full work. The
  mirrorer verifies this and exits non-zero if incomplete.
- Two `git` repos in one workspace means `git status` in the wrong directory
  produces confusing output. Mitigated by `AGENTS.md`.