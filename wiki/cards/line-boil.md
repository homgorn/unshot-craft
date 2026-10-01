# line-boil

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/line-boil`.

## Identity

- **slug**: `line-boil` (join key across cards, demos, media and deep links)
- **category**: `effects` — Light & Emphasis / 光效与强调
- **energy**: `低` — rank 1/8
- **suggested duration**: 寄生型——沸腾段随宿主 hold 长度，无自身时长 → not a timed card (technique card)
- **cross-category tags**: `typography`, `effects`
- **upstream source**: references/shots/effects/line-boil.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `line-boil` | 105f | B | `demos/effects/line-boil/LineBoil.tsx` |

## What it does

线条沸腾——hold 期间文字/描边轮廓每 3 帧轻微扭动一次，像手绘逐帧重描，静止画面保持"活着"的呼吸感

**When to use it.** 标题字卡/描边元素的长 hold 段（黑场字卡升级首选）；质感层手法，寄生在别的镜头上

**Why this shot earns its place.** 库内 R 系判例要求落定后"真静止"，但长字卡（3s+ 的黑场字卡、片尾） 完全冻结会读作"片子卡了"。本卡给第三种状态：**活着的静止**——轮廓 每 3 帧被"重描"一次，位置内容全然不动，只有线条边缘在极轻微地呼吸， 手绘动画 hold 帧的百年惯例。与 noise-drift（被否决）的区别正是可感性： 漂移是整体 1–3px 位移（肉眼读不出），沸腾是轮廓形变+阶梯跳变（每次 换 seed 都是一次可见的"重描"）。纸墨审美里这是"手工感"的直接来源。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| displacement scale | 8（大字标题）；小字/细线 5–6 | >12 读作故障扭曲；<4 不可感 |
| seed 节拍 | floor(f/3)，即每 3 帧重描 | /2 太贼、/4 以上读作卡顿跳帧 |
| baseFrequency | 0.015（形变尺度约字高级） | 0.05+ 变成毛边噪点，不是"重描" |
| 适用对象 | 大标题、描边框、手绘圈注 | 实心小元素（图标/头像）沸腾读作模糊 |
| 与 R 系关系 | 沸腾段视作合法 hold；宿主镜头收尾若需绝对静止则提前 ≥15f 摘罩 | 摘罩瞬间轮廓归位本身就是一次收束 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 全片同时沸腾的元素 ≤1 组——标题在沸腾、卡片框也在沸腾，观众
- 与 speed-lines/集中线的"沸腾"（impact-feedback C 式每 2 帧换形态）
- SVG filter 对大面积层有渲染开销；1920 全幅文字层可接受，整页
- paper-title-card/黑场字卡（shot-transitions D 式）是本卡首选宿主，

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/effects/line-boil/LineBoil.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
