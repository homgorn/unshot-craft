# ring-diagram-annotation-reveal

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/ring-diagram-annotation-reveal`.

## Identity

- **slug**: `ring-diagram-annotation-reveal` (join key across cards, demos, media and deep links)
- **category**: `data` — Data & Metrics / 数据与指标
- **energy**: `中高` — rank 5/8
- **suggested duration**: 约 6.3s（190f@30fps；最终构图保留 30f 可读时间） → **190 frames @30fps = 6.3s**
- **cross-category tags**: `ui-entrance`, `camera`, `data`
- **upstream source**: references/shots/data/ring-diagram-annotation-reveal.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `ring-diagram-annotation-reveal` | 190f | A | `demos/data/ring-diagram-annotation-reveal/RingDiagramAnnotationReveal.tsx` |

## What it does

全屏主体被圆形窗口收束成同心环图解，分段外环与 12 支向心箭头建立机制，整组随后左移缩小并为四块标题和两级注释让出右栏

**When to use it.** 把抽象名词解释成结构图；系统/装置/流程的“主体→机制→注释”镜头；需要先制造沉浸特写、再退成可读说明图的横屏 B-roll

**Why this shot earns its place.** 直接出现一张环形图，观众只会把它当作静态信息图。本卡先让主体占满全画面，再用 收缩的圆形窗口把“内容”压成一个可分析对象；细环、分段环与向心箭头依次补齐机制， 最后整组退到左侧，右栏才给出名称和解释。视觉顺序因此是**先经历对象，再理解结构， 最后阅读定义**，适合科技、工程、数据和概念科普。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 圆窗收束 | f11–50，半径 540→61px（480×270 设计坐标） | 终点半径必须刚好包住内容圈；过大会失去“聚焦”，过小会切主体 |
| 细环收缩 | f18–60，scale 3.8→1 | 比圆窗晚起、晚收，形成两层深度；与圆窗同帧同速会粘成一层 |
| 分段环 | f30–50，204px，7px dashed border | dash 数量要稀疏可数；太密会读作普通虚线描边 |
| 外环旋转 | f29–187，总计 44.2° | **命门**：仅外环旋转；箭头跟转会把“向心关系”变成装饰转盘 |
| 向心箭头 | 12 支，f35–50，97→72px | 线端和箭头头必须一起推进；头先到、线后长会穿帮 |
| 布局让位 | f90–134，x -86px，scale 1→.84 | 移动和缩放必须共享一条进度，否则同心结构会漂 |
| 标题错峰 | f112 起，每块间隔 3f，单块 8f | 间隔 >6f 会像逐字点名；0f 同时出现则失去“命名被拼出”的节奏 |
| 最终 hold | f160–189 | 可继续保留外环慢转，但文字、主体和箭头必须完全静止 |

## Known pitfalls

- 圆窗半径大于画幅时 CSS `circle()` 仍要以同一中心计算；改分辨率时不要用宽度百分比近似，否则开头边角会提前露白
- 分段外环、细环和箭头是三层独立几何；合并成一张旋转 PNG 会让箭头也跟着转，破坏机制语义
- 布局左移后再单独定位右栏，不能把右栏放进同一 transform 容器，否则标签会跟着缩小漂走
- 四块标题是四个独立运动单元，不代表必须使用四个汉字；落地时可换四段短词、四个图标或四枚状态块
- 终段只允许外环的低速持续运动；标题 glow、箭头呼吸或多点闪光会把解释镜头做成廉价 HUD
- demo 为原创灰阶 DOM/SVG 重构，不包含研究参考中的品牌、装置图片或文字资产

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/data/ring-diagram-annotation-reveal/RingDiagramAnnotationReveal.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
