# outline-word-fill

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/outline-word-fill`.

## Identity

- **slug**: `outline-word-fill` (join key across cards, demos, media and deep links)
- **category**: `typography` — Typography & Title Cards / 文字与字卡
- **energy**: `高` — rank 6/8
- **suggested duration**: 约 2.5s（75f@30fps，短促单拍） → **75 frames @30fps = 2.5s**
- **cross-category tags**: `typography`
- **upstream source**: references/shots/typography/outline-word-fill.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `outline-word-fill` | 75f | A | `demos/typography/outline-word-fill/OutlineWordFill.tsx` |

## What it does

空心词（1px 灰描边、500 字重）从 3.2 倍急缓收缩落位，虚线大圆随后从 2.8 倍收到字周围并缓慢自转，左右水平虚线从画框边缘内伸；描边先微微增亮，实心白在 0.6 帧内瞬间点亮，一闪辉光即定格

**When to use it.** 单词式利益点/口号的重锤一拍；节奏卡点上的"钉子"镜；深底品牌片的强调帧

**Why this shot earns its place.** 一个词要打成钉子，靠的不是慢慢淡入而是**两次落定**：先是巨大空心字 急速收缩到位（这是尺寸的落定），再是描边在一帧内变实心白（这是质感的 落定）。中间那 1.5s 的虚线圆收缩与水平虚线内伸是"瞄准"过程——技术 制图语汇，让点亮那一下读作"确认"。填充**必须是瞬时**的：慢扫填充会把 钉子变成缓慢的美化动画。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 收缩 | `scale 3.2 → 1`，窗 10f，outCubic | 3.2 倍是"从脸前退开"的量；<2 倍读作普通缩放；窗 >20f 就成了缓慢 zoom，冲击全失 |
| 字重字号 | 48px / **500** / `letter-spacing:.5px`，占画宽约三成 | 空心字上 700+ 会让 1px 描边包住一大块空白，读作气球字；500 是空心字的甜点 |
| 描边 | `1px #565b63`，点亮前预热到灰度 145 | 1px 细描边是"制图"语汇；2px+ 变涂鸦；预热那一档删了硬切显得没由来 |
| 虚线圆 | r=88、`dash 6 8`、scale 2.8→1（45f）、自转 `t·18`° | 45f 慢收缩是全片的"呼吸"，与 10f 的字收缩形成快慢对比；窗压到 20f 两者撞在一起 |
| 水平虚线 | `dash 5 7`，从 ±240 内伸 144，窗 0.5→0.72 | 内伸终点要停在圆边（不进圆内）；伸满全宽读作十字准星，过头了 |
| 瞬时填充 | `seg(0.742, 0.762)`（≈0.6f） | **这一下是全卡的目的**：任何形式的慢扫（>3f）都会把钉子降级成美化动画 |
| 辉光 | 峰值 16px，`rgba(255,255,255,.45)`，7f 衰完 | 一闪即逝才像"点亮"；持续辉光读作发光字体，质感立刻廉价 |
| 微尘 | 14 颗，静态不动 | 静态是对的（本卡只 2.5s，动尘会抢戏）；数量 >25 底噪太脏 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- **只适合单个短词（demo `Faster`，6 字母）**：字号与虚线圆半径是写死的
- `-webkit-text-stroke` 是前缀属性，Chromium/WebKit 才生效；Firefox 下
- 瞬时填充窗 `0.02` 在 75f 片长下不足一帧：这是**故意的**（要的就是硬切），
- 时间窗注释里的秒数（4.83→5.15s 等）是原片时间轴的残留，与本卡
- 深底专用：`#050505` 底 + 白描边 + 辉光是效果的全部；浅底上空心字
- 声音强依赖：点亮那一帧必须有一记短促重音（金属/开关/低频撞击），

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/typography/outline-word-fill/OutlineWordFill.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
