"""Negative tests for platform/docs_freshness.py.

    python platform/_gate_test.py

A gate nobody has tried to break is an assumption. These three mutations each
target a way the check could be made to pass without the document being right:

  1. a number that is simply wrong            -> must FAIL with both values
  2. the anchor phrase deleted or reworded    -> must FAIL as "no longer verified"
  3. the line re-wrapped                      -> must still PASS, because the
     gate normalises whitespace; if a rewrap could switch a check off, the
     check would be decorative
"""
import re
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

DOC = Path("progress.md")
GATE = "platform/docs_freshness.py"
# Bytes, not text. Path.write_text goes through newline translation on Windows and
# would rewrite the file as CRLF, so the test would dirty the repository it is
# testing -- which is the failure mode this whole exercise is about.
ORIGINAL = DOC.read_bytes()
original = ORIGINAL.decode("utf-8")


def write(text: str) -> None:
    DOC.write_bytes(text.encode("utf-8"))


def run() -> tuple[int, str]:
    r = subprocess.run([sys.executable, GATE], capture_output=True, text=True,
                       encoding="utf-8", env={**__import__("os").environ,
                                              "PYTHONIOENCODING": "utf-8"})
    return r.returncode, r.stdout


cases = [
    ("wrong number in a table",
     lambda t: re.sub(r"\| techniques \| \d+ across", "| techniques | 999 across", t),
     "fail"),
    ("anchor phrase reworded away",
     lambda t: t.replace("| cards | 157 / 157 |", "| card count | 157 / 157 |"),
     "fail"),
    ("claim row deleted entirely",
     lambda t: re.sub(r"\| locales tracked \| \d+.*\n", "", t),
     "fail"),
    ("a different document drifts",
     lambda t: t.replace("| aesthetic rules | 27 |", "| aesthetic rules | 30 |"),
     "fail"),
    ("line re-wrapped, nothing else changed",
     lambda t: t.replace("| audio assets audited | 154 (5 untraceable",
                         "| audio assets audited | 154\n(5 untraceable"),
     "pass"),
    ("extra blank line inside a table row",
     lambda t: t.replace("| cells filled | 791 |",
                         "| cells\n\nfilled | 791 |"),
     "pass"),
]

fails = 0
try:
    for name, mutate, expect in cases:
        mutated = mutate(original)
        if mutated == original:
            print(f"  SKIP  {name}: the mutation did not change the file")
            fails += 1
            continue
        write(mutated)
        code, out = run()
        want = 0 if expect == "pass" else 1
        ok = code == want
        detail = ""
        m = re.search(r"FAIL .*", out)
        if m:
            detail = m.group(0)[:88]
        print(f"  {'ok  ' if ok else 'FAIL'} {name:<38} exit={code} (want {want})  {detail}")
        fails += 0 if ok else 1
finally:
    DOC.write_bytes(ORIGINAL)

code, out = run()
restored = code == 0 and DOC.read_bytes() == ORIGINAL
print(f"\n  {'ok  ' if restored else 'FAIL'} document restored byte-for-byte, "
      f"gate green again (exit={code})")
fails += 0 if restored else 1

print(f"\n{len(cases) + 1 - fails}/{len(cases) + 1} negative tests behaved as required")
raise SystemExit(1 if fails else 0)
