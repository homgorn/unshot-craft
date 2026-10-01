# gauge-readout-moves

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/gauge-readout-moves`.

## Identity

- **slug**: `gauge-readout-moves` (join key across cards, demos, media and deep links)
- **category**: `data` — Data & Metrics / 数据与指标
- **energy**: `中高` — rank 5/8
- **suggested duration**: A 4–5s / B 4–5s → **150 frames @30fps = 5.0s**
- **cross-category tags**: `data`
- **upstream source**: references/shots/data/gauge-readout-moves.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| A | `needle-sweep-selftest` | —f | B | `demos/data/gauge-readout-moves/NeedleSweepSelftest.tsx` |
| B | `tape-scroll-fixed-pointer` | —f | B | `demos/data/gauge-readout-moves/TapeScrollFixedPointer.tsx` |

## What it does

仪表读数两式——needle-sweep-selftest 满弧扫针（点火自检指针甩满全弧再回落真值）与 tape-scroll-fixed-pointer 滚带定针（针不动刻度带滚过+冲刺刹车）

**When to use it.** dashboard 开场仪式/性能指标揭晓；A 多表盘开机感，B 单指标大跳变

**Why this shot earns its place.** 把"报数值"做成仪表的身体动作：A 是汽车点火自检——表盘指针先"唰"地 甩满全弧（270°）再回落定格真实值，多表错峰成波浪，先亮量程再报数， 开场宣誓感；B 是飞机空速带语法——指针/取景窗钉死画面正中，带刻度的 标尺整体从底下滚过，大数值跳变时刻度带 45px/f 冲刺、末尾 spring 刹车 带回摆过冲，"世界动、针不动"，数值大小变成看得见的位移距离。 与 odometer-digit-roll 分工：那是数字在窗里滚，B 是连刻度格线全在平移。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| A 甩弧幅度 | 满量程 270° | 只甩到真值=没有自检仪式感；满弧再回落才是"先亮量程" |
| A 过冲 | 回落带 5–8° 回摆 | 无过冲读作电子表；过冲=机械指针的质量 |
| A 错峰 | 3–5f/表 | 齐甩读作复制粘贴；错峰成波浪 |
| B 冲刺速度 | 45px/f（大跳变段） | 慢了读作匀速爬升，"世界动"不成立 |
| B 刹车 | spring 过冲（冲过头再弹回停位） | 词汇原案的回摆是"哐"的来源，直停可惜 |
| 真静止 | 停位后 ≥30f 全锁死 | 指针类最忌尾漂 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 同批 ring-close-overfill（合环过盈）改改再看无附言——环形进度类
- A 的表盘是自绘 SVG（弧刻度+指针），实战贴真 dashboard 时优先找
- 声音：A 甩针一声"唰"+落定"嗒"（多表错峰各一声）；B 冲刺段

## Card structure

`intention` | `variants` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/data/gauge-readout-moves/NeedleSweepSelftest.tsx`
- `demos/data/gauge-readout-moves/TapeScrollFixedPointer.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
