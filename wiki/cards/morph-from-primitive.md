# morph-from-primitive

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/morph-from-primitive`.

## Identity

- **slug**: `morph-from-primitive` (join key across cards, demos, media and deep links)
- **category**: `ui-entrance` — UI Entrance & Showcase / 界面登场与陈列
- **energy**: `中低` — rank 3/8
- **suggested duration**: ~4.7s（呼吸 20f + 变形 24f + 内容淡入 12f） → **20 frames @30fps = 0.7s**
- **cross-category tags**: `opening`, `ui-entrance`
- **upstream source**: references/shots/ui-entrance/morph-from-primitive.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `morph-from-primitive` | —f | B | `demos/ui-entrance/morph-from-primitive/MorphFromPrimitive.tsx` |

## What it does

原型变形——正圆呼吸一拍（anticipation）后 SVG path 插值 24f 长成圆角卡轮廓，内容淡入

**When to use it.** 图形/图标/卡轮廓类主体的入场；logo→UI 容器的经典原语

**Why this shot earns its place.** 入场库全是"从外面进来"——飞入、砸落、翻面，主体都预先存在于画外； 本卡是**就地长出来**：画面中心一个描边正圆先鼓一口气（scale 1→1.12→1），随即轮廓连续变形为圆角矩形卡片，内容再淡入。原型 停留加呼吸这一拍就是预备动作——迪士尼 anticipation 的图形学翻译： 圆先"吸气"，观众就知道它要变，变形本身因此不需要任何解释。 仅适用图形/图标/卡轮廓类主体——位图截图不能 morph。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 呼吸幅度 | 1→1.12→1，20f inOut cubic | <1.1 读不出"吸气"；>1.2 像要爆炸不是要变形 |
| 原型停留 | 静置 10f + 呼吸 20f，合计 30f 才起变形 | 停留 <15f 读不出"预备"，变形显得突兀 |
| 变形时长 | 24f | 太快像切换、太慢像融化；24f 是"生长"的速度 |
| 目标形态 | 520×300 圆角矩形卡（demo 值） | 圆角越大与圆同构性越好、中段越顺 |
| 内容淡入 | 变形落定后 2f 起，12f 淡入 | 变形没完就进内容 = 内容跟着轮廓扭 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- **变形中途别叠其他动画**——morph 本身就是全部信息，同时飞入/
- 位图截图不能 morph：本卡只对矢量轮廓成立，页面截图请回
- path 插值两端命令数必须严格同构（同为 M+8C），命令数不齐
- 变形中段呈"桶形"过渡是正常形态（QA 判例），不是穿帮；

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/ui-entrance/morph-from-primitive/MorphFromPrimitive.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
