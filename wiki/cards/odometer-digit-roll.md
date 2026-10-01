# odometer-digit-roll

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/odometer-digit-roll`.

## Identity

- **slug**: `odometer-digit-roll` (join key across cards, demos, media and deep links)
- **category**: `data` — Data & Metrics / 数据与指标
- **energy**: `中高` — rank 5/8
- **suggested duration**: 滚动+逐位锁定 ~63f + 脉冲 8f + hold ≥45f，约 5s → **63 frames @30fps = 2.1s**
- **cross-category tags**: `typography`, `data`
- **upstream source**: references/shots/data/odometer-digit-roll.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `odometer-digit-roll` | —f | B | `demos/data/odometer-digit-roll/OdometerDigitRoll.tsx` |

## What it does

里程表数字滚动大字报——全屏巨号指标每个数位像老虎机滚轮独立纵向滚动带残影，从左到右逐位过冲停稳，全部锁定瞬间整体加深脉冲

**When to use it.** 单个王牌指标的全屏亮相（"10x"/"99.98%"级）；与 impact-feedback B 式（伤害数字弹出）分工——那是元素级配菜，这是全屏级主菜

**Why this shot earns its place.** 王牌数字的登场库内有"砸"（score-slam）和"弹"（damage-number）， 都是位移系。本卡是**机械系**：数字不是飞进来的，是"算出来的"—— 每位一条 0–9 滚轮高速转动，从左到右逐位减速、过冲半格、咔哒锁定， Vercel Ship/Stripe Sessions 指标段的标准语法。滚动过程自带悬念 （它会停在几？），逐位锁定自带节奏（哒、哒、哒、哒），比直接显示 终值多一整拍的期待感。与 VerticalTicker（backlog 待选）的区别： 有终值、逐位停稳，不是无限滚动墙。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 字号/字体 | 190px fw800 + fontVariantNumeric: tabular-nums | 非等宽数字每滚一格整行抖动（同 scramble 等宽判例） |
| 错峰 | 20+i×7f 起停，从左到右 | 从右往左停读作倒着算；同时停失去"哒哒哒" |
| 过冲 | +0.5 行再 6f 弹回 | 无过冲读作滑到即停，机械感减半 |
| 残影 | 2 副本 0.25/0.12，速度门控 | 3+ 副本高速下糊成一条（行高小于卡片场景） |
| 终值脉冲 | 加深 + 1.035 缩放 8f | 只加深不缩放在 190px 黑字上不可感（实渲加码） |
| 收尾 | 脉冲归零后真静止 ≥45f | R1 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 数位 ≤6（含小数点前后）——每多一位多 7f 错峰，8 位滚完 >2.5s
- 与 impact-feedback B（伤害数字）同片可共存但分工要清：全屏主菜
- 滚动的数字必须是**真值的各位**——终值 99.98 就滚 9/9/9/8，
- 声音强依赖候选位：逐位锁定"哒"×N + 终值确认一声低音

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/data/odometer-digit-roll/OdometerDigitRoll.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
