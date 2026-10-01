# card-stack

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/card-stack`.

## Identity

- **slug**: `card-stack` (join key across cards, demos, media and deep links)
- **category**: `ui-entrance` — UI Entrance & Showcase / 界面登场与陈列
- **energy**: `中高` — rank 5/8
- **suggested duration**: 约 4.2s（126f@30fps） → **126 frames @30fps = 4.2s**
- **cross-category tags**: `ui-entrance`
- **upstream source**: references/shots/ui-entrance/card-stack.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `card-stack` | 126f | A | `demos/ui-entrance/card-stack/CardStack.tsx` |

## What it does

8 张卡从屏幕下方逐张 spring 弹入叠成一摞，全员落位后整摞一次性展成 3D 扇面——每张按序号偏转 8°、横移 34px、向后退一层 z

**When to use it.** 需要交代"我们有一组东西"的产品段落；卡片墙/模板库/方案列表的建立镜头，也能当 logo 前的一拍蓄势

**Why this shot earns its place.** 一摞卡先聚成一个物体，再摊开成一组物体——顺序很关键：先给"整体"再给"个体"。 观众第一眼记住的是有分量的一摞（数量感），第二眼才看清每张不一样（多样性）。 展开动作留到最后一次性完成，是为了不和入场的节拍打架。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 卡数 | N=8（hue 222→334，每张 +16°） | 8 张是扇面 56° 总张角的舒适上限；>10 张要把每张角度降到 5–6°，否则两端卡飞出画框 |
| 入场 stagger | 0.033/张（≈4f） | 4f 是"一串"的手感；≥8f 读作逐张点名，≤2f 读作一团一起冒 |
| 入场行程 | 窗 0.3（≈38f），y 300→0 | 300px 保证起点在画框外；行程缩到 0.15 以内 spring 的回弹会被截断，落位变硬 |
| spring 阻尼 | `E.spring(inT, 0.3)` | 0.3 是可见但不夸张的一次回弹；调小回弹次数增多，卡会"抖两下"，成组时抖动会互相干扰 |
| 展开窗 | 0.55→0.8（inOutCubic） | inOut 让展开缓起缓收像一只手在摊牌；换 outBack 会过冲成"甩开"，与前段的 spring 撞手感 |
| 扇形张角 | `k*8°`，横移 `k*34px` | 角度与横移要同比调：只加角度不加横移，卡会互相穿插；34/8 的比值决定扇面是"疏"还是"叠" |
| 深度递退 | `tz = -10* | k |
| 旋转轴 | `transform-origin: 50% 130%` | 130% 决定"扇柄"离卡多远；改成 50% 50% 立刻退化成风车式散开，失去手持感 |

## Known pitfalls

- 两段时间窗刚好首尾相接：末张入场结束于 `0.02+7*0.033+0.3 = 0.551`，展开始于 0.55。
- 卡数为偶数时 `k` 取半整数（±0.5, ±1.5…），`zIndex = 20-|k*2|` 让中间两张同层，
- 卡片尺寸 110×150 与 `margin:-85px 0 0 -55px` 是绑定的居中量，改尺寸要一起改 margin
- 卡面内容是灰阶骨架条 + 单个几何字符的占位，落地必须换成真实页面切片；hue 色环是
- 展开后没有收尾动作，末帧停在扇面终态。要接下一镜就在 0.8 之后切，别让扇面白停太久

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/ui-entrance/card-stack/CardStack.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
