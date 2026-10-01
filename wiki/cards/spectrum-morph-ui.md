# spectrum-morph-ui

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/spectrum-morph-ui`.

## Identity

- **slug**: `spectrum-morph-ui` (join key across cards, demos, media and deep links)
- **category**: `rhythm` — Rhythm & Montage / 节奏与蒙太奇
- **energy**: `中` — rank 4/8
- **suggested duration**: ~4.7s（裂开 8f + 跳动 64f + 收拢 12f + 静止 39f） → **64 frames @30fps = 2.1s**
- **cross-category tags**: `typography`, `rhythm`
- **upstream source**: references/shots/rhythm/spectrum-morph-ui.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `spectrum-morph-ui` | 12f | B | `demos/rhythm/spectrum-morph-ui/SpectrumMorphUi.tsx` |

## What it does

频谱化 UI——标题下划线裂成一排竖条按频谱跳动两小节，再收拢还原成直线；音乐可视化长在 UI 上

**When to use it.** 有音轨片子的声画同步高光段（BGM 副歌起/鼓点密集段）；标题字卡、章节页的下划线/分隔线构件

**Why this shot earns its place.** 声画同步库内已有 type-rhythm-sync A（字重脉冲）——那是"文字自己动"； 本卡是"UI 构件变成均衡器"：下划线这个最不起眼的构件被音乐借用两小节， 裂成 28 根竖条跳出频谱，然后**收拢还原、完璧归赵**。借用-归还结构是 全部优雅所在——观众先认出"这是下划线"，再看它变成别的东西，最后 看它变回来；若一开始就是频谱条，只是又一个音乐可视化。跳完必须还原 成那条 8px 直线，一像素不差。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 条数/条宽 | 28 根、gap 6px 时 ≈20px 宽 | >40 根读作噪声；<16 根读作柱状图 |
| 峰值幅度 | AMP=92，实测峰值 75–85px | spec 62 实测只有 ~55px 不够响，已加码 1.5×（可感性判例） |
| 包络 | 左高右矮（低频高/高频矮） | 均匀高度像栅栏不像频谱 |
| 换挡节拍 | seed 每 4 帧换挡 | 逐帧换读作电噪；8f 以上读作慢动作 |
| 时间轴 | 裂开 8f out-cubic / 跳动 64f（两小节）/ 收拢 12f | 跳动 <1 小节读作故障闪了一下 |
| 收尾 | 收线后真静止 ≥39f，像素级 diff 为零 | 归还之后再动一下，借用结构就毁了 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- **声音强依赖**：跳动段必须真的踩在音乐上——无音轨的频谱跳动读作
- 全片 ≤1 次，且只借用一个构件——标题下划线在跳、卡片分隔线也在跳，
- 与 type-rhythm-sync 同为声画同步族，同一段落二选一——文字在脉冲、
- 收拢帧后的静止段是"归还仪式"的一部分，从重给（≥35f），别急着切

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/rhythm/spectrum-morph-ui/SpectrumMorphUi.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
