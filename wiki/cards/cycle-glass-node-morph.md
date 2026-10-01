# cycle-glass-node-morph

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/cycle-glass-node-morph`.

## Identity

- **slug**: `cycle-glass-node-morph` (join key across cards, demos, media and deep links)
- **category**: `data` — Data & Metrics / 数据与指标
- **energy**: `中高` — rank 5/8
- **suggested duration**: 约 8.6s（257f@30fps；最终状态保留 34f） → **257 frames @30fps = 8.6s**
- **cross-category tags**: `camera`, `data`, `interaction`
- **upstream source**: references/shots/data/cycle-glass-node-morph.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `cycle-glass-node-morph` | 257f | A | `demos/data/cycle-glass-node-morph/CycleGlassNodeMorph.tsx` |

## What it does

单一主体在对角擦除中缩入机制图，三段循环标签沿弧线依次建立，连续推近时三枚玻璃节点从下方托起并接管原标签，最后诊断标记错峰钉住系统状态

**When to use it.** AI agent/自动化/控制系统的感知—推理—执行循环；“一个对象背后有三段机制”的解释镜头；从真实场景过渡到抽象系统图的技术型 B-roll

**Why this shot earns its place.** 循环图最容易沦为“画三个圆加两支箭头”。本卡把机制解释建立在一个连续主体上： 主体不是被另一份灰阶副本替换，而是在对角擦除发生时同步缩入系统中心；循环文字先作为 黑色概念标签出现，推近后玻璃节点从它们下方升起，把同一标签转为白色节点标题。 观众因此读到的是**场景里的对象被解释成一套运行机制**，而不是切到另一页 PPT。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 场景 hold | f0–61 | 至少留 1.5s 看清主体；缩短后会像片头缓冲失败 |
| 主体缩入 | f62–94，宽 332→154px | **命门**：始终是同一个主体对象；复制一份灰阶主体叠化会破坏连续性 |
| 对角擦除 | f66–90，135° 硬边 gradient stop -40%→140% | 擦除线必须越过两个对角并与主体缩入同时发生；提前结束会露出“双世界”接缝 |
| 标签节奏 | f124/129/134 起，七帧闪现后锁定 | 闪现只是“系统识别”口吻；全程随机 glitch 会牺牲可读性 |
| 弧线建立 | f127–176 | 约 1.6s 的持续生长让观众能顺着关系读；压到 20f 只剩装饰扫线 |
| 连续推近 | f176–198，scale .61→1 | 中间关键帧不得做 hold；分三段 easing 后速度归零会产生三次启停 |
| 节点顶起 | f184/192/200 起，各 8f，rise 86px | 每枚只允许一次越位回落；三枚同时弹出会丢掉阅读顺序 |
| 诊断标记 | f208/213/217 起，5–6f | 标记是收尾证据，不与节点共享 transform，避免“整组一起弹” |
| 最终 hold | f222–256 | 34f 是三段机制通读时间；若标签更长，优先延长总时长 |

## Known pitfalls

- 对角擦除边界必须从画外进入并越过另一侧画外；只插值 0%→100% 会在起止帧残留旧场景角落
- 主体、背景圆、弧线和标签的 z-index 必须明确：主体在圆上、弧线在圆上但不盖主体、节点最后压过标签
- 玻璃节点需要真实 `backdrop-filter`、内高光与外阴影三层质感；单一半透明灰填充会像普通圆形按钮
- 标签变白必须只发生在玻璃圆覆盖区域。demo 用节点内同文白字模拟；落地到长标签时应使用圆形 mask 裁切同一文字层，避免双文本错位
- 推近作用于机制组，不作用于开场背景和对角擦除层；把整画面一起缩放会让转场边界漂移
- demo 为原创通用 DOM/SVG 重构，不含参考研究中的车辆、品牌、道路或 UI 资产

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/data/cycle-glass-node-morph/CycleGlassNodeMorph.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
