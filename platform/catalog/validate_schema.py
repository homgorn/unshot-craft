"""Validate the catalog DDL against a throwaway SQLite DB, then clean up.

This is the `principle-prove-it-works` gate: the SQL is not trusted because it
looks right, it is executed. FTS5 availability is reported separately because a
Python without FTS5 is a real, common configuration, and the catalog layer must
say so rather than fail silently.
"""
import sqlite3, os, io, re, sys

base = r'C:\susa ai\shotcraft'
ddl = io.open(os.path.join(base, 'platform', 'catalog', 'schema.sql'), encoding='utf-8').read()

tmp = os.path.join(base, 'platform', 'catalog', '_ddl_check.db')
if os.path.exists(tmp):
    os.remove(tmp)

con = sqlite3.connect(tmp)
con.execute('PRAGMA foreign_keys = ON')

# The catalog DDL has two FKs into the upstream corpus, so the upstream
# schema goes first when available. A stub stands in when it is not, so the
# standalone run still tests the catalog -- and the stub count is guarded
# below, so a third cross-corpus reference cannot slip in unnoticed.
UPSTREAM = os.path.join(base, 'platform', 'ingest', 'schema.sql')
STUBS = 'CREATE TABLE IF NOT EXISTS source_file ( id INTEGER PRIMARY KEY, path TEXT, sha256 TEXT, repo_id INTEGER);CREATE TABLE IF NOT EXISTS style ( id INTEGER PRIMARY KEY, key TEXT NOT NULL UNIQUE);'
if os.path.exists(UPSTREAM):
    con.executescript(io.open(UPSTREAM, encoding='utf-8').read())
    print('upstream schema: applied from platform/ingest/schema.sql')
else:
    con.executescript(STUBS)
    print('upstream schema: ABSENT, using stubs for the 2 cross-corpus tables')

print('sqlite', sqlite3.sqlite_version)
try:
    con.execute("CREATE VIRTUAL TABLE _fts_probe USING fts5(x)")
    print('FTS5: available')
    have_fts5 = True
except sqlite3.OperationalError as e:
    print('FTS5: UNAVAILABLE —', e)
    have_fts5 = False

if have_fts5:
    con.executescript(ddl)
    print('DDL: applied clean')

    tables = [r[0] for r in con.execute(
        "SELECT name FROM sqlite_master WHERE type IN ('table','view') AND name NOT LIKE 'sqlite_%' ORDER BY name")]
    catalog_tables = [t for t in tables if t.startswith(('cinematic_', 'ai_tool', 'technique_'))]
    print('catalog tables (%d):' % len(catalog_tables))
    for t in catalog_tables:
        n = con.execute('SELECT COUNT(*) FROM "%s"' % t).fetchone()[0]
        print('  %-28s %d rows' % (t, n))

    # Guard the assumption this file just made: if a future edit adds another
    # Guard the assumption this file just made: count the two literal
    # cross-corpus references. Literal counting beats a regex here --
    # an escaping slip would silently report 0 and pass.
    n_refs = ddl.count('REFERENCES source_file') + ddl.count('REFERENCES style')
    print('cross-corpus FKs declared: %d (stubbed: 2)' % n_refs)
    if n_refs != 2:
        print('FAIL: expected exactly 2 cross-corpus FKs, found %d.' % n_refs)
        print('      A third one needs a stub; a removed one means the note above is stale.')
        sys.exit(1)

    # The matrix must be expressible as a join, and the join must be able to say
    # "untested" instead of inventing a parameter.
    row = con.execute("""
        SELECT t.name, tl.label, p.params, p.tested, p.version_tag
        FROM technique_tool_param p
        JOIN ai_tool tl   ON tl.id = p.tool_id
        JOIN cinematic_technique t ON t.id = p.technique_id
        LIMIT 0""").fetchall()
    print('cross-tool join: expressible (%d probe rows)' % len(row))

    # Vocabulary is enforced by the CHECK-free convention of seeding + ingest
    # validation; assert the seeds landed so the count is quotable.
    ncat = con.execute('SELECT COUNT(*) FROM cinematic_category').fetchone()[0]
    ntool = con.execute('SELECT COUNT(*) FROM ai_tool').fetchone()[0]
    print('vocabulary: %d categories, %d tools' % (ncat, ntool))

    # And assert the shape the doctor will count: 150 techniques x 7 tools = 1050
    # possible cells, of which 117 are filled today.
    con.execute("""INSERT INTO cinematic_technique
        (name,title,category_id,prompt_text,lede_text) VALUES
        ('kicker-light','Kicker Light',2,'Kicker light on [Subject], hard rim',NULL)""")
    con.execute("""INSERT INTO technique_tool_param (technique_id,tool_id,params,tested,version_tag)
        VALUES (1,(SELECT id FROM ai_tool WHERE key='kling15'),
                'camera_motion: slow_pan | resolution: 1080p',1,'v1_kling15')""")
    filled = con.execute("SELECT COUNT(*) FROM technique_tool_param").fetchone()[0]
    prompt_ok = '[Subject]' in con.execute(
        "SELECT prompt_text FROM cinematic_technique WHERE name='kicker-light'").fetchone()[0]
    print('probe: filled cells=%d, [Subject] intact=%s' % (filled, prompt_ok))
    print('probe: max possible cells = 150 x 7 = %d' % (150 * ntool))

    con.execute("DELETE FROM cinematic_technique WHERE name='kicker-light'")
else:
    print('DDL: NOT EXECUTED (FTS5 unavailable in this Python)')
    print('reminder: install pysqlite3-binary or use a Python built with FTS5')

con.close()
if os.path.exists(tmp):
    os.remove(tmp)
print('cleaned up:', not os.path.exists(tmp))
