# flying-words

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/flying-words`.

## Identity

- **slug**: `flying-words` (join key across cards, demos, media and deep links)
- **category**: `typography` — Typography & Title Cards / 文字与字卡
- **energy**: `高` — rank 6/8
- **suggested duration**: 约 6.0s（180f@30fps，2 个完整循环，可无缝接续） → **180 frames @30fps = 6.0s**
- **cross-category tags**: `typography`
- **upstream source**: references/shots/typography/flying-words.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `flying-words` | 180f | A | `demos/typography/flying-words/FlyingWords.tsx` |

## What it does

22 个关键词按黄金角铺在扁椭圆截面上，沿 z 轴从 -1750px 飞到相机前 800px 擦身而过，透明度走 [0,1,0.5,0.2,0] 生命曲线，跑满 2 整圈首尾无缝

**When to use it.** 关键词云/能力清单的动态背景；片头片尾的"信息量"垫底层；需要纵深穿越感的转场

**Why this shot earns its place.** 关键词列举最土的做法是堆一屏静态词云。词语隧道把同一批词**摊到时间轴上**： 远处生成、由小变大、擦过镜头消失，观众永远只在读三五个词，但主观感受是 "词很多"。它是背景层不是主角层——相机不动、元素动，所以前景压一层标题 或 UI 完全不打架。词表整体替换成项目关键词即可，不改一行运动逻辑。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 词表 | 22 词，字号 `20 + rand·16`px（20–36），800 字重 | 词数与相位 `i/N` 绑定：<12 词画面稀，>30 词近处糊成一片；字号随机是层次感来源，全同号读作贴图 |
| 纵深行程 | z −1750 → +800px，perspective 1100 | 起点更远（−2500+）词太小认不出；终点不过 0 就没有"穿过去"只有"飞到脸前停住" |
| 散开系数 | `drift = 0.5 + u·1.35` | 系数 <1 词全从正中喷出像爆炸；>2 早早飞出画外，隧道变喷泉 |
| 生命曲线 | `[0,1,0.5,0.2,0]` @ `[0,0.25,0.6,0.85,1]` | 中段那个 0.5 是给前景让位的；改成一路满亮就抢主角，改成早早归零隧道变空 |
| 循环圈数 | `CYCLES = 2`（必须整数） | 非整数 → t=1 与 t=0 不接，loop 处一跳；圈数越多单词过镜越快 |
| 近端模糊 | `u>0.86` 起 `(u-0.86)·26`px | 阈值提到 0.95 巨大词硬边扎眼；系数 >40 末段成色斑 |
| 配色 | `hsl(200+rand·130, …)` 蓝→紫，光晕 `rgba(120,150,255,.22)` | 深底浅字发光是身份证，白底套本卡直接失效——要浅底得整套重配 |
| 中心光晕 | 220px、blur 6、呼吸 2 次/片 | 删了隧道尽头没有焦点，词像随机乱飞；呼吸频率跟 CYCLES 对齐才不打拍 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 词表替换要**保持词数与字长量级**（demo 22 词、单词 4–9 字母）：相位是
- `CYCLES` 必须是整数，否则首尾不接——这是本卡"可无缝 loop"的唯一前提，
- 只做背景层：中段生命曲线压到 0.5 就是为了给前景让位，把它当主角
- 深底专用：`text-shadow` 发光 + 径向暗角是效果的一半，浅底上词会糊成

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/typography/flying-words/FlyingWords.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
