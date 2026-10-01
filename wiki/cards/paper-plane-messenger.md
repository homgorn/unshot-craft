# paper-plane-messenger

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/paper-plane-messenger`.

## Identity

- **slug**: `paper-plane-messenger` (join key across cards, demos, media and deep links)
- **category**: `transition` — Transitions / 转场
- **energy**: `中` — rank 4/8
- **suggested duration**: ~5s（150f：点击 12f → 拉远 16–42f → 飞行 34–104f → B 接管 112–146f） → **150 frames @30fps = 5.0s**
- **cross-category tags**: `camera`, `transition`
- **upstream source**: references/shots/transition/paper-plane-messenger.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `paper-plane-messenger` | —f | B | `demos/transition/paper-plane-messenger/PaperPlaneMessenger.tsx` |

## What it does

纸飞机信使转场——点击"发送"后镜头拉远脱离窗口 A，折纸飞机沿贝塞尔弧线飞出（俯仰跟随切线），镜头伴飞穿过多层视差道具，飞抵窗口 B 门前落定，B 放大接管全屏

**When to use it.** "发送/邀请/分享"动作连接两个人物/场景视角的叙事转场；抽象动作需要一个隐喻实体当转场载具时

**Why this shot earns its place.** transition-travel 是镜头钻进画面里的既有元素换景；本卡反过来——从 动作里**放出一个语义信使**，让镜头跟着它飞去下一个场景。"发送"这个 抽象动作被实体化成折纸飞机，A/B 两窗的空间关系被飞行轨迹真实丈量 过，观众对"消息去了哪"有了身体感。命门是 2.5D 相机管线：所有元素 挂在同一世界坐标系上，镜头中心 A→跟飞机→B、变焦拉远再推近，视差 道具按 depth 乘相机位移——重 3D 原片降级成一台"假三维"，成本掉一个 量级而纵深感保留。飞机俯仰角跟随弧线切线是"它在飞"而非"它在平移" 的全部区别。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 变焦三段 | 1.55 → 0.62 → 3.1 | 不先拉远直接跟飞，观众不知道 B 在哪个方位；拉远 <0.7 才装得下旅程感 |
| 飞行时长 | 70f，ease-in-out | <45f 读作弹射；匀速读作拖拽平移 |
| 切线采样 | dt = 0.012 | 太大角度滞后、太小抖动；俯仰角是"飞"的命门，删掉立即变贴图滑动 |
| 途中放大 | ×1.7（0.25–0.75 区间），落定 ×1.1 | 拉远后飞机只剩几十像素，不放大就丢主角 |
| 视差层 | depth 0.45/0.75/1.3，远 blur3 近 blur8 | 全同 depth 就没有穿越感；近景不虚会抢飞机视线 |
| B 接管 | 112–146f，变焦推到 3.1，道具/飞机同步淡出 | 道具不淡出会在推近时变成巨大糊块扫过全屏 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 与 transition-travel 分工：那卡钻进**画面里既有的**元素/容器完成
- 与 glow-flyline-moves B（flyline-arc）分工：飞线是暗场数据流向的
- 信使实体必须来自动作语义（发送→纸飞机、上传→气球、部署→火箭），
- 相机三段（拉远/伴飞/接管）的切换帧上中心与变焦都要连续——demo 里
- 2.5D 的极限：道具只能是剪影级形状，写实道具会暴露"没有真透视"；

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/transition/paper-plane-messenger/PaperPlaneMessenger.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
