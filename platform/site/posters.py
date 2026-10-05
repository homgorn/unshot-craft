"""Generate a poster frame for every clip that lacks one.

    python platform/site/posters.py            # write into site/dist/media/poster/
    python platform/site/posters.py --check    # count only, change nothing

Why the posters are extracted rather than fetched
-------------------------------------------------
64 of the 214 clips had a poster, drawn by whoever produced the original
recording. The other 150 had none, and a `<video>` with no `poster` is a black
rectangle for as long as it takes to fetch and decode -- long enough that a
reader scrolling the library sees 97 black tiles and concludes the site is
broken. `preload="none"` makes it worse, not better: nothing arrives until the
IntersectionObserver fires.

The frame is taken from the clip itself, so the poster cannot disagree with the
video. The upstream posters stay where they exist: they are real design work, and
replacing them with an auto-extracted frame would be a downgrade dressed as a fix.

Frame choice
------------
A third of the way in, not the first frame and not the middle. Most of this
corpus animates *in* from an empty stage, so frame 0 is a blank canvas and the
poster would show nothing at all. One third in, the composition has assembled
and the motion has not yet resolved, which is the frame that tells a reader what
the shot is.

Clips shorter than 0.3 s have no third, so they take 60 % of their length. A clip
that cannot be read by `ffprobe` is reported and skipped rather than guessed at:
a poster extracted from the wrong frame is worse than no poster, because it
looks like the video does not show what it shows.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MEDIA = ROOT / "site" / "dist" / "media"
POSTER = MEDIA / "poster"

# Where in the clip to grab, as a fraction. See the module docstring.
FRACTION = 1 / 3
MIN_POS = 0.6          # seconds; below this a fraction is a better answer
QUALITY = "4"          # ffmpeg -q:v for mjpeg, 2 (best) .. 31 (worst)


def duration_of(path: Path) -> float | None:
    exe = shutil.which("ffprobe")
    if not exe:
        return None
    p = subprocess.run(
        [exe, "-v", "error", "-show_entries", "format=duration", "-of", "json",
         str(path)], capture_output=True, text=True, errors="replace", timeout=60)
    try:
        return float(json.loads(p.stdout)["format"]["duration"])
    except (json.JSONDecodeError, KeyError, ValueError, subprocess.SubprocessError):
        return None


def ffmpeg_exe() -> str | None:
    return shutil.which("ffmpeg")


def grab(clip: Path, out: Path, seconds: float) -> tuple[bool, str]:
    exe = ffmpeg_exe()
    if not exe:
        return False, "ffmpeg is not on PATH"
    cmd = [exe, "-y", "-v", "error", "-ss", f"{seconds:.3f}", "-i", str(clip),
           "-frames:v", "1", "-q:v", QUALITY, str(out)]
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, errors="replace",
                           timeout=120)
    except subprocess.TimeoutExpired:
        return False, f"ffmpeg timed out after 120s"
    if p.returncode != 0:
        return False, (p.stderr or p.stdout or "").strip().splitlines()[-1][:160]
    if not out.exists() or out.stat().st_size < 1000:
        return False, f"wrote {out.stat().st_size if out.exists() else 0} bytes"
    return True, ""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--force", action="store_true",
                    help="re-extract even where a poster exists")
    a = ap.parse_args()

    if not MEDIA.is_dir():
        raise SystemExit("site/dist/media missing; run build_site.py")

    clips = sorted(MEDIA.glob("*.mp4"))
    if not clips:
        raise SystemExit("no clips in site/dist/media; "
                         "run `python platform/mirror_site.py --media`")

    POSTER.mkdir(parents=True, exist_ok=True)
    made = kept = skipped = 0
    problems: list[str] = []

    for clip in clips:
        out = POSTER / f"{clip.stem}.jpg"
        if out.exists() and out.stat().st_size > 1000 and not a.force:
            kept += 1
            continue
        if a.check:
            skipped += 1
            continue
        secs = duration_of(clip)
        if secs is None:
            problems.append(f"{clip.name}: ffprobe could not read its length")
            continue
        target = secs * FRACTION if secs < MIN_POS * 2 else max(MIN_POS, secs * FRACTION)
        ok, why = grab(clip, out, target)
        if ok:
            made += 1
        else:
            skipped += 1
            if len(problems) < 12:
                problems.append(f"{clip.name}: {why}")

    total = len(clips)
    have = len([p for p in POSTER.glob("*.jpg") if p.stat().st_size > 1000])
    if a.check:
        print(f"{have}/{total} clips have a poster "
              f"({round(100.0 * have / total) if total else 0}%)")
        return 0 if have == total else 1

    print(f"posters: {kept} kept, {made} extracted, {skipped} skipped, "
          f"{have}/{total} present")
    if problems:
        print("\nskipped:")
        for p in problems[:12]:
            print(f"  {p}")
    report = ROOT / "site" / "build" / "poster_report.json"
    report.write_text(json.dumps(
        {"clips": total, "posters": have, "extracted": made, "kept": kept,
         "skipped": skipped, "problems": problems}, ensure_ascii=False, indent=2)
        + "\n", encoding="utf-8")
    print(f"report: {report.relative_to(ROOT)}")
    # Not a failure. A clip ffmpeg cannot read is a gap in the corpus, and
    # `check_dist.py` reports poster coverage on every run, so a growing hole is
    # visible without making the build refuse to finish.
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())