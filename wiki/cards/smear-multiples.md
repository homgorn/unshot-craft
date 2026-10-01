# smear-multiples

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/smear-multiples`.

## Identity

- **slug**: `smear-multiples` (join key across cards, demos, media and deep links)
- **category**: `rhythm` — Rhythm & Montage / 节奏与蒙太奇
- **energy**: `中高` — rank 5/8
- **suggested duration**: 元素级技法（移动 12f + 合拢回弹 8f，寄生在位移动作上） → **12 frames @30fps = 0.4s**
- **cross-category tags**: `rhythm`, `effects`
- **upstream source**: references/shots/rhythm/smear-multiples.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `smear-multiples` | —f | B | `demos/rhythm/smear-multiples/SmearMultiples.tsx` |

## What it does

残像分身——卡片高速横移时拖 4 个清晰可数的半透明分身副本，落位瞬间收拢合一；motion blur 的动画式平替

**When to use it.** 元素高速位移段想要"漫画式速度感"而非"摄影式模糊"时；与 CameraMotionBlur 二选一

**Why this shot earns its place.** 快速位移的速度感库内标准答案是 CameraMotionBlur（摄影隐喻：快门拖影， 连续的糊）。本卡给第二个答案，动漫演出的 smear frame 传统：残像是 **离散、清晰、可数的**完整副本——观众能数出 4 张卡，读作"快到留下 分身"而非"快到糊掉"。两者气质完全不同：blur 是实拍级质感，分身是 漫画级趣味；同一次位移二选一，叠用读作渲染错误。分身式还有一个 实用优势：残像里内容仍可辨，适合"移动的东西本身是信息"的场景。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 分身数/间隔 | 4 个 / 各差 2f | >5 个读作队伍；间隔 >3f 断成跳帧 |
| 移动速度 | ~900px/12f（峰值 ~100px/f） | 慢移动不配分身（门限管住）；快过 3f/程分身来不及被看见 |
| 合拢窗口 | 落位前 3f 内收干 | 分身残留到落位后读作重影故障 |
| 收尾 | 落位回弹后真静止 ≥20f | R1 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 与 CameraMotionBlur 同一次位移**互斥**；同片不同镜头可以各用（一次
- 分身是"清晰完整副本"——加 blur、拉伸、变形都会滑向另一个手法
- 深底浅卡对比度下分身层次才读得开；同色系底上 0.09 那档会消失，

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/rhythm/smear-multiples/SmearMultiples.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
