# segmented-thumb-hero

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/segmented-thumb-hero`.

## Identity

- **slug**: `segmented-thumb-hero` (join key across cards, demos, media and deep links)
- **category**: `interaction` — Interaction & Feature Demo / 交互与功能演示
- **energy**: `中` — rank 4/8
- **suggested duration**: ~3.5s（demo 110f：浮入 18f + 光标 24f + 点击 + 滑动 8f + 图标弹出 + hold） → **110 frames @30fps = 3.7s**
- **cross-category tags**: `interaction`
- **upstream source**: references/shots/interaction/segmented-thumb-hero.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `segmented-thumb-hero` | 60f | B | `demos/interaction/segmented-thumb-hero/SegmentedThumbHero.tsx` |

## What it does

分段控件 thumb 位移当主角特写——超大胶囊 segmented control 弹簧浮入，描边箭头光标画外滑入按下，白 thumb 8f ease-out 滑到另一段，到位瞬间新图标 spring 弹出、旧图标收起

**When to use it.** "模式切换/二选一"功能的宣告镜头（Ask→Computer、Chat→Agent 式）；一个 UI 微交互撑一整镜的特写拍法

**Why this shot earns its place.** 产品切到新模式，通常拍法是整个界面换掉。本卡反着来：把 segmented control 放大到 1080px 宽拍特写，**thumb 那 8 帧位移本身就是叙事**—— "我们从 A 走到了 B"。没有任何页面上下文，控件即舞台。因果链完整： 光标滑入（有人来了）→ 按下+涟漪（做了决定）→ thumb 滑动（世界响应） → 新图标弹出（新身份确立）。四拍缺一不可，缺了光标就是 UI 自己在动， 缺了图标弹出就是切换没有奖励。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 控件尺寸 | 1080×220，thumb 内缩 16px | 缩到 <600px 宽就不是特写了，thumb 位移读不出重量 |
| thumb 时长 | 8f Easing.out(cubic) | >14f 读作慢动作演示视频；<5f 读作瞬移，"滑"没了 |
| 光标滑入 | 24f 从画外，ease-out | linear 或 <14f 读作光标被扔进来；起点必须画外 |
| 按下 | scale 0.86 + 涟漪 12f | 无按下直接滑 thumb，因果链断，读作自动播放 |
| 图标弹出 | spring damping 10/stiffness 220 | damping <8 弹三下抢 thumb 的戏；旧图标不收起文字会挤出控件 |
| 收尾 hold | 新态静置 ≥30f | 切换完立刻切镜，"新模式"没被看清 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 与 input-trigger-moves 分工：cursor-performance 是光标在完整页面里
- 图标塌缩用 width 归零而不是只 scale——只 scale 会留空位，文字不回流，
- 二段以上（3+ 段）控件慎用：thumb 跨多段滑行 8f 太快读不出停靠，
- 涟漪圆环要 zIndex 压在 thumb 之上、圆心锁点击点——跟着 thumb 走
- 实战替换素材：段标签/图标换成真功能名即可，但"新段图标带表情"

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/interaction/segmented-thumb-hero/SegmentedThumbHero.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
