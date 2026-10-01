# draw-svg-trace

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/draw-svg-trace`.

## Identity

- **slug**: `draw-svg-trace` (join key across cards, demos, media and deep links)
- **category**: `ui-entrance` — UI Entrance & Showcase / 界面登场与陈列
- **energy**: `中` — rank 4/8
- **suggested duration**: 描边 40f + 闪黑交棒 16f + hold ≥35f，约 3–4s → **40 frames @30fps = 1.3s**
- **cross-category tags**: `typography`, `ui-entrance`
- **upstream source**: references/shots/ui-entrance/draw-svg-trace.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `draw-svg-trace` | —f | B | `demos/ui-entrance/draw-svg-trace/DrawSvgTrace.tsx` |

## What it does

描边生长圈注——一条带笔头的墨线沿元素轮廓跑一圈把它"画"出来，闭合瞬间闪黑交棒、内容淡入；同套路可给标题画下划线

**When to use it.** 单个卡片/图表/标题的被点名入场；元素级手法（整页级蓝图描线归 wall-reveal-moves C 式）

**Why this shot earns its place.** "画出来"是纸墨审美里最顺手的入场隐喻：元素不是飞进来也不是淡进来， 而是被一支看不见的笔当场描出来。库内 wall-reveal-moves C 式已有整页 蓝图版（全屏线框逐段画+区域点亮），本卡是它的**元素级特写版**—— 一条线、一个主体、一次闭合，笔头可见、方向可读，适合"接下来讲它" 的点名时刻。第二用法是标题下划线生长：同一套路 18f 短版，给重点词 一笔手绘强调，与马克笔审美 token 天然同族。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 描边速度 | 一整圈 40f（inOut cubic 起收有呼吸） | <28f 读不出"在画"，>60f 读作加载中 |
| 笔头 | 7px、dash 长 0.045 | 笔头≤主线粗细就消失在主线里 |
| 闭合闪 | 2f 冲黑+加粗，6f 回落 | 没有这一下，"画完"没有句号 |
| 下划线版 | 18f out cubic 单向生长，画完常驻 | 用在单个重点词；一屏 ≥2 条读作装饰线 |
| 收尾 | 交棒完成真静止 ≥35f | R1 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 与 wall-reveal-moves C 式（整页蓝图描线）同族互斥：同片二选一，
- 描边路径必须与元素真实轮廓吻合（圆角 rx 一致）——线画的是 14px
- 真实素材上内容淡入别抢在闭合前：线还没画完内容先出来，"画"的
- 一次点名画一个主体；同屏多元素排队各画一圈读作加载动画

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/ui-entrance/draw-svg-trace/DrawSvgTrace.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
