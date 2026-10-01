# radial-wave

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/radial-wave`.

## Identity

- **slug**: `radial-wave` (join key across cards, demos, media and deep links)
- **category**: `ui-entrance` — UI Entrance & Showcase / 界面登场与陈列
- **energy**: `中高` — rank 5/8
- **suggested duration**: 约 3.8s（114f@30fps） → **114 frames @30fps = 3.8s**
- **cross-category tags**: `ui-entrance`
- **upstream source**: references/shots/ui-entrance/radial-wave.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `radial-wave` | 114f | A | `demos/ui-entrance/radial-wave/RadialWave.tsx` |

## What it does

17×9 圆点阵列按到波源的欧氏距离错峰点亮，每点 scale 过冲到 1.5 再落回常亮，第一道波扫完后第二道亮蓝脉冲从外圈反向收拢回中心

**When to use it.** 产品/品牌开场的"系统上电"一拍；也用作数据网格、节点地图、覆盖范围类叙事的建立镜头

**Why this shot earns its place.** 把"很多点同时存在"这件静态事实，改写成"能量从一个源头扩散到全体"的动态事实。观众 看到的不是一张点阵图，而是一次通电：中心先亮，亮度像水波推过去，走完之后整张阵列 留在常亮态——为下一拍要放的内容铺好底。第二道反向波是回执，告诉观众这个系统会回应。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 阵列规模 | COLS=17 / ROWS=9（153 点） | 点数决定波前的"分辨率"；<8 列时距离分档太粗，波读作三四圈同心环在跳 |
| 波速系数 | `dist*0.35` | 这个 0.35 就是波速倒数：调大波走得慢、拖尾长；>0.5 时最外圈要等到全片过半才亮 |
| 单点行程 | 0.18（≈21f） | 决定波前的厚度；<0.1 波前锐利像扫描线，>0.3 全场几乎同时亮，扩散感消失 |
| 过冲幅度 | `1+0.5*sin(w1*π)` → 峰值 1.5 | 系数 0.5 是"弹一下"的量；去掉正弦项就是平淡的 0→1 淡入，>0.8 点会互相咬边 |
| 第二道波 | 起点 `0.62+(1-dist)*0.25`，窗 0.15，幅度 0.8 | 0.62 是两波之间的呼吸；提前到 0.5 以下会和第一道波尾巴叠在一起读作一团乱闪 |
| 常亮底 | `opacity = 0.25 + w1*0.5 + pulse2*0.25` | 0.25 是未点亮点的存在感；调到 0 则波前之外一片黑，阵列的"规模"交代不出来 |
| 高亮阈值 | `pulse2 > 0.3` 切色 + 光晕 | 阈值越低发光段越长；这是硬切不是渐变，阈值贴近 0 时会看到明显的开关跳变 |

## Known pitfalls

- 波源写死在几何中心（`cx=(COLS-1)/2, cy=(ROWS-1)/2`）。要改成从角落或某个"节点"起波，
- 末帧不完全静止：中心点（dist=0）的第二道波窗是 0.87→1.02，t=1 时才走到 87%，
- dot 的 `width:10px` 与 `margin:-5px` 是绑定的一对（靠负 margin 居中），改点径必须同步改
- 颜色只有两档（常色 `#6c8cff` / 峰值 `#b9f2ff`），换品牌色要改这两处加光晕色共三处；

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/ui-entrance/radial-wave/RadialWave.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
