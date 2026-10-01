# aurora-bloom-bg-flip

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/aurora-bloom-bg-flip`.

## Identity

- **slug**: `aurora-bloom-bg-flip` (join key across cards, demos, media and deep links)
- **category**: `effects` — Light & Emphasis / 光效与强调
- **energy**: `由低到高` — arc or n/a, not sortable
- **suggested duration**: 约5.2s（156f@30fps） → **156 frames @30fps = 5.2s**
- **cross-category tags**: `effects`
- **upstream source**: references/shots/effects/aurora-bloom-bg-flip.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `aurora-bloom-bg-flip` | 156f | A | `demos/effects/aurora-bloom-bg-flip/AuroraBloomBgFlip.tsx` |

## What it does

浅灰底从底部升起紫橙柔焦 blob，随后整个底色在约 0.36s 内压暗到近黑、blob 压成余晖；文案同步 blur-out 换句 blur-in，换句间留空档不 cross-fade

**When to use it.** 叙事转折点（"多年以来…→一切都变了"）；品牌片从铺垫拉到重音的那一拍；深浅色系之间的段落切换

**Why this shot earns its place.** 把"底色反转"当成重音符号用：前 62% 让极光慢慢升起、观众适应浅底， 然后用不到 0.4s 把整个画面压到近黑——这一下比任何缩放/闪白都更像 "翻页"。文案的换句必须卡在反转之后，且中间留空档，让观众先接住画面 变化再读新句。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| blob 模糊/尺寸 | blur(60px)，主层 90%×85%，容器 inset −10% | 模糊小于 40px 就看得出是圆，成了"色球"不是"光" |
| 升起 | translateY 32%→−6% + scale 1→1.25，t 0.04→0.62 outCubic | 占掉 60% 时长是故意的：酝酿越长，反转越有分量 |
| 反转时长 | t 0.63→0.70 inOutQuad ≈ 0.36s | **命门**：拉到 1s 就不是重音而是渐变过场 |
| 底色 | #ececec → #0a0a12（不是纯黑） | 纯黑会让余晖 blob 边缘出现色阶断层 |
| blob 压暗 | opacity 1→0.4，白色融边层同步归零 | 不压暗 blob，暗场里紫橙会过曝糊成一团 |
| 橙核漂移 | translateX ±8%，2.2 周期/全片 | 幅度到 15% 就看得出是"一个球在动" |
| A 句 blur-out | 逐词 stagger 0.04、各 0.10、inQuad、blur→8px | inQuad 让消失是加速的，读作"被光吞掉" |
| B 句 blur-in | 逐词 stagger 0.06、各 0.11 outQuint + 0.16 内紫→白 | 收色比入场晚一点，落定瞬间才转白，是"定稿"的信号 |
| 换句空档 | A 收完 t≈0.64 → B 起 0.76（≈0.6s 无字） | cross-fade 会把两句糊在一起，空档才读出"翻篇" |

## Known pitfalls

- 白色融边层（blobC）只在浅底成立，反转时必须 `1−flip` 收掉，
- DEEPP/PURPLE 是这个效果的**本体光色**，不是品牌色槽位；要换成项目色
- 文案是中性占位（"For many years" / "everything changed"），逐词
- 底色用 JS 逐帧写 `background`（`mix()` 出实色），不要用 CSS transition，

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/effects/aurora-bloom-bg-flip/AuroraBloomBgFlip.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
