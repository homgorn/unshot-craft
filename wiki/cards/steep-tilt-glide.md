# steep-tilt-glide

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/steep-tilt-glide`.

## Identity

- **slug**: `steep-tilt-glide` (join key across cards, demos, media and deep links)
- **category**: `camera` — Camera & Space / 运镜与空间
- **energy**: `中高` — rank 5/8
- **suggested duration**: 4s（120f）单镜；页面越宽越可拉长 → **120 frames @30fps = 4.0s**
- **cross-category tags**: `ui-entrance`, `camera`
- **upstream source**: references/shots/camera/steep-tilt-glide.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `steep-tilt-glide` | —f | B | `demos/camera/steep-tilt-glide/SteepTiltGlide.tsx` |

## What it does

固定镜头下直立页面以 60° 强透视侧立（右近左远），页面自身沿其 3D 横面方向滑移掠过镜头（物动镜不动），滑移带速度重影、文字组件悬空贴落、由暗揭亮

**When to use it.** 长页面/多区块 UI 的炫技巡览（内容依次滑过固定机位）；暗场霓虹调性；与贴面运镜卡互补的"侧掠"机位

**Why this shot earns its place.** 把页面立成一堵斜墙：镜头钉死不动，60° 强透视让右缘贴脸、左缘 消失在灭点，页面自己沿自身平面横向滑移——内容像列车车厢一样 依次掠过。命门是**物动镜不动**：perspective/origin/rotY 全程常数， 唯一动的量是页面局部 translateX——镜头一动语义就变成运镜炫技， 这里的戏是"页面在自我展示"。角度经三轮收敛为精确 60° （-45°"不对"→-53°"再大一点"→-60°选中）。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 倾斜角 | rotateY **-60°**（用户精确定值） | -45° 被裁"角度不对"、-53°"再大一点"；>-70° 内容读不清 |
| 运动模型 | 镜头全常数、页面自移 | **命门**——镜头横移版被裁"镜头是固定的，页面本身往其3d空间的横面方向移动" |
| 滑移曲线 | 尾段斜率不归零的 bezier | 中途停死被抓（v4 返工）；全 linear 少了起步呼吸 |
| 重影 | 透明度∝速度，双层 f-2.5/f-5 | 恒定重影读作重像故障 |
| 页面宽度 | ≥3 屏内容 | 太窄滑两秒就完，撑不起一镜 |
| 悬空贴落 | 错峰（巡礼语法）+ 影随高度 | 语义判例见 graze-face-tour/orbit-drop 三卡族 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 角度判例：透视角是本卡身份，实战微调范围建议 55–65°，出这个
- 与 graze-face-tour 分工：那张镜头动（贴面游走）、页面静；本卡
- 与 runway-ground-skim 分工：那张是俯角平躺+垂直贴落+立起；
- 超宽页面手绘成本高；实战可用真实长截图代替（滑移逻辑不变）

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/camera/steep-tilt-glide/SteepTiltGlide.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
