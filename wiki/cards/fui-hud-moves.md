# fui-hud-moves

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/fui-hud-moves`.

## Identity

- **slug**: `fui-hud-moves` (join key across cards, demos, media and deep links)
- **category**: `effects` — Light & Emphasis / 光效与强调
- **energy**: `A 中 / B 中高` — arc or n/a, not sortable
- **suggested duration**: A 3–4s（含退场）/ B 2–3s → **120 frames @30fps = 4.0s**
- **cross-category tags**: `ui-entrance`, `effects`
- **upstream source**: references/shots/effects/fui-hud-moves.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| A | `line-unfold-panel` | —f | B | `demos/effects/fui-hud-moves/LineUnfoldPanel.tsx` |
| B | `reticle-lock-on` | 24f | B | `demos/effects/fui-hud-moves/ReticleLockOn.tsx` |

## What it does

FUI/HUD 两式——line-unfold-panel 一线展面（线→面 CRT 语法）与 reticle-lock-on 准星咬合（取景框飞入锁定目标）

**When to use it.** 暗场/科技感段落的面板入退场用 A；任何"看这里"的目标点名用 B（替代箭头圈红，画面不冻结）

**Why this shot earns its place.** 科幻虚构界面（Jarvis/Territory）的两个可中性化母题。A 是面板的 仪式感开关机：1px 细线极快抽出→纵向撑开成面板→内容淡入，退场反向 压线缩点熄灭（老 CRT 关机）；灰阶细线即成立，不需要科技蓝。 B 是运动中的捕获：四个 L 形角标从画外冲入、超调回弹、"咔"地咬合 到目标元素四角+弹标签——与 freeze-annotate 分工：那卡冻结画面标注， 本卡在流动中点名。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| A 两段节奏 | 抽线 5f 急 vs 撑面 9f 缓 | 节奏差是手法本体，等长就平了 |
| A 线体 | 白色发光条 3px 级；线/点阶段与面板阶段条件切换 | 熄灭后必须条件卸载才有真静止 |
| B 飞入行程 | 画外 ≥1000px 冲入 | 行程短读作"角标出现"不是"扑过来" |
| B 超调 | 收缩过头到 0.94× 再回弹 1 | 无超调没有"咔"的咬合感 |
| B 咬合帧 | 目标白 overlay 快闪 0.55→停 0.28 + 标签同帧弹出 | 微亮与标签错帧就散了 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- Remotion 无 `Easing.quart`——用 `Easing.poly(4)`（demo 实测报
- B 一支片 ≤2 次：连用读作军事模板；两次锁定目标必须不同
- A 与 glow-flyline 同属暗场词汇，相邻段落别背靠背堆光效（Q4 同源） _(rules Q4)_
- 声音：A 抽线一声短 whoosh、撑开一声轻 pop；B 咬合帧一声"咔"

## Card structure

`intention` | `variants` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/effects/fui-hud-moves/LineUnfoldPanel.tsx`
- `demos/effects/fui-hud-moves/ReticleLockOn.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
