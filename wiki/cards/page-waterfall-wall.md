# page-waterfall-wall

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/page-waterfall-wall`.

## Identity

- **slug**: `page-waterfall-wall` (join key across cards, demos, media and deep links)
- **category**: `ui-entrance` — UI Entrance & Showcase / 界面登场与陈列
- **energy**: `中` — rank 4/8
- **suggested duration**: 4–6s（无限循环体，时长由段落需要裁） → **180 frames @30fps = 6.0s**
- **cross-category tags**: `ui-entrance`
- **upstream source**: references/shots/ui-entrance/page-waterfall-wall.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `page-waterfall-wall` | —f | B | `demos/ui-entrance/page-waterfall-wall/PageWaterfallWall.tsx` |
| — | `vertical-ticker` | —f | B | `demos/ui-entrance/page-waterfall-wall/VerticalTicker.tsx` |

## What it does

页面瀑布墙——真实页面截图切成 3–4 列在 3D 后仰墙面上差速反向无限滚动，视差 + 镜头缓推做"内容多到流不完"的一览

**When to use it.** "多页面/多功能/多模板"体量感段落；montage 中段铺陈或 intro 后的产品广度镜头

**Why this shot earns its place.** 流动式一览：让观众在几秒内"看到很多页面流过"，读感是体量而非细节。 与 outro-group-photo-launch 分工：那是**聚拢式**一览（元素飞来围住 字标定格合影，语义"属于同一产品"），本卡是**流动式**一览（内容持续 流过不定格，语义"还有很多没给你看完"）。与 odometer-digit-roll 分工： 那是有终值的机械滚轮（逐位停稳读数字），本卡无终值无限循环。 与 wall-reveal-moves 分工：那是整墙**入场动作**，本卡是墙的**持续状态**， 可用那卡入场后交棒本卡续流。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 列数 | 3（1080p）/ 4（超宽） | 2 列读不出"墙"，5 列单列过窄纹理糊 |
| loop 时长 | 相邻列差 ≥25%（12/9/14s） | 差速太小视差读不出；最快列 <7s 开始读作"刷屏" |
| 方向 | 中列反向（-1,1,-1 或交替） | 全同向=一张大图；反向列是"独立列"的最强证据 |
| 倾角/透视 | rotateX 20° / perspective 1000px | >25° 顶部行文字透视压糊（Q2）；<12° 读不出墙面后仰 |
| scale | 1.2 基础 + 缓推至 ~1.26 | 1.2 是补透视收缩的底值，低于它四角露底 |
| 遮罩高度 | 200px | 太矮行硬进硬出；太高可视区剩不下 2 行 |
| 循环周期 | -50% 位移必须恰等于单副本周期（内容高+n·gap） | lib 已用 marginBottom 保证；自写实现用 flex gap 会差 gap/2 跳帧 |

## Known pitfalls

- **参数借鉴自外部实现（remotion-3d-ticker），非实战定稿；
- 每列 items 总高必须 ≥ 视口有效高（否则同屏见同一切片两次，穿帮）；
- 本卡是氛围/铺陈镜头不是信息镜头：切片上文字只求"看得出是真页面"
- P4 去重：与 outro 合影同片共存没问题（一流动一聚拢），但全片 _(rules P4)_

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/ui-entrance/page-waterfall-wall/PageWaterfallWall.tsx`
- `demos/ui-entrance/page-waterfall-wall/VerticalTicker.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
