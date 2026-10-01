# magician-card-flourish

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/magician-card-flourish`.

## Identity

- **slug**: `magician-card-flourish` (join key across cards, demos, media and deep links)
- **category**: `opening` — Opening & Brand / 开场与品牌
- **energy**: `高` — rank 6/8
- **suggested duration**: 闪光 0.3s + 飞行 ~1.7s + 定格展示+扫光 ~2s；全段 4.2s → **9 frames @30fps = 0.3s**
- **cross-category tags**: `opening`, `ui-entrance`, `effects`
- **upstream source**: references/shots/opening/magician-card-flourish.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `magician-card-flourish` | 12f | B | `demos/opening/magician-card-flourish/MagicianCardFlourish.tsx` |

## What it does

纯黑场上蓝色星芒闪现 0.3s（X 形针状光束旋转 90°+中心辉光放射小光芒），卡片从闪光点弹射而出——极速自旋弧线飞向镜头、自旋随靠近衰减、瞬间硬定格近满幅、定格后 sheen 扫光

**When to use it.** 单张卡片/海报/封面的魔术性登场（片头主视觉、产品卡揭晓）；纯黑暗场；需要"变出来"仪式感的爆点

**Why this shot earns its place.** 魔术师甩牌：一道蓝色星芒闪过，卡片仿佛从光里被变出来——从画面 中心极远处（视觉上一个小点）弹射而出，沿弧线极速自旋飞向镜头， 到达中心瞬间硬定格成近满幅展示。三个魔术感命门：**闪光先行** （光是"变"的仪式，0.3s 短促干脆）、**弹射节奏**（起飞慢速蓄力→ 急加速踢出→弧线段减速抵达，slow-in→burst→decelerating arc）、 **定格即静**（无减速尾巴无回弹，13 整圈自旋保证定格恰为正面）。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 闪光时长 | 9f（0.3s，用户精确定值；曾 1.5s→0.8s→0.5s 逐轮压短） | 光是仪式不是主角；>15f 抢卡片的戏 |
| 星芒旋转 | 闪光期间动态转 90°（判例：静态摆角被裁"没看到旋转"） | 旋转要逐帧可见；>120° 读作螺旋桨 |
| 光束颜色 | 纯饱和蓝贯穿全长 | 白段过长/衰减过快被裁"不够还原"；青蓝偏灰被裁"要蓝色的" |
| 中心 | 小亮点+辉光+放射短刺 | **白色圆球被裁**——中心是光学辉光不是实体球 |
| 弹射曲线 | slow-in 14%→burst→减速弧线 | 直接匀速/纯 easeOut 没有"弹射"的蓄力感 |
| 自旋衰减 | 后 60% 行程 2.4 次幂减速 | 匀速到底被裁"靠近镜头时应随距离衰减"；整圈数=定格正面的保证 |
| 定格尺寸 | 卡高 94% 画面高 | 初版 1.0x 被裁"更近更大基本靠近上下界" |
| 硬定格 | 全量冻结零回弹 | 魔术感=瞬间静止；回弹读作物理玩具 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- **光效质感判例链**（本卡贡献的全局方法论）：几何色块被裁"5毛
- 工程坑：细针光束**不能放进 CameraMotionBlur**——旋转被模糊采样
- 工程坑：星芒 SVG viewBox 要 ≥ 光束长+旋转扫掠半径，否则端点
- 与 card-flip-reveal/deck-deal-flyin 分工：那两张是翻牌/发牌的

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/opening/magician-card-flourish/MagicianCardFlourish.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
