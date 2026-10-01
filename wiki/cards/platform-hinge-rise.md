# platform-hinge-rise

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/platform-hinge-rise`.

## Identity

- **slug**: `platform-hinge-rise` (join key across cards, demos, media and deep links)
- **category**: `ui-entrance` — UI Entrance & Showcase / 界面登场与陈列
- **energy**: `中` — rank 4/8
- **suggested duration**: 约 3.5s（104f@30fps；结论落定后保留 30f 静止） → **104 frames @30fps = 3.5s**
- **cross-category tags**: `opening`, `ui-entrance`
- **upstream source**: references/shots/ui-entrance/platform-hinge-rise.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `platform-hinge-rise` | 104f | A | `demos/ui-entrance/platform-hinge-rise/PlatformHingeRise.tsx` |

## What it does

承托平台先横向建立，两块主体从相邻底部铰点反向翻起并做一次克制阻尼回摆，最后结论台从画外升入，形成“舞台→证据→结论”的三段式揭示

**When to use it.** 两个主体/方案/品牌并列登场；建筑、设备、卡片从基座后升起；需要在一个固定机位里完成“先摆证据再下结论”的解释镜头

**Why this shot earns its place.** 先让平台成为可信的“承托关系”，再让两个主体从平台后方翻起，观众会自然把它们 理解为同组证据；最后从下方升起的结论台不是第三个平级元素，而是对前两者的归纳。 固定机位和明确的遮挡顺序让这张卡适合解释性 B-roll，也能换成产品卡、人物、建筑或 对比方案。核心不是“东西从下方出现”，而是**两个相邻铰点产生方向相反的展开力**。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 平台建立 | f0–15，scaleX .012→1 | 少于 10f 像硬切，多于 22f 会拖慢主体登场 |
| 语境圆 | f12–32，scale .88→1，rise 18px | 背景必须先于主体可辨认，但不能先完成太久 |
| 双主体翻起 | f14–30；左 rise 112px/-18°，右 rise 90px/+18° | **命门**：两块必须从相邻铰点反向展开；同向旋转会失去“打开舞台”的力学关系 |
| 阻尼回摆 | 16f；左 1.5°，右 1.2°，右延迟 1f | 只允许一次可感回摆；振幅 >2° 会像卡片玩具 |
| 结论台 | f52–74，rise 96px | 与主体落定至少隔 6f，避免证据和结论同时抢读 |
| 收尾 hold | 30f | 结论文字若超过 8 个汉字，继续延长总时长，不要压缩升台动作 |

## Known pitfalls

- 主体必须被平台上缘或独立遮罩裁住底部；没有遮挡会暴露它们从画外平移而非从平台后翻起
- `transform-origin` 不能放在各自主体中心：中心旋转读作两张卡在晃，只有相邻底部铰点才读作展开
- 左右块不要做成完全同尺寸、同高度、同振幅；轻微不对称是让双主体保持可辨认轮廓的关键
- 结论台是总结层，视觉对比应低于两个主体；若给它更深颜色或更大过冲，会反客为主
- demo 只含原创通用 DOM 形状和占位文字，不依赖复刻研究里的品牌、建筑或视频素材

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/ui-entrance/platform-hinge-rise/PlatformHingeRise.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
