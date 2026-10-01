# gradient-transition

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/gradient-transition`.

## Identity

- **slug**: `gradient-transition` (join key across cards, demos, media and deep links)
- **category**: `transition` — Transitions / 转场
- **energy**: `低` — rank 1/8
- **suggested duration**: 约 6.0s（180f@30fps；linear 0–2.4s · radial 2–4.2s · conic 4–6s） → **180 frames @30fps = 6.0s**
- **cross-category tags**: `transition`
- **upstream source**: references/shots/transition/gradient-transition.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `gradient-transition` | 180f | A | `demos/transition/gradient-transition/GradientTransition.tsx` |

## What it does

背景在 linear、radial、conic 三类 CSS 渐变间平滑过渡——角度、色标、中心、半径逐参数插值，段间交叉淡化换类型

**When to use it.** 氛围底/章节底色的连续变奏；给静态排版段落提供"活着"的背景层

**Why this shot earns its place.** 渐变不是静态贴图而是可动画的参数集：同类型渐变内部任何参数都能插值出丝滑变化，跨类型则用短交叉淡化衔接。作背景层用，给"没有主体运动"的段落一层持续的低速能量。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 段窗口重叠 | 相邻段起点比前段终点早 0.07 | 重叠保证淡化时两层都在动；无重叠会看到"接管瞬间静止" |
| 交叉淡化 | 0.30–0.38 / 0.63–0.71，各 0.08 | 拉宽会同屏看到两种渐变结构打架；窄淡化 + 参数同动是"换类型不换气"的关键 |
| HSL 插值 | h/s/l 三通道独立 lerp | 色相差 >180° 时会绕远路（如 340→160），需要短路径时给起点 +360 |
| radial 迁移 | 中心对角走位 + 半径近倍扩 | 中心不动只扩半径会读作"呼吸"不是"游走" |
| conic 旋转 | from 0→300°（不满一圈） | 转满 360° 收尾与开头同帧，接循环时用；单次播放留 60° 缺口避免"回到原点"感 |
| 色标组 | 每段两组 HSL 起止 | 换项目色时保持"亮色+暗色"配对结构，radial 外圈必须暗（光斑成立的前提） |

## Known pitfalls

- 这是背景卡：前景放排版/UI 时把 label pill 删掉，并把整层 opacity 压到 0.6–0.8 或叠暗色 scrim，否则彩虹 conic 段会吃掉前景对比度
- CSS 渐变字符串每帧重写触发 repaint 而非 composite——大画幅 + 低端设备需实测；Remotion 服务端渲染无此顾虑
- conic 段的七段色环是"演出"性质，品牌化场景建议换成三色循环（A→B→C→A）
- 三段各自独立可拆用：只要 linear 段（0–0.4 重归一化到 0–1）就是一张"角度扫过"的极简底

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/transition/gradient-transition/GradientTransition.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
