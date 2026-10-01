# text-column-converge

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/text-column-converge`.

## Identity

- **slug**: `text-column-converge` (join key across cards, demos, media and deep links)
- **category**: `typography` — Typography & Title Cards / 文字与字卡
- **energy**: `中低` — rank 3/8
- **suggested duration**: 轮换 7–16f/词 × 8–9 词 + 合拢 ~36f + 小字后静置；全段约 5–6s → **16 frames @30fps = 0.5s**
- **cross-category tags**: `typography`, `outro`
- **upstream source**: references/shots/typography/text-column-converge.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `text-column-converge` | 36f | B | `demos/typography/text-column-converge/TextColumnConverge.tsx` |

## What it does

双词对峙合拢——左"NEW"右特性词钉死在等屏边距两侧硬切轮换、全程零收缩，换到最后一词才唯一一次 ease-in-out 滑到居中咬合成短语，下方小字近乎硬切浮现；收尾揭晓型文字卡

**When to use it.** 特性清单收束到产品名/口号的段落（"NEW × 一串特性 → NEW <产品名>"式）；发布会式 recap、版本号揭晓

**Why this shot earns its place.** 两词分踞左右像目录页对峙，观众以为只是轮换字幕；直到最后一词 停稳才发现左右其实是同一句话的两半——唯一一次连续合拢把整段 轮换追认为"悬念铺垫"。命门是**钉死**：轮换期两词位置一像素不动、 左右屏边距完全相等（原片实测 412 vs 413@1280），任何渐进收缩都会 提前剧透合拢、把揭晓稀释成进度条。合拢只许发生一次，且必须在 最后一词之后——这是收尾揭晓，不是持续动效。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 屏边距 | 618px@1920（**原片实测** 412/413@1280 ×1.5） | 左右差 >2px 读作没对齐；边距是本卡身份，别改成黄金分割 |
| 词停留 | 7–16f 不均 | 均匀停留读作节拍器；<7f 读不完词 |
| 合拢触发 | 末词停稳 +10f（原片 32.4→32.7s 实测） | 停稳期太短，观众没意识到"这词不换了"就开始滑 |
| 合拢时长 | 36f ease-in-out cubic（**原片实测** ~1.2s 连续滑动） | <24f 读作弹跳归位；>50f 读作拖 |
| 咬合步进 | 0.6em+letterSpacing/字符，等宽字体 | 非等宽字体步进不可预测，会重叠或漏缝 |
| 字号 | 42@1080p（**原片实测**字高 ~20/720） | 这段是小字规格清单气质，放大到 60+ 就成了砸字（去用 cel-flash-stomp） |
| 小字浮现 | 定格 +18f，4f 快淡零位移（原片 34.4→34.6s 间直接出现） | 加滑入/长淡入就抢了合拢的戏 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 与 type-rhythm-sync（字属性节拍）/beat-cut-moves（硬切节拍）撞
- 合拢只许一次——每切一词收一档的渐进收缩版已被原片对照证伪并
- 必须等宽字体（demo 用 SF Mono）；比例字体下咬合终点算不准
- 与原片残余差距：原片词换瞬间带 1 帧亮度闪烁（打字机换行感），

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/typography/text-column-converge/TextColumnConverge.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
