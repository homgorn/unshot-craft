"""F070: ingest the cinematic catalog (data/cinematic/) into shotcraft.db.

Called from platform/ingest/run.py. Deliberately tolerant of both inputs being
missing, because ADR 0007 requires each corpus to build alone:

    upstream present, catalog missing  -> upstream tables still build
    upstream missing, catalog present  -> catalog tables still build
    both present                       -> the cross-corpus join becomes possible

Three rules this module enforces rather than documents:

1. `[Subject]` survives verbatim. An expanded prompt reads exactly like an authored
   one, and an agent handed it will paste it to a client as though the studio wrote
   it. Same failure mode F050 documents for copy slots.
2. `category` is a controlled vocabulary. An unknown value fails the ingest rather
   than bucketing into 'other', which is what makes `--category lighting` a filter
   instead of a guess.
3. An absent cross-tool cell is NULL, never a default. `tested: no` is the honest
   state for a parameter nobody has run.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from shotcraft_ingest.parsing import split_frontmatter, sha256  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
CATALOG = ROOT / "data" / "cinematic"
SLOT = "[Subject]"

# Controlled vocabulary. Mirrors the rows seeded in platform/catalog/schema.sql.
# Kept as data so the ingest can fail loudly on drift rather than import it.
#
# Seven. Cinematique's source catalog has "Visual Effects & Promptable FX" as its
# own group, distinct from "Genres & Styles", so squashing it into visual-style
# would have made `--category visual-style` return rows that are not about visual
# style. There is no separate 'visual-style' key because the corpus has no such
# group: a vocabulary entry nothing can populate is a broken filter, not a
# category.
CATEGORIES = {
    "camera-work": "Camera Work",
    "lighting": "Lighting",
    "composition": "Composition",
    "editing": "Editing",
    "narrative": "Narrative",
    "visual-effects": "Visual Effects & Promptable FX",
    "genres": "Film Genres",
}

SECTION_RE = re.compile(r"^##\s+(.+?)\s*$", re.M)
TOOL_ROW_RE = re.compile(r"^\|\s*([a-z0-9_]+)\s*\|\s*(.*?)\s*\|\s*([\w.\-]*)\s*\|\s*(yes|no)\s*\|$",
                         re.I | re.M)
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


class CatalogError(RuntimeError):
    pass


def parse(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    fm, body = split_frontmatter(text)

    slug = (fm.get("slug") or path.stem).strip()
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
        raise CatalogError(f"{path.name}: slug {slug!r} is not ASCII kebab-case")

    category = (fm.get("category") or "").strip()
    if category not in CATEGORIES:
        raise CatalogError(
            f"{path.name}: category {category!r} is outside the controlled vocabulary "
            f"{sorted(CATEGORIES)}")

    title = (fm.get("title") or "").strip()
    if not title:
        raise CatalogError(f"{path.name}: missing title")

    # The prompt is everything before the first H2, verbatim.
    first_h2 = SECTION_RE.search(body)
    prompt_text = (body[: first_h2.start()] if first_h2 else body).strip()
    if not prompt_text:
        raise CatalogError(f"{path.name}: no prompt text")
    if SLOT not in prompt_text:
        raise CatalogError(
            f"{path.name}: prompt has no {SLOT} slot. The corpus stores prompts verbatim "
            f"with the slot intact; a prompt without it was expanded somewhere upstream.")

    sections: dict[str, str] = {}
    marks = [(m.start(), m.end(), m.group(1).strip().lower()) for m in SECTION_RE.finditer(body)]
    for i, (_s, e, heading) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(body)
        sections.setdefault(heading, body[e:end].strip())

    lede = sections.get("lede", "")
    when = sections.get("when to use", "")
    directing = sections.get("directing the ai", "")

    # Common mistakes: bullets, each its own row, so they are queryable.
    mistakes = []
    for line in sections.get("common mistakes", "").splitlines():
        m = re.match(r"^\s*[-*]\s+(.+)$", line)
        if m:
            mistakes.append(m.group(1).strip())

    # Cross-tool matrix. An empty params cell is NULL, never a default.
    params: list[dict] = []
    for tm, pv, ver, tested in TOOL_ROW_RE.findall(sections.get("cross-tool", "")):
        tool = tm.strip()
        if tool in ("tool", "---"):
            continue
        # Markdown inline-code fences are presentation, not content: the DB stores
        # the parameter string, not the backticks. `` `` `` means "nothing here",
        # which must land as NULL rather than as a two-backtick string.
        value = pv.strip().strip("`").strip()
        # A parameter string is `k=v | k=v | k=v`, so the pipes have to be escaped
        # to survive a markdown table cell. Undo it here; storing `\|` would put a
        # backslash into every tool parameter we ever send to a model.
        value = value.replace("\\|", "|").strip()
        if not value or set(value) <= set("-: "):
            value = ""
        params.append({
            "tool": tool,
            "params": value or None,
            "version_tag": (ver or "").strip() or None,
            "tested": 1 if tested.lower() == "yes" else 0,
        })

    citations = []
    src_text = sections.get("sources", "")
    # `[Title](url)` when the source gave a link, and `- Title` when it did not.
    # The Cinematique corpus lists its sources as plain text with no URL at all,
    # and storing a fabricated URL beside a real title would be the most damaging
    # thing this ingest could do. A source with no link is stored with url NULL.
    for i, (label, url) in enumerate(LINK_RE.findall(src_text)):
        if url.startswith("http"):
            citations.append({"ord": i, "title": label, "url": url})
    if not citations:
        for line in src_text.splitlines():
            m = re.match(r"^\s*[-*]\s+(.+)$", line)
            if m and len(m.group(1).strip()) > 8:
                citations.append({"ord": len(citations), "title": m.group(1).strip(),
                                  "url": None})

    related = []
    for label, target in LINK_RE.findall(sections.get("related", "")):
        rel = target.lstrip("./")
        related.append({"label": label, "target": rel})

    declared = []
    raw_styles = fm.get("styles", "")
    if raw_styles:
        inner = raw_styles.strip().strip("[]")
        declared = [s.strip() for s in re.split(r"[,，]", inner) if s.strip()]

    return {
        "slug": slug,
        "title": title,
        "category": category,
        "level": (fm.get("level") or "").strip() or None,
        "prompt_text": prompt_text,
        "prompt_slot": SLOT,
        "lede_text": lede or None,
        "when_to_use_text": when or None,
        "directing_text": directing or None,
        "image_url": (fm.get("image") or "").strip() or None,
        "video_url": (fm.get("video") or "").strip() or None,
        "mistakes": mistakes,
        "params": params,
        "citations": citations,
        "related": related,
        "declared_styles": declared,
        "source_path": path.relative_to(ROOT).as_posix(),
        "sha256": sha256(path),
        "bytes": path.stat().st_size,
    }


def ingest(conn, repo_root: Path = ROOT) -> dict:
    files = sorted(p for p in CATALOG.glob("*.md") if p.name != "README.md")
    if not files:
        return {"status": "absent", "techniques": 0}

    repo = conn.execute(
        "INSERT INTO catalog_repo(slug,url,license,local_path,description) VALUES(?,?,?,?,?)",
        ("cinematique", "data/cinematic", "authored in-repo",
         "data/cinematic", "Cinematic prompting techniques with a cross-tool matrix")).lastrowid

    parsed: list[dict] = []
    errors: list[str] = []
    for f in files:
        try:
            parsed.append(parse(f))
        except CatalogError as exc:
            errors.append(str(exc))
    if errors:
        # A controlled vocabulary and an intact slot are invariants, not warnings.
        raise CatalogError("\n".join(errors))

    # catalog_repo.head_sha is a tree hash: the digest of every file digest in
    # order, so it changes if and only if the corpus changed.
    tree = hashlib.sha256(
        "".join(f"{p['source_path']}:{p['sha256']}\n" for p in parsed).encode()).hexdigest()
    conn.execute("UPDATE catalog_repo SET head_sha=? WHERE id=?", (tree, repo))

    # register the authored files in source_file so the cross-corpus FK works
    file_ids: dict[str, int] = {}
    for p in parsed:
        row = conn.execute("SELECT id FROM source_file WHERE path=?", (p["source_path"],)).fetchone()
        if row:
            file_ids[p["source_path"]] = row[0]
        else:
            file_ids[p["source_path"]] = conn.execute(
                "INSERT INTO source_file(repo_id,path,sha256,bytes,role) VALUES(?,?,?,?,'catalog')",
                (_upstream_repo_id(conn), p["source_path"], p["sha256"], p["bytes"])).lastrowid

    style_by_key = {r[0]: r[1] for r in conn.execute("SELECT key, id FROM style")}
    # A `styles:` entry may name a shot card rather than a style. Cards are the
    # level a client buys and the level our pairings table declares at, so
    # resolving only against style keys silently dropped 51 of 155 declared
    # links while still exiting 0.
    #
    # Every variant of the card is recorded, not just the first. Picking MIN(id)
    # paired `crash-zoom-punch` — an 11-frame card — with `crash-impact-real`,
    # a 120-frame hold, which is confidently wrong and looks researched.
    style_by_card: dict[str, list[int]] = {}
    for card, sid in conn.execute("""
            SELECT sc.name, st.id FROM shot_card sc
            JOIN card_variant v ON v.card_id = sc.id
            JOIN style st ON st.id = v.style_id
            ORDER BY st.key"""):
        style_by_card.setdefault(card, []).append(sid)
    stats = {
        "techniques": 0, "mistakes": 0, "citations": 0,
        "cells_filled": 0, "cells_null": 0, "cells_tested": 0, "cells_unknown_tool": 0,
        "motions_declared": 0, "motions_unresolved": 0, "related_links": 0,
    }

    for p in parsed:
        p["_ingested_at"] = now_iso()
        cat_id = conn.execute("SELECT id FROM cinematic_category WHERE key=?",
                              (p["category"],)).fetchone()
        if not cat_id:
            raise CatalogError(f"{p['slug']}: category {p['category']} missing from the vocabulary")
        tid = conn.execute(
            "INSERT INTO cinematic_technique(name,title,category_id,level,prompt_text,prompt_slot,"
            "lede_text,when_to_use_text,directing_text,image_url,video_url,source_file_id)"
            " VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
            (p["slug"], p["title"], cat_id[0], p["level"], p["prompt_text"], p["prompt_slot"],
             p["lede_text"], p["when_to_use_text"], p["directing_text"],
             p["image_url"], p["video_url"], file_ids[p["source_path"]])).lastrowid
        stats["techniques"] += 1

        for i, text in enumerate(p["mistakes"]):
            conn.execute(
                "INSERT INTO technique_section(technique_id,kind,ord,text,is_critical)"
                " VALUES(?,'common_mistake',?,?,?)",
                (tid, i, text, int("critical" in text.lower() or "without" in text.lower())))
            stats["mistakes"] += 1

        for c in p["citations"]:
            conn.execute("INSERT INTO technique_citation(technique_id,ord,title,url) VALUES(?,?,?,?)",
                         (tid, c["ord"], c["title"], c["url"]))
            stats["citations"] += 1

        for key in p["declared_styles"]:
            sids = ([style_by_key[key]] if key in style_by_key
                    else style_by_card.get(key))
            if sids:
                for sid in sids:
                    conn.execute("INSERT OR IGNORE INTO technique_motion"
                                 "(technique_id,style_id,kind) VALUES(?,?,'declared')",
                                 (tid, sid))
                    stats["motions_declared"] += 1
            else:
                # Never infer: a name that does not resolve is recorded as a gap,
                # not silently attached to whatever was closest.
                stats["motions_unresolved"] += 1

        for tp in p["params"]:
            row = conn.execute("SELECT id FROM ai_tool WHERE key=?", (tp["tool"],)).fetchone()
            if not row:
                stats["cells_unknown_tool"] += 1
                continue
            # full_prompt is NULL when params is NULL. Composing "prompt + nothing"
            # would invent a second version of the prompt that nobody authored,
            # and an agent would not be able to tell it apart from a real one.
            full = f"{p['prompt_text']} {tp['params']}".strip() if tp["params"] else None
            conn.execute(
                "INSERT OR REPLACE INTO technique_tool_param(technique_id,tool_id,params,"
                "full_prompt,version_tag,tested,tested_at) VALUES(?,?,?,?,?,?,?)",
                (tid, row[0], tp["params"], full, tp["version_tag"], tp["tested"],
                 p["_ingested_at"] if tp["tested"] else None))
            if tp["params"]:
                stats["cells_filled"] += 1
                if tp["tested"]:
                    stats["cells_tested"] += 1
            else:
                stats["cells_null"] += 1

        for rel in p["related"]:
            target = rel["target"]
            if target.endswith(".md") and "wiki/cards/" in target:
                card = conn.execute("SELECT id FROM shot_card WHERE name=?",
                                    (Path(target).stem,)).fetchone()
                if card:
                    # curated: a shot-card link written by a human in a Related
                    # block is a stronger claim than a frontmatter `styles:` entry,
                    # which may name a style that was later renamed.
                    row = conn.execute(
                        "INSERT OR IGNORE INTO technique_motion(technique_id,style_id,kind)"
                        " VALUES(?,(SELECT id FROM style WHERE card_id=? LIMIT 1),'curated')"
                        " RETURNING style_id", (tid, card[0])).fetchone()
                    if row:
                        stats["motions_declared"] += 1
                    stats["related_links"] += 1
                else:
                    stats["related_links"] += 1
                    stats["motions_unresolved"] += 1
            else:
                stats["related_links"] += 1

    return {"status": "ok", "sha": tree, **stats}


def now_iso() -> str:
    from datetime import datetime, timezone
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _upstream_repo_id(conn) -> int | None:
    row = conn.execute("SELECT id FROM source_repo LIMIT 1").fetchone()
    return row[0] if row else None


def main() -> int:
    """Standalone run, for iterating on the catalog without a full ingest."""
    import sqlite3
    db = ROOT / "platform" / "db" / "shotcraft.db"
    if not db.exists():
        raise SystemExit("run platform/ingest/run.py first")
    conn = sqlite3.connect(db)
    for t in ("technique_tool_param", "technique_motion", "technique_citation",
              "technique_section", "cinematic_technique", "catalog_repo"):
        conn.execute(f"DELETE FROM {t}")
    conn.execute("DELETE FROM source_file WHERE role='catalog'")
    conn.commit()
    try:
        res = ingest(conn)
    except CatalogError as exc:
        print(f"catalog ingest FAILED:\n{exc}", file=sys.stderr)
        return 1
    conn.commit()
    print(json.dumps(res, indent=2))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())