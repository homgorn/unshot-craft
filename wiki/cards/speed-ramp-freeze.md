# speed-ramp-freeze

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/speed-ramp-freeze`.

## Identity

- **slug**: `speed-ramp-freeze` (join key across cards, demos, media and deep links)
- **category**: `rhythm` — Rhythm & Montage / 节奏与蒙太奇
- **energy**: `中高` — rank 5/8
- **suggested duration**: 变速全程 4–5s（慢速窗 ≥40f）；定格标注全程 4–5s（定格段 ≥45f） → **40 frames @30fps = 1.3s**
- **cross-category tags**: `rhythm`
- **upstream source**: references/shots/rhythm/speed-ramp-freeze.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `freeze-annotate-real` | 135f | B | `demos/rhythm/speed-ramp-freeze/FreezeAnnotateReal.tsx` |
| — | `speed-ramp-real` | 135f | B | `demos/rhythm/speed-ramp-freeze/SpeedRampReal.tsx` |

## What it does

帧号非线性 remap 的两款节奏手法——变速（快→0.2x 凝视→快）与定格标注（流动→定格圈注→解冻）

**When to use it.** 卡片流/长横移中把一个重点"放慢/停下给人看"；教学解说语境用定格标注

**Why this shot earns its place.** 匀速流读作 PPT（R2），全程快流观众抓不住重点（R3）。变速在一条 运动里制造"冲刺-凝视-冲刺"；定格标注更进一步——干脆停下来， 马克笔圈出重点再走。两款同一技术根（帧号 remap），语义不同： 变速是"路过时多看一眼"，定格是"停课划重点"。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 慢窗/定格时长 | ≥40f / ≥45f | 短了凝视不成立（R3 宁慢勿快） |
| 快慢斜率反差 | ≥10 倍 | 反差不足读不出"慢下来了" |
| 圈注描边 | 8f 划完 + 抖动 scale 7 | 太慢像加载动画；无抖动像机械标注 |

## Known pitfalls

- 变速段 SFX 钉帧跟**输出帧**不跟源帧（画面动作在输出时间轴上发生）；
- 定格标注一支 30s 片 ≤2 次（同 D 式克制原则）
- 参数经占位素材调校转正，非实战定稿，首次实战后回验

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/rhythm/speed-ramp-freeze/FreezeAnnotateReal.tsx`
- `demos/rhythm/speed-ramp-freeze/SpeedRampReal.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
