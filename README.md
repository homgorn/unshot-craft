# shotcraft

An index, a wiki and a site for **video-shotcraft** — an open-source Apache-2.0
agent skill (10.1k stars) that turns Claude Code or Codex into a motion-design
studio: 157 shot recipe cards, 218 tuned Remotion demos, 154 sound effects and a
validated 36.2-second promo template.

We build **beside** that project, under our own brand, with upstream pinned and
credited.

## What is here

| | |
|---|---|
| `platform/ingest/` | `upstream tree → SQLite`. 24 tables, 4 FTS5 indexes, zero dependencies |
| `platform/db/shotcraft.db` | the single source of truth: cards, styles, media, parameters, pitfalls, motion grammar, methodology, licences, research |
| `platform/wiki/build_wiki.py` | `DB → wiki/`. Deterministic; hand-editing is a bug |
| `wiki/` | generated LLM wiki: `llms.txt`, `llms-full.txt`, 157 card pages, 9 domain docs, OpenAPI contract |
| `platform/query.py` | agent CLI — cards, search in any language, params, pitfalls, rules, licences |
| `platform/mirror_site.py` | mirrors the live site **including the mp4 previews that are not in git** |
| `site/` | our i18n rebuild of the gallery (9 locales) — see ADR-0004 |
| `docs/` | architecture, 6 ADRs, monetization research |
| `specs/` | SDD: vision, `feature-list.json` (the work ledger) |
| `upstream/video-shotcraft/` | read-only clone, git-ignored, never edited |

## Quick start

```powershell
scripts\init.ps1        # clone upstream if needed, ingest, build the wiki
```

Then:

```powershell
$env:PYTHONIOENCODING = "utf-8"

python platform/query.py stats
python platform/query.py cards --energy high --max-frames 60
python platform/query.py card crash-zoom-punch
python platform/query.py search 弹簧          # works in zh, en and slugs
python platform/query.py rules
python platform/query.py licenses
```

## What we extract that upstream never exposes

| data | count |
|---|---|
| tuned parameters from `## 参数表` | 1,057 |
| pitfalls from `## 已知坑` (3 marked 命门) | 792 |
| easing/spring/timing extracted from `demos/**/*.tsx` | 1,607 |
| distinct bezier curves, ranked by usage | 50 |
| aesthetic rules parsed from `references/aesthetic-rules.md` | 27 |

The motion grammar exists only as literals inside the TSX. Nothing upstream
indexes it. That data is the most reusable thing in this repo.

## Read these first

1. [`docs/architecture/README.md`](docs/architecture/README.md) — how it all fits
2. [`specs/vision.md`](specs/vision.md) — what we are building and what we are not
3. [`wiki/index.md`](wiki/index.md) — the generated knowledge base
4. [`docs/monetization/brainstorm.md`](docs/monetization/brainstorm.md) — how this makes money
5. [`AGENTS.md`](AGENTS.md) — conventions and hard rules

## Two constraints that shape everything

- **The Apache-2.0 core is free to fork and resell.** Anything we sell must be an
  outcome, a service, or support.
- **Remotion requires a paid licence for companies**, and the sibling skill
  `video-talkcraft` is **PolyForm Noncommercial**. Both are hard boundaries.

See `docs/adr/0005-upstream-policy.md` and `wiki/domains/licensing.md`.

## Credits

Content, code and audio assets derive from
[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)
(Apache-2.0) and [Remotion](https://www.remotion.dev/). Audio is Mixkit Free
Licence. The upstream author is unaffiliated with us and does not endorse this
work.