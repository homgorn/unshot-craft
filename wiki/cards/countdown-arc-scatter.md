# countdown-arc-scatter

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/countdown-arc-scatter`.

## Identity

- **slug**: `countdown-arc-scatter` (join key across cards, demos, media and deep links)
- **category**: `typography` — Typography & Title Cards / 文字与字卡
- **energy**: `高` — rank 6/8
- **suggested duration**: 约 1.1s（33f@30fps，极短单拍） → **33 frames @30fps = 1.1s**
- **cross-category tags**: `typography`
- **upstream source**: references/shots/typography/countdown-arc-scatter.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `countdown-arc-scatter` | 33f | A | `demos/typography/countdown-arc-scatter/CountdownArcScatter.tsx` |

## What it does

白底表盘 9 个等大数字沿大弧切向排布，整盘扫过 96° 后减速急停，"5" 停在弧顶随即平移落位成标题首字符，其余数字带 blur 原地散去，标题逐词模糊淡入、末词转强调色

**When to use it.** 倒计时/时长承诺类文案（"5 min to install"）；数据揭晓的一拍；需要"仪表盘"语汇的浅底短镜

**Why this shot earns its place.** "5 分钟装完"写成静态字卡没人信。表盘扫过的做法把这个数字放进一个 **量程**里：45、35、28、22、17、10 一路扫过去，停在 5——观众看到的是 "从很多降到很少"，数字自带论证。停下后 "5" 不消失而是**平移变成标题的 首字符**，一个元素完成从仪表到文案的身份切换，这是本卡最值钱的一手。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 数列 | `[45,35,28,22,17,10,5,4,3]`，间距 24° | 递减不等距（45→35→28…）才像真量程，等差数列读作刻度尺；"5" 必须在 i=6 位（前 6 个扫过、后 2 个预留） |
| 弧半径 | R0 = 150px，pivot 在 top 58% | 半径决定弧的曲度：<100 数字挤成小圈，>220 弧近乎直线，表盘感消失 |
| 扫动 | 96° → 0°，窗 0.52（≈17f），outCubic | 96° 约等于扫过 4 格；outCubic 的急停是唯一的"到位"信号，改 inOut 就成了缓缓停下，没有仪表的干脆 |
| 可视角窗 | `(70- | pa |
| "5" 落位 | 窗 0.52→0.7（≈6f），目标 `(-148,-30)`，同步回正 | 落位窗紧接扫停，中间不留静置——留了就断成两个动作；目标点必须正好是标题首字符位 |
| 其余淡出 | 窗 0.5→0.7 inQuad + `blur(out·3)` | 淡出**早于** "5" 落位 0.02 起手，先让路；blur 让散去像失焦而非消失 |
| 刻度差速 | `rot·0.35`；标题逐词窗重叠约 0.06、`blur (1-p)·6`px | 差速是"盘 vs 指针"的层次来源，1.0（同速）读作一整块贴图在转；逐词窗重叠才是"一句话"，排队读作三个词各自出场 |
| 末词染色 | `seg(0.84, 0.98)` → ACCENT | 全片唯一的颜色事件，落在最后一个词上就是句子的落点 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- **1.1s（33f）是极限压缩**：扫动只 17f、"5" 落位 6f、三词淡入各约 5f，
- **换文案时字符数要贴近占位（`min` / `to` / `install`）**：标题的
- 数字必须**等大同字重**（40px/600）：大小不一读作数据可视化，
- "5" 的角度设计（i=6 → ang=0）是本卡的地基：改数列长度或改哪个数字
- 白底专用：`#fff` 底 + `#17181c` 墨色数字是这卡的干净感来源；深底版
- 声音：扫停那一下 + 落位那一下是两个紧连的节奏点（相隔仅 6f），

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/typography/countdown-arc-scatter/CountdownArcScatter.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
