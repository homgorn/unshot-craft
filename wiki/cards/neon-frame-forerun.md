# neon-frame-forerun

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/neon-frame-forerun`.

## Identity

- **slug**: `neon-frame-forerun` (join key across cards, demos, media and deep links)
- **category**: `ui-entrance` — UI Entrance & Showcase / 界面登场与陈列
- **energy**: `中高` — rank 5/8
- **suggested duration**: 框奔画 ~0.6s + 点亮&贴落 ~2s + 背景熄灭收束 ~0.8s；全段 4–4.5s → **18 frames @30fps = 0.6s**
- **cross-category tags**: `ui-entrance`, `effects`
- **upstream source**: references/shots/ui-entrance/neon-frame-forerun.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `neon-frame-forerun` | —f | B | `demos/ui-entrance/neon-frame-forerun/NeonFrameForerun.tsx` |

## What it does

强透视直角霓虹框自左缘两头奔画先行成型，页面在框内由暗转亮，同时框内组件/文字从 3D 上空带同形软影错峰贴落、随页面点亮同步完成贴合，背景霓虹管群终段熄灭让位

**When to use it.** 暗场品牌片里给 UI 面板做"登场仪式"（框先到、内容后落）；功能区首次亮相；霓虹/赛博调性的段落开场

**Why this shot earns its place.** 先立框后填肉：霓虹线框像跑道灯一样两头奔画圈出位置，宣告 "这里要出现东西"；页面在框内由暗转亮的同时，组件从空中带影 贴落——观众看见界面被"安放"进框里。三层动作（框奔画/页面点亮/ 组件贴落）必须**同步咬合**：贴落进程与点亮进程同步推进、稍滞后 收尾，框光最终并入面板辉光。背景霓虹管群终段熄灭，把亮度让给 主角完成收束。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 框奔画 | ~18f 两头对奔 | 单头描画读作画图；>30f 观众等不及内容 |
| 悬浮高度 | 100–150px、影随高度收敛 | 判例：高度过小+启动过早=影子不可感（v3 第 1 轮返工加大 1.7x 并延后） |
| 贴落窗口 | 与点亮窗口同步、滞后 ~20f 收尾 | 贴落先于点亮完＝黑屋子里落家具；滞后太多读作两段戏 |
| 错峰 | 错开起点、下落重叠并行 | 串行等待被裁（掉落节奏通用判例） |
| 背景熄灭 | 终段中亮尾熄 ~22f | 不熄灭主角不突出；同帧全熄读作断电 |
| 贴落粒度 | 行/卡级（原片为逐 UI 卡片级，更细） | 粒度越细越贵；行级已验证可读 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 悬空贴落=clickup 语言核心签名（已验证的口味信号），本卡
- 与 brand-frame-snap 分工：那张是品牌框咔哒定位的
- 衍生方向备忘：视角旋转变体（镜头左→右弧线旋转+同时贴落）

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/ui-entrance/neon-frame-forerun/NeonFrameForerun.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
