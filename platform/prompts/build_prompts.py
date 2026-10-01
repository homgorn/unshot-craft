#!/usr/bin/env python3
"""platform/prompts/build_prompts.py — compile every shot card into a renderable brief.

    upstream tree -> shotcraft.db -> prompts/generated/<slug>.json

A "brief" is the thing you hand to a renderer or to an agent that will render:
everything needed to execute one shot, pre-joined, with a real normalized timeline.

Design rule, deliberately strict: **the brief is structure, the copy is a slot.**

The compiler never invents prose. Every string it emits is either a verbatim
upstream fragment (card frontmatter, a `## 动效核心` bullet, a `## 参数表` cell, a
`## 已知坑` line) or a literal marker. The one genuinely new thing this file
produces is the `beats[].window`: numeric [t0, t1] ranges scraped out of prose
like `seg(t, 0.55, 0.8, E.inOutCubic)`. That timeline is what makes a recipe
executable, and it exists nowhere upstream.

Pure function of the database. Delete the output tree, re-run, get it back.
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
DB = ROOT / "platform" / "db" / "shotcraft.db"
OUT = ROOT / "prompts" / "generated"

SCHEMA = "shotcraft.brief/1"
DEFAULT_FPS = 30
DEFAULT_W, DEFAULT_H = 1920, 1080

# Motion-section headings, in the order upstream uses them.
MOTION_KINDS = ("motion", "phases", "variants")

# --- prose scrapers -------------------------------------------------------
# seg(t, 0.55, 0.8, E.inOutCubic)   -> window (0.55, 0.8), ease "inOutCubic"
_SEG = re.compile(r"seg\(\s*t\s*,\s*(-?[\d.]+)\s*,\s*\+?(-?[\d.]+)(?:\s*,\s*(E\.\w+))?")
# t=0.06-0.56 / 0.3-2.6s           -> window, no easing named
_RANGE = re.compile(r"(\d\.\d+)\s*[–-]\s*(\d\.\d+)\s*s?\b")
_EASE = re.compile(r"\bE\.(\w+)")
_BEZIER = re.compile(r"bezier\(\s*([\d.]+)\s*,\s*([\d.]+)\s*,\s*([\d.]+)\s*,\s*([\d.]+)\s*\)")
# 126f / 150f @30fps                -> explicit frame budget
_FRAMES = re.compile(r"\b(\d{2,4})f\b")


def _window(text: str):
    """Best-effort normalized [t0, t1] from one bullet. None if not stated."""
    m = _SEG.search(text)
    if m:
        t0, t1 = float(m.group(1)), float(m.group(2))
        return [round(t0, 4), round(t1, 4)]
    m = _RANGE.search(text)
    if m:
        t0, t1 = float(m.group(1)), float(m.group(2))
        if 0 <= t0 < t1 <= 1.5:
            return [round(t0, 4), round(t1, 4)]
    return None


def _ease(text: str):
    m = _EASE.search(text)
    return m.group(1) if m else None


def _beats(sections: list[tuple[str, str, str]]) -> list[dict]:
    """One beat per motion-section bullet, keeping the bullet verbatim."""
    out: list[dict] = []
    ord_ = 0
    for heading, kind, body in sections:
        if kind not in MOTION_KINDS:
            continue
        for raw in body.splitlines():
            line = raw.strip().lstrip("-*").strip()
            if not line:
                continue
            beat = {
                "ord": ord_,
                "heading": heading,
                "window": _window(line),
                "frame_hints": _frame_hints(line),
                "ease": _ease(line),
                "beziers": [list(map(float, m.groups()))
                            for m in _BEZIER.finditer(line)],
                "raw": line,
            }
            out.append(beat)
            ord_ += 1
    return out


def _segments(conn: sqlite3.Connection, style_ids: list[int]) -> list[dict]:
    """Authoritative segment timing, taken from the demo source rather than prose.

    motion.py already extracted every `seg(...)` call into motion_param. But only
    some carry numbers: `from: "0" to: "0.14"` is executable, while
    `from: "FLY_AT[i]"` is symbolic and means "look it up in the file". Flagging
    that difference is the whole point - a renderer must not be handed `FLY_AT[i]`
    as if it were a number.
    """
    out: list[dict] = []
    for sid in style_ids:
        for r in conn.execute("""
            SELECT name, args_json, detail, line_no, raw FROM motion_param
            WHERE style_id=? AND kind='segment' ORDER BY line_no""", (sid,)):
            try:
                args = json.loads(r["args_json"])
            except (json.JSONDecodeError, TypeError):
                args = {}
            frm, to = str(args.get("from", "")), str(args.get("to", ""))
            concrete = _is_num(frm) and _is_num(to)
            out.append({
                "style_id": sid,
                "name": r["name"],
                "window": [float(frm), float(to)] if concrete else None,
                "from": frm, "to": to,
                "ease": args.get("ease"),
                "concrete": concrete,
                "line_no": r["line_no"],
                "raw": r["raw"],
            })
    return out


def _is_num(s: str) -> bool:
    try:
        float(s)
        return True
    except (TypeError, ValueError):
        return False


def _frame_hints(text: str) -> list[int]:
    """`126f` / `stagger 0.033（≈4f）` -> [126] / [4]. The corpus states timing in
    frames far more often than in normalized units (136 bullets vs ~45 ranges)."""
    return sorted({int(m) for m in _FRAMES.findall(text)})


def _copy_slots(card: dict, styles: list[dict]) -> dict:
    """Copy is authored by a human or an agent, never by this script."""
    slots = [{
        "id": "headline",
        "max_chars": 40,
        "hint": "One line. If a demo uses 2 title words, keep 2 words.",
        "status": "unfilled",
    }]
    if len(styles) > 1:
        slots.append({
            "id": "subtitle",
            "max_chars": 80,
            "hint": "Optional. Cards with N variants usually need a per-variant line.",
            "status": "unfilled",
        })
    return {
        "status": "unfilled",
        "authored": False,
        "note": ("Structure below is generated from the recipe. Copy is NOT. "
                 "Every slot must be filled before render, and a filled brief "
                 "must set authored=true and record who wrote it."),
        "slots": slots,
    }


def build_card(conn: sqlite3.Connection, slug: str) -> dict | None:
    card = conn.execute("""
        SELECT sc.*, c.key AS cat_key, c.label_en AS cat_en, c.label_zh AS cat_zh,
               c.label_ru AS cat_ru,
               e.key AS energy_key, e.label_zh AS energy_zh, e.label_en AS energy_en
        FROM shot_card sc
        JOIN category c ON c.id = sc.category_id
        LEFT JOIN energy_level e ON e.id = sc.energy_level_id
        WHERE sc.name = ?""", (slug,)).fetchone()
    if card is None:
        return None
    card = dict(card)

    sections = [(r[0], r[1], r[2]) for r in conn.execute(
        "SELECT heading, kind, body FROM card_section WHERE card_id=? ORDER BY ordinal",
        (card["id"],))]
    params = [dict(r) for r in conn.execute("""
        SELECT ordinal, variant_letter, param_key, typical_value, feel_note
        FROM card_param WHERE card_id=? ORDER BY ordinal""", (card["id"],))]
    pitfalls = [dict(r) for r in conn.execute("""
        SELECT ordinal, text, is_critical, rule_refs FROM card_pitfall
        WHERE card_id=? ORDER BY ordinal""", (card["id"],))]

    styles = []
    for r in conn.execute("""
        SELECT v.letter, v.label_zh, v.description_zh, s.key, s.demo_path,
               s.component_name, s.duration_frames, s.duration_source,
               s.uses_normalized_t, s.design_stage, s.gallery_style_key
        FROM card_variant v JOIN style s ON s.id = v.style_id
        WHERE v.card_id=? ORDER BY v.ordinal""", (card["id"],)):
        styles.append(dict(r))

    # Rules cited by this card's pitfalls, resolved.
    cited: dict[str, dict] = {}
    for p in pitfalls:
        for rid in (p.get("rule_refs") or "").split(","):
            rid = rid.strip()
            if not rid:
                continue
            rule = conn.execute(
                "SELECT rule_id, family, title, check_question FROM rule WHERE rule_id=?",
                (rid,)).fetchone()
            if rule:
                cited[rule["rule_id"]] = dict(rule)

    tags = [r[0] for r in conn.execute("""
        SELECT c.key FROM shot_card_tag t JOIN category c ON c.id=t.category_id
        WHERE t.card_id=? ORDER BY c.order_idx""", (card["id"],))]

    sha = conn.execute(
        "SELECT sha256 FROM source_file WHERE path=?",
        (card["source_path"],)).fetchone()

    frames = card["duration_frames"]
    window_frames = None
    if frames is None:
        m = _FRAMES.search(card["duration_text"] or "")
        window_frames = int(m.group(1)) if m else None

    return {
        "schema": SCHEMA,
        "slug": card["name"],
        "category": card["cat_key"],
        "category_label": {"en": card["cat_en"], "zh": card["cat_zh"], "ru": card["cat_ru"]},
        "tags": tags,
        "source": {
            "card": card["source_path"],
            "card_sha256": sha[0] if sha else None,
            "brief_kind": "generated",
        },
        "render": {
            "fps": DEFAULT_FPS,
            "duration_frames": frames,
            "duration_frames_hint": window_frames,
            "duration_verbatim": card["duration_text"],
            "width": DEFAULT_W,
            "height": DEFAULT_H,
            "energy": card["energy_key"],
            "energy_label": {"zh": card["energy_zh"], "en": card["energy_en"]},
            "energy_verbatim": card["energy_text"],
            "energy_rationale": card["energy_rationale"],
        },
        "intent_zh": card["intention_zh"],
        "use_zh": card["use_zh"],
        "summary_zh": card["summary_zh"],
        "beats": _beats(sections),
        "segments": _segments(conn, [r["id"] for r in conn.execute(
            "SELECT s.id FROM style s JOIN card_variant v ON v.style_id=s.id "
            "WHERE v.card_id=?", (card["id"],))]),
        "parameters": [
            {"ord": p["ordinal"], "variant": p["variant_letter"],
             "key": p["param_key"], "typical": p["typical_value"],
             "feel": p["feel_note"]}
            for p in params
        ],
        "pitfalls": [
            {"ord": p["ordinal"], "text": p["text"],
             "critical": bool(p["is_critical"]), "rules": p["rule_refs"]}
            for p in pitfalls
        ],
        "rules": sorted(cited.values(), key=lambda r: r["rule_id"]),
        "styles": [
            {"key": s["key"], "variant_letter": s["letter"],
             "upstream_key": s["gallery_style_key"],
             "demo": s["demo_path"], "component": s["component_name"],
             "duration_frames": s["duration_frames"],
             "duration_source": s["duration_source"],
             "uses_normalized_t": bool(s["uses_normalized_t"]),
             "design_stage": s["design_stage"],
             "label_zh": s["label_zh"], "description_zh": s["description_zh"]}
            for s in styles
        ],
        "copy": _copy_slots(card, styles),
    }


def build_all(conn: sqlite3.Connection) -> tuple[list[dict], list[str]]:
    slugs = [r[0] for r in conn.execute("SELECT name FROM shot_card ORDER BY name")]
    briefs, missing = [], []
    for slug in slugs:
        b = build_card(conn, slug)
        if b is None:
            missing.append(slug)
        else:
            briefs.append(b)
    return briefs, missing


# The reference set exists to show a range, not three variations on one theme.
# Below this the comparison the briefs exist for cannot be made.
MIN_REFERENCE_BRIEFS = 3


def lint(conn: sqlite3.Connection, briefs: list[dict]) -> list[str]:
    """Every authored brief must be complete. Machine briefs need no copy.

    A missing reference directory is a FAILURE, not an empty result. Returning
    no problems when there is nothing to check made this lint pass vacuously on
    a repo that had never written a single reference brief, which is the exact
    state the lint exists to catch.
    """
    problems: list[str] = []
    ref = ROOT / "prompts" / "reference"
    if not ref.is_dir():
        return [f"prompts/reference/ is missing: the reference briefs are the quality bar "
                f"for the {len(briefs)} generated ones, so with none written there is no bar"]
    paths = sorted(ref.glob("*.json"))
    if len(paths) < MIN_REFERENCE_BRIEFS:
        problems.append(f"prompts/reference/ holds {len(paths)} briefs, "
                        f"need at least {MIN_REFERENCE_BRIEFS} to show a range")
    for path in paths:
        try:
            b = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            problems.append(f"{path.name}: invalid JSON: {e}")
            continue
        if b.get("source", {}).get("brief_kind") != "hand":
            problems.append(f"{path.name}: source.brief_kind must be 'hand'")
        if not b.get("copy", {}).get("authored"):
            problems.append(f"{path.name}: copy.authored must be true")
        # A slot is satisfied by being filled OR by being explicitly omitted with
        # a reason. An omission with no reason is indistinguishable from an
        # unfinished brief, which is the failure mode worth catching.
        for s in b.get("copy", {}).get("slots", []):
            sid, status = s.get("id"), s.get("status")
            text = str(s.get("text") or "").strip()
            if status == "omitted":
                if not str(s.get("rationale") or "").strip():
                    problems.append(
                        f"{path.name}: slot {sid!r} is omitted with no rationale")
            elif status != "filled" or not text:
                problems.append(f"{path.name}: copy slot {sid!r} is {status!r}, "
                                f"not filled")
            elif not str(s.get("rationale") or "").strip():
                problems.append(f"{path.name}: filled slot {sid!r} has no rationale; "
                                f"the reference set is the quality bar, so an unexplained "
                                f"line is not a demonstration")
        slug = b.get("slug")
        row = conn.execute(
            "SELECT duration_frames FROM shot_card WHERE name=?", (slug,)).fetchone()
        if row is None:
            problems.append(f"{path.name}: slug {slug!r} is not a card")
        elif b.get("render", {}).get("duration_frames") != row[0]:
            problems.append(
                f"{path.name}: duration_frames {b.get('render', {}).get('duration_frames')} "
                f"!= card value {row[0]}")
        # The brief must cite the card it was derived from. A null hash is
        # allowed but has to say so, because a reference brief authored from the
        # render rather than the card is a weaker claim and must not hide.
        src = b.get("source", {})
        if not src.get("card"):
            problems.append(f"{path.name}: source.card is missing; a reference brief "
                            f"must name the card it was derived from")
        if src.get("card_sha256") is None and "card_sha256" in src \
                and "note" not in src and not src.get("provenance_declared"):
            problems.append(f"{path.name}: card_sha256 is null without a note explaining "
                            f"why the provenance is weaker than a hash")
    return problems


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(OUT))
    ap.add_argument("--lint", action="store_true",
                    help="validate prompts/reference/ briefs instead of building")
    args = ap.parse_args()

    if not DB.exists():
        print(f"no database at {DB}", file=sys.stderr)
        return 2
    conn = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row

    if args.lint:
        briefs, _ = build_all(conn)
        by_slug = {b["slug"]: b for b in briefs}
        del by_slug
        problems = lint(conn, briefs)
        for p in problems:
            print(f"LINT FAIL {p}")
        print(f"lint: {len(problems)} problem(s)")
        return 1 if problems else 0

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    briefs, missing = build_all(conn)

    for b in briefs:
        (out / f"{b['slug']}.json").write_text(
            json.dumps(b, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    index = {
        "schema": SCHEMA + "/index",
        "count": len(briefs),
        "generated_from": {
            "db": "platform/db/shotcraft.db",
            "cards": len(briefs),
            "fps": DEFAULT_FPS,
        },
        "notes": [
            "copy.authored is false everywhere in this tree by construction",
            "duration_frames is null for technique cards; see duration_frames_hint",
            "beats[].window is scraped from prose and is null when not stated",
        ],
        "briefs": [{
            "slug": b["slug"], "category": b["category"],
            "duration_frames": b["render"]["duration_frames"],
            "energy": b["render"]["energy"],
            "beats": len(b["beats"]), "parameters": len(b["parameters"]),
            "pitfalls": len(b["pitfalls"]), "styles": len(b["styles"]),
            "rules": len(b["rules"]), "tags": b["tags"],
        } for b in briefs],
    }
    (out / "index.json").write_text(
        json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    windowed = sum(1 for b in briefs if any(x["window"] for x in b["beats"]))
    framey = sum(1 for b in briefs if any(x["frame_hints"] for x in b["beats"]))
    segs = sum(len(b["segments"]) for b in briefs)
    concrete = sum(1 for b in briefs for s in b["segments"] if s["concrete"])
    print(f"wrote {len(briefs)} briefs to {out}")
    print(f"  duration_frames known    : "
          f"{sum(1 for b in briefs if b['render']['duration_frames'] is not None)}/{len(briefs)}")
    print(f"  prose beat with a window : {windowed}/{len(briefs)}")
    print(f"  prose beat with frame    : {framey}/{len(briefs)}")
    print(f"  demo segments extracted  : {segs} ({concrete} with literal numbers, "
          f"{segs - concrete} symbolic)")
    print(f"  unresolved cards         : {missing or 'none'}")
    print()
    print("  Honest coverage note: a normalized [t0,t1] timeline is NOT derivable")
    print("  for most cards. The corpus states timing in ~5 incompatible notations")
    print("  and only 44/218 demos contain literal seg() calls. The demos remain the")
    print("  authoritative implementation; prompts/reference/ briefs are where a")
    print("  real timeline gets written by hand.")
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())