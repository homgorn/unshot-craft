# hatch-depth

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/hatch-depth`.

## Identity

- **slug**: `hatch-depth` (join key across cards, demos, media and deep links)
- **category**: `data` — Data & Metrics / 数据与指标
- **energy**: `中` — rank 4/8
- **suggested duration**: 约 4.4s（132f@30fps；生长 0–1.7s · 蜕变 2.2–3.4s · 微颤收尾） → **132 frames @30fps = 4.4s**
- **cross-category tags**: `data`
- **upstream source**: references/shots/data/hatch-depth.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `hatch-depth` | 132f | A | `demos/data/hatch-depth/HatchDepth.tsx` |

## What it does

斜纹占位条逐条 wipe 伸长后，斜纹淡出、强调色实心层淡入并弹出数值，占位图蜕变为真数据条形图

**When to use it.** "从草稿到真实数据"的叙事拍；dashboard/报表功能引入，或强调数据实时性的段落

**Why this shot earns its place.** 把"占位符变成真数据"这个产品瞬间拍成看得见的材质转换：先用 45° 斜纹条画出"这里将有数据"的草稿感，再让实心色层原位替换——几何完全不动、只换皮肤，观众读到的是"同一样东西活了"。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 错峰间隔 | 生长 0.05/条、蜕变 0.03/条 | 生长间隔可到 0.08 增强"逐条点亮"；蜕变间隔别超 0.05，拖长会读作故障闪烁 |
| 生长时长 | 0.22（outCubic） | 缩到 0.15 更利落；配合错峰保证末条 ≤0.5 长完，给蜕变留窗口 |
| 蜕变窗口 | 0.5 起、每条 0.14 交叉淡化 | 这是卡点位——BGM 重音应压在首条蜕变（t=0.5）上 |
| 柱宽数据 | [0.85, 0.55, 0.95, 0.4, 0.7] | 换成真实数据比例即可；最长条 ≥0.9 保证画面有满幅锚点 |
| 微颤幅度 | ±2%，t=0.7–0.85 | >4% 读作抖动 bug；不想要"呼吸感"可归零，但收尾会偏死板 |
| 强调色 | `ACCENT='#5B8DEF'` / `ACCENT_HI='#8FB2F7'` | 双常量整体换肤；HI 用于数值文字，保持同族但更亮 |

## Known pitfalls

- 斜纹层和实心层宽度必须共用同一条 `grow` 曲线——分开算会在蜕变瞬间产生 1–2px 宽度跳变，"原位换皮"的错觉立刻穿帮
- 标签（SERIES_A 等）是占位词，换项目真实指标名时注意 70px 定宽标签列，超长会被裁
- 数值 `w*420` 是演示映射，接真数据时换成实际数值格式化函数，但保持"随 grow 滚动"（终值 ×grow）的读数感
- 微颤用全局 t 驱动（`sin(t*30)`），改动画总时长 dur 会改变颤动频率，需重新目检

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/data/hatch-depth/HatchDepth.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
