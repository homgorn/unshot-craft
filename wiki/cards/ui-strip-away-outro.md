# ui-strip-away-outro

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/ui-strip-away-outro`.

## Identity

- **slug**: `ui-strip-away-outro` (join key across cards, demos, media and deep links)
- **category**: `outro` — Outro / 收尾
- **energy**: `中` — rank 4/8
- **suggested duration**: ~4.3s（130f：光标就位 34f → 蒸发 ~40f → 按钮独占 → 字标接棒） → **130 frames @30fps = 4.3s**
- **cross-category tags**: `outro`
- **upstream source**: references/shots/outro/ui-strip-away-outro.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `ui-strip-away-outro` | 14f | B | `demos/outro/ui-strip-away-outro/UiStripAwayOutro.tsx` |

## What it does

减法式收尾——点击 Publish 后整个编辑器 UI 从外围到中心层层错峰蒸发，黑场上只剩那颗按钮滑到屏心放大，按钮再淡出交棒字标定版

**When to use it.** "发布/完成"语义的 outro；想讲"一键之后一切复杂性消失"的产品收尾

**Why this shot earns its place.** 库内收尾全是"加法"：outro-group-photo-launch 元素飞来合影，logo sting 是定住再彩蛋。本卡是唯一的"减法"路线——点击引爆全 UI 退场， 黑场只留语义焦点（那颗被点的按钮），把"发布 = 复杂性归零"翻译成 动效叙事。命门有二：**蒸发要有秩序**——从外围到中心每 4f 一层、 每层带方向性位移（各自往画外散），乱序或同帧齐灭读作断电故障； **按钮是唯一幸存者且必须迁移**——蒸发期间从工具条角落滑到屏心 放大 1.5 倍、白晕随黑场增强，完成从"UI 控件"到"仪式主角"的升格， 最后淡出把黑场交给字标。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 层间错峰 | 4f × 6 层 | 同帧齐灭读作断电；>8f 拖成慢拆迁，仪式感散 |
| 单层时长 | 14f，ease-in 加速 | ease-out 离场读作"飘走"不读作"蒸发"；>20f 黏 |
| 蒸发顺序 | 外围 → 中心，按钮所在层最后 | 中心先空读作故障；按钮层先走全卡崩塌 |
| 位移幅度 | 50–140px，方向各自向画外 | 无位移纯 fade 读作调透明度；同方向读作整屏平移 |
| 按钮迁移 | 18f 滑到屏心 + scale ×1.5 + 晕光增强 | 不迁移则黑场上一颗角落小钮，读作漏删；先迁后灭顺序不可反 |
| 字标接棒 | 按钮淡出后 ~10f 进，spring 定版 | 与按钮同屏抢戏；黑场空窗 >20f 像放完了 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 与 outro-group-photo-launch 分工：全家福是"加法"峰值终镜（多功能
- 与 edit-hook-moves B（logo-sting-button）衔接：本卡字标定版后可接
- 蒸发的每层必须是**语义完整的 UI 区块**（侧栏/面板/工具条），按
- 按钮迁移全程 zIndex 压最顶——任何蒸发层从按钮前面飘过都是穿帮
- 触发动作必须是"终结性"语义（Publish/Ship/Done）；拿 Save 或普通
- 实战按钮用品牌高亮色（原片是 Framer 蓝），demo 的白钮只是灰阶占位

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/outro/ui-strip-away-outro/UiStripAwayOutro.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
