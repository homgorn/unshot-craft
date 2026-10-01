# ADR-0003 — The LLM wiki is generated, never hand-written

**Status:** accepted · **Date:** 2026-10-01

## Context

Upstream ships a small `gallery/llms.txt` (a link list produced by
`build-seo.py`). We want a wiki that an agent can actually *use*: the shot cards,
the parameters, the pitfalls, the motion grammar, the methodology, and the
licensing constraints.

The corpus moves. Card count went 104 → 152 → 157 in two release waves, and the
author adds ~50 cards per batch. A hand-written wiki is stale within two weeks,
and nobody notices until an agent confidently cites a card that no longer exists.

## Decision

`platform/wiki/build_wiki.py` generates every artefact under `wiki/` from
`platform/db/shotcraft.db`. Hand-editing generated output is a bug.

## Output contract

| file | consumer | contract |
|---|---|---|
| `wiki/index.json` | site, SaaS, scripts | one object: stats, categories, locales, licenses, opportunities, all 157 cards |
| `wiki/llms.txt` | LLM crawlers | `llms.txt` convention: one-line purpose, then links |
| `wiki/llms-full.txt` | RAG ingestion | the whole corpus in one file (~620 KB) |
| `wiki/cards/<slug>.md` + `.json` | humans, agents | one page per card: identity, variants, parameters, pitfalls |
| `wiki/domains/*.md` | humans, agents | 9 domain documents |
| `wiki/api/openapi.json` | future HTTP API | read-only contract |
| `platform/db/shotcraft.db` | agents | SQL + FTS5 |

## Design rules

1. **Slugs are the API.** An agent addressing `crash-zoom-punch` gets the card,
   its two demo components, its four parameters, its three pitfalls and its rule
   citations. That slug is already the join key across markdown, TSX, media and
   deep links upstream, so it needs no translation layer.
2. **Every claim carries its evidence.** Numbers in prose are generated from
   counts, never typed. If upstream adds a card, the sentence "157 cards" becomes
   "158 cards" on the next run.
3. **The wiki adds what upstream lacks, and says so.** The motion-grammar domain
   exists because those parameters exist only as TSX literals. The licensing
   domain exists because the constraints are scattered across three licence
   files and one README footnote.
4. **Deny by default on money and legal.** `domains/monetization.md` ends with an
   explicit "what we are not doing", because an LLM asked "how do I monetise this"
   will otherwise confidently suggest selling the Apache-2.0 core.
5. **`wiki/` is committed; the generator is committed.** A reviewer can rebuild
   and diff.

## Consequences

**Good**

- Cannot drift from upstream.
- Diffable: a card-count change shows up as a one-word diff.
- An agent gets a total, not a sample — the whole corpus fits in one file.

**Bad**

- Reviewing prose means reviewing a generator, which has a worse feedback loop
  than editing a document. Mitigated by keeping each domain's template readable.
- Generated text cannot be *nuanced* — the value-add sections (the "what we are
  not doing" lists) are the ones most likely to need editorial judgement. Kept as
  explicit constants in the generator so they are visible to a reviewer.

## Alternatives rejected

- **Hand-written wiki + a sync script.** Two sources of truth for the same facts.
- **Docs site (Docusaurus/MkDocs).** Better human reading experience, worse for
  agents: a build step, JS-routed pages, and no single-file ingestion target.
  `wiki/*.md` is plain markdown precisely so both humans and agents can read it.
- **Serve a live API only.** An agent with no network should still be able to
  answer "what is crash-zoom-punch". Files win.