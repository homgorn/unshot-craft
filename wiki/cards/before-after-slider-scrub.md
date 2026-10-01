# before-after-slider-scrub

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/before-after-slider-scrub`.

## Identity

- **slug**: `before-after-slider-scrub` (join key across cards, demos, media and deep links)
- **category**: `data` — Data & Metrics / 数据与指标
- **energy**: `中` — rank 4/8
- **suggested duration**: 4–5s → **150 frames @30fps = 5.0s**
- **cross-category tags**: `data`, `interaction`
- **upstream source**: references/shots/data/before-after-slider-scrub.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `before-after-slider-scrub` | —f | B | `demos/data/before-after-slider-scrub/BeforeAfterSliderScrub.tsx` |

## What it does

前后对比拉杆——"处理前/后"两版叠放，分割杆先猛甩后慢扫，杆过处新版"显影"揭出

**When to use it.** AI 增强/优化/重构类功能的效果对比段落（"用前 vs 用后"一镜讲清）

**Why this shot earns its place.** AI 图像产品发布片的标准对比语法：同一画面"处理前"（低对比灰蒙） 与"处理后"（清晰版）叠放，带圆手柄的竖分割杆先从左端猛甩到 70% （overshoot 回弹）、停一拍，再以约 1/5 的速度慢扫回来让观众看清 差异——**快甩慢扫的速度对比就是节奏**：快甩宣告"变了"， 慢扫证明"变在哪"。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 速度比 | 快甩 12f vs 慢扫 48f，约 5:1 | 比例 <3:1 节奏对比不可感 |
| 揭示 | after 层 clip-path inset 右边界跟随杆 x | 杆和揭示边界错位即穿帮 |
| 手柄 | 圆形手柄 + 速度差分驱动 scaleX 微拉伸（峰值 1.18），静止自动归 1 | 拉伸给手柄"被甩"的重量感 |
| before 处理 | 低对比灰蒙版 | before 太难看是自黑，"差"要可信（真实旧版/未优化态） |
| 角标 | BEFORE/AFTER 角标放内容区 | demo 判例：初版压住侧栏/头像穿帮 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 两版必须同布局同机位——布局不同读作两个页面，对比失效
- 实战 before/after 都用真实截图（Q1）：before 是注入旧数据/关闭 _(rules Q1)_
- 慢扫终点停 40% 而非 0%——留一段 after 在画面上定格（结论可见）
- 声音：快甩一声 whoosh + 回弹轻 tick，慢扫无声或极轻摩擦音（S4） _(rules S4)_

## Card structure

`intention` | `phases` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/data/before-after-slider-scrub/BeforeAfterSliderScrub.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
