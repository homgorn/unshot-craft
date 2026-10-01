# scroll-brake-moves

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/scroll-brake-moves`.

## Identity

- **slug**: `scroll-brake-moves` (join key across cards, demos, media and deep links)
- **category**: `data` — Data & Metrics / 数据与指标
- **energy**: `高开中收` — arc or n/a, not sortable
- **suggested duration**: A 4–5s / B 5s → **150 frames @30fps = 5.0s**
- **cross-category tags**: `data`, `rhythm`
- **upstream source**: references/shots/data/scroll-brake-moves.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| B | `brake-reticle-lock` | 150f | B | `demos/data/scroll-brake-moves/BrakeReticleLock.tsx` |
| A | `changelog-scroll-brake` | —f | B | `demos/data/scroll-brake-moves/ChangelogScrollBrake.tsx` |

## What it does

长卷急刹两式——changelog-scroll-brake 基本款（高速长卷指数减速精准停位+目标抬升）与 brake-reticle-lock 组合款（急刹帧同帧准星咬合）

**When to use it.** changelog/发布史/长列表段落："一直在发货，今天这条最大"；要给停点更强打击感用 B

**Why this shot earns its place.** Linear changelog 视频语法：一整年的更新日志作为长卷高速掠过 （糊成色带），指数减速精准急刹停在本次发布那条上，该条抬升离面 高亮、其余退暗——密度感讲"一直在发货"，急停讲"今天这条最大"。 B 是组合变异：急刹帧**同帧**四个 L 角标从画外飞入咬合锁定停点 条目——急刹的"哐"与咬合的"咔"叠在同一帧共振（组合命门： 角标起跳帧=列表首停帧，错开退化成两招并置）。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 减速曲线 | A 纯 out-exp；B 加"冲过头 30px 回弹" | 匀速滚读作跑马灯；B 的过头回弹是"哐"的来源 |
| blur 驱动 | 帧间位移差分 ` | p(f)-p(f-1) |
| 行高节奏 | 72/94/116 三档错落 | 等高行高速掠过时色带无节奏 |
| 停位 | 目标行停画面纵向正中 | 停偏读作事故 |
| B 共振帧 | 角标挂载起跳帧 = 列表首次停住帧（严格同帧） | 组合命门，错 2f 以上就散 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 与 timeline-travel 分工：本卡纵向列表急刹停"最新"，
- 高速段条目内容不用真实可读文本——反正糊成色带，占位灰块即可；
- 停点后其余行退暗 0.38 是构图动作：别退到 0（上下文消失）
- 声音：高速段低频 riser 铺垫，急刹一声 impact；B 咬合帧

## Card structure

`intention` | `variants` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/data/scroll-brake-moves/BrakeReticleLock.tsx`
- `demos/data/scroll-brake-moves/ChangelogScrollBrake.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
