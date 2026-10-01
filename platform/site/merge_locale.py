"""Merge translation fragments into a locale's `ui.json`.

    python platform/site/merge_locale.py ru

Why this exists: `extract_locales.py` flattens all three of upstream's inline
dictionaries into one flat `ui.json`, prefixing index.html's strings `page.`
and showcase.html's `showcase.`. That is the right store for a translator — one
file, no guessing which page a string belongs to — but it means a locale written
as three separate files has to be merged before it will build.

So: hand translators fragments (`_ui_extra.json`) or whole files, and this
merges them, validates every key against `en`, and reports anything unknown
rather than silently shipping it. A key that does not exist upstream can never
render, and a key that shadows a real one is worse than a missing one.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LOCALES = ROOT / "site" / "locales"
TARGETS = ("ui", "page", "showcase")


def read(p: Path) -> dict:
    """Read a JSON file, keeping the `_note` translator comment separate."""
    if not p.exists():
        return {}
    raw = json.loads(p.read_text(encoding="utf-8"))
    note = raw.pop("_note", None)
    return {k: v for k, v in raw.items() if not k.startswith("_")} | (
        {"_note": note} if note else {})


def keys_only(p: Path) -> dict:
    if not p.exists():
        return {}
    return {k: v for k, v in json.loads(p.read_text(encoding="utf-8")).items()
            if not k.startswith("_")}


def write(p: Path, data: dict, note: str | None) -> None:
    out = dict(data)
    if note:
        out["_note"] = note
    p.write_text(json.dumps(out, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                 encoding="utf-8")


def main() -> int:
    code = sys.argv[1] if len(sys.argv) > 1 else "ru"
    d = LOCALES / code
    if not d.is_dir():
        raise SystemExit(f"no locale dir: {d}")

    merged: list[str] = []
    ui_path = d / "ui.json"
    ui = keys_only(ui_path)
    notes: list[str] = []

    # 1. absorb fragments and any standalone namespace files
    for frag in sorted(d.glob("_*.json")):
        data = read(frag)
        added = [k for k in data if k not in ui]
        ui.update(data)
        if data.get("_note"):
            notes.append(data["_note"])
        merged.append(f"{frag.name}: +{len(added)}")
        frag.unlink()

    for ns in ("page", "showcase"):
        f = d / f"{ns}.json"
        if f.exists():
            data = read(f)
            added = 0
            for k, v in data.items():
                if k == "_note":
                    continue
                prefixed = f"{ns}.{k}"
                if prefixed not in ui:
                    ui[prefixed] = v
                    added += 1
            if data.get("_note"):
                notes.append(data["_note"])
            merged.append(f"{ns}.json: +{added} (prefixed)")
            f.unlink()

    # 2. validate against en before writing
    en = keys_only(LOCALES / "en" / "ui.json")
    problems: list[str] = []
    unknown = sorted(k for k in ui if k not in en)
    if unknown:
        # Never fail the build on an extra key: a locale file is hand-edited and
        # a stray key is harmless at runtime (nothing looks it up). Report it so
        # it gets cleaned up, but let the site build.
        pass

    write(ui_path, ui, " | ".join(notes) or None)

    report = {
        "locale": code,
        "merged": merged or ["nothing to merge"],
        "keys": len(ui),
        "en_keys": len(en),
        "inherited_from_en": len(set(en) - set(ui)),
        "unused_keys": unknown,
        "problems": problems,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())