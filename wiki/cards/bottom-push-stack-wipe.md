# bottom-push-stack-wipe

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/bottom-push-stack-wipe`.

## Identity

- **slug**: `bottom-push-stack-wipe` (join key across cards, demos, media and deep links)
- **category**: `transition` — Transitions / 转场
- **energy**: `中` — rank 4/8
- **suggested duration**: 单次推入 30f + 章内 hold ~1s；demo 三连推 140f（~4.7s） → **30 frames @30fps = 1.0s**
- **cross-category tags**: `transition`
- **upstream source**: references/shots/transition/bottom-push-stack-wipe.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `bottom-push-stack-wipe` | 30f | B | `demos/transition/bottom-push-stack-wipe/BottomPushStackWipe.tsx` |

## What it does

底边上推换章——新场景连底色整屏从底边向上推入，把旧场景物理顶出画外，连推数章各配一种饱和底色，内容钉死在各自色底坐标系里随底色走

**When to use it.** 多章节产品片的换章骨架（每章一个卖点一种底色）；需要"翻页节奏感"贯穿全片的段落切换

**Why this shot earns its place.** wipe-transitions 是一条边界扫过、新旧页都不动；page-turn 是立方体 翻转。本卡是第三种物性：**新章把旧章顶出去**——两屏刚性接触、同速 同向位移，像自动售货机压栈。命门是"连底色整屏走"：底色+窗口卡+装饰 条焊成一块整料从底边推入，观众读到"换了个世界"而不是"换了张卡"。 重 ease-out（快进慢停）给推入一个"哐"的落位感；上缘 40px 接缝阴影 是两屏物理接触的证据。连推三章且底色饱和度拉满，换章本身就成了全片 的节拍器——slack 原片全片就靠这一招做骨架。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 推入时长 | 30f，重 ease-out | <20f 读作闪切；线性匀速读作卷帘门，"哐"感全无 |
| 章间 hold | ~37f（1.2s 左右） | 章内是内容表演区，<25f 观众没看清就被顶走 |
| 接缝阴影 | 上缘 40px，黑 0.30 渐变 | 去掉后两屏像叠影滑动；>80px 读作新章自带黑边 |
| 底色 | 每章一种饱和色，相邻章色相拉开 | 相邻章同色系则"换章"读作"微调"；灰阶章只能当第 0 章 |
| 内容钉死 | 窗口卡/装饰条用章内绝对坐标 | 内容若相对视口定位就会"漂"在推入动画上，穿帮 |
| 连推次数 | 2–4 章 | 1 次不成节奏；>4 次观众开始数底色，疲劳 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 与 wipe-transitions 分工：那卡新旧页都不动、一条几何边界扫过交接
- 与 shot-transitions 六式同层选型：本卡能量中档、方向固定向上，
- 方向统一是骨架感的来源：全片所有章都从底边推，中途换成左推/顶推
- 推入进行中两章同屏，都是满屏层——章内动画（卡片入场等）避开推入
- 实战底色用品牌色板的饱和档；底色饱和度不足时窗口卡"钉在色底上"

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/transition/bottom-push-stack-wipe/BottomPushStackWipe.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
