# mosaic-reframe

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/mosaic-reframe`.

## Identity

- **slug**: `mosaic-reframe` (join key across cards, demos, media and deep links)
- **category**: `transition` — Transitions / 转场
- **energy**: `中` — rank 4/8
- **suggested duration**: 约 6.0s（180f@30fps；浮现 0–0.6s · A→B 1.6–2.5s · hold · B→C 3.7–4.8s） → **180 frames @30fps = 6.0s**
- **cross-category tags**: `transition`
- **upstream source**: references/shots/transition/mosaic-reframe.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `mosaic-reframe` | 180f | A | `demos/transition/mosaic-reframe/MosaicReframe.tsx` |

## What it does

12 张瓦片在规则网格、feature mosaic、对角瀑布串三种排版间连续变形，位置宽高各自插值、逐片微错峰，段间留 hold

**When to use it.** "同一批内容多种看法"的陈列转场：作品集/模板库/相册产品的布局能力展示

**Why this shot earns its place.** 让观众看见"布局本身在思考"：同样 12 张内容，从整齐档案态（网格）变成有主次的策展态（feature mosaic），再变成有态度的动态态（对角瀑布）。三段排版是三种叙事语气，变形过程即产品能力。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 段窗口 | 每段变形 0.16–0.18，hold ≥0.2 | hold 是读版面的呼吸位，压缩到 <0.1 三段糊成一段 |
| 微 stagger | 0.007/片（≈2 帧） | 0 = 整版机械闪变；>0.02 波浪太明显抢过版面本身 |
| 瀑布参数 | 间距 6.4/7.6%，rot −15°+3°/片 | 旋转递增是"串"的灵魂；等角会退化成斜排网格 |
| mosaic 大位 | 首片 3×2 单元格 | 换 slots 表可重排主次；保证有一块 ≥2×2 的锚点位 |
| 浮现节奏 | 0.012/片 + 0.14 时长 | 12 片合计约 0.27 进完；作转场用时可砍掉浮现直接从 A 态起 |
| 瓦片内容 | 渐变底 + 圆点 + 双信息条（占位） | 换真实截图/图片时保留 overflow:hidden 圆角容器，宽高插值不裁坏内容 |

## Known pitfalls

- 五通道独立插值意味着**不能**换成 `transform: scale`——宽高动画会引发子元素重排，占位内容用了百分比定位可自适应，换成真实图片要用 `object-fit: cover`
- C 段瓦片有意越出画框（y 从 −7% 到 91%），画框裁切是构图的一部分，别加 padding "修复"
- 三套坐标表都以 92% 内容区 + 4% 边距为基准，改画幅比例需整表重算
- 段窗口与 stagger 叠加后末片 B→C 到 0.887 才结束，再加段落需压缩前段而不是顺延（保证 t=1 前全部落定）

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/transition/mosaic-reframe/MosaicReframe.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
