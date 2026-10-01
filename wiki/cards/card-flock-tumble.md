# card-flock-tumble

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/card-flock-tumble`.

## Identity

- **slug**: `card-flock-tumble` (join key across cards, demos, media and deep links)
- **category**: `transition` — Transitions / 转场
- **energy**: `极高` — rank 7/8
- **suggested duration**: 翻飞 ~1.5s + 慢转展示 ~0.3s + 收束 0.3s + 烟环+巨字 ~2s；全段 4.5s → **45 frames @30fps = 1.5s**
- **cross-category tags**: `transition`
- **upstream source**: references/shots/transition/card-flock-tumble.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `card-flock-tumble` | —f | B | `demos/transition/card-flock-tumble/CardFlockTumble.tsx` |

## What it does

三张 UI 页卡从侧棱薄边 3D 翻飞成阶梯站定（全程清晰、样条连续丝滑），站定后保持慢转不停，快速收束吸入中心，炸出单个湍流烟雾环扩散，巨字横贯收场

**When to use it.** 能量高潮段（功能页群→品牌口号的爆点转场）；霓虹暗场调性；"多页面能力"收束成一句话的段落

**Why this shot earns its place.** 三张页卡像被甩出的扑克在 3D 空间翻飞列队，站定亮相后被瞬间 吸入中心，炸出一圈烟雾环，品牌巨字穿环而出——"能力展示→能量 坍缩→口号爆发"一气呵成。命门有三：**丝滑**（侧棱→翻飞→站定 一条 Catmull-Rom 样条导数连续，分段插值的顿挫会被读出来）、 **不许停**（站定后保持低角速度慢转到收束，静止段被裁"不要停住， 保持旋转"——高潮段没有静帧）、**全程清晰**（motion blur/景深糊 全删，被裁"不要加模糊效果"）。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 三卡间距/大小 | 大幅重叠成一叠阶梯、scale 1.6–1.74 | 两轮加码判例："再靠近一些，再大些"——阶梯要读作一组不是三张 |
| 站定慢转 | ry ~0.34°/f 连续 | **不许静止**（判例）；>1°/f 读作还没站定 |
| 收束时长 | 10f ease-in | 22f 版被裁"要快"；透明度早退=吸入不可读（返工判例） |
| 烟雾环 | 单圈、湍流絮边、衰减极慢 | 多圈被裁；平滑霓虹圈/粒子版被裁——对照原片密帧做湍流质感 |
| 模糊 | 全程零 blur | 翻飞/收束加 blur 均被裁 |
| 样条 | 一条 Catmull-Rom 贯穿 | 分段 lerp 有速度台阶，"丝滑流畅"是裁决原话 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 烟雾环质感判例：干净图形环（描边圆/同心波）三轮被裁，最终版
- 与 particle-celebrate-hits 分工：那张是粒子礼花打击点；本卡
- 与 bubble-swarm-takeover 分工：那张是群体涌入接管；本卡是

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/transition/card-flock-tumble/CardFlockTumble.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
