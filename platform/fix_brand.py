"""One-time correction of the brand name inside the locale data.

`video-shotcraft` is upstream's project. ADR-0005 makes this repository an
independent fork under its own brand, and `platform/site/check_dist.py` fails on
any page that still carries the upstream name. The strings below were inherited
from upstream's `translations.js` when the locale files were first extracted, and
they are what a reader sees in the page intro, the document title and the
accessible name of the star button.

Replacing the name is the whole of it: the sentences stay, the noun changes.
Where a value ends up *not* matching `en`, `check_coverage.py` would normally
complain -- and here nothing becomes less translated, because the substitution is
inside all three locales equally.

    python platform/fix_brand.py            # report
    python platform/fix_brand.py --apply    # rewrite
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# parents[1], not parents[2]: this file is at <root>/platform/fix_brand.py, so
# parents[0] is `platform` and parents[1] is the repository root. The other
# spelling walks out of the repository entirely and then FileNotFoundError names
# a path nobody recognises.
ROOT = Path(__file__).resolve().parents[1]
LOCALES = ROOT / "site" / "locales"

UPSTREAM = "video-shotcraft"
OURS = "shotcraft"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true",
                    help="rewrite the files; without it, only report")
    a = ap.parse_args()

    changed = 0
    for loc_dir in sorted(p for p in LOCALES.iterdir() if p.is_dir()):
        for f in sorted(loc_dir.glob("*.json")):
            raw = f.read_text(encoding="utf-8")
            if UPSTREAM not in raw:
                continue
            n = raw.count(UPSTREAM)
            rel = f.relative_to(ROOT)
            if a.apply:
                data = json.loads(raw)

                def fix(v):
                    if isinstance(v, str):
                        return v.replace(UPSTREAM, OURS)
                    if isinstance(v, dict):
                        return {k: fix(x) for k, x in v.items()}
                    if isinstance(v, list):
                        return [fix(x) for x in v]
                    return v

                out = json.dumps(fix(data), ensure_ascii=False, indent=2) + "\n"
                f.write_text(out, encoding="utf-8")
                print(f"  fixed {n} occurrence(s) in {rel.as_posix()}")
            else:
                print(f"  {rel.as_posix()}: {n} occurrence(s)")
            changed += n

    if not changed:
        print("no occurrence of the upstream name in site/locales/")
    if not a.apply:
        print("\nre-run with --apply to rewrite them")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())