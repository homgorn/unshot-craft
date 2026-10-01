# grain-dissolve

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/grain-dissolve`.

## Identity

- **slug**: `grain-dissolve` (join key across cards, demos, media and deep links)
- **category**: `outro` — Outro / 收尾
- **energy**: `中高` — rank 5/8
- **suggested duration**: 约 2.0s（60f@30fps；砂化 0.26–0.56s · 凝聚 1.2–1.42s · 凝固回落收尾） → **60 frames @30fps = 2.0s**
- **cross-category tags**: `outro`
- **upstream source**: references/shots/outro/grain-dissolve.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `grain-dissolve` | 60f | A | `demos/outro/grain-dissolve/GrainDissolve.tsx` |

## What it does

整行字爆裂成沸腾颗粒噪点并浮现斜纹选区框，噪点云急速凝聚成更大号发光短字标，位移衰减归零定格

**When to use it.** 收尾"XX. Now Live"式上线宣告；长句信息压缩成品牌短标的能量聚合拍

**Why this shot earns its place.** 把"一句话浓缩成一个词"拍成物理事件：句子先失稳沸腾成颗粒（信息解体），选区框暗示"正在选中提取"，然后所有颗粒能量向中心坍缩成更大更亮的短字标——观众读到的是"这一切归结为它"。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| displacement scale | 峰值 52 | <30 只是"轻微毛边"；>80 颗粒散到认不出轮廓，"隐约可辨"是砂化质感的底线 |
| baseFrequency | 0.9 → +0.4 | 越高颗粒越细；低于 0.5 变成大块扭曲不是"砂" |
| seed 换帧率 | floor(t*46)，2s 内 46 次 | 降低会看出噪声图重复；保持 ≥20 次/秒的换图率 |
| 砂化窗口 | 0.13–0.28（outCubic） | 前 0.13 的干净字停留是"失稳前的常态"，砍掉则没有对比 |
| 凝聚交叉 | 0.60–0.71（inOutCubic） | 必须落在最沸腾段内完成换字；提前会穿帮看到两行字叠影 |
| 辉光包络 | burst·0.3 + cond·0.7 − settle·0.45 | 凝聚冲高是卡点位，压 BGM 重音；回落别到 0，留柔光"余温" |

## Known pitfalls

- 换字标文案（ACME → 项目短标）时两行 `<text>` 都要改：整行句式 `{ XX. Now Live }` 与短标 XX 必须指同一对象，否则叙事断裂
- 短标变长（>6 字符）需同步缩 54px 字号或加宽选区框 bw，否则凝聚后超出框位视觉重心偏移
- `feDisplacementMap` 在 Safari 上性能较差，这张卡是 2s 短拍可接受；拉长时长需实测帧率
- 选区框撤场（0.55–0.64）必须早于凝聚完成（0.71）——框留到凝固后会读作"还没选完"，语义反了

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/outro/grain-dissolve/GrainDissolve.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
