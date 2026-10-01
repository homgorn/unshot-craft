# brace-expand

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/brace-expand`.

## Identity

- **slug**: `brace-expand` (join key across cards, demos, media and deep links)
- **category**: `typography` — Typography & Title Cards / 文字与字卡
- **energy**: `中` — rank 4/8
- **suggested duration**: 约 3.8s（114f@30fps：7f 出现 → 弹开 → 落定后字距松弛 → hold） → **114 frames @30fps = 3.8s**
- **cross-category tags**: `typography`
- **upstream source**: references/shots/typography/brace-expand.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `brace-expand` | 114f | A | `demos/typography/brace-expand/BraceExpand.tsx` |

## What it does

一对花括号先小字号出现在正中，随即带过冲向左右滑到 ±148px 并放大到标题级，文字 clip 宽度严格绑括号间距、像被拉开幕布般揭示，落定后字距再细微松弛

**When to use it.** 开发者/技术产品的标题字卡；章节开场；需要"一个符号完成揭示"的极简一拍

**Why this shot earns its place.** 标题揭示的手法里，本卡最省：不做遮罩条、不做逐字、不做位移——只让 一对括号往两边走，文字被"括出来"。它天生带代码语感（`{}` 是花括号）， 所以在技术产品语境里读作"这就是内容本体"。命门是 clip 宽度**必须严格 绑括号位置**：一旦文字自己淡入或自己擦入，括号就退化成装饰，幕布感全失。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 括号出现 | `t >= 0.07`（≈7f）硬切 | 硬切是对的（符号"啪"地在那儿）；改淡入就少了 2 帧的"先看清括号"，弹开显得突然 |
| 弹开窗 | 0.13→0.34（≈24f），`E.outBack` | outBack 的过冲是全片唯一峰值；纯 outCubic 读作滑开，没有"撑"的力道；窗 <14f 看不清文字揭示 |
| 半距 | HALF = 148px | 决定标题可容纳的字数；文案变长必须同步加大，不然字被 clip 裁掉（clip 只裁不缩字） |
| 缩放 | `lerp(ex, 0.6, 1)`，括号 44px / 字 38px | 0.6 起点是"小字号"的量；起点 >0.85 就看不出放大，<0.4 括号一开始小得像标点 |
| clip 留位 | `x·2 - 34`px | 34 是括号笔画宽的经验值；不减则字压括号，减太多字被裁得早、露不全 |
| 字距松弛 | `1 → 2.6`px，窗 0.42→0.62 inOutQuad | 这一下是"落定后的呼吸"；>4px 标题散架，删了收尾略僵但不算错 |
| 布局 | 零尺寸 `root` + 三个绝对定位子元素 | 宽度全程变化，**必须绝对定位**；用 flex 会让括号随 clip 宽度被推着走（判例） |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- **文案长度必须与 HALF 匹配**：占位文案是 `Your title`（10 字符），
- clip 宽度是从 0 长起来的，所以文字**总是从中间往两边露**：文案的
- 括号与文字必须共用同一个 `sc`：分别写两条缩放曲线（哪怕数值相同）
- 过冲只此一次：全片其他运动都无过冲，这是把注意力压在"撑开"这一
- `overflow:hidden` 的 clip 高度写死 60px，字号大改时要同步——不然
- 声音：弹开那一下值得一记短促的机械/木质开合音，落定后无声；

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/typography/brace-expand/BraceExpand.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
