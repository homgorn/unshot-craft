# hashtag-to-pill-materialize

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/hashtag-to-pill-materialize`.

## Identity

- **slug**: `hashtag-to-pill-materialize` (join key across cards, demos, media and deep links)
- **category**: `interaction` — Interaction & Feature Demo / 交互与功能演示
- **energy**: `中` — rank 4/8
- **suggested duration**: 打字 ~40f + 硬切胶囊 hold ~18f + 缩移 ~14f + 硬切揭示后静置；全段约 3.5s（原片 18–21.5s） → **40 frames @30fps = 1.3s**
- **cross-category tags**: `typography`, `interaction`
- **upstream source**: references/shots/interaction/hashtag-to-pill-materialize.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `hashtag-to-pill-materialize` | 80f | B | `demos/interaction/hashtag-to-pill-materialize/HashtagToPillMaterialize.tsx` |

## What it does

话题词打字实体化——居中打出 "#word"（红实心光标恒亮），1 帧硬切变成宽大胶囊标签，hold 后缩小左移落到页面标签位，再 1 帧硬切揭示成品页；"两次硬切一次滑动"的节奏骨架

**When to use it.** 标签/分类/关键词功能的演示段（笔记 app 打 tag、话题聚合）；"输入 → 变成 UI 实体 → 归位到成品"的三段式叙事

**Why this shot earns its place.** 文字变实体的常规做法是渐变/morph/展开，原片帧级拆解证明 Bear 反着 来：**实体化是 1 帧硬切**——上一帧还是文字+光标，下一帧就是完整 胶囊，无展开无 cross-fade 无回弹。硬切给的是"啪、成了"的确定感， 任何渐变都会把"实体"软化成"特效"。全段骨架是**两次硬切夹一次 滑动**：硬切实体化 → 平滑缩移归位 → 硬切揭示成品页。唯一的连续 运动（缩移）被两记硬切框住，才显得又快又稳。这个节奏骨架是命门， 三段挪动任何一段的性质（把硬切改渐变、把滑动改硬切）整卡就塌。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 打字节奏 | 4–6f/字（原片 ~6 字/秒），mulberry32 抖动 | 均匀间隔读作机打；光标必须恒亮（**原片实测**不闪烁） |
| 实体化 | **1 帧硬切**（原片帧级实测无任何过渡）+ 3f 1.03→1 微落定 | 加淡入/展开立刻降级成普通 morph；微落定 >4f 读作弹跳 |
| 胶囊几何 | 740×236@1920（**原片实测** 493×157@720p ×1.5），无描边 | 胶囊要"宽大过头"才有实体感；加描边读作按钮 |
| hold | ~18f（0.6s，**原片实测**） | <12f 观众没看清胶囊长啥样就飞了 |
| 缩移 | ~0.55x（**原片实测** 273/493）、14f、bezier(0.5,0,0.25,1) | 缩放与位移必须同曲线；分开调会读作两个动画 |
| 揭示 | 落位 +3f 再 1 帧硬切全页 | 揭示若做转场，第二记硬切没了，骨架塌一半 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 与 typewriter-moves/ai-stream-response（打字呈现）、
- 早期版本曾杜撰"胶囊飞入下方滑入笔记卡"段，原片对照证伪已砍；
- transformOrigin 默认 50% 50% 会让缩放落位中心漂移 (1−s)×半宽，
- 与原片残余差距：音符图标手绘 SVG 曲线、Futura 回退字重、揭示帧

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/interaction/hashtag-to-pill-materialize/HashtagToPillMaterialize.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
