"""Generate the LLM wiki and every index from shotcraft.db.

    python platform/wiki/build_wiki.py

Everything under wiki/ is generated. Editing it by hand is a bug: the next run
overwrites it. Source of truth is the DB, which is itself a pure function of the
pinned upstream tree.

Output:
  wiki/index.md            human navigation
  wiki/index.json          machine navigation (the site and the SaaS read this)
  wiki/llms.txt            llms.txt convention: index + links
  wiki/llms-full.txt       the whole corpus in one file, for RAG ingestion
  wiki/api/openapi.json    read-only HTTP contract for the future API
  wiki/domains/*.md        one document per knowledge domain
  wiki/cards/<name>.md     one page per shot recipe card (+ .json)
  wiki/stats.json          the numbers every other doc quotes
"""

from __future__ import annotations

import json
import re
import sqlite3
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DB = ROOT / "platform" / "db" / "shotcraft.db"
OUT = ROOT / "wiki"

UPSTREAM_URL = "https://github.com/Vincentwei1021/video-shotcraft"
UPSTREAM_SITE = "https://vincentwei1021.github.io/video-shotcraft"

DOMAINS = [
    ("overview", "What video-shotcraft is, what it ships, and the four layers"),
    ("cards", "The 157 shot recipe cards, indexed by category, energy and duration"),
    ("motion-grammar", "Easing curves, spring configs and timing primitives extracted from the demos"),
    ("methodology", "The production pipeline, the 27 aesthetic rules, the energy arc, sound and QA"),
    ("architecture", "How the upstream repo, the gallery site and the workbench fit together"),
    ("licensing", "Every licence in the stack and what it allows or blocks"),
    ("landscape", "The sibling skill, the tools, the channels, and the upstream author"),
    ("monetization", "Revenue models, ranked by time to first dollar, with the evidence"),
    ("glossary", "Motion-design vocabulary as used by these cards, with card references"),
    ("cinematic", "The cinematic-technique catalog: what to shoot, and how to say it per tool"),
]


def esc(s: str | None) -> str:
    return (s or "").replace("|", "\\|").replace("\n", " ").strip()


def clip(text: str | None, n: int) -> str:
    t = (text or "").replace("\n", " ").strip()
    return t if len(t) <= n else t[: n - 1].rstrip() + "…"


def main() -> int:
    if not DB.exists():
        print(f"missing {DB}; run platform/ingest/run.py first", file=sys.stderr)
        return 1
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    # Accepts either Q(sql, id) or Q(sql, (id,)): flatten a single tuple so a
    # stray comma at a call site cannot silently bind a tuple as one parameter.
    def Q(sql, *a):
        params = a[0] if len(a) == 1 and isinstance(a[0], (tuple, list)) else (a or ())
        return [dict(r) for r in conn.execute(sql, params).fetchall()]

    (OUT / "cards").mkdir(parents=True, exist_ok=True)
    (OUT / "domains").mkdir(parents=True, exist_ok=True)
    (OUT / "api").mkdir(parents=True, exist_ok=True)

    repo = Q("SELECT * FROM source_repo LIMIT 1")[0]
    run = Q("SELECT * FROM ingest_run ORDER BY id DESC LIMIT 1")[0]
    cats = Q("SELECT * FROM category ORDER BY order_idx")
    stats = {
        "upstream_sha": repo["head_sha"],
        "upstream_stars": repo["stars"],
        "upstream_forks": repo["forks"],
        "upstream_license": repo["license"],
        "cards": Q("SELECT COUNT(*) n FROM shot_card")[0]["n"],
        "styles": Q("SELECT COUNT(*) n FROM style")[0]["n"],
        "styles_registered": Q("SELECT COUNT(*) n FROM style WHERE registered=1")[0]["n"],
        "media_previews": Q("SELECT COUNT(*) n FROM style_media WHERE kind='preview'")[0]["n"],
        "media_present_locally": Q("SELECT COUNT(*) n FROM style_media WHERE kind='poster' AND present=1")[0]["n"],
        "card_params": Q("SELECT COUNT(*) n FROM card_param")[0]["n"],
        "pitfalls": Q("SELECT COUNT(*) n FROM card_pitfall")[0]["n"],
        "pitfalls_critical": Q("SELECT COUNT(*) n FROM card_pitfall WHERE is_critical=1")[0]["n"],
        "motion_params": Q("SELECT COUNT(*) n FROM motion_param")[0]["n"],
        "easing_curves": Q("SELECT COUNT(*) n FROM easing_curve")[0]["n"],
        "rules": Q("SELECT COUNT(*) n FROM rule")[0]["n"],
        "method_docs": Q("SELECT COUNT(*) n FROM method_doc")[0]["n"],
        "sfx": Q("SELECT COUNT(*) n FROM audio_asset WHERE kind='sfx'")[0]["n"],
        "bgm": Q("SELECT COUNT(*) n FROM audio_asset WHERE kind='bgm'")[0]["n"],
        "audio_untraceable": Q("SELECT COUNT(*) n FROM audio_asset WHERE traceable=0")[0]["n"],
        "locales": Q("SELECT COUNT(*) n FROM locale")[0]["n"],
        "translations": Q("SELECT COUNT(*) n FROM translation")[0]["n"],
        "opportunities": Q("SELECT COUNT(*) n FROM opportunity")[0]["n"],
        "files_indexed": run["files_seen"],
        "generated_from": "platform/db/shotcraft.db",
    }

    # ---------------------------------------------------------------- cards
    card_rows = Q("""
        SELECT s.*, c.key cat_key, c.label_en cat_en, c.label_zh cat_zh,
               e.label_zh energy_zh, e.label_en energy_en, e.rank energy_rank
        FROM shot_card s
        JOIN category c ON c.id = s.category_id
        LEFT JOIN energy_level e ON e.id = s.energy_level_id
        ORDER BY c.order_idx, s.name""")
    tr = {(r["code"], r["ns"], r["key"]): r["text"] for r in Q("SELECT l.code, t.ns, t.key, t.text FROM translation t JOIN locale l ON l.id=t.locale_id")}
    styles_by_card = defaultdict(list)
    for r in Q("""SELECT v.card_id, s.key, s.demo_path, s.component_name, s.duration_frames,
                          s.family, v.letter FROM card_variant v JOIN style s ON s.id=v.style_id ORDER BY s.key"""):
        styles_by_card[r["card_id"]].append(r)
    params_by_card = defaultdict(list)
    for r in Q("SELECT card_id, param_key, typical_value, feel_note FROM card_param ORDER BY card_id, ordinal"):
        params_by_card[r["card_id"]].append(r)
    pitfalls_by_card = defaultdict(list)
    for r in Q("SELECT card_id, text, is_critical, rule_refs FROM card_pitfall ORDER BY card_id, ordinal"):
        pitfalls_by_card[r["card_id"]].append(r)
    sections_by_card = defaultdict(list)
    for r in Q("SELECT card_id, heading, kind FROM card_section ORDER BY card_id, ordinal"):
        sections_by_card[r["card_id"]].append(r)

    card_index = []
    for card in card_rows:
        name = card["name"]
        zh_desc = tr.get(("zh", "card", name)) or card["summary_zh"]
        en_desc = tr.get(("en", "card", name)) or name
        styles = styles_by_card.get(card["id"], [])
        entry = {
            "name": name,
            "category": card["cat_key"],
            "category_en": card["cat_en"],
            "summary_zh": zh_desc,
            "summary_en": en_desc,
            "intention": card["intention_zh"],
            "use": card["use_zh"],
            "duration_frames": card["duration_frames"],
            "duration_text": card["duration_text"],
            "energy": card["energy_zh"] or card["energy_text"].split("（")[0].strip(),
            "energy_rank": card["energy_rank"],
            "energy_text": card["energy_text"],
            "styles": [s["key"] for s in styles],
            "tags": [r["key"] for r in Q(
                "SELECT c.key FROM shot_card_tag t JOIN category c ON c.id=t.category_id WHERE t.card_id=?",
                card["id"])],
            "params": [p["param_key"] for p in params_by_card.get(card["id"], [])],
            "pitfall_count": len(pitfalls_by_card.get(card["id"], [])),
            "critical_pitfalls": sum(1 for p in pitfalls_by_card.get(card["id"], []) if p["is_critical"]),
            "source": f"{UPSTREAM_URL}/blob/main/references/shots/{card['cat_key']}/{name}.md",
            "demo": card["source_path"],
            "demo_urls": [f"{UPSTREAM_SITE}/library.html#{name}"],
            "wiki": f"wiki/cards/{name}.md",
        }
        card_index.append(entry)

        # per-card page
        L = [f"# {name}", "",
             f"> One of {stats['cards']} shot recipe cards in video-shotcraft. "
             f"Machine index: `wiki/index.json#/cards/{name}`.",
             "", "## Identity", "",
             f"- **slug**: `{name}` (join key across cards, demos, media and deep links)",
             f"- **category**: `{card['cat_key']}` — {card['cat_en']} / {card['cat_zh']}",
             f"- **energy**: `{card['energy_zh'] or card['energy_text'].split('（')[0].strip()}`"
             + (f" — rank {card['energy_rank']}/8" if card["energy_rank"] else " — arc or n/a, not sortable"),
             f"- **suggested duration**: {esc(card['duration_text'])}"
             + (f" → **{card['duration_frames']} frames @30fps = {card['duration_frames']/30:.1f}s**"
                if card["duration_frames"] else " → not a timed card (technique card)"),
             f"- **cross-category tags**: {', '.join('`'+t+'`' for t in entry['tags'])}",
             f"- **upstream source**: {card['source_path']}",
             ""]
        if styles:
            L += ["## Variants (styles)", "",
                  "| letter | style key | duration | family | demo |",
                  "|---|---|---|---|---|"]
            for s in styles:
                L.append(f"| {s['letter'] or '—'} | `{s['key']}` | "
                         f"{s['duration_frames'] or '—'}f | {s['family']} | `{s['demo_path']}` |")
            L += [""]
        L += ["## What it does", "", clip(card["summary_zh"], 600), "",
              "**When to use it.** " + clip(card["use_zh"], 400), "",
              "**Why this shot earns its place.** " + clip(card["intention_zh"], 700), ""]
        plist = params_by_card.get(card["id"], [])
        if plist:
            L += ["## Parameters", "",
                  "| parameter | typical value | how to tune |", "|---|---|---|"]
            for p in plist:
                L.append(f"| {esc(p['param_key'])} | {esc(p['typical_value'])} | {clip(p['feel_note'], 180)} |")
            L.append("")
        pit = pitfalls_by_card.get(card["id"], [])
        if pit:
            L += ["## Known pitfalls", ""]
            for p in pit:
                flag = " **[命门]**" if p["is_critical"] else ""
                refs = f" _(rules {p['rule_refs']})_" if p["rule_refs"] else ""
                L.append(f"- {clip(p['text'], 320)}{flag}{refs}")
            L.append("")
        secs = sections_by_card.get(card["id"], [])
        L += ["## Card structure", "",
              " | ".join(f"`{s['kind']}`" for s in secs), "",
              "**Implementations**"]
        L += [f"- `{p}`" for p in (s["demo_path"] for s in styles)] or ["- (see upstream card)"]
        L += ["", "---", "",
              f"Generated from `platform/db/shotcraft.db` @ `{repo['head_sha'][:12]}`. "
              f"Do not edit: regenerate with `python platform/wiki/build_wiki.py`.", ""]
        (OUT / "cards" / f"{name}.md").write_text("\n".join(L), encoding="utf-8")
        (OUT / "cards" / f"{name}.json").write_text(
            json.dumps(entry, ensure_ascii=False, indent=2), encoding="utf-8")

    # ------------------------------------------------------- domain: cards
    lines = [f"# Shot recipe cards", "",
             f"{stats['cards']} cards across {len(cats)} categories, "
             f"{stats['styles']} motion styles, {stats['card_params']} documented parameters, "
             f"{stats['pitfalls']} pitfalls. Every row links to a per-card page.", "",
             "## How to choose a card", "",
             "1. Pick the narrative beat (open / feature / transition / close) — that is the category.",
             "2. Read the energy ladder: the film opens low, alternates mid-high with breath beats, "
             "peaks at the outro (`references/sequences/promo-energy-arc.md`).",
             "3. Check `duration_frames`: a card longer than ~150f needs a breath beat after it.",
             "4. Read the card's known pitfalls before wiring it in — the budget rules (≤2 crash zooms, "
             "≤2 light effects per film) are hard limits, not suggestions.",
             "5. Copy the referenced demo TSX rather than rewriting it: the tuned easing and timing "
             "ratios in the demo are the truth; the card only states the intent.", ""]
    for cat in cats:
        rows = [c for c in card_index if c["category"] == cat["key"]]
        if not rows:
            continue
        lines += [f"## {cat['label_en']} / {cat['label_zh']} / {cat['label_ru']}  (`{cat['key']}`, {len(rows)} cards)", "",
                  "| card | energy | frames | styles | params | pitfalls | summary |",
                  "|---|---|---|---|---|---|---|"]
        for c in sorted(rows, key=lambda r: (-(r["energy_rank"] or 0), r["name"])):
            lines.append(
                f"| [`{c['name']}`](cards/{c['name']}.md) | {c['energy']} | "
                f"{c['duration_frames'] or '—'} | {len(c['styles'])} | {len(c['params'])} | "
                f"{c['pitfall_count']}{' ⚠' if c['critical_pitfalls'] else ''} | {clip(c['summary_zh'], 110)} |")
        lines.append("")
    (OUT / "domains" / "cards.md").write_text("\n".join(lines), encoding="utf-8")

    # ------------------------------------------------ domain: motion grammar
    top_curves = Q("SELECT * FROM easing_curve ORDER BY usage_count DESC LIMIT 20")
    springs = Q("""SELECT s.key style, p.args_json, p.detail, p.line_no, p.raw
                   FROM motion_param p JOIN style s ON s.id=p.style_id
                   WHERE p.kind='spring' ORDER BY s.key""")
    kind_counts = Q("SELECT kind, COUNT(*) n FROM motion_param GROUP BY kind ORDER BY n DESC")
    fam = Q("SELECT family, COUNT(*) n FROM style GROUP BY family")
    dur = Q("""SELECT MIN(duration_frames) mn, MAX(duration_frames) mx, AVG(duration_frames) av,
                     SUM(CASE WHEN duration_frames IS NULL THEN 1 ELSE 0 END) missing FROM style""")
    famA = [r["n"] for r in fam if r["family"] == "A"][0]
    famB = [r["n"] for r in fam if r["family"] == "B"][0]
    lines = ["# Motion grammar", "",
             "This is the part of video-shotcraft that exists **only** as literals inside "
             "`demos/**/*.tsx`: the tuned curves, springs and timing windows. Nothing upstream indexes "
             f"it. We extracted {stats['motion_params']} parameter occurrences across {stats['styles']} demos.", "",
             "## Two demo families", "",
             f"- **Family A ({famA} demos)** — the Motion lab. Normalized progress `t ∈ [0,1]` derived from "
             "`useCurrentFrame()` only, a 480×270 `DesignStage` design space, and a shared easing table `E`. "
             "Lengthening a clip *slows* the animation instead of truncating it.",
             f"- **Family B ({famB} demos)** — frame-driven. "
             "`interpolate(frame, [frames], [values], {easing, clamp})` "
             "plus Remotion's `spring({frame, fps, config})`. Absolute frame math.", "",
             "Both are deterministic by rule 9 of SKILL.md: no `Date.now()`, no unseeded `Math.random()`.", "",
             "## The house easing curve", "",
             f"{stats['easing_curves']} distinct bezier curves are used. The dominant one is the de-facto "
             "house style — reach for it first when writing a new shot:", "",
             "| curve | styles using it | overshoot |", "|---|---|---|"]
    for c in top_curves:
        lines.append(f"| `{c['spec']}` | {c['usage_count']} | {'yes (y1>1)' if c['overshoot'] else 'no'} |")
    lines += ["",
              "Overshoot curves (`y1 > 1`) are the ones that produce the springy settle; the repo treats "
              "them as a cost, not a default — a shot gets **one** overshoot beat, not a bouncing loop.", "",
              "## Spring configs observed", "",
              "| style | damping | stiffness | mass | frames |", "|---|---|---|---|---|"]
    for s in springs:
        a = json.loads(s["args_json"])
        lines.append(f"| `{s['style']}` | {a.get('damping', '—')} | {a.get('stiffness', '—')} | "
                     f"{a.get('mass', '—')} | {a.get('durationInFrames', '—')} |")
    lines += ["",
              "Modal cluster: damping 9–16, stiffness 60–260, mass 0.6–1.1. "
              "`damping ≤ 10` with `stiffness ≥ 200` reads as a hard mechanical snap; "
              "`damping ≥ 15` with `stiffness ≈ 90` reads as a heavy object settling.", "",
              "## Timing envelope", "",
              f"Durations across all demos: min {dur[0]['mn']}f, max {dur[0]['mx']}f, "
              f"mean {dur[0]['av']:.0f}f, {dur[0]['missing']} demos with no discoverable constant.", "",
              "The hard holds that must survive translation into any new film:", "",
              "- brand wordmark settle ≥ 1s (30f) — rule R1",
              "- batch motion tail 0.5s (15f) still — rule R3",
              "- opening hero action arc ≥ 3s — rule R3",
              "- beat-sync cut error ≤ 3 frames after render, measured against the extracted audio track", "",
              "## Parameter kinds found", "", "| kind | count | what it is |", "|---|---|---|"]
    KIND_DOC = {
        "interpolate": "`interpolate(input, inputRange, outputRange, opts)` — the frame-driven workhorse",
        "easing_fn": "`Easing.in/out/inOut(Easing.base)`",
        "segment": "`seg(t, t0, t1, E.x)` — the family-A equivalent of interpolate",
        "bezier": "`Easing.bezier(x1,y1,x2,y2)`",
        "spring": "Remotion `spring({frame, fps, config})`",
        "easing_const": "a module-scope easing constant, resolved before use",
        "easing_name": "a named curve from the shared table, e.g. `E.outCubic`",
        "helper": "a shared `Motion.tsx` helper call: `lerp` / `rand`",
        "exp_decay": "`Math.exp(...)` shake/decay envelopes",
        "motion_blur": "`<CameraMotionBlur shutterAngle samples>`",
        "sin": "`Math.sin(...)` oscillation",
        "constant": "exported duration/frame constants",
        "color": "named palette constants such as `BG`, `ACCENT`",
    }
    for k in kind_counts:
        lines.append(f"| `{k['kind']}` | {k['n']} | {KIND_DOC.get(k['kind'], '')} |")
    (OUT / "domains" / "motion-grammar.md").write_text("\n".join(lines), encoding="utf-8")

    # ------------------------------------------------- domain: methodology
    docs = Q("SELECT * FROM method_doc ORDER BY slug")
    rules = Q("SELECT * FROM rule ORDER BY family, rule_id")
    byfam = defaultdict(list)
    for r in rules:
        byfam[r["family"]].append(r)
    FAM_DOC = {"R": "rhythm and holds", "Q": "texture, camera, composition",
               "S": "sound", "C": "copy", "P": "process"}
    lines = ["# Methodology", "",
             "The part of the repo that makes it a production discipline rather than a component "
             "library. Four documents plus the ruling law.", "",
             "## Documents", ""]
    for d in docs:
        lines.append(f"### `{d['slug']}.md` — {d['purpose'] or 'see upstream'}")
        lines.append("")
        heads = json.loads(d["headings_json"] or "[]")
        lines.append("Sections: " + ", ".join(f"`{h}`" for h in heads[:14]) + ("…" if len(heads) > 14 else ""))
        lines.append("")
    lines += ["## The ruling law: aesthetic-rules.md", "",
              f"{len(rules)} numbered precedents in five families. IDs are append-only upstream and must "
              "never be renumbered — they are cited from the shot cards, so a renumber silently breaks "
              "every cross-reference.", ""]
    for fam in sorted(byfam):
        lines += [f"### Family {fam} — {FAM_DOC.get(fam, '')} ({len(byfam[fam])} rules)", "",
                  "| id | title |", "|---|---|"]
        for r in byfam[fam]:
            lines.append(f"| `{r['rule_id']}` | {clip(r['title'] or r['body'], 150)} |")
        lines.append("")
    lines += ["## The energy arc", "",
              "`references/sequences/promo-energy-arc.md` is the default whole-film skeleton for a "
              "30–60s multi-feature web product promo:", "",
              "| stage | share | energy | duty |", "|---|---|---|---|"]
    for s in Q("""SELECT st.ordinal, st.label_zh, st.label_en, st.duration_pct, st.energy, st.duty
                  FROM sequence_stage st JOIN sequence_stage_candidate c ON c.stage_id=st.id
                  WHERE c.template_id=(SELECT id FROM sequence_template LIMIT 1)
                  GROUP BY st.ordinal ORDER BY st.ordinal"""):
        lines.append(f"| {s['ordinal']} {s['label_en']} | {s['duration_pct'] or '—'} | {s['energy'] or '—'} | {esc(s['duty'])} |")
    lines += ["", "Rule of thumb the cards repeat: **open low, alternate mid-high with breath beats, "
              "peak at the outro.** Historical feedback in the repo only ever asked for slower/hold "
              "longer; there is no 'too slow' precedent.", ""]
    (OUT / "domains" / "methodology.md").write_text("\n".join(lines), encoding="utf-8")

    # ------------------------------------------------ domain: architecture
    top_dirs = Q("""SELECT path FROM source_file WHERE role IN ('card','demo','reference','component','site','asset','sequence','config','ci','doc','other')
                     ORDER BY length(path) LIMIT 0""")
    role_counts = Q("SELECT role, COUNT(*) n, SUM(bytes) bytes FROM source_file GROUP BY role ORDER BY n DESC")
    lines = ["# Architecture of the upstream repo", "",
             "video-shotcraft is four coupled layers plus a distribution layer. Every downstream product "
             "we build sits *beside* this, never inside it.", "",
             "| layer | path | role |", "|---|---|---|",
             "| knowledge | `SKILL.md` + `references/` | the agent's entry point: 3 production modes, 9 hard rules, "
             "157 cards, 27 aesthetic rules, the pipeline |",
             "| implementation | `demos/**/*.tsx` + `assets/lib/` | the tuned truth: one TSX per motion style, "
             "plus reusable components (PageCam, ClipCard, DigitRoll, Caption, FlashCut) |",
             "| runnable | `template/` + `workbench/` | the validated 36.2s Ink Press film (10 shots) and a "
             "CapCut-style browser timeline editor on port 5198 |",
             "| distribution | `gallery/` | the static site: 157 cards, 214 previews, 2 locales, SEO prerender |",
             "| delivery | `jianying-export/` | export the finished film as an editable CapCut CN draft |", "",
             "## The join keys", "",
             "- `name` (card slug) — identical across `references/shots/<cat>/<name>.md`, "
             "`gallery/source/<name>.md`, `library.json.cards[].name`, the demo directory, and the "
             "`library.html#<name>` deep link.",
             "- `key` (style slug) — kebab-case of the demo TSX basename, equal to "
             "`media/<key>.mp4` and `media/poster/<key>.jpg`.", "",
             "## Gallery build pipeline", "",
             "```",
             "references/shots/*.md ──sync-from-cards.py──> gallery/source/*.md + gallery/api/library.json",
             "                             ──build-seo.py────> sitemap.xml, llms.txt, library.html prerender",
             "             ──deploy-pages.yml───────> GitHub Pages (+ mp4s from the gallery-media release)",
             "```", "",
             "Note: **the mp4 previews are not in git.** They are downloaded from the `gallery-media` "
             "GitHub release at deploy time. A local checkout has zero previews; the 66 poster jpgs are "
             "in the tree. Any mirror of the site must fetch the release.", "",
             "## Upstream i18n today", "",
             "Three independent mechanisms, all inline, none shared:", "",
             "1. `gallery/translations.js` → `window.GALLERY_I18N` with `ui` (zh/en) plus flat maps "
             "`cardsZh/cardsEn/stylesZh/stylesEn` (157 + 157 + 214 + 214 entries).",
             "2. `gallery/index.html` → its own inline `L10N` object, 11 keys, applied via `data-l10n` "
             "and `innerHTML`.",
             "3. `gallery/showcase.js` → its own `SHOWCASE_L10N`, 19 keys, `data-i18n`.", "",
             "Locale lives in `localStorage`, not in the URL — so there is no indexable per-language URL, "
             "no `hreflang`, and no way for a crawler or a link to reach the Russian library. "
             "Fixing that is our first site change (ADR-0004).", "",
             "## Repository composition (files indexed: %d)" % stats["files_indexed"], "",
             "| role | files |", "|---|---|"]
    for r in role_counts:
        lines.append(f"| `{r['role']}` | {r['n']} |")
    (OUT / "domains" / "architecture.md").write_text("\n".join(lines), encoding="utf-8")

    # ------------------------------------------------- domain: licensing
    lic = Q("SELECT * FROM license_registry ORDER BY blocking DESC, subject")
    lines = ["# Licensing", "",
             "The stack is not uniformly free. Before anything is sold or published, this is the table "
             "that decides it.", "",
             "| subject | licence | commercial use | blocks us | obligation |", "|---|---|---|---|---|"]
    for l in lic:
        lines.append(f"| {l['subject']} | {l['spdx']} | `{l['commercial_use']}` | "
                     f"{'**yes**' if l['blocking'] else 'no'} | {l['obligation'] or '—'} |")
    untrace = Q("SELECT path, note FROM audio_asset WHERE traceable=0")
    lines += ["", "## Audio audit", "",
              f"{stats['sfx']} SFX across 16 scene categories and {stats['bgm']} BGM tracks, all Mixkit free licence. "
              f"`assets/audio/ATTRIBUTION.md` records the source of every file at download time "
              "(the rule there is: record it when you fetch it, you cannot reverse-look-it-up later).", ""]
    if untrace:
        lines += [f"**{len(untrace)} files are marked untraceable (无法反查) and must not ship in a "
                  "commercial delivery until re-sourced:**", ""]
        lines += [f"- `{r['path']}`" for r in untrace]
        lines.append("")
    lines += ["## What this means for us", "",
              "- The **core is Apache-2.0**: fork, modify, sell services built on it. Keep the copyright "
              "and add a NOTICE when redistributing.",
              "- **Remotion's paid tier applies to companies above three people, not to "
              "individuals.** This repo is rendered by an individual, so the free tier applies and "
              "`platform/render/run.py` runs; see `render/out/` and "
              "`platform/render/render_report.json`. A client deliverable rendered *for a company* "
              "has to price the licence in, or the client buys it — which is a pricing question, not "
              "a legal one.",
              "- **The distinction is which kind of fact it is.** A licence term binds whoever ships "
              "the code. A free tier is a fact about who is running it. Collapsing the two is how a "
              "project refuses to build something it is allowed to build — or, worse, ships something "
              "it is not.",
              "- **video-talkcraft is PolyForm Noncommercial.** We can read it for ideas and port techniques "
              "(upstream already did: 19 cards were ported across), but we cannot ship it or build a "
              "product on it commercially without authorisation. This one *is* a hard constraint.",
              "- **Tracked-out audio** is the quietest risk: 5 files with no traceable source "
              "(`commercial_ok = 0`). Replace them before a client-facing delivery rather than "
              "arguing about it later.", ""]
    (OUT / "domains" / "licensing.md").write_text("\n".join(lines), encoding="utf-8")

    # ------------------------------------------------- domain: landscape
    actors = Q("SELECT * FROM actor ORDER BY stars DESC NULLS LAST")
    channels = Q("SELECT * FROM source_channel ORDER BY id")
    lines = ["# Landscape", "",
             "## Actors", "", "| name | kind | stars | licence | positioning |", "|---|---|---|---|---|"]
    for a in actors:
        lines.append(f"| [{a['name']}]({a['url'] or ''}) | `{a['kind']}` | {a['stars'] or '—'} | "
                     f"{a['license'] or '—'} | {clip(a['positioning'], 160)} |")
    lines += ["", "## Distribution channels observed", "",
              "These are the surfaces that already carry the skill. They are also the surfaces a fork "
              "has to exist on to be found.", "", "| channel | kind | reach signal |", "|---|---|---|"]
    for c in channels:
        lines.append(f"| [{c['name']}]({c['url']}) | `{c['kind']}` | {c['reach'] or '—'} |")
    star_rows = Q("SELECT name, stars FROM actor WHERE stars IS NOT NULL ORDER BY stars DESC")
    lines += ["", "## Traction", "",
              f"- Upstream: **{repo['stars']:,} stars / {repo['forks']:,} forks**, Apache-2.0, "
              f"{run['files_seen']} tracked files. That fork:star ratio (~{repo['forks']/repo['stars']*100:.0f}%) "
              "is the tell: people install it, they don't just bookmark it.",
              "- Sibling video-talkcraft: 1.3k stars / 126 forks, but a *non-commercial* licence — "
              "the author chose to fence the newer installment.",
              "- The install path is one command: `npx skills add Vincentwei1021/video-shotcraft`. "
              "Distribution is the skill registry, not a website.", ""]
    (OUT / "domains" / "landscape.md").write_text("\n".join(lines), encoding="utf-8")

    # ------------------------------------------------- domain: monetization
    opps = Q("SELECT * FROM opportunity ORDER BY time_to_first_revenue")
    lines = ["# Monetization", "",
             "Five models, ranked by time to first dollar rather than by ceiling. The evidence column is "
             "in `platform/db/shotcraft.db#/opportunity` and every number is traceable.", "",
             "| key | model | effort | first revenue | status |", "|---|---|---|---|---|"]
    for o in opps:
        lines.append(f"| `{o['key']}` | {o['revenue_model']} | {o['effort']} | {o['time_to_first_revenue']} | {o['status']} |")
    for o in opps:
        ev = json.loads(o["evidence"] or "{}")
        lines += ["", f"## {o['title']}  (`{o['key']}`)", "", o["thesis"], "",
                  f"- **model**: {o['revenue_model']} · **effort**: {o['effort']} · "
                  f"**first revenue**: {o['time_to_first_revenue']}",
                  f"- **depends on**: {o['depends_on'] or 'nothing'}",
                  "- **evidence**: " + ", ".join(f"{k}={v}" for k, v in ev.items()), ""]
    lines += ["## What we are not doing", "",
              "- **Not selling the core.** Apache-2.0 means anyone can sell a fork; our advantage has to "
              "be something a fork cannot copy — a rendered film, a supported pipeline, or a language "
              "nobody else bothered to translate.",
              "- **Not competing on stars.** Upstream has 10.1k and a fast-moving release cadence. A fork "
              "chases upstream forever and loses.",
              "- **Not touching video-talkcraft commercially.** PolyForm Noncommercial. Reading is fine; "
              "shipping is not.", ""]
    (OUT / "domains" / "monetization.md").write_text("\n".join(lines), encoding="utf-8")

    # ------------------------------------------------- domain: glossary
    cards_text = " ".join(f"{c['name']} {c['summary_zh']}" for c in card_index)
    terms = ["入场", "落位", "hold", "呼吸位", "动作弧", "错峰", "摘罩", "条件挂载", "过渡", "硬切",
             "藏切点", "甩镜", "配光", "聚光", "晕染", "过冲", "回弹", "刹车", "蓄力", "弹簧",
             "阻尼回摆", "指数衰减", "逐词", "逐字", "打字机", "翻牌", "字距", "压印",
             "视差", "环绕", "荷兰角", "俯拍", "升降臂", "子弹时间", "俯冲", "缓动", "曲线",
             "幕底", "字卡", "呼吸光", "真静止", "顿挫", "频闪", "变速", "卡点", "拍点", "重心"]
    lines = ["# Glossary", "",
             "The cards write in a specific motion-design vocabulary. These are the load-bearing terms, "
             "with the cards that use them. Translations must keep the term consistent across all 9 "
             "locales or the wiki and the site drift apart.", "",
             "| term | what it means here | cards using it |", "|---|---|---|"]
    card_by_text = {}
    for c in card_index:
        card_by_text[c["name"]] = f"{c['name']} {c['summary_zh']} {c['use'] or ''} {c['intention'] or ''}"
    for t in terms:
        hits = [n for n, txt in card_by_text.items() if t in txt]
        if not hits:
            continue
        lines.append(f"| {t} | {'see the card page for the authoritative description'} | "
                     + ", ".join(f"`{h}`" for h in hits[:6]) + (f" (+{len(hits)-6} more)" if len(hits) > 6 else "") + " |")
    (OUT / "domains" / "glossary.md").write_text("\n".join(lines), encoding="utf-8")

    # ------------------------------------------------- domain: cinematic (F072)
    cat_rows = Q("SELECT t.*, cc.key cat_key, cc.label_en cat_label FROM cinematic_technique t"
                 " JOIN cinematic_category cc ON cc.id=t.category_id"
                 " ORDER BY cc.sort_order, t.name")
    if cat_rows:
        pair_total = Q("SELECT COUNT(*) n FROM technique_motion")[0]["n"]
        pair_techs = Q("SELECT COUNT(DISTINCT technique_id) n FROM technique_motion")[0]["n"]
        cell = Q("""SELECT SUM(p.params IS NOT NULL) filled, SUM(p.tested=1) tested,
                           SUM(p.params IS NULL) nulls, COUNT(*) listed
                    FROM technique_tool_param p""")[0]
        tcount = len(cat_rows)
        videos = sum(1 for r in cat_rows if r["video_url"])
        lines = [
            "# Cinematic techniques", "",
            f"A second corpus: **{tcount} techniques** that answer *what to shoot*, "
            f"complementing the {stats['cards']} shot cards that answer *how it moves*. "
            "Same DB, same join keys, same generated-from-the-DB rule (ADR 0007).", "",
            "| stage | corpus | answers |",
            "|---|---|---|",
            "| 1 | `data/cinematic/` | **what to shoot** — camera, light, composition, editing rhythm, genre |",
            "| 2 | `references/shots/` | **how it moves** — easing, spring, timing, render duration |",
            "| 3 | Remotion | motion execution and render |", "",
            "## Two rules that are not stylistic", "",
            "1. **`[Subject]` is a slot and is never expanded.** The prompts below are "
            "verbatim. An expanded prompt reads exactly like an authored one, and an agent "
            "handed it will paste it to a client as though the studio wrote it.",
            f"2. **An absent cross-tool cell is `null`, never a default.** Of {cell['listed']} "
            f"listed cells, {cell['filled']} carry a parameter, {cell['tested']} have actually "
            f"been run against the model version, and {cell['nulls']} are empty because nobody "
            "has tested them. A plausible string in an untested cell is a claim we cannot "
            "defend to a client.", "",
            f"**{pair_total} declared motion pairings across {pair_techs} of the "
            f"{tcount} techniques.** Declared, never inferred: they come from an "
            f"explicit `styles:` list in `data/cinematic/<slug>.md`, authored in "
            f"`platform/catalog/pairings.py`. A technique with no entry returns an "
            f"empty list and says so, because a wrong pairing hands a client a "
            f"duration and an easing and looks researched.", "",
            f"`data/cinematic/` is **source**, not generated: authored, committed, reviewed in a "
            f"diff. See `data/cinematic/README.md`. Reference stills are linked; "
            f"{videos}/{tcount} techniques have a reference video.", ""]

        by_cat: dict[str, list] = defaultdict(list)
        for r in cat_rows:
            by_cat[r["cat_label"]].append(r)
        for label, rows in by_cat.items():
            lines += [f"## {label}  (`{rows[0]['cat_key']}`, {len(rows)})", "",
                      "| technique | level | motions | tested tools | prompt |",
                      "|---|---|---|---|---|"]
            for r in rows:
                motions = Q("SELECT COUNT(*) n FROM technique_motion m WHERE m.technique_id=?",
                            (r["id"],))[0]["n"]
                tools_tested = [x["key"] for x in Q(
                    """SELECT a.key FROM technique_tool_param p JOIN ai_tool a ON a.id=p.tool_id
                       WHERE p.technique_id=? AND p.tested=1 ORDER BY a.key""", (r["id"],))]
                lines.append(
                    f"| [{r['name']}](#{r['name']}) | {r['level'] or '—'} | {motions} | "
                    f"{', '.join(tools_tested) or 'none'} | {clip(r['prompt_text'], 90)} |")
            lines.append("")

        lines.append("## Techniques in full")
        for r in cat_rows:
            lines += ["", f"### {r['name']}", "",
                      f"**{r['title']}** · `{r['cat_key']}` · level {r['level'] or '—'}",
                      "", "```", r["prompt_text"], "```", ""]
            if r["lede_text"]:
                lines += [clip(r["lede_text"], 400), ""]
            if r["when_to_use_text"]:
                lines += ["**When to use.** " + clip(r["when_to_use_text"], 300), ""]
            if r["directing_text"]:
                lines += ["**Directing the AI.** " + clip(r["directing_text"], 400), ""]
            mist = Q("SELECT text FROM technique_section WHERE technique_id=? AND kind='common_mistake'"
                     " ORDER BY ord", (r["id"],))
            if mist:
                lines.append("**Common mistakes.**")
                for m in mist:
                    lines.append(f"- {clip(m['text'], 220)}")
                lines.append("")
            tools = Q("""SELECT a.key, a.label, p.params, p.version_tag, p.tested
                         FROM technique_tool_param p JOIN ai_tool a ON a.id=p.tool_id
                         WHERE p.technique_id=? ORDER BY a.key""", (r["id"],))
            if tools:
                lines += ["| tool | params | version | tested |", "|---|---|---|---|"]
                for t in tools:
                    lines.append(f"| `{t['key']}` {t['label']} | "
                                 f"{('`' + t['params'] + '`') if t['params'] else '**null**'} | "
                                 f"{t['version_tag'] or '—'} | {'yes' if t['tested'] else 'no'} |")
                lines.append("")
            mot = Q("""SELECT m.kind, s.key style, sc.name card, sc.duration_frames
                       FROM technique_motion m JOIN style s ON s.id=m.style_id
                       LEFT JOIN shot_card sc ON sc.id=s.card_id
                       WHERE m.technique_id=? ORDER BY s.key""", (r["id"],))
            if mot:
                lines += ["**Shot cards that can carry it.** "
                          + ", ".join(f"`{m['style']}`"
                                      + (f" ({m['card']})" if m["card"] and m["card"] != m["style"] else "")
                                      + (f", {m['duration_frames']}f" if m["duration_frames"] else "")
                                      for m in mot),
                          ""]
            cites = Q("SELECT title, url FROM technique_citation WHERE technique_id=? ORDER BY ord",
                      (r["id"],))
            if cites:
                lines.append("**Sources.** " + ", ".join(
                    f"[{c['title']}]({c['url']})" for c in cites))
                lines.append("")
    else:
        lines = ["# Cinematic techniques", "",
                 "The catalog corpus has not been ingested. See `data/cinematic/README.md`.",
                 ""]

    # -- per-technique pages (F072) -----------------------------------------
    # One page per technique, not one page with 150 entries. A technique page is
    # what an LLM loads when a brief names a slug; making it grep the 40 KB
    # domain document to find out that `dolly-shot` has two declared pairings
    # costs a context window to learn one fact.
    tech_dir = OUT / "techniques"
    tech_dir.mkdir(parents=True, exist_ok=True)
    for old in tech_dir.glob("*.md"):
        old.unlink()
    page_count = 0
    for r in cat_rows:
        tl = [f"# {r['title']}", "",
              f"`{r['name']}` · {r['cat_label']} · level {r['level'] or '—'}", ""]
        if r["video_url"]:
            tl += [f"Reference video: `{r['video_url']}`", ""]
        elif cat_rows and any(x["video_url"] for x in cat_rows):
            tl += ["No reference video for this technique.", ""]
        tl += ["## Prompt (verbatim, `[Subject]` intact)", "", "```", r["prompt_text"], "```", ""]
        if r["lede_text"]:
            tl += [clip(r["lede_text"], 600), ""]
        if r["when_to_use_text"]:
            tl += ["**When to use.** " + clip(r["when_to_use_text"], 400), ""]
        if r["directing_text"]:
            tl += ["**Directing the AI.** " + clip(r["directing_text"], 500), ""]
        mist = Q("SELECT text FROM technique_section WHERE technique_id=? AND kind='common_mistake'"
                 " ORDER BY ord", (r["id"],))
        if mist:
            tl.append("**Common mistakes.**")
            for m in mist:
                tl.append(f"- {clip(m['text'], 240)}")
            tl.append("")
        tools = Q("""SELECT a.key, a.label, p.params, p.version_tag, p.tested
                     FROM technique_tool_param p JOIN ai_tool a ON a.id=p.tool_id
                     WHERE p.technique_id=? ORDER BY a.key""", (r["id"],))
        if tools:
            tl += ["| tool | params | version | tested |", "|---|---|---|---|"]
            for t in tools:
                tl.append(f"| `{t['key']}` | "
                          f"{('`' + t['params'] + '`') if t['params'] else '**null**'} | "
                          f"{t['version_tag'] or '—'} | {'yes' if t['tested'] else 'no'} |")
            tl.append("")
        mot = Q("""SELECT m.kind, s.key style, sc.name card, cc.key category,
                          sc.duration_frames
                   FROM technique_motion m JOIN style s ON s.id=m.style_id
                   LEFT JOIN shot_card sc ON sc.id=s.card_id
                   LEFT JOIN category cc ON cc.id=sc.category_id
                   WHERE m.technique_id=? ORDER BY sc.name, s.key""", (r["id"],))
        tl.append("## Motion pairings")
        if mot:
            tl += ["", "**Declared, not inferred.** These come from an explicit "
                      "`styles:` list in `data/cinematic/<slug>.md`, authored in "
                      "`platform/catalog/pairings.py`. Nothing here is matched by "
                      "name similarity.", ""]
            tl += ["| kind | shot card | category | frames | style |",
                   "|---|---|---|---|---|"]
            for m in mot:
                tl.append(f"| {m['kind']} | `{m['card'] or '—'}` | {m['category'] or '—'} | "
                          f"{m['duration_frames'] or '—'} | `{m['style']}` |")
            tl.append("")
            tl += ["```", f"python platform/query.py technique-motions {r['name']}", "```", ""]
        else:
            tl += ["", "**None declared.** No entry in `platform/catalog/pairings.py` "
                      "maps this technique to a shot card, so this page does not "
                      "claim one. Pairing is authored, never guessed — a wrong "
                      "pairing hands a client a duration and an easing and looks "
                      "researched.", ""]
        cites = Q("SELECT title, url FROM technique_citation WHERE technique_id=? ORDER BY ord",
                  (r["id"],))
        if cites:
            tl.append("## Sources")
            tl.append("")
            for c in cites:
                tl.append(f"- {c['title']}" + (f" — <{c['url']}>" if c["url"] else ""))
            tl.append("")
        sibs = re.findall(r"\[([^\]]+)\]\((\w[\w-]*)\.md\)",
                          (ROOT / "data" / "cinematic" / f"{r['name']}.md").read_text(
                              encoding="utf-8").split("## Related")[-1]
                          if (ROOT / "data" / "cinematic" / f"{r['name']}.md").exists() else "")
        if sibs:
            tl += ["## Related techniques", ""]
            tl += [f"- [{s}]({s}.md)" for s in sibs]
            tl.append("")
        (tech_dir / f"{r['name']}.md").write_text("\n".join(tl), encoding="utf-8")
        page_count += 1

    lines += ["", "## Per-technique pages", "",
              f"One page per technique, {page_count} in total, so loading a single "
              f"technique does not cost a 40 KB document:", "",
              "| technique | category | level | video | pairings |",
              "|---|---|---|---|---|"]
    for r in cat_rows:
        mot_n = Q("SELECT COUNT(*) n FROM technique_motion WHERE technique_id=?",
                  (r["id"],))[0]["n"]
        lines.append(f"| [{r['name']}](../techniques/{r['name']}.md) | {r['cat_key']} | "
                     f"{r['level'] or '—'} | {'yes' if r['video_url'] else 'no'} | {mot_n} |")
    lines.append("")
    (OUT / "domains" / "cinematic.md").write_text("\n".join(lines), encoding="utf-8")

    # ------------------------------------------------- domain: overview
    lines = ["# video-shotcraft — overview", "",
             f"An open-source agent skill (Apache-2.0) that turns Claude Code or Codex into a "
             f"motion-design studio: {stats['cards']} shot recipe cards, {stats['styles']} tuned Remotion "
             f"demos, {stats['sfx']} sound effects and a validated 36.2-second promo template.", "",
             f"- **upstream**: {UPSTREAM_URL} — {repo['stars']:,} stars, {repo['forks']:,} forks, "
             f"`{repo['head_sha'][:12]}`",
             f"- **site**: {UPSTREAM_SITE}", "",
             "| | |", "|---|---|",
             f"| shot cards | {stats['cards']} |", f"| motion styles (demos) | {stats['styles']} |",
             f"| documented parameters | {stats['card_params']} |", f"| pitfalls | {stats['pitfalls']} "
             f"({stats['pitfalls_critical']} marked 命门) |",
             f"| motion params extracted by us | {stats['motion_params']} |",
             f"| aesthetic rules | {stats['rules']} |", f"| SFX / BGM | {stats['sfx']} / {stats['bgm']} |",
             f"| upstream locales | 2 (en, zh) |", f"| our target locales | {stats['locales']} |",
             f"| translation strings | {stats['translations']} |", "",
             "## Read in this order", ""]
    for slug, title in DOMAINS:
        lines.append(f"- [{title}](domains/{slug}.md)")
    lines += ["", "## Hard rules that survive everything", "",
              "1. **Real screenshots for real products.** Reproducing an existing page means capturing it "
              "with a headless browser at 2x, with element cutouts and a layout.json. Hand-drawn UI is only "
              "allowed outside reproduction contexts.",
              "2. **The visual language grows from the product**, not from a borrowed promo skin. The cards "
              "supply motion grammar and timing; type, colour and material are re-derived from the target.",
              "3. **One shot, one motion idea.** Repeat a technique across a film and it stops being a "
              "technique and starts being noise.",
              "4. **Hold after every key beat.** Wordmark settle ≥1s, batch tail 0.5s still, opening hero ≥3s. "
              "Feedback history only ever asked for slower.",
              "5. **With strong BGM, every cut lands on a beat.** Measure real BPM and phase first, then "
              "verify cut error ≤3 frames against the rendered audio.",
              "6. **Determinism.** Seeded pseudo-randomness only; renders must be frame-reproducible.",
              "7. **Independent final review.** The maker never does the first QA pass.", ""]
    (OUT / "domains" / "overview.md").write_text("\n".join(lines), encoding="utf-8")

    # ------------------------------------------------- index.json / index.md
    index = {
        "generated_from": "platform/db/shotcraft.db",
        "upstream_sha": repo["head_sha"],
        "upstream": {"url": UPSTREAM_URL, "site": UPSTREAM_SITE,
                     "stars": repo["stars"], "forks": repo["forks"], "license": repo["license"]},
        "stats": stats,
        "domains": [{"slug": s, "title": t, "path": f"wiki/domains/{s}.md"} for s, t in DOMAINS],
        "cinematic": {
            "techniques": [dict(r) | {
                "mistakes": [m["text"] for m in Q(
                    "SELECT text FROM technique_section WHERE technique_id=? AND kind='common_mistake' ORDER BY ord",
                    (r["id"],))],
                "citations": [dict(x) for x in Q(
                    "SELECT title, url FROM technique_citation WHERE technique_id=? ORDER BY ord",
                    (r["id"],))],
                "motions": [dict(m) for m in Q(
                    """SELECT m.kind, s.key style, sc.name card, sc.duration_frames
                       FROM technique_motion m JOIN style s ON s.id=m.style_id
                       LEFT JOIN shot_card sc ON sc.id=s.card_id
                       WHERE m.technique_id=? ORDER BY s.key""", (r["id"],))],
                "tools": [dict(t) for t in Q(
                    """SELECT a.key, a.label, p.params, p.version_tag, p.tested, p.tested_at
                       FROM technique_tool_param p JOIN ai_tool a ON a.id=p.tool_id
                       WHERE p.technique_id=? ORDER BY a.key""", (r["id"],))],
            } for r in cat_rows],
        } if cat_rows else {"techniques": []},
        "categories": [dict(c) for c in cats],
        "locales": Q("SELECT code, bcp47, name_en, native_name, status FROM locale ORDER BY id"),
        "licenses": Q("SELECT subject, spdx, commercial_use, blocking FROM license_registry"),
        "opportunities": [dict(o) for o in opps],
        "cards": card_index,
    }
    (OUT / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")

    md = ["# video-shotcraft wiki", "",
          f"Generated from `{stats['upstream_sha'][:12]}` — {stats['cards']} cards, {stats['styles']} styles, "
          f"{stats['motion_params']} extracted motion parameters, {stats['rules']} aesthetic rules.", "",
          "**Machine-readable entry points**", "",
          "- `wiki/index.json` — everything, one object (cards, categories, locales, licenses, opportunities)",
          "- `wiki/llms.txt` — index in the llms.txt convention",
          "- `wiki/llms-full.txt` — the whole corpus in one file, for RAG ingestion",
          "- `wiki/api/openapi.json` — the read-only HTTP contract",
          "- `platform/db/shotcraft.db` — SQLite, FTS5 search over cards, params, pitfalls and docs", "",
          "**Documents**", ""]
    for s, t in DOMAINS:
        md.append(f"- [{t}](domains/{s}.md)")
    md += ["", "**Cards**", "",
           f"- {stats['cards']} pages in [`wiki/cards/`](cards/), one `.md` and one `.json` each",
           "- index table: [domains/cards.md](domains/cards.md)", ""]
    (OUT / "index.md").write_text("\n".join(md), encoding="utf-8")

    # ------------------------------------------------- llms.txt / llms-full.txt
    L = ["# video-shotcraft", "",
         f"> A wiki of the video-shotcraft motion-design system: {stats['cards']} shot recipe cards, "
         f"{stats['styles']} tuned Remotion demos, {stats['card_params']} documented parameters, "
         f"{stats['rules']} aesthetic rules, extracted easing/spring/timing grammar, and a licence audit. "
         f"Generated from upstream `{repo['head_sha'][:12]}`.", "",
         "This is a static knowledge base for language models. Every card is addressed by a stable slug; "
         "the slug is the join key across the markdown cards, the Remotion demos, the media files and the "
         "deep links on the live gallery.", "",
         "## Documents", ""]
    for s, t in DOMAINS:
        L.append(f"- [{t}](domains/{s}.md)")
    L += ["", "## Cards by category", ""]
    for cat in cats:
        rows = [c for c in card_index if c["category"] == cat["key"]]
        if rows:
            L.append(f"### {cat['label_en']} / {cat['label_zh']}")
            L.append("")
            for c in rows:
                L.append(f"- [{c['name']}](cards/{c['name']}.md): {clip(c['summary_zh'], 150)}")
            L.append("")
    (OUT / "llms.txt").write_text("\n".join(L), encoding="utf-8")

    full = ["# video-shotcraft — full corpus", "",
            f"upstream {UPSTREAM_URL} @ {repo['head_sha']}", ""]
    for s, t in DOMAINS:
        body = (OUT / "domains" / f"{s}.md").read_text(encoding="utf-8")
        full.append("\n".join(["\n---\n", f"<!-- domain: {s} -->", body]))
    for c in card_index:
        full.append("\n".join(["\n---\n", (OUT / "cards" / f"{c['name']}.md").read_text(encoding="utf-8")]))
    (OUT / "llms-full.txt").write_text("\n".join(full), encoding="utf-8")

    # ------------------------------------------------- openapi
    openapi = {
        "openapi": "3.1.0",
        "info": {"title": "shotcraft index API", "version": "1.0.0",
                 "description": "Read-only access to the indexed video-shotcraft knowledge base. "
                                "Generated from shotcraft.db; no write endpoints.",
                 "license": {"name": "Apache-2.0", "url": "https://www.apache.org/licenses/LICENSE-2.0"}},
        "servers": [{"url": "http://localhost:8080", "description": "local"}],
        "components": {"schemas": {
            "Error": {"type": "object", "required": ["error"],
                      "properties": {"error": {"type": "string"}}},
            "CardRef": {
                "type": "object",
                "required": ["name", "category"],
                "properties": {
                    "name": {"type": "string"},
                    "category": {"type": "string"},
                    "energy": {"type": ["string", "null"], "enum": ENERGY_ORDER + [None]},
                    "duration_frames": {"type": ["integer", "null"]},
                    "summary": {"type": "string",
                                "description": "Chinese one-liner, upstream verbatim"},
                }},
        }},
        "paths": {
            "/": {"get": {"summary": "Health check and the route list"}},
            "/locales": {"get": {"summary": "Locales and how many strings each has"}},
            "/techniques": {"get": {"summary": "The cinematic-technique catalog with a "
                                                "cross-tool matrix summary per technique"}},
            "/optimize/{slug}": {"get": {
                "summary": "One technique, every tool: the verbatim prompt, each tool's "
                           "parameters, and whether any cell has been run",
                "parameters": [{"name": "tool", "in": "query",
                                "schema": {"type": "string",
                                           "enum": ["mj61", "runway_gen3", "veo2",
                                                    "kling15", "luma", "pika15", "sora"]},
                                "description": "restrict to one tool; omit for all seven"}]}},
            "/categories": {"get": {"summary": "The 10 card categories with counts"}},
            "/cards": {"get": {"summary": f"All {stats['cards']} shot cards",
                               "parameters": [
                                   {"name": "category", "in": "query", "schema": {"type": "string", "enum": [c["key"] for c in cats]}},
                                   {"name": "energy", "in": "query", "schema": {"type": "string", "enum": [r[0] for r in ENERGY_ORDER]}},
                                   {"name": "q", "in": "query", "schema": {"type": "string"},
                                    "description": "Full-text search. 3+ characters use the trigram "
                                                   "index (substring, any script); 1-2 characters fall "
                                                   "back to LIKE, which is why CJK works either way."},
                                   {"name": "max_frames", "in": "query",
                                    "schema": {"type": "integer"},
                                    "description": "Only cards whose suggested duration fits"},
                                   {"name": "limit", "in": "query", "schema": {"type": "integer"}}]}},
            "/cards/{slug}": {"get": {"summary": "One card with its parameters, pitfalls and styles"}},
            "/styles": {"get": {"summary": f"All {stats['styles']} motion styles"}},
            "/styles/{key}": {"get": {"summary": "One style with its extracted motion parameters and easings"}},
            "/rules": {"get": {"summary": f"The {stats['rules']} aesthetic rules, grouped by family"}},
            "/licenses": {"get": {"summary": "Licence audit for the whole stack"}},
            "/opportunities": {"get": {"summary": "Monetization models with their evidence"}},
            "/stats": {"get": {"summary": "Counts used by every document in this wiki"}},
        },
    }
    (OUT / "api" / "openapi.json").write_text(json.dumps(openapi, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps({
        "cards": len(card_index), "domains": len(DOMAINS),
        "llms_full_bytes": (OUT / "llms-full.txt").stat().st_size,
        "index_json_bytes": (OUT / "index.json").stat().st_size,
    }, indent=2))
    return 0


ENERGY_ORDER = ["low", "low-mid", "mid-low", "mid", "mid-high", "high", "very-high", "peak"]

if __name__ == "__main__":
    raise SystemExit(main())