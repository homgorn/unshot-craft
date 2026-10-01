# tear-streak-transitions

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/tear-streak-transitions`.

## Identity

- **slug**: `tear-streak-transitions` (join key across cards, demos, media and deep links)
- **category**: `transition` — Transitions / 转场
- **energy**: `高` — rank 6/8
- **suggested duration**: 前态 ≥40f + 撕裂 17–24f + 收尾 ≥40f，约 4.5s（135–140f） → **40 frames @30fps = 1.3s**
- **cross-category tags**: `transition`, `effects`
- **upstream source**: references/shots/transition/tear-streak-transitions.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| A | `glitch-displace` | —f | B | `demos/transition/tear-streak-transitions/GlitchDisplace.tsx` |

## What it does

撕裂转场——glitch-displace 噪声撕裂（16 横条错位抖动中硬切），数字故障语义的条带级撕裂

**When to use it.** 高能换页：数字故障/断裂语义；页面完整性不破、能量拉满的条带级撕裂

**Why this shot earns its place.** 本卡管**条带级撕裂**——页面被切成横条高速运动，但每条内容完整。 这是反复裁决划出的品味分界：碎块系转场三连否（doom-melt 竖条坠落、 pixel-dissolve 方块翻黑、facade-block 砖块翻飞全部淘汰），条带系过关。碎块读作"页面被破坏"，条带读作"页面在高速 运动"——完整性不破、能量却拉满。横向撕：条带左右错位抖动 + 明暗重影，数字故障的灰阶降维（RGB split 改明暗双重影）。 适用系统故障/瞬间跳变语义。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 抖幅 | ±70px（spec 加码档），底层垫完整页防露底缝 | 峰值帧条带错位必须肉眼明显——±12px 级读不出撕裂 |
| 包络 | 45–48f out-cubic 冲起 → 平台 → 56–62f 线性消散 | 冲击判例：扩散 out-cubic、消散线性 |
| 重影 | ±12px 明暗双重影（brightness 0.45 / invert） | RGB 分离的灰阶降维；无重影只是抖不是 glitch |
| 摘罩 | 62f 起条带、重影、filter 全部条件卸载直出裸 B | opacity 0 不算摘；滤镜残留毁真静止 |
| 收尾 | 73f 真静止（≥40f） | R1 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- **条带不碎块**——后续同类手法一律做条带：横条各自完整，
- 高能转场，与 whip-pan/crash 系同片注意能量预算——
- 硬切藏在抖动衰减中（58f 切、62f 归位）——切点暴露在静止帧上

## Card structure

`intention` | `variants` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/transition/tear-streak-transitions/GlitchDisplace.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
