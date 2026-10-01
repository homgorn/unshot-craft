"""Final gate: the layer's own artifacts must be self-consistent before anyone
builds on it. F070's ledger entry tells a verifier to run checks; this is the
same checks, run once here so the report is evidence rather than assertion.
"""
import io, json, os, sqlite3, subprocess, sys

base = r'C:\susa ai\shotcraft'
ok, bad = [], []

# 1. ledger parses and the 5 catalog features are present, all not passing
feats = json.load(io.open(os.path.join(base, 'specs', 'feature-list.json'), encoding='utf-8'))
ids = [f['id'] for f in feats]
for i in ['F070', 'F071', 'F072', 'F073', 'F074']:
    if i in ids:
        f = next(x for x in feats if x['id'] == i)
        if f.get('passes') is False and f.get('steps') and f.get('description'):
            ok.append('%s: %d steps, passes=false (correct -- only a verifier may set it)' % (i, len(f['steps'])))
        else:
            bad.append('%s: passes=%r steps=%d -- a feature must ship unproven' % (i, f.get('passes'), len(f.get('steps', []))))
    else:
        bad.append('%s missing from the ledger' % i)
if len(feats) == 23:
    ok.append('ledger has 23 features (18 baseline + 5 catalog)')

# 2. every catalog feature step is executable in form: starts with a verb and
#    names a file, command or observable. This is the F070 spec's own test.
import re
for i in ['F070', 'F071', 'F072', 'F073', 'F074']:
    f = next(x for x in feats if x['id'] == i)
    # Accept the step grammar the baseline ledger already uses: a leading verb
    # (Run/Verify/Open/Delete/Count/Re-run/Request/Ask/Install/Clone/Pull/Compare)
    # plus an observable (exists/returns/is/are/equals/contains/matches/reports/
    # changed/resolves/fails/passes/exits/has/carries/shows/includes/null/byte-
    # identically). Reject a step that names neither a command nor a file/observable.
    LEAD = r'(Run:|Verify |verify |Open |Delete |Count |Re-run|Request |Ask |Install |Clone |Pull |Compare )'
    OBS = r'(exists|returns|is |are |equals|contains|matches|reports|changed|resolves|fails|passes|exits|has |carries|shows|includes|null|byte-identically|no such|not |present|correct)'
    vague = [st for st in f['steps']
             if not (re.search(LEAD, st) and re.search(OBS, st))
             and not re.search(r'(python |\.py|\.md|\.json|\.csv|/\w)', st)]
    if vague:
        bad.append('%s has unverifiable steps: %s' % (i, vague))
    else:
        ok.append('%s: all %d steps name an observable' % (i, len(f['steps'])))

# 3. the DDL applies and the FK guard holds
r = subprocess.run([sys.executable, os.path.join(base, 'platform', 'catalog', 'validate_schema.py')],
                   capture_output=True, text=True, cwd=base)
out = r.stdout
if r.returncode == 0 and 'DDL: applied clean' in out and 'cross-corpus FKs declared: 2' in out \
   and '[Subject] intact=True' in out:
    ok.append('DDL applies clean; 2 cross-corpus FKs declared and stubbed; [Subject] survives')
else:
    bad.append('DDL gate failed:\n' + out[-800:] + r.stderr[-400:])

# 4. the docs the layer claims to have patched actually mention it
checks = [
    ('AGENTS.md', 'data/cinematic/'),
    ('AGENTS.md', '0007'),
    ('docs/architecture/README.md', 'data/cinematic/'),
    ('prompts/README.md', 'catalog/'),
    ('data/README.md', '[Subject]'),
    ('docs/adr/0007-cinematic-catalog-layer.md', 'Status: accepted'),
    ('specs/features/F070-cinematic-catalog-ingest.md', 'Status: specified'),
    ('progress.md', 'F070'),
]
for rel, needle in checks:
    p = os.path.join(base, rel.replace('/', os.sep))
    s = io.open(p, encoding='utf-8').read()
    if needle in s:
        ok.append('%s mentions %r' % (rel, needle))
    else:
        bad.append('%s does not mention %r' % (rel, needle))

# 5. the cinematique side of the bridge
ci = r'C:\susa ai\cinematique'
for rel, needle in [('INTEGRATION.md', 'technique_motion'),
                    ('INTEGRATION.md', '117 of 150'),
                    ('ARCHITECTURE.md', 'RENDER / MOTION LAYER')]:
    s = io.open(os.path.join(ci, rel), encoding='utf-8').read()
    if needle in s:
        ok.append('cinematique/%s mentions %r' % (rel, needle))
    else:
        bad.append('cinematique/%s does not mention %r' % (rel, needle))

print('PASS (%d)' % len(ok))
for o in ok:
    print('  +', o)
if bad:
    print()
    print('FAIL (%d)' % len(bad))
    for b in bad:
        print('  -', b)
    sys.exit(1)
print()
print('layer is consistent; nothing here marks itself done that is not')
