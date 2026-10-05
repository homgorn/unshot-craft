"""Negative tests for the `_headers` line classifier.

    python platform/site/check_headers.py

`platform/site/check_dist.py` fails a build whose `_headers` has an indented path
pattern. A gate needs a negative test, or it is indistinguishable from a gate that
is always green: the three cases below each reproduce a way the classifier could
be wrong, and the six "must be accepted" cases pin down the half of the format
that is legitimately indented, so the check cannot be satisfied by flagging
everything.

`platform/_gate_test.py` is the same idea for `docs_freshness.py`.
"""
import importlib.util
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


bs = load("platform/site/build_site.py", "bs")
f = bs.indented_non_header

real = Path("_headers").read_text(encoding="utf-8")
bad = f(real)
print(f"real _headers: {len(real.splitlines())} lines, {len(bad)} flagged")
for b in bad:
    print("   FLAG:", repr(b))

print("\nnegative tests -- each of these must be caught")
cases = {
    "the bug we shipped": "/*\n  X-Frame-Options: DENY\n /media/*\n  Cache-Control: x\n",
    "tab-indented pattern": "/*\n\t/media/*\n  Cache-Control: x\n",
    "pattern after a comment": "# c\n  /assets/*\n  X: y\n",
}
fail = 0
for name, raw in cases.items():
    got = f(raw)
    ok = bool(got)
    fail += 0 if ok else 1
    print(f"  {'ok  ' if ok else 'FAIL'} {name}: {got}")

print("\npositive tests -- each of these must be accepted")
ok_cases = {
    "well-formed rule": "/*\n  X-Frame-Options: DENY\n/media/*\n  Cache-Control: x\n",
    "header with empty value": "  Referrer-Policy:\n",
    "header with a url value": "  CSP: default-src 'self'; img-src https://a.b\n",
    "comment inside a rule": "/*\n  # why\n  X-Frame-Options: DENY\n",
    "status-code rule": "404:\n  Cache-Control: x\n",
    "blank lines": "\n\n/*\n\n  X: y\n\n",
}
for name, raw in ok_cases.items():
    got = f(raw)
    bad_flag = bool(got)
    fail += 1 if bad_flag else 0
    print(f"  {'FAIL' if bad_flag else 'ok  '} {name}: {got}")

print(f"\n{'PASS' if fail == 0 and not bad else 'FAIL'}: "
      f"{fail} wrong classification(s), {len(bad)} false positive(s) on the real file")
raise SystemExit(1 if fail or bad else 0)