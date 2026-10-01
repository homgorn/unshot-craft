"""Ingest the upstream video-shotcraft clone into shotcraft.db.

    python -m platform.ingest.run --repo upstream/video-shotcraft

Idempotent: the database is rebuilt from scratch each run, so the run is a pure
function of (upstream tree, this code). Every run records itself in ingest_run.
"""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from shotcraft_ingest import motion, parsing  # noqa: E402
from shotcraft_ingest.parsing import (  # noqa: E402
    block_at, parse_card, parse_js_map, top_level_member, unescape_js,
)

ROOT = Path(__file__).resolve().parents[2]  # workspace root
SCHEMA = Path(__file__).resolve().parent / "schema.sql"

CATEGORY_ORDER = [
    "opening", "typography", "ui-entrance", "camera", "data",
    "interaction", "transition", "rhythm", "effects", "outro",
]
CATEGORY_LABELS = {
    "opening": ("Opening & Brand", "开场与品牌", "Открытие и бренд"),
    "typography": ("Typography & Title Cards", "文字与字卡", "Типографика и титры"),
    "ui-entrance": ("UI Entrance & Showcase", "界面登场与陈列", "Появление UI"),
    "camera": ("Camera & Space", "运镜与空间", "Камера и пространство"),
    "data": ("Data & Metrics", "数据与指标", "Данные и метрики"),
    "interaction": ("Interaction & Feature Demo", "交互与功能演示", "Взаимодействие и демо"),
    "transition": ("Transitions", "转场", "Переходы"),
    "rhythm": ("Rhythm & Montage", "节奏与蒙太奇", "Ритм и монтаж"),
    "effects": ("Light & Emphasis", "光效与强调", "Свет и акценты"),
    "outro": ("Outro", "收尾", "Финал"),
}

ENERGY_ROWS = [
    ("peak", 8, "峰值", "peak", "пик"),
    ("very-high", 7, "极高", "very high", "очень высокая"),
    ("high", 6, "高", "high", "высокая"),
    ("mid-high", 5, "中高", "mid-high", "средне-высокая"),
    ("mid", 4, "中", "mid", "средняя"),
    ("mid-low", 3, "中低", "mid-low", "ниже среднего"),
    ("low-mid", 2, "低中", "low-mid", "ниже низкой"),
    ("low", 1, "低", "low", "низкая"),
]

LOCALES = [
    # code, bcp47, en, native, status, is_source
    ("en", "en-US", "English", "English", "source", 1),
    ("zh", "zh-CN", "Chinese", "中文", "source", 1),
    ("ru", "ru-RU", "Russian", "Русский", "partial", 0),
    ("es", "es-ES", "Spanish", "Español", "pending", 0),
    ("de", "de-DE", "German", "Deutsch", "pending", 0),
    ("fr", "fr-FR", "French", "Français", "pending", 0),
    ("pt", "pt-BR", "Portuguese", "Português", "pending", 0),
    ("ko", "ko-KR", "Korean", "한국어", "pending", 0),
    ("ja", "ja-JP", "Japanese", "日本語", "pending", 0),
]

LICENSE_ROWS = [
    ("video-shotcraft core", "Apache-2.0", "https://github.com/Vincentwei1021/video-shotcraft/blob/main/LICENSE",
     "free", 0, "keep copyright + NOTICE when redistributing", "LICENSE"),
    ("Remotion (render engine)", "Remotion License",
     "https://github.com/remotion-dev/remotion/blob/main/LICENSE.md",
     "restricted", 1, "free for individuals and small companies; companies may need a paid licence", "README.md"),
    ("Mixkit SFX + BGM", "Mixkit Free License", "https://mixkit.co/license/",
     "free", 0, "free for commercial use, no attribution required", "assets/audio/ATTRIBUTION.md"),
    ("video-talkcraft (sibling skill)", "PolyForm Noncommercial 1.0.0",
     "https://github.com/Vincentwei1021/video-talkcraft/blob/main/LICENSE",
     "requires-license", 1, "commercial use of the tool requires written authorisation", ""),
    ("Shot-recipe provenance (48 cards, 2026-08)", "Apache-2.0, techniques re-implemented",
     "https://github.com/Vincentwei1021/video-shotcraft/blob/main/references/shots/ATTRIBUTION.md",
     "free", 0, "no third-party footage or brand assets included; do not claim endorsement", "references/shots/ATTRIBUTION.md"),
    ("Tracked-out audio (6 files 无法反查)", "unknown", "",
     "unknown", 1, "must be re-licensed or replaced before any commercial delivery", "assets/audio/ATTRIBUTION.md"),
]

OPPORTUNITIES = [
    {
        "key": "localized-library-hub",
        "title": "9-locale shot library hub (the site itself)",
        "thesis": "Upstream ships a library site with exactly two locales and English-only card copy. "
                  "RU/ES/DE/FR/PT/KO/JA pages for 'product promo video' + 'motion design shot library' "
                  "intent have almost no competition: the keyword space is English-dominant while the "
                  "audience is global. Every page is a proof-of-work asset that also serves as a lead magnet.",
        "revenue_model": "ads + service lead-gen",
        "effort": "M", "time_to_first_revenue": "6-8 weeks",
        "evidence": json.dumps({"upstream_locales": 2, "target_locales": 9,
                                "cards": 157, "styles": 214,
                                "stars": 10100, "forks": 899,
                                "source_sites": ["enterprise-dna", "moclaw", "bigprompthub", "onei.ai"]}),
        "depends_on": json.dumps(["F010", "F011", "F012"]),
        "status": "idea",
    },
    {
        "key": "render-farm-saas",
        "title": "Hosted render + shot-preview micro-SaaS",
        "thesis": "The repo explicitly does not ship a hosted renderer; it documents three headless-Linux "
                  "wall (concurrency cap, chrome-headless-shell, blocked CDN). A hosted 'render this shot "
                  "with your product screenshots' API converts a documented pain point into a paid action.",
        "revenue_model": "saas",
        "effort": "L", "time_to_first_revenue": "3-4 months",
        "evidence": json.dumps({"render_blockers_documented": 3,
                                "install_step": "ln -s into ~/.claude/skills or ~/.codex/skills",
                                "free_tier": "single-shot preview"}),
        "depends_on": json.dumps(["F020", "F021"]),
        "status": "idea",
    },
    {
        "key": "brand-pack-marketplace",
        "title": "Paid brand kits (themes, palettes, SFX packs)",
        "thesis": "The Apache-2.0 core already ships 9 visual themes (template/THEMES.md) and 149 SFX. "
                  "Selling pre-skins that drop into the same schema is pure margin: the runtime, the cards "
                  "and the acceptance rules are already paid for by the community.",
        "revenue_model": "marketplace",
        "effort": "S", "time_to_first_revenue": "3-5 weeks",
        "evidence": json.dumps({"themes_upstream": 9, "sfx_upstream": 149, "core_license": "Apache-2.0"}),
        "depends_on": json.dumps(["F030"]),
        "status": "idea",
    },
    {
        "key": "agency-film-in-a-day",
        "title": "Agency: 36-second film in a day",
        "thesis": "A hands-on third-party run reports 35 minutes hands-on for a 36-second promo, and the "
                  "template is a validated 36.2s / 10-shot cut. That is a unit-economics story, not a "
                  "tool story: sell the outcome (a launch film before the funding announcement), not the repo.",
        "revenue_model": "service",
        "effort": "S", "time_to_first_revenue": "immediately",
        "evidence": json.dumps({"hands_on_minutes_reported": 35, "output_seconds": 36,
                                "shots": 10, "source": "moclaw.ai hands-on report"}),
        "depends_on": json.dumps([]),
        "status": "idea",
    },
    {
        "key": "enterprise-license",
        "title": "B2B: branded skill + support SLA",
        "thesis": "Upstream is Apache-2.0, so the code cannot be locked up. The defensible B2B product is "
                  "the part that is NOT in the repo: a branded skill pinned to the client's design system, "
                  "CI that renders on every PR, and an acceptance report per release.",
        "revenue_model": "license",
        "effort": "M", "time_to_first_revenue": "2-3 months",
        "evidence": json.dumps({"core_license": "Apache-2.0",
                                "remotion_commercial": "requires licence for companies",
                                "existing_ci": "pr-checks.yml (tsc + vitest + smoke render)"}),
        "depends_on": json.dumps(["F020", "F040"]),
        "status": "idea",
    },
]

DECISIONS = [
    ("upstream-policy", "Independent fork under our own brand; upstream stays the source, we pin its SHA",
     "Apache-2.0 permits it, the author has no commercial licence to grant us, and a fork that competes "
     "on localisation and service does not need his roadmap.", "docs/adr/0005-upstream-policy.md"),
    ("data-layer", "SQLite + FTS5 as the single index for wiki, site and research",
     "157 cards x 9 locales x ~6 derived fields does not fit in the one-line library.json, and every "
     "downstream consumer (wiki, site, SaaS) needs the same rows exactly once.", "docs/adr/0002-data-layer.md"),
    ("i18n-layer", "Extract inline JS dictionaries into per-locale JSON and generate locale-prefixed static HTML",
     "Today each page embeds its own L10N object (three separate mechanisms). 9 locales x 3 pages cannot "
     "stay inline, and hreflang needs URL-addressable locales for the SEO play to work.",
     "docs/adr/0004-i18n-architecture.md"),
    ("wiki-generation", "LLM wiki is generated from the DB, never hand-edited",
     "The repo moves fast (157 cards and counting). A hand-written wiki is stale within two weeks; a "
     "generated one is a query away from current.", "docs/adr/0003-llm-wiki.md"),
]


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def classify(rel: str) -> str:
    if rel.startswith("references/shots/") and rel.endswith(".md"):
        return "card" if not rel.endswith("ATTRIBUTION.md") else "doc"
    if rel.startswith("references/sequences/"):
        return "sequence"
    if rel.startswith("references/"):
        return "reference"
    if rel.startswith("demos/"):
        return "demo"
    if rel.startswith("assets/lib/"):
        return "component"
    if rel.startswith("assets/audio/"):
        return "asset"
    if rel.startswith("gallery/"):
        return "site"
    if rel.startswith(".github/workflows/"):
        return "ci"
    if rel.startswith("template/src/"):
        return "component"
    if rel.startswith("workbench/src/"):
        return "component"
    if rel.endswith("LICENSE"):
        return "license"
    if rel.endswith((".md", ".yml", ".yaml", ".json")):
        return "config" if rel.endswith((".json", ".yml", ".yaml")) else "doc"
    return "other"


CATALOG_SCHEMA = Path(__file__).resolve().parent.parent / "catalog" / "schema.sql"


def build_db(db_path: Path, repo: Path) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    if db_path.exists():
        db_path.unlink()
    for suffix in ("-wal", "-shm"):
        p = db_path.with_name(db_path.name + suffix)
        if p.exists():
            p.unlink()
    conn = sqlite3.connect(db_path)
    conn.executescript(SCHEMA.read_text(encoding="utf-8"))
    # Section 10 (the cinematic catalog, ADR 0007) is applied after the upstream
    # schema because two FKs cross the corpus boundary on purpose. Kept in a
    # separate file so the two workstreams do not merge-conflict in one document.
    if CATALOG_SCHEMA.exists():
        conn.executescript(CATALOG_SCHEMA.read_text(encoding="utf-8"))
    return conn


def run(repo: Path, db_path: Path) -> dict:
    conn = build_db(db_path, repo)
    warnings: list[str] = []
    stats = {"files": 0, "cards": 0, "styles": 0, "params": 0, "translations": 0,
             "sfx": 0, "docs": 0, "rules": 0}

    # -- provenance ---------------------------------------------------------
    head_sha = subprocess_sha(repo)
    cur = conn.execute(
        "INSERT INTO source_repo(slug,url,license,owner,local_path,head_sha,head_date,stars,forks,description,cloned_at)"
        " VALUES(?,?,?,?,?,?,?,?,?,?,?)",
        ("video-shotcraft", "https://github.com/Vincentwei1021/video-shotcraft", "Apache-2.0",
         "Vincentwei1021", str(repo).replace("\\", "/"), head_sha, head_date(repo), 10100, 899,
         "Agent skill for cinematic product videos with Remotion", now_iso()),
    )
    repo_id = cur.lastrowid
    run_id = conn.execute(
        "INSERT INTO ingest_run(repo_id, upstream_sha) VALUES(?,?)", (repo_id, head_sha)).lastrowid

    # -- taxonomy -----------------------------------------------------------
    cat_ids: dict[str, int] = {}
    for i, key in enumerate(CATEGORY_ORDER):
        en, zh, ru = CATEGORY_LABELS[key]
        cid = conn.execute(
            "INSERT INTO category(key,order_idx,label_en,label_zh,label_ru) VALUES(?,?,?,?,?)",
            (key, i, en, zh, ru)).lastrowid
        cat_ids[key] = cid
    for key, rank, zh, en, ru in ENERGY_ROWS:
        conn.execute(
            "INSERT INTO energy_level(key,rank,label_zh,label_en,label_ru) VALUES(?,?,?,?,?)",
            (key, rank, zh, en, ru))
    energy_id = {r[0]: r[1] for r in conn.execute("SELECT key,id FROM energy_level")}

    for ordinal, zh, en in [("①", "品牌开场", "Brand open"), ("②", "单主角立传", "Single-hero portrait"),
                            ("③", "功能爬升段", "Feature climb"), ("④", "发布会收场", "Launch finale")]:
        conn.execute("INSERT INTO sequence_stage(ordinal,label_zh,label_en) VALUES(?,?,?)", (ordinal, zh, en))

    for code, bcp, en, native, status, is_src in LOCALES:
        font = ("'PingFang SC','Hiragino Sans','Microsoft YaHei',sans-serif" if code in ("zh", "ja", "ko")
                else "'Avenir Next',Inter,system-ui,sans-serif")
        conn.execute(
            "INSERT INTO locale(code,bcp47,name_en,native_name,is_source,status,font_stack,html_lang)"
            " VALUES(?,?,?,?,?,?,?,?)",
            (code, bcp, en, native, is_src, status, font,
             {"zh": "zh-CN", "ja": "ja", "ko": "ko"}.get(code, code)))

    # -- file walk ----------------------------------------------------------
    file_ids: dict[str, int] = {}
    for path in sorted(repo.rglob("*")):
        if not path.is_file() or ".git" in path.parts or "node_modules" in path.parts:
            continue
        rel = path.relative_to(repo).as_posix()
        if rel.endswith((".mp4", ".mov", ".webm")):
            continue
        stats["files"] += 1
        try:
            sha, size = parsing.sha256(path), path.stat().st_size
        except OSError:
            continue
        fid = conn.execute(
            "INSERT INTO source_file(repo_id,path,sha256,bytes,role) VALUES(?,?,?,?,?)",
            (repo_id, rel, sha, size, classify(rel))).lastrowid
        file_ids[rel] = fid

    # -- shot cards FIRST: the demo directory name is the authoritative
    #    card <-> style link, so the card table has to exist before we scan demos
    card_id: dict[str, int] = {}
    pending_variants: list[tuple[int, list]] = []
    for md in sorted((repo / "references" / "shots").rglob("*.md")):
        if md.name == "ATTRIBUTION.md":
            continue
        rel = md.relative_to(repo).as_posix()
        category = md.parent.name
        if category not in cat_ids:
            warnings.append(f"unknown category dir: {category}")
            continue
        card = parse_card(md, category, rel)
        cid = conn.execute(
            "INSERT INTO shot_card(name,category_id,summary_zh,use_zh,duration_text,duration_frames,"
            "energy_level_id,energy_text,energy_rationale,intention_zh,source_file_id,source_path,source_url)"
            " VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (card.name, cat_ids[category], card.summary, card.use, card.duration_text,
             card.duration_frames, energy_id.get(card.energy_key or ""), card.energy_text,
             card.energy_rationale, card.intention, file_ids.get(rel), rel,
             f"./source/{card.name}.md")).lastrowid
        card_id[card.name] = cid
        stats["cards"] += 1
        for tag in [category, *card.tags]:
            if tag in cat_ids:
                conn.execute("INSERT OR IGNORE INTO shot_card_tag(card_id,category_id) VALUES(?,?)", (cid, cat_ids[tag]))
        for i, (heading, kind, body) in enumerate(card.sections):
            conn.execute("INSERT INTO card_section(card_id,ordinal,heading,kind,body) VALUES(?,?,?,?,?)",
                         (cid, i, heading, kind, body))
        for j, (key, typ, feel, _l) in enumerate(card.params):
            m = re.match(r"^([A-Z])\s", key)
            conn.execute("INSERT INTO card_param(card_id,ordinal,variant_letter,param_key,typical_value,feel_note)"
                         " VALUES(?,?,?,?,?,?)",
                         (cid, j, m.group(1) if m else None, key, typ, feel))
        for j, (text, crit, refs) in enumerate(card.pitfalls):
            conn.execute("INSERT INTO card_pitfall(card_id,ordinal,text,is_critical,rule_refs) VALUES(?,?,?,?,?)",
                         (cid, j, text, int(crit), refs))
            conn.execute("INSERT INTO pitfall_fts(text) VALUES(?)", (text,))
            conn.execute("INSERT INTO pitfall_fts_trgm(text) VALUES(?)", (text,))
        pending_variants.append((cid, card.variants))

    # -- demos -> style + motion params ------------------------------------
    style_id: dict[str, int] = {}
    style_by_norm: dict[str, int] = {}
    demo_files = sorted((repo / "demos").rglob("*.tsx"))
    curve_counts: dict[str, dict] = {}
    for tsx in demo_files:
        rel = tsx.relative_to(repo).as_posix()
        if "/_fixtures/" in rel or "/_textures/" in rel:
            continue
        info = motion.scan_demo(tsx)
        if not info["component_name"]:
            continue
        parts = tsx.relative_to(repo).parts
        category = parts[1] if len(parts) > 3 else None
        card_slug = tsx.parent.name          # authoritative: demos/<cat>/<slug>/<Comp>.tsx
        key = motion.kebab(tsx.stem)
        if key in style_id:
            continue
        sid = conn.execute(
            "INSERT INTO style(key,card_id,category_id,demo_path,component_name,duration_frames,"
            "duration_source,family,uses_normalized_t,design_stage) VALUES(?,?,?,?,?,?,?,?,?,?)",
            (key, card_id.get(card_slug), cat_ids.get(category), rel, info["component_name"],
             info["duration_frames"], info["duration_source"], info["family"],
             info["uses_normalized_t"], info["design_stage"])).lastrowid
        style_id[key] = sid
        style_by_norm.setdefault(motion.norm(key), sid)
        stats["styles"] += 1
        for p in info["params"]:
            conn.execute(
                "INSERT INTO motion_param(style_id,kind,name,args_json,detail,line_no,raw)"
                " VALUES(?,?,?,?,?,?,?)",
                (sid, p["kind"], p["name"], json.dumps(p["args"], ensure_ascii=False),
                 p["detail"], p["line"], p["raw"]))
            stats["params"] += 1
            if p["kind"] == "bezier":
                a = p["args"]
                spec = f"bezier({a['x1']:g},{a['y1']:g},{a['x2']:g},{a['y2']:g})"
                rec = curve_counts.setdefault(spec, dict(args=a, over=int(a["y1"] > 1), n=0))
                rec["n"] += 1

    for spec, rec in sorted(curve_counts.items(), key=lambda kv: -kv[1]["n"]):
        a = rec["args"]
        eid = conn.execute(
            "INSERT INTO easing_curve(kind,spec,x1,y1,x2,y2,overshoot,usage_count) VALUES(?,?,?,?,?,?,?,0)",
            ("bezier", spec, a["x1"], a["y1"], a["x2"], a["y2"], rec["over"])).lastrowid
        # attach every style that uses exactly this curve
        needle = json.dumps(a, ensure_ascii=False)
        rows = conn.execute(
            "SELECT style_id, COUNT(*) FROM motion_param WHERE kind='bezier' AND args_json=?"
            " GROUP BY style_id", (needle,)).fetchall()
        for sid, n in rows:
            conn.execute("INSERT OR REPLACE INTO style_easing(style_id,easing_id,occurrences) VALUES(?,?,?)",
                         (sid, eid, n))
        conn.execute("UPDATE easing_curve SET usage_count=? WHERE id=?", (sum(r[1] for r in rows), eid))

    # every style in demos/<cat>/<slug>/ belongs to card <slug> by construction
    for sc_id in card_id.values():
        seq = 0
        for (sv_id,) in conn.execute(
                "SELECT id FROM style WHERE card_id=? ORDER BY key", (sc_id,)).fetchall():
            conn.execute("INSERT OR IGNORE INTO card_variant(card_id,style_id,ordinal) VALUES(?,?,?)",
                         (sc_id, sv_id, seq))
            seq += 1
    # variant letters scraped from the cards' `## N式选型` tables
    for cid, variants in pending_variants:
        for slug, letter in variants:
            sid = style_id.get(slug) or style_by_norm.get(motion.norm(slug))
            if sid:
                conn.execute("UPDATE card_variant SET letter=? WHERE card_id=? AND style_id=?",
                             (letter, cid, sid))

    # -- library.json cross-check -----------------------------------------
    lib_path = repo / "gallery" / "api" / "library.json"
    if lib_path.exists():
        lib = json.loads(lib_path.read_text(encoding="utf-8"))
        orphan_keys: list[str] = []
        for entry in lib.get("cards", []):
            cid = card_id.get(entry.get("name"))
            if not cid:
                warnings.append(f"library.json card not in references/shots: {entry.get('name')}")
                continue
            conn.execute("UPDATE shot_card SET added_at=?,updated_at=? WHERE id=?",
                         (entry.get("addedAt"), entry.get("updatedAt"), cid))
            for st in entry.get("styles", []):
                gkey = st.get("key")
                # NOTE: style.card_id comes from the demo directory, not from here.
                # library.json is lossy (e.g. crash-zoom-punch lists one key while the
                # demo dir holds two components), so it is matched, never trusted.
                sid = style_id.get(gkey) or style_by_norm.get(motion.norm(gkey or ""))
                if not sid:
                    orphan_keys.append(f"{entry.get('name')}:{gkey}")
                    conn.execute(
                        "INSERT INTO gallery_style(key,card_id,label,description_zh,media_url,media_type)"
                        " VALUES(?,?,?,?,?,?)",
                        (gkey, cid, st.get("label"), st.get("description"),
                         (st.get("media") or {}).get("url") if isinstance(st.get("media"), dict) else st.get("media"),
                         (st.get("media") or {}).get("type") if isinstance(st.get("media"), dict) else None))
                    continue
                conn.execute("UPDATE style SET gallery_style_key=? WHERE id=?", (gkey, sid))
                if not conn.execute("SELECT 1 FROM card_variant WHERE card_id=? AND style_id=?", (cid, sid)).fetchone():
                    conn.execute("INSERT INTO card_variant(card_id,style_id,ordinal) VALUES(?,?,?)",
                                 (cid, sid, 999))
                media = st.get("media") or {}
                url = media.get("url") if isinstance(media, dict) else media
                for kind, murl, mtype in (("preview", url, (media.get("type") if isinstance(media, dict) else None)),
                                          ("poster", f"./media/poster/{gkey}.jpg", "jpg")):
                    local = repo / "gallery" / murl.split("?")[0].lstrip("./") if murl else None
                    present = int(bool(local and local.exists()))
                    conn.execute("INSERT INTO style_media(style_id,kind,url,media_type,remote_url,local_path,present)"
                                 " VALUES(?,?,?,?,?,?,?)",
                                 (sid, kind, murl, mtype, murl, str(local) if present else None, present))
        if orphan_keys:
            warnings.append(f"library.json style keys with no matching demo component: {len(orphan_keys)} "
                            f"(e.g. {', '.join(orphan_keys[:5])})")
        if lib.get("stats"):
            conn.execute("INSERT INTO decision_log(area,decision,rationale) VALUES(?,?,?)",
                         ("upstream-stats", json.dumps(lib["stats"], ensure_ascii=False),
                          f"library.json revision {lib.get('revision')}"))
    # Every style gets an explicit media row, even when library.json advertises
    # none for it. A missing row means "we never looked"; a present row with
    # present=0 means "we looked and the file is not there". Collapsing the two
    # hides 35 real gaps behind an absence.
    for sid, key in conn.execute("SELECT id, key FROM style"):
        have = conn.execute("SELECT COUNT(*) FROM style_media WHERE style_id=?", (sid,)).fetchone()[0]
        if not have:
            poster_rel = f"gallery/media/poster/{key}.jpg"
            present = int((repo / poster_rel).exists())
            conn.execute("INSERT INTO style_media(style_id,kind,url,media_type,local_path,present)"
                         " VALUES(?,?,?,?,?,?)",
                         (sid, "poster", f"./media/poster/{key}.jpg", "jpg",
                          poster_rel if present else None, present))
            conn.execute("INSERT INTO style_media(style_id,kind,url,media_type,present)"
                         " VALUES(?,?,?,?,0)",
                         (sid, "preview", f"./media/{key}.mp4", "mp4"))
        # style_fts covers every style, not only the 183 that library.json
        # advertises. The 35 library.json-orphan styles are real demos (AGENTS.md
        # rule 5 keeps them in gallery_style, it does not delete them), and an
        # agent searching by style key must be able to find them.
        zh = conn.execute(
            "SELECT t.text FROM translation t JOIN locale l ON l.id=t.locale_id "
            "WHERE l.code='zh' AND t.ns='style' AND t.key=?", (key,)).fetchone()
        conn.execute("INSERT OR IGNORE INTO style_fts(key,name_zh,description_zh) VALUES(?,?,?)",
                     (key, zh[0] if zh else None, None))

    conn.execute("""UPDATE category SET card_count =
                    (SELECT COUNT(*) FROM shot_card WHERE shot_card.category_id=category.id)""")

    # CJK-capable index: unicode61 cannot match inside a Chinese phrase
    for c in conn.execute("SELECT id, name, summary_zh, use_zh, intention_zh FROM shot_card"):
        conn.execute("INSERT INTO card_fts_trgm(name, summary_zh, use_zh, intention_zh) VALUES(?,?,?,?)",
                     (c[1], c[2], c[3], c[4]))

    # -- i18n source strings ----------------------------------------------
    ui_ids: dict[tuple[str, str], int] = {}

    def add_tr(locale_code: str, ns: str, key: str, text: str, method: str = "human"):
        lid = conn.execute("SELECT id FROM locale WHERE code=?", (locale_code,)).fetchone()[0]
        conn.execute(
            "INSERT OR REPLACE INTO translation(locale_id,ns,key,text,method,status) VALUES(?,?,?,?,?,'translated')",
            (lid, ns, key, text, method))
        stats["translations"] += 1

    tr_path = repo / "gallery" / "translations.js"
    if tr_path.exists():
        src = tr_path.read_text(encoding="utf-8")
        ui_seg = top_level_member(src, "ui") or ""
        for loc in ("zh", "en"):
            m = re.search(rf"(?m)^\s*{loc}\s*:\s*\{{", ui_seg)
            if m:
                seg, _ = block_at(ui_seg, m.end() - 1)
                for k, v in parse_js_map(seg).items():
                    add_tr(loc, "ui", k, v)
        for member, ns, loc in (("cardsZh", "card", "zh"), ("cardsEn", "card", "en"),
                                ("stylesZh", "style", "zh"), ("stylesEn", "style", "en")):
            seg = top_level_member(src, member) or ""
            for k, v in parse_js_map(seg).items():
                add_tr(loc, ns, k, v, "human" if loc == "zh" else "human")

    index_html = repo / "gallery" / "index.html"
    if index_html.exists():
        html = index_html.read_text(encoding="utf-8")
        m = re.search(r"const L10N\s*=\s*\{", html)
        if m:
            seg, _ = block_at(html, m.end() - 1)
            for loc in ("en", "zh"):
                mm = re.search(rf"(?m)^\s*{loc}\s*:\s*\{{", seg)
                if mm:
                    s2, _ = block_at(seg, mm.end() - 1)
                    for k, v in parse_js_map(s2).items():
                        add_tr(loc, "page", f"index.{k}", unescape_js(v))

    showcase_js = repo / "gallery" / "showcase.js"
    if showcase_js.exists():
        js = showcase_js.read_text(encoding="utf-8")
        m = re.search(r"SHOWCASE_L10N\s*=\s*\{", js)
        if m:
            seg, _ = block_at(js, m.end() - 1)
            for loc in ("zh", "en"):
                mm = re.search(rf"(?m)^\s*{loc}\s*:\s*\{{", seg)
                if mm:
                    s2, _ = block_at(seg, mm.end() - 1)
                    for k, v in parse_js_map(s2).items():
                        add_tr(loc, "showcase", k, v)

    # workbench already ships Russian demo names -> seed ru as 'machine'-sourced
    wb_ru = repo / "workbench" / "i18n" / "ru"
    if wb_ru.is_dir():
        for f in sorted(wb_ru.glob("*.json")):
            data = json.loads(f.read_text(encoding="utf-8"))
            ns = {"names.json": "card", "categories.json": "category",
                  "summaries.1.json": "summary", "summaries.2.json": "summary"}.get(f.name, f.stem)
            items = data.items() if isinstance(data, dict) else []
            for k, v in items:
                if isinstance(v, str):
                    add_tr("ru", ns, k, v, "machine")
                elif isinstance(v, dict):
                    for k2, v2 in v.items():
                        if isinstance(v2, str):
                            add_tr("ru", ns, f"{k}.{k2}", v2, "machine")

    # -- audio assets + licences ------------------------------------------
    att_path = repo / "assets" / "audio" / "ATTRIBUTION.md"
    att_text = att_path.read_text(encoding="utf-8") if att_path.exists() else ""
    # Files upstream could not trace at download time. Upstream marks them inside
    # the row's source column rather than in a separate list, so the flag has to
    # be read per row, not by filename anywhere in the document.
    untraceable: set[str] = set()
    for line in att_text.splitlines():
        if "无法反查" not in line:
            continue
        untraceable.update(re.findall(r"`([\w\-.]+\.mp3)`", line))
    for mp3 in sorted((repo / "assets" / "audio").rglob("*.mp3")):
        rel = mp3.relative_to(repo).as_posix()
        kind = "bgm" if "/bgm/" in rel else "sfx"
        cat = mp3.parent.name if kind == "sfx" else None
        # ATTRIBUTION.md keys its table by bare filename with the directory in
        # a separate column, so the row is `| `name.mp3` | `sfx/text/` | ... |`.
        # Presence of a row proves the file was catalogued; whether the *source*
        # column is filled is the separate, and more important, question.
        row_present = bool(re.search(rf"\|\s*`{re.escape(mp3.name)}`\s*\|", att_text))
        flagged = mp3.name in untraceable or rel in untraceable
        traceable = 1 if (row_present and not flagged) else 0
        note = None
        if flagged:
            note = "ATTRIBUTION.md marks this 无法反查: source cannot be traced"
        elif not row_present:
            note = "no ATTRIBUTION.md row found; treated as unverified"
        conn.execute(
            "INSERT OR IGNORE INTO audio_asset(kind,path,category,title,traceable,commercial_ok,bytes,note)"
            " VALUES(?,?,?,?,?,?,?,?)",
            (kind, rel, cat, mp3.stem, traceable, 0 if traceable == 0 else 1, mp3.stat().st_size,
             note))
        stats["sfx"] += 1

    # Upstream's ATTRIBUTION.md prose claims 6 untraceable files while its table
    # marks 5. The table is the evidence, so the table wins -- but the gap is
    # recorded rather than reconciled in silence, because "which file did they
    # mean" is a question for upstream and not something to guess at.
    prose = re.search(r"剩余\s*(\d+)\s*个仍无法反查", att_text)
    if prose and int(prose.group(1)) != len(untraceable):
        conn.execute(
            "INSERT INTO decision_log(area,decision,rationale) VALUES(?,?,?)",
            ("audio-provenance",
             json.dumps({"table_flags": sorted(untraceable),
                         "table_count": len(untraceable),
                         "prose_claims": int(prose.group(1))}, ensure_ascii=False),
             "ATTRIBUTION.md prose says " + prose.group(1) + " untraceable but its "
             f"table marks {len(untraceable)}. The table is the evidence and wins; "
             "the extra file is unidentified. Every flagged file is commercial_ok=0 "
             "either way, so the delivery gate is unaffected."))
        warnings.append(f"audio provenance discrepancy: ATTRIBUTION.md prose says "
                        f"{prose.group(1)} untraceable, its table marks {len(untraceable)}")

    for subject, spdx, url, commercial, blocking, obligation, evidence in LICENSE_ROWS:
        conn.execute(
            "INSERT OR REPLACE INTO license_registry(subject,spdx,url,commercial_use,blocking,obligation,evidence_path)"
            " VALUES(?,?,?,?,?,?,?)", (subject, spdx, url, commercial, blocking, obligation, evidence))

    # -- methodology docs + rules -----------------------------------------
    METHOD_PURPOSE = {
        "pipeline": "Eight-stage production pipeline, stage 0 product understanding to stage 7 independent final review",
        "guided-free-creation": "Co-creation mode: five user confirmation gates plus the Gallery shot-name resolution protocol",
        "aesthetic-rules": "The ruling law: 26 numbered precedents in five families (R rhythm, Q quality, S sound, C copy, P process)",
        "final-review": "Clean-context subagent acceptance checklist, eight groups, frame-numbered evidence required",
        "sound-design": "SFX methodology: BGM energy skeleton, genre vocabulary, declarative cue table, exclusion lists",
        "music-beat-sync": "BGM beat-grid methodology: least-squares fit, transient classification, beatF(n) timeline, 3-frame tolerance",
        "workbench": "Integration contract for the post-delivery browser workbench: manifest shape and the fixed-vs-exposed parameter rule",
        "jianying-export": "Export a Remotion timeline to an editable JianYing (CapCut CN) draft",
    }
    for md in sorted((repo / "references").glob("*.md")):
        slug = md.stem
        text = md.read_text(encoding="utf-8")
        headings = re.findall(r"^#{2,3}\s+(.+)$", text, re.M)
        conn.execute("INSERT INTO method_doc(slug,title,purpose,headings_json,bytes,source_path,source_file_id)"
                     " VALUES(?,?,?,?,?,?,?)",
                     (slug, headings[0] if headings else slug, METHOD_PURPOSE.get(slug, ""),
                      json.dumps(headings, ensure_ascii=False), len(text.encode("utf-8")),
                      md.relative_to(repo).as_posix(), file_ids.get(md.relative_to(repo).as_posix())))
        conn.execute("INSERT INTO doc_fts(slug,title,body) VALUES(?,?,?)", (slug, slug, text))
        stats["docs"] += 1

    ar = repo / "references" / "aesthetic-rules.md"
    if ar.exists():
        text = ar.read_text(encoding="utf-8")
        for m in re.finditer(r"^###\s*([RQSPC]\d{1,2})[^\n]*\n(.*?)(?=\n###\s|\Z)", text, re.M | re.S):
            rule_id, blob = m.group(1), m.group(2)
            body_lines = [l.strip("> ").strip() for l in blob.splitlines() if l.strip()]
            q = next((l for l in body_lines if l.startswith("自检") or l.endswith("？") or "?" in l), None)
            conn.execute("INSERT OR IGNORE INTO rule(family,rule_id,title,body,check_question,source_file_id)"
                         " VALUES(?,?,?,?,?,?)",
                         (rule_id[0], rule_id, body_lines[0] if body_lines else None,
                          re.sub(r"\n{2,}", "\n", blob).strip()[:4000], q,
                          file_ids.get("references/aesthetic-rules.md")))
            stats["rules"] += 1

    seq = repo / "references" / "sequences" / "promo-energy-arc.md"
    if seq.exists():
        text = seq.read_text(encoding="utf-8")
        fm, body = parsing.split_frontmatter(text)
        tid = conn.execute(
            "INSERT INTO sequence_template(name,summary_zh,use_zh,stage_count,source_file_id) VALUES(?,?,?,?,?)",
            (fm.get("name", "promo-energy-arc"), fm.get("一句话"), fm.get("适用"), fm.get("段数"),
             file_ids.get("references/sequences/promo-energy-arc.md"))).lastrowid
        for heading, kind, sec_body in parsing.parse_sections(body):
            if kind != "stages":
                continue
            for row in parsing.parse_md_table(sec_body):
                if len(row) >= 5:
                    ordinal = next((s for s in ("①", "②", "③", "④") if row[0].startswith(s)), None)
                    st = conn.execute("SELECT id FROM sequence_stage WHERE ordinal=?", (ordinal,)).fetchone()
                    conn.execute(
                        "INSERT INTO sequence_stage_candidate(template_id,ordinal,stage_id,card_name)"
                        " VALUES(?,?,?,?)", (tid, ord(ordinal) if ordinal else 0, st[0] if st else None, row[4]))

    # -- research + decisions ---------------------------------------------
    for subject, spdx, url, *_ in LICENSE_ROWS:
        if subject == "video-shotcraft core":
            conn.execute("INSERT INTO actor(name,kind,url,repo,stars,license,positioning) VALUES(?,?,?,?,?,?,?)",
                         ("Vincentwei1021 / video-shotcraft", "upstream-author",
                          "https://github.com/Vincentwei1021", "Vincentwei1021/video-shotcraft", 10100,
                          "Apache-2.0", "Author of the video-shotcraft / video-talkcraft agent skill series"))
    for name, url, kind, stars, lic, pos in [
        ("video-talkcraft", "https://github.com/Vincentwei1021/video-talkcraft", "sibling-skill", 1300,
         "PolyForm Noncommercial 1.0.0", "Narration-video installment of the same series, word-level voiceover sync, 108 cards"),
        ("Remotion", "https://www.remotion.dev/", "tool", None, "Remotion License",
         "React video framework the whole repo renders through; company licence required for companies"),
        ("skills.sh", "https://skills.sh/", "channel", None, "",
         "CLI/registry that installs the skill: npx skills add Vincentwei1021/video-shotcraft"),
        ("claudepluginhub.com", "https://www.claudepluginhub.com/", "channel", None, "",
         "Plugin directory mirroring the skill"),
    ]:
        conn.execute("INSERT INTO actor(name,kind,url,stars,license,positioning) VALUES(?,?,?,?,?,?)",
                     (name, kind, url, stars, lic, pos))
    for name, url, kind, reach in [
        ("Enterprise DNA AI Pulse", "https://enterprisedna.co/resources/ai-pulse/", "newsletter", "1387 stars in 5 days"),
        ("MoClaw blog", "https://moclaw.ai/blog/product-video-claude-code-video-shotcraft", "blog", "hands-on 36s film report"),
        ("Big Prompt Hub", "https://www.bigprompthub.com/video-shotcraft-remotion-product-video-skill/", "directory", "review page"),
        ("onei.ai", "https://onei.ai/skills/video-shotcraft", "directory", "skill index"),
        ("Trendshift", "https://trendshift.io/repositories/88911", "social", "repo tracking"),
    ]:
        conn.execute("INSERT INTO source_channel(name,url,kind,reach) VALUES(?,?,?,?)", (name, url, kind, reach))

    for op in OPPORTUNITIES:
        conn.execute(
            "INSERT INTO opportunity(key,title,thesis,revenue_model,effort,time_to_first_revenue,evidence,depends_on,status)"
            " VALUES(?,?,?,?,?,?,?,?,?)",
            (op["key"], op["title"], op["thesis"], op["revenue_model"], op["effort"],
             op["time_to_first_revenue"], op["evidence"], op["depends_on"], op["status"]))
    for area, decision, rationale, adr in DECISIONS:
        conn.execute("INSERT INTO decision_log(area,decision,rationale,adr) VALUES(?,?,?,?)",
                     (area, decision, rationale, adr))

    # style labels are the union of label + description; keep the FTS complete
    # param_fts is its own index rather than a column on shot_card, because the
    # searchable unit is the parameter ("词间 stagger"), not the card. Without it
    # an agent asking "what gap looks right here" gets nothing back.
    for pk, tv, fn in conn.execute(
            "SELECT param_key, typical_value, feel_note FROM card_param"):
        conn.execute("INSERT INTO param_fts(param_key, typical_value, feel_note) VALUES(?,?,?)",
                     (pk, tv, fn))

    # -- unified search surface: pool every locale + params + pitfalls + styles
    #    into one blob per card so a query works in any language.
    tr_rows = conn.execute("""
        SELECT t.key, l.code, t.ns, t.text FROM translation t JOIN locale l ON l.id=t.locale_id
        WHERE t.ns IN ('card','style','summary')""").fetchall()
    by_key: dict[str, list[str]] = defaultdict(list)
    for key, code, ns, text in tr_rows:
        by_key[key].append(f"{ns}:{code}:{text}")
    latin_pool: dict[int, list[str]] = defaultdict(list)
    for cid, key in conn.execute("SELECT s.card_id, s.key FROM style s WHERE s.card_id IS NOT NULL"):
        if key not in latin_pool[cid]:
            latin_pool[cid].append(key)
    for cid, name, summary, use, intention in conn.execute(
            "SELECT id, name, summary_zh, use_zh, intention_zh FROM shot_card").fetchall():
        parts = [name, summary or "", use or "", intention or ""]
        parts += by_key.get(name, [])
        parts += [r[0] for r in conn.execute(
            "SELECT param_key || ' ' || COALESCE(typical_value,'') FROM card_param WHERE card_id=?", (cid,))]
        parts += [r[0] for r in conn.execute("SELECT text FROM card_pitfall WHERE card_id=?", (cid,))]
        parts += [r[0] for r in conn.execute("SELECT heading FROM card_section WHERE card_id=?", (cid,))]
        latin = " ".join([name, *latin_pool.get(cid, [])])
        blob = " ".join(p for p in parts if p)
        conn.execute("INSERT INTO card_search(card_id,slug,text_all,text_latin) VALUES(?,?,?,?)",
                     (cid, name, blob, latin))
        conn.execute("INSERT INTO search_fts(slug, text_all) VALUES(?,?)", (name, blob))
        conn.execute("INSERT INTO search_fts_trgm(slug, text_all) VALUES(?,?)", (name, blob))

    # -- second corpus: the cinematic catalog (ADR 0007).
    # Tolerant of absence in both directions: either corpus must build alone.
    catalog: dict = {}
    try:
        import catalog as catalog_ingest
        catalog = catalog_ingest.ingest(conn)
        if catalog.get("status") == "ok":
            for p in (ROOT / "data" / "cinematic").glob("*.md"):
                if p.name == "README.md":
                    continue
                stats["files"] += 1
    except Exception as exc:                      # noqa: BLE001
        catalog = {"status": "failed", "error": str(exc)}
        warnings.append(f"catalog ingest failed: {exc}")

    conn.execute(
        "UPDATE ingest_run SET finished_at=?, files_seen=?, cards_seen=?, styles_seen=?, params_extracted=?,"
        " locale_rows=?, warnings=?, status='ok' WHERE id=?",
        (now_iso(), stats["files"], stats["cards"], stats["styles"], stats["params"],
         stats["translations"], json.dumps(warnings[:200], ensure_ascii=False), run_id))
    conn.commit()
    return {"stats": stats, "warnings": warnings, "head_sha": head_sha, "catalog": catalog}


def subprocess_sha(repo: Path) -> str:
    import subprocess
    try:
        return subprocess.run(["git", "-C", str(repo), "rev-parse", "HEAD"],
                              capture_output=True, text=True, timeout=20).stdout.strip() or "unknown"
    except Exception:
        return "unknown"


def head_date(repo: Path) -> str | None:
    import subprocess
    try:
        out = subprocess.run(["git", "-C", str(repo), "log", "-1", "--format=%cI"],
                             capture_output=True, text=True, timeout=20).stdout.strip()
        return out or None
    except Exception:
        return None


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default="upstream/video-shotcraft")
    ap.add_argument("--db", default="platform/db/shotcraft.db")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    result = run(ROOT / a.repo, ROOT / a.db)
    print(json.dumps(result, indent=2, ensure_ascii=False))