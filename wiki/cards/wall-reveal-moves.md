# wall-reveal-moves

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/wall-reveal-moves`.

## Identity

- **slug**: `wall-reveal-moves` (join key across cards, demos, media and deep links)
- **category**: `ui-entrance` — UI Entrance & Showcase / 界面登场与陈列
- **energy**: `中` — rank 4/8
- **suggested duration**: 单式约 4.3–5s（A 150f / B 130f / C 150f @30fps，含建立 hold 与静止收尾） → **150 frames @30fps = 5.0s**
- **cross-category tags**: `ui-entrance`
- **upstream source**: references/shots/ui-entrance/wall-reveal-moves.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| A | `bento-light-up` | —f | B | `demos/ui-entrance/wall-reveal-moves/BentoLightUp.tsx` |
| B | `grid-wave-flip` | —f | B | `demos/ui-entrance/wall-reveal-moves/GridWaveFlip.tsx` |
| C | `wireframe-draw-on` | —f | B | `demos/ui-entrance/wall-reveal-moves/WireframeDrawOn.tsx` |

## What it does

整墙批量入场三式——bento 逐格点亮、网格波浪翻面、蓝图描线成形，全部原位显形不位移，与 deck-deal-flyin 的飞入位移型互补成品类矩阵

**When to use it.** 功能墙/卡片墙/整页界面的整体亮相；内容已在原位、要"显形"而非"涌入"的段落

**Why this shot earns its place.** "一墙内容怎么出场"库内此前只有 deck-deal-flyin 一个答案——高能量、位移型、 "东西涌进来"。但不是每面墙都该涌：品牌段要庄重、功能墙要轻快、 "从设计到实物"要讲工序。这三式共同点是**非位移批量入场**——元素原地显形， 版式从第一帧就成立，观众看的是"状态变化的波前扫过一面墙"而不是"物体飞行"。 选型先问一句：这面墙该"涌进来"还是"亮起来"？前者去 deck-deal-flyin，后者进本卡。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| A 节拍 | hold 20f → 每格间隔 12f 依次激活（六格 ~96f 全亮）→ scale 1→1.04 缓推 25f（bezier 0.33,0,0.2,1）→ 静止收尾 | 12f 级联是"逐格可辨"与"整墙拖沓"的平衡点；格数增多可压到 8–10f，但间隔均匀本身就是这一式的庄重感来源，别学发牌加速 |
| A 单格 | 暗态 opacity 0.18 + translateY 20px；SVG rect pathLength=100 + dashoffset 描边 8f（强调色 #e8b45e 4px + drop-shadow 辉光）；描边过半（+6f）内容 back-out(0.3,1.4,0.5,1) 弹出 8f 提亮归位；描完 +12f 流光退火到 0.4 常亮细边 | 描边与内容弹出要**接力不同步**——同帧起读作整格闪现；点亮中段辉光脉冲用 lit·(1−lit)·4 抛物线，峰值幅度按格 seed 微差（正弦哈希，禁真随机） |
| B 波前 | hold 20f → delay=(row+col)*6f 对角线步进，每张 rotateX 0→180° 翻 14f bezier(0.35,0,0.25,1)；尾张冲到 190° 再 8f 弹回 180° | (row+col) 是对角波的灵魂，换 row 或 col 单向扫立刻平庸；只给尾张过冲——张张过冲读作整墙果冻 |
| B 翻面结构 | 共享 perspective 1200px 容器（整墙一个消失点），每张双面卡 preserve-3d：灰背朝外 + 正面预转 rotateX(180°)，两面都 backfaceVisibility hidden | perspective 加在墙容器不是单卡上，否则九个消失点各翻各的；翻到 90° 最薄处叠一道 4px 白色高光线（不随卡旋转、贴格位随角度 45°→135° 从上缘扫到下缘，opacity=1− |
| C 描线 | hold 20f → 分组错峰各 30f 描完：侧栏 20f 起/顶栏 30f 起/6 卡 40+i*3f 起/折线图 52f 起；SVG pathLength=1 + dashoffset 1→0，描边 #8f8f8d 2.5px round | 分组错峰是"手在画"的感觉来源，全部同帧起笔读作打印机；卡内占位线再按 +3f 细错峰，长短用 seed 哈希微差 |
| C 实体化 | 88–118f 实体层 clip-path inset(0 right% 0 0) 从左向右展开 30f，bezier(0.55,0,0.25,1)；前沿跟 4px 强调色竖线（#ffc46b + 双层辉光 boxShadow），86–92f 淡入、112–120f 淡出 | 竖线位置与 clip 前沿必须同一个 scan 值驱动，异步读作穿帮；描线段与扫描段之间留 ~6f 喘息（82→88f），线框画完立刻扫读作赶工 |
| 静止收尾 | 三式动作全部落定后真静止 ≥15f（A 在缓推结束后、B 在尾张回弹后、C 在扫描线淡出后起算） | R1 呼吸判例：静止期一切属性锁死，包括辉光/阴影/高光残留 |

## Known pitfalls

- **demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- A/C 的强调色描边/扫描线属"单点高质量光效"范畴（Q4 三约束内合规），但一支片 _(rules Q4)_
- B 式翻面后的正面实战要接真实截图：backface 侧预留高清纹理（Q2），翻转中 _(rules Q2)_
- C 式线框几何必须与实体层布局逐像素对位（demo 里按 FakeDashboard A 手排），
- 三式都是"原位显形"，别混入位移入场（如 B 翻面时再加 translateY 飞入）——
- A 式暗态 opacity 0.18 依赖暗底（#2a2a28）成立，亮底下压暗读作褪色故障

## Card structure

`intention` | `variants` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/ui-entrance/wall-reveal-moves/BentoLightUp.tsx`
- `demos/ui-entrance/wall-reveal-moves/GridWaveFlip.tsx`
- `demos/ui-entrance/wall-reveal-moves/WireframeDrawOn.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
