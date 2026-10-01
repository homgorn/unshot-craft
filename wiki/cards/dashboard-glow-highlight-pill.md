# dashboard-glow-highlight-pill

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/dashboard-glow-highlight-pill`.

## Identity

- **slug**: `dashboard-glow-highlight-pill` (join key across cards, demos, media and deep links)
- **category**: `effects` — Light & Emphasis / 光效与强调
- **energy**: `高` — rank 6/8
- **suggested duration**: 约2.0s（60f@30fps） → **60 frames @30fps = 2.0s**
- **cross-category tags**: `effects`
- **upstream source**: references/shots/effects/dashboard-glow-highlight-pill.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `dashboard-glow-highlight-pill` | 60f | A | `demos/effects/dashboard-glow-highlight-pill/DashboardGlowHighlightPill.tsx` |

## What it does

金字悬于黑场，数据仪表盘自底带透视升入并持续 3D 漂移；金色光斑从右侧巡游到底部拉成胶囊，再由它起笔描出弹窗的辉光轮廓

**When to use it.** 金融/数据类产品的重功能揭示；"注意这里"的高级指引；黑金调品牌片的核心一拍

**Why this shot earns its place.** 用一束光把观众的注意力从"整个仪表盘"收到"这一个弹窗"上。光斑先在 面板间巡游（宣布有东西要来），拉成胶囊（蓄力），再从胶囊落点起笔 描出弹窗轮廓（交棒）——三段是同一束光的连续变形，任何一处断开就 变成三个不相干的动画。全片仅 2s，每段都靠上一段的落点做起点。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 金字淡出 | 满亮到 t≈0.30，0.30→0.355 inQuad | 要和仪表盘升入叠着走；先清场再升入就断了 |
| 仪表盘升入 | rotateX 34°→5.5°、scale 1.62→1.055，t 0.300→0.365 | 0.065（≈4f）内摆正是故意的：慢了读作"面板飘上来"而非"镜头压下去" |
| 常驻 3D 漂移 | yaw −13°→+2.6°，scale 0.943→0.707 | 漂移不能停：一静止就露出这是张贴图 |
| 光斑巡游 | 6 帧关键帧，22×22 → 96×16 | 单调向左下 + 只拉长不回摆；回摆一次就读作"光在找东西" |
| 背景虚化 | blur 峰值 4.5px，0.80→0.93 退掉 52%，dim 0.22 | 只起不退 = 结尾整幅糊；退到 0 又失去弹窗的层次 |
| 描边 draw-on | dashoffset 0.655→0.775 outQuad，从底边起笔逆时针 | outQuad 快起步才接得住胶囊的"甩出去"的势 |
| 描边收敛 | 0.79→0.93：2.9→1.0px、#fff0c4→#e6c887 | 收敛是"光变成 UI"的语义；不收敛就一直是特效 |
| 弹窗淡入 | 底板 0.665→0.75（上限 0.72 透明度）、文字 0.715→0.84 | 底板先于文字，才有"框先在、内容后填"的顺序 |

## Known pitfalls

- **描边 SVG 与弹窗必须共用同一个盒子和 1:1 px 的 viewBox**。曾用
- 光斑不能用 `mix-blend-mode:screen`：root 上有 `perspective` 会把混合
- 描边起笔点 `SX` 必须由光斑末帧 x 反算。写死坐标后一改巡游路径，
- 金字用 `background-clip:text`，辉光只能走 `filter: drop-shadow`——
- 仪表盘的订单簿/K 线/买卖面板与弹窗文案全是占位数据（确定性随机

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/effects/dashboard-glow-highlight-pill/DashboardGlowHighlightPill.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
