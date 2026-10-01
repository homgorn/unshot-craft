# crash-zoom-punch

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/crash-zoom-punch`.

## Identity

- **slug**: `crash-zoom-punch` (join key across cards, demos, media and deep links)
- **category**: `camera` — Camera & Space / 运镜与空间
- **energy**: `高` — rank 6/8
- **suggested duration**: 约 0.5s 动作 + 前后 hold（动作 6–11f，前 hold ≥30f 建立全景、后 hold ≥45f 读特写） → **11 frames @30fps = 0.4s**
- **cross-category tags**: `camera`, `effects`
- **upstream source**: references/shots/camera/crash-zoom-punch.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `crash-impact-real` | 120f | B | `demos/camera/crash-zoom-punch/CrashImpactReal.tsx` |
| — | `crash-zoom-real` | 120f | B | `demos/camera/crash-zoom-punch/CrashZoomReal.tsx` |

## What it does

全景一拍急推到目标特写（6f），落位二选一——过冲回弹（弹性）或撞停震屏（重量）

**When to use it.** 功能段"点名"镜头——把观众视线一拍按到目标卡/模块上；强调级用撞停

**Why this shot earns its place.** 慢推近（spotlight-hero-card）是"请看"，急推是"看这个！"——一拍之内 从全景砸到特写，视线没有选择余地。落位质感分两款：回弹是弹性 （"看这个"），撞停震屏是重量（"就是它"），按强调级选。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 急推时长 | 6f（4–8f） | >10f 读作普通推近，冲击感消失 |
| 目标 zoom | 2.4–2.8 | 终点构图以目标卡占画面 60–75% 为准 |
| 回弹幅度 | zoom 的 3–6% | 过大读作弹簧玩具 |
| 震屏包络 | 14px·e^(−t/1.8) | 幅度须过肉眼阈值（可感性判例），>20px 读作故障 |

## Known pitfalls

- 终点必须是高清纹理槽位（card4-hires 级）——急推后全程特写它，
- 两款别混用：回弹后再震屏读作穿帮；一支片急推 ≤2 次（P4 手法去重精神） _(rules P4)_
- 参数经占位素材调校转正，非实战定稿，首次实战后回验

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/camera/crash-zoom-punch/CrashImpactReal.tsx`
- `demos/camera/crash-zoom-punch/CrashZoomReal.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
