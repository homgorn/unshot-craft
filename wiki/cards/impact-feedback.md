# impact-feedback

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/impact-feedback`.

## Identity

- **slug**: `impact-feedback` (join key across cards, demos, media and deep links)
- **category**: `effects` — Light & Emphasis / 光效与强调
- **energy**: `高` — rank 6/8
- **suggested duration**: n/a（元素级技法，寄生在落位动作上；各式占用帧数见参数表） → not a timed card (technique card)
- **cross-category tags**: `effects`
- **upstream source**: references/shots/effects/impact-feedback.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| C | `anime-impact` | 30f | B | `demos/effects/impact-feedback/AnimeImpact.tsx` |
| B | `hit-counter` | —f | B | `demos/effects/impact-feedback/HitCounter.tsx` |

## What it does

命中反馈两式——hit-counter 连招计数（顿帧+伤害数字+combo 跳字）、anime-impact 动漫打击帧（负片+集中线+色散）

**When to use it.** 元素落位/撞击的"命中一瞬"——给砸入、撞停加游戏级手感；按强度阶梯选式

**Why this shot earns its place.** 元素砸到位却没有"砸到了"的一瞬，落位读作 PPT 飞入。游戏 juice （Vlambeer screenshake 理论）与动漫演出 impact frames 给了同一答案： 命中的那几帧把时间咬住，冲量才传到观众手上。两式是一条强度阶梯： B 用局部顿帧叠伤害数字和 combo 跳字，把功能清单剪成一套连招， 叙事感最强；C 是最重的一拳——撞停 3 帧翻负片炸集中线，强调级最高、 最风格化。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| B 节奏 | 三卡各隔 30f，命中前 10f ease-in(quad) 砸落；每命中全局冻结 2f | 间隔均匀才有"连招"节拍感 |
| B 伤害数字 | 落点 scale 1.4→1 + 上浮 40–60px + 12f 渐隐 | 渐隐 >16f 拖泥带水，遮住下一击 |
| B 计数器 | 脉冲峰值 1.3/1.45/1.6、rotate −2/−4/−6°、字号递增，`exp(−t/2.4)` 回落 | 逐次加码是命门——三次一样大读不出"越打越狠" |
| C 急推撞停 | crash-zoom 6f ease-in(cubic) 推到 2.4x，卡心收敛到画面正中 | 急推参数走 crash-zoom-punch 卡 |
| C 冲击帧 | 撞停起 3f：`invert(1) grayscale(1)` + 30 根楔形集中线（每 1–2f 换形态）+ 红/青负片副本 screen 叠加 ±8px 错位；第 4f 全撤 | 3f 是甜点——4f 起观众开始"看清"负片，魔术就穿帮 |
| C 恢复震屏 | 第 4f 起 6px 指数衰减（τ≈2.2f），~12f 收干 | 幅度须过肉眼阈值（可感性判例） |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- B 式顿帧**必须全局**——背景滚动也要一起冻，否则读不出"时间被
- 帧 remap 与 speed-ramp-freeze 同技术根，同一镜头别叠用两卡——
- C 式负片帧在纸墨审美的片子里非常抢戏——限高潮一次，且必须与
- B 式游戏化语言浓（伤害数字/combo 是明晃晃的游戏梗），产品调性
- B 式多次顿帧后真实帧比动画时间多出累计冻结帧，排镜头预算时

## Card structure

`intention` | `variants` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/effects/impact-feedback/AnimeImpact.tsx`
- `demos/effects/impact-feedback/HitCounter.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
