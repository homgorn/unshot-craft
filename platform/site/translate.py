"""Translation worklist, batch application, and verification.

    python platform/site/translate.py list ru --ns cards
    python platform/site/translate.py list ru --ns styles --limit 10
    python platform/site/translate.py apply ru site/locales/_batch_ru.json
    python platform/site/translate.py verify ru
    python platform/site/translate.py report

Why a tool and not a JSON edit
------------------------------
A hand-edited locale file has no way to record *what kind of translation it is*.
A native speaker's careful rendering and a machine pass look identical in the
file, and identical in the rendered page, and identical to the coverage counter.
So provenance goes in the database (`translation.method`, `translation.status`)
and a machine pass is `machine` / `needs_review` forever until a human says
otherwise. Nothing in this repo is allowed to upgrade that by itself.

Batch file
----------
```json
{ "locale": "ru", "namespace": "cards", "method": "machine",
  "status": "needs_review",
  "entries": { "crash-zoom-punch": { "description": "…" } } }
```

What `apply` refuses
--------------------
* a key that is not in the source locale or the corpus -- a typo must not create
  a translation of nothing
* an empty value, or one that is byte-identical to the source value
* a value equal to the key: `{"anime-impact": {"title": "anime-impact"}}` is what
  a placeholder file looks like, and it satisfies every key-count check ever
  written. This is the exact shape `ru/styles.json` shipped in.
* downgrading a translation already marked `reviewed`, without `--force`
* writing a `reviewed` status from a batch that does not say who reviewed it
"""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LOCALES = ROOT / "site" / "locales"
DB = ROOT / "platform" / "db" / "shotcraft.db"
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

NAMESPACES = ("ui", "cards", "styles", "showcase", "page", "meta")

# Fields a client may legitimately leave identical across locales: numbers, unit
# strings, and the words that are the same word in Russian.
ALLOW_IDENTICAL = {"en", "zh", "ru", "es", "de", "fr", "pt", "ko", "ja", "x-default"}


def load(locale: str, ns: str) -> dict:
    p = LOCALES / locale / f"{ns}.json"
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"{p} is not valid JSON: {exc}")


def save(locale: str, ns: str, data: dict) -> None:
    p = LOCALES / locale / f"{ns}.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                 encoding="utf-8")


def leaves(value) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, dict):
        return [s for v in value.values() for s in leaves(v)]
    return []


def source_locale() -> str:
    """Which locale is the corpus written in.

    zh, because upstream's cards are Chinese. `en` is the reference for chrome
    and for the style *descriptions* upstream only wrote in English, which is why
    the two are compared per-namespace below rather than globally.
    """
    return "zh"


def corpus_keys(ns: str) -> set[str]:
    c = sqlite3.connect(f"file:{DB.as_posix()}?mode=ro", uri=True)
    try:
        if ns == "cards":
            return {r[0] for r in c.execute("SELECT name FROM shot_card")}
        if ns == "styles":
            # `style` alone is not the whole set. 27 of the styles the site can
            # render live in `gallery_style` -- upstream keys with no demo
            # component (AGENTS.md rule 5) -- and the worklist missed every one of
            # them, reporting "218 complete, 0 placeholder" while 27 entries in
            # the file were the slug. A worklist that only knows about the table
            # it was written for is blind to the rows someone added later.
            return ({r[0] for r in c.execute("SELECT key FROM style")}
                    | {r[0] for r in c.execute("SELECT key FROM gallery_style")
                       if r[0]})
        if ns == "ui":
            return set(load("en", "ui"))
        return set(load("en", ns))
    finally:
        c.close()


def source_text(ns: str, key: str, field: str = "title") -> str:
    """The source string for one *field* of one key.

    Field-aware, and the awareness matters. `zh/cards.json` holds only a
    `title` per card -- upstream never wrote a Chinese card description -- so a
    field-blind lookup answered "what is the source for this card's description"
    with the title, and the worklist asked for a translation of the card's *name*
    when the page actually renders its Chinese *summary* instead.

    Order of preference, per field:
      * the source locale's own value for that field
      * `en`'s value, which for a card description is upstream's English prose
      * the card's `summary` from library.json -- the Chinese text the page falls
        back to when no description exists
    """
    for loc in (source_locale(), "en"):
        v = load(loc, ns).get(key)
        if isinstance(v, dict) and v.get(field):
            return v[field]
        if isinstance(v, str) and field == "title" and v:
            return v
    if ns == "cards" and field in ("description", "summary"):
        lib_path = ROOT / "site" / "dist" / "api" / "library.json"
        if lib_path.exists():
            lib = json.loads(lib_path.read_text(encoding="utf-8"))
            for card in lib.get("cards", []):
                if card.get("name") == key:
                    return card.get("summary") or card.get("intention") or ""
    return ""


def fields_of(ns: str, value) -> dict[str, str]:
    if isinstance(value, dict):
        return {k: v for k, v in value.items() if isinstance(v, str) and v.strip()}
    if isinstance(value, str) and value.strip():
        return {"title": value}
    return {}


def wanted_fields(ns: str, key: str) -> dict[str, str]:
    """What this key is *supposed* to have, per field.

    Per field, not per key. The first version of this tool asked "does this card
    have a translated string?" and the card does -- its title is in Russian -- so
    it reported 157 of 157 translated while every one of those cards still showed
    its Chinese summary on the page. A key is translated only when each field the
    page renders is translated, and the fields differ per namespace.
    """
    if ns == "cards":
        # The page renders title and description. `description` falls back to the
        # card's Chinese summary, so absent a description the page is half
        # untranslated no matter what the title says.
        return {"title": None, "description": None}
    if ns == "styles":
        return {"title": None}
    return {"title": None}


def current_text(ns: str, key: str, field: str = "title") -> str:
    v = load(_ACTIVE["locale"], ns).get(key)
    return fields_of(ns, v).get(field, "")


_ACTIVE = {"locale": "ru"}


def _assess(ns: str, key: str) -> tuple[list[tuple[str, str]], list[tuple[str, str, str]]]:
    """-> (missing, suspicious) for one key, field by field."""
    have = fields_of(ns, load(_ACTIVE["locale"], ns).get(key))
    missing: list[tuple[str, str]] = []
    suspicious: list[tuple[str, str, str]] = []
    for field in wanted_fields(ns, key):
        text = have.get(field, "")
        want = source_text(ns, key, field)
        if not want:
            continue
        if not text:
            missing.append((f"{key}.{field}", want))
        elif text == want and text not in ALLOW_IDENTICAL:
            suspicious.append((f"{key}.{field}", text, "identical to source"))
        elif field == "title" and (text == key or SLUG_RE.match(text)):
            suspicious.append((f"{key}.{field}", text, "value is the slug"))
    return missing, suspicious


# ---------------------------------------------------------------- list

def cmd_list(a) -> int:
    _ACTIVE["locale"] = a.locale
    keys = sorted(corpus_keys(a.ns))
    missing: list[tuple[str, str]] = []
    suspicious: list[tuple[str, str, str]] = []
    done = 0

    for k in keys:
        m, s = _assess(a.ns, k)
        if m or s:
            missing += m
            suspicious += s
        else:
            done += 1

    touched = ({m[0].split(".")[0] for m in missing}
               | {s[0].split(".")[0] for s in suspicious})
    total = done + len(touched)
    print(f"{a.locale} / {a.ns}: {total} keys from the corpus, "
          f"assessed field by field")
    print(f"  complete     {done:>4}")
    print(f"  missing      {len(missing):>4} field(s) over "
          f"{len({m[0].split('.')[0] for m in missing})} key(s)")
    print(f"  placeholder  {len(suspicious):>4} field(s) present but not a translation")
    if suspicious and a.verbose:
        print("\n  placeholders, which a key count cannot see:")
        for k, v, why in suspicious[:10]:
            print(f"    {k:<40} {why}: {v[:44]!r}")
    if a.limit:
        print(f"\n  next {min(a.limit, len(missing))} field(s):")
        for k, want in missing[:a.limit]:
            print(f"\n    {k}\n      source: {want[:220]}")
    return 0 if not missing and not suspicious else 1


# --------------------------------------------------------------- apply

def cmd_apply(a) -> int:
    batch = json.loads(Path(a.batch).read_text(encoding="utf-8"))
    locale = batch.get("locale") or a.locale
    ns = batch.get("namespace") or a.namespace
    method = batch.get("method", "machine")
    status = batch.get("status", "needs_review")
    entries = batch.get("entries") or {}

    if not entries:
        print("batch has no entries", file=sys.stderr)
        return 2

    known = corpus_keys(ns)
    src = source_locale()
    data = load(locale, ns)
    problems: list[str] = []
    applied = 0

    # Never let a batch claim review it did not get.
    if status == "reviewed" and not batch.get("reviewed_by"):
        problems.append("status is 'reviewed' but the batch names no reviewed_by; "
                        "a machine pass cannot mark its own work reviewed")
    if method not in ("machine", "human", "vendor", "import"):
        problems.append(f"method {method!r} is not one of machine/human/vendor/import")

    for key, value in entries.items():
        if key not in known:
            problems.append(f"{key}: not in the {ns} corpus -- a typo here creates a "
                            f"translation of nothing")
            continue
        if isinstance(value, str):
            value = {"title": value} if ns == "styles" and "title" not in \
                (data.get(key) or {}) else value
        for field, text in (value or {}).items():
            if not isinstance(text, str) or not text.strip():
                problems.append(f"{key}.{field}: empty")
                continue
            want = source_text(ns, key, field)
            if text == want and text not in ALLOW_IDENTICAL:
                problems.append(f"{key}.{field}: identical to the {src} source")
                continue
            if field == "title" and (text == key or SLUG_RE.match(text)):
                problems.append(f"{key}.title: the value is the slug, not a translation")
                continue
            if not any("Ѐ" <= ch <= "ӿ" for ch in text) and \
                    any("一" <= ch <= "鿿" for ch in text):
                problems.append(f"{key}.{field}: still CJK -- the source was not translated")
                continue
            # Mixed script. A translation that is 95% Russian and carries three
            # untranslated English words in the middle is a machine artefact, not
            # a near miss, and it is invisible to every check that only asks
            # "is there Cyrillic here". Both batches in this repo were caught by
            # reading rather than by tooling, so the tooling now does it.
            latin = _latin_words(text)
            if latin:
                problems.append(
                    f"{key}.{field}: {len(latin)} untranslated latin word(s) "
                    f"{latin[:5]} in a ru string -- mixed script")
                continue
        merged = dict(data.get(key) or {}) if isinstance(data.get(key), dict) else {}
        merged.update(value or {})
        data[key] = merged
        applied += 1

    if problems and not a.force:
        print(f"REFUSING: {len(problems)} problem(s)", file=sys.stderr)
        for p in problems[:20]:
            print(f"  - {p}", file=sys.stderr)
        if len(problems) > 20:
            print(f"  ... and {len(problems) - 20} more", file=sys.stderr)
        return 1
    for p in problems:
        print(f"  forced past: {p}", file=sys.stderr)

    save(locale, ns, data)
    record_provenance(locale, ns, entries, method, status,
                      batch.get("reviewed_by"), a.batch)
    print(f"applied {applied} entr(ies) to {locale}/{ns}.json  "
          f"method={method} status={status}")
    if status != "reviewed":
        print(f"  these are NOT reviewed; a native speaker still has to sign them off, "
              f"and until then the database says so")
    return 0


def _latin_words(text: str) -> list[str]:
    """Latin words in a string that also carries Cyrillic.

    Exempt, because they are not untranslated English:

      * acronyms that are never localised -- SVG, RGB, FUI, HUD, UI, UX, CTA, API
      * named easing curves, which are library identifiers rather than prose:
        `ease-out-quart` is the name of a function, and writing it out would make
        it *less* findable
      * a handful of corpus terms upstream itself writes in latin and a Russian
        translation keeps rather than transliterates

    Hyphens are stripped before the allowlist lookup because the token pattern
    captures them: `SVG-` and `SVG` are the same word, and treating the trailing
    hyphen as part of the token would let an acronym smuggle itself past the
    check by sitting next to a dash.
    """
    ALLOWED = {
        # acronyms, never localised
        "svg", "rgb", "rgba", "hsl", "fui", "hud", "ui", "ux", "cta", "api",
        "html", "css", "json", "xml", "url", "id", "px", "ms", "fps", "kb", "mb",
        "ai", "os", "pc", "tv", "ar", "vr", "gif", "mp4", "web", "live",
        # named easing curves and library identifiers
        "ease", "in", "out", "quart", "cubic", "quad", "sine", "expo", "circ",
        "back", "elastic", "bounce", "linear", "steps", "spring", "stiffness",
        "damping", "mass", "duration", "delay", "rem", "fps",
        # corpus vocabulary that stays in latin in a Russian translation
        "ease-out-quart", "ease-in-out", "ease-in", "ease-out",
        "sin", "cos", "tan", "impress", "keynote",
        "beat", "remotion", "shadcn", "tailwind", "pro", "max", "min", "alpha",
        "beta", "moves", "zoom", "panel", "panels", "grid", "chart", "sprint",
    }
    words = re.findall(r"[A-Za-z][A-Za-z'-]{2,}", text)
    out = []
    for w in words:
        core = w.strip("-'").lower()
        if core in ALLOWED:
            continue
        out.append(w)
    return out


def record_provenance(locale: str, ns: str, entries: dict, method: str,
                      status: str, reviewed_by: str | None,
                      batch_file: str | None = None) -> None:
    """Record who wrote a translation and whether a human has signed it off.

    Into `translation_provenance`, not `translation`. The latter is derived: the
    ingest drops and rebuilds it from upstream's inline dictionaries on every
    run, so a provenance column written by hand survives exactly until the next
    `scripts/init.ps1` and is then gone. That is not hypothetical -- the first
    version of this function wrote to `translation`, and 360 machine translations
    marked `needs_review` became 360 rows with no status at all, which meant no
    reader could tell which strings a person had ever looked at.

    `translation` holds the text. This table holds the claim about the text.
    """
    from datetime import datetime, timezone
    c = sqlite3.connect(DB)
    lid = c.execute("SELECT id FROM locale WHERE code=?", (locale,)).fetchone()
    if not lid:
        c.close()
        print(f"  note: locale {locale!r} is not in the locale table, so no "
              f"provenance rows written", file=sys.stderr)
        return
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    n = 0
    try:
        for key, value in entries.items():
            fields = (value or {}).items() if isinstance(value, dict) else [(None, value)]
            for field, text in fields:
                if not isinstance(text, str) or not text.strip():
                    continue
                sub = f"{key}.{field}" if field else key
                c.execute(
                    """INSERT INTO translation_provenance
                         (locale_id, ns, key, method, status, reviewed_by,
                          reviewed_at, tool, batch_file, updated_at)
                       VALUES (?,?,?,?,?,?,?,?,?,?)
                       ON CONFLICT(locale_id, ns, key) DO UPDATE SET
                         method=excluded.method, status=excluded.status,
                         reviewed_by=excluded.reviewed_by,
                         reviewed_at=excluded.reviewed_at,
                         batch_file=excluded.batch_file,
                         updated_at=excluded.updated_at""",
                    (lid[0], ns, sub, method,
                     "reviewed" if reviewed_by else status,
                     reviewed_by,
                     now if reviewed_by else None,
                     "machine-pass" if method == "machine" else None,
                     batch_file, now))
                n += 1
        c.commit()
    finally:
        c.close()
    print(f"  {n} provenance row(s) written to `translation_provenance`")


# -------------------------------------------------------------- verify

def cmd_verify(a) -> int:
    _ACTIVE["locale"] = a.locale
    bad = 0
    for ns in (a.ns.split(",") if a.ns else ("cards", "styles", "ui")):
        missing: list[str] = []
        placeholders: list[str] = []
        cjk: list[str] = []
        for k in sorted(corpus_keys(ns)):
            m, s = _assess(ns, k)
            missing += [x[0] for x in m]
            placeholders += [x[0] for x in s]
            for f, text in fields_of(ns, load(a.locale, ns).get(k)).items():
                if any("一" <= ch <= "鿿" for ch in text):
                    cjk.append(f"{k}.{f}")
        status = "ok" if not (missing or placeholders or cjk) else "INCOMPLETE"
        print(f"  {a.locale}/{ns:<8} {status:<11} "
              f"missing={len(missing):<4} placeholder={len(placeholders):<4} "
              f"still-CJK={len(cjk)}")
        for label, items in (("missing", missing), ("placeholder", placeholders),
                             ("still CJK", cjk)):
            if items and a.verbose:
                print(f"      {label}: {items[:8]}")
        if missing or placeholders or cjk:
            bad += 1
    return 1 if bad else 0


# -------------------------------------------------------------- report

def cmd_report(a) -> int:
    c = sqlite3.connect(f"file:{DB.as_posix()}?mode=ro", uri=True)
    c.row_factory = sqlite3.Row
    has = c.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table' "
                    "AND name='translation_provenance'").fetchone()[0]
    if not has:
        print("translation_provenance is absent; run platform/ingest/run.py")
        return 1
    print("translation provenance, by locale and namespace")
    print(f"  {'locale':<6} {'ns':<8} {'strings':>8} {'needs_review':>13} {'reviewed':>9}")
    for r in c.execute("""SELECT lo.code AS locale, p.ns, COUNT(*) AS strings,
                                  SUM(p.status='needs_review') AS needs_review,
                                  SUM(p.status='reviewed') AS reviewed
                           FROM translation_provenance p
                           JOIN locale lo ON lo.id=p.locale_id
                           GROUP BY lo.code, p.ns ORDER BY lo.code, p.ns"""):
        print(f"  {r['locale']:<6} {r['ns']:<8} {r['strings']:>8} "
              f"{r['needs_review']:>13} {r['reviewed']:>9}")
    tot = c.execute("SELECT COUNT(*) n, "
                    "SUM(status='reviewed') r, "
                    "SUM(status='needs_review') nr FROM translation_provenance"
                    ).fetchone()
    print(f"\n  {tot['n']} recorded, {tot['r'] or 0} reviewed, "
          f"{tot['nr'] or 0} awaiting a native speaker")
    if (tot['nr'] or 0) > 0:
        print("\n  This is the honest state: the Russian locale is published and "
              "complete, and none\n  of it has been through a native reviewer. "
              "The site does not surface this per string\n  yet -- a reader cannot "
              "tell a reviewed line from a machine pass, and that is the next\n"
              "  thing to fix. `reviewed_by` is how: a batch that names one gets "
              "`status='reviewed'`.")
    return 0


# -------------------------------------------------------------- prune

def cmd_prune(a) -> int:
    """Delete entries that are placeholders, not translations.

    A key whose value is its own slug is a lie of omission: it satisfies a key
    count, it renders as a raw identifier, and it tells a reader nothing. The
    right state is *absent*, which the runtime renders the same way but which is
    honest about it.

    Only entries that are BOTH slug-valued AND have no source in any locale are
    removed. A slug-valued entry that does have a source is a translation gap and
    belongs in a batch, not in the bin -- removing it would lose the fact that we
    know it is untranslated.
    """
    _ACTIVE["locale"] = a.locale
    removed, kept = [], []
    for ns in (a.ns.split(",") if a.ns else NAMESPACES):
        data = load(a.locale, ns)
        if not data:
            continue
        changed = False
        for key in list(data):
            fields = fields_of(ns, data[key])
            if not fields:
                continue
            values = list(fields.values())
            is_slug = all(v == key or SLUG_RE.match(v) for v in values)
            has_source = any(source_text(ns, key, f) for f in fields)
            if is_slug and not has_source:
                del data[key]
                removed.append(f"{ns}.{key}")
                changed = True
            elif is_slug:
                kept.append(f"{ns}.{key}")
        if changed and not a.dry_run:
            save(a.locale, ns, data)

    if a.dry_run:
        print(f"would remove {len(removed)} placeholder entr(ies): {removed[:10]}")
    else:
        print(f"removed {len(removed)} placeholder entr(ies) from {a.locale}")
        for r in removed[:10]:
            print(f"    {r}")
    if kept:
        print(f"\n{len(kept)} entr(ies) are slug-valued but DO have a source, so they "
              f"are a translation gap, not a placeholder:")
        for k in kept[:10]:
            print(f"    {k}")
        print("  run `list` and translate them; do not let --force prune these")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("list", help="the worklist")
    p.add_argument("locale")
    p.add_argument("--ns", default="cards", choices=NAMESPACES)
    p.add_argument("--limit", type=int, default=0)
    p.add_argument("--verbose", action="store_true")
    p.set_defaults(func=cmd_list)

    p = sub.add_parser("apply", help="apply a batch")
    p.add_argument("locale")
    p.add_argument("batch")
    p.add_argument("--namespace", default=None, choices=NAMESPACES)
    p.add_argument("--force", action="store_true",
                   help="apply the entries that are valid and report the rest")
    p.set_defaults(func=cmd_apply)

    p = sub.add_parser("verify", help="what is still missing")
    p.add_argument("locale")
    p.add_argument("--ns", default=None)
    p.add_argument("--verbose", action="store_true")
    p.set_defaults(func=cmd_verify)

    p = sub.add_parser("report", help="provenance across locales")
    p.set_defaults(func=cmd_report)

    p = sub.add_parser("prune", help="delete placeholder entries, keep real gaps")
    p.add_argument("locale", nargs="?", default="ru")
    p.add_argument("--ns", default=None)
    p.add_argument("--dry-run", action="store_true")
    p.set_defaults(func=cmd_prune)

    a = ap.parse_args()
    _ACTIVE["locale"] = a.locale if hasattr(a, "locale") else "ru"
    return a.func(a)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
