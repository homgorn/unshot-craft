# orbit-ring-title-open

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/orbit-ring-title-open`.

## Identity

- **slug**: `orbit-ring-title-open` (join key across cards, demos, media and deep links)
- **category**: `opening` — Opening & Brand / 开场与品牌
- **energy**: `中` — rank 4/8
- **suggested duration**: 约 4.3s（130f@30fps；标题落定 f50 到退场 f108 之间是 1.9s 稳态巡回） → **130 frames @30fps = 4.3s**
- **cross-category tags**: `opening`, `ui-entrance`
- **upstream source**: references/shots/opening/orbit-ring-title-open.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `orbit-ring-title-open` | 130f | B | `demos/opening/orbit-ring-title-open/OrbitRingTitleOpen.tsx` |

## What it does

八张 16:9 内容卡按 45° 均布在 700×375 椭圆上匀速公转（卡身永不倾斜，纵深只由 sin θ 给出 ±9% 缩放与 z 序），环撑开期间卡内容冻结首帧、f24 之后八张一起开播；居中标题逐字解糊下沉落定，关键词到位那一刻黄色马克块自左横扫铺满，mono 副行随后浮出，末段整行失焦淡出、环继续转着交棒下一镜

**When to use it.** 开场第一镜 = 「这个产品有一整套东西」；素材库/模板库/功能矩阵/案例集的门面拍；需要用真实运动的产品画面托住一句主张，而不是把截图摆成静态九宫格

**Why this shot earns its place.** 开场想说"我们有一整套东西"，最常见的做法是把截图排成网格——但网格是静止的，观众 读到的是"一堆图片"，不是"一套会动的产品"。这张卡把陈列改成**环形巡回**：八张卡沿 椭圆匀速公转，永远有卡在进画、有卡在出画，画面自带"还有更多"的暗示，而标题稳稳 钉在正中间不受影响。 关键的取舍是**卡内容要真的在播**。静态截图上环，观众只会认出"轮播图"；卡里跑着真 动效，同一个环立刻变成"产品在工作"。但八张卡同时开播会八个动效抢戏，谁也读不进去 ——所以入场期把卡内容**冻结在首帧**，等环撑开、标题起手之后再统一开播。观众的注意 力顺序因此是：先认出这是一圈产品画面 → 读标题 → 才注意到卡里都在动。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 椭圆半径 | RX=700 / RY=375（卡 380×214） | RY/RX≈0.54 是"俯视环"的甜点；比值 →1 读作正圆转盘，→0.3 卡会在上下缘挤成一条 |
| 卡数 | 8（方位角间隔 45°） | 8 张在这个半径上任意转角互不遮挡；≥10 张必须同步加大 RX/RY，否则近处卡压边 |
| 公转速度 | 0.3 rad/s（4.3s 转约 74°） | **别因为"看起来慢"就调快**：>0.5 rad/s 时卡扫过画面边缘会有频闪感，且喧宾夺主 |
| 环入场 | f0–21，scale .62→1，outCubic | <15f 像弹窗；>30f 标题起手时环还在长，两件事互相盖 |
| 逐卡淡入 | 窗口 `[0.06+0.05i, 0.42+0.05i]`s | 步长 0.05s 刚够读出"依次"；>0.1s 最后一张会晚到标题之后 |
| 开播帧 | PLAY_START=24f | 必须 ≥ 环撑开结束帧；提前会让八个动效在入场期一起抢戏 |
| 纵深缩放 | ±9% | >15% 顶部卡会缩成图标，环读作"透视隧道"；=0 则整环扁平，失去前后关系 |
| 标题 | 64px / 600 字重 / 字距 −0.05em | 环一直在动，标题必须够重才压得住；<48px 或 400 字重会被环吃掉 |
| 逐字节奏 | lead .35s，解糊 .9s，下沉 .3s，错峰 1f | 错峰 1f 是"整体解糊"的手感；≥3f 会读成逐字打字机 |
| 马克块 | f40 起，spring damping 14，#facc15 | damping <10 会回弹出色块边缘；起扫早于末字 ease 0.9 时读作"色块追着字跑" |
| 副行 | mono 28px，字距 0.35em，1.0–1.5s 淡入 | 大字距 mono 是"产品代号"的读法；跟标题同字体会读作第二行标题 |
| 退场 | f108–118，blur 0→6.5px | 整行统一失焦；**逐字退场会读作第二次入场** |

## Known pitfalls

- **卡不能跟着 θ 倾斜**。给卡加 `rotate(θ)` 后环立刻从"陈列"变成"过山车"，而且卡内
- 卡内容首帧必须自带静态骨架（底色/边框/标签/灰底轨迹）。冻结期显示的就是第 0 帧，
- `zIndex` 必须跟着 depth 走。只做缩放不排 z 序时，DOM 顺序会让后面的卡压住前面的，
- 马克色块和字的层级是一对：色块 `zIndex:0` + 字 `position:relative; zIndex:1`。漏掉
- 标题 `white-space: nowrap` 是马克块的前提——`inset:.06em -.08em` 假设高亮词组在同
- 环是背景层但它一直在动，所以**不要在环上再叠第二个动的东西**（粒子、扫光、渐变
- 与 `carousel-3d` 的分工：那张卡是真 3D（`rotateY + translateZ` + backface-hidden），
- demo 的八张卡是原创通用 DOM 占位（灰阶骨架 + 一条强调色），不含任何产品截图；

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/opening/orbit-ring-title-open/OrbitRingTitleOpen.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
