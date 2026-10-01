# glow-flyline-moves

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/glow-flyline-moves`.

## Identity

- **slug**: `glow-flyline-moves` (join key across cards, demos, media and deep links)
- **category**: `effects` — Light & Emphasis / 光效与强调
- **energy**: `A 低` — arc or n/a, not sortable
- **suggested duration**: A ~5s / B ~4.7s / C ~5.2s → **150 frames @30fps = 5.0s**
- **cross-category tags**: `data`, `effects`
- **upstream source**: references/shots/effects/glow-flyline-moves.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| B | `flyline-arc` | 22f | B | `demos/effects/glow-flyline-moves/FlylineArc.tsx` |
| A | `glow-orb-ambient` | —f | B | `demos/effects/glow-flyline-moves/GlowOrbAmbient.tsx` |
| C | `orb-flyline-relay` | 24f | B | `demos/effects/glow-flyline-moves/OrbFlylineRelay.tsx` |

## What it does

暗场光斑与飞线三式——glow-orb-ambient 光斑底噪、flyline-arc 飞线连接、orb-flyline-relay 同帧共振组合

**When to use it.** 全片唯一暗场段落的氛围与数据叙事：铺底噪用 A、讲数据流向用 B、要背景给前景搭腔用 C；Linear 官网味

**Why this shot earns its place.** 这是库内第一张整卡住在**暗场**的卡。白底提亮不可见判例反过来读就是： 要玩光，先去暗场。A 是空间的呼吸——近黑底三团重 blur 光斑有机漂移， 中央深卡边缘随最近光斑靠近而泛光，背景不再是死的；B 是数据的动词—— 发光弧线从 A 卡"打"到 B 卡，亮点头领跑、渐隐光尾，落点描边脉冲点亮， 指标关联第一次有了方向；C 是 A+B 的焊接——飞线落点帧邻近光斑同帧 涨亮一拍，氛围层与事件层**同帧共振**，互相搭腔而非各演各的（组合命门： 拆开共振帧就退化成两张卡并置）。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| A 光斑 | 峰值 opacity 0.32/0.22/0.18；漂移振幅合计 ≥240px、周期 92–134f 交叉不等 | 同周期漂移读作整体晃动不是"有机" |
| A 卡缘辉光 | box-shadow 0→28px 白 0.25 | 无辉光光斑与卡互不认识 |
| A 收敛 | 90–120f out-sine 收敛冻结（起始斜率≈0.94 近似连续），末 30f 真静止 | 硬停一帧读作卡死；缓动收敛才有真静止 |
| B 线体 | 白线 4.5px + 9px 深色衬底；暗场版可去衬底 | 浅底无衬底白线直接消失（demo 判例） |
| B 光头 | 白点 9px + halo，仅生长期条件挂载 | opacity 到 0 不算摘罩，永不真静止 |
| B 脉冲 | 描边扩散 out-cubic 6f / 消散线性 12f | 白底禁提亮——用加深罩 0.16 替代 |
| C 共振 | 落点帧同帧起 surge；卡 8f 亮到 1 + 描边脉冲残余 0.3 | 错 2f 以上共振读不出"搭腔" |
| C 时间轴 | 动作 f98 前结束、光斑 f120 冻结，末 35f 真静止 | 氛围层最后冻，事件层先收 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 暗场段与纸墨浅底主视觉切换成本高——全片暗场段 ≤1 段，进出
- 光斑漂移末段**必须**缓动收敛到静止再冻结——匀速漂移直接 clamp
- 实战品牌色版：光斑用品牌色对（如蓝紫），灰阶参数只保证明度关系，
- B 接力线 ≥3 条时改用 C——纯飞线连打读作大屏模板，共振才有作者感
- 声音：B/C 每次落点一声轻打点，A 无声（sound-design §4.5）

## Card structure

`intention` | `variants` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/effects/glow-flyline-moves/FlylineArc.tsx`
- `demos/effects/glow-flyline-moves/GlowOrbAmbient.tsx`
- `demos/effects/glow-flyline-moves/OrbFlylineRelay.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
