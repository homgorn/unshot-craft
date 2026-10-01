# F070 — Cinematic catalog ingest

- Status: specified, **not implemented** (`passes: false`)
- Ledger entry: `specs/feature-list.json` → `F070`
- ADR: `docs/adr/0007-cinematic-catalog-layer.md`
- Ingest: `platform/ingest/catalog.py`
- Source: `data/cinematic/` (authored, committed)

## Status update, 2026-10-01

**Implemented and verified at full scale, with one number that must be read twice:**

| | scoped | actual |
|---|---|---|
| techniques | 150 | **150** (7 categories) |
| matrix cells listed | 1050 | **1050** |
| cells with a parameter | 933 | **791** (113 of 150 per tool) |
| cells actually tested | — | **0** |
| cells `null` | 117 | **259** (37 source rows are `TODO`) |
| declared motion pairings | — | **233** across 142 / 150 techniques |

The architecture is the one specified below and nothing in it changed. What changed
is the corpus: it is **imported from a separate MIT-licensed project**
(`cinematique`) by `platform/catalog/import_cinematique.py` rather than authored
here, and the honest scale is the full 150.

**The `0` is the point of the whole exercise.** The source matrix has a
`FILLED`/`TODO` status column and *no verification column* — their pipeline wrote
parameters, and nothing recorded a run against a model version. 791 parameters
exist and not one has been tested. The importer therefore forces `tested: no` on
every imported cell, `doctor.py` asserts `tested == 0` as an equality rather than
counting it, and `query.py optimize-all` prints `READY — tested` as an empty
group. A catalog that claimed 791 verified tool parameters would look more
valuable and be worth less than one that admits it has none.

Verification: `python platform/catalog/selftest.py` → 31/31.

## What this is

The shot-card corpus answers *how a shot moves*. It cannot answer *what to shoot*.
A `dolly-shot` card knows the easing, the frame window and the spring config; it
has no opinion on focal length, key direction or colour science, because
upstream never needed one — they render design-system demos, not films.

The cinematic catalog answers the second question: techniques with a production-ready
prompt template, a rationale, a set of common mistakes, film citations, a reference
image, and a cross-tool parameter matrix covering Midjourney v6.1, Runway Gen-3,
Google Veo 2, Kling 1.5, Luma Dream Machine, Pika 1.5 and Sora.

This feature ingests it into `shotcraft.db` as schema section 10, so the join we
actually want becomes a `JOIN`:

```sql
-- which motion cards can realize a rim-lit three-quarter, and with what params?
SELECT c.name, c.energy_level, m.raw
FROM cinematic_technique t
JOIN technique_tool_param p ON p.technique_id = t.id AND p.tool_id = :kling
JOIN card_style_tag st      ON st.style_id = t.related_style_id
JOIN shot_card c            ON c.id = st.card_id
WHERE t.slug = 'kicker-light';
```

## The one design rule

> **The prompt is verbatim source with a slot in it. Never expand `[Subject]`.**

`prompt_template` arrives as authored prose containing the literal token
`[Subject]`. That token is the same class of thing as `copy.slots[].id` in F050:
a promise that a human fills it. Ingest stores the string exactly as authored.
The compiler never substitutes, reorders, "improves" or wraps it.

Why this is hard rather than stylistic: an expanded prompt reads exactly like an
authored one, and an agent handed it will paste it to a client as though the
studio wrote it. Same failure mode F050 documents, same slot-shaped answer.

## What is actually derived

| field | source | notes |
|---|---|---|
| `technique.name` | `data/cinematic/<slug>.md` frontmatter `slug` | the join key, kebab-case, ASCII |
| `technique.title` | frontmatter `title` | |
| `technique.category` | frontmatter `category` | 7 values; see controlled vocabulary below |
| `technique.prompt_text` | body, verbatim | `[Subject]` **intact** |
| `technique.prompt_slot` | literal `'[Subject]'` | recorded so a linter can assert it survives |
| `technique.lede_text` | body `## Lede` | verbatim |
| `technique.section_*` | `## When to use` / `## Directing the AI` / `## Common mistakes` | verbatim |
| `technique.citation_url` | `## Sources` links | one row each |
| `technique.media_url` | frontmatter `image` | |
| `technique.video_url` | frontmatter `video` | nullable — none have one yet |
| `technique.source_sha256` | computed over the authored file | provenance to the byte, as everywhere else |
| `technique_tool_param.params` | `## Cross-tool` table, per tool | **nullable** — see below |
| `technique_tool_param.full_prompt` | same table | nullable, same reason |
| `technique_related.slug` | `## Related` links | resolved against `shot_card.name` where it matches |

## The honest gap, which matters

**The cross-tool matrix is sparse by construction, and the empty cells are not
defaults.**

| | count |
|---|---|
| matrix cells listed | 1050 |
| cells carrying a parameter | 791 |
| cells actually tested | **0** |
| cells `null` | 259 |

The unfilled cells are `NULL`, and `platform/catalog/selftest.py` counts them and
prints the number. They are **not** filled with a plausible default, for the same
reason `render.duration_frames` is `null` for 5 upstream technique cards: a tool
parameter we have not tested is an untested claim, and a plausible string in that
cell is a claim we cannot defend to a client.

**And the same rule applies to the 791 cells that *are* filled.** They were written
by the source project's pipeline, which records no run against a model version, so
they land as `tested: no` too. `platform/catalog/selftest.py` asserts
`tested == 0` and `tested_at IS NULL` everywhere, and
`platform/catalog/import_cinematique.py` refuses to write any other value.

A second, sharper version of the rule applies to **citations**: the source corpus
lists its sources as `Title — Publisher` with no link, so all 150 citations are
stored with `url IS NULL`. `technique_citation.url` was `NOT NULL` and is now
nullable, because a fabricated URL beside a real title would be worse than a
missing citation — a reviewer follows it, finds nothing, and stops trusting every
other citation in the row.

The one parameter present on every MJ row is `--ar 16:9 --v 6.1 --style raw
--cw 50`, because that is a mechanical transform of the base prompt, not a
judgement.

## Category vocabulary is controlled, not free text

Seven categories, `category_key` + `category_label_en`:

```
camera-work   lighting   composition   editing
narrative     visual-style   genres
```

A technique whose `category` is not in that list **fails the ingest** rather than
being bucketed into `other`. Upstream does the same thing via
`platform/ingest/roles.py`; a controlled vocabulary is what makes
`query.py technique --category lighting` a filter rather than a guess.

## Why `data/cinematic/` is source and `upstream/` is not

`upstream/` is read-only and git-ignored because it is someone else's repo under a
pinned SHA. The catalog is ours — curated, owned, versioned by us — so it is
committed as source. That is ADR 0007's only structural decision; everything else
follows from the existing rules.

Ingest must therefore treat the two inputs differently and stay green when one is
absent: **no `upstream/` clone → catalog tables still build; no `data/cinematic/`
→ upstream tables still build.** `run.py` reports which corpus it ingested and
`doctor.py` treats a missing corpus as a WARN, not a FAIL, until both are
required.

## Verification

```powershell
python platform/ingest/run.py
python platform/query.py technique --category lighting
python platform/query.py optimize kicker-light --tool kling
python platform/doctor.py            # catalog.* family
```

`platform/catalog/selftest.py` fails if a technique lacks a prompt, if any prompt
lost its `[Subject]` slot, if a category is outside the vocabulary, if a
`technique_motion` row points at a style that does not exist, if `full_prompt` is
non-NULL where `params` is NULL, if a `tested=1` cell has no `tested_at`, or if a
stored `params` still carries markdown fences. A missing corpus is a WARN and the
run still passes, because F070 requires either corpus to build alone.

## What is deliberately not here

- **No prose generation.** The catalog is already prose. F050's problem does not
  apply.
- **No `[Subject]` expansion.** See the rule above.
- **No invented tool parameters.** 259 cells stay `NULL`, and **all 791** filled
  cells are marked `tested: no` — including the ones the source project wrote,
  because that project recorded no run either.
- **No invented techniques.** The 150 are real, with film citations. They are
  imported rather than authored here, which is a statement about provenance, not
  about quality: each file carries `upstream_sha256`, so any row traces to the
  exact byte it came from, and editing one is a divergence from Cinematique rather
  than a local decision.
- **No invented citation URLs.** 150 citations, all `url IS NULL`, for the reason
  in the matrix section above.
- **Reference videos are mirrored, MP4s are not rendered.** 41 techniques have a
  reference `video_url` and the files are committed under `data/cinematic/media/`
  (65 MB). What we do *not* do is render our own: F060 stays blocked on the Remotion
  commercial licence, and no render in this repo is claimed to exist.
- **No Remotion integration.** The catalog knows nothing about easing. It becomes
  renderable only when a shot card is paired with it — which is F073.
