# vertical-word-roll-blur-cycle

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/vertical-word-roll-blur-cycle`.

## Identity

- **slug**: `vertical-word-roll-blur-cycle` (join key across cards, demos, media and deep links)
- **category**: `typography` — Typography & Title Cards / 文字与字卡
- **energy**: `中` — rank 4/8
- **suggested duration**: 约 5.0s（150f@30fps：静置 → 3 次换词 → 尾部整组淡出） → **150 frames @30fps = 5.0s**
- **cross-category tags**: `typography`
- **upstream source**: references/shots/typography/vertical-word-roll-blur-cycle.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `vertical-word-roll-blur-cycle` | 150f | A | `demos/typography/vertical-word-roll-blur-cycle/VerticalWordRollBlurCycle.tsx` |

## What it does

句尾词换成竖向滚轮，3 次换词各 0.55s（outQuint 七成 + outBack 三成，前快后极慢带微过冲），相邻行按距离上垂直 blur 与灰度，中心词落定瞬间从灰染成强调色

**When to use it.** "Built for ___" 这类句干 + 受众/对象列举的一句话卖点；浅底品牌片的干净一拍

**Why this shot earns its place.** 句尾换词的最优解是滚轮而不是淡入淡出：滚轮自带**方向**（往上翻页）， 观众知道"还有下一个"。这卡的两个身份记号是相邻行的**垂直 blur** （滚轮景深，模拟机械转筒的失焦）和落定时的**染色**（灰→强调色， "这个才是答案"）。句干 `Built for` 全程纹丝不动——眼睛钉在滚轮上， 句干一晃列举感就散。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 词表 | 4 词（Apps→Teams→Data→Everyone），3 次换词 | 末词是结论（最宽那个词），前三个是例子；>5 词观众开始数，<3 词读不出"列举" |
| 拍点 | `[0.16, 0.36, 0.56]`，窗 0.11（≈16f） | 段间 0.09（≈13f）静置是给读词的，读不完的拍子等于没换；窗 >0.18 新旧同屏太久 |
| 缓动配方 | `0.7·outQuint + 0.3·outBack` | outQuint 是机械减速的来源；outBack 那三成给落定"咔"一下，纯 outQuint 读作电子屏滑动 |
| 行高/视窗 | ROW 44px、mask `44×3`px、词宽 190px | 露三行才有滚筒感（露一行读作淡入淡出）；宽度写死 190 是为不挤句干，词更长要同步加 |
| 相邻行 blur | 邻行 3px，最远 5px，**仅垂直向感知** | blur 是"滚筒景深"的身份证，删了退化成词条平移；>8px 邻行糊成灰条看不出是字 |
| 落定染色 | `1 - 2.4d` 映射 ACCENT_DIM→ACCENT | 系数 2.4 让染色只发生在落定瞬间；<1.5 滚动中途就上色，答案感散掉 |
| 字号字重 | 句干与滚轮同为 30px/800、`letter-spacing:-.5px` | 必须完全一致——滚轮词比句干大就读作两个元素，不是一句话 |
| 收尾淡出 | `seg(t, 0.9, 0.985)` 整组 | 末词落定后约 40f 静置再淡出；不 hold 等于白列举 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- **mask 宽度写死 190px**：换词表时最长词（demo `Everyone`）必须能装进去，
- 词长差别不宜过大：mask 宽度是固定的（本卡不做宽度自适应，那是
- 句干必须钉死：demo 用 `flex + gap:14px` 是因为 mask 宽度恒定不会推挤
- `p` 是三段窗**累加**出来的，所以三段窗不能重叠：重叠会让 p 在一帧内
- 与 pill-chip-slot-cycle-handled 分工：那卡是深色胶囊 + 宽度自适应挤开
- 声音：每次落定是一个节奏点，配轻机械/开关音；三连发要交替双样本

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/typography/vertical-word-roll-blur-cycle/VerticalWordRollBlurCycle.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
