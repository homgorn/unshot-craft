# space-camera-moves

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/space-camera-moves`.

## Identity

- **slug**: `space-camera-moves` (join key across cards, demos, media and deep links)
- **category**: `camera` — Camera & Space / 运镜与空间
- **energy**: `高` — rank 6/8
- **suggested duration**: A 5s（炸开-悬停-合体全程）；C 3–5s 单向俯冲 → **150 frames @30fps = 5.0s**
- **cross-category tags**: `camera`
- **upstream source**: references/shots/camera/space-camera-moves.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| C | `drone-dive-landing` | 45f | B | `demos/camera/space-camera-moves/DroneDiveLanding.tsx` |
| A | `exploded-view` | —f | B | `demos/camera/space-camera-moves/ExplodedView.tsx` |

## What it does

3D 空间化运镜两式——exploded-view 爆炸分解（构件沿 Z 炸开再合体）、drone-dive-landing 无人机俯冲降落

**When to use it.** 把平面页面当 3D 实体拍的高光段落；两式都是"大动作"，一支片合计 ≤2 次

**Why this shot earns its place.** depth-layer 卡是给平移加纵深——层在动、页面还是页面。这两式更进一步： 整页被当成一个 3D 实体，相机（或世界）绕着它做实拍级机动。两式叙事 语义各占一格：A 说"看看它由什么组成"（拆解展示，Apple 发布片语言）； C 说"从全局俯瞰砸到主角"（上帝视角一头扎进 hero 特写，全景→焦点）。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| A 空间基座 | perspective 1600 + 整组 scale 0.76 + rotateX 18° rotateY -12° + preserve-3d | 倾角是空间感来源；正视炸开读不出深度 |
| A 炸开 | 各构件 translateZ 60–320px 错落分布，错峰 3f，每层 14f ease-out-back(1.7) | back 回弹给"咔"一声的机械感；深度全同读作整页浮起 |
| A 合体 | 逆序 ease-in 12f，归位帧 2f 指数衰减震屏（幅 ~13px） | 震屏是落锤——没有它合体读作软趴趴的淡入 |
| A 深度锚 | 投影随 z·p 下移变虚 + 底板压暗 22% + 远层 brightness ↓28% | 三个线索缺一层间关系就糊 |
| C 行程 | 同一条 p 驱动 rotateX 72°→0 + scale 0.42→1.35 + translate 收拢；origin 钉死 hero 卡中心（如 518,335） | 一条 p = 一台相机一次机动；分开驱动读作三个动画打架 |
| C 速度曲线 | 主俯冲 25f Easing.in(cubic) 吃 82% 行程 → 气垫 20f Easing.out(poly(5)) 走 18% | 切换帧速度骤降 = 气垫顶住的体感；82/18 比例比帧数更关键 |
| C 氛围 | 全场包 CameraMotionBlur(shutterAngle 220, samples 9)；俯视期页面下方椭圆软影随落地收干 | 软影卖"悬空高度"；blur 卖速度，缺一维就假 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 两式都吃真实截图分层/高清纹理：A 需页面按构件切块截图（顶栏/侧栏/
- C 式易错：Remotion 无 Easing.quint，写 Easing.poly(5)（本批实渲踩坑）
- A 式构件布局要绝对定位复刻原页面网格（demo 里 8 层复刻 FakeDashboard

## Card structure

`intention` | `variants` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/camera/space-camera-moves/DroneDiveLanding.tsx`
- `demos/camera/space-camera-moves/ExplodedView.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
