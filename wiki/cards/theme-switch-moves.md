# theme-switch-moves

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/theme-switch-moves`.

## Identity

- **slug**: `theme-switch-moves` (join key across cards, demos, media and deep links)
- **category**: `interaction` — Interaction & Feature Demo / 交互与功能演示
- **energy**: `A 中 / B 中高` — arc or n/a, not sortable
- **suggested duration**: A 3–4s / B 5–6s → **120 frames @30fps = 4.0s**
- **cross-category tags**: `interaction`
- **upstream source**: references/shots/interaction/theme-switch-moves.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| B | `palette-theme-ripple` | 95f | B | `demos/interaction/theme-switch-moves/PaletteThemeRipple.tsx` |
| A | `theme-sweep-toggle` | —f | B | `demos/interaction/theme-switch-moves/ThemeSweepToggle.tsx` |

## What it does

主题切换两式——theme-sweep 斜向扫场（边界扫过处就地换肤）与 palette-ripple 组合款（⌘K 面板收缩成点、涟漪从点荡开换肤）

**When to use it.** 深色模式/主题功能的叙事段落；同一 UI "在你眼前变色"而非切到新场景

**Why this shot earns its place.** 深浅模式切换的两种拍法。A（Notion/Figma/Linear 惯用）：15° 斜向 边界带亮线从左上扫到右下，边界经过处浅色**就地**变深色，同布局 双主题共存一瞬——观众看到的是"同一个 UI 换肤"，不是转场。 B（组合变异）：⌘K 面板输入 "dark" 回车，面板收缩成一个亮点， 深色涟漪**从该点**荡开扫过全 UI——"命令引发换肤"的因果链完整可读。 组合命门：涟漪圆心必须是面板收缩点、起始帧必须是收缩完成帧。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 深色版制作 | 对色板逐键手工映射（bg/card/border 各自定深色值） | 滤镜反转出来的深色是错的（图像/头像全反） |
| A 斜边超扫 | 底端超出 SLANT+40px | 不超扫右下角残留浅色三角 |
| A 坐实 | scale 0.995 幅度偏微妙（demo 自评） | 实战可加大到 0.985 |
| B 因果钉扎 | 高光核在收缩点挂 10f，涟漪圆心=该点坐标 | 圆心错位/错帧就断了"命令→换肤"因果（组合命门） |
| B 浅色层 | 扫场完成后条件卸载 | 真静止前提 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 两版布局必须逐像素一致——布局有出入就读作"切换到另一个页面"，
- 真实页面实战：深浅两版分别真实截图（Q1），不做滤镜假深色 _(rules Q1)_
- 一支片主题切换 ≤1 次：它是功能叙事不是转场，反复切读作演示事故
- 声音：A 扫场一声长 whoosh；B 回车一声确认 + 涟漪荡开接 whoosh

## Card structure

`intention` | `variants` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/interaction/theme-switch-moves/PaletteThemeRipple.tsx`
- `demos/interaction/theme-switch-moves/ThemeSweepToggle.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
