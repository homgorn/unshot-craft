# cloner-depth-echo

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/cloner-depth-echo`.

## Identity

- **slug**: `cloner-depth-echo` (join key across cards, demos, media and deep links)
- **category**: `ui-entrance` — UI Entrance & Showcase / 界面登场与陈列
- **energy**: `中` — rank 4/8
- **suggested duration**: 4–5s → **150 frames @30fps = 5.0s**
- **cross-category tags**: `ui-entrance`
- **upstream source**: references/shots/ui-entrance/cloner-depth-echo.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `cloner-depth-echo` | 10f | B | `demos/ui-entrance/cloner-depth-echo/ClonerDepthEcho.tsx` |

## What it does

克隆纵队——主卡瞬间"复印"出 7 个半透明分身沿斜向纵深排开成队，停一拍后全体加速吸回本体合一+弹跳

**When to use it.** "多副本/多租户/规模感/批量处理"卖点；一镜讲完"一个=很多"

**Why this shot earns its place.** Spline/C4D Cloner 语汇的 UI 翻译：一张主卡"啪"地复印出 7 个克隆体 沿 Z 轴向后等距排开（间隔 120px、透明度 100%→20% 递减），错峰弹出 成纵队；停 ~25f 让观众数得清"有很多个"；然后全体 ease-in 加速吸回 本体合一，合体瞬间本体弹 1.08x 收束。与 depth-layer-moves 视差 （不同内容分层）分工：这是**同一内容**的等距重影阵列，语义是规模 不是空间。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 斜向错位 | dx=64·idx / dy=−34·idx | **命门**：纯 translateZ 排开在正视角下克隆体全被本体挡住（不可感）；斜向错位让纵队肉眼可见 |
| 侧视角 | 整队 rotateY 16° | 8° 仍近正视，16° 纵队清晰 |
| 克隆数/间隔 | 7 个 / 120px | 少于 5 读不出"队"，多于 9 尾部糊成一团 |
| 透明衰减 | 100%→20% 线性 | 越远越淡=纵深证据；等透明读作贴纸阵 |
| 排开/吸回 | spring 错峰 1.6f/个；merge ease-in 10f 全体同步 | 排开要错峰（复印感），吸回要同步（收束感）——节奏不对称是设计 |
| 合体弹跳 | sin(spring×π) 单脉冲 1.08x | 吸回无弹跳读作淡出；弹跳=质量证据 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 克隆体必须从后往前渲染保证遮挡正确；透明度 ≤0.005 条件卸载
- 同批 3D 渠道另两条（厚板转台淘汰、走廊改改再看）——纯陈列型
- 声音：排开一串细"啪"错峰，吸回一声上扬 whoosh，合体一声实"咚"

## Card structure

`intention` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/ui-entrance/cloner-depth-echo/ClonerDepthEcho.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
