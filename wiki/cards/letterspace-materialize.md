# letterspace-materialize

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/letterspace-materialize`.

## Identity

- **slug**: `letterspace-materialize` (join key across cards, demos, media and deep links)
- **category**: `opening` — Opening & Brand / 开场与品牌
- **energy**: `低` — rank 1/8
- **suggested duration**: 静置 ~15f + 描画 ~50f + 终态静置 ≥30f；全段 3–4s → **15 frames @30fps = 0.5s**
- **cross-category tags**: `opening`, `typography`, `outro`
- **upstream source**: references/shots/opening/letterspace-materialize.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `letterspace-materialize` | 52f | B | `demos/opening/letterspace-materialize/LetterspaceMaterialize.tsx` |

## What it does

大字距字标全字符并行连续描画结晶——所有字母同帧起笔、笔画像手写一样连续生长、同帧齐收成词；氛围底景上的品牌字标显影

**When to use it.** 片尾/片头品牌字标登场（SUPERHUMAN 式大字距全大写）；章节题字；needs 静谧/高级感的收束帧

**Why this shot earns its place.** 字标不是淡入也不是打字机，而是"结晶"：全部字母的笔画同时 开始连续生长，像一只看不见的手同时写所有字母，同一瞬间齐收 成词。两个命门：**连续**（笔画必须是连续画出的过程，不许遮罩 分段——先半截再另半截会被读穿；任何中间帧都该像"写到一半"）； **同步**（所有字母同帧起笔、同帧完成——逐字错峰是打字机语义， 这里是整词一体的仪式感）。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 描画时长 | ~50f（f16 起 f68 收 @30fps） | <30f 读不出"画"的过程；>80f 拖 |
| 同步性 | 全字符同帧起收、零错峰 | 判例：逐字错峰版被裁"所有字母是在同一个时间完成书写" |
| 连续性 | pathLength 连续生长、无分段跳变 | 判例：遮罩分段版被裁"应该是连续的笔画画出来" |
| 字形 | 骨架单线、字面宽高比 ~1.07、笔画细 | 竖长（比 <0.8）被裁；粗笔画丢结晶感 |
| 字距 | ~0.6em | 大字距是本卡身份；<0.3em 改用普通描画卡 |
| 终态静置 | ≥30f | 结晶完成后必须让观众读一次整词 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 与 draw-svg-trace 分工：那张是通用描画（图标/插画/单元素）；
- 与 type-assembly-moves 分工：那张是字块组装（位移拼合）；
- 骨架字形需手绘 path（现成字体轮廓是双线勾边，描画观感不同）；
- 原片（superhuman-promo）底景是实拍暮色山景+水面倒影；demo 为

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/opening/letterspace-materialize/LetterspaceMaterialize.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
