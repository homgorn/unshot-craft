# glitch-cycle

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/glitch-cycle`.

## Identity

- **slug**: `glitch-cycle` (join key across cards, demos, media and deep links)
- **category**: `typography` — Typography & Title Cards / 文字与字卡
- **energy**: `中高` — rank 5/8
- **suggested duration**: 约 5.6s（168f@30fps，4 条短语各 42f） → **168 frames @30fps = 5.6s**
- **cross-category tags**: `typography`
- **upstream source**: references/shots/typography/glitch-cycle.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `glitch-cycle` | 168f | A | `demos/typography/glitch-cycle/GlitchCycle.tsx` |

## What it does

同一行等宽槽位循环轮播 4 条状态短语，每条头尾按概率关键帧 [1,0,0,0.1,0,0,1] 全乱码、中段偶发单字抖动，切换瞬间叠 RGB 分离与整行位移；末条概率收 0 保证收尾干净

**When to use it.** 加载/构建/部署过程的状态播报；技术型片头的"系统自述"；需要机器口吻推进时间的一段垫底

**Why this shot earns its place.** 状态播报最笨的做法是四行字逐条淡入。轮播把它们压进**一个槽位**： 短语头尾用乱码"熔断"再"凝固"，中段几乎干净只偶尔抽一下——观众读到的 是"系统在一步步推进"，而不是四条独立文案。乱码浓度是这卡的语法： 浓 = 正在切换，淡 = 正在这一状态里。底部进度条把四拍串成一条时间线， 最后一条把概率收到 0，落定即结束。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 短语表 | 4 条，最长 17 字符（`COMPILING SHADERS`） | 每条 42f 是"读得完一个状态"的下限；5 条以上单条不足 34f 观众只看到闪 |
| 概率关键帧 | `[1,0,0,0.1,0,0,1]`（6 段） | 中间那个 0.1 是"活着"的证据，删了短语中段死板；把 0 段调到 0.3+ 全片糊成故障 |
| 重掷频率 | 每 2 帧（`floor(frame/2)`） | 1 帧一换糊成灰带；4 帧以上乱码看得清是"另一个词"，不像噪声 |
| 抖动幅度 | `x ±g·10` / `y ±g·4`px | x 大于 y 是横向撕裂的关键（等比抖动读作地震）；>20px 整行跳出槽位 |
| RGB 分离 | 左红右青各 `g·3`px，阈值 g>0.04 | 这是"电子故障"的身份证；无阈值时中段那 0.1 的概率会让字常年带毛边 |
| 槽宽字体 | SF Mono 26px、`letter-spacing:3px`、槽 `0.66em` | 等宽 + 固定槽宽是刚需；字距 3px 让乱码之间有呼吸，挤在一起读作乱码块 |
| 进度条 | 120×2px，`#6c8cff` 填充，线性 | 唯一的线性元素，给四拍噪声一个稳定参照；删了轮播读不出"在推进" |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- **换项目文案时四条短语字符数要接近（demo 12–17 字符）**：槽位数按最长
- 概率关键帧是 6 段等分映射到短语内进度：短语条数变了单条时长跟着变，
- 末条必须用 `KF_LAST`（结尾收 0）：用普通 KF 会让 t=1 停在满乱码上，
- 深底专用：#0a0b10 底 + 冷蓝噪声是整套配色的地基，浅底上 RGB 分离
- 与 scramble 分工：那卡是**一次性解密**（乱→定，不再乱），本卡是

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/typography/glitch-cycle/GlitchCycle.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
