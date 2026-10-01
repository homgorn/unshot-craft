# sakuga-timing-shift

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/sakuga-timing-shift`.

## Identity

- **slug**: `sakuga-timing-shift` (join key across cards, demos, media and deep links)
- **category**: `rhythm` — Rhythm & Montage / 节奏与蒙太奇
- **energy**: `中高` — rank 5/8
- **suggested duration**: ~5s → **150 frames @30fps = 5.0s**
- **cross-category tags**: `ui-entrance`, `rhythm`
- **upstream source**: references/shots/rhythm/sakuga-timing-shift.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `sakuga-timing-shift` | —f | B | `demos/rhythm/sakuga-timing-shift/SakugaTimingShift.tsx` |

## What it does

一拍三转一拍一——元素先以每 3 帧一步的手翻书顿挫移动，高潮瞬间切成逐帧丝滑冲刺，帧率量化的突变本身就是看点

**When to use it.** 单元素的强调性位移（卡片入场、指标冲线）；需要"手工感→高潮爆发"反差的段落

**Why this shot earns its place.** 库内时间轴操纵已有 speed-ramp 连续变速与 hit-counter 的局部顿帧。 本卡是另一种——**改的不是速度是帧率本身**： 顿挫段驱动帧 q=floor(f/3)*3，元素每 3 帧才动一步（10fps 手翻书）， 切换帧起改用原始 f 逐帧驱动，丝滑冲刺。一拍三的钝与一拍一的滑 同屏对切，日式作画的拍数演出（shooting on 3s / on 1s）。顿挫段 不是低级感是手工感，切换点即高潮标记。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 拍数 | 顿挫段 floor(f/3)（一拍三） | /2 顿感不足、/4 以上读作播放器卡死 |
| 每步位移 | ≈79px（总程 ÷ 步数倒推） | <30px 读作卡顿掉帧不是顿挫——命门 |
| 步间姿势 | sin(q) rotate ±5° | 无姿势变化的纯位移顿挫像 bug 不像手翻书 |
| 切换帧 | f48（顿挫:冲刺 ≈ 3:2） | 切换必须一帧完成，任何补间都毁掉"换拍"感 |
| 冲刺缓动 | Easing.out(poly(4)) + 过冲 36px + 3f 回弹 | 初速要猛，与顿挫段拉满反差 |
| 收尾 | 真静止 ≥42f，角标沸腾同步冻结 | 沸腾残留毁真静止（feTurbulence 摘罩判例同族） |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 同一镜头单一时间操纵者判例：与 speed-ramp / hit-counter 顿帧
- 顿挫段每步位移 ≥30px 才读得出"顿"——微步顿挫读作渲染掉帧，
- 切换点必须有标注（角标 "on 3s"→"on 1s" 或一声打点，

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/rhythm/sakuga-timing-shift/SakugaTimingShift.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
