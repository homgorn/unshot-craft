r"""Read a `.env` file with no third-party dependency.

    from _env import load; load(); os.environ["SITE_ORIGIN"]

Why this file exists instead of `python-dotenv`
----------------------------------------------
Every gate in this repo runs `python platform/<something>.py` directly, and
several of them run each other in subprocesses. Adding a dependency to read one
file would mean every fresh clone needs a `pip install` before
`scripts\init.ps1` can run, and a gate that cannot run without a package install
is a gate nobody runs on a new machine. The format we need is four lines of
`KEY=value`.

What is deliberately not supported
-----------------------------------
* **no interpolation.** `FOO=${BAR}` is stored verbatim. Shell-style expansion
  in a config file is where secrets end up in logs by accident, and nothing here
  needs it.
* **no `export` prefix**, no multi-line values, no nested quoting beyond
  stripping matching surrounding quotes.
* **an already-set variable wins.** A real environment variable must beat the
  file, because CI sets secrets as real variables and a stale `.env` left in a
  checkout must not silently override them.

`.env` is gitignored and `.env.example` is committed. This loader never prints a
value, and `doctor.py` reports only the *names* that are set — a leak of names is
a leak of what the project needs; a leak of values is a leak of the keys.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENV_FILE = ROOT / ".env"
EXAMPLE = ROOT / ".env.example"


def parse(text: str) -> dict[str, str]:
    """`KEY=value` lines into a dict. Comments, blanks and `export` tolerated."""
    out: dict[str, str] = {}
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[7:].lstrip()
        if "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip()
        # Strip one layer of matching quotes, which is how a Windows user will
        # write a path like C:\Users\...
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        if key:
            out[key] = value
    return out


def load(path: Path | None = None) -> dict[str, str]:
    """Merge `.env` into the environment without overwriting what is already set."""
    target = path or ENV_FILE
    if not target.exists():
        return {}
    values = parse(target.read_text(encoding="utf-8", errors="replace"))
    applied = {}
    for key, value in values.items():
        if key in os.environ:
            continue
        os.environ[key] = value
        applied[key] = value
    if applied and "-v" in sys.argv:
        print(f"[env] {target.name}: {len(applied)} key(s) applied "
              f"({', '.join(sorted(applied))})", file=sys.stderr)
    return applied


def configured(*names: str) -> dict[str, str]:
    """The subset of `names` that is set, for a doctor report. Names only."""
    load()
    return {n: "set" for n in names if os.environ.get(n)}


if __name__ == "__main__":
    values = parse(ENV_FILE.read_text(encoding="utf-8", errors="replace")) \
        if ENV_FILE.exists() else {}
    # Snapshot before `load()`, not after. Reading it afterwards says every key
    # was "already set", because `load()` is what set it -- which is a report
    # that cannot distinguish a real environment variable from a file it just
    # applied, and therefore reports nothing.
    preexisting = {k for k in values if k in os.environ}
    load()
    if not values:
        where = f"no {ENV_FILE.name}"
    else:
        where = f"{ENV_FILE.name} defines {len(values)} variable(s)"
    print(where)
    for key in sorted(values):
        state = ("pre-set in the environment, .env value ignored"
                 if key in preexisting else "applied")
        # Names and state only. Never the value: this file exists to make it easy
        # to check what is configured, and printing a value would undo that.
        print(f"  {key:<24} {state}")
    if not values:
        print(f"\ncopy {EXAMPLE.name} to {ENV_FILE.name} to create one")
    print("\nValues are never printed. `python platform/doctor.py` reports the "
          "same list from inside the gates.")