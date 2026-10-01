# color-block-step-wipe

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/color-block-step-wipe`.

## Identity

- **slug**: `color-block-step-wipe` (join key across cards, demos, media and deep links)
- **category**: `transition` — Transitions / 转场
- **energy**: `中高` — rank 5/8
- **suggested duration**: A ~2.5s（生长 44f + 徽章 + hold）/ B ~1.5–2s（3 跳 30f + hold）；demo 合计 150f → **44 frames @30fps = 1.5s**
- **cross-category tags**: `transition`
- **upstream source**: references/shots/transition/color-block-step-wipe.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `color-block-step-wipe` | —f | B | `demos/transition/color-block-step-wipe/ColorBlockStepWipe.tsx` |

## What it does

离散阶跃色块吞屏两式——A 中央小条按 3–5 步硬跳阶跃扩成全屏（接管后徽章两跳弹出），B 色块从角落斜向 3 步吃屏并携带一张页面卡逐跳前进

**When to use it.** 品牌色转场/章节交接；"硬朗无缓动"的像素游戏手感段落；接管后的纯色场当下一段的舞台

**Why this shot earns its place.** 库里 wipe 类全是连续扫过——边界匀速或缓动地推过去。本卡反着来： **全程零插值零缓动**，色块像老式像素游戏的方块生长，每一跳都是硬切， 跳与跳之间完全静止。顿挫本身就是节奏：3–5 声"咔、咔、咔"比一次 平滑扫过更有宣告感。变体 B 再加一层：色块推进时携带一张内容卡同拍 离散跳位——卡不做补间，读作"整块被搬进来"，色块是运货的不是装饰的。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 步数 | A 4–5 跳 / B 3 跳 | ≥7 跳读作低帧率滚动而非阶跃；2 跳读作闪切 |
| 跳位间隔 | 6–12f | <5f 眼睛跟不上"跳了几步"；>16f 中段静止读作卡死 |
| 徽章过冲 | 0.55→1.12→1 三档硬跳 | 改成连续 spring 破语法；过冲档 >1.2 读作弹跳动画 |
| 携带卡 | 与色块同拍跳位，rotate -4° 定角 | 卡若做补间滑动，"整块搬运"手感全失；逐跳换角度读作抖动 |
| 斜角 clip | polygon 直角三角形从角落长出 | 边缘加圆角/羽化即破"硬边"人设 |
| 接管 hold | 铺满后 ≥30f 纯色静置再进下段内容 | 刚铺满就上内容，"吞屏"这一拍没呼吸完 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 与 wipe-transitions 分工：clock-wipe/blinds 是连续几何边界扫过（顺滑系），
- 与 shot-transitions 的关系：本卡是"转场+接管"复合体（色块留下当新场底色），
- **声音强依赖**：每跳一声打点（同 cel-flash-stomp 的 kick 逻辑）——
- 阶跃的"故意感"靠对比成立：同段落其他元素须是顺滑补间，全片到处阶跃
- 实战品牌色：色块用品牌主色，A/B 两式同片可各一次但换色（demo 蓝/红）；

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/transition/color-block-step-wipe/ColorBlockStepWipe.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
