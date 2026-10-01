# typing-code-block

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/typing-code-block`.

## Identity

- **slug**: `typing-code-block` (join key across cards, demos, media and deep links)
- **category**: `typography` — Typography & Title Cards / 文字与字卡
- **energy**: `中` — rank 4/8
- **suggested duration**: 约 4.6s（138f@30fps） → **138 frames @30fps = 4.6s**
- **cross-category tags**: `typography`
- **upstream source**: references/shots/typography/typing-code-block.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `typing-code-block` | 138f | A | `demos/typography/typing-code-block/TypingCodeBlock.tsx` |

## What it does

同一段语法高亮代码左右并置两种 reveal——左侧行级 stagger 4f 淡入上浮 8px，右侧逐字符打字但字符保持原 token 色，当前字符垫一块 #3a4468 方块光标

**When to use it.** 代码/配置揭示镜头；开发者产品的"就三行"演示；需要对比两种揭示节奏时的选型参考镜

**Why this shot earns its place.** 代码揭示只有两种真解法：**整行浮出来**（读的是结构）和**一个字一个字打** （读的是过程）。这卡把两者并排放在同一段代码上，是选型用的对照镜： 左侧 4 行 4 拍就完，适合"代码不是重点、结果才是"；右侧 138 帧才打完 59 个字符，适合"看我写"。关键细节是右侧**打字不丢色**——常见错误是 打字时先出白字再着色，那就退化成终端回显，不是代码编辑器。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 代码量 | 4 行 / 约 59 字符 | 打字速度 = 字符数 / 113f；行数超过 6 行面板要缩字号，超过 100 字符右侧打不完 |
| 行 stagger | 0.14（≈19f），单行窗 0.3（≈41f） | 19f 是"逐行"可读下限；<8f 四行齐亮没有 stagger，>28f 最后一行等太久 |
| 行位移 | `(1-k)·8`px 上浮 | 8px 是代码块该有的克制幅度；>20px 行像卡片飞进来，抢了代码本身 |
| 打字窗 | `seg(t, 0.08, 0.9)`（11f→124f） | 结束点留 14f 静置读全文；推到 1.0 打完即切，最后一行没人读 |
| 光标块 | `#3a4468` 背景，仅当前字符 | 方块光标是编辑器语感；换成竖线要另加闪烁，代码块里反而更碎 |
| 面板 | 45%×72%、`#10121a` 底、`#1c2030` 边框、圆角 8、12px/1.9 行高 | 1.9 行高是代码可读下限；两侧必须同规格，尺寸不一就不是对照而是两个镜头 |
| 空行占位 | 右侧行 `min-height:1.9em` | 不设则面板随打字长高，整块跳版——这是本卡最容易漏的一处 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- **换成项目代码时字符总数要贴近 59**：右侧打字是把 113f 平摊到全部
- 着色必须在 setup 期写进每个 span：render 期改色（先白后染）会把
- 左侧行级淡入与右侧逐字符**不同步**（左侧 4 行 ~68f 就收完，右侧要打到
- token 数组是手写的，没有真词法分析——换代码时得手动切 token；
- 实战里通常**只留一侧**：对照版是选型镜，正片里两块面板一起动会分散

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/typography/typing-code-block/TypingCodeBlock.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
