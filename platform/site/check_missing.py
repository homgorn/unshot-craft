"""The chrome strings a locale needs translated, with the English source.

    python platform/site/check_missing.py ru

`en/ui.json` is 104 keys, `page.json` 11, `showcase.json` 18. Upstream keeps
them apart only because its three inline mechanisms are separate — which is
exactly the coupling ADR-0004 removed. A locale therefore inherits English
chrome automatically, and only genuinely new work shows up here.

Coverage is measured as *difference from en*, not presence: an inherited value
is present but not translated, and conflating the two made ru report 100% while
every card description was still English.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LOCALES = ROOT / "site" / "locales"

# Assigned via innerHTML, so the tags must survive translation.
MARKUP_KEYS = {"page.heroTitle", "page.heroSub"}

# Never translate: these are codes, not prose.
CODE_VALUES = {"meta.htmlLang", "meta.ogLocale"}


def load(p: Path) -> dict:
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("code", nargs="?", default="ru")
    ap.add_argument("--write", default=None, metavar="PATH",
                    help="also write the report to PATH (default: stdout only)")
    a = ap.parse_args()
    code = a.code
    if not (LOCALES / code).is_dir():
        raise SystemExit(f"no locale dir: {LOCALES / code}")

    total = missing = 0
    out = [f"# {code}: chrome strings to translate", "",
           f"Paste into `site/locales/{code}/<ns>.json`. Keep every key; "
           f"translate the value.", ""]

    for ns in ("ui", "page", "showcase"):
        en = load(LOCALES / "en" / f"{ns}.json")
        loc = load(LOCALES / code / f"{ns}.json")
        rows = []
        for k, v in en.items():
            total += 1
            cur = loc.get(k)
            if cur is None:
                missing += 1
                rows.append((k, v, "MISSING"))
            elif cur == v:
                missing += 1
                rows.append((k, v, "INHERITED"))
        if not rows:
            continue
        out.append(f"## {ns}.json — {len(rows)} of {len(en)}")
        out.append("")
        for k, v, state in rows:
            note = "  ← keep the markup" if f"{ns}.{k}" in MARKUP_KEYS else ""
            out.append(f"- `{state:10}` **{k}**: {json.dumps(v, ensure_ascii=False)}{note}")
        out.append("")

    out.append(f"**{total - missing}/{total}** chrome strings translated, "
               f"**{missing}** outstanding.")

    # Print, do not write. This is a checker: running it used to drop a
    # MISSING.md into site/locales/<code>/, which put an untracked generated file
    # inside a source directory and left the working tree dirty. A report goes to
    # stdout or to a path the caller names.
    print("\n".join(out))
    if a.write:
        dest = Path(a.write)
        dest.write_text("\n".join(out) + "\n", encoding="utf-8")
        print(f"\nwritten: {dest}")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())