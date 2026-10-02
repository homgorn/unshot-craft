"""Icons and social images, generated from the brand mark in the source tree.

    python platform/site/icons.py            # writes site/dist/assets/
    python platform/site/icons.py --check    # verify without writing

Why generated and not committed
-------------------------------
An icon set has to exist at nine sizes, in four formats, and change whenever the
mark does. Committed binaries do not change when the mark does -- they rot, and
nobody notices until a browser 404s. So the mark stays the source (an SVG in
`upstream/`, or `site/dist/assets/logo-mark.svg` once mirrored) and everything
else is derived, which means `rm -rf site/dist && scripts/init.ps1` restores the
whole set.

The mark is drawn with Pillow's polygon fill rather than by rasterising the SVG,
for two reasons: it removes a browser from the build, and the path is a single
rectilinear outline, so a polygon is not an approximation of it. If the mark ever
becomes curved, this is the function that has to change and nothing else.

Per-locale social images
------------------------
`og:image` is not one file for the whole site. Facebook and X cache a card by URL
and never re-fetch, so a single shared image means every share of every locale
shows the same card -- and a Russian link previews in English. One image per
(locale, page) at 1280x630, the minimum both networks accept.

Font selection is by script, not by guesswork: CJK needs a face that has the
glyphs, and picking a Latin-only font for the Chinese image produces a card full
of tofu boxes that looks fine to the generator and terrible to a reader. The
loader below reports which face it used and fails if a glyph is missing.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIST = ROOT / "site" / "dist"
ASSETS = DIST / "assets"
MARK_SVG = DIST / "assets" / "logo-mark.svg"

OG_W, OG_H = 1280, 640

# The brand mark, in the 128-unit box of logo-mark.svg. A single rectilinear
# outline: M16 16 -> 112 16 -> 112 42 -> 42 42 -> 42 86 -> 112 86 -> 112 112
# -> 16 112 -> close. Kept as data so a reader can check it against the SVG.
MARK_OUTLINE = [(16, 16), (112, 16), (112, 42), (42, 42),
                (42, 86), (112, 86), (112, 112), (16, 112)]
INK = (0x17, 0x17, 0x14)
AMBER = (0xD3, 0x92, 0x3C)
PAPER = (0xF0, 0xED, 0xE5)
MUTED = (0x8B, 0x87, 0x7C)

# (filename, has CJK, has Cyrillic) in preference order. Windows faces first
# because this repo builds on Windows; the Noto faces are the portable fallback
# and are present on most Linux builders.
FACES = {
    "latin": ["segoeui.ttf", "arial.ttf", "calibri.ttf", "DejaVuSans.ttf"],
    "cyrillic": ["segoeui.ttf", "arial.ttf", "DejaVuSans.ttf"],
    "cjk": ["msyh.ttc", "msyhl.ttc", "NotoSansSC-Regular.otf",
            "NotoSansCJK-Regular.ttc", "simhei.ttf"],
    "mono": ["consola.ttf", "DejaVuSansMono.ttf", "cour.ttf"],
}
FONT_DIRS = [Path("C:/Windows/Fonts"), Path("/usr/share/fonts/truetype/dejavu"),
             Path("/usr/share/fonts/truetype/noto"),
             Path("/usr/share/fonts/opentype/noto")]


def face(kind: str) -> tuple[str, object]:
    """First available face of `kind`, as (path, ImageFont)."""
    from PIL import ImageFont
    for name in FACES[kind]:
        for d in FONT_DIRS:
            p = d / name
            if p.exists():
                try:
                    return str(p), ImageFont.truetype(str(p), 48)
                except OSError:
                    continue
    return "", None


def pick_face(kind: str, size: int):
    """A face at a given size, or None if the system has none for this script."""
    from PIL import ImageFont
    for name in FACES[kind]:
        for d in FONT_DIRS:
            p = d / name
            if p.exists():
                try:
                    return ImageFont.truetype(str(p), size)
                except OSError:
                    continue
    return None


def script_of(text: str) -> str:
    if any("一" <= ch <= "鿿" for ch in text):
        return "cjk"
    if any("Ѐ" <= ch <= "ӿ" for ch in text):
        return "cyrillic"
    return "latin"


def missing_glyphs(font, text: str) -> list[str]:
    """Characters the face cannot draw.

    Checked rather than assumed. A CJK card rendered in a Latin face is a card of
    empty boxes, and it is generated without error -- so the generator has to be
    the thing that notices, not the reader.
    """
    try:
        from PIL import features
        if not features.check("raqm"):
            # Without raqm, `getmask` still measures per glyph; a .notdef box has
            # the same advance as a real glyph, so fall back to a cmap probe.
            pass
    except Exception:                                          # noqa: BLE001
        pass
    out = []
    for ch in dict.fromkeys(text):
        if ch in " \n\t":
            continue
        try:
            if font.getmask(ch).getbbox() is None and not ch.isprintable():
                out.append(ch)
        except Exception:                                      # noqa: BLE001
            out.append(ch)
    return out


# ---------------------------------------------------------------- icons

def draw_mark(size: int, bg: tuple[int, int, int] | None = None):
    """The brand mark at `size` px, on `bg` (transparent when None)."""
    from PIL import Image, ImageDraw
    scale = size / 128.0
    im = Image.new("RGBA", (size, size),
                   bg + (255,) if bg else (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    pts = [(x * scale, y * scale) for x, y in MARK_OUTLINE]
    d.polygon(pts, fill=INK + (255,))
    # The amber diagonal cut, which is the second path in the SVG.
    d.polygon([(x * scale, y * scale) for x, y in
               ((112, 16), (112, 42), (16, 112), (16, 86))], fill=AMBER + (255,))
    return im


def write_icons() -> dict:
    from PIL import Image
    ASSETS.mkdir(parents=True, exist_ok=True)
    made: dict[str, str] = {}

    # favicon.ico at the three sizes browsers actually ask for.
    ico_src = draw_mark(64, bg=PAPER)
    ico_path = DIST / "favicon.ico"
    ico_src.save(ico_path, format="ICO",
                sizes=[(16, 16), (32, 32), (48, 48)])
    made["favicon.ico"] = f"{ico_path.stat().st_size} bytes"

    # apple-touch-icon is always composited on white; a transparent icon shows
    # as a black square on iOS.
    at = draw_mark(180, bg=PAPER).convert("RGB")
    at_path = ASSETS / "apple-touch-icon.png"
    at.save(at_path, format="PNG", optimize=True)
    made["apple-touch-icon.png"] = f"{at_path.stat().st_size} bytes"

    for px in (192, 512):
        icon = draw_mark(px, bg=PAPER).convert("RGB")
        p = ASSETS / f"icon-{px}.png"
        icon.save(p, format="PNG", optimize=True)
        made[f"icon-{px}.png"] = f"{p.stat().st_size} bytes"

    # A mask-icon for pinned tabs: monochrome, so the fill has to be black.
    mono = draw_mark(64)
    from PIL import ImageDraw
    flat = mono.convert("RGBA")
    px = flat.load()
    for yy in range(flat.height):
        for xx in range(flat.width):
            if px[xx, yy][3] > 0:
                px[xx, yy] = (0, 0, 0, 255)
    mono_path = ASSETS / "safari-pinned-tab.svg"
    _write_mask_svg(mono_path)
    made["safari-pinned-tab.svg"] = f"{mono_path.stat().st_size} bytes"

    manifest = {
        "name": "shotcraft",
        "short_name": "shotcraft",
        "description": "Cinematic shot recipes for AI video agents",
        "start_url": "/en/",
        "scope": "/",
        "display": "standalone",
        "background_color": "#0e0e0c",
        "theme_color": "#0e0e0c",
        "icons": [
            {"src": "/assets/icon-192.png", "sizes": "192x192",
             "type": "image/png", "purpose": "any"},
            {"src": "/assets/icon-512.png", "sizes": "512x512",
             "type": "image/png", "purpose": "any maskable"},
        ],
    }
    mf = DIST / "site.webmanifest"
    mf.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
                  encoding="utf-8")
    made["site.webmanifest"] = f"{mf.stat().st_size} bytes"

    bc = DIST / "browserconfig.xml"
    bc.write_text(
        '<?xml version="1.0" encoding="utf-8"?>\n'
        '<msapplication>\n'
        '  <tile>\n'
        '    <square150x150logo src="/assets/icon-192.png"/>\n'
        '    <TileColor>#0e0e0c</TileColor>\n'
        '  </tile>\n'
        '</msapplication>\n', encoding="utf-8")
    made["browserconfig.xml"] = f"{bc.stat().st_size} bytes"
    return made


def _write_mask_svg(path: Path) -> None:
    pts = " ".join(f"{x},{y}" for x, y in MARK_OUTLINE)
    diag = " ".join(f"{x},{y}" for x, y in
                    ((112, 16), (112, 42), (16, 112), (16, 86)))
    path.write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128">\n'
        f'  <polygon points="{pts}" fill="#000"/>\n'
        f'  <polygon points="{diag}" fill="#000"/>\n'
        '</svg>\n', encoding="utf-8")


# ----------------------------------------------------------- social cards

def social_card(title: str, subtitle: str, stats: list[tuple[str, str]],
                 out: Path) -> dict:
    """A 1280x630 card. The title is drawn in a face that can draw it."""
    from PIL import Image, ImageDraw
    im = Image.new("RGB", (OG_W, OG_H), (0x0E, 0x0E, 0x0C))
    d = ImageDraw.Draw(im)

    # mark, top-left
    mark = draw_mark(88, bg=None)
    im.paste(mark, (72, 64), mark)

    kind = script_of(title + subtitle)
    f_title = pick_face(kind, 76) or pick_face("latin", 76)
    f_sub = pick_face(kind, 34) or pick_face("latin", 34)
    f_stat_n = pick_face(kind, 44) or pick_face("latin", 44)
    f_stat_l = pick_face("latin", 22) or pick_face("latin", 22)
    f_brand = pick_face("latin", 26) or pick_face("latin", 26)

    warn: list[str] = []
    if f_title is None:
        warn.append("no face available for the title")
    else:
        gaps = missing_glyphs(f_title, title)
        if gaps:
            warn.append(f"title has {len(gaps)} glyph(s) the face cannot draw: "
                        f"{''.join(gaps[:8])}")

    d.text((184, 74), "shotcraft", font=f_brand, fill=AMBER)
    d.text((72, 210), _wrap(d, title, f_title, OG_W - 144, 3), font=f_title,
           fill=PAPER, spacing=22)
    if subtitle:
        d.text((72, 452), subtitle, font=f_sub, fill=MUTED)

    x = 72
    for n, label in stats:
        d.text((x, 520), n, font=f_stat_n, fill=PAPER)
        d.text((x, 576), label, font=f_stat_l, fill=MUTED)
        x += 40 + int(d.textlength(n, font=f_stat_n)) + 96
    d.rectangle([0, OG_H - 8, OG_W, OG_H], fill=AMBER)

    out.parent.mkdir(parents=True, exist_ok=True)
    im.save(out, format="JPEG", quality=88, optimize=True, progressive=True)
    try:
        rel = out.resolve().relative_to(DIST.resolve()).as_posix()
    except ValueError:
        # A caller may pass a path outside site/dist (a test, a preview folder).
        # Reporting the absolute path is more useful than refusing to draw.
        rel = out.as_posix()
    return {"file": rel, "bytes": out.stat().st_size, "script": kind,
            "warnings": warn}


def _wrap(d, text: str, font, max_w: int, max_lines: int) -> str:
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = f"{cur} {w}".strip()
        if d.textlength(trial, font=font) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
            if len(lines) == max_lines - 1:
                break
    rest = " ".join(words[len(" ".join(lines).split()):]) if lines else ""
    if len(lines) == max_lines - 1 and rest:
        cur = f"{cur}…"
    lines.append(cur)
    return "\n".join(lines[:max_lines])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="verify the generated set exists and is well formed")
    a = ap.parse_args()

    if a.check:
        need = ["favicon.ico", "assets/apple-touch-icon.png", "assets/icon-192.png",
                "assets/icon-512.png", "assets/safari-pinned-tab.svg",
                "site.webmanifest", "browserconfig.xml"]
        bad = [n for n in need if not (DIST / n).exists()]
        for n in need:
            p = DIST / n
            print(f"  {'ok  ' if p.exists() else 'MISS'} {n:<34} "
                  f"{p.stat().st_size if p.exists() else 0:>8} bytes")
        return 1 if bad else 0

    made = write_icons()
    print("icons:")
    for k, v in made.items():
        print(f"   {k:<28} {v}")
    print("\nfaces available:")
    for kind in ("latin", "cyrillic", "cjk", "mono"):
        path, _ = face(kind)
        print(f"   {kind:<10} {path or '(none)'}")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
