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

The bug that made this tool itself non-reproducible
--------------------------------------------------
The first version spliced attributes into the page one key at a time, and its
candidate offsets were computed **once, before the loop**. Every splice made the
html longer, so the second splice onwards landed at a byte offset that no longer
pointed at the element it had been matched against. Measured on a clean build,
**9 annotations landed on the element they were matched to and 12 did not** --
`searchPlaceholder` went onto the `<label class="search-field">` instead of the
`<input>`, and four keys piled onto the theme toggle as four duplicate
attributes, which an HTML parser resolves by taking the first and dropping the
rest.

Because the misplacement moved text and attributes around, the *next* pass saw a
different candidate set and wired more. Over four passes the same clean tree went
21 -> 9 -> 3 -> 0, so the number this tool printed depended on how many times it
had been run, and the chrome it produced depended on which pass got there first.
Two further rules made it worse:

  * the reachability set was threaded **across pages**, so a key claimed by
    `index.html` was denied to `library.html` and `showcase.html`. That is how
    `showcase.html` came out of every run with **zero** annotations while
    claiming the most chrome of the three pages;
  * key -> element was not injective. `ui.themeDark`, `showcase.themeDark`,
    `ui.themeToDark` and `showcase.themeToDark` all match the theme toggle, and
    each was wired independently.

How the wiring is decided now
-----------------------------
**Plan, then apply.** Phase 1 parses each page and resolves every key to exactly
one element, touching nothing. Phase 2 applies all of a page's bindings in a
single pass, in descending offset order, so no splice can invalidate another's
offset. Both phases are pure functions of the file and `site/locales/en/ui.json`,
which is what makes the output reproducible: the same tree always yields the same
annotations.

Because the plan is computed from the whole page rather than from whatever the
page already contains, the tool is **idempotent by construction**: a second run
finds the planned attributes already on their elements, emits no splice, and
writes an identical file. `--check` asserts exactly that and exits non-zero if
the tree and the plan disagree.

Which attribute gets used
-------------------------
`data-i18n` sets `textContent`, `data-l10n` sets `innerHTML`. The runtime draws
that distinction on purpose, so a string containing markup (`page.heroTitle` has
a `<br>` and an `<em>`) goes through `data-l10n` and would arrive as literal
`<br>` text through `data-i18n`. The choice is made from the value, not by hand.

`data-ns` is emitted on **every** annotation rather than only for the non-`ui`
namespaces. The runtime reads `node.dataset.ns || 'ui'`, so omitting it is
harmless at runtime -- but the reverse read, `reachable_keys`, has to decide what
a bare attribute name meant, and on `showcase.html` the default is `showcase`, not
`ui`. Spelling it out removes the ambiguity that made the first version report 62
orphans against a real ceiling of 43.

A key that matches zero elements, or more than one, is **skipped and reported**.
A key that matches two elements -- "Dark", "Retry", "Copy" -- would otherwise be
stamped onto both, and a mistranslation would then appear twice on the page with
no way to tell which was intended. Refusing is cheap. The skipped list is the work
queue, and it is printed. Where several *keys* match the *same* element, the
winner is chosen by a stated precedence rather than by iteration order: the
namespace the page's runtime resolves bare names against, then the more specific
attribute, then the key name. The losers are reported.
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
# Elements whose opening tag cannot carry a translation attribute, or whose
# contents are not page copy.
OPAQUE = {"script", "style", "svg", "path", "meta", "link"}
MARKUP = re.compile(r"<[^>]+>")
TAG = re.compile(r"<(?P<name>[a-zA-Z][\w-]*)(?P<attrs>[^>]*)>")

# Any attribute that already makes an element a translation target. An element
# carrying one is hand-marked upstream and is not this tool's to overwrite.
TRANSLATION_ATTRS = ("data-i18n", "data-l10n", "data-i18n-aria-label",
                     "data-i18n-placeholder", "data-i18n-title")
BOUND_ATTR = re.compile(
    r'\s(data-i18n|data-i18n-aria-label|data-i18n-placeholder|data-i18n-title|l10n)'
    r'="([^"]*)"')
NS_ATTR = re.compile(r'data-ns="([^"]+)"')


def qualify(attr: str, bare: str, ns: str | None, fallback: str) -> str:
    """The dotted ui.json key an annotation names.

    Both the writer and the reader go through here, because they have to agree.
    Comparing *bare* names instead is the bug this replaces: `ui.languageToggle`
    and `showcase.languageToggle` are the same two words, so a slot check on the
    bare name saw the key it was about to write as already there, wrote it
    anyway, and the second pass added a second `data-i18n-aria-label` to one tag.
    """
    ns = ns or ("page" if attr == "data-l10n" else fallback)
    return bare if ns == "ui" else f"{ns}.{bare}"

# Which namespace a page's runtime resolves a *bare* `data-i18n` against. This is
# the same rule `reachable_keys` reads back, and it is why `showcase.html` has to
# be planned differently from the other two pages.
def default_ns(page: str) -> str:
    return "showcase" if page == "showcase" else "ui"


# Attribute specificity, most specific first. Only used to break a tie between
# two keys that matched the same element through the same kind of offer.
KIND_RANK = {"placeholder": 0, "aria-label": 1, "title": 2, "text": 3}


def strip_markup(s: str) -> str:
    return re.sub(r"\s+", " ", MARKUP.sub(" ", s)).strip()


def esc_attr(v: str) -> str:
    return v.replace("&", "&amp;").replace('"', "&quot;")


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


class Element:
    """One opening tag, and the page copy it displays.

    `start`/`end` are offsets into the html **as it was parsed**. They stay valid
    for the whole plan, and Phase 2 applies bindings in descending `start` order
    so that no splice moves an offset another splice still needs. `idx` is the
    element's position in that parse, and is what identifies it throughout the
    plan -- offsets are only used for the splice itself.
    """

    __slots__ = ("idx", "start", "end", "name", "attrs", "annotated")

    def __init__(self, idx: int, start: int, end: int, name: str, attrs: str) -> None:
        self.idx = idx
        self.start = start
        self.end = end
        self.name = name
        self.attrs = attrs
        self.annotated = any(a in attrs for a in TRANSLATION_ATTRS)

    def values(self) -> dict[str, str]:
        """The attributes of one opening tag, as a dict.

        Named attributes only: an `href` or `src` is never a translatable string,
        and `attrs` arrives here as the raw text between the tag name and the `>`.
        """
        return dict(re.findall(r'([\w-]+)\s*=\s*"([^"]*)"', self.attrs))


def elements(html: str) -> list[Element]:
    return [Element(i, m.start(), m.end(), m.group("name"), m.group("attrs"))
            for i, m in enumerate(TAG.finditer(html))]


def slots(attrs: str, fallback: str) -> dict[str, str]:
    """Translation attributes already on one tag -> the dotted key each names."""
    ns = NS_ATTR.search(attrs)
    return {m.group(1): qualify(m.group(1), m.group(2),
                                ns.group(1) if ns else None, fallback)
            for m in BOUND_ATTR.finditer(attrs)}


def content_range(html: str, el: Element) -> tuple[int, int]:
    """(start, end) of an element's content, or (-1, -1) if unterminated."""
    close = html.find(">", el.end - 1)
    if close < 0:
        return (-1, -1)
    i, depth = close + 1, 1
    pattern = re.compile(rf"<(/?)({re.escape(el.name)})\b[^>]*?(/?)>", re.I)
    while i < len(html):
        m = pattern.search(html, i)
        if not m:
            break
        if m.group(1):
            depth -= 1
            if depth == 0:
                return (close + 1, m.start())
        elif not m.group(3):
            depth += 1
        i = m.end()
    return (-1, -1)


def inner_text(html: str, el: Element) -> str:
    """The full text an element contains, across any nested markup.

    Depth-aware, because the naive version -- text up to the next `</` -- returns
    the empty string for every button that contains an icon. `<button><svg
    ...></svg>Dark</button>` is the header's theme toggle, and its label is the
    one string a visitor sees most often after the cards themselves. Matching
    only leaf text silently excluded every labelled control in the UI.
    """
    lo, hi = content_range(html, el)
    return strip_markup(html[lo:hi]) if lo >= 0 else ""


class Offer:
    """One translatable string an element displays, and where it lives."""

    __slots__ = ("kind", "value", "el")

    def __init__(self, kind: str, value: str, el: Element) -> None:
        self.kind = kind
        self.value = value
        self.el = el


class Binding:
    """A key resolved to one element, ready to be spliced in."""

    __slots__ = ("key", "el", "attr", "ns", "bare")

    def __init__(self, key: str, el: Element, attr: str, ns: str, bare: str) -> None:
        self.key = key
        self.el = el
        self.attr = attr
        self.ns = ns
        self.bare = bare

    def insert(self) -> str:
        return f' {self.attr}="{esc_attr(self.bare)}" data-ns="{esc_attr(self.ns)}"'


def attr_for(offer: Offer, markup: bool) -> str:
    if offer.kind == "text":
        return "data-l10n" if markup else "data-i18n"
    return ATTRS[offer.kind]


def plan_page(html: str, en: dict, page: str) -> tuple[list[Binding], list[str], set[str]]:
    """Resolve every key against this page. Pure: `html` is not modified.

    Returns (bindings, refused, already_present). The caller applies the bindings
    and must not re-derive them, because re-deriving them from a partially
    annotated page is exactly how the previous version became unreproducible.
    """
    refused: list[str] = []
    present = reachable_keys(html, page)
    dn = default_ns(page)

    els = elements(html)
    spans: dict[int, tuple[int, int]] = {}
    offers: list[Offer] = []
    held_by: dict[int, dict[str, str]] = {}
    for el in els:
        if el.name in OPAQUE:
            continue
        # What this tag already carries, keyed by attribute and named by its
        # **dotted** key. One tag can legitimately hold two of them -- `data-i18n`
        # for its label and `data-i18n-aria-label` for its accessible name are
        # different strings on the same control -- so this is per attribute.
        held_by[el.idx] = slots(el.attrs, dn)
        av = el.values()
        for attr in ATTRS:
            if av.get(attr, "").strip():
                offers.append(Offer(attr, strip_markup(av[attr]), el))
        text = inner_text(html, el)
        if text:
            lo, hi = content_range(html, el)
            spans[el.idx] = (lo, hi)
            offers.append(Offer("text", text, el))

    candidates: list[tuple[Binding, str]] = []
    for key in sorted(en):
        value = en[key]
        if not isinstance(value, str) or not value.strip():
            continue
        if key in present:
            # Idempotency, not a heuristic: the planned attribute is already on
            # its element. Anything still absent is planned from scratch below,
            # because the whole page was parsed, not just its tail.
            continue

        want = strip_markup(value)
        markup = bool(MARKUP.search(value))
        ns, bare = namespace_of(key)

        # Every element that displays this string, before any question of
        # whether it still has room for the annotation.
        matches: list[tuple[Element, Offer]] = [
            (o.el, o) for o in offers
            if o.value == want and not (markup and o.kind == "text")]

        # An element that merely *aggregates* another candidate does not own the
        # text. `<button id="themeToggle">` renders "Dark" only because its child
        # `<span id="themeToggleLabel">` does, and stamping `data-i18n` on the
        # button would set its textContent -- replacing both moon and sun icons
        # with a bare word. Siblings still refuse, because between two siblings
        # there is no evidence about which one was meant.
        #
        # This runs *before* the slot check below, and that order is load
        # bearing. Doing it after let a key whose inner slot was taken fall back
        # outward onto the button, which is how `showcase.themeDark` ended up
        # replacing the theme toggle's two icons on the second pass and not the
        # first: the outcome depended on what an earlier pass had already done.
        text_idx = {el.idx for el, o in matches if o.kind == "text"}
        kept = [(el, o) for el, o in matches
                if not (o.kind == "text"
                        and any(j != el.idx and _contains(spans, els, el.idx, j)
                                for j in text_idx))]

        # One attribute per element: an element offering both a matching text and
        # a matching aria-label takes the more specific one.
        by_el: dict[int, tuple[Element, Offer, str]] = {}
        for el, offer in kept:
            attr = attr_for(offer, markup)
            cur = by_el.get(el.idx)
            if cur is None or KIND_RANK[offer.kind] < KIND_RANK[cur[1].kind]:
                by_el[el.idx] = (el, offer, attr)

        if not by_el:
            refused.append(f"{key}: no element says {want!r}")
            continue
        if len(by_el) > 1:
            refused.append(
                f"{key}: {len(by_el)} elements say {want!r} -- refusing to guess; "
                f"add data-i18n=\"{key}\" to the right one by hand")
            continue

        el, offer, attr = next(iter(by_el.values()))
        # A slot that is already spoken for is refused, not stolen. The holder is
        # named by its dotted key, so `ui.languageToggle` and
        # `showcase.languageToggle` are told apart -- they are the same two words,
        # and comparing the bare name is what let a second pass write
        # `data-i18n-aria-label` onto a tag that already had one.
        held = held_by[el.idx].get(attr)
        if held is not None:
            refused.append(
                f"{key}: <{el.name}> already bound to {held} through {attr}")
            continue
        candidates.append((Binding(key, el, attr, ns, bare), offer.kind))

    # Injective per (element, attribute). Two keys naming the same tag through the
    # same attribute would produce the same attribute name twice, and an HTML
    # parser resolves a duplicate by keeping the first -- so the winner would be
    # decided by which key sorted first rather than by anything about the page.
    by_slot: dict[tuple[int, str], list[tuple[Binding, str]]] = {}
    for cand in candidates:
        by_slot.setdefault((cand[0].el.idx, cand[0].attr), []).append(cand)
    bound: list[Binding] = []
    for (_idx, attr), group in by_slot.items():
        if len(group) == 1:
            bound.append(group[0][0])
            continue
        winner, _kind = min(
            group,
            key=lambda c: (0 if c[0].ns == dn else 1, KIND_RANK[c[1]], c[0].key))
        bound.append(winner)
        for cand, _k in group:
            if cand is not winner:
                refused.append(
                    f"{cand.key}: <{cand.el.name}> already bound to {winner.key} "
                    f"through {attr}; two keys on one tag is that attribute twice, "
                    f"and the parser keeps whichever it reads first")

    # Descending offset order. Applying right-to-left means every remaining
    # offset is still the one Phase 1 recorded, which is the entire reason this
    # tool is reproducible.
    bound.sort(key=lambda b: b.el.start, reverse=True)
    return bound, refused, present


def _contains(spans: dict[int, tuple[int, int]], els: list[Element],
              outer: int, inner: int) -> bool:
    a, b = spans.get(outer), spans.get(inner)
    if not a or not b or a[0] < 0 or b[0] < 0:
        return False
    return els[outer].start < els[inner].start and a[0] <= b[0] and b[1] <= a[1]


def apply_bindings(html: str, bindings: list[Binding]) -> str:
    for b in bindings:
        html = (html[:b.el.end - 1] + b.insert() + html[b.el.end - 1:])
    return html


def verify(html: str, before: str, bindings: list[Binding], label: str) -> list[str]:
    """Confirm every splice landed on the tag it was planned for.

    Matching is done on the *tag's own attributes*, not on its byte offset. An
    earlier version of this check looked the element up by offset in the spliced
    html, which is the same mistake the splice itself used to make: every
    insertion shifts the offsets of the elements after it, so the check found the
    wrong tag and reported placements as missing that had in fact landed
    correctly. Matching on the tag name plus the attribute set it had before the
    splice is immune to that, because a wrong landing point cannot have the same
    tag name *and* the same other attributes.

    `html` is the spliced page; `before` is what it was parsed from.
    """
    out: list[str] = []
    per_el: dict[int, list[Binding]] = {}
    for b in bindings:
        per_el.setdefault(b.el.idx, []).append(b)
    index: dict[tuple[str, str], Element] = {}
    for el in elements(html):
        index.setdefault((el.name, el.attrs), el)
    for group in per_el.values():
        el = group[0].el
        # Apply order within one tag is ascending attribute name, because that is
        # the tiebreak in the sort apply_bindings uses.
        want = (el.name, el.attrs
                + "".join(b.insert() for b in sorted(group, key=lambda b: b.attr)))
        if index.get(want) is None:
            for b in group:
                out.append(f"{label}: {b.key}: {b.attr} did not reach its "
                           f"<{el.name}> -- it landed somewhere else in the page")
    return out


def duplicate_attrs(html: str, label: str) -> list[str]:
    """Translation attributes repeated inside one tag.

    A duplicate is not a cosmetic problem: the HTML parser drops the second
    occurrence, so which key wins is decided by byte order and not by meaning.
    The first version of this tool produced five attributes on the theme toggle,
    two of them the same name, and the page shipped that way with every gate
    green.
    """
    out: list[str] = []
    for m in TAG.finditer(html):
        attrs = m.group("attrs")
        found = [a for a in TRANSLATION_ATTRS if attrs.count(a + "=") > 1]
        if found:
            out.append(f"{label}: <{m.group('name')}> carries "
                       f"{len(found)} duplicate translation attribute(s): "
                       f"{', '.join(found)}")
    return out


JS_FILES = ("app.js", "showcase.js")

# `{n} selected` -- the runtime's `t()` does no interpolation, and adding it for
# four strings is not worth a second failure mode. They stay unwired and are
# listed, rather than being emitted with a literal `{n}` in the interface.
PLACEHOLDER = re.compile(r"\{[a-zA-Z_]\w*\}")


def wire_js(path: Path, en: dict, keys: set[str],
            write: bool) -> tuple[int, list[str]]:
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
    wrong string turns into two. Already a lookup? Left alone, and the rewritten
    form is recognised so a second pass is a no-op.
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
        hit = None
        for quote in ("'", '"'):
            token = f"{quote}{value}{quote}"
            n = src.count(token)
            if n > 1:
                skipped.append(
                    f"{key}: the literal {value!r} occurs {n} times in "
                    f"{path.name}; refusing to rewrite a string that is not unique")
                hit = None
                break
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
                hit = None
                break
            hit = (quote, token, pos)
            break
        if hit is None:
            continue
        quote, token, pos = hit
        src = (src[:pos]
               + f"window.__I18N__.t({quote}{ns}{quote}, {quote}{bare}{quote})"
               + src[pos + len(token):])
        done += 1
    if write:
        path.write_text(src, encoding="utf-8")
    return done, skipped


TRANSLATION_ATTR = re.compile(
    r'(?P<attr>data-(?:i18n|i18n-aria-label|i18n-placeholder|i18n-title|l10n))'
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
    exactly the number of pre-existing showcase annotations. This build also
    writes `data-ns` on every annotation it emits, so the default is only ever
    consulted for upstream's own hand-marked attributes.
    """
    fallback = default_ns(page)
    out: set[str] = set()
    for m in TRANSLATION_ATTR.finditer(html):
        key = m.group("key")
        # `data-ns` sits in the same tag, after the attribute that named it.
        tag_end = html.find(">", m.end())
        tag = html[m.start():tag_end] if tag_end > 0 else html[m.start():m.end() + 60]
        ns_m = NS_ATTR.search(tag)
        out.add(qualify(m.group("attr"), key,
                        ns_m.group(1) if ns_m else None, fallback))
    return out


def reachable_from_js(src: str) -> set[str]:
    """The dotted keys the scripts can display, from `t('ns', 'key')` calls."""
    out = set()
    for ns, key in re.findall(
            r"__I18N__\.t\(\s*['\"]([\w-]+)['\"]\s*,\s*['\"]([\w.]+)['\"]\s*\)", src):
        out.add(key if ns == "ui" else f"{ns}.{key}")
    return out


# Keys `check_seo.py` asserts are translatable on every built locale's library
# page. Asserted *here* as well, because the failure they guard is the one this
# tool caused: `searchPlaceholder` landing on the `<label>` that wraps the search
# box instead of the `<input>`, which leaves the most prominent control on the
# page in English while `check_seo` still finds a `data-i18n-placeholder`
# somewhere in the file. A gate that passes on a substring it cannot locate is
# not a gate, so the assertion names the element it has to be on.
#
# The theme toggle's *label* is `<span id="themeToggleLabel">`, not the button:
# `data-i18n` sets textContent, so binding it to the button would replace the
# button's two icon `<svg>`s with the word "Dark".
REQUIRED = (
    ("searchPlaceholder", "data-i18n-placeholder", "input", "searchInput"),
    ("themeDark", "data-i18n", "span", "themeToggleLabel"),
)


def check_required(htmls: dict[str, str]) -> list[str]:
    """The REQUIRED bindings must be on the named element, on every locale.

    Attribute *order* inside a tag is not checked, because a splice appends: the
    first version of this assertion read `data-i18n-placeholder="..."` followed by
    `id="..."` and reported both required keys missing on a file where both were
    present and correct.
    """
    out: list[str] = []
    for loc, html in sorted(htmls.items()):
        tagged = {el.values().get("id"): el for el in elements(html)}
        for key, attr, want_tag, want_id in REQUIRED:
            el = tagged.get(want_id)
            if el is not None and el.name == want_tag and \
                    slots(el.attrs, default_ns("library")).get(attr) == key:
                continue
            out.append(
                f"{loc}/library.html: {key} is not wired as {attr}=\"{key}\" on "
                f'<{want_tag} id="{want_id}">; check_seo.py asserts this key is '
                f"translatable and it is not reachable")
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="report only; fail if the tree is not the plan")
    a = ap.parse_args()

    en_dir = LOCALES / "en"
    if not en_dir.is_dir():
        raise SystemExit("site/locales/en missing; run extract_locales.py")
    # English keeps every namespace -- `ui`, `page.*`, `showcase.*` -- in one flat
    # ui.json, because that is what a translator wants to see. The runtime's
    # namespace split is a build-time concern, not a file layout one.
    en = json.loads((en_dir / "ui.json").read_text(encoding="utf-8"))

    locales = sorted(p.name for p in LOCALES.iterdir()
                     if p.is_dir() and (p / "ui.json").exists())
    built = [c for c in locales if (DIST / c / "library.html").exists()]
    if not built:
        raise SystemExit("no built locales; run platform/site/build_site.py")

    problems: list[str] = []
    report: dict[str, dict] = {}
    total_wired = total_present = 0
    libs: dict[str, str] = {}

    for loc in built:
        # The locale's own ui.json is read so a locale whose file is unparseable
        # fails here rather than in a browser. It is deliberately **not** what the
        # plan is built from: the page ships English copy and the runtime
        # substitutes, so the template is matched against `en` for every locale.
        # That also makes the plan identical across locales, which is a stronger
        # reproducibility property than "each locale wires what it can".
        json.loads((LOCALES / loc / "ui.json").read_text(encoding="utf-8"))
        per_page: dict[str, dict] = {}
        for page in PAGES:
            p = DIST / loc / f"{page}.html"
            if not p.exists():
                continue
            html = p.read_text(encoding="utf-8")
            bindings, refused, present = plan_page(html, en, page)

            if bindings:
                new = apply_bindings(html, bindings)
                problems += verify(new, html, bindings, f"{loc}/{page}")
                if not a.check and new != html:
                    p.write_text(new, encoding="utf-8")
                html = new

            # Every page, not only the ones just spliced: a duplicate attribute
            # is a pre-existing condition and is a failure wherever it is found.
            problems += duplicate_attrs(html, f"{loc}/{page}")

            if a.check and bindings:
                problems.append(
                    f"{loc}/{page}: {len(bindings)} planned annotation(s) are "
                    f"absent from the file; --check is reproducible only if a "
                    f"wired tree is already the plan")

            annotations = [f"{b.key} -> {b.attr}/{b.ns}" for b in bindings]
            per_page[page] = {"wired": len(bindings), "already": len(present),
                              "skipped": refused, "annotations": annotations}
            total_wired += len(bindings)
            total_present += len(present)

        lib = DIST / loc / "library.html"
        if lib.exists():
            libs[loc] = lib.read_text(encoding="utf-8")
        report[loc] = per_page

    problems += check_required(libs)

    # The keys the DOM could not claim, as a *distinct* set over every locale and
    # page. Collected from the whole tree rather than from locale[0], so the JS
    # pass is given the same input on every run: it used to inherit the DOM's
    # non-determinism through a skip list built from a single locale.
    distinct: set[str] = set()
    for pages in report.values():
        for r in pages.values():
            for s in r["skipped"]:
                distinct.add(s.split(":", 1)[0])

    js_done = 0
    js_skipped: list[str] = []
    js_reachable: set[str] = set()
    for name in JS_FILES:
        p = DIST / "assets" / name
        if not p.exists():
            continue
        n, sk = wire_js(p, en, distinct, write=not a.check)
        js_done += n
        js_skipped.extend(sk)
        js_reachable |= reachable_from_js(p.read_text(encoding="utf-8"))
        if a.check and n:
            problems.append(
                f"assets/{name}: {n} literal(s) still need rewriting; --check is "
                f"reproducible only if a wired tree is already the plan")

    # An orphan is a translated key that nothing can display: not an attribute on
    # any element of any locale, and not a `t()` call in either script.
    dom_reachable: set[str] = set()
    for loc in built:
        for page in PAGES:
            p = DIST / loc / f"{page}.html"
            if p.exists():
                dom_reachable |= reachable_keys(p.read_text(encoding="utf-8"), page)
    orphans = sorted(k for k in en
                     if isinstance(en[k], str) and en[k].strip()
                     and k not in dom_reachable and k not in js_reachable)

    print(f"DOM: wired {total_wired} key(s) across {len(built)} locale(s); "
          f"{total_present} annotation(s) were already in place")
    print(f"JS : rewrote {js_done} literal(s) in {' and '.join(JS_FILES)}")
    print(f"\n{len(en)} translated ui key(s); "
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

    if problems:
        print("\nFAILED:")
        for p in sorted(set(problems)):
            print(f"   {p}")
    else:
        print("\nverified: every planned annotation is on its own element, "
              "no tag carries a duplicate translation attribute, and the "
              "keys check_seo.py asserts are wired on every locale.")

    print(f"\nreport: {out.relative_to(ROOT)}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())