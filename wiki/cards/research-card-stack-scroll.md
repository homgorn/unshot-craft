# research-card-stack-scroll

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/research-card-stack-scroll`.

## Identity

- **slug**: `research-card-stack-scroll` (join key across cards, demos, media and deep links)
- **category**: `ui-entrance` — UI Entrance & Showcase / 界面登场与陈列
- **energy**: `中高` — rank 5/8
- **suggested duration**: 约 4.8s（144f@30fps） → **144 frames @30fps = 4.8s**
- **cross-category tags**: `ui-entrance`
- **upstream source**: references/shots/ui-entrance/research-card-stack-scroll.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `research-card-stack-scroll` | 144f | A | `demos/ui-entrance/research-card-stack-scroll/ResearchCardStackScroll.tsx` |

## What it does

深色论文卡每 12 帧一张沿右下轴线飞入中心叠压，落位带 1 帧压缩，只有最上一张全清晰渲染标题+作者+摘要，下方卡按堆积深度递增模糊变暗只露标题条，背景横向 grid 同步下移做速度参照

**When to use it.** "读了大量资料/处理了海量文档"的量级交代；研究类、检索类、批处理类产品的能力镜头

**Why this shot earns its place.** 要说的是"数量"，但一次给 13 张卡会读成一堵墙。改成流水线：卡一张一张进，每张都被 读过（最上一张永远是全文渲染的那张），读完就沉进堆里变模糊。观众感受到的是持续不断 的吞吐量，而不是一个静态的堆。背景 grid 同速下移是速度参照——没有它，堆积会读作 "卡在原地缩小"。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 节拍 | PER=12 帧/张，13 张 | 12f 是"紧但看得清"的下限；<8f 标题来不及读，>20f 量级感垮掉变成逐张展示 |
| 入场行程 | 6 帧（outCubic），提前量 -6 帧 | 行程只有节拍的一半 → 每张在下一张来之前已经落定；行程 ≥ PER 时会有两张同时在飞 |
| 入场位移/缩放 | `translateY(-40→0)`、`scale 0.94→1` | 40px 相对 96px 卡高是小幅——卡是"落进去"不是"飞进来"；缩放差只有 0.06，再大就读作弹窗 |
| 落位压缩 | 1.6 帧，y 轴 ×0.97 | 3% 是刚好能感知的量；>6% 或时长 >3f 会看出橡皮变形 |
| 堆积轴线 | 每节拍 y+30px、x+9px | 9/30 的比值决定轴线斜度；x 归零会变成正下方同心叠压，厚度感消失 |
| 深度衰减 | `depth = drift/90`，blur 0→4px、brightness 1→0.75 | 90px（3 个节拍）内衰减完 → 画面里始终只有约 3 张是"半清晰"的；衰减距离拉长会让下方糊卡堆太厚，画面变脏 |
| 回收窗 | `drift > 96px` 起淡出，48px 内到 0 | 回收太早会看到卡在画面中央消失；太晚 13 张全在场，DOM 与 blur 开销都上去 |
| 内容坐标系 | 逻辑 420×250，整体 `scale(min(W/420, H/250))` | 所有像素值写在逻辑坐标系里，改画布尺寸不用重排；卡 296×96、字号 9.5px 都是逻辑值 |

## Known pitfalls

- 卡数与节拍是绑定的：`13 张 × 12 帧 = 156 帧 > F=144`，末两张在 t=1 时仍在入场途中，
- `focus = floor(f/12)` 会超出卡数上界（f=144 时 focus=12，正好是最后一张）——加卡数
- 全部时间常量都写死在 144 帧的假设上（`F=144`, `fr=f/F`）。改时长必须同时改 F，
- 标题是 13 条真实感的论文标题占位、`preprint:24xx` 编号由索引生成，落地要换成项目
- 深色卡（`INK` 底 + `#2A2A2A` 描边）压在 `#FAFAFA` 浅底上是这套对比度的前提；卡色

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/ui-entrance/research-card-stack-scroll/ResearchCardStackScroll.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
