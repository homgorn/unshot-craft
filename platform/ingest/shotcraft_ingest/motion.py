"""Extract real motion parameters out of the upstream Remotion demos.

Nothing upstream exposes these as data: the tuned easing curves, spring
configs, segment windows and decay envelopes only exist as literals inside
`demos/**/*.tsx`. This module turns them into rows in `motion_param` so they can
be indexed, ranked and reused.

Strategy is regex, not AST — the TSX is machine-generated-ish and consistent,
and a regex pass is auditable (every row keeps its source line). We deliberately
keep `E.spring(...)` (the analytic spring of demos/_fixtures/Motion.tsx) and
Remotion's `spring({config})` as distinct kinds: they are not the same thing.
"""

from __future__ import annotations

import re
from pathlib import Path

DURATION_RE = re.compile(r"export\s+const\s+(\w+_(?:DURATION|DUR|FRAMES))\s*(?::\s*number\s*)?=\s*(\d+)")
COMPONENT_RE = re.compile(r"export\s+const\s+(\w+)\s*:\s*(?:React\.)?(?:FC|memo)\s*(?:<[^>]*>)?\s*=")
BEZIER_RE = re.compile(r"Easing\.bezier\(\s*([-\d.]+)\s*,\s*([-\d.]+)\s*,\s*([-\d.]+)\s*,\s*([-\d.]+)\s*\)")
EASING_FN_RE = re.compile(r"Easing\.(inOut|in|out)\(\s*Easing\.(\w+)\s*\(?\s*([-\d.]*)\s*\)?\s*\)")
EASING_BARE_RE = re.compile(r"easing\s*:\s*Easing\.(quad|cubic|quartic|quint|expo|circ|back|elastic|bounce|sine|linear)")
SPRING_CFG_RE = re.compile(
    r"spring\(\s*\{(.*?)\}\s*\)", re.S)
INTERPOLATE_RE = re.compile(
    r"interpolate\(\s*(\w+)\s*,\s*\[([^\]]*)\]\s*,\s*\[([^\]]*)\]\s*,?\s*(\{[^}]*\})?", re.S)
SEGMENT_RE = re.compile(
    r"seg\(\s*(\w+)\s*,\s*([^,()]+?)\s*,\s*([^,()]+?)\s*(?:,\s*(E\.\w+|\w+))?\s*\)")
EXP_RE = re.compile(r"Math\.exp\(-?[^()]{0,24}\)")
SIN_RE = re.compile(r"Math\.sin\([^()]{0,24}\)")
MOTION_BLUR_RE = re.compile(r"shutterAngle=\{(\d+)\}\s*samples=\{(\d+)\}")
NORMALIZED_T_RE = re.compile(r"_fixtures/Motion")
DESIGN_STAGE_RE = re.compile(r"<DesignStage")
USE_VIDEO_CONFIG_RE = re.compile(r"useVideoConfig\(\)")
SPRING_FIELDS = {
    "damping": re.compile(r"damping\s*:\s*([-\d.]+)"),
    "stiffness": re.compile(r"stiffness\s*:\s*([-\d.]+)"),
    "mass": re.compile(r"mass\s*:\s*([-\d.]+)"),
    "durationInFrames": re.compile(r"durationInFrames\s*:\s*(\d+)"),
}
# module-scope easing constants must be resolved before scanning usages
EASE_CONST_RE = re.compile(
    r"(?:const|let)\s+(\w*[Ee]ase\w*|glide|flipEase)\s*(?::[^=]+)?=\s*(Easing\.[^;]+);")
COLOR_RE = re.compile(r"(?:const\s+)?(?:const\s+)?(BG|INK|ACCENT|AMBER|WHITE|BLACK|MID|GRAY)\s*=\s*['\"](#[0-9a-fA-F]{3,8})['\"]")


def line_of(src: str, pos: int) -> int:
    return src.count("\n", 0, pos) + 1


def _arg_list(text: str) -> list[str]:
    return [a.strip() for a in text.split(",") if a.strip()]


def extract_motion_params(src: str) -> list[dict]:
    """-> list of {kind, name, args, detail, line, raw}"""
    out: list[dict] = []

    def add(kind: str, name: str | None, args: dict, pos: int, detail: str = ""):
        line_start = src.rfind("\n", 0, pos) + 1
        line_end = src.find("\n", pos)
        raw = src[line_start: line_end if line_end != -1 else len(src)].strip()[:400]
        out.append(
            {
                "kind": kind,
                "name": name,
                "args": args,
                "detail": detail,
                "line": line_of(src, pos),
                "raw": raw,
            }
        )

    for m in BEZIER_RE.finditer(src):
        x1, y1, x2, y2 = (float(g) for g in m.groups())
        add(
            "bezier",
            None,
            {"x1": x1, "y1": y1, "x2": x2, "y2": y2},
            m.start(),
            "overshoot" if y1 > 1 else "standard",
        )

    for m in EASING_FN_RE.finditer(src):
        mode, base, arg = m.group(1), m.group(2), m.group(3)
        add("easing_fn", None, {"mode": mode, "base": base, "arg": arg or None}, m.start(),
            f"{mode}({base})")

    for m in EASING_BARE_RE.finditer(src):
        add("easing_fn", None, {"mode": None, "base": m.group(1), "arg": None}, m.start(), m.group(1))

    for m in SPRING_CFG_RE.finditer(src):
        blob = m.group(1)
        args: dict[str, float] = {}
        for field, pat in SPRING_FIELDS.items():
            hit = pat.search(blob)
            if hit:
                args[field] = int(hit.group(1)) if field == "durationInFrames" else float(hit.group(1))
        if args:
            parts = [f"{k} {v:g}" for k, v in args.items()]
            add("spring", None, args, m.start(), "spring: " + ", ".join(parts))

    for m in INTERPOLATE_RE.finditer(src):
        add("interpolate", m.group(1),
            {"input": m.group(1), "inputRange": _arg_list(m.group(2)),
             "outputRange": _arg_list(m.group(3)),
             "opts": re.sub(r"\s+", " ", m.group(4) or "").strip()},
            m.start())

    for m in SEGMENT_RE.finditer(src):
        add("segment", m.group(1),
            {"input": m.group(1), "from": m.group(2).strip(), "to": m.group(3).strip(),
             "ease": (m.group(4) or "E.linear")},
            m.start())

    for m in EASE_CONST_RE.finditer(src):
        add("easing_const", m.group(1), {"expr": re.sub(r"\s+", " ", m.group(2))}, m.start())

    for m in EXP_RE.finditer(src):
        add("exp_decay", None, {"expr": m.group(0)}, m.start())

    for m in SIN_RE.finditer(src):
        add("sin", None, {"expr": m.group(0)}, m.start())

    for m in MOTION_BLUR_RE.finditer(src):
        add("motion_blur", None,
            {"shutterAngle": int(m.group(1)), "samples": int(m.group(2))}, m.start())

    for m in COLOR_RE.finditer(src):
        add("color", m.group(1), {"value": m.group(2)}, m.start())

    for m in DURATION_RE.finditer(src):
        add("constant", m.group(1), {"value": int(m.group(2)), "unit": "frames"}, m.start())

    # de-dup identical (kind, raw) pairs from overlapping patterns
    seen: set[tuple[str, str]] = set()
    unique: list[dict] = []
    for item in out:
        key = (item["kind"], item["raw"])
        if key in seen:
            continue
        seen.add(key)
        unique.append(item)
    return unique


def kebab(stem: str) -> str:
    """PascalCase -> kebab-case, digit-aware: Basic3DScene -> basic-3-d-scene."""
    s = re.sub(r"([A-Za-z])(\d)", r"\1-\2", stem)
    s = re.sub(r"(\d)([A-Za-z])", r"\1-\2", s)
    return re.sub(r"([a-z])([A-Z])", r"\1-\2", s).lower()


def norm(s: str) -> str:
    """Upstream's fuzzy key normaliser (workbench/scripts/gen-index.mjs:18)."""
    return re.sub(r"[^a-z0-9]", "", s.lower())


def scan_demo(path: Path) -> dict:
    src = path.read_text(encoding="utf-8")
    normalized_t = bool(NORMALIZED_T_RE.search(src))
    duration: int | None = None
    duration_source = None
    m = DURATION_RE.search(src)
    if m:
        duration, duration_source = int(m.group(2)), "_DURATION/_DUR export"
    else:
        for pat in (r"const\s+\w*(?:DUR|FRAMES|TOTAL|END)\w*\s*=\s*(\d{2,4})\s*;",
                    r"const\s+(\d{2,4})\s*=\s*\d+\s*;.*total"):
            mm = re.search(pat, src)
            if mm:
                duration, duration_source = int(mm.group(1)), "const scan"
                break
    cm = COMPONENT_RE.search(src)
    return {
        "duration_frames": duration,
        "duration_source": duration_source,
        "component_name": cm.group(1) if cm else None,
        "family": "A" if normalized_t else "B",
        "uses_normalized_t": 1 if normalized_t else 0,
        "design_stage": 480 if DESIGN_STAGE_RE.search(src) else None,
        "params": extract_motion_params(src),
        "bytes": len(src.encode("utf-8")),
    }