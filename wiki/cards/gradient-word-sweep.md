# gradient-word-sweep

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/gradient-word-sweep`.

## Identity

- **slug**: `gradient-word-sweep` (join key across cards, demos, media and deep links)
- **category**: `typography` — Typography & Title Cards / 文字与字卡
- **energy**: `高` — rank 6/8
- **suggested duration**: 扫充 ~15–20f（要快）+ 稳态闪电呼吸 1–2s；全段 2.5–3.5s → **20 frames @30fps = 0.7s**
- **cross-category tags**: `typography`, `effects`
- **upstream source**: references/shots/typography/gradient-word-sweep.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `gradient-word-sweep` | 30f | B | `demos/typography/gradient-word-sweep/GradientWordSweep.tsx` |

## What it does

黑底标语里关键词被渐变彩光从左到右快速扫过"充能"——波前字符辉光最强向后衰减，填满后字符间勾连细紫红闪电、整词稳态泛光呼吸

**When to use it.** 标语里给单个动词/卖点词充能（Supercharged/faster/AI…）；能量高潮段的文字戏；黑场品牌片的口号帧

**Why this shot earns its place.** 整句白字里只有关键词被"通电"：渐变彩光从左到右快速扫过字符， 像能量注入——扫过的瞬间最亮（波前尾迹），随后衰减到稳态； 填满后字符之间跳起勾连的细闪电，词保持泛光呼吸。三个命门： **快**（扫充 15–20f，慢了读作进度条）、**波前最亮**（刚点亮的 字符效果最强，没有这个梯度就是静态渐变裁切）、**辉光克制** （AE 式多层泛光但别糊成一团，闪电细而稀疏才是点缀）。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 扫充时长 | 15–20f | 原片"速度很快"；>28f 读作进度条 |
| 波前增亮带 | ~34% 词宽，波前最亮向后衰减 | 无梯度＝静态渐变；带太宽＝整词一起亮没有"注入"感 |
| 稳态泛光 | 4 层 opacity 0.55/0.55/0.62/0.72 | 0.75+ 档被裁太强；辉光层数<3 读作纯色 |
| 闪电线宽 | 外 6/中 2.4/核 1.4 @1080p | 加倍即被裁"粗"；颜色偏紫红（magenta 216,60,190 系） |
| 闪电频率 | 稀疏零星（同屏 ≤2 道，间歇 >8f） | 频率高读作电弧故障；实测 demo 仍略密于原片 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 判例三条（用户逐字意见沉淀）：①填充过程禁跟随光点；②闪电
- 与 type-rhythm-sync/cel-flash-stomp 分工：那些是节拍/砸字；
- 关键词外的正文保持纯白静止——全句都动就没有"只有它通电"的戏

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/typography/gradient-word-sweep/GradientWordSweep.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
