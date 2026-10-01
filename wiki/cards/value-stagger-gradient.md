# value-stagger-gradient

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/value-stagger-gradient`.

## Identity

- **slug**: `value-stagger-gradient` (join key across cards, demos, media and deep links)
- **category**: `ui-entrance` — UI Entrance & Showcase / 界面登场与陈列
- **energy**: `中高` — rank 5/8
- **suggested duration**: 约 5.0s（150f@30fps） → **150 frames @30fps = 5.0s**
- **cross-category tags**: `ui-entrance`
- **upstream source**: references/shots/ui-entrance/value-stagger-gradient.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `value-stagger-gradient` | 150f | A | `demos/ui-entrance/value-stagger-gradient/ValueStaggerGradient.tsx` |

## What it does

16 根柱入场时 delay 是时间错峰，同时高度/色相/位移/模糊四个属性各自铺成从首到末的数值梯度；第二拍把错峰原点换成中心，脉冲幅度以中心为最大重新铺开

**When to use it.** 技法演示与参数化能力的展示镜头；也可直接当数据/频谱/均衡器类界面的入场

**Why this shot earns its place.** stagger 通常只被用来错开时间。这张卡要说的是它还能错开**值**——同一个索引既决定 "什么时候动"，也决定"动到多少"。两拍是一组对照实验：第一拍原点在首位（梯度从左到 右单调铺开），第二拍原点换到中心（梯度以中轴对称铺开）。观众看到的不是两个动画， 而是同一个配方换了一个参数。屏幕上的代码字幕同步换成对应的 stagger 调用，明说这件事。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 柱数 | N=16（`left: 8+i*5.4%`，宽 3.4%） | 16 根让梯度有足够分档；<8 根梯度读作"每根都不一样"而非一道斜坡，>24 根柱间距要重算 |
| 时间错峰 | `d = i*0.02`（≈3f/根，总 0.3） | 3f 是连绵的铺开；>0.05 会变成逐根点名，梯度的"整体感"丢失 |
| 单柱行程 | 窗 0.22（≈33f，outCubic） | 行程是总错峰的 0.73 倍 → 大部分时间十来根同时在动；行程 < 错峰总量时变成一根接一根 |
| 高度梯度 | `stagger([92, 32])`px | 首末 2.9 倍差是明确斜坡；比值 <1.5 读不出梯度，>4 末端柱矮到看不见 |
| 色相梯度 | `stagger([200, 320])` | 120° 跨度（蓝→紫）；跨度 <40° 时色相白给，>200° 会绕回红色让斜坡读作环形 |
| 位移/模糊梯度 | `stagger([46,14])`px / `stagger([8,2])`px | 这两条是本卡的"值 stagger"主证据——把它们改成常量，动效立刻退化成普通的 stagger 入场 |
| 第二拍原点 | `from:'center'`，`distC*0.13` | 0.13 是从中心到端点的传播延迟（≈4f）；归零则整排同时脉冲，`from` 参数就没有意义了 |
| 脉冲幅度梯度 | `lerp(1-distC, 0.06, 0.42)` | 中心 42% / 端点 6% 是 7 倍差，波形明显；两端也给大幅度会读作整排一起鼓，中心原点看不出 |
| 亮度脉冲 | `brightness(1 + pulse*0.55)` | 55% 提亮让脉冲在暗底上可读；这一项没做梯度（全柱同幅），是有意的——太多梯度叠一起观众读不清哪个是主角 |

## Known pitfalls

- 第一拍与第二拍首尾相接：末柱入场结束于 `0.28+15*0.02 = 0.58`，而中心柱的脉冲在 0.56
- 端点柱的第二拍窗口是 `0.69→0.87`，之后到 t=1 有约 0.13（20f）的完全静止。这是给
- `distC` 的分母 `C=(N-1)/2` 在 N=1 时会除零；`staggerVal` 里已用 `n<=1 ? 0` 兜住，
- 柱位 `left: 8+i*5.4%` 与宽 `3.4%` 是为 N=16 手配的（末柱右缘 8+15*5.4+3.4 = 92.4%）。
- 字幕是 anime.js 的 API 调用字符串，本质是**技法说明**而不是内容。用在真实成片里
- 底部的 16 个小圆点（`bottom:17%`，opacity .35）是静态装饰，不参与任何动画；它们的
- 深底（`#0a0b10`）+ 高饱和柱（85%/66%）+ 12px 光晕是一套；浅色主题下光晕与

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/ui-entrance/value-stagger-gradient/ValueStaggerGradient.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
