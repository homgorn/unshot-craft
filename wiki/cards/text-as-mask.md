# text-as-mask

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/text-as-mask`.

## Identity

- **slug**: `text-as-mask` (join key across cards, demos, media and deep links)
- **category**: `opening` — Opening & Brand / 开场与品牌
- **energy**: `中高` — rank 5/8
- **suggested duration**: 5s（hold 20f + 字内漂移 80f + 放大接管 30f + 静止 20f） → **20 frames @30fps = 0.7s**
- **cross-category tags**: `opening`, `typography`
- **upstream source**: references/shots/opening/text-as-mask.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `text-as-mask` | —f | B | `demos/opening/text-as-mask/TextAsMask.tsx` |

## What it does

文字视频遮罩——超粗大标题字内部透出缓慢平移的产品画面，结尾字形放大 26 倍溢出、内部画面接管全屏

**When to use it.** 品牌词/口号与产品画面二合一的开场或章节卡；字是门、产品在门里

**Why this shot earns its place.** 标题和产品画面抢屏幕是老问题——先字后画慢，画上压字挤。这一式让 两者同体：字形就是遮罩，产品只透过笔画显形，观众同时读到词和画面 质感；结尾字形胀开溢出画幅，产品自然接管全屏——"从品牌词走进产品" 一条镜头说完，兼任章节转场（与 transition-travel C 字腔穿越同族： 那边是镜头钻进字腔，这边是字形自己胀开，前者相机动、后者门动）。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 字号/字重 | ≥360px / 900 | 笔画就是视口——细字重等于把产品塞进门缝 |
| 漂移速度 | ~2.75px/f 匀速 | 快了字内画面读不清；漂移方向选画面信息密的轴 |
| 放大倍率 | 26x（按字形/画幅比配，洞撑满即可） | 不足则接管帧还看得到字边残影 |
| 收尾 | 接管后真静止 ≥20f | R1；接管完成帧产品应落在标准构图 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 字内透出的产品画面全程被特写盯着看——真实素材先过
- 换词/换字体后 origin 手推值必失效——渲后看放大方向，洞不对中就微调
- 与 transition-travel C 字腔穿越同片不并用——同为"字里长出世界"，
- mask 层与内容层的 transform 必须分离驱动（wrapper 放大/内容反向补偿），

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/opening/text-as-mask/TextAsMask.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
