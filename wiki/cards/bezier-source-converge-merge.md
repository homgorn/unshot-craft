# bezier-source-converge-merge

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/bezier-source-converge-merge`.

## Identity

- **slug**: `bezier-source-converge-merge` (join key across cards, demos, media and deep links)
- **category**: `ui-entrance` — UI Entrance & Showcase / 界面登场与陈列
- **energy**: `中` — rank 4/8
- **suggested duration**: 约 5.6s（168f@30fps） → **168 frames @30fps = 5.6s**
- **cross-category tags**: `ui-entrance`
- **upstream source**: references/shots/ui-entrance/bezier-source-converge-merge.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `bezier-source-converge-merge` | 168f | A | `demos/ui-entrance/bezier-source-converge-merge/BezierSourceConvergeMerge.tsx` |

## What it does

左侧四个来源节点各有一条细贝塞尔曲线连向右侧同一汇聚点，曲线先错峰由左向右 draw-on，节点沿自己的曲线滑向汇聚点并三段式加速缩小到消失，强调色数据包全程沿路径滑行，吞并完成后曲线从左端反向擦除只留圆形徽标

**When to use it.** "多源整合/统一接入/数据汇聚"的核心机制镜头；集成、聚合、单一入口类产品的说明段落

**Why this shot earns its place.** "我们把四个来源统一了"是一句抽象话。这个动效把它变成可看的物理过程：先建立四条独立 的通路（draw-on 是"连上了"），再让四个来源真的顺着通路走进同一个点并被吸进去（缩小 到 0 是"被吞并"），最后擦掉通路只留徽标（"现在只有一个"）。三段叙事各自有明确的 起止，观众不需要旁白就能读出因果。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 来源数 | 4 条（y=36/92/148/204，间距 56） | 4 条是曲率差异明显又不打结的甜点；>6 条中间几条的贝塞尔几乎重合，汇入角读不出区别 |
| draw-on | 起点 `0.04+i*0.045`，窗 0.17，outQuad | 0.045 的错峰约 7f；归零会读作四条线一起刷出，失去"逐路接通"的语义 |
| 汇聚窗 | 0.34→0.74（inOutCubic） | 占全片 40%，是主段落；inOut 的缓起是"启动"、缓收是"到位"，换 linear 立刻变成匀速传送带 |
| 三段缩小 | 44→15px（前 75%）→ 0（后 25%） | 拐点 0.75 越靠后吸入越突然；把它挪到 0.5 会变成"一路缩小"，吞并的那一下就没了 |
| 数据包周期 | 2 个整数周期（0.1→0.74 线性） | 必须是整数周期，否则末帧包停在半路；周期加密到 4 会读作数据流很急，也更容易和节点重叠 |
| 包相位偏移 | `i*0.13` | 错开四路的包，避免它们排成一行同时汇入；0 会看到四个包整齐并进，像一次发车 |
| 擦除 | 0.78→0.9，dashoffset 取负 | 12f 完成；擦除必须在节点全部消失（conv=0.74 结束、节点 0.92 前淡完）之后，否则线先没了节点悬在空中 |
| 徽标脉冲 | outBack +12%（0.7→0.78）→ 回落（0.78→0.86） | 12% 是"接收到了"的量级；>25% 会抢过汇聚本身的注意力 |

## Known pitfalls

- `getTotalLength` / `getPointAtLength` 必须在 SVG 已挂到文档且完成布局之后才有效，
- `f0` 是用 40 步线性扫描找出的"x 首次 ≥74"的比例，精度只有 1/40。曲线形状改动大时
- 节点 opacity 在 `conv > 0.92` 后才开始淡出，而 conv 在 t=0.74 就到 1，所以节点是在
- 节点是 `S1`–`S4` 的中性灰阶占位圆（灰度分层仅用于区分四路），落地要换成真实来源 _(rules S1,S4)_
- 汇聚点 (332,120) 与 SVG 视口 440×240、`overflow:visible` 是绑定的一组坐标。改画布
- 字幕 "Four sources unified" 是占位文案，出现在 0.84 之后——如果要配旁白，这句的

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/ui-entrance/bezier-source-converge-merge/BezierSourceConvergeMerge.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
