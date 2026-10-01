# chart-live-moves

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/chart-live-moves`.

## Identity

- **slug**: `chart-live-moves` (join key across cards, demos, media and deep links)
- **category**: `data` — Data & Metrics / 数据与指标
- **energy**: `中高` — rank 5/8
- **suggested duration**: 各 4–6s → **180 frames @30fps = 6.0s**
- **cross-category tags**: `data`
- **upstream source**: references/shots/data/chart-live-moves.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `axis-rescale-shock-v2` | —f | B | `demos/data/chart-live-moves/AxisRescaleShockV2.tsx` |
| — | `oscilloscope-stream-v2` | 112f | B | `demos/data/chart-live-moves/OscilloscopeStreamV2.tsx` |
| — | `unit-dot-swarm-regroup-v2` | 20f | B | `demos/data/chart-live-moves/UnitDotSwarmRegroupV2.tsx` |

## What it does

活体图表三式——oscilloscope-stream 示波流线（曲线右端实时写入+突发尖峰）、unit-dot-swarm-regroup 点阵重组（点群三幕迁徙聚成数字）、axis-rescale-shock 轴爆表重标（新值冲出画框逼 y 轴重标）

**When to use it.** 数据叙事段落；分别讲"实时性"、"每个数字是一个人"、"增长装不下"

**Why this shot earns its place.** 图表不是插图是剧情。三式共同前提（实测判例）：**必须真图表语境** ——真轴标/真数据/真文案，灰阶占位条测不出数据叙事的表达力。 A 示波流线：曲线写入点钉在右端上下起伏，旧数据左流出画，中途一次 突发尖峰（振幅 2.2×、读数跳大变强调色）——"实时"不用说出口，还有事件； B 点阵重组：320 个点（每点≈40 customers）散布→聚三簇（浮 Free/Pro/ Enterprise 真标签）→列队成柱（真轴标）→聚成点阵大数字 "12,847"—— 同一批点，观众能跟着某一颗看它归队； C 轴爆表：折线正常爬升，新值顶破图表上沿冲出卡片 220px（强调色粗线 插进标题区），停半拍，y 轴"哗"地重标（旧刻度飞出/新刻度滑入/网格 加密/旧线压扁成地平线），新值落回+弹真值标签——用"坐标轴装不下"演增长。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 真语境 | 真标题/真轴标/真单位/真读数 | **入库前提**：灰阶版三条全数被裁，换真语境后全过 |
| 主角色 | 强调色（模板片为琥珀）标事件/主角（尖峰读数、Pro 簇、爆表段） | 全灰读不出"哪里是重点" |
| A 流速 | 8px/f | 5.5 已可感，8 更明确；波形纯函数禁随机 |
| B 点数/点径 | 320 / 9px | 点太少拼不出数字，太小看不见个体 |
| C 冲出幅度 | 卡顶外 220px | 80px 版不够"爆"；真的插进标题区才是事故感 |
| 收尾 | 三式都要 ≥36f 真静止 | 数据图表尾漂读作还没播完 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 三式是三种独立手法不是套餐——同片用两式以上时各 ≤1 次且错开段落
- A 的尖峰事件、C 的重标只能发生一次；重复即廉价
- B 终幕数字位图字形要预先手算（点数=位点数用满才整齐）
- 与 dataviz-landscape-open（抽象数据地景开场）分工：那是开场氛围，
- 声音：A 尖峰一声警示 tick；B 每幕迁徙一声 whoosh；C 冲出框

## Card structure

`intention` | `variants` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/data/chart-live-moves/AxisRescaleShockV2.tsx`
- `demos/data/chart-live-moves/OscilloscopeStreamV2.tsx`
- `demos/data/chart-live-moves/UnitDotSwarmRegroupV2.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
