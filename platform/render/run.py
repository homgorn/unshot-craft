"""F060: render the demo corpus to MP4 with Remotion.

    python platform/render/run.py --list
    python platform/render/run.py --install
    python platform/render/run.py --render crash-zoom-punch
    python platform/render/run.py --render --limit 20 --scale 2
    python platform/render/run.py --render-all
    python platform/render/run.py --verify

Why a working copy and not the template in place
-----------------------------------------------
`upstream/` is a pinned read-only clone (AGENTS.md rule 1). `npm install` writes
`node_modules/` and a lockfile into whatever directory it runs in, so rendering
from the template itself would dirty a directory whose whole property is that it
matches someone else's commit. So the template and the demo corpus are copied
into `platform/render/.work/`, which is gitignored, and everything is built there.

What is actually rendered
-------------------------
The 218 `demos/**/*.tsx` components, not the briefs. A brief is a description of
a shot; a demo is the shot. Every demo is a self-contained Remotion component
driven by `useT()`, which reads `useCurrentFrame()`, so each one is a composition
in its own right with a duration exported as `*_DURATION`. Rendering a brief
would mean writing the animation, which is a different project with a different
licence question; rendering the demos produces real footage of real motion.

Durations come from the database, not from parsing the TSX, because ADR-0002 says
the database is the source of truth and the parser already solved the naming
problem (`_DURATION`, `*_DURATION`, and the numeric-fallback cases).

Licensing
---------
Remotion is free for individuals and for companies of up to three people, and
paid above that. This repo is rendered by its author as an individual, so the
free tier applies. That is a fact about who runs it, not a property of the code,
so `platform/doctor.py` reports the renderer's licence state alongside the
`video-talkcraft` PolyForm Noncommercial blocker rather than quietly allowing it.
"""

from __future__ import annotations

import argparse
import json
import shutil
import sqlite3
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TEMPLATE = ROOT / "upstream" / "video-shotcraft" / "template"
DEMOS = ROOT / "upstream" / "video-shotcraft" / "demos"
WORK = ROOT / "platform" / "render" / ".work"
OUT = ROOT / "render" / "out"
DB = ROOT / "platform" / "db" / "shotcraft.db"
REPORT = ROOT / "platform" / "render" / "render_report.json"

FPS = 30
DESIGN_W, DESIGN_H = 480, 270   # the demos draw into a 480x270 DesignStage


def log(*a) -> None:
    print(*a, flush=True)


def compositions() -> list[dict]:
    """Every demo component with its duration and category, from the database."""
    if not DB.exists():
        raise SystemExit("no database; run platform/ingest/run.py")
    conn = sqlite3.connect(f"file:{DB.as_posix()}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    rows = []
    for r in conn.execute("""
            SELECT st.key, st.component_name, st.demo_path, st.duration_frames,
                   st.uses_normalized_t, st.design_stage,
                   c.key AS category, sc.name AS card
            FROM style st
            JOIN card_variant v ON v.style_id = st.id
            JOIN shot_card sc ON sc.id = v.card_id
            JOIN category c ON c.id = sc.category_id
            WHERE st.component_name IS NOT NULL AND st.demo_path IS NOT NULL
            ORDER BY c.key, st.key"""):
        rows.append(dict(r))
    conn.close()
    return rows


DEFAULT_FRAMES = FPS   # only used under --include-unspecified, and labelled


def duration_of(row: dict) -> "int | None":
    """The component's stated length in frames, or None if it states none.

    None is a real answer and it is load-bearing. 93 of the 218 demo components
    export no duration at all: they are fragments meant to be placed inside a
    timeline, not standalone films. The seven that export something
    duration-shaped export `BEAT_LEN=18`, `FPS=30`, `SEG_LEN=50`, `LEN=252` --
    none of which is a length, and `FPS=30` is the one that would have been
    silently wrong most often.

    Rendering those at a guessed frame count produces a clip of the wrong size
    that looks fine in a file listing, which is the "plausible string in an
    untested cell" failure this project has refused everywhere else. So they are
    not rendered by default and the gap is reported.
    """
    d = row.get("duration_frames")
    return int(d) if d and d > 0 else None


def prepare() -> Path:
    """Copy the template and the demos into the gitignored work directory."""
    WORK.mkdir(parents=True, exist_ok=True)
    for name in ("src", "themes", "public", "scripts"):
        s = TEMPLATE / name
        if s.is_dir():
            shutil.copytree(s, WORK / name, dirs_exist_ok=True)
    for f in ("package.json", "tsconfig.json", "remotion.config.ts"):
        if (TEMPLATE / f).exists():
            shutil.copy2(TEMPLATE / f, WORK / f)
    shutil.copytree(DEMOS, WORK / "demos", dirs_exist_ok=True)
    return WORK


REGISTRY_TSX = '''// GENERATED by platform/render/run.py. One Composition per demo.
//
// The list is written from the database, not discovered at runtime, so a demo
// that fails to import is a build error rather than a silently missing clip.
import {{ Composition }} from 'remotion';
import React from 'react';
{imports}
export const Root: React.FC = () => (
  <>
{comps}
  </>
);
'''


def write_registry(rows: list[dict], work: Path) -> tuple[Path, list[dict]]:
    comps, imports, problems = [], [], []
    for r in rows:
        key = r["key"]
        # The ingest recorded the demo's real path, so this never has to guess
        # the directory name from the kebab key -- which it did at first, and
        # which is wrong for every style whose folder is not its slug.
        rel = "../" + str(r["demo_path"]).replace("\\", "/").lstrip("./")
        target = work / str(r["demo_path"]).replace("\\", "/")
        if not target.exists():
            problems.append(f"{key}: demo_path {r['demo_path']} not in the work dir")
            continue
        name = r["component_name"]
        frames = duration_of(r) or DEFAULT_FRAMES
        comps.append(
            f'    <Composition id="{key}" component={{{name}}} '
            f'durationInFrames={{{frames}}} fps={{{FPS}}} '
            f'width={{{DESIGN_W}}} height={{{DESIGN_H}}} />')
        imports.append(f"import {{ {name} }} from '{rel}';")
    src = REGISTRY_TSX.format(imports="\n".join(imports), comps="\n".join(comps))
    p = work / "src" / "Root.render.tsx"
    p.write_text(src, encoding="utf-8")
    entry = work / "src" / "index.render.ts"
    entry.write_text(
        "import { registerRoot } from 'remotion';\n"
        "import { Root } from './Root.render';\n"
        "registerRoot(Root);\n", encoding="utf-8")
    tsconfig = work / "tsconfig.json"
    if tsconfig.exists():
        t = tsconfig.read_text(encoding="utf-8")
        if '"demos/**/*"' not in t:
            t = t.replace('"include"', '"include": ["demos/**/*"],\n  "x"', 1)
            tsconfig.write_text(t, encoding="utf-8")
    return p, problems


def npm_exe() -> str:
    """The npm launcher, which on Windows is a `.cmd` shim.

    `subprocess.run(["npm", ...])` raises FileNotFoundError here, and the error
    names the wrong thing -- it looks like npm is missing when it is on PATH and
    working. Resolution order is deliberate: the npx that sits next to the node
    that is running, then PATH.
    """
    import os
    import shutil
    node = shutil.which("node")
    if node:
        base = Path(node).parent
        for cand in ("npm.cmd", "npm.exe", "npm"):
            if (base / cand).exists():
                return str(base / cand)
    found = shutil.which("npm.cmd") or shutil.which("npm")
    if found:
        return found
    # A last resort that also covers a broken PATH: drive the shell.
    return "cmd /c npm"


def _run(exe: str, args: list[str], cwd: Path | None, timeout: int) -> subprocess.CompletedProcess:
    if exe.startswith("cmd "):
        return subprocess.run(f'{exe} {" ".join(args)}', cwd=str(cwd or WORK),
                              capture_output=True, text=True, encoding="utf-8",
                              errors="replace", timeout=timeout, shell=True)
    return subprocess.run([exe, *args], cwd=str(cwd or WORK),
                          capture_output=True, text=True, encoding="utf-8",
                          errors="replace", timeout=timeout)


def npx_exe() -> str:
    """The npx launcher, resolved the same way as npm."""
    import shutil
    from pathlib import Path as _P
    node = shutil.which("node")
    if node:
        base = _P(node).parent
        for cand in ("npx.cmd", "npx.exe", "npx"):
            if (base / cand).exists():
                return str(base / cand)
    found = shutil.which("npx.cmd") or shutil.which("npx")
    if found:
        return found
    return "cmd /c npx"


def npm(*args: str, cwd: Path | None = None, timeout: int = 1800) -> subprocess.CompletedProcess:
    return _run(npm_exe(), list(args), cwd, timeout)


def npx(*args: str, cwd: Path | None = None, timeout: int = 1800) -> subprocess.CompletedProcess:
    """Run a *local* binary.

    `npm remotion render ...` fails with `Unknown command: "remotion"` --
    remotion is installed into node_modules/.bin, not registered as an npm
    script, so the render has to go through npx. The first version of this file
    used npm for everything and reported that message as the render's error,
    which sent the diagnosis after the wrong subsystem entirely.
    """
    return _run(npx_exe(), list(args), cwd, timeout)


def external_imports(work: Path) -> list[str]:
    """Every non-relative module the demo corpus imports.

    Discovered rather than assumed. The template's `package.json` declares six
    packages and the demos import a seventh: `@remotion/motion-blur`, in 8 files.
    Rendering a corpus whose dependency list is taken on faith produces a wall of
    `Module not found` and a report full of `failed` with no explanation, which
    is what the first full run did.
    """
    import re
    mods: set[str] = set()
    for p in sorted((work / "demos").rglob("*.tsx")):
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for m in re.finditer(r"""from\s+['"]([^'"]+)['"]|require\(['"]([^'"]+)['"]\)""",
                             text):
            spec = m.group(1) or m.group(2)
            if spec.startswith(".") or spec.startswith("/"):
                continue
            mods.add("/".join(spec.split("/")[:2]) if spec.startswith("@")
                     else spec.split("/")[0])
    return sorted(mods)


def ensure_dependencies(work: Path) -> tuple[list[str], list[str]]:
    """Add any module the corpus imports but the template does not declare.

    Versions are pinned to whatever `remotion` itself is on, because a motion
    package built against a different Remotion version fails at render time with
    a hook error rather than an import error.
    """
    pkg_path = work / "package.json"
    pkg = json.loads(pkg_path.read_text(encoding="utf-8"))
    declared = set(pkg.get("dependencies", {})) | set(pkg.get("devDependencies", {}))
    rm = pkg.get("dependencies", {}).get("remotion", "")
    major_minor = ".".join(rm.split(".")[:2]) if rm else ""
    added = []
    for mod in external_imports(work):
        if mod in declared:
            continue
        version = f"{major_minor}.x" if major_minor and mod.startswith("@remotion/") \
            else "latest"
        pkg.setdefault("dependencies", {})[mod] = version
        added.append(f"{mod}@{version}")
    if added:
        pkg_path.write_text(json.dumps(pkg, ensure_ascii=False, indent=2) + "\n",
                            encoding="utf-8")
    return added, sorted(declared | set(pkg["dependencies"]))


def cmd_install(a) -> int:
    work = prepare()
    added, deps = ensure_dependencies(work)
    log(f"dependencies: {', '.join(deps)}")
    if added:
        log(f"  added because the demos import them and the template does not "
            f"declare them: {', '.join(added)}")
    log("installing (this is the slow part)…")
    t0 = time.time()
    r = npm("install", "--no-audit", "--no-fund")
    log(f"  npm install -> {r.returncode} in {time.time() - t0:.0f}s")
    if r.returncode:
        log((r.stdout or "")[-1500:])
        log((r.stderr or "")[-2500:])
        return 1
    log("remotion:", npm("ls", "remotion", "--depth", "0").stdout.strip()[:200])
    return 0


def cmd_list(a) -> int:
    rows = compositions()
    log(f"{len(rows)} compositions from the database")
    yes = [r for r in rows if duration_of(r)]
    no = [r for r in rows if duration_of(r) is None]
    log(f"  {len(yes)} state a duration and are renderable as-is")
    log(f"  {len(no)} state none -- timeline fragments, not standalone films; "
        f"rendered only under --include-unspecified")
    for r in rows[:a.limit]:
        log(f"  {r['key']:<34} {str(duration_of(r) or '—'):>5}f  {r['category']:<12} {r['component_name']}")
    if a.limit:
        log(f"  … {len(rows)} total")
    return 0


def cmd_render(a) -> int:
    if not (WORK / "node_modules").is_dir():
        log("work directory has no node_modules; run --install first")
        return 2
    rows = compositions()
    if not a.include_unspecified:
        skipped = [r for r in rows if duration_of(r) is None]
        rows = [r for r in rows if duration_of(r) is not None]
        if skipped and not a.render:
            log(f"  {len(skipped)} component(s) state no duration and are NOT "
                f"rendered by default;")
            log(f"  they are timeline fragments, not films. "
                f"--include-unspecified renders them at "
                f"{DEFAULT_FRAMES}f and labels every one.")
    if a.render:
        rows = [r for r in rows if r["key"] in set(a.render)]
        if not rows:
            log(f"no such composition: {a.render}")
            return 1
    if a.limit:
        rows = rows[:a.limit]
    reg, problems = write_registry(rows, WORK)
    if problems:
        for p in problems[:8]:
            log("  !", p)
    if not reg.exists():
        return 1
    OUT.mkdir(parents=True, exist_ok=True)

    scale = f"--scale={a.scale}" if a.scale and a.scale != 1 else ""
    quality = a.quality
    results = []
    for i, r in enumerate(rows, 1):
        dest = OUT / f"{r['key']}.mp4"
        if dest.exists() and dest.stat().st_size > 1000 and not a.force:
            log(f"  [{i}/{len(rows)}] {r['key']:<34} cached")
            results.append({**r, "status": "cached", "bytes": dest.stat().st_size})
            continue
        t0 = time.time()
        cmd = ["remotion", "render", "src/index.render.ts", r["key"], str(dest)]
        if scale:
            cmd.append(scale)
        if quality != "default":
            cmd += ["--crf", str(quality)]
        cmd += ["--log", "error"]
        p = npx(*cmd, timeout=a.timeout)
        ok = p.returncode == 0 and dest.exists() and dest.stat().st_size > 1000
        log(f"  [{i}/{len(rows)}] {r['key']:<34} "
            f"{'ok' if ok else 'FAIL'} {time.time() - t0:5.1f}s "
            f"{(dest.stat().st_size / 1024 if dest.exists() else 0):.0f} KB")
        if not ok:
            log("      " + (p.stderr or p.stdout or "").strip().splitlines()[-1][:200]
                if (p.stderr or p.stdout) else "")
        results.append({**r, "status": "ok" if ok else "failed",
                        "seconds": round(time.time() - t0, 1),
                        "bytes": dest.stat().st_size if dest.exists() else 0,
                        "error": "" if ok else (p.stderr or p.stdout or "")[-400:]})

    write_report(results, a)
    failed = [r for r in results if r["status"] == "failed"]
    log(f"\n{len(results) - len(failed)}/{len(results)} rendered, "
        f"output in render/out/")
    return 1 if failed else 0


def write_report(results: list[dict], a) -> None:
    ok = [r for r in results if r["status"] in ("ok", "cached")]
    rep = {
        "renderer": "remotion",
        "remotion_version": _remotion_version(),
        "fps": FPS,
        "design_stage": [DESIGN_W, DESIGN_H],
        "scale": a.scale,
        "rendered": len(ok),
        "failed": len(results) - len(ok),
        "total_bytes": sum(r.get("bytes", 0) for r in ok),
        "total_seconds": round(sum(r.get("seconds", 0) for r in ok), 1),
        "licence": {
            "remotion": "free for individuals and companies of up to three people; "
                        "paid above that. This repo is rendered by its author as an "
                        "individual, so the free tier applies. That is a fact about "
                        "who runs the render, not about the code.",
            "video_talkcraft": "PolyForm Noncommercial -- still a blocker for "
                               "anything we deliver to a paying client",
        },
        "clips": [{k: r.get(k) for k in
                   ("key", "component_name", "category", "status", "bytes", "seconds",
                    "duration_frames", "error")} for r in results],
    }
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(rep, ensure_ascii=False, indent=2) + "\n",
                      encoding="utf-8")
    log(f"report: platform/render/render_report.json")


def _remotion_version() -> str:
    p = WORK / "node_modules" / "remotion" / "package.json"
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8")).get("version", "?")
    return "not installed"


def ffprobe(path: Path) -> dict | None:
    """Stream facts from ffprobe, or None if it is unavailable or fails.

    Checking for an `ftyp` box proves the file is an MP4. It does not prove the
    clip is the right length, and a render that silently used the wrong
    `durationInFrames` produces a file that passes every byte-level check while
    showing the wrong thing. So the frame count is read back and compared with
    what the database said.
    """
    exe = shutil.which("ffprobe")
    if not exe:
        return None
    p = subprocess.run(
        [exe, "-v", "error", "-select_streams", "v:0",
         "-count_frames",
         "-show_entries", "stream=nb_read_frames,width,height,r_frame_rate",
         "-show_entries", "format=duration", "-of", "json", str(path)],
        capture_output=True, text=True, encoding="utf-8", errors="replace")
    if p.returncode:
        return None
    try:
        data = json.loads(p.stdout)
        st = (data.get("streams") or [{}])[0]
        return {
            "frames": int(st.get("nb_read_frames") or 0),
            "width": st.get("width"),
            "height": st.get("height"),
            "fps": st.get("r_frame_rate"),
            "seconds": float((data.get("format") or {}).get("duration") or 0),
        }
    except (json.JSONDecodeError, ValueError, IndexError):
        return None


def cmd_verify(a) -> int:
    """Every claimed clip exists, is a real MP4, and is the stated length."""
    scale = getattr(a, "scale", 1) or 1
    if not REPORT.exists():
        log("no render report; nothing to verify")
        return 1
    rep = json.loads(REPORT.read_text(encoding="utf-8"))
    clips = [c for c in rep["clips"] if c["status"] in ("ok", "cached")]
    log(f"report claims {len(clips)} rendered clips "
        f"(remotion {rep['remotion_version']}, scale {rep['scale']})")
    bad: list[str] = []
    probed = 0
    for c in clips:
        p = OUT / f"{c['key']}.mp4"
        if not p.exists():
            bad.append(f"{c['key']}: report says rendered, file is absent")
            continue
        head = p.read_bytes()[:12]
        if b"ftyp" not in head:
            bad.append(f"{c['key']}: not an MP4 (no ftyp box)")
            continue
        if p.stat().st_size < 1000:
            bad.append(f"{c['key']}: {p.stat().st_size} bytes is not a video")
            continue
        info = ffprobe(p)
        if not info:
            continue
        probed += 1
        want = c.get("duration_frames")
        # A stated duration must match the render exactly. An unspecified one
        # was rendered at the floor and the report already says so.
        if want and info["frames"] and abs(info["frames"] - int(want)) > 1:
            bad.append(f"{c['key']}: rendered {info['frames']} frames, "
                       f"the index states {want}")
        if info["width"] and info["height"] and \
                (info["width"], info["height"]) != (DESIGN_W * scale,
                                                   DESIGN_H * scale):
            bad.append(f"{c['key']}: {info['width']}x{info['height']}, expected "
                       f"{DESIGN_W * scale}x{DESIGN_H * scale}")
    for b in bad[:10]:
        log("  !", b)
    log(f"{len(clips) - len(bad)}/{len(clips)} clips verified on disk"
        + (f"; {probed} probed with ffprobe" if probed else ""))
    if clips and not bad:
        total = sum(p.stat().st_size for p in OUT.glob("*.mp4"))
        log(f"  {len(list(OUT.glob('*.mp4')))} files, {total / 1e6:.1f} MB")
    return 1 if bad else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--install", action="store_true")
    ap.add_argument("--render", nargs="*", metavar="STYLE", default=None,
                    help="render these styles; with no names, every style "
                         "that states a duration")
    ap.add_argument("--render-all", action="store_true")
    ap.add_argument("--verify", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--scale", type=int, default=1)
    ap.add_argument("--quality", default="18",
                    help="crf for libx264; lower is better quality and a bigger file")
    ap.add_argument("--timeout", type=int, default=600)
    ap.add_argument("--include-unspecified", action="store_true",
                    help="also render components that state no duration, at "
                         "the 30-frame floor; the report labels every such clip")
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()
    if a.verify:
        return cmd_verify(a)
    if a.install:
        return cmd_install(a)
    # `a.render` is None when the flag was absent and [] when it was given with
    # no names. Only the first means "not asked".
    if a.list or (a.render is None and not a.render_all):
        return cmd_list(a)
    a.render = a.render or []
    return cmd_render(a)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
