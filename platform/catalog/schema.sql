-- ============================================================================
-- Cinematic-technique catalog — schema section 10
--
-- Second corpus. Same DB, same design rules (see platform/ingest/schema.sql
-- preamble). Source: data/cinematic/ (authored, committed). See ADR 0007.
--
-- Why a separate file: platform/ingest/schema.sql is being edited for the
-- upstream corpus, and a 150-line append from a different workstream is a merge
-- conflict waiting to happen. run.py applies both files; the section number keeps
-- the two schemas ordered the same way.
--
-- ORDERING: this file must be applied AFTER platform/ingest/schema.sql. Two FKs
-- cross the corpus boundary on purpose -- `cinematic_technique.source_file_id`
-- points at `source_file` and `technique_motion.style_id` points at `style`,
-- because a catalog row must be traceable to its authored byte and a motion
-- pairing must point at a real style. Found by platform/catalog/validate_schema.py
-- on the first run, which is why it is written down.
--
-- Design rules repeated here because they bind harder on this corpus:
--   * `name` (technique slug) is the join key, exactly as for shot cards.
--   * `prompt_text` is verbatim with `[Subject]` intact. Never normalized.
--   * The cross-tool matrix is a join table, never a JSON column on the row.
--   * An absent value is NULL and is counted by doctor.py. Never a default.
-- ============================================================================

-- ---------------------------------------------------------------------------
-- 10.0 Catalog provenance
-- ---------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS catalog_repo (
  id            INTEGER PRIMARY KEY,
  slug          TEXT NOT NULL UNIQUE,      -- 'cinematique'
  url           TEXT NOT NULL,
  license       TEXT,                      -- source terms; see SECURITY.md upstream
  local_path    TEXT NOT NULL,             -- 'data/cinematic'
  head_sha      TEXT,                      -- sha256 of the concatenated tree
  description   TEXT,
  ingested_at   TEXT NOT NULL DEFAULT (datetime('now'))
);

-- ---------------------------------------------------------------------------
-- 10.1 Controlled vocabulary
-- ---------------------------------------------------------------------------

-- `role` style: a closed set, enforced at ingest, the same way
-- platform/ingest/roles.py handles the shot-card role. A technique whose
-- category is not here fails the ingest rather than landing in 'other'.
CREATE TABLE IF NOT EXISTS cinematic_category (
  id            INTEGER PRIMARY KEY,
  key           TEXT NOT NULL UNIQUE,      -- 'camera-work'
  label_en      TEXT NOT NULL,
  sort_order    INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS ai_tool (
  id            INTEGER PRIMARY KEY,
  key           TEXT NOT NULL UNIQUE,      -- 'mj61'
  label         TEXT NOT NULL,             -- 'Midjourney v6.1'
  param_style   TEXT,                      -- '--flag' | 'k=v | k=v'
  max_params_len INTEGER,                  -- 0 when untested/unbounded
  notes         TEXT
);

-- ---------------------------------------------------------------------------
-- 10.2 Techniques
-- ---------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS cinematic_technique (
  id                INTEGER PRIMARY KEY,
  name              TEXT NOT NULL UNIQUE,  -- the slug; the join key
  title             TEXT NOT NULL,
  category_id       INTEGER NOT NULL REFERENCES cinematic_category(id),
  level             TEXT,                  -- 'basic' | 'intermediate' | 'advanced'
  prompt_text       TEXT NOT NULL,         -- VERBATIM, [Subject] intact
  prompt_slot       TEXT NOT NULL DEFAULT '[Subject]',
  lede_text         TEXT,                  -- verbatim
  when_to_use_text  TEXT,                  -- verbatim
  directing_text    TEXT,                  -- verbatim
  image_url         TEXT,
  video_url         TEXT,                  -- 41 of 150 have one; NULL otherwise
  source_file_id    INTEGER REFERENCES source_file(id),
  ingested_at       TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_technique_cat ON cinematic_technique(category_id);

CREATE TABLE IF NOT EXISTS technique_section (
  id            INTEGER PRIMARY KEY,
  technique_id  INTEGER NOT NULL REFERENCES cinematic_technique(id) ON DELETE CASCADE,
  kind          TEXT NOT NULL,             -- 'common_mistake' | 'note'
  ord           INTEGER NOT NULL,
  text          TEXT NOT NULL,             -- verbatim
  is_critical   INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS technique_citation (
  id            INTEGER PRIMARY KEY,
  technique_id  INTEGER NOT NULL REFERENCES cinematic_technique(id) ON DELETE CASCADE,
  ord           INTEGER NOT NULL,
  title         TEXT NOT NULL,
  -- Nullable, deliberately. The source corpus lists its sources as
  -- `Title — Publisher` with no link, so every one of its citations has a real
  -- title and no URL. Storing a plausible URL next to a real title would be the
  -- most damaging thing this layer could do: a reviewer would follow it and find
  -- nothing, and every other citation in the row would stop being trusted. NULL
  -- means "we have the citation, we do not have the link"; it is never a guess.
  url           TEXT
);

-- Declared relation to the shot corpus. Populated only from an explicit
-- `styles:` list in the authored file — never inferred from a name match.
-- `kind` records what the relation asserts so a renderer knows how far to trust it.
CREATE TABLE IF NOT EXISTS technique_motion (
  technique_id  INTEGER NOT NULL REFERENCES cinematic_technique(id) ON DELETE CASCADE,
  style_id      INTEGER NOT NULL REFERENCES style(id) ON DELETE CASCADE,
  kind          TEXT NOT NULL DEFAULT 'declared',  -- 'declared' | 'curated'
  PRIMARY KEY (technique_id, style_id)
);

-- ---------------------------------------------------------------------------
-- 10.3 Cross-tool matrix
-- ---------------------------------------------------------------------------

-- One row per (technique, tool). Nullable columns are the honest state of an
-- untested cell, not a gap to fill with a default.
--
--   params      the tool's parameter string, e.g. '--ar 16:9 --v 6.1 --cw 50'
--   full_prompt prompt + params, composed; NULL when params is NULL
--   version_tag e.g. 'v2_mj61' — the model version the params were written for
--   tested      1 when a human ran it against that model version
--   tested_at   ISO-8601, NULL when tested = 0
CREATE TABLE IF NOT EXISTS technique_tool_param (
  technique_id  INTEGER NOT NULL REFERENCES cinematic_technique(id) ON DELETE CASCADE,
  tool_id       INTEGER NOT NULL REFERENCES ai_tool(id) ON DELETE CASCADE,
  params        TEXT,
  full_prompt   TEXT,
  version_tag   TEXT,
  tested        INTEGER NOT NULL DEFAULT 0,
  tested_at     TEXT,
  PRIMARY KEY (technique_id, tool_id)
);

CREATE INDEX IF NOT EXISTS idx_ttp_tool ON technique_tool_param(tool_id, tested);

-- The 7 tools are seeded here so an absent matrix row means "not researched",
-- which is different from "tool does not exist".
INSERT OR IGNORE INTO ai_tool (key, label, param_style) VALUES
  ('mj61',         'Midjourney v6.1',        '--flag'),
  ('runway_gen3',  'Runway Gen-3 Alpha',     'k=v'),
  ('veo2',         'Google Veo 2',           'k=v'),
  ('kling15',      'Kling 1.5',              'k=v'),
  ('luma',         'Luma Dream Machine',     'k=v'),
  ('pika15',       'Pika 1.5',               'k=v'),
  ('sora',         'OpenAI Sora',            'k=v');

INSERT OR IGNORE INTO cinematic_category (key, label_en, sort_order) VALUES
  ('camera-work',  'Camera Work',  1),
  ('lighting',     'Lighting',     2),
  ('composition',  'Composition',  3),
  ('editing',      'Editing',      4),
  ('narrative',    'Narrative',    5),
  -- Cinematique's source catalog keeps "Visual Effects & Promptable FX" as its
  -- own group alongside "Genres & Styles". Two rows rather than one squashed
  -- key: a controlled vocabulary that does not match the corpus is how
  -- `--category` stops being a filter.
  --
  -- There is deliberately no 'visual-style' key. An earlier draft had one, and it
  -- was always empty: the source corpus has no such group. A controlled
  -- vocabulary is a claim about what exists; an entry nothing can populate makes
  -- `--category visual-style` look broken rather than absent.
  ('visual-effects','Visual Effects & Promptable FX', 6),
  ('genres',       'Film Genres',  7);

-- ---------------------------------------------------------------------------
-- 10.4 FTS5 — catalog surface
-- ---------------------------------------------------------------------------

-- Same cascade as the main index: unicode61 cannot match inside a CJK phrase,
-- trigram cannot do 1-2 character queries. The catalog is English-only today,
-- but the rule is copied rather than re-derived, because the day someone adds a
-- zh technique the cascade has to already be right.
CREATE VIRTUAL TABLE IF NOT EXISTS technique_fts USING fts5(
  name, title, prompt_text, lede_text, when_to_use_text, directing_text,
  content='cinematic_technique',
  content_rowid='id',
  tokenize='unicode61'
);

CREATE TRIGGER IF NOT EXISTS technique_ai AFTER INSERT ON cinematic_technique BEGIN
  INSERT INTO technique_fts (rowid, name, title, prompt_text, lede_text,
                             when_to_use_text, directing_text)
  VALUES (new.id, new.name, new.title, new.prompt_text, new.lede_text,
          new.when_to_use_text, new.directing_text);
END;

CREATE TRIGGER IF NOT EXISTS technique_ad AFTER DELETE ON cinematic_technique BEGIN
  INSERT INTO technique_fts (technique_fts, rowid, name, title, prompt_text,
                             lede_text, when_to_use_text, directing_text)
  VALUES ('delete', old.id, old.name, old.title, old.prompt_text, old.lede_text,
          old.when_to_use_text, old.directing_text);
END;

CREATE TRIGGER IF NOT EXISTS technique_au AFTER UPDATE ON cinematic_technique BEGIN
  INSERT INTO technique_fts (technique_fts, rowid, name, title, prompt_text,
                             lede_text, when_to_use_text, directing_text)
  VALUES ('delete', old.id, old.name, old.title, old.prompt_text, old.lede_text,
          old.when_to_use_text, old.directing_text);
  INSERT INTO technique_fts (rowid, name, title, prompt_text, lede_text,
                             when_to_use_text, directing_text)
  VALUES (new.id, new.name, new.title, new.prompt_text, new.lede_text,
          new.when_to_use_text, new.directing_text);
END;
