# slam-entrance-moves

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/slam-entrance-moves`.

## Identity

- **slug**: `slam-entrance-moves` (join key across cards, demos, media and deep links)
- **category**: `effects` — Light & Emphasis / 光效与强调
- **energy**: `高` — rank 6/8
- **suggested duration**: 单式动作段 6–22f + 冲击余波 ~16f + hold ≥45f → **22 frames @30fps = 0.7s**
- **cross-category tags**: `ui-entrance`, `effects`
- **upstream source**: references/shots/effects/slam-entrance-moves.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| C | `impact-burst-kit` | —f | B | `demos/effects/slam-entrance-moves/ImpactBurstKit.tsx` |
| A | `kanada-perspective-snap` | —f | B | `demos/effects/slam-entrance-moves/KanadaPerspectiveSnap.tsx` |
| B | `score-slam` | —f | B | `demos/effects/slam-entrance-moves/ScoreSlam.tsx` |

## What it does

高能砸入三式——kanada-perspective-snap 金田透视急停、score-slam 比分砸落、impact-burst-kit 落点冲击套件（波及邻卡）

**When to use it.** 主角卡/KPI 卡的重拳入场；impact-feedback 管落位后的反馈，本卡管入场本身就是冲击

**Why this shot earns its place.** 库内入场词汇的力度上限一直是 deck-deal-flyin 的"发牌"——快但不重。 本卡补"砸"这一档，三种口味：A 是方向感——卡片带鱼眼级夸张透视贴着 镜头甩进来，"啪"地弹平，动漫金田流的潇洒；B 是重量感——KPI 卡从 镜头前 2.5 倍大小砸落，圆环+尘点+震屏三件套同帧起爆，体育比分弹窗 的分量；C 是传导感——B 的三件套之上，冲击波前沿扫过左右邻卡时把 它们可见地推开再弹回，"这一下震到了邻居"，一件事说清力量大小。 选型按叙事需要：告诉观众"它来了"用 A，"它很重"用 B，"它震动了 全场"用 C。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| A 甩入 | 18f Easing.out(cubic)，translateX -700→0 与透视变形同跑；途中 blur 2px 落定即摘 | 快于 12f 读不到鱼眼畸变，慢于 24f 泄劲 |
| A 落定 | rotateY 过冲 +5° 4f 回 0 + 6px 震屏 2f + 斜长影收正常投影 | "啪"在过冲回弹那一下，不在位移结束 |
| B 砸落 | 6f Easing.in(quad)（加速砸，不是减速落） | ease-out 落地是"放下"，ease-in 才是"砸" |
| B 三件套 | 圆环 80→860px/14f + 尘点 18–30px 飞 160–320px + 震屏 18px 指数衰减 4f | 原案(720px/10px 尘/8px 震)全档不可感，实渲已 ×1.5–2 |
| B 解耦命门 | 环/尘的"扩散"用 out-cubic、"消散"用线性帧时间 | 同用 out-cubic 前段跑太快，刚扩开就淡没 |
| C 波及帧 | 前沿过邻卡中心距反解（460px 距 ≈ 落点后 3f）；包络 cos(t/2)·e^(−t/8)，40f 硬钳 0 | 邻卡与主卡同帧动读作整版抖动，晚 3f 才是"被波及" |
| 收尾 | 全部余波归零后真静止 ≥45f | 重拳 hold 按平常两倍给（同 beat-cut B 判例） |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 三式都带震屏，震屏族（impact-feedback、montage-rhythm A/C）同一镜头
- 声音强依赖：A 的"啪"、B/C 的音爆必须同帧钉（sound-design §4.5），
- C 式邻卡必须先驻场稳定 ≥15f 再被波及——邻卡自己还在入场时被推开，
- 与 domino-cascade（montage-rhythm C 式）的区别要守住：domino 是
- 全片砸入 ≤2 次；三次以上每次都响等于都不响（P4） _(rules P4)_

## Card structure

`intention` | `variants` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/effects/slam-entrance-moves/ImpactBurstKit.tsx`
- `demos/effects/slam-entrance-moves/KanadaPerspectiveSnap.tsx`
- `demos/effects/slam-entrance-moves/ScoreSlam.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
