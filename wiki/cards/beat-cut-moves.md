# beat-cut-moves

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/beat-cut-moves`.

## Identity

- **slug**: `beat-cut-moves` (join key across cards, demos, media and deep links)
- **category**: `rhythm` — Rhythm & Montage / 节奏与蒙太奇
- **energy**: `高` — rank 6/8
- **suggested duration**: A 全程 ~4.3s（建立 49f + 五连切 + 定格 hold 35f）；B 全程 ~4.3s（活素材 30f + 三闪 + hold 60f） → **49 frames @30fps = 1.6s**
- **cross-category tags**: `transition`, `rhythm`
- **upstream source**: references/shots/rhythm/beat-cut-moves.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| A | `beat-cut-accelerando` | —f | B | `demos/rhythm/beat-cut-moves/BeatCutAccelerando.tsx` |
| B | `paparazzi-flash` | —f | B | `demos/rhythm/beat-cut-moves/PaparazziFlash.tsx` |

## What it does

硬切当节拍乐器的两式——递进硬切串（间隔减半加速逼近）与连闪定格（三次白闪各切一个裁切）

**When to use it.** 高光/冲刺段落把"切"本身打成鼓点；A 式预告片式加速逼近，B 式颁奖连拍仪式感

**Why this shot earns its place.** 库内节奏词汇一直只管"一条运动内"的速率（speed-ramp 是同一条 take 里变速）和"落定后停多久"（R 系呼吸判例），没有词管**多镜之间切点 怎么排**。本卡补这一块：硬切不做任何过渡，切点间隔本身就是乐谱—— 间隔递减读作加速逼近（A），等距三闪读作快门连拍（B）。与 R 系不 冲突：R 管落定后的停，本卡管切点排布，切串结束必须接足量 hold 把 呼吸还回去。注意这是刻意的例外——节奏偏好判例是单向"放慢"，硬切 串切得越狠，切完的 hold 要比平常更长。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| A 切点帧 | 0/49/65/77/85/91/95（建立 49f，间隔 16→12→8→6→4f） | 间隔按"减半律"缩，等差缩读不出加速；末间隔 <4f 肉眼跟不上 |
| A 视图池 | 6 个 = 两块 FakeDashboard × scale 1/1.8/2.6 + 对焦点，transformOrigin 钉焦点再平移居中 | 视图必须是同一产品的不同构图（语义连续），六个无关画面读作故障 |
| A 切帧快门感 | 切帧 1f brightness 1.05 + 叠 6% 不透明度白层 | 只在切帧亮一下，是"咔"不是闪光灯；再厚就抢了 B 式的活 |
| A 末段收住 | 定格回主画面 hold 35f，scale 1→1.06 ease-out 慢推 20f 后静止 | 戛然而止是这式的句号——末刀后不许再有任何切 |
| B 三闪切点 | 30/52/70（间隔 22f→18f 渐紧），闪前 30f 慢推"活素材"衬托闪后定格 | 闪前必须是活的，全片死素材三闪读不出"定格" |
| B 白闪层 | 每闪 opacity 0.95→0 走 4f ease-out 衰减；闪帧 ±2px seed 哈希全屏抖动 | 0.95 起步才有闪光灯的爆点；衰减 >6f 变柔光转场，失去快门感 |
| B 快门余韵 | 切入视图 scale 1.03→1 走 6f ease-out 回落 + −16px 沉降归零 | 余韵是"被拍到晃了一下"；去掉后三闪读作幻灯片翻页 |
| B 三裁切 | 同一 Footage 换 scale/transformOrigin：1.0 全景 / 2.3 卡片 / 4.0 数字 | 层层逼近有叙事方向；乱序（特写→全景→特写）读作剪错 |
| B 末段收束 | 第三闪后数字特写 hold 60f 静止 | 三闪是重击，hold 要给足平常两倍以上 |

## Known pitfalls

- **demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 两式都是**声音强依赖**手法：切点必须钉在音轨拍点上，每切一声
- A 式六视图要"同一产品的不同构图"而非六个无关画面——观众要在加速
- 切串全片 ≤1 次（P4 克制原则）：这是全片最响的一记，第二次出现 _(rules P4)_
- 节奏偏好判例是单向"放慢"，本卡是刻意例外——切完的 hold（A 35f /
- 真硬切 = frame 落区间渲染对应视图，无任何过渡帧；手滑加 2f 交叉

## Card structure

`intention` | `variants` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/rhythm/beat-cut-moves/BeatCutAccelerando.tsx`
- `demos/rhythm/beat-cut-moves/PaparazziFlash.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
