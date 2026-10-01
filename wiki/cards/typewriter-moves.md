# typewriter-moves

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/typewriter-moves`.

## Identity

- **slug**: `typewriter-moves` (join key across cards, demos, media and deep links)
- **category**: `typography` — Typography & Title Cards / 文字与字卡
- **energy**: `A 中高 / B 中低` — arc or n/a, not sortable
- **suggested duration**: A ~5s / B ~5.5s → **150 frames @30fps = 5.0s**
- **cross-category tags**: `opening`, `typography`
- **upstream source**: references/shots/typography/typewriter-moves.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| A | `terminal-typewriter` | —f | B | `demos/typography/typewriter-moves/TerminalTypewriter.tsx` |
| — | `typewriter-error-retype` | —f | B | `demos/typography/typewriter-moves/TypewriterErrorRetype.tsx` |

## What it does

打字机两式——terminal-typewriter 终端命令敲完即引爆场景切换、error-retype 误删重打的"改口"三幕剧

**When to use it.** 开发者产品开场（A）、slogan/卖点字卡（B）；文字自带时间性的入场

**Why this shot earns its place.** 打字是唯一自带时间性的文字入场——字符一个个到来本身就是节奏， 不需要额外动效。A 把打字当**引信**：暗色终端窗逐字敲出命令、 方块光标方波闪，回车帧镜头急推进命令行硬切产品界面，命令行是 场景的导火索，开发者产品标配；B 把打字当**独白**：逐字打出平庸词 （"just a dashboard"）→ 停顿犹豫 → 退格删掉 → 更快打出卖点词 （"your command center"），犹豫-否定-宣言的三幕剧，戏全在三档 速度差里。与 scramble-decode 的区别：乱码解码是机器在猜， 打字是人在说。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 字符节奏 | substring(0, floor((f-起点)/步长))，帧确定无插值 | 任何缓动打字都读作加载动画 |
| A 光标 | 方块，f%12<6 方波 | 淡入淡出的光标不是终端是网页 |
| A 急推 | f58–64 scale 1→3.2 Easing.in(cubic)，origin 钉命令行文字中心 | 幅度小于 3x 读作抖了一下，不是"冲进去" |
| A 硬切 | f64 条件挂载切换（终端整棵卸载，blur 随之摘罩），落定回稳 4f | 交叉溶解毁掉引信-爆炸因果 |
| B 三档速度 | 打 2f/字符、删 1.5f、重打 1.5f 且零犹豫 | 三档差必须可感——等速改口读作 bug 不是戏，命门 |
| B 光标三态 | 打删常亮＝果断；停顿 4f 半周期闪两下＝犹豫；完稿闪两下后条件摘除 | 光标就是演员的脸，全程等速闪就没有"犹豫" |
| B 排版 | 逐字符固定宽 span（58px 等宽），左缘锚定 | 变宽字体/整串测宽会逐帧重排抖动 |
| 收尾 | A 静止 ≥77f / B 静止 ≥50f | 光标残留 0.05 opacity 都毁真静止 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 声音强依赖：键击声逐字符对齐、B 退格音调更低（sound-design
- A 回车急推是与 crash-zoom 的交棒衔接：急推末帧动势最猛处硬切，
- B 全片 ≤1 次——改口是一次性的戏剧转折，改两次口是口吃
- 等宽字体或逐字符 span 二选一必须占一个，否则字符到来时

## Card structure

`intention` | `variants` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/typography/typewriter-moves/TerminalTypewriter.tsx`
- `demos/typography/typewriter-moves/TypewriterErrorRetype.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
