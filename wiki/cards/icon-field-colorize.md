# icon-field-colorize

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/icon-field-colorize`.

## Identity

- **slug**: `icon-field-colorize` (join key across cards, demos, media and deep links)
- **category**: `opening` — Opening & Brand / 开场与品牌
- **energy**: `中` — rank 4/8
- **suggested duration**: 浮现 ~45f 错峰 + 静置 ~10f + 翻色 12–45f + 终态静置；全段 3–4s → **45 frames @30fps = 1.5s**
- **cross-category tags**: `opening`, `ui-entrance`, `outro`
- **upstream source**: references/shots/opening/icon-field-colorize.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `icon-field-colorize` | —f | B | `demos/opening/icon-field-colorize/IconFieldColorize.tsx` |

## What it does

灰阶小图标点阵错峰浮现铺满全屏，停一拍后多道品牌色横带波纹极快向下扫翻全场——"功能全景先摆满，品牌一瞬间点亮"的开场/收束卡

**When to use it.** 开场铺陈产品能力面（图标=功能宇宙）再一举打上品牌色；功能集合页、生态/集成规模展示、片头 logo 前垫场

**Why this shot earns its place.** 先用灰阶把"多"摆足——上百个小图标错峰浮进来铺满画面，灰阶保证 读作背景纹理不抢戏；停一拍让观众意识到"摆满了"，然后品牌色以 横带波纹形式极快扫过全场，灰世界一瞬间被点亮。命门在**翻色不是 同帧硬翻**：原片实测是 ~0.5s 内多道色波依次向下快扫（蓝先覆盖全场， 橙/绿/红依次覆盖更低行带），终态呈四色横带分层——波纹感让"点亮" 有方向和速度，硬翻只读作换了张图。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 图标数 | 170（17×10 @1080p，CELL 110px） | <100 读不出"原野"；>250 单个太小翻色 pop 看不见 |
| 浮现总长 | ~45f（10 批 × 4f + 尾批淡入 8f） | 太快读作闪现；>60f 观众等不及爆点 |
| 翻色总长 | 原片 ~12f 全场完成；demo 45f | 越快越爆；教学/慢节奏场合才拉长 |
| 波数 | 4 道（对应终态色带数） | 1 道=单色点亮也成立；波色=品牌色板 |
| 行差 | 1.4f/行 + 列 0.25f 微倾 | 行差 >3f 波读作逐行扫描仪；0 = 硬翻 |
| 翻色 pop | 1.22x 正弦 3f | 无 pop 波前沿读不出来；>1.4x 图标互相打架 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- **翻色不许同帧硬翻**——原片密帧核实为多道波纹快扫（bear-app
- 图标需可辨认的实心简笔形（心/星/闪电/对勾…）；抽象色块读不出
- 与 bubble-swarm-takeover 分工：那张是气泡群涌入接管
- 与 theme-switch-moves 分工：那张是 UI 界面明暗主题切换；本卡

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/opening/icon-field-colorize/IconFieldColorize.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
