# page-turn-transitions

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/page-turn-transitions`.

## Identity

- **slug**: `page-turn-transitions` (join key across cards, demos, media and deep links)
- **category**: `transition` — Transitions / 转场
- **energy**: `中高` — rank 5/8
- **suggested duration**: 单式 前态建立 30f + 转场 20–38f + 收尾 ≥40f，约 4.4–4.7s → **30 frames @30fps = 1.0s**
- **cross-category tags**: `transition`
- **upstream source**: references/shots/transition/page-turn-transitions.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| B | `barn-door-split` | —f | B | `demos/transition/page-turn-transitions/BarnDoorSplit.tsx` |
| A | `cube-rotate` | —f | B | `demos/transition/page-turn-transitions/CubeRotate.tsx` |

## What it does

整页体块转场两式——cube-rotate 立方体翻转（两页贴盒子相邻面转 90°）与 barn-door-split 对开门裂幕（旧页裂两半滑出、新页迎上）

**When to use it.** 章节级换页：两个并列大段落之间的"翻篇"仪式；与 shot-transitions 系（镜头交棒）分工——那是"航拍机移过去"，这是"页面自己是实体"

**Why this shot earns its place.** shot-transitions 六式和 transition-travel/hidden-cut 都把页面当"场景" ——相机在场景间移动。本卡把页面当**实体**：它有厚度、有重量、会翻面 会裂开。体块隐喻的仪式感更强，适合章节级大换页（功能 A 讲完→功能 B） 而非镜头级小交棒。A 立方体是"空间上并列"——两页是盒子的两面， 暗示同级关系；B 对开门是"旧的让位"——旧页从正中撕开滑走、新页 从底下迎上来，暗示取代关系。按语义选：并列翻篇用 A，新旧交替用 B。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| A 结构命门 | 场景层 `translateZ(−W/2) rotateY(θ)` 把正面拉回 z=0 | 少了这层 hold 段页面尺度不对（被 perspective 推远） |
| A 转速 | θ 0→−90° / 38f inOut cubic；中段叠 blur 1.5px 落定摘 | <28f 读不出体块感；>50f 读作慢慢挪 |
| A 亮度对切 | 旧面 1→0.55、新面 0.55→1 + 接缝竖向渐变阴影 sin(pπ) | 无明暗对切两面读作同一张图在转 |
| B 预告 | 裂前中缝 2px 细线闪现两次（18–22/25–29f） | 直接裂开观众没看到裂点在哪 |
| B 滑出 | 各 translateX ∓980px / 20f Easing.in(cubic) 加速 | ease-out 滑出是"被推走"，ease-in 才是"让位" |
| B 撕裂边 | 内边缘 3px G.ink 亮线 + 8px 投影 | 无边线两半读作普通左右擦除 |
| 收尾 | 新页落定真静止 ≥40f | R1 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 一缝一式规矩同 shot-transitions；体块转场比镜头交棒更重，
- A 式官方 `@remotion/transitions` cube() 是付费件——本卡是 CSS 自实现，
- B 式两半必须**对位拼合无缝**（右半内层 translateX(−960px)）——
- 转场前后两页都要有 ≥30f 静止建立/收尾——两端都在动，体块感被

## Card structure

`intention` | `variants` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/transition/page-turn-transitions/BarnDoorSplit.tsx`
- `demos/transition/page-turn-transitions/CubeRotate.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
