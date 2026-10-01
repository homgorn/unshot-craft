# card-flip-reveal

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/card-flip-reveal`.

## Identity

- **slug**: `card-flip-reveal` (join key across cards, demos, media and deep links)
- **category**: `transition` — Transitions / 转场
- **energy**: `中高` — rank 5/8
- **suggested duration**: 单卡翻转 26f，三卡错峰 10f，全程 ~4.9s（含 hold） → **26 frames @30fps = 0.9s**
- **cross-category tags**: `data`, `transition`
- **upstream source**: references/shots/transition/card-flip-reveal.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `card-flip-reveal` | 18f | B | `demos/transition/card-flip-reveal/CardFlipReveal.tsx` |

## What it does

功能卡 3D 翻面揭示——卡片沿 Y 轴翻 180°，正面 UI 翻到侧棱最薄处闪过一道随角度移动的高光带，背面揭出大号结论数字，逐张错峰扫过整排

**When to use it.** "功能→成果"的成对叙事：一排功能卡逐张翻出各自的指标/结论；元素级转场卡

**Why this shot earns its place.** 库内"翻"字辈已有 wall-reveal-moves B（整墙波浪翻面，讲入场）和 split-flap（字符翻牌，讲文字）。本卡是**语义翻面**：一张卡的正反两面 是一对因果——正面是功能界面，背面是它带来的数字结论。翻面动作本身 就是"所以呢？"的回答，Apple bento 段落的标准语法。逐张错峰 10f 扫过 一排，三张卡三个数字节奏读作"成果连报"。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 翻转时长 | 18f + 8f 回弹 | <14f 看不到侧棱瞬间；>28f 读作慢慢转 |
| 过冲 | 192°→180°（12°） | 无过冲落定读作生硬停表 |
| 高光峰值 | 0.32 加深灰 @90° | 峰值错开 90° 读作贴图错误 |
| 错峰 | 10f/卡，≤4 卡 | 同时翻读作整墙翻面（那是 wall-reveal B 的活） |
| 背面内容 | 大号数字（90px 级）+ 一行小标签 | 背面塞完整 UI 读不完——翻面后只有一拍注意力 |
| 收尾 | 末卡落定真静止 ≥40f | R1 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 与 wall-reveal-moves B 式（网格波浪翻面）同技术根不同语义：那是
- 正反两面必须语义成对（界面→它的成果）；翻出无关内容，翻面就
- 真实素材正面用截图时注意 backface 渲染开销，三卡以上分 Sequence
- 声音候选位：每卡翻停帧一声轻"啪"（sound-design §4.5），三连啪

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/transition/card-flip-reveal/CardFlipReveal.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
