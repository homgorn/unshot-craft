# scramble

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/scramble`.

## Identity

- **slug**: `scramble` (join key across cards, demos, media and deep links)
- **category**: `typography` — Typography & Title Cards / 文字与字卡
- **energy**: `中高` — rank 5/8
- **suggested duration**: 约 3.2s（96f@30fps） → **96 frames @30fps = 3.2s**
- **cross-category tags**: `typography`
- **upstream source**: references/shots/typography/scramble.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `scramble` | 96f | A | `demos/typography/scramble/Scramble.tsx` |

## What it does

等宽整行字符先每 2 帧高速跳乱码，再从左到右逐个锁定为真字，锁定瞬间蓝白高光闪一下——种子驱动可复现的解密感

**When to use it.** 技术型开场标题；版本号/代号揭晓；"系统就绪""数据解锁"这类带机器口吻的一拍

**Why this shot earns its place.** 同一句标题的三种"造字"手法里，打字机是人在写、翻牌是机器在播报， 乱码锁定是**机器在算**——先满屏噪声表示"还没解出来"，再左→右一个个 咬定真字符。它天然带黑客/解密腔，适合技术产品的开场；但也最挑文案： 字符是被逐个点名的，字数就是节拍数。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 占位文案 | `TEMPLATE MOTION DEMO`，20 字符 | 字符数直接决定 stagger 密度：<10 字锁定太快读不出"逐个"，>30 字末字等到片尾 |
| 锁定窗 | 全局 0.25→0.85（24f→82f） | 起点早于 0.2 噪声段太短没建立感；终点晚于 0.9 没有静置收尾 |
| 锁定抖动 | `rand(i·7)·0.06`（≤6f） | 去掉就是完美等分，读作进度条而非"逐个咬定"；>0.12 顺序会乱 |
| 跳字频率 | 每 2 帧（15 次/秒） | 1 帧一换糊成灰带；4 帧以上读作"慢慢翻"不是高速运算 |
| 锁定闪光 | 窗 0.1（约 3f），光晕 18px 峰值 | 这一闪是"咬定"的画面体，删了只剩换字；>30px 相邻字光晕连成一片 |
| 字体字距 | SF Mono/Menlo 34px、`letter-spacing:2px`、槽宽 `min-width:0.62em` | 等宽 + 固定槽宽是刚需，比例字体会随乱码字符宽度整行抖动 |
| 起手空屏 | `t < 0.06`（前 6f） | 直接开噪声读作故障闪烁；>12f 空屏在剪辑里成了黑场 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- **换成项目文案时字符数要贴近 20**：lockAt 是按 `i/n` 归一化铺开的，
- 必须等宽字体：槽宽写死 `0.62em`，比例字体下 `#`/`W`/`I` 宽度不一，
- 空格字符被显式跳过（永不参与乱码），所以词间隙全程保持——文案里
- 与 split-flap-title / 打字机类分工：那两个是**机械/人工**造字，本卡是

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/typography/scramble/Scramble.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
