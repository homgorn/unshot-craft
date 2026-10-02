"""Wire translated strings to the elements that show them.

    python platform/site/localise_dom.py          # annotate site/dist
    python platform/site/localise_dom.py --check  # report only, change nothing

The problem this exists to solve
-------------------------------
The Russian locale shipped 104 translated `ui` strings, and 65 of them were
**unreachable**: no element carried `data-i18n`, so the runtime had nothing to
apply them to. On `/ru/library.html` the card titles and descriptions were
Russian and everything around them was English -- the search placeholder, the
theme toggle, the energy filter labels, the whole hero, and all 24 showcase
strings.

`check_coverage.py` reported ru at 99.7 % throughout, because it measures whether
a string exists in the locale file, not whether anything displays it. Coverage of
a translation nobody can read is not coverage, and the gap between "translated"
and "shown" is exactly the kind that survives a green gate.

How the wiring is decided
-------------------------
By **exact text match against the English value**, per element, with markup
stripped and whitespace collapsed. Not by guessing from position, not by
fuzzy-matching, and not by a hand-maintained table of selectors that rots the
next time upstream reorders a div.

The rule that matters: if a key matches zero elements, or more than one, it is
**skipped and reported**. A key that matches two elements -- "Dark", "Retry",
"Copy" -- would otherwise be stamped onto both, and a mistranslation would then
appear twice on the page with no way to tell which was intended. Refusing is
cheap. The skipped list is the work queue, and it is printed.

Which attribute gets used
-------------------------
`data-i18n` sets `textContent`, `data-l10n` sets `innerHTML`. The runtime draws
that distinction on purpose, so a string containing markup (`page.heroTitle` has
a `<br>` and an `<em>`) goes through `data-l10n` and would arrive as literal
`<br>` text through `data-i18n`. The choice is made from the value, not by hand.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIST = ROOT / "site" / "dist"
LOCALES = ROOT / "site" / "locales"
PAGES = ("index", "library", "showcase")

# textContent attributes -> the data attribute that sets them
ATTRS = {
    "placeholder": "data-i18n-placeholder",
    "aria-label": "data-i18n-aria-label",
    "title": "data-i18n-title",
}
MARKUP = re.compile(r"<[^>]+>")
TAG = re.compile(r"<(?P<name>[a-zA-Z][\w-]*)(?P<attrs>[^>]*)>")
VOID = {"img", "br", "hr", "input", "meta", "link", "source", "path", "circle",
        "rect", "polygon", "use", "stop", "area", "col", "embed", "track", "wbr"}


def strip_markup(s: str) -> str:
    return re.sub(r"\s+", " ", MARKUP.sub(" ", s)).strip()


def esc_attr(v: str) -> str:
    return v.replace("&", "&amp;").replace('"', "&quot;")


def elements(html: str) -> list[tuple[int, int, str, str]]:
    """(start, end, tagname, attrs) for every element opening tag."""
    out = []
    for m in TAG.finditer(html):
        out.append((m.start(), m.end(), m.group("name"), m.group("attrs")))
    return out


def inner_text(html: str, tag_end: int, name: str) -> str:
    """The full text an element contains, across any nested markup.

    Depth-aware, because the naive version -- text up to the next `</` -- returns
    the empty string for every button that contains an icon. `<button><svg
    ...></svg>Dark</button>` is the header's theme toggle, and its label is the
    one string a visitor sees most often after the cards themselves. Matching
    only leaf text silently excluded every labelled control in the UI.
    """
    close = html.find(">", tag_end)
    if close < 0:
        return ""
    i, depth = close + 1, 1
    pattern = re.compile(rf"<(/?)({re.escape(name)})\b[^>]*?(/?)>", re.I)
    while i < len(html):
        m = pattern.search(html, i)
        if not m:
            break
        if m.group(1):
            depth -= 1
            if depth == 0:
                return strip_markup(html[close + 1:m.start()])
        elif not m.group(3):
            depth += 1
        i = m.end()
    return ""


def attribute_values(attrs: str) -> dict[str, str]:
    """The attributes of one opening tag, as a dict.

    Named attributes only: an `href` or `src` is never a translatable string, and
    `attrs` arrives here as the raw text between the tag name and the `>`.
    """
    return dict(re.findall(r'([\w-]+)\s*=\s*"([^"]*)"', attrs))


def wire_page(html: str, ui: dict, en: dict,
              reachable: set[str], page: str = "") -> tuple[str, list[str], list[str]]:
    """Add translation attributes for every key with exactly one candidate element.

    `reachable` is the union over *all* built pages, not this page's own set. A
    key already wired on library.html must not be re-attempted on index.html,
    where most of the copy is drawn by JavaScript and simply is not in the static
    file -- otherwise index reports 90-odd "unwired" keys that are in fact
    translated, and the real work queue is buried under noise.
    """
    wired: list[str] = []
    skipped: list[str] = []
    already = reachable | reachable_keys(html, page)

    # Candidate targets, collected once: (kind, value, tag_start, tag_end).
    targets: list[tuple[str, str, int, int]] = []
    for start, end, name, attrs in elements(html):
        if name in ("script", "style", "svg", "path", "meta", "link"):
            continue
        if any(a in attrs for a in ("data-i18n", "data-l10n",
                                    "data-i18n-aria-label",
                                    "data-i18n-placeholder", "data-i18n-title")):
            # Already translated, or deliberately hand-marked. Not a candidate.
            continue
        av = attribute_values(attrs)
        for attr in ATTRS:
            if av.get(attr, "").strip():
                targets.append((attr, strip_markup(av[attr]), start, end))
        text = inner_text(html, end, name)
        if text:
            targets.append(("text", text, start, end))

    for key in sorted(ui):
        if key in already:
            continue
        en_value = en.get(key)
        if en_value is None:
            skipped.append(f"{key}: no English value to match the template against")
            continue

        want = strip_markup(en_value)
        # The runtime draws textContent vs innerHTML, so a value carrying markup
        # has to take the innerHTML path or the tags arrive as literal text.
        markup = bool(MARKUP.search(en_value))
        ns, bare = namespace_of(key)

        hits: dict[int, tuple[int, str]] = {}   # tag_start -> (tag_end, attribute)
        for kind, got, start, end in targets:
            if got != want:
                continue
            attr = "data-l10n" if (markup and kind == "text") else (
                ATTRS[kind] if kind in ATTRS else "data-i18n")
            # A text match on a markup value would put a `<br>` into textContent.
            if markup and attr == "data-i18n":
                continue
            hits.setdefault(start, (end, attr))

        if not hits:
            skipped.append(f"{key}: no element says {want!r}")
            continue
        if len(hits) > 1:
            skipped.append(
                f"{key}: {len(hits)} elements say {want!r} -- refusing to guess; "
                f"add data-i18n=\"{key}\" to the right one by hand")
            continue

        start, (end, attr) = next(iter(hits.items()))
        # `data-i18n` alone resolves against the `ui` namespace. A `page.*` or
        # `showcase.*` key needs `data-ns` as well, or it silently renders as the
        # key name -- the same failure as calling t() with one argument.
        ns_attr = "" if attr == "data-l10n" and key.startswith("page.") else ""
        if attr == "data-i18n" and ns != "ui":
            ns_attr = f' data-ns="{esc_attr(ns)}"'
        elif attr == "data-l10n":
            ns_attr = ""
        html = (html[:end - 1] + f' {attr}="{esc_attr(bare)}"{ns_attr}'
                + html[end - 1:])
        wired.append(f"{key} -> {attr}{'/' + ns if ns_attr else ''}")
    return html, wired, skipped


JS_FILES = ("app.js", "showcase.js")

# `{n} selected` -- the runtime's `t()` does no interpolation, and adding it for
# four strings is not worth a second failure mode. They stay unwired and are
# listed, rather than being emitted with a literal `{n}` in the interface.
PLACEHOLDER = re.compile(r"\{[a-zA-Z_]\w*\}")


def wire_js(path: Path, ui: dict, en: dict,
            keys: set[str]) -> tuple[int, list[str]]:
    """Replace a JS string literal with a lookup through the runtime.

    The same problem as the DOM, one layer down: `app.js` and `showcase.js`
    carry their own English literals and never consult `__I18N__`, so the energy
    filter chips, the copy buttons and the whole showcase page stayed English on
    `/ru/` even with the Russian strings sitting in `ru/ui.json`.

    Upstream solved this with a 60 KB `translations.js` carrying an en/zh table.
    That file is gone -- its content is the locale JSON now -- but the *lookup*
    it fed is what was dropped with it, and this restores it without the table.

    Only an exact quoted literal is replaced, and only when it occurs **once**.
    A literal appearing twice is skipped rather than rewritten, because the two
    sites may want different keys and guessing which is which is how a single
    wrong string turns into two.
    """
    src = path.read_text(encoding="utf-8", errors="replace")
    done, skipped = 0, []
    for key in sorted(keys):
        value = en.get(key)
        if not isinstance(value, str) or not value.strip():
            continue
        if PLACEHOLDER.search(value):
            skipped.append(f"{key}: contains a {{{{'...'}}}} placeholder and the "
                           f"runtime does no interpolation")
            continue
        ns, bare = namespace_of(key)
        for quote in ("'", '"'):
            token = f"{quote}{value}{quote}"
            n = src.count(token)
            if n > 1:
                skipped.append(
                    f"{key}: the literal {value!r} occurs {n} times in "
                    f"{path.name}; refusing to rewrite a string that is not unique")
                continue
            if n == 0:
                continue
            pos = src.find(token)
            # Already an argument of a lookup. The first version of this
            # rewrote `t('page', 'styles')` into
            # `t('page', window.__I18N__.t('styles'))` -- because the *key*
            # argument is itself a string literal, and 'styles' happens to be a
            # UI value. Every existing lookup in both files was silently broken,
            # and the library rendered key names instead of labels. A literal
            # that is already inside a `t(` call is not a user-facing string.
            before = src[max(0, pos - 24):pos]
            if re.search(r"\.?t\(\s*$", before) or \
                    re.search(r"\.?t\(\s*['\"][^'\"]{0,20}['\"]\s*,\s*$", before):
                skipped.append(
                    f"{key}: {value!r} is already a lookup argument in "
                    f"{path.name}; left alone")
                continue
            src = (src[:pos]
                   + f"window.__I18N__.t({quote}{ns}{quote}, {quote}{bare}{quote})"
                   + src[pos + len(token):])
            done += 1
            break
        else:
            skipped.append(f"{key}: {value!r} does not appear as a string "
                           f"literal in {path.name}")
    path.write_text(src, encoding="utf-8")
    return done, skipped


def namespace_of(key: str) -> tuple[str, str]:
    """(namespace, bare key) for a dotted key.

    The runtime splits the flat locale file into namespaces at build time:
    `ui.json` holds the plain keys, `page.*` becomes namespace `page`, and
    `showcase.*` becomes namespace `showcase`. Calling `t('showcase.title')`
    with one argument looks up a namespace named `showcase.title`, finds none,
    and returns the key -- so a label renders as the word "title".
    """
    if key.startswith("page."):
        return "page", key[len("page."):]
    if key.startswith("showcase."):
        return "showcase", key[len("showcase."):]
    return "ui", key


TRANSLATION_ATTR = re.compile(
    r'data-(?P<kind>i18n|i18n-aria-label|i18n-placeholder|i18n-title|l10n)'
    r'="(?P<key>[^"]+)"')


def reachable_keys(html: str, page: str = "") -> set[str]:
    """The dotted ui.json keys this page can actually display.

    Namespace-aware, because the attributes carry the **bare** key and the
    namespace lives in `data-ns`. Reading the attribute alone turns every
    `page.*` and `showcase.*` key into a permanent false orphan: the first
    version reported 62 orphans against a real ceiling of 43 for exactly that
    reason, having just successfully wired them.

    The default namespace is per page, not global. `showcase.js` resolves its own
    bare `data-i18n` names against the `showcase` namespace, so reading them as
    `ui` counted `navLibrary` and `submitCta` twice -- once reachable under the
    wrong name, once orphaned under the right one -- and inflated the count by
    exactly the number of pre-existing showcase annotations.
    """
    default_ns = "showcase" if page == "showcase" else "ui"
    out: set[str] = set()
    for m in TRANSLATION_ATTR.finditer(html):
        key = m.group("key")
        # `data-ns` sits in the same tag, after the attribute that named it.
        tag_end = html.find(">", m.end())
        tag = html[m.start():tag_end] if tag_end > 0 else html[m.start():m.end() + 60]
        ns_m = re.search(r'data-ns="([^"]+)"', tag)
        ns = ns_m.group(1) if ns_m else (
            "page" if m.group("kind") == "l10n" else default_ns)
        out.add(key if ns == "ui" else f"{ns}.{key}")
    return out


def reachable_from_js(src: str) -> set[str]:
    """The dotted keys the scripts can display, from `t('ns', 'key')` calls."""
    out = set()
    for ns, key in re.findall(
            r"__I18N__\.t\(\s*['\"]([\w-]+)['\"]\s*,\s*['\"]([\w.]+)['\"]\s*\)", src):
        out.add(key if ns == "ui" else f"{ns}.{key}")
    return out


EN_UI: dict = {}
EN_PAGE: dict = {}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()

    global EN_UI, EN_PAGE
    en_dir = LOCALES / "en"
    if not en_dir.is_dir():
        raise SystemExit("site/locales/en missing; run extract_locales.py")
    # English keeps every namespace -- `ui`, `page.*`, `showcase.*` -- in one flat
    # ui.json, because that is what a translator wants to see. The runtime's
    # namespace split is a build-time concern, not a file layout one.
    EN_UI = json.loads((en_dir / "ui.json").read_text(encoding="utf-8"))
    EN_PAGE = EN_UI

    locales = sorted(p.name for p in LOCALES.iterdir()
                     if p.is_dir() and (p / "ui.json").exists())
    built = [c for c in locales if (DIST / c / "library.html").exists()]

    report: dict[str, dict] = {}
    for loc in built:
        ui = json.loads((LOCALES / loc / "ui.json").read_text(encoding="utf-8"))
        # Pass 1, **per locale**: what is already annotated on this locale's own
        # pages. Computing it globally would let a key annotated on /en/ suppress
        # the annotation on /ru/, and then /ru/ would render English -- which is
        # the exact failure this tool exists to remove, introduced by the tool
        # meant to remove it.
        reachable: set[str] = set()
        for page in PAGES:
            p = DIST / loc / f"{page}.html"
            if p.exists():
                reachable |= reachable_keys(p.read_text(encoding="utf-8"), page)

        per_page: dict[str, dict] = {}
        for page in PAGES:
            p = DIST / loc / f"{page}.html"
            if not p.exists():
                continue
            html = p.read_text(encoding="utf-8")
            new, wired, skipped = wire_page(html, ui, EN_UI, reachable, page)
            if wired:
                # Newly wired keys become reachable for the next page, so the
                # same string is not stamped twice if it appears in both.
                reachable |= {w.split(" -> ")[0] for w in wired}
            if not a.check and new != html:
                p.write_text(new, encoding="utf-8")
            per_page[page] = {"wired": len(wired), "skipped": skipped,
                              "annotations": wired}
        report[loc] = per_page

    total_wired = sum(v["wired"] for p in report.values() for v in p.values())
    total_skip = sum(len(v["skipped"]) for p in report.values() for v in p.values())

    # The keys the DOM could not claim, as a *distinct* set -- the per-page and
    # per-locale counts triple every miss and bury the actual work queue.
    distinct: dict[str, str] = {}
    for loc, pages in report.items():
        if loc != built[0]:
            continue
        for r in pages.values():
            for s in r["skipped"]:
                distinct.setdefault(s.split(":", 1)[0], s)

    # Pass 3: the same strings, in the scripts that draw them at runtime.
    js_done = 0
    js_skipped: list[str] = []
    js_reachable: set[str] = set()
    for name in JS_FILES:
        p = DIST / "assets" / name
        if not p.exists():
            continue
        n, sk = wire_js(p, {}, EN_UI, set(distinct))
        js_done += n
        js_skipped.extend(sk)
        js_reachable |= reachable_from_js(p.read_text(encoding="utf-8"))

    # An orphan is a translated key that nothing can display: not an attribute on
    # any element of any locale, and not a `t()` call in either script. Counting
    # a JS-wired key as an orphan is the other half of the earlier 62-vs-43
    # discrepancy -- the string *is* shown, just not through an attribute.
    dom_reachable: set[str] = set()
    for loc in built:
        for page in PAGES:
            p = DIST / loc / f"{page}.html"
            if p.exists():
                dom_reachable |= reachable_keys(p.read_text(encoding="utf-8"), page)
    orphans = sorted(k for k in EN_UI
                     if isinstance(EN_UI[k], str) and EN_UI[k].strip()
                     and k not in dom_reachable and k not in js_reachable)

    print(f"DOM: wired {total_wired} key(s) across {len(built)} locale(s)")
    print(f"JS : rewrote {js_done} literal(s) in {' and '.join(JS_FILES)}")
    print(f"\n{len(EN_UI)} translated ui key(s); "
          f"{len(dom_reachable | js_reachable)} "
          f"have a display site; {len(orphans)} are orphaned.")
    if orphans:
        print("\norphaned (translated, shown nowhere):")
        for k in orphans[:14]:
            print(f"   {k}")
        if len(orphans) > 14:
            print(f"   … and {len(orphans) - 14} more")
    if js_skipped:
        print("\nJS, refused or unmatched:")
        for s in js_skipped[:10]:
            print(f"   {s}")
        if len(js_skipped) > 10:
            print(f"   … and {len(js_skipped) - 10} more")

    out = ROOT / "site" / "build" / "localise_report.json"
    out.write_text(json.dumps(
        {"report": report, "js_rewritten": js_done, "js_skipped": js_skipped,
         "dom_reachable": sorted(dom_reachable),
         "js_reachable": sorted(js_reachable),
         "orphaned": orphans}, ensure_ascii=False, indent=2),
        encoding="utf-8")
    print(f"\nreport: {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())