# brand-frame-snap

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/brand-frame-snap`.

## Identity

- **slug**: `brand-frame-snap` (join key across cards, demos, media and deep links)
- **category**: `effects` — Light & Emphasis / 光效与强调
- **energy**: `中` — rank 4/8
- **suggested duration**: 单次翻色 ~4.3s（130f）；画框本身可全片驻场 → **130 frames @30fps = 4.3s**
- **cross-category tags**: `transition`, `effects`
- **upstream source**: references/shots/effects/brand-frame-snap.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `brand-frame-snap` | —f | B | `demos/effects/brand-frame-snap/BrandFrameSnap.tsx` |

## What it does

品牌色画框语法——一圈粗纯色画框先于内容长出包住全屏，录屏窗口落进框内；模式切换时整圈画框同帧硬翻色+窗内布局同帧换，一个 borderColor 干完章节导航/状态提示/品牌露出三件事

**When to use it.** 双模式/双章节产品片的全片包装层（蓝=模式A、绿=模式B 颜色编码）；真实录屏素材的品牌化包裹

**Why this shot earns its place.** 真实录屏直接铺满屏没有品牌存在感，加 logo 水印又廉价。本卡用一圈 粗品牌色画框把录屏"装裱"起来：画框**先于内容出现**（先立画框再放 画，仪式感），之后画框颜色成为全片的语义编码——蓝=Design、绿=Dev Mode。章节切换时整圈画框一帧内硬翻色，无渐变，颜色硬切就是"换挡" 声效的视觉等价物；窗内布局同帧 A→B、角标与徽标同步换字，三处同帧 共振把"模式切换"砸实。与 theme-switch-moves 分工：那换的是 UI 本体 肤色（有扫过边界），本卡换的是"画框"这个包装层（同帧无边界）， 语义是模式/章节切换不是主题切换。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 画框厚度 | 44px（1080p） | 太薄读作描边不读作"装裱"；>60px 开始吃内容区 |
| 画框生长 | 18f ease-out，先于窗口 14f | 画框必须先立——内容先到画框后包读作补救 |
| 窗口落位 | spring(damping 16, stiffness 110)，y 560→0 + scale 0.82→1 | 落进"框内"是语义关键，落点必须完全在框带内侧 |
| 翻色时刻 | demo 78f；停一拍（窗口落定后 ≥30f）再翻 | 落定没坐稳就翻，观众还没建立"蓝=当前模式"的编码 |
| 白闪脉冲 | 2–3f，0.55→0.19 阶梯 | 帮眼睛登记"这一帧变了"；>4f 抢了 cel-flash 的活 |
| 厚度弹跳 | exp 衰减 cos，初幅 10px | 纯硬切略干；弹跳是"挡位卡进去"的机械回馈 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 翻色必须真同帧：画框、窗内布局、角标文字三者错开哪怕 2f，"换挡"就散成三个小动画
- 颜色编码要全片守约：蓝框段落里不许出现绿色主 UI 元素，编码被稀释后翻色就只是换色
- 画框是包装层不是主角：全片翻色 ≤2 次，翻多了读作霓虹灯（P4 克制原则） _(rules P4)_
- 两个模式的品牌色对比度要够（demo 蓝 #3E7BFA / 绿 #1BC47D）；同明度邻近色翻了等于没翻
- 声音：翻色帧钉一声干脆的机械 click/换挡声，白闪与声同帧；画框生长段可静

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/effects/brand-frame-snap/BrandFrameSnap.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
