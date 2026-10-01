# type-assembly-moves

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/type-assembly-moves`.

## Identity

- **slug**: `type-assembly-moves` (join key across cards, demos, media and deep links)
- **category**: `typography` — Typography & Title Cards / 文字与字卡
- **energy**: `A 中 / B 中高 / C 低中 / D 中` — arc or n/a, not sortable
- **suggested duration**: 单式 4–5s（动作段 A ~56f / B ~104f / C ~58f / D ~99f，均含 hold） → **56 frames @30fps = 1.9s**
- **cross-category tags**: `typography`
- **upstream source**: references/shots/typography/type-assembly-moves.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `letterform-drift-assembly` | —f | B | `demos/typography/type-assembly-moves/LetterformDriftAssembly.tsx` |
| A | `split-text-stagger` | —f | B | `demos/typography/type-assembly-moves/SplitTextStagger.tsx` |
| D | `text-on-path` | —f | B | `demos/typography/type-assembly-moves/TextOnPath.tsx` |
| — | `tracking-expand-reveal` | —f | B | `demos/typography/type-assembly-moves/TrackingExpandReveal.tsx` |

## What it does

文字集结四式——split-text-stagger 逐字裂升、letterform-drift-assembly 漂移合拢、tracking-expand-reveal 字距呼吸、text-on-path 沿线流入

**When to use it.** 大标题/标语的入场；与 type-entrance-moves 两式、split-flap-title、document-typewriter-reveal 同属标题入场大品类，全片 ≤2 种

**Why this shot earns its place.** 标题入场已有"原位变形系"四式（乱码解码/字符坠落/翻牌/打字机——字 在原地换形态）。本卡补"集结系"：字符从别处**汇聚成**标题，运动轨迹 本身有戏。A 琴键式——每字从看不见的裁切线下滑升，理性利落，通用度 最高；B 片头式——字符四散带模糊漂入、逐个锁定加深，Stranger Things 的仪式感，适合品牌名亮相;C 呼吸式——字母从叠压一团吸一口气展开， 最安静的一式，适合抒情段落；D 语义式——字符沿一条上升曲线鱼贯流入 再摆正，曲线可以正好描着图表增长线走，文字与数据同框叙事。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| A 过冲 | 10%（原案 6% 可测不可感，实渲加码） | 正常速度要看得见回落那一下 |
| B 锁定脉冲 | 字色深到 #000 + 描边 0→3px→0 / 8f | 白底上加深+描边，不用发光（判例） |
| B 漂移三绑定 | 位移 (1−p)、blur 8(1−p)、opacity 0.35→1 共用一条 p | 三者分曲线走，字会"到了还糊着" |
| C 实现命门 | letter-spacing 恒为终态，逐字符 span 只做 translateX=(1−p)(i−词心)(−0.56em) | 直接动 letter-spacing 逐帧重排必抖 |
| D 摆正 | 到达停 8f 再 12f lerp 到水平基线（y 拉平 rotate→0） | 不摆正就永远是"挂在线上"，读不出标题 |
| D 曲线 | evolve（dashoffset）随最前字符同步生长 | 曲线先画完字再走，读作两个动画 |
| 收尾 | 全员落定真静止 ≥30f | R1 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 标题入场大品类现已八式（本卡四式 + type-entrance-moves 两式 +
- B 式与 D 式都是高注意力入场，别再叠相机动作——字在飞的时候镜头必须稳
- C 式幅度命门：起始叠压至少 −0.4em 级（每缝 80px+ 位移）才可感， **[命门]**
- D 式字符在曲线低段会短暂交叠，是鱼贯读感的一部分；但字号 >80px 时

## Card structure

`intention` | `variants` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/typography/type-assembly-moves/LetterformDriftAssembly.tsx`
- `demos/typography/type-assembly-moves/SplitTextStagger.tsx`
- `demos/typography/type-assembly-moves/TextOnPath.tsx`
- `demos/typography/type-assembly-moves/TrackingExpandReveal.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
