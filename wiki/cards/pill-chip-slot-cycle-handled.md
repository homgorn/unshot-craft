# pill-chip-slot-cycle-handled

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/pill-chip-slot-cycle-handled`.

## Identity

- **slug**: `pill-chip-slot-cycle-handled` (join key across cards, demos, media and deep links)
- **category**: `typography` — Typography & Title Cards / 文字与字卡
- **energy**: `中` — rank 4/8
- **suggested duration**: 约 5.0s（150f@30fps：静置 → 3 次切换（0.25/0.47/0.69）→ 尾部静置） → **150 frames @30fps = 5.0s**
- **cross-category tags**: `typography`
- **upstream source**: references/shots/typography/pill-chip-slot-cycle-handled.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `pill-chip-slot-cycle-handled` | 150f | A | `demos/typography/pill-chip-slot-cycle-handled/PillChipSlotCycleHandled.tsx` |

## What it does

白底句式 "Your `chip` Handled" 里深色胶囊内词竖向滚轮轮换，胶囊宽度按预量文本宽插值平滑伸缩、两侧文字被自然挤开收拢，胶囊上下露出 13% 透明度的灰色幽灵项

**When to use it.** "我们替你搞定 ___" 这类句式卖点；SaaS 功能列举的一句话收口；浅底品牌片主视觉一拍

**Why this shot earns its place.** 词槽轮换有两派：让句子躲开变化（宽度固定的滚轮），或者让句子**接受** 变化（胶囊撑宽、两侧文字被挤开）。这卡是后者，代价是必须把宽度算准， 回报是句子读起来活的——"Your" 和 "Handled" 被推着走，观众感到胶囊里 的词有分量。上下露出的灰色幽灵项是第二个记号：它明示"这是个可以滚的 列表"，让观众预期还有下一个词。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 词表 | 4 词 + emoji（Sales/Workflow/Admin/Reports），3 次切换 | 词长差决定挤开幅度的观感：demo 最短 5 字母最长 8 字母；差 >2 倍胶囊跳变太猛，句子重心左右甩 |
| 切换点 | `[0.25, 0.47, 0.69]`，窗 0.12（≈18f） | 段间约 0.10（≈15f）静置读词；起手 0.25 前的静置让观众先认出句式 |
| 缓动 | `E.inOutCubic` | 两头缓才像滚轮起停；outCubic（只后缓）读作被甩上来，胶囊宽度也会跟着突变 |
| 胶囊 | 高 48px、圆角 99、`#1a1c24`、宽 = 文本宽 + 74 | +74 是左右内边距 + emoji 位；<50 词贴边，>100 胶囊胖成按钮 |
| 幽灵项 | 上 -38 / 下 58px，基础透明度 0.13 | 0.13 是"看得见但不抢"的甜点；>0.25 读作三行并列文字，不是幽灵；删了列表暗示就没了 |
| 幽灵视差 | `(pos-near)·48·0.5`（半速） | 半速是"外圈更远"的立体感来源；同速则三行像一整块滑动，幽灵失去意义 |
| 句子字号 | 两侧 30px/800、胶囊内 22px/700 | 胶囊内比句子小是正确层级（徽章依附句子）；等大或更大就读作两个标题打架 |
| 配色 | 底 `#fbfbfd`、句子 `#15171d`、胶囊白字 | 浅底 + 单一深色块是本卡的身份证；深底版会让胶囊消失，需整套重配 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- **宽度靠 setup 期 `offsetWidth` 实测**：字体没加载完时量到的是回退字体
- 词长差要控制在 2 倍内：宽度自适应是本卡的卖点也是风险，
- 两侧文字必须 `flex:none`：不然 flex 会去压缩它们而不是移动它们，
- 幽灵项文本取 `round(pos)` 的邻居，所以在切换的正中间（pos=x.5）会
- emoji 在不同平台字形宽度不一（尤其 `⚙️` 带变体选择符），会让实测宽度
- 与 vertical-word-roll-blur-cycle 分工：那卡宽度固定、裸词、带滚筒 blur

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/typography/pill-chip-slot-cycle-handled/PillChipSlotCycleHandled.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
