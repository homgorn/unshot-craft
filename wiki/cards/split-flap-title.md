# split-flap-title

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/split-flap-title`.

## Identity

- **slug**: `split-flap-title` (join key across cards, demos, media and deep links)
- **category**: `typography` — Typography & Title Cards / 文字与字卡
- **energy**: `中` — rank 4/8
- **suggested duration**: 约 4.7s（140f：≥20f 乱码静止建立 + 级联翻牌 + ≥15f 停定静止） → **140 frames @30fps = 4.7s**
- **cross-category tags**: `opening`, `typography`
- **upstream source**: references/shots/typography/split-flap-title.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `split-flap-flip` | —f | B | `demos/typography/split-flap-title/SplitFlapFlip.tsx` |

## What it does

机场翻牌屏字标题——每字符上下两半机械翻牌格，翻过 2 个乱码咔哒停在目标字，左→右级联成波

**When to use it.** 开场/章节大标题；倒计时、发布日期、数据播报类文案；需要"机械宣告感"的一拍

**Why this shot earns its place.** 文字三式的第三式：压印（paper-title-card）是纸上落墨的"低语"，打字机 （document-typewriter-reveal）是文档被人写出来的"叙述"，翻牌是车站大屏的 "播报"——带机械宣告腔。选翻牌的语境：倒计时/发车感（版本发布、截止日）、 数据播报感（指标揭晓）、或想给标题一层复古机械质感。它天然是等宽深底 格子，在库内纸墨审美里读作"纸面上摆了一块机械显示屏"——异色块本身 就是看点，背景产品画面压暗降饱和给它让位。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 单次翻牌 | 5f，p 走 Easing.in(quad)；<0.5 旧字上半叶 0→-90 掉落，≥0.5 新字下半叶 90→0 拍下 | Easing.in 是重力感来源——越掉越快才像机械叶片；匀速读作电子屏假翻 |
| 翻牌次数 | 每格 3 次（2 乱码中间态 + 1 落定） | 少于 2 次读不出"翻找"过程；多于 4 次拖节奏且乱码抢戏 |
| 级联 | stagger 4f 左→右；10 字符约 36f 波峰扫完 | 4f 是波浪感甜点——太密整排齐翻没有波，太疏尾部字符等太久 |
| 停定咔哒 | 落定后 local 15→22f：translateY 0→6→-1.5→0，Easing.out(quad) | 6px 是可感下限（4px 无感判例）；这一下就是"咔哒"的画面体，删了只剩滑动 |
| 明暗 | 掉落叶 brightness 1→0.55，拍下叶 0.55→1 | 明暗差是叶片"转过铰链"的立体感来源，比 rotateX 本身更被肉眼读到 |
| 翻牌格 | 118×156，perspective 420，圆角 10，中缝铰链线 4px #141412 | 铰链线压住翻转轴穿帮；perspective 太大叶片透视变形夸张 |
| 配色字体 | 格底 #262624 / 字 #f4f4f2，Helvetica 800 100px；空格占 52px、格间 gap 12 | 深底浅字是翻牌屏的身份证；等宽格子布局，别用比例字体挤格 |
| 节拍 | 建立 0–21f 静止 → 22f 起级联 → 全停后静止 ≥15f | 建立段让观众先认出"这是块翻牌屏"，直接开翻读作故障闪烁 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 声音强依赖：每格停定的机械拍打声是效果的一半，实战必须配——级联
- 下沉回弹 6px 是可感下限：肉眼看不出就照可感性判例加大幅度，别调
- 一支片翻牌字 ≤1 次：机械宣告腔太抢，重复即贬值（P4 手法去重精神）； _(rules P4)_

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/typography/split-flap-title/SplitFlapFlip.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
