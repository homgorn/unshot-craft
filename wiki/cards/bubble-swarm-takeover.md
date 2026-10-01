# bubble-swarm-takeover

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/bubble-swarm-takeover`.

## Identity

- **slug**: `bubble-swarm-takeover` (join key across cards, demos, media and deep links)
- **category**: `transition` — Transitions / 转场
- **energy**: `中高` — rank 5/8
- **suggested duration**: ~4.3s（130f：飘入 ~67f + 峰值藏切 + 散开 ~43f） → **130 frames @30fps = 4.3s**
- **cross-category tags**: `transition`
- **upstream source**: references/shots/transition/bubble-swarm-takeover.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `bubble-swarm-takeover` | —f | B | `demos/transition/bubble-swarm-takeover/BubbleSwarmTakeover.tsx` |

## What it does

珠光气泡群幕布转场——大小不一的气泡从画外飘入越涨越大遮满整屏，页面同步"洗白"，遮蔽峰值处藏切换，气泡向外散开后已是新场景；可混入 i18n 文字胶囊变体

**When to use it.** 章节级换景且品牌世界里有"实体装饰物"可当幕布（气泡/花瓣/图标皆可换皮）；转场即品牌露出的段落

**Why this shot earns its place.** transition-hidden-cut 的前景遮挡式是"一件东西扫过去的 1–3 帧"， wipe-transitions 是一条几何边界扫过——都是"边界"思维。本卡是"幕布" 思维：让一**群**品牌实体花 2 秒飘入前景涨大遮屏，遮蔽峰值藏硬切， 再散开露出新场景。比几何擦除高级的地方在于幕布本身就是品牌资产， 转场时间越长品牌露出越足，反而不嫌慢。命门有二：**峰值必须真遮满** （6 颗巨型气泡按网格钉落点兜底，随机群只管氛围）；**洗白层压在页面 与气泡之间**——页面先被洗掉细节，气泡才接得住全部视线，切换在白纱 后面完成，观众无从对比前后帧。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 峰值帧 | 75/130 | 藏切点；峰值前飘入 ≥60f 才有"涨潮"感，<40f 读作扑脸 |
| 气泡数 | 34 随机 + 6 网格巨型 | 巨型是遮屏保底，删了必漏缝；随机 <20 颗群感散 |
| 洗白 | 0→0.92→0，峰值区间持续 0.92 | <0.8 新旧场景对比穿帮；1.0 变纯白闪，气泡被吞 |
| 景深 | blur 7 / 0.5 / 9 三层 | 全实心读作贴纸雨；近景不虚就没有"穿过泡群"的纵深 |
| 散开 | 径向 1700px ease-in + scale ×0.65 + 尾段淡出 | 原路退回读作倒放；只淡出不外推读作气泡"爆了" |
| wobble | sin(f×0.09) × 10–32px | 去掉后群体像贴图平移；>50px 读作乱流 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 与 transition-hidden-cut 分工：那卡是 1–3 帧的"看不见剪刀"（遮挡物
- 与 wipe-transitions/shot-transitions 同层选型：几何擦除/流白是中性
- 珠光渐变的高光偏移（34%/28%）是"3D 球"错觉来源，改成居中径向渐变
- 峰值帧前后各 ±2f 内不得有任何气泡 opacity <1 的空隙露底——检查
- 实战换皮（花瓣/logo/表情）时保持三层景深 + 网格保底两条铁律，

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/transition/bubble-swarm-takeover/BubbleSwarmTakeover.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
