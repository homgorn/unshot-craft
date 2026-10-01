# list-reveal

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/list-reveal`.

## Identity

- **slug**: `list-reveal` (join key across cards, demos, media and deep links)
- **category**: `ui-entrance` — UI Entrance & Showcase / 界面登场与陈列
- **energy**: `低` — rank 1/8
- **suggested duration**: 约 3.6s（108f@30fps） → **108 frames @30fps = 3.6s**
- **cross-category tags**: `ui-entrance`
- **upstream source**: references/shots/ui-entrance/list-reveal.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `list-reveal` | 108f | A | `demos/ui-entrance/list-reveal/ListReveal.tsx` |

## What it does

垂直菜单 6 项按 0.09 的间隔依次 scale 找位、outBack 轻微过冲落定，同时整个列表容器全程线性上移 32px——逐项入场与整体漂移是两层不相干的运动

**When to use it.** 导航/侧边栏/设置面板的入场；任何"界面自己长出来"的 UI 段落，也适合做旁白铺垫时的低能量底

**Why this shot earns its place.** 列表逐项淡入是最容易做得死板的一类动效：每项动完就停，画面在两项之间是完全静止的。 这张卡的解法是给容器加一层与逐项入场无关的慢速漂移——局部在"找位"，整体在"呼吸"。 观众读得清每一项，同时画面从头到尾没有一帧是钉死的。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 项数 | 6（Dashboard…Sign out） | 末项窗口 0.51→0.75，尾部留 0.25 静置给观众收尾；>8 项必须压 stagger，否则末项吃到收尾 |
| stagger | 0.09/项（≈10f） | 10f 是"逐项读得完"；压到 0.04 变成一次铺开（另一种手法），拉到 0.15 以上节拍会散 |
| 单项行程 | 窗 0.24（≈26f） | 行程比 stagger 长 2.6 倍 → 相邻三项同时在动，队列是连绵的；两者相等会变成一项一项硬接 |
| 起始 scale | 0.78 | 0.78 是"已经能认出是个条目"的尺度；<0.5 读作从零弹出，和 pop 类手法混淆 |
| 起始位移 | 14px | 位移必须远小于行高（9px gap + 约 33px 项高），否则项与项之间穿插 |
| 过冲 | `E.outBack` | 这里的过冲要小到几乎读不出来；换 spring 或加大 back 系数，6 项连续抖会显得廉价 |
| 容器漂移 | `lerp(t, 16, -16)`，全程线性 | 总位移 32px 摊在 3.6s 上（约 0.3px/f）——刚好在"感觉画面活着"和"看得出在动"之间；>60px 会与逐项位移量级相当，两层运动混为一件事 |
| 透明度斜率 | `min(1, p*2.2)` | 2.2 决定多早变实；降到 1 会看到半透明项叠在背景上，深色主题下尤其脏 |

## Known pitfalls

- 容器漂移是线性且贯穿全程，t=1 时停在 -16px 而不是 0——这个动效**末帧不回位**。
- 项数变化必须重算 stagger：末项起点 `0.06+(n-1)*0.09`，10 项时起点已到 0.87，行程会
- 文案没设 `white-space:nowrap`，容器宽度写死 240px——中文或更长的英文标签会换行，
- 漂移方向（向上）与逐项位移方向（14px→0，也是向上）同向。这是有意的（同向叠加更
- 图标是 hue 色环渐变方块的占位（6 个色相区分条目），落地要换成真实图标；条目底色

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/ui-entrance/list-reveal/ListReveal.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
