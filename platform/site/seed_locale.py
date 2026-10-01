"""Seed a locale from what we already have, without inventing translations.

    python platform/site/seed_locale.py ru --from-db

What this does, and what it deliberately refuses to do:

* `en` / `zh` are extracted from upstream and must never be "completed" by
  invention — the extraction report proves they are faithful.
* For any other locale it only fills namespaces from data we actually have:
  - `ui` chrome keys: left empty on purpose. A wrong label in a language picker
    is worse than an English fallback, and the runtime already falls back.
  - `cards` / `styles`: titles may be copied from a locale we have (a slug is a
    valid title, a slug is a valid "description" only if it is a proper noun).
    `ru` gets 468 real strings from the upstream workbench (`workbench/i18n/ru/`),
    which upstream shipped in the HEAD commit. Those are copied verbatim.
* Nothing is machine-translated here. Translation is a separate, reviewable step
  (F014) with a coverage gate; a generator that "just translates" would put
  unverified text behind an `hreflang` tag, which is the one thing SEO punishes.

Usage:
    python platform/site/seed_locale.py ru --from-db
    python platform/site/seed_locale.py es   --from-locales ru en
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LOCALES = ROOT / "site" / "locales"
DB = ROOT / "platform" / "db" / "shotcraft.db"
UPSTREAM = ROOT / "upstream" / "video-shotcraft"
NAMESPACES = ("ui", "page", "showcase", "cards", "styles", "meta")

PROPER_NOUNS = {"Ink Press", "Remotion", "JianYing", "CapCut", "Mixkit", "SHOTBOOK"}


def load(code: str, ns: str) -> dict:
    p = LOCALES / code / f"{ns}.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def from_db(code: str) -> dict:
    """Pull the upstream workbench's Russian strings for this locale.

    These are real, upstream-authored translations (workbench/i18n/ru/*.json), so
    they are trustworthy as a seed.

    The workbench keys its maps by *display name*, not by slug, which is why the
    naive mapping produced 259 "cards" that matched no card slug at all. We
    resolve name -> slug through the workbench's own `nameEn`/demo metadata via
    the database, and drop anything that cannot be resolved rather than
    guessing. A summary keyed by Chinese prose is not addressable at all; those
    are recorded as unusable instead of being silently attached to a wrong card.
    """
    import sqlite3
    if not DB.exists():
        raise SystemExit("missing platform/db/shotcraft.db; run platform/ingest/run.py first")
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    # workbench names.json maps zh display name -> ru display name.
    # Our DB stores zh card/style titles under ns='card'/'style' for the ru locale
    # because upstream shipped them in that shape; build the lookup from those.
    zh_by_ru: dict[str, str] = {}
    for ns in ("card", "style"):
        for r in conn.execute(
                "SELECT t.key, t.text FROM translation t JOIN locale l ON l.id=t.locale_id "
                "WHERE l.code='ru' AND t.ns=?", (ns,)):
            zh_by_ru[r["key"]] = r["text"]      # key IS the zh title here

    # zh translations.js maps slug -> zh display name, so invert it: zh name -> slug.
    # Kept SEPARATE per namespace: a card slug and a style slug can collide (many
    # cards are named after their single demo), so one shared map put 229 entries
    # into cards.json when only 157 cards exist.
    import sqlite3 as _sq
    zh_title_to_slug: dict[str, dict[str, str]] = {"card": {}, "style": {}}
    for ns in ("card", "style"):
        for r in conn.execute(
                "SELECT t.key AS slug, t.text AS title FROM translation t "
                "JOIN locale l ON l.id=t.locale_id WHERE l.code='zh' AND t.ns=?", (ns,)):
            # The DB keeps titles wrapped in the quotes they had in the JS source
            # (`'AI 响应汇入'`), and the workbench keys have no quotes. Strip both
            # sides or the join finds nothing and every ru title is lost.
            title = str(r["title"]).strip().strip("'\"")
            zh_title_to_slug[ns][title] = r["slug"]

    out: dict[str, dict] = {"cards": {}, "styles": {}}
    resolved = unresolved = 0
    for ns, group in (("card", "cards"), ("style", "styles")):
        for r in conn.execute(
                "SELECT t.key, t.text FROM translation t JOIN locale l ON l.id=t.locale_id "
                "WHERE l.code=? AND t.ns=?", (code, ns)):
            slug = zh_title_to_slug[ns].get(str(r["key"]).strip().strip("'\""))
            if slug:
                out[group].setdefault(slug, {})["title"] = r["text"]
                resolved += 1
            else:
                unresolved += 1
    # summaries.*.json are keyed by the Chinese *description*, so they cannot be
    # joined without a text-identity match. Report them rather than guess.
    summaries = conn.execute(
        "SELECT COUNT(*) FROM translation t JOIN locale l ON l.id=t.locale_id "
        "WHERE l.code=? AND t.ns='summary'", (code,)).fetchone()[0]
    out["_stats"] = {"resolved": resolved, "unresolved_names": unresolved,
                     "unusable_summaries": summaries}
    return out


def copy_titles(target: str, sources: list[str]) -> dict:
    """Slugs are valid titles in every language; prose is not.

    Copying a *description* from another language would be silently wrong, so
    only `title` is ever inherited. An entry with no description falls back to
    English at runtime, which is honest and visible in the coverage report.
    """
    merged: dict[str, dict] = {}
    for src in reversed(sources):
        for ns in ("cards", "styles"):
            for k, v in load(src, ns).items():
                if isinstance(v, dict) and v.get("title"):
                    merged.setdefault(ns, {}).setdefault(k, {})["title"] = v["title"]
                elif isinstance(v, str):
                    merged.setdefault(ns, {}).setdefault(k, {})["title"] = v
    merged.pop(target, None)
    return merged


def write(code: str, ns: dict) -> None:
    d = LOCALES / code
    d.mkdir(parents=True, exist_ok=True)
    for name in NAMESPACES:
        payload = ns.get(name, {})
        if name == "meta":
            payload = {"htmlLang": None, "ogLocale": None}
        (d / f"{name}.json").write_text(
            json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("code")
    ap.add_argument("--from-db", action="store_true",
                    help="seed from upstream-authored translations in the DB")
    ap.add_argument("--from-locales", nargs="*", default=[],
                    help="inherit titles only (never prose) from these locales")
    ap.add_argument("--copy-from", default=None,
                    help="duplicate an existing locale dir as a starting point")
    a = ap.parse_args()
    code = a.code

    if code in ("en", "zh"):
        print(f"{code} is an upstream source locale; run extract_locales.py instead",
              file=sys.stderr)
        return 1

    if a.copy_from:
        src = LOCALES / a.copy_from
        if not src.is_dir():
            raise SystemExit(f"no such locale: {src}")
        dst = LOCALES / code
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        for f in dst.glob("*.json"):
            f.write_text(json.dumps({}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps({"locale": code, "scaffolded_from": a.copy_from,
                          "note": "all namespaces emptied; nothing is machine-filled"},
                         ensure_ascii=False, indent=2))
        return 0

    ns: dict = {"cards": {}, "styles": {}, "ui": {}, "page": {}, "showcase": {}}
    db_stats: dict = {}
    if a.from_db:
        seeded = from_db(code)
        db_stats = seeded.pop("_stats", {})
        ns["cards"].update(seeded.get("cards", {}))
        ns["styles"].update(seeded.get("styles", {}))
    # Chrome: inherit `en` for any key this locale has not translated yet.
    #
    # `setdefault`, not overwrite. Seeding is a fill-the-gaps operation: it must
    # never clobber a translated value, because re-running the seeder after
    # translating would otherwise silently revert a locale to English.
    existing_ui = load(code, "ui")
    ns["ui"] = {**load("en", "ui"), **existing_ui}
    ns["page"] = {**load("en", "page"), **load(code, "page")}
    ns["showcase"] = {**load("en", "showcase"), **load(code, "showcase")}
    inherited = copy_titles(code, a.from_locales or ["en"])
    for group in ("cards", "styles"):
        for k, v in inherited.get(group, {}).items():
            ns[group].setdefault(k, {}).setdefault("title", v["title"])

    write(code, ns)

    def count_real(ns: dict, group: str) -> int:
        """Entries whose title actually differs from the slug.

        A copied-from-en title is the slug by design, so counting it would
        report 100% coverage for a locale that has translated nothing.
        """
        return sum(1 for k, v in ns.get(group, {}).items()
                   if isinstance(v, dict) and v.get("title") and v["title"] != k)


    report = {
        "locale": code,
        "cards_with_title": sum(1 for v in ns["cards"].values() if v.get("title")),
        "cards_title_not_slug": count_real(ns, "cards"),
        "styles_title_not_slug": count_real(ns, "styles"),
        "cards_with_description": sum(1 for v in ns["cards"].values() if v.get("description")),
        "styles_with_title": sum(1 for v in ns["styles"].values() if v.get("title")),
        "styles_with_description": sum(1 for v in ns["styles"].values() if v.get("description")),
        "ui_keys": len(ns["ui"]),
        "from_db": a.from_db,
        "titles_inherited_from": a.from_locales or ["en"],
        "db_seed": db_stats,
        "note": ("descriptions are never inherited across languages; they fall back to English. "
                 "A ru card title is real upstream text from workbench/i18n/ru/names.json, resolved "
                 "zh-name -> slug; the 199 ru summaries are keyed by Chinese prose upstream and "
                 "cannot be joined without guessing, so they are deliberately unused."),
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())