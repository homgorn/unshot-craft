# graze-face-tour

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/graze-face-tour`.

## Identity

- **slug**: `graze-face-tour` (join key across cards, demos, media and deep links)
- **category**: `camera` — Camera & Space / 运镜与空间
- **energy**: `中高` — rank 5/8
- **suggested duration**: 单段 4–5s；可多段接力延长 → **150 frames @30fps = 5.0s**
- **cross-category tags**: `ui-entrance`, `camera`
- **upstream source**: references/shots/camera/graze-face-tour.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `graze-face-tour` | —f | B | `demos/camera/graze-face-tour/GrazeFaceTour.tsx` |

## What it does

大倾角贴面游走特写——镜头贴着 UI 表面低飞掠过（侧栏树/顶栏/列表当地形），页面文字初始悬浮在界面上空带同形软影，随镜头行进先后加速贴落回界面

**When to use it.** 功能区巡礼（把 UI 当地景飞掠）；配合暗场+霓虹缘光做产品"内部世界"段落；界面内容逐区登场

**Why this shot earns its place.** 把 UI 拍成地形：大倾角特写让侧栏树、导航、列表行变成掠过的地貌， 浅景深强化"贴面"。戏眼是**文字空中贴落**：文字/组件不是原地淡入， 而是悬浮在界面上空（3D z 轴抬高），在空中时往界面投同形软影， 随镜头行进先后加速贴落、影子随高度收敛消失——观众看见界面在 镜头经过时"完成自己"。影子是可感命门：没有影子，悬浮读作 普通位移入场；有影子，空间关系瞬间成立。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 悬浮高度 | 120–180px | <80px 影子和位移都读不出；>250px 落地砸得太重 |
| 影子参数 | blur/offset/opacity 随高度线性收敛 | 影子恒定不随高度变＝贴纸感；落地影必须归零 |
| 贴落错峰 | 按镜头行进方向 0.2→0.85 归一化排布 | 同帧齐落读作开关；乱序落读作 bug；**错峰=错开起点但下落过程重叠并行**，串行等待（一个落完另一个才开始）被裁（runway 判例） |
| 下落曲线 | easeFall 加速+软着陆 | ease-out 下落读作气球飘落，重力感靠加速 |
| 段间接力 | 相邻段交叉淡化 ≥8f | 透明度窗口不搭接会黑闪（返工判例 f100 纯黑帧） |
| 景深 | 远处 blur 渐强 | 全清晰读作平面滚动，浅景深才有"贴面"体感 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 悬空元素别被环境压黑带吞掉（邻候选 runway 判例）：空中元素
- 与 space-camera-moves/tension-camera-moves 分工：那两张是相机
- **贴落节奏语义判例**（与 neon-frame-orbit-drop 互为反例）：
- 原片（clickup-30）是一条连续上行长镜；复刻用三段接力，段落

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/camera/graze-face-tour/GrazeFaceTour.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
