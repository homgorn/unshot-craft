# crane-rise-reveal

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/crane-rise-reveal`.

## Identity

- **slug**: `crane-rise-reveal` (join key across cards, demos, media and deep links)
- **category**: `opening` — Opening & Brand / 开场与品牌
- **energy**: `中高` — rank 5/8
- **suggested duration**: 5s（特写 hold 20f + 拉升 100f + 满幅静止 30f） → **20 frames @30fps = 0.7s**
- **cross-category tags**: `opening`, `camera`, `data`
- **upstream source**: references/shots/opening/crane-rise-reveal.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `crane-rise-reveal` | 120f | B | `demos/opening/crane-rise-reveal/CraneRiseReveal.tsx` |

## What it does

升降臂拉升揭示——开场怼在一行数据特写，相机沿 Y 轴减速升起后拉，行行涌入直到整面 dashboard 铺满全幅

**When to use it.** "从细节到全局"的开场定场；与 drone-dive-landing（全局→单点俯冲）互为反向

**Why this shot earns its place.** 开场定场库内已有 drone-dive-landing——从上帝视角砸进 hero 特写， "全局→焦点"。本卡是它的镜像："焦点→全局"——先怼在一行真实数据上 让观众看清"这是什么"，再升降臂式拉升后退，一排排内容涌入画面， 最后整面产品铺满——"你看到的这一行，只是这一面墙的一格"。 适合以产品体量/内容丰富度为卖点的开场；两卡同片只用一个方向。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 起点特写 | scale 3.2，对准最底行（一行占满画幅） | hold ≥20f 让"这是一行数据"可读再起飞 |
| 拉升 | 100f Easing.out(quad)，scale 3.2→1.0 | 快于 80f 行脉冲追不上；慢于 130f 中段拖 |
| 行脉冲 | 越线触发，0→0.22→0 深色叠层 22f | 脉冲跟不上相机（固定间隔触发）立刻穿帮 |
| 收尾 | 满幅后真静止 ≥30f | R1；满幅帧即标准构图，不再补推 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 起点特写 = 一行内容被放大 3.2 倍盯着看，真实素材先过
- 快速拉升段可包 CameraMotionBlur（参数见 deck-deal-flyin 运动模糊行），
- 与 drone-dive-landing 同片不并用（一升一降互为镜像，观众读作同一招）；

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/opening/crane-rise-reveal/CraneRiseReveal.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
