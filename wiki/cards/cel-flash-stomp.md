# cel-flash-stomp

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/cel-flash-stomp`.

## Identity

- **slug**: `cel-flash-stomp` (join key across cards, demos, media and deep links)
- **category**: `typography` — Typography & Title Cards / 文字与字卡
- **energy**: `高` — rank 6/8
- **suggested duration**: 每词 ~30f × 词数 + 收尾 ≥45f；三词约 4.8s → **30 frames @30fps = 1.0s**
- **cross-category tags**: `typography`, `rhythm`
- **upstream source**: references/shots/typography/cel-flash-stomp.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `cel-flash-stomp` | —f | B | `demos/typography/cel-flash-stomp/CelFlashStomp.tsx` |

## What it does

底色闪砸字——大词逐拍像图章歪着砸满屏，每词落定瞬间背景层在两个纯色间频闪数帧而文字纹丝不动；动漫必杀技字卡的 UI 翻译

**When to use it.** 口号/三连词的高能段落（"SHIP / FASTER / TODAY"式）；文字节奏卡，与 type-rhythm-sync 互补（那是字属性动，这是字砸+底闪）

**Why this shot earns its place.** 逐词砸字（stomp typography）单用只有重量；背景纯色闪（动漫背景 フラッシュ——必杀技名出现时底色交替闪）单用只是闪。焊在一起互补 成立：词砸下的落定帧正是底闪的起爆帧，**主体稳、背景闪**——观众 盯着字，眼角余光里整个世界在震颤，打击感来自周边视野而不来自主体 抖动。这是与震屏完全相反的路线：震屏晃主体，本卡晃世界。三词逐拍 递进，末词闪加倍+标签条收束，一句口号剪成三记盖章。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 词时长 | ~30f/词，3–4 词 | <22f 读不完词；5+ 词读作 rap 字幕（那去用 karaoke） |
| 砸落 | 6f scale 1.18→1 + 2% 过冲 | 幅度 >1.3 起步会先读到"缩小动画"再读到"砸" |
| 歪角 | ±2.5° 交替，末词归 0° | 同方向连歪读作版式错误 |
| 底闪 | 2f 交替 × 6f；末词 8f + 对比拉大 | 闪 >10f 读作背景故障；1f 交替在 30fps 下读不出色差 |
| 标签条 | 末词闪结束同帧起 14f 淡入 | 早于末闪出现会被闪没 |
| 收尾 | 末词落定真静止 ≥45f | R1；重拳双倍 hold |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- **声音强依赖**：每词砸落一声 kick、底闪对齐鼓点（sound-design
- 底闪层里不许有任何内容元素（logo/纹理都不行）——闪的必须是
- 与 background-cel-flash 单用（关键词驻场只闪底）的区别：本卡词
- 与 beat-cut-moves A（递进硬切串）能量档相同且都是"切+拍"，
- 实战品牌色版：底闪两色用品牌色对（如强调色×深墨），对比度须 ≥

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/typography/cel-flash-stomp/CelFlashStomp.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
