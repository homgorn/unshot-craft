# dataviz-landscape-open

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/dataviz-landscape-open`.

## Identity

- **slug**: `dataviz-landscape-open` (join key across cards, demos, media and deep links)
- **category**: `opening` — Opening & Brand / 开场与品牌
- **energy**: `低开缓升` — arc or n/a, not sortable
- **suggested duration**: 5–8s（开场氛围段，一支片 ≤1 次） → **240 frames @30fps = 8.0s**
- **cross-category tags**: `opening`, `camera`, `data`
- **upstream source**: references/shots/opening/dataviz-landscape-open.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `dataviz-landscape-open` | 165f | B | `demos/opening/dataviz-landscape-open/DatavizLandscapeOpen.tsx` |

## What it does

暗场支流线束地景开场——多条流线汇入主干、虚构 ID 标签浮在线上、相机重景深低速飞越

**When to use it.** 品牌级抽象开场（"数据宇宙"隐喻），接亮场产品段或字标；与 glow-flyline-moves 分工：那卡是段落内卡片之间的连线叙事，本卡是开场专用的全画幅地景

**Why this shot earns its place.** Linear Releases 发布片开场实证的品牌级开场品类：把产品背后的数据世界 拍成一片**暗场地景**——支流线束从画面深处汇入一条主干（"无数工作流 汇成一个产品"的隐喻），真实感来自三样东西：①虚构 issue/任务 ID 标签 浮在线上（观众认出"这是我每天看到的那种东西"）；②重景深——近景大虚焦 流过、中景标签清晰可读、远景渐隐，三层纵深让平面 SVG 读作空间； ③相机低速匀稳飞越——这是氛围段不是炫技段，速度感交给后面的镜头。 手搓 UI 合规依据：非复刻场景（页面上不存在此画面），按核心理念 1 修订版走质量+表达明确性门槛。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 线束规模 | 支流 8–14 条汇入 1 条主干；分层 近 2–3 / 中 5–8 / 远 4–6 | 超过 ~16 条读作屏保/科技模板；主干必须唯一（单主角原则的地景版） |
| 汇流拓扑 | 支流以 bezier 切向汇入主干（切线连续），汇点偏画面一侧 1/3 处 | 垂直相交读作电路图不是水系；汇点居中构图死板 |
| 景深三层 | 近景 blur 10–16px + 线宽 6–10px + 亮度 0.15–0.25；中景清晰 2–3px 亮度 0.5–0.8;远景 1–1.5px 亮度 0.2–0.35 | 近景不虚焦则三层塌成一张平面图；远景过亮抢中景 |
| 相机飞越 | 世界画布 ≥2× 视口，横移速度 2–5px/f 匀稳 + 视差（近 1.4×/中 1×/远 0.6×），可叠极缓 zoom 1.0→1.06 | 快了变追逐镜头（那是 crash-zoom 的活）；无视差立刻穿帮为平面滚动 |
| 视差可见性 | 近/远层线条必须与运动方向成角（斜率明显）或带画内可见特征点（端点/交叉/节点标记穿过画面） | **平行于运动方向的线横移时沿自身滑动，视差机制再对也不可见**（L2 评估判例：0.6×/1×/1.4× 全写对，正常播放只有中景在动） |
| 流动感 | draw-on 完成后线条保持"活"：沿线明暗脉冲/虚线相位低速漂向汇点（速度 1–2px/f，透明度 ≤0.3 叠加） | 生长期结束后无流动元素，后半段退化成"路线图飞越"不是"数据流" |
| 标签 | 中景层 5–9 枚：方块图钉 + 等宽字 ID（如 APP-1843），错峰 6–10f 间隔淡入 + 沿线微漂 | ID 一律虚构（合规底线）；标签挂近景/远景层会因虚焦/过暗不可读；图钉方块要落在线上（钉线分离读作浮尘不是锚点） |
| 生长节奏 | 主干 30–40f out-cubic 先行，支流每条错峰 3–6f | 全部同帧生长读作 loading 动画 |
| 收尾 | 交棒帧前 ≥15f 标签停止新增、相机斜率连续（不急刹） | 氛围段急刹是一次可见的顿挫（glow-orb 收敛判例同源） |

## Known pitfalls

- 借鉴来源：Linear Releases 开场（进化轮 #3 breakdown #7），单例样本
- 与 glow-flyline-moves 别混用在相邻段落：两卡都是"暗场发光线"，
- 暗场进出成本同 glow 卡：接亮场产品段用 shot-transitions 藏切族垫，
- 线条纯白全亮会糊成蛛网——亮度按层拉开（见参数表），中景才是主角层；
- 标签字号在目标画幅下 ≥18px 等效，否则"可读"沦为装饰噪点（Q6 同源） _(rules Q6)_
- 声音：铺 riser/低频 pad 底噪，标签浮现不逐枚打点（批量不逐个发声，

## Card structure

`intention` | `phases` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/opening/dataviz-landscape-open/DatavizLandscapeOpen.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
