"""Import the Cinematique catalog (MIT) into `data/cinematic/` in our format.

    python platform/catalog/import_cinematique.py
    python platform/catalog/import_cinematique.py --source "D:/other/cinematique"

Why an importer instead of hand-editing 150 files
-------------------------------------------------
The catalog exists as its own MIT-licensed project with its own repo, its own
architecture and its own render pipeline. Copying it by hand would create a fork
we then have to keep in sync. Importing it means:

  * the upstream of the catalog stays one repository, which is theirs;
  * `data/cinematic/` stays *our* source in *our* format, so ADR 0007's ingest
    contract, the controlled category vocabulary and the `[Subject]` rule apply
    unchanged;
  * a bump is `git clone && python platform/catalog/import_cinematique.py && git diff`.

What this refuses to do
-----------------------
1. **Mark any cell `tested`.** Cinematique's `cross-tool-matrix.csv` has a
   `Status` column that is either FILLED or TODO, and no verification column at
   all. Their pipeline wrote parameters; nothing recorded a run against a model
   version. So every imported cell lands as `tested: no` and the ingest reports
   0 tested cells. That is the single most important thing this importer does:
   without it the DB would claim 1050 verified tool parameters.
2. **Drop a TODO.** A row with `Status: TODO` has no parameters, and the honest
   representation of "we looked and there is nothing" is an empty cell that lands
   as NULL, not an omission that looks like "not researched".
3. **Touch upstream shotcraft.** It never reads that repo.

Provenance is recorded per file: source repo, source file, sha256 of the byte we
read, and the MIT notice. Every technique row in the DB traces back to a specific
input line, so a disputed claim can be checked against the CSV.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import pairings  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "cinematic"
MEDIA_OUT = OUT / "media"

# Their 21 category strings are "<group> · <level>". We keep the group as a
# controlled value and the level as our own column, which is what makes
# `--category lighting` a filter rather than a guess.
GROUP_TO_CATEGORY = {
    "camera work": "camera-work",
    "lighting": "lighting",
    "composition": "composition",
    "editing": "editing",
    "storytelling": "narrative",
    "visual effects & promptable fx": "visual-effects",
    "genres & styles": "genres",
}

TOOLS = [
    ("MJ v6.1", "mj61", "v6.1"),
    ("Runway Gen-3", "runway_gen3", "gen-3-alpha"),
    ("Veo 2", "veo2", "veo-2"),
    ("Kling 1.5", "kling15", "kling-1.5"),
    ("Luma Dream Machine", "luma", "dream-machine"),
    ("Pika 1.5", "pika15", "pika-1.5"),
    ("Sora", "sora", "sora-1"),
]

# Cinematique writes parameters as `k=v | k=v | k=v`. An unescaped `|` inside a
# markdown table cell ends the cell, so a single Runway parameter string silently
# became four columns and the ingest read a truncated value. Escaped on write and
# unescaped on read; the round trip is asserted by platform/catalog/selftest.py.
CELL_ESCAPE = "\\|"


def escape_cell(value: str) -> str:
    return value.replace("|", CELL_ESCAPE)

# Section headings are per-technique prose titles ("When to use Aerial Shot"), so
# matching is by prefix rather than equality.
SECTION_MATCH = [
    ("prompt template", None),
    ("when to use", "when_to_use"),
    ("directing the ai", "directing"),
    ("common mistakes", "common_mistakes"),
    ("sources and further reading", "sources"),
    ("related techniques", "related"),
]


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def load_catalog(src: Path) -> list[dict]:
    return json.loads((src / "cinematique-catalog.json").read_text(encoding="utf-8"))


def load_matrix(src: Path) -> dict[str, dict]:
    with (src / "cross-tool-matrix.csv").open(encoding="utf-8-sig", newline="") as f:
        return {r["Slug"]: r for r in csv.DictReader(f)}


def split_category(raw: str) -> tuple[str, str]:
    group, _, level = (raw or "").partition("·")
    key = GROUP_TO_CATEGORY.get(group.strip().lower())
    if key is None:
        raise ValueError(f"unknown catalog group {group.strip()!r} in {raw!r}")
    return key, level.strip().lower()


def section_map(sections: list[dict]) -> dict[str, str]:
    out: dict[str, str] = {}
    for s in sections:
        title = (s.get("title") or "").strip()
        body = (s.get("content") or "").strip()
        for prefix, key in SECTION_MATCH:
            if key is None:
                continue
            if title.lower().startswith(prefix):
                out.setdefault(key, body)
    return out


def bullets(text: str) -> list[str]:
    """Common mistakes arrive as a prose paragraph, not a list.

    They are split on sentence boundaries rather than bullets, because in the
    source corpus they are sentences. Anything already bulleted is passed
    through, so the importer handles both shapes without a flag.
    """
    items = []
    for line in (text or "").splitlines():
        m = re.match(r"^\s*(?:[-*•]|\d+[.)])\s+(.+)$", line)
        if m:
            items.append(m.group(1).strip())
    if items:
        return items
    flat = re.sub(r"\s+", " ", text or "").strip()
    if not flat:
        return []
    # Split after . ! ? only when followed by a capital, so "e.g." and "3.5mm"
    # do not become their own item.
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z(\"'])", flat)
    return [p.strip() for p in parts if len(p.strip()) > 12]


def sources(text: str) -> list[tuple[str, str | None]]:
    """Sources are plain text with no URLs. Never invent one.

    The source catalog's "Sources and further reading" section lists
    `Title — Publisher` with no link. Recording a fabricated URL next to a real
    title would be the single most damaging thing this importer could do, so the
    title is stored and the URL stays NULL.
    """
    out: list[tuple[str, str | None]] = []
    for line in (text or "").splitlines():
        line = line.strip(" \t-—–*")
        if not line:
            continue
        m = re.match(r"^(.*?)\s+[—–]\s+(.*)$", line)
        if m:
            out.append((m.group(1).strip(), None))
        elif len(line) > 8:
            out.append((line, None))
    return out


def related_slugs(item: dict) -> list[str]:
    """Sibling techniques, taken from the structured field, not the prose blob.

    The `Related techniques` *section* concatenates nine entries with no
    delimiter. `related_techniques` on the item is the same data as structured
    records with a URL, and the slug in that URL resolves to a real catalog
    entry. This is a declared relation, which is exactly what F074 requires:
    pairing is declared by the catalog, never inferred from a name match.
    """
    out = []
    for r in item.get("related_techniques") or []:
        url = (r or {}).get("url", "")
        if "/cinematique/" in url:
            s = url.rsplit("/", 1)[-1]
            if s:
                out.append(s)
    return out


def links(text: str) -> list[tuple[str, str]]:
    return [(a.strip(), b.strip()) for a, b in re.findall(r"\[([^\]]+)\]\(([^)]+)\)", text or "")]


def slugify_title(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")


def clean(text: str) -> str:
    """Collapse prose to one line per paragraph so the .md stays readable."""
    return re.sub(r"\n{3,}", "\n\n", (text or "").strip())


def build_file(item: dict, row: dict | None, media: Path | None,
               meta: dict) -> tuple[str, dict]:
    slug = item["slug"]
    category, level = split_category(item.get("category", ""))
    prompt = (item.get("prompt_template") or "").strip()
    if "[Subject]" not in prompt:
        raise ValueError(f"{slug}: prompt_template has no [Subject] slot")
    secs = section_map(item.get("sections") or [])

    lines = [
        "---",
        f"slug: {slug}",
        f"title: {json.dumps(item['title'], ensure_ascii=False)}",
        f"category: {category}",
        f"level: {level}",
        f"image: {json.dumps((item.get('image') or {}).get('url', ''), ensure_ascii=False)}",
        f"source_url: {item.get('url', '')}",
        f"upstream_file: {meta['catalog_file']}",
        f"upstream_sha256: {meta['catalog_sha']}",
    ]
    # Declared motion pairings, ours, from platform/catalog/pairings.py. Written
    # into the file so the relation travels with the row and is reviewable in a
    # diff rather than hidden in a join table.
    declared = pairings.cards_for(slug)
    if declared:
        lines.append("styles: [" + ", ".join(declared) + "]")
    if media:
        lines.append(f"video: media/{media.name}")
    lines += ["---", "", prompt, ""]

    if item.get("lede"):
        lines += ["## Lede", "", clean(item["lede"]), ""]
    if secs.get("when_to_use"):
        lines += ["## When to use", "", clean(secs["when_to_use"]), ""]
    if secs.get("directing"):
        lines += ["## Directing the AI", "", clean(secs["directing"]), ""]
    if secs.get("common_mistakes"):
        items_m = bullets(secs["common_mistakes"])
        if items_m:
            lines += ["## Common mistakes", ""]
            lines += [f"- {i}" for i in items_m]
            lines.append("")

    cites = sources(secs.get("sources", ""))
    if cites:
        # Plain text, no URL. Rendered without a link target on purpose.
        lines += ["## Sources", ""]
        for title, url in cites:
            lines.append(f"- {title}" if not url else f"- [{title}]({url})")
        lines.append("")

    # The cross-tool matrix. `Status: TODO` becomes an explicitly empty row for
    # every tool, so "we looked and there is nothing" is visible in the source
    # rather than inferred from a missing line.
    lines += ["## Cross-tool", "",
              "| tool | params | version | tested |", "|---|---|---|---|"]
    filled = tested = 0
    status = (row or {}).get("Status", "").strip()
    for label, key, version in TOOLS:
        params = ((row or {}).get(f"{label} Params") or "").strip()
        if status.upper() != "FILLED":
            params = ""
        if params:
            filled += 1
            # tested is `no` for every imported cell. See the module docstring.
            lines.append(f"| {key} | `{escape_cell(params)}` | {version} | no |")
        else:
            lines.append(f"| {key} |  | {version} | no |")
    lines.append("")

    sibs = related_slugs(item)
    if sibs:
        lines += ["## Related", ""]
        for s in sibs:
            lines.append(f"- [{s}]({s}.md)")
        lines.append("")

    body = "\n".join(lines)
    stats = {"filled": filled, "tested": tested, "status": status,
             "mistakes": len(bullets(secs.get("common_mistakes", ""))),
             "citations": len(cites), "related": len(sibs)}
    return body, stats


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", default=r"C:\susa ai\cinematique",
                    help="path to the Cinematique checkout")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-videos", action="store_true",
                    help="skip the 41 reference videos (68 MB)")
    a = ap.parse_args()

    src = Path(a.source)
    if not (src / "cinematique-catalog.json").exists():
        raise SystemExit(f"no cinematique-catalog.json under {src}")

    catalog = load_catalog(src)
    matrix = load_matrix(src)

    cat_bytes = (src / "cinematique-catalog.json").read_bytes()
    mat_bytes = (src / "cross-tool-matrix.csv").read_bytes()
    meta = {
        "catalog_file": "cinematique-catalog.json",
        "catalog_sha": sha256_bytes(cat_bytes),
        "matrix_file": "cross-tool-matrix.csv",
        "matrix_sha": sha256_bytes(mat_bytes),
        "license": "MIT",
        "license_holder": "Cinematique Vault Team",
        "imported_at": now_iso(),
    }

    if not a.dry_run:
        if OUT.exists():
            for old in OUT.glob("*.md"):
                old.unlink()
        OUT.mkdir(parents=True, exist_ok=True)

    videos = {}
    if not a.no_videos and (src / "videos").is_dir():
        if not a.dry_run:
            MEDIA_OUT.mkdir(parents=True, exist_ok=True)
            for old in MEDIA_OUT.glob("*.mp4"):
                old.unlink()
        for v in sorted((src / "videos").glob("*.mp4")):
            if a.dry_run:
                videos[v.stem] = v
            else:
                shutil.copy2(v, MEDIA_OUT / v.name)
                videos[v.stem] = MEDIA_OUT / v.name

    rows = []
    problems: list[str] = []
    for item in catalog:
        slug = item["slug"]
        try:
            body, stats = build_file(item, matrix.get(slug), videos.get(slug), meta)
        except ValueError as exc:
            problems.append(str(exc))
            continue
        if not a.dry_run:
            (OUT / f"{slug}.md").write_text(body + "\n", encoding="utf-8")
        rows.append({"slug": slug, "category": item.get("category", ""), **stats})

    filled = sum(r["filled"] for r in rows)
    todos = sum(1 for r in rows if r["status"].upper() != "FILLED")
    slugs = [r["slug"] for r in rows]
    mapped = [s for s in slugs if pairings.cards_for(s)]
    unmapped = pairings.unmapped(slugs)
    report = {
        "source": str(src),
        "license": meta["license"],
        "techniques": len(rows),
        "matrix_cells_filled": filled,
        "matrix_cells_todo": todos,
        "matrix_cells_tested": 0,
        "videos_copied": len(videos),
        "by_category": {},
        "problems": problems,
        "source_sha256": {"catalog": meta["catalog_sha"], "matrix": meta["matrix_sha"]},
        "motion_pairings": {
            "techniques_mapped": len(mapped),
            "techniques_unmapped": len(unmapped),
            "declared_links": sum(len(pairings.cards_for(s)) for s in slugs),
            "note": ("pairing is declared in platform/catalog/pairings.py, never "
                     "inferred from a name match; an unmapped technique returns an "
                     "empty list rather than a guess"),
            "unmapped": unmapped,
        },
        "note": ("every cell is tested:no because the source matrix has a FILLED/TODO "
                 "status column and no verification column; nothing records a run "
                 "against a model version"),
    }
    for r in rows:
        report["by_category"][r["category"]] = report["by_category"].get(r["category"], 0) + 1

    if not a.dry_run:
        (ROOT / "platform" / "catalog" / "import_report.json").write_text(
            json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())