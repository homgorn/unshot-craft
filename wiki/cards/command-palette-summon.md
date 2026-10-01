# command-palette-summon

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/command-palette-summon`.

## Identity

- **slug**: `command-palette-summon` (join key across cards, demos, media and deep links)
- **category**: `interaction` — Interaction & Feature Demo / 交互与功能演示
- **energy**: `中` — rank 4/8
- **suggested duration**: 4–5s → **150 frames @30fps = 5.0s**
- **cross-category tags**: `ui-entrance`, `interaction`
- **upstream source**: references/shots/interaction/command-palette-summon.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `command-palette-summon` | 104f | B | `demos/interaction/command-palette-summon/CommandPaletteSummon.tsx` |

## What it does

命令面板降临——整屏压暗加模糊，⌘K 面板带过冲弹落，候选行错峰浮现，敲字列表实时收窄

**When to use it.** 效率型产品的"全产品在一个输入框里"叙事；命令面板/搜索/快捷键功能的标志性登场

**Why this shot earns its place.** Raycast/Linear 发布片的标志性仪式：一声轻响，整个 UI 世界压暗 让路，⌘K 面板从中心上方弹落，候选列表错峰浮现；敲两个字母， 列表实时收窄——"你要的一切都在这个输入框里"。模拟交互按真人 操作速度走（R3），收窄的"挤压感"来自行高塌缩而非淡出。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 压暗 | 亮度 45% + blur 10px，10f | 压不够面板不突出；全黑失去上下文 |
| 弹落 | 起点上方 20px，overshoot 一拍回正 | 无过冲读作淡入，仪式感没了 |
| 候选错峰 | 4f/行 | 同帧出读作贴图 |
| 收窄 | height→0 + overflow hidden 塌缩 | 淡出收窄没有"挤压"感；塌缩完必须卸载 |
| 光标 | 闪烁周期 16f；定格后强制常亮 | 闪到结尾就永不真静止（demo 判例） |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 输入节奏按真人打字速度（R3 判例），两键间隔 ≥12f _(rules R3)_
- 组合款见 theme-switch-moves B 式（面板收缩成点引发主题涟漪）
- 实战候选行放真实功能名——这是功能清单的天然展位（P4 映射） _(rules P4)_
- 声音：唤出一声轻响（非游戏音），按键 2 声键帽拟音，

## Card structure

`intention` | `phases` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/interaction/command-palette-summon/CommandPaletteSummon.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
