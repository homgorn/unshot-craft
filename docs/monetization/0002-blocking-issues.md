# Two blocking issues — correction and escalation

- Status: **blocks paid delivery.** Not a roadmap item.
- Date: 2026-10-01
- Canonical monetization doc: [`brainstorm.md`](brainstorm.md). This document does not
  re-rank it; it corrects one of its premises and escalates one data defect that has
  legal consequences.
- Verify: `python platform/doctor.py` → `license.audio_consistency` FAIL

---

## 1. The workbench may not be Apache-2.0, and it is the biggest asset we have

### The contradiction

`brainstorm.md` says two things that cannot both hold:

> **"Touch `video-talkcraft` commercially. PolyForm Noncommercial. Reading and
> porting techniques is fine … Shipping is not."**

> **"Build a full editor — The upstream workbench already exists and is Apache-2.0."**

The second sentence treats upstream's `workbench/` as clean Apache-2.0 code. It is
not straightforwardly that.

### The evidence

`upstream/video-shotcraft/references/workbench.md`, lines 3–4:

> `workbench/` 是一个剪映式的浏览器工作台（多轨时间线 + 素材库 + 属性面板 + Remotion
> 实时预览 + 一键导出），**从系列姊妹项目 video-talkcraft 的 `workbench/` 移植而来**。

> …a CapCut-style browser workbench, **ported from the sibling project
> video-talkcraft's `workbench/`**.

And from our own `license_registry`:

| subject | SPDX | commercial_use | blocking |
|---|---|---|---|
| video-talkcraft (sibling skill) | PolyForm Noncommercial 1.0.0 | requires-license | **1** |

So: a **PolyForm Noncommercial** workbench was ported into an **Apache-2.0**
repository. PolyForm NC permits use, copying and modification for noncommercial
purposes and requires a licence for commercial use of the software. A port is a
derivative work; wrapping it in an Apache-2.0 file tree does not launder that. The
outer licence and the inner licence now disagree, and the more restrictive one wins.

### What this costs us

The workbench is the most differentiated thing in the corpus: a real multi-track
editor with a schema-driven inspector, `npm run parity` pixel-diff verification, and
an i18n layer with three locales. It is also the part `brainstorm.md` wants to avoid
rebuilding ("we would be rebuilding a CapCut clone").

If it is encumbered then the correct strategy is not "don't touch it commercially" —
it is that **we cannot ship it, cannot market it as ours, and cannot base a product
on it**, without a licence from that author. That is a very different sentence, and
it should not be discovered during an enterprise sales call.

### The recommendation

Two emails, in this order, before any further work on the workbench:

1. **Ask the `video-talkcraft` author for a commercial licence** for the workbench
   code. He is the same author as upstream (`Vincentwei1021`), the relationship is
   warm, and ADR 0005 already establishes a good-faith posture. A conversation, not
   a purchase.
2. **In parallel, ask a lawyer the narrow question:** does the PolyForm NC
   restriction on `video-talkcraft` propagate into `video-shotcraft`'s
   `workbench/`? This is a short, specific question and it deserves an answer from
   someone who does this for a living, not from us.

Until both are answered:

> `workbench/` is out of scope for anything commercial, and no product doc may
> describe it as ours or Apache-2.0.

Note this also touches ADR 0005, which recorded `video-talkcraft` as
`requires-license / blocking` but framed the risk as *"do not ship talkcraft code"*.
The sharper risk is that **we may already be shipping it**, inside upstream, inherited.

---

## 2. Six audio files are recorded as blocked and simultaneously as cleared

### The data defect

`assets/audio/ATTRIBUTION.md` records 6 of the 154 audio files as 无法反查 —
not traceable to a source URL, therefore not cleared for commercial delivery.
`license_registry` agrees and marks them `blocking = 1`.

But the asset table says otherwise:

```
audio_asset:   154 rows, 154 commercial_ok = 1, 0 traceable = 0
license_registry: 3 blocking rows, one of which is the audio provenance
```

`python platform/doctor.py` flags this as `license.audio_consistency` **FAIL**. It is
not a stylistic disagreement between two tables: **the field that is supposed to stop
a file from shipping in a paid delivery is set to "clear" on every single row.**

AGENTS.md hard rule 4 states the principle for prose — *"never replace the verbatim
column with the normalized value"* — and the same discipline should apply here in the
other direction: `commercial_ok` must be **derived from** `license_registry`, never
asserted independently.

### Why it matters beyond tidiness

`brainstorm.md` Tier 0 starts with an agency offer in week 0–1. An agency deliverable
is a paid, commercial film. If any of those 6 files is in its audio bed, we have
invoiced for something we cannot prove we may use. That is the entire "we must not
touch audio commercially" rule being violated by a default value rather than a
decision.

### The fix

Small, and it belongs in the ingest so it cannot drift again:

- derive `audio_asset.commercial_ok` and `traceable` from the `license_registry`
  row for that file's source, not from a literal;
- parse `assets/audio/ATTRIBUTION.md` into `attribution_entry` — that table exists,
  is the right home, and currently holds **0 rows**;
- treat "registry has no entry for this file" as `commercial_ok = 0`, not `1`.
  Fail closed.

`doctor.py` already asserts the result. It should read FAIL until the ingest honours it.

---

## What this changes in `brainstorm.md`

Nothing about the tiering, which is sound. Two amendments:

1. **The "do not build a full editor" reasoning needs a second reason.** It currently
   rests on "upstream's workbench is Apache-2.0, we would be rebuilding a CapCut
   clone." If §1 resolves against us, we are barred from building the thing as well
   as barred from reusing the thing — which makes a hosted thin client over a clean
   reimplementation the only remaining option.
2. **Add a week-0 legal gate to the sequence.** `brainstorm.md` week 0–1 is "Agency
   first offer." Make it "Agency first offer, **after** §1 and §2 are cleared." Two
   emails and one ingest fix sit between us and the first invoice.

The one number from `brainstorm.md` — *does inbound say "render this" or "do this" for
me"* — is unchanged and still the right question. Neither of these issues changes the
answer; they change when we are allowed to start asking it.