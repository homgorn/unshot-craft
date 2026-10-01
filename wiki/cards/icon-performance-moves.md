# icon-performance-moves

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/icon-performance-moves`.

## Identity

- **slug**: `icon-performance-moves` (join key across cards, demos, media and deep links)
- **category**: `effects` — Light & Emphasis / 光效与强调
- **energy**: `A 高潮点缀 / B 蓄势引入` — arc or n/a, not sortable
- **suggested duration**: A 3–4s / B 4–5s → **120 frames @30fps = 4.0s**
- **cross-category tags**: `interaction`, `effects`
- **upstream source**: references/shots/effects/icon-performance-moves.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| B | `attention-bounce` | —f | B | `demos/effects/icon-performance-moves/AttentionBounce.tsx` |
| A | `pop-burst-confirm` | 120f | B | `demos/effects/icon-performance-moves/PopBurstConfirm.tsx` |

## What it does

图标表演两式——pop-burst-confirm 爆花确认（对勾蓄力弹大+炸粒子+扩散环）与 attention-bounce 求关注弹跳（图标连跳递增+落地压扁+镜头被吸引）

**When to use it.** 半屏级 icon 特写段落；A "完成/成功"的标点符号，B 新功能引出

**Why this shot earns its place.** 库内图标动画品类首批入库：icon 是镜头怼着拍的表演者，不是 UI 角落的 微交互。A 是确认时刻的三连爆——大对勾先缩 0.6x 蓄力 3f、弹 1.35x 过冲 落回，同帧中心射出 10 根短线粒子+一圈描边环从边缘扩到 2.5 倍直径淡出， "部署成功"不是画出来的是炸出来的；B 是 macOS Dock 语汇——app 图标 原地连跳 4 次一次比一次高（0.5→1.2 倍 icon 高），每次落地压扁 （宽 1.2x 高 0.8x）+溅尘点，跳最高那下镜头向它轻推 8%（被吸引）， 落定后弹开功能面板——把"用户注意力"剪进叙事。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| icon 尺寸 | 400–500px 高（半屏特写） | 角落小图标做表演没人看见——表演者必须占 C 位 |
| A 蓄力 | 缩 0.6x 停 3f | anticipation：无蓄力的弹出没有"爆"感 |
| A 粒子/环 | 10 根短线飞 40–60px + 环扩 2.5 倍 | 三件套同帧齐发是"爆花"成立条件 |
| B 递增弹跳 | 4 跳 0.5→1.2 倍 icon 高 | 等高连跳读作 loading；递增才是"越喊越大声" |
| B 落地挤压 | 宽 1.2x 高 0.8x（1–2f） | squash 缺席=没有重量 |
| B 镜头推近 | 峰值帧 8% | 镜头动作把"被吸引"的观众视角演出来 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 同批 bell-swing-alert（铃铛甩摆）淘汰无附言——挂点摆动型 icon
- A 与 particle-celebrate-hits 同属爆发点缀，同一段落二选一
- B 首版曾出画框（末跳最高点顶出），弹跳高度与画面上留白先算像素
- 声音：A 蓄力静默→爆发帧"pop"+粒子细响；B 每次落地一声"duk"

## Card structure

`intention` | `variants` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/effects/icon-performance-moves/AttentionBounce.tsx`
- `demos/effects/icon-performance-moves/PopBurstConfirm.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
