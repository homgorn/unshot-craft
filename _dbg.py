import sqlite3, sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")

c = sqlite3.connect("platform/db/shotcraft.db")
q = lambda s: c.execute(s).fetchone()[0]
print("translation rows:", q("SELECT COUNT(*) FROM translation"))
for r in c.execute("""SELECT lo.code, t.method, t.status, COUNT(*)
                      FROM translation t JOIN locale lo ON lo.id=t.locale_id
                      GROUP BY lo.code, t.method, t.status ORDER BY lo.code"""):
    print("  ", tuple(r))
print("reviewed rows:", q("SELECT COUNT(*) FROM translation WHERE status='reviewed'"))

for p in ("site/locales/ru/cards.json", "site/locales/ru/styles.json",
          "site/locales/ru/ui.json"):
    import json
    d = json.loads(Path(p).read_text(encoding="utf-8"))
    print(f"{p}: {len(d)} keys")
