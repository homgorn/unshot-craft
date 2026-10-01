# white-flash-logo-simplify-cut

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/white-flash-logo-simplify-cut`.

## Identity

- **slug**: `white-flash-logo-simplify-cut` (join key across cards, demos, media and deep links)
- **category**: `transition` — Transitions / 转场
- **energy**: `中高` — rank 5/8
- **suggested duration**: 约 3.6s（108f@30fps；静置流光 0–1.2s · 冲白 1.2–1.5s · 扁平定格 1.7–2.7s） → **108 frames @30fps = 3.6s**
- **cross-category tags**: `transition`
- **upstream source**: references/shots/transition/white-flash-logo-simplify-cut.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `white-flash-logo-simplify-cut` | 108f | A | `demos/transition/white-flash-logo-simplify-cut/WhiteFlashLogoSimplifyCut.tsx` |

## What it does

彩色液态渐变字标静置流光，画面一拍冲白过曝，白底上扁平版字标淡入定格——一次闪白完成质感降维

**When to use it.** 品牌段落收束（华丽演绎→干净定妆）；情绪从炫技切换到正式宣告的转场拍

**Why this shot earns its place.** 先给足华丽（六色液态渐变在字面上流动、柔光扫掠），再用一次白闪把它"净化"成扁平三色字标——观众读到的是"演出结束，这就是它的正式形象"。降维是修辞：从感性质感切到理性识别。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 冲白窗口 | 0.34–0.42（inQuad） | 换算 0.29s@3.6s——冲白必须"快进慢不退"；用 outQuad 会显得白光是飘进来的 |
| 过曝脉冲 | blur 5px + brightness ×2.2，sin 包络 | 砍掉脉冲则冲白像纯剪辑；>8px blur 液态字彻底糊掉反而看不出"是它在烧" |
| 扁平入场 | 0.48–0.74，scale 0.96→1 | 与冲白间隔 0.06 的白屏静默是呼吸位；缩太短观众来不及"清屏" |
| 液态流速 | backgroundPosition t*100% | 拉长 dur 时流速自动变慢，静置段够 1s 以上流动感才可读 |
| 字标字号 | 液态 62px / 扁平 58px | 扁平版略小一号是"落定收束"暗示；同号会读作换皮不换人 |
| 渐变常量 | `GRAD_A/B/C`（块顶定义） | 换成项目品牌三色即完成收编；液态层六色一般保留（它是"演出"不是品牌） |

## Known pitfalls

- 白层是"冲入后保持"，不是闪一下回黑——后半场底色即白色，若下一镜是暗场需另接转场，或复用本卡结尾白底直切
- `WORDMARK` 常量是占位字标（5 字母），换长词需同步缩字号与 letter-spacing，两层（液态/扁平）都要改
- 冲白配 SFX 是必选项（impact/whoosh-bright 类），无声的白闪读作素材丢帧
- mix-blend-mode:screen 的柔光层在白底上不可见属预期，别在冲白后调它

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/transition/white-flash-logo-simplify-cut/WhiteFlashLogoSimplifyCut.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
