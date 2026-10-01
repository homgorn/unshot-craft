-- ============================================================================
-- shotcraft.db — schema v1
--
-- Single source of truth for every index we serve: the LLM wiki, the localized
-- site, the micro-SaaS, and the competitive/monetization research.
--
-- Design rules:
--   * `name` (card slug) and `key` (style slug) are the join keys of the whole
--     upstream repo. They are the only natural keys; everything else is a FK.
--   * Every table that mirrors an upstream artifact carries `source_file_id`,
--     so any row can be traced back to a file + sha256 + upstream commit.
--   * Prose that upstream keeps as free text (energy, duration) is stored twice:
--     verbatim in a `*_text` column AND normalized into a lookup row. Never
--     throw away the original — the parenthetical rationale is the signal.
--   * Translations are rows, not columns. 9 locales x 371 strings does not
--     belong in the card table.
-- ============================================================================

PRAGMA journal_mode = WAL;
PRAGMA foreign_keys = ON;

-- ---------------------------------------------------------------------------
-- 0. Provenance
-- ---------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS source_repo (
  id            INTEGER PRIMARY KEY,
  slug          TEXT NOT NULL UNIQUE,      -- 'video-shotcraft'
  url           TEXT NOT NULL,
  license       TEXT,                      -- 'Apache-2.0'
  owner         TEXT,
  local_path    TEXT,                      -- 'upstream/video-shotcraft'
  head_sha      TEXT,
  head_date     TEXT,
  stars         INTEGER,
  forks         INTEGER,
  description   TEXT,
  cloned_at     TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS source_commit (
  id            INTEGER PRIMARY KEY,
  repo_id       INTEGER NOT NULL REFERENCES source_repo(id) ON DELETE CASCADE,
  sha           TEXT NOT NULL,
  committed_at  TEXT,
  subject       TEXT,
  author        TEXT,
  UNIQUE(repo_id, sha)
);

-- role is a controlled vocabulary, see platform/ingest/roles.py
CREATE TABLE IF NOT EXISTS source_file (
  id            INTEGER PRIMARY KEY,
  repo_id       INTEGER NOT NULL REFERENCES source_repo(id) ON DELETE CASCADE,
  path          TEXT NOT NULL,             -- repo-relative, forward slashes
  sha256        TEXT,
  bytes         INTEGER,
  role          TEXT,                      -- card|sequence|reference|demo|component|asset|site|config|doc|ci|license|other
  lang          TEXT,
  UNIQUE(repo_id, path)
);

CREATE TABLE IF NOT EXISTS ingest_run (
  id              INTEGER PRIMARY KEY,
  repo_id         INTEGER NOT NULL REFERENCES source_repo(id) ON DELETE CASCADE,
  started_at      TEXT NOT NULL DEFAULT (datetime('now')),
  finished_at     TEXT,
  upstream_sha    TEXT,
  files_seen      INTEGER DEFAULT 0,
  cards_seen      INTEGER DEFAULT 0,
  styles_seen     INTEGER DEFAULT 0,
  params_extracted INTEGER DEFAULT 0,
  locale_rows     INTEGER DEFAULT 0,
  warnings        TEXT,                    -- JSON array
  status          TEXT DEFAULT 'running'   -- running|ok|failed
);

-- ---------------------------------------------------------------------------
-- 1. Taxonomy
-- ---------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS category (
  id            INTEGER PRIMARY KEY,
  key           TEXT NOT NULL UNIQUE,      -- 'ui-entrance'
  parent_key    TEXT REFERENCES category(key),
  order_idx     INTEGER,
  label_en      TEXT,
  label_zh      TEXT,
  label_ru      TEXT,
  card_count    INTEGER DEFAULT 0
);

-- The energy ladder. `rank` is the sort key for the energy arc; `is_arc_text`
-- marks values that describe an arc rather than a level (低开缓升, 低→瞬时中→低).
CREATE TABLE IF NOT EXISTS energy_level (
  id            INTEGER PRIMARY KEY,
  key           TEXT NOT NULL UNIQUE,      -- 'mid-high'
  rank          INTEGER,                   -- 1..8, NULL for n/a
  label_zh      TEXT NOT NULL,             -- '中高'
  label_en      TEXT NOT NULL,             -- 'mid-high'
  label_ru      TEXT,
  is_arc_text   INTEGER NOT NULL DEFAULT 0,
  is_na         INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS sequence_stage (
  id            INTEGER PRIMARY KEY,
  ordinal       TEXT NOT NULL UNIQUE,      -- '①' .. '④'
  label_zh      TEXT,
  label_en      TEXT,
  duration_pct  TEXT,                      -- '8–12%'
  energy        TEXT,
  duty          TEXT
);

-- ---------------------------------------------------------------------------
-- 2. Shot recipe cards  (upstream: references/shots/<category>/<name>.md)
-- ---------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS shot_card (
  id              INTEGER PRIMARY KEY,
  name            TEXT NOT NULL UNIQUE,    -- kebab slug == filename stem
  category_id     INTEGER NOT NULL REFERENCES category(id),
  summary_zh      TEXT,                    -- frontmatter 一句话
  use_zh          TEXT,                    -- frontmatter 适用
  duration_text   TEXT,                    -- frontmatter 时长, verbatim
  duration_frames INTEGER,                 -- parsed, NULL when 时长 is n/a
  energy_level_id INTEGER REFERENCES energy_level(id),
  energy_text     TEXT,                    -- frontmatter 能量, verbatim
  energy_rationale TEXT,                   -- the parenthesised part only
  intention_zh    TEXT,                    -- '## 意图' body, collapsed
  added_at        TEXT,
  updated_at      TEXT,
  source_file_id  INTEGER REFERENCES source_file(id),
  source_path     TEXT,
  source_url      TEXT,                    -- './source/<name>.md' on the live site
  UNIQUE(name)
);
CREATE INDEX IF NOT EXISTS idx_card_category ON shot_card(category_id);
CREATE INDEX IF NOT EXISTS idx_card_energy   ON shot_card(energy_level_id);
CREATE INDEX IF NOT EXISTS idx_card_frames   ON shot_card(duration_frames);

-- Cross-category relation. Upstream key is 标签; values are always category keys.
CREATE TABLE IF NOT EXISTS shot_card_tag (
  card_id      INTEGER NOT NULL REFERENCES shot_card(id) ON DELETE CASCADE,
  category_id  INTEGER NOT NULL REFERENCES category(id) ON DELETE CASCADE,
  PRIMARY KEY (card_id, category_id)
);

-- One row per card body section. Section order matters, so ordinal is explicit.
CREATE TABLE IF NOT EXISTS card_section (
  id          INTEGER PRIMARY KEY,
  card_id     INTEGER NOT NULL REFERENCES shot_card(id) ON DELETE CASCADE,
  ordinal     INTEGER NOT NULL,
  heading     TEXT NOT NULL,
  kind        TEXT NOT NULL,              -- intention|motion|phases|variants|params|sound|pitfalls|impl|other
  body        TEXT,
  UNIQUE(card_id, ordinal)
);
CREATE INDEX IF NOT EXISTS idx_section_kind ON card_section(kind);

-- `## 参数表` — the highest-value un-mined structured field upstream.
-- Columns: | 参数 | 典型值 | 调节手感 |
CREATE TABLE IF NOT EXISTS card_param (
  id           INTEGER PRIMARY KEY,
  card_id      INTEGER NOT NULL REFERENCES shot_card(id) ON DELETE CASCADE,
  ordinal      INTEGER NOT NULL,
  variant_letter TEXT,                     -- 'A'/'B' on multi-variant cards
  param_key    TEXT NOT NULL,
  typical_value TEXT,
  feel_note    TEXT                        -- 调节手感: pass/fail thresholds
);
CREATE INDEX IF NOT EXISTS idx_param_card ON card_param(card_id);

-- Multi-variant cards (`## N式选型`). Join table card -> style.
CREATE TABLE IF NOT EXISTS card_variant (
  id             INTEGER PRIMARY KEY,
  card_id        INTEGER NOT NULL REFERENCES shot_card(id) ON DELETE CASCADE,
  style_id       INTEGER NOT NULL REFERENCES style(id) ON DELETE CASCADE,
  letter         TEXT,                     -- 'A'/'B'/'D' — letters skip upstream
  ordinal        INTEGER,
  label_zh       TEXT,
  description_zh TEXT,
  UNIQUE(card_id, style_id)
);

-- Pitfalls, split out of 已知坑 so they can be queried as a corpus.
CREATE TABLE IF NOT EXISTS card_pitfall (
  id          INTEGER PRIMARY KEY,
  card_id     INTEGER NOT NULL REFERENCES shot_card(id) ON DELETE CASCADE,
  ordinal     INTEGER NOT NULL,
  text        TEXT NOT NULL,
  is_critical INTEGER NOT NULL DEFAULT 0,  -- 命门 marker
  rule_refs   TEXT,                        -- 'R1,Q8' style citations
  UNIQUE(card_id, ordinal)
);

-- ---------------------------------------------------------------------------
-- 3. Styles / demos  (upstream: demos/<category>/<name>/<PascalCase>.tsx)
-- ---------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS style (
  id                INTEGER PRIMARY KEY,
  key               TEXT NOT NULL UNIQUE,  -- kebab-case of the tsx basename
  card_id           INTEGER REFERENCES shot_card(id) ON DELETE SET NULL,
  category_id       INTEGER REFERENCES category(id),
  demo_path         TEXT,                  -- repo-relative path to the .tsx
  component_name    TEXT,                  -- `export const X: React.FC =`
  duration_frames   INTEGER,
  duration_source   TEXT,                  -- _DURATION|_DUR|card-md|library.json|const-scan|default-150
  family            TEXT,                  -- A=normalized-t Motion lab | B=frame-driven template
  uses_normalized_t INTEGER NOT NULL DEFAULT 0,
  design_stage      INTEGER,               -- 480x270 design space (family A)
  registered        INTEGER NOT NULL DEFAULT 1,  -- in workbench demo-index
  gallery_style_key TEXT,                        -- library.json key, when it differs from `key`
  skip_reason       TEXT
);
CREATE INDEX IF NOT EXISTS idx_style_card ON style(card_id);

-- Style keys that gallery/api/library.json advertises but that have no matching
-- demo component. Upstream is lossy here (e.g. crash-zoom-punch advertises one key
-- while demos/camera/crash-zoom-punch/ holds two components). We keep the
-- divergence visible instead of silently dropping it.
CREATE TABLE IF NOT EXISTS gallery_style (
  id             INTEGER PRIMARY KEY,
  key            TEXT NOT NULL UNIQUE,
  card_id        INTEGER REFERENCES shot_card(id) ON DELETE CASCADE,
  label          TEXT,
  description_zh TEXT,
  media_url      TEXT,
  media_type     TEXT,
  note           TEXT DEFAULT 'advertised in library.json but no matching demos/<cat>/<card>/ component'
);

CREATE TABLE IF NOT EXISTS style_media (
  id           INTEGER PRIMARY KEY,
  style_id     INTEGER NOT NULL REFERENCES style(id) ON DELETE CASCADE,
  kind         TEXT NOT NULL,              -- preview|poster
  url          TEXT,
  media_type   TEXT,                       -- mp4|gif
  remote_url   TEXT,
  local_path   TEXT,
  bytes        INTEGER,
  present      INTEGER NOT NULL DEFAULT 0
);
CREATE INDEX IF NOT EXISTS idx_media_style ON style_media(style_id);

-- ---------------------------------------------------------------------------
-- 4. Extracted motion parameters  (the thing no upstream artifact exposes)
-- ---------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS motion_param (
  id          INTEGER PRIMARY KEY,
  style_id    INTEGER NOT NULL REFERENCES style(id) ON DELETE CASCADE,
  kind        TEXT NOT NULL,   -- bezier|easing_fn|spring|interpolate|segment|exp_decay|sin|motion_blur|constant
  name        TEXT,            -- variable / constant identifier
  args_json   TEXT,            -- normalized arguments
  detail      TEXT,            -- human readable
  line_no     INTEGER,
  raw         TEXT             -- the source line, for audit
);
CREATE INDEX IF NOT EXISTS idx_param_style ON motion_param(style_id);
CREATE INDEX IF NOT EXISTS idx_param_kind  ON motion_param(kind);

-- The house easing curves actually used upstream. Normalized so we can rank
-- "which curves does this repo prefer" — a real, sellable insight.
CREATE TABLE IF NOT EXISTS easing_curve (
  id           INTEGER PRIMARY KEY,
  kind         TEXT NOT NULL,             -- bezier|standard|composed|spring
  spec         TEXT NOT NULL UNIQUE,      -- 'bezier(0.3,0,0.2,1)'
  x1 REAL, y1 REAL, x2 REAL, y2 REAL,
  base         TEXT,                       -- quad|cubic|quint|expo|back|elastic|...
  overshoot    INTEGER NOT NULL DEFAULT 0, -- y1 > 1
  usage_count  INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS style_easing (
  style_id     INTEGER NOT NULL REFERENCES style(id) ON DELETE CASCADE,
  easing_id    INTEGER NOT NULL REFERENCES easing_curve(id) ON DELETE CASCADE,
  occurrences  INTEGER NOT NULL DEFAULT 1,
  PRIMARY KEY (style_id, easing_id)
);

-- ---------------------------------------------------------------------------
-- 5. Methodology corpus  (references/*.md, sequences/, rule families)
-- ---------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS sequence_template (
  id             INTEGER PRIMARY KEY,
  name           TEXT NOT NULL UNIQUE,
  summary_zh     TEXT,
  use_zh         TEXT,
  stage_count    TEXT,
  source_file_id INTEGER REFERENCES source_file(id)
);

CREATE TABLE IF NOT EXISTS sequence_stage_candidate (
  id          INTEGER PRIMARY KEY,
  template_id INTEGER NOT NULL REFERENCES sequence_template(id) ON DELETE CASCADE,
  ordinal     INTEGER NOT NULL,
  stage_id    INTEGER REFERENCES sequence_stage(id),
  card_name   TEXT,
  UNIQUE(template_id, ordinal)
);

-- aesthetic-rules.md rule families: R rhythm, Q quality/camera, S sound,
-- C copy, P process. IDs are append-only upstream and must never be renumbered.
CREATE TABLE IF NOT EXISTS rule (
  id             INTEGER PRIMARY KEY,
  family         TEXT NOT NULL,           -- R|Q|S|C|P
  rule_id        TEXT NOT NULL,           -- 'R1'
  title          TEXT,
  body           TEXT,
  check_question TEXT,
  source_file_id INTEGER REFERENCES source_file(id),
  UNIQUE(family, rule_id)
);

CREATE TABLE IF NOT EXISTS method_doc (
  id             INTEGER PRIMARY KEY,
  slug           TEXT NOT NULL UNIQUE,    -- 'pipeline', 'aesthetic-rules', ...
  title          TEXT,
  purpose        TEXT,
  headings_json  TEXT,
  bytes          INTEGER,
  source_path    TEXT,
  source_file_id INTEGER REFERENCES source_file(id)
);

-- ---------------------------------------------------------------------------
-- 6. Assets & licensing audit
-- ---------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS audio_asset (
  id             INTEGER PRIMARY KEY,
  kind           TEXT NOT NULL,           -- sfx|bgm
  path           TEXT NOT NULL UNIQUE,
  category       TEXT,                    -- 16 sfx categories
  title          TEXT,
  source_url     TEXT,
  license        TEXT,
  traceable      INTEGER NOT NULL DEFAULT 1,   -- 0 == 无法反查, block commercial use
  commercial_ok  INTEGER NOT NULL DEFAULT 1,
  bytes          INTEGER,
  note           TEXT
);
CREATE INDEX IF NOT EXISTS idx_audio_kind ON audio_asset(kind, category);

CREATE TABLE IF NOT EXISTS license_registry (
  id            INTEGER PRIMARY KEY,
  subject       TEXT NOT NULL,            -- 'video-shotcraft core' | 'Remotion' | 'Mixkit SFX' | ...
  spdx          TEXT,
  url           TEXT,
  commercial_use TEXT,                    -- free|restricted|requires-license|unknown
  blocking      INTEGER NOT NULL DEFAULT 0,
  obligation    TEXT,
  evidence_path TEXT,
  UNIQUE(subject)
);

CREATE TABLE IF NOT EXISTS attribution_entry (
  id          INTEGER PRIMARY KEY,
  scope       TEXT NOT NULL,              -- 'shots-2026-08' | 'audio'
  subject     TEXT NOT NULL,
  source      TEXT,
  original_name TEXT,
  note        TEXT
);

-- ---------------------------------------------------------------------------
-- 7. Localization
-- ---------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS locale (
  id           INTEGER PRIMARY KEY,
  code         TEXT NOT NULL UNIQUE,      -- 'en','zh','ru','es','de','fr','pt','ko','ja'
  bcp47        TEXT NOT NULL,
  name_en      TEXT NOT NULL,
  native_name  TEXT NOT NULL,
  dir          TEXT NOT NULL DEFAULT 'ltr',
  html_lang    TEXT,
  is_source    INTEGER NOT NULL DEFAULT 0,
  font_stack   TEXT,
  status       TEXT NOT NULL DEFAULT 'pending',  -- source|partial|complete
  UNIQUE(code)
);

-- ns = ui | page | card | style | showcase | meta
CREATE TABLE IF NOT EXISTS translation (
  id           INTEGER PRIMARY KEY,
  locale_id    INTEGER NOT NULL REFERENCES locale(id) ON DELETE CASCADE,
  ns           TEXT NOT NULL,
  key          TEXT NOT NULL,
  text         TEXT,
  method       TEXT,                      -- human|machine|review|derived
  status       TEXT NOT NULL DEFAULT 'pending',  -- pending|translated|reviewed|stale
  source_sha   TEXT,
  updated_at   TEXT NOT NULL DEFAULT (datetime('now')),
  UNIQUE(locale_id, ns, key)
);
CREATE INDEX IF NOT EXISTS idx_tr_status ON translation(locale_id, status);

-- ---------------------------------------------------------------------------
-- 8. Research: competitive intel & monetization
-- ---------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS actor (
  id            INTEGER PRIMARY KEY,
  name          TEXT NOT NULL UNIQUE,
  kind          TEXT NOT NULL,            -- upstream-author|sibling-skill|competitor|channel|tool
  url           TEXT,
  repo          TEXT,
  stars         INTEGER,
  license       TEXT,
  positioning   TEXT,
  captured_at   TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS source_channel (
  id          INTEGER PRIMARY KEY,
  actor_id    INTEGER REFERENCES actor(id) ON DELETE SET NULL,
  name        TEXT NOT NULL,              -- 'Enterprise DNA','skills.sh','MoClaw blog'
  url         TEXT,
  kind        TEXT,                       -- newsletter|directory|blog|marketplace|social
  reach       TEXT,
  captured_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS opportunity (
  id            INTEGER PRIMARY KEY,
  key           TEXT NOT NULL UNIQUE,
  title         TEXT NOT NULL,
  thesis        TEXT,                     -- why it works, in one paragraph
  revenue_model TEXT,                     -- service|saas|marketplace|ads|license|training
  effort        TEXT,                     -- S|M|L
  time_to_first_revenue TEXT,
  evidence      TEXT,                     -- JSON: measurements backing the thesis
  depends_on    TEXT,                     -- JSON: feature ids
  status        TEXT NOT NULL DEFAULT 'idea'  -- idea|validated|building|shipped|rejected
);

CREATE TABLE IF NOT EXISTS decision_log (
  id         INTEGER PRIMARY KEY,
  decided_at TEXT NOT NULL DEFAULT (datetime('now')),
  area       TEXT NOT NULL,
  decision   TEXT NOT NULL,
  rationale  TEXT,
  adr        TEXT                         -- link to docs/adr/NNNN-*.md
);

-- ---------------------------------------------------------------------------
-- 9. FTS5 — full text across everything (this is what an agent queries)
-- ---------------------------------------------------------------------------

CREATE VIRTUAL TABLE IF NOT EXISTS card_fts USING fts5(
  name, summary_zh, use_zh, intention_zh, energy_text, duration_text,
  content='shot_card', content_rowid='id', tokenize='unicode61'
);
CREATE TRIGGER IF NOT EXISTS card_fts_ai AFTER INSERT ON shot_card BEGIN
  INSERT INTO card_fts(rowid, name, summary_zh, use_zh, intention_zh, energy_text, duration_text)
  VALUES (new.id, new.name, new.summary_zh, new.use_zh, new.intention_zh, new.energy_text, new.duration_text);
END;
CREATE TRIGGER IF NOT EXISTS card_fts_ad AFTER DELETE ON shot_card BEGIN
  INSERT INTO card_fts(card_fts, rowid, name, summary_zh, use_zh, intention_zh, energy_text, duration_text)
  VALUES ('delete', old.id, old.name, old.summary_zh, old.use_zh, old.intention_zh, old.energy_text, old.duration_text);
END;
CREATE TRIGGER IF NOT EXISTS card_fts_au AFTER UPDATE ON shot_card BEGIN
  INSERT INTO card_fts(card_fts, rowid, name, summary_zh, use_zh, intention_zh, energy_text, duration_text)
  VALUES ('delete', old.id, old.name, old.summary_zh, old.use_zh, old.intention_zh, old.energy_text, old.duration_text);
  INSERT INTO card_fts(rowid, name, summary_zh, use_zh, intention_zh, energy_text, duration_text)
  VALUES (new.id, new.name, new.summary_zh, new.use_zh, new.intention_zh, new.energy_text, new.duration_text);
END;

CREATE VIRTUAL TABLE IF NOT EXISTS style_fts USING fts5(
  key, name_zh, description_zh, content='', tokenize='unicode61'
);

CREATE VIRTUAL TABLE IF NOT EXISTS param_fts USING fts5(
  param_key, typical_value, feel_note, content='', tokenize='unicode61'
);

CREATE VIRTUAL TABLE IF NOT EXISTS doc_fts USING fts5(
  slug, title, body, content='', tokenize='unicode61'
);

CREATE VIRTUAL TABLE IF NOT EXISTS pitfall_fts USING fts5(
  text, content='', tokenize='unicode61'
);

-- ------------------------------------------------------------------
-- CJK search. `unicode61` treats a whole Chinese phrase as ONE token, so
-- MATCH '转场' can never hit '...转场...' inside a sentence. SQLite's trigram
-- tokenizer does substring matching for any script, so CJK queries go here.
-- Caveat: trigram requires a query of at least 3 characters.
-- ------------------------------------------------------------------
CREATE VIRTUAL TABLE IF NOT EXISTS card_fts_trgm USING fts5(
  name, summary_zh, use_zh, intention_zh, tokenize='trigram'
);

CREATE VIRTUAL TABLE IF NOT EXISTS pitfall_fts_trgm USING fts5(
  text, tokenize='trigram'
);

-- ------------------------------------------------------------------
-- Unified search surface.
--
-- Problems this solves:
--  * the cards are written in Chinese, so a latin FTS over the raw card text
--    matches nothing useful ("overshoot" -> 0 hits);
--  * `unicode61` makes a whole Chinese phrase one token, so MATCH '转场' can
--    never hit inside '...转场...';
--  * `trigram` fixes CJK but requires a query of at least 3 characters, so
--    2-character CJK words still need a LIKE fallback.
--
-- card_search therefore carries one searchable blob per card, pooled across
-- every locale plus parameters, pitfalls and style keys, and both tokenizers
-- index it. Short queries go through LIKE (see platform/query.py).
-- ------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS card_search (
  card_id     INTEGER PRIMARY KEY REFERENCES shot_card(id) ON DELETE CASCADE,
  slug        TEXT,
  text_all    TEXT,      -- every locale description + params + pitfalls + styles
  text_latin  TEXT       -- slugs, style keys, latin-only tokens
);

CREATE INDEX IF NOT EXISTS idx_search_slug ON card_search(slug);

CREATE VIRTUAL TABLE IF NOT EXISTS search_fts USING fts5(
  slug, text_all, tokenize='unicode61'
);

CREATE VIRTUAL TABLE IF NOT EXISTS search_fts_trgm USING fts5(
  slug, text_all, tokenize='trigram'
);