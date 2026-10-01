# transition-travel

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/transition-travel`.

## Identity

- **slug**: `transition-travel` (join key across cards, demos, media and deep links)
- **category**: `transition` — Transitions / 转场
- **energy**: `n/a` — arc or n/a, not sortable
- **suggested duration**: n/a（技法卡；各式动作段 25–60f，前后 hold 另计，帧数从相邻镜头预算里划） → not a timed card (technique card)
- **cross-category tags**: `camera`, `transition`
- **upstream source**: references/shots/transition/transition-travel.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `letterform-zoom` | —f | B | `demos/transition/transition-travel/LetterformZoom.tsx` |
| — | `shared-element-morph` | 60f | B | `demos/transition/transition-travel/SharedElementMorph.tsx` |

## What it does

穿越式转场两式——共享元素归位、字腔穿越，镜头钻进画面里的真实元素完成换景

**When to use it.** 前后两镜存在"元素/容器"级空间关系的接缝（技法卡，与 shot-transitions 六式互补选用）

**Why this shot earns its place.** shot-transitions 六式是"交棒"型——前镜收尾、后镜入场，接缝靠白闪/暗场/ 焦点/黑场/糊帧/窗口盖住换页瞬间。本卡两式是"穿越"型——后景在前景画面里 以真实元素存在（网格槽位/字形洞），镜头一条连续空间运动钻进去， 观众从头到尾跟着同一个物体，没有交棒瞬间。选型口径：后景能在前景里"预先 在场"→穿越；两景只是先后关系、无空间嵌套→交棒。两式内部再按语义分—— A 是"把这张卡放回去"（详情→总览，F 式穿窗的逆向）；C 是"标题即是门" （章节字卡与转场二合一）。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| A morph 主曲线 | 25f bezier(0.4,0,0.2,1) 冲到 1.03 过冲 + 10f Easing.out(cubic) 弹回 1；位置/尺寸/圆角共用同一条进度 p | 三属性各走各的曲线立刻读作"变形"而非"同一物体"；过冲 >5% 读作果冻 |
| A 同一物体感 | 内容按槽位尺寸渲染、随容器等比缩放（scale 3.66→1，origin 左上）；投影随 p 从 0/36/110/0.32 收敛到 0/2/8/0.06 | 内容重排版=换了张卡，穿越感断；投影不收敛则卡永远悬空、落不了座 |
| A 落座仪式 | 背景 dashboard 0.9 透明度待命，落座瞬间 5f 提到 1 | 背景全程满亮则飞落没有"到家"的一拍；提亮窗口跨骑落座帧前后 |
| C 穿腔主推 | 盖板 SVG mask（白底+黑字 900 字重）挖洞，transform-origin 对准腔心（demo："DASH" A 腔 ≈773,508）；scale=28^t，t 60f bezier(0.6,0,0.85,0.5) 慢起陡收 | ZOOM_MAX 按"洞撑满画面"配，字腔越小倍数越大；慢起段留给观众看清"洞里有东西" |
| C 撤场与呼应 | scale∈[15,24] 盖板 opacity 1→0（残余笔画边飞边撤）；期望模糊量 0→16px 除以 scale 写进 blur 补偿；洞内 B 层微 dolly 1→1.1、接管后 25f 落回 1 | blur 不除 scale 会被 transform 放大成糊墙；B 不跟着 dolly 则洞里是张死图，"穿进活页面"的感知断掉 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- C 式腔心坐标是字体度量估算（字宽 em 值手推），换字体/换词/渲染器字距
- A 式槽位坐标必须精确到像素（demo 里从 fixtures 布局逐项推算 808,590,
- 穿越两式与交棒六式同一接缝不叠加，一缝一式；穿越式已自带高能量，

## Card structure

`intention` | `variants` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/transition/transition-travel/LetterformZoom.tsx`
- `demos/transition/transition-travel/SharedElementMorph.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
