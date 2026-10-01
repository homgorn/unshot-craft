# line-carry-transition

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/line-carry-transition`.

## Identity

- **slug**: `line-carry-transition` (join key across cards, demos, media and deep links)
- **category**: `transition` — Transitions / 转场
- **energy**: `中` — rank 4/8
- **suggested duration**: ~5.3s（进度条走满 + 横移 60f + 围框 + 内容淡入 + 静止 36f） → **60 frames @30fps = 2.0s**
- **cross-category tags**: `camera`, `transition`
- **upstream source**: references/shots/transition/line-carry-transition.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `line-carry-transition` | 3980f | B | `demos/transition/line-carry-transition/LineCarryTransition.tsx` |

## What it does

线条接力横移转场——场景 A 的进度条延伸出画，镜头跟线横移，线在移动中拐角围出场景 B 的卡框，全程无剪切

**When to use it.** 两个有图形亲缘的场景之间（进度条→卡框、下划线→图表轴）；一支片子的招牌转场位，Catch Me If You Can 片头的图形接力

**Why this shot earns its place.** 转场库三大族（穿越/藏切/体块）都在回答"场景怎么换"；本卡的回答是 **根本不换——一条线牵着你走过去**。进度条走满后末端延伸成长线冲出 卡缘，镜头跟着线横移 1920px 进入新世界，线在移动中拐直角围出 B 场景 的卡框，框闭合、内容淡入，从头到尾观众的眼睛没离开过这条线。图形 连续性本身就是转场。与 match-cut 的区别：那是切点两侧形状对位—— 终究还是切；这是连续绘制——**没有切**。线的身份要有叙事逻辑（进度条 "走完了"所以延伸出去），无来由的线只是装饰。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 线体 | 6px ink 实线 | 太细横移中读丢；虚线读作未完成态 |
| 横移配比 | 1920px / 60f（32px/f） | 更远的横移等比拉长时长，别提速——>40px/f 笔头开始拖影跟丢 |
| 笔头位置 | 画面 x≈1500（约 78% 处偏右） | 居中读作"线追镜头"；贴边一颤就出画 |
| 拐角 | 直角硬拐，不倒圆 | 圆角软拐丢掉制图感，Saul Bass 味就没了 |
| 框闭合 | 闭合帧起 B 内容再淡入 | 框没闭合内容先出，线的悬念白搭 |
| 收尾 | 淡入完 ≥36f 真静止 | 笔头墨点必须条件卸载，残留即毁静止 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 与 draw-svg-trace 的关系：那是元素级描边点名（线属于元素），这是
- 全片 ≤1 次——这是招牌转场不是常规转场，第二次出现魔法就穿帮
- 起点必须是已有图形构件的自然延伸（进度条走满、下划线画完），
- 声音：线生长一声持续笔擦、框闭合一声轻叩（sound-design §4.5）

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/transition/line-carry-transition/LineCarryTransition.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
