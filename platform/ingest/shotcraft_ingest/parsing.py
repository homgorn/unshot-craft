"""Pure parsers for upstream video-shotcraft artifacts.

No third-party dependencies: the upstream format is regular enough that a
careful hand parser is more predictable than a YAML/JS engine, and it keeps the
whole ingest runnable on a bare Python 3.10+.
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass, field
from pathlib import Path

# ---------------------------------------------------------------------------
# frontmatter + markdown sections
# ---------------------------------------------------------------------------

FRONTMATTER_RE = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n?(.*)$", re.S)
SECTION_RE = re.compile(r"^##\s+(.+?)\s*$", re.M)


def split_frontmatter(text: str) -> tuple[dict[str, str], str]:
    """Return (frontmatter_dict, body). Frontmatter keys are Chinese; parse by
    key, never by position (upstream key order is not stable)."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    raw, body = m.group(1), m.group(2)
    fm: dict[str, str] = {}
    key: str | None = None
    for line in raw.splitlines():
        km = re.match(r"^([^\s:#][^:]*)\s*:\s*(.*)$", line)
        if km:
            key = km.group(1).strip()
            fm[key] = km.group(2).strip()
        elif key and line.strip():
            fm[key] = (fm[key] + " " + line.strip()).strip()
    return fm, body


# Heading -> normalized kind. Order matters: the first match wins.
SECTION_KINDS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"^意图"), "intention"),
    (re.compile(r"^动效核心"), "motion"),
    (re.compile(r"^动作阶段"), "phases"),
    (re.compile(r"(式选型|选型表|选型)"), "variants"),
    (re.compile(r"^段位表"), "stages"),
    (re.compile(r"^参数表"), "params"),
    (re.compile(r"^填空流程"), "fill"),
    (re.compile(r"^声音"), "sound"),
    (re.compile(r"^已知坑"), "pitfalls"),
    (re.compile(r"^参考实现"), "impl"),
]


def section_kind(heading: str) -> str:
    for pat, kind in SECTION_KINDS:
        if pat.search(heading):
            return kind
    return "other"


def parse_sections(body: str) -> list[tuple[str, str, str]]:
    """-> [(heading, kind, body)] in document order."""
    marks = [(m.start(), m.end(), m.group(1)) for m in SECTION_RE.finditer(body)]
    out: list[tuple[str, str, str]] = []
    for i, (_s, e, heading) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(body)
        out.append((heading, section_kind(heading), body[e:end].strip()))
    return out


def parse_md_table(section_body: str) -> list[list[str]]:
    """Markdown table -> list of row cell-lists, header row dropped."""
    rows: list[list[str]] = []
    for line in section_body.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if all(re.fullmatch(r":?-{2,}:?", c or "-") for c in cells):
            continue
        rows.append(cells)
    return rows[1:] if rows else []


def parse_bullets(section_body: str) -> list[str]:
    """Ordered/unordered list items, one level deep."""
    out = []
    for line in section_body.splitlines():
        m = re.match(r"^\s*(?:[-*]\s+|\d+[.)]\s+)(.+)$", line)
        if m:
            out.append(m.group(1).strip())
    return out


# ---------------------------------------------------------------------------
# duration / energy normalization
# ---------------------------------------------------------------------------

FRAMES_RE = re.compile(r"(\d{2,4})\s*f\b")
SECONDS_RE = re.compile(r"(\d+(?:\.\d+)?)\s*s\b")


def parse_duration(text: str) -> int | None:
    """Frames @30fps. None for technique cards (时长: n/a（技法卡…）)."""
    if not text or "n/a" in text.lower():
        return None
    m = FRAMES_RE.search(text)
    if m:
        return int(m.group(1))
    s = SECONDS_RE.search(text)
    return int(round(float(s.group(1)) * 30)) if s else None


ENERGY_LADDER: list[tuple[str, int, str]] = [
    ("峰值", 8, "peak"),
    ("极高", 7, "very-high"),
    ("高", 6, "high"),
    ("中高", 5, "mid-high"),
    ("中低", 3, "mid-low"),
    ("低中", 2, "low-mid"),
    ("中", 4, "mid"),
    ("低", 1, "low"),
]

# directional shapes: 低开缓升, 低起中收, 低→瞬时中→低, 高开中收, 低压升 ...
ARC_RE = re.compile(r"(开|起|收)|→|⇄|\^|\^|\bfrom\b")


def split_energy(text: str) -> tuple[str | None, str, str | None]:
    """-> (level_key, level_zh, rationale). level_key is None for arc text and
    for n/a technique cards; the verbatim string is always kept by the caller."""
    if not text:
        return None, "", None
    rationale = ""
    m = re.search(r"[（(]([^）)]*)[）)]", text)
    if m:
        rationale = m.group(1).strip()
        head = text[: m.start()].strip()
    else:
        head = text.strip()
    if not head or head.lower().startswith("n/a"):
        return None, head, rationale or None
    if ARC_RE.search(head):
        return None, head, rationale or None
    for zh, rank, key in ENERGY_LADDER:
        if head == zh or head.startswith(zh):
            return key, zh, rationale or None
    return None, head, rationale or None


# ---------------------------------------------------------------------------
# JavaScript object literals (translations.js, showcase.js)
# ---------------------------------------------------------------------------

JS_PAIR_RE = re.compile(r"'((?:[^'\\]|\\.)*)'\s*:\s*'((?:[^'\\]|\\.)*)'")
JS_BARE_RE = re.compile(r'([A-Za-z_$][\w$]*)\s*:\s*"((?:[^"\\]|\\.)*)"')


def unescape_js(s: str) -> str:
    return (
        s.replace("\\'", "'")
        .replace('\\"', '"')
        .replace("\\/", "/")
        .replace("\\n", "\n")
        .replace("\\\\", "\\")
    )


def block_at(text: str, brace_idx: int) -> tuple[str, int]:
    """Return (contents, index_after) of the {...} starting at brace_idx.
    Brace counting skips single- and double-quoted strings."""
    assert text[brace_idx] == "{"
    depth = 0
    i = brace_idx
    n = len(text)
    quote: str | None = None
    while i < n:
        ch = text[i]
        if quote:
            if ch == "\\":
                i += 2
                continue
            if ch == quote:
                quote = None
        elif ch in "'\"`":
            quote = ch
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return text[brace_idx + 1 : i], i + 1
        i += 1
    return text[brace_idx + 1 :], n


def parse_js_map(segment: str) -> dict[str, str]:
    """Flat {'k': 'v', ...} or {k: "v"} object -> dict."""
    out: dict[str, str] = {}
    for k, v in JS_PAIR_RE.findall(segment):
        out[unescape_js(k)] = unescape_js(v)
    if not out:
        for k, v in JS_BARE_RE.findall(segment):
            out[k] = v.replace('\\"', '"')
    return out


def top_level_member(text: str, key: str) -> str | None:
    """Contents of `key: { ... }` at the given brace depth."""
    for m in re.finditer(rf"(?m)^\s*{re.escape(key)}\s*:\s*\{{", text):
        seg, _ = block_at(text, m.end() - 1)
        return seg
    return None


# ---------------------------------------------------------------------------
# misc
# ---------------------------------------------------------------------------


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


@dataclass
class Card:
    name: str
    category: str
    summary: str = ""
    use: str = ""
    duration_text: str = ""
    duration_frames: int | None = None
    energy_text: str = ""
    energy_key: str | None = None
    energy_zh: str = ""
    energy_rationale: str | None = None
    intention: str = ""
    tags: list[str] = field(default_factory=list)
    sections: list[tuple[str, str, str]] = field(default_factory=list)
    params: list[tuple[str, str, str, str | None]] = field(default_factory=list)
    pitfalls: list[tuple[str, bool, str | None]] = field(default_factory=list)
    variants: list[tuple[str, str | None]] = field(default_factory=list)  # (style_key, letter)
    impl_paths: list[str] = field(default_factory=list)
    source_path: str = ""
    bytes: int = 0
    sha256: str = ""

    @property
    def extras(self) -> dict[str, str]:
        return {"duration_frames": str(self.duration_frames or "")}


def parse_card(path: Path, category: str, repo_rel: str) -> Card:
    text = path.read_text(encoding="utf-8")
    fm, body = split_frontmatter(text)
    card = Card(
        name=fm.get("name", path.stem),
        category=category,
        summary=fm.get("一句话", ""),
        use=fm.get("适用", ""),
        duration_text=fm.get("时长", ""),
        energy_text=fm.get("能量", ""),
        source_path=repo_rel,
        bytes=len(text.encode("utf-8")),
    )
    card.duration_frames = parse_duration(card.duration_text)
    card.energy_key, card.energy_zh, card.energy_rationale = split_energy(card.energy_text)
    raw_tags = fm.get("标签", "")
    card.tags = [t for t in re.split(r"[,，、\s]+", raw_tags) if t]

    card.sections = parse_sections(body)
    for heading, kind, sec_body in card.sections:
        if kind == "intention":
            card.intention = re.sub(r"\s+", " ", sec_body).strip()
        elif kind == "params":
            for row in parse_md_table(sec_body):
                if len(row) >= 2:
                    card.params.append((row[0], row[1], row[2] if len(row) > 2 else "", None))
        elif kind == "pitfalls":
            for item in parse_bullets(sec_body):
                crit = "命门" in item
                refs = sorted(set(re.findall(r"\b([RQSPC]\d{1,2})\b", item)))
                card.pitfalls.append((item, crit, ",".join(refs) or None))
        elif kind == "variants":
            for row in parse_md_table(sec_body):
                if not row:
                    continue
                letter = None
                m = re.match(r"^([A-Z])\s+(?:[A-Z]\s+)?([a-z0-9][a-z0-9-]+)", row[0])
                if m:
                    letter, slug = m.group(1), m.group(2)
                    card.variants.append((slug, letter))
                for slug in re.findall(r"[a-z0-9]+(?:-[a-z0-9]+)+", row[0]):
                    if not card.variants or card.variants[-1][0] != slug:
                        card.variants.append((slug, letter))
        elif kind == "impl":
            card.impl_paths = re.findall(r"demos/[a-z0-9\-_/]+", sec_body)
            card.impl_paths += re.findall(r"template/src/[A-Za-z0-9_/\.\-]+", sec_body)
    return card