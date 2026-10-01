# brand-ink-open

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/brand-ink-open`.

## Identity

- **slug**: `brand-ink-open` (join key across cards, demos, media and deep links)
- **category**: `opening` — Opening & Brand / 开场与品牌
- **energy**: `低` — rank 1/8
- **suggested duration**: 约 2.8s（83f） → **83 frames @30fps = 2.8s**
- **cross-category tags**: `opening`, `typography`
- **upstream source**: references/shots/opening/brand-ink-open.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `brand-ink-open` | 104f | B | `demos/typography/brand-ink-open/BrandInkOpen.tsx` |

## What it does

墨线十字准星描画→字标逐字压印→打字机副标→满一秒静止再上浮消散

**When to use it.** 品牌开场；任何"先立名号再进产品"的片头

**Why this shot earns its place.** 第一拍先给品牌记忆点：观众在任何产品画面出现之前，先看清并记住名字。安静、纸墨质感、有一个完整的静止时刻。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 准星描画 | 竖线 0→9f、横线 8→18f，24→34f 淡出 | 描画完必须淡出，残留准星会和字标抢焦点 |
| 字标逐字 | 第 i 字 delay=10+i·3、12f；scale 1.6→1（origin center bottom）+ blur 6px→0 | "opacity+位移/scale+blur→0"是全片入场三件套定式，缺 blur 会显得硬 |
| kicker 打字机 | 0.7f/字符（28 起 ~43.4 完），光标 2f 周期闪、74f 停闪 | 0.7f/字符只适用于装饰性小字；正文交互打字要 3f/字符（对照 type-and-filter，用户嫌快返工过） |
| 品牌 hold | 46→76 帧整整 1 秒 | 硬底线：用户两轮点名"出现后延长停留1秒"（R1）；短于 1s 必返工 |
| 退场 | 7f 上浮 40px + 缩 12% + 淡出 | 退场快于入场——观众已读完，拖长反而泄气 |

## Known pitfalls

- hold 要给的是 wordmark 落定时刻，不是普通字卡/内容卡（R1）——曾把 hold 错加给普通内容卡后很快回滚；指代含糊的"停留"反馈先确认对象再动手（P3） _(rules P3,R1)_
- 开场能量必须低起步：全片能量曲线低开→中段推进→outro 峰值，开场炫技会压死后面的爬升（对照 Q8 的能量曲线要求） _(rules Q8)_

## Card structure

`intention` | `motion` | `params` | `sound` | `pitfalls` | `impl`

**Implementations**
- `demos/typography/brand-ink-open/BrandInkOpen.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
