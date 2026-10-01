# type-rhythm-sync

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/type-rhythm-sync`.

## Identity

- **slug**: `type-rhythm-sync` (join key across cards, demos, media and deep links)
- **category**: `typography` — Typography & Title Cards / 文字与字卡
- **energy**: `A 高` — arc or n/a, not sortable
- **suggested duration**: 单式 4–5s；A 每拍占 10f 衰减窗、B 每词按语速 15–35f → **10 frames @30fps = 0.3s**
- **cross-category tags**: `typography`, `rhythm`
- **upstream source**: references/shots/typography/type-rhythm-sync.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| A | `font-weight-pump` | —f | B | `demos/typography/type-rhythm-sync/FontWeightPump.tsx` |
| B | `karaoke-fill-sync` | —f | B | `demos/typography/type-rhythm-sync/KaraokeFillSync.tsx` |

## What it does

文字随声同步两式——font-weight-pump 字重脉冲（笔画随鼓点变粗弹回）与 karaoke-fill-sync 卡拉OK填色（词随旁白逐个点亮）

**When to use it.** 标题/标语与音轨强绑定的段落；A 绑节拍（鼓点），B 绑语音（旁白逐词）

**Why this shot earns its place.** 文字动效库内此前全是"入场怎么进"，没有词管"在场的字怎么跟着声音活"。 这两式补上：A 让标题变成节奏器官——笔画随低音鼓抽动变粗又弹回， 文字在蹦迪，适合高能段落的视觉低音炮；B 让标语变成跟读字幕—— 旁白读到哪个词哪个词从左到右填色点亮，视线被牵着走，适合口播/ 标语强调段。共同点是**字不动、属性动**：无位移、无入退场， 纯粹是字重/颜色在声音的拍点上呼吸。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| A 脉冲包络 | `env=(1−t/10)^0.8`（t=命中后帧数，≥10f 精确归 0）；`-webkit-text-stroke: 10px·env` + fontWeight 在 env>0.15 窗口 400↔900 跳变 | stroke 连续衰减 + 字重离散跳变叠加才读作"连续变粗"；单用 fontWeight 只有两挡、单用 stroke 变化太细 |
| A 节拍 | 每 20f 一拍；重音拍额外 `scaleX = 1+0.08·env`（transform 缩放不改排版） | 拍距必须 > 衰减窗（20>10），两拍重叠读作抽搐 |
| A 节拍参照物 | 画面下方一排小节拍点，命中哪拍哪个点闪深并放大 | 静音环境（预览/静帧）没有这排点就读不出"在跟拍" |
| B 词级时间表 | 逐词 [start,end] 帧区间，词内 linear 填充；词间留 4–10f 停顿（换气） | 时间戳实战来自旁白打点表；均匀分配读作机器朗读 |
| B 填色实现 | 每词双层同文本叠放：底层浅灰 + 上层深色 `clipPath: inset(0 X% 0 0)`，X=(1−p)·100 | 逐词独立叠层免量测词宽占比；整行单层 clip 需精确像素表、易漂 |
| B 读指 | 活跃词下 8px 深色下划线，宽度 = p·100% | 4px 浅灰在 1080p 缩略下不可见（本批实渲踩坑）；读完的词不留线 |
| 收尾 | A 末拍衰减归零后 / B 末词填完后真静止 ≥20f | R1 呼吸判例 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 两式都是**声音强依赖**手法：A 命中帧必须与鼓点同帧、B 填色区间必须
- A 式实战想要真·可变字体连续字重（wght 轴逐帧插值）需先确认字体加载
- A 式全片 ≤1 段（P4）——标题蹦迪是抢戏大户，两段同片互相拆台 _(rules P4)_
- B 式词数 ≤6/屏：更多词时填色进度读不过来，拆行或拆镜

## Card structure

`intention` | `variants` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/typography/type-rhythm-sync/FontWeightPump.tsx`
- `demos/typography/type-rhythm-sync/KaraokeFillSync.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
