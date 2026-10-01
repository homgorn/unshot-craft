# svg-shape-morph

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/svg-shape-morph`.

## Identity

- **slug**: `svg-shape-morph` (join key across cards, demos, media and deep links)
- **category**: `ui-entrance` — UI Entrance & Showcase / 界面登场与陈列
- **energy**: `低` — rank 1/8
- **suggested duration**: 约 5.2s（156f@30fps） → **156 frames @30fps = 5.2s**
- **cross-category tags**: `ui-entrance`
- **upstream source**: references/shots/ui-entrance/svg-shape-morph.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `svg-shape-morph` | 156f | A | `demos/ui-entrance/svg-shape-morph/SvgShapeMorph.tsx` |

## What it does

一条 140 点闭合轮廓平滑变形为另一条再变回，两形状先在极坐标下重采样到相同点数、逐点半径插值 + inOutCubic，变形中段叠轻微 scale 呼吸、缓慢自转与色相从 185° 漂到 305°

**When to use it.** 抽象概念的"形态转换/自适应/有机生长"表达；开场 logo 前的氛围一拍，或章节之间的过渡形

**Why this shot earns its place.** "形态会变"这件事，用两张图交叉淡入是说不清的——观众看到的是两个东西重叠。真正的 morph 要让观众相信这一直是**同一个东西**在改变形状。等点数重采样加逐点插值就是这个 "同一性"的技术保证：没有点的生成或消失，只有半径在变。变回原形是为了闭环——观众 看到往返，才知道这是可逆的能力而不是一次性的变身。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 采样点数 | N=140 | 140 点在 480×270 上足够平滑（`L` 直线段肉眼看不出）；<60 点能看到多边形棱角，>300 点是纯浪费 |
| 基半径 | BASE=76，中心 (240,138) | 76 相对 270 高度约占 56%——留边给光晕；调大要检查 `0.30` 的凸起是否顶出 viewBox |
| 形状 A | `1 + 0.30cos(3θ) + 0.05sin(7θ+0.8)` | 3θ 定瓣数、0.30 定凸起深度；深度 >0.5 时凹处半径趋近 0，形状会掐出尖角 |
| 形状 B | `1 + 0.26sin(5θ+1.2) + 0.06cos(2θ)` | 与 A 的瓣数不同（5 vs 3）才有变形张力；瓣数相同只会看到形状"转了转" |
| 变形窗 | 0.08→0.42 / 0.58→0.92，均 inOutCubic | 行程 0.34（≈53f）；inOut 的缓起缓收是"有机"的关键，换 linear 立刻读作机械插值 |
| 中段静置 | 0.42→0.58（≈25f） | 这是让观众认清 B 形态的时间；砍掉会读作一次来回摆动而不是 A→B→A |
| 呼吸幅度 | 0.045 × `sin(m*π)` | 4.5% 的呼吸在变形中途达峰；>10% 会读作缩放动画而不是形变 |
| 自转 | `sin(t*2π)*4°`（1 个整数周期） | 4° 是暗示级别的漂移，末帧回零可循环；>15° 会看出是整体旋转，与形变抢注意力 |
| 色相区间 | 185°→305°（青→紫） | 跨度 120° 让两个形态有明确的身份差；跨度 <40° 时颜色变化读不出，色相就白给了 |

## Known pitfalls

- 极坐标定义天生只能表达"从中心看每个角度一个半径"的形状——星形、花瓣、水滴都行，
- 路径用 `L` 直线段拼接而非曲线段，靠点数密度掩盖。如果做大幅放大（>2 倍）或极粗
- 每帧重建整条 `d` 字符串（140 点字符串拼接 × 2 个 path）。480×270 无压力，但如果同屏
- 两条形状函数写死在 setup 里，没有做成参数。要换形状是改函数体而不是传参——移植时
- 字幕 `morphTo(shapeB)` 是 anime.js API 的自我说明式占位文案，成片里应换成有语义的
- 背景写死 `#0a0b10`，整套颜色（90% 饱和描边 + 8px 光晕）依赖深底。白底上光晕失效，

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/ui-entrance/svg-shape-morph/SvgShapeMorph.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
