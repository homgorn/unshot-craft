# wipe-transitions

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/wipe-transitions`.

## Identity

- **slug**: `wipe-transitions` (join key across cards, demos, media and deep links)
- **category**: `transition` — Transitions / 转场
- **energy**: `中` — rank 4/8
- **suggested duration**: 单式 前态 ≥20f + 擦除 32–60f + 收尾 ≥40f，约 5s（150f） → **20 frames @30fps = 0.7s**
- **cross-category tags**: `transition`
- **upstream source**: references/shots/transition/wipe-transitions.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| B | `blinds-slice` | —f | B | `demos/transition/wipe-transitions/BlindsSlice.tsx` |
| A | `clock-wipe` | —f | B | `demos/transition/wipe-transitions/ClockWipe.tsx` |

## What it does

几何擦除转场两式——clock-wipe 时钟扫描（雷达指针扫一圈换页）与 blinds-slice 百叶窗切条（12 竖条错峰翻换成波）

**When to use it.** 新旧页都不动、一条几何边界扫过完成交接的通用转场；不依赖构图里有合适元素，哪儿都能用

**Why this shot earns its place.** 转场库已有三族：穿越系（钻进去）、藏切系（遮住切）、体块系（页面是 实体）。本卡是第四族**几何擦除系**——新旧页都不动，一条几何边界扫过 完成交接，擦除的形状即语义：A 圆扫是"仪表盘刷新了一屏数据"，B 条扫 是"百叶窗逐叶翻面换页"。与 shot-transitions F 元素遮罩擦除的区别： F 用页面内真实元素当遮罩（依赖构图），本卡是纯几何形——通用性即定位。 按语义选：数据刷新用 A，横向推进翻页用 B。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| A 扇形 | 中心屏心(960,540)、半径 1400 盖满四角，固定 73 顶点(SEGS=72) | 顶点数恒定且够密（40+）防锯齿跳变——命门 |
| A 扫速 | 30–90f 指针 0→360° 纯 linear，双向 clamp | 雷达要匀速；加缓动就不是雷达是钟摆 |
| A 亮线 | 四层 SVG line：26px 白 0.35 柔光 + 13px 白 0.60 + 9px 黑 0.55 暗描边 + 4px 白核 | 白底判例：纯提亮不可见，必须加暗描边；首渲 3px 白线太弱，加码 1.5x 才过 |
| B 波 | 20–52f：delay=列号×2f，每条 10f Easing.in(cubic) | 交接点恒为 x+160(1-p)，数学上无露底 |
| B 缝亮线 | 三层 SVG：16px 白 0.45 柔光 + 6px 黑 0.55 暗描边 + 3px 白核，进出各 2f 淡入淡出 | 同 A 白底判例 |
| 摘罩 | A 96f / B 52f 起条件卸载全部擦除结构，B 页直出 | opacity 0 不算摘，残留 clip-path 毁真静止 |
| 收尾 | A 54f / B 98f 真静止（≥40f） | R1 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 擦除边界必须带亮线/高光——无亮线的 wipe 读作 PPT 转场，命门； **[命门]**
- A 与 circle-match-iris 的区别：iris 是从锚点炸开的圆（半径在长），
- 几何擦除全片 ≤2 次，且 A/B 别同片连用（两次"边界扫过"读作模板感）
- 亮线淡出与摘罩必须同帧衔接（A 90–96f 淡出、96f 卸载），

## Card structure

`intention` | `variants` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/transition/wipe-transitions/BlindsSlice.tsx`
- `demos/transition/wipe-transitions/ClockWipe.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
