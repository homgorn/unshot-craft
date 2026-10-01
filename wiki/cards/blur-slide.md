# blur-slide

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/blur-slide`.

## Identity

- **slug**: `blur-slide` (join key across cards, demos, media and deep links)
- **category**: `typography` — Typography & Title Cards / 文字与字卡
- **energy**: `低` — rank 1/8
- **suggested duration**: 约 3.8s（114f@30fps） → **114 frames @30fps = 3.8s**
- **cross-category tags**: `typography`
- **upstream source**: references/shots/typography/blur-slide.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `blur-slide` | 114f | A | `demos/typography/blur-slide/BlurSlide.tsx` |

## What it does

标题逐词入场，y 40→0 + blur 10→0 + opacity 0→1 三通道走同一条 outCubic 同步收敛，词间隔约 3.5f；副标题在标题收完前就错峰跟进

**When to use it.** 几乎所有标题/副标题成对出现的场合；产品页首屏文案、章节小标题；需要"专业但不抢戏"的默认文字 reveal

**Why this shot earns its place.** 这是文字 reveal 的**默认解**——没有奇观、没有机械感，只是把词一个个 柔和地放到位。它的专业感全来自一件事：y、blur、opacity 三个通道共用 同一个进度 `p`、同一条缓动，所以词是"从虚焦里浮出来"而不是"滑进来 顺便淡一下"。当一支片里已经有别的重手法（乱码/翻牌/滚轮），标题就该 用这一卡，让位给主角。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 词间 stagger | 主 0.055（≈3.5f）/ 副 0.04（≈2.5f） | 3–4f 是"逐词"的甜点；<2f 整行齐入没有 stagger，>8f 观众开始一个个数词 |
| 单词入场窗 | 0.32（≈20f），`E.outCubic` | <10f 读作硬弹；>30f 每个词都在慢慢浮，整句拖沓 |
| y 位移 | 主 40px / 副 26px | 主副不等幅是层级来源；<20px 位移无感，>60px 词从画外飞进来变成滑入 |
| blur 通道 | `(1-p)·10`px | 这一通道就是"专业感"，删了退化成普通淡入上移；>18px 中间帧糊成色块 |
| 主副错峰 | 主 0.06–0.62 / 副 0.34–0.90 | 重叠 32f 是"一句话"；副标题起点推到 0.62 之后就读成两拍 |
| 字号字重 | 34px/800 对 14px/400 | 差 2 倍以上才有主副关系；副标题上 600+ 字重会和主标打架 |
| 收尾 hold | 副标题 103f 收完，尾部约 11f 静置 | 静置 <8f 观众还没读完就切了；这是全片唯一的静态帧 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- **占位文案是主 4 词 / 副 5 词，换项目文案时词数要贴近**：stagger 总长
- 三通道必须共用同一个 `p`：分开写三条缓动（哪怕曲线相同）就会出现
- 词级拆分对中文文案要手动切：`split(' ')` 在中文上得到一整块，
- 定位用 `flex` 居中列 + `gap:16px`，主副行高变化会带动整体重排——
- 这是**低能量默认卡**：与本类里的乱码/翻牌/滚轮属于不同职能，同片可以

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/typography/blur-slide/BlurSlide.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
