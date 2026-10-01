# neon-frame-orbit-drop

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/neon-frame-orbit-drop`.

## Identity

- **slug**: `neon-frame-orbit-drop` (join key across cards, demos, media and deep links)
- **category**: `ui-entrance` — UI Entrance & Showcase / 界面登场与陈列
- **energy**: `中高` — rank 5/8
- **suggested duration**: 描框 ~0.5s + 旋转&同时贴落 ~2.5s + 落定 ~1s；全段 4–4.5s → **15 frames @30fps = 0.5s**
- **cross-category tags**: `ui-entrance`, `camera`, `effects`
- **upstream source**: references/shots/ui-entrance/neon-frame-orbit-drop.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `neon-frame-forerun-orbit` | —f | B | `demos/ui-entrance/neon-frame-orbit-drop/NeonFrameForerunOrbit.tsx` |

## What it does

霓虹框先行描框后，镜头绕页面左→右弧线旋转，页面全部组件/文字**同帧**从空中往下贴合（同形软影同步收敛）——整体登场式的框内安放

**When to use it.** 单页 UI 的一次性隆重登场（与巡礼/逐区亮相相对）；暗场霓虹调性段落的主视觉揭幕；neon-frame-forerun 的姊妹镜

**Why this shot earns its place.** neon-frame-forerun 的孪生变体：同样框先行、内容后落，但镜头 不是固定的——从页面左侧视角连续弧线旋转到右侧视角，旋转进行 的同时全部组件从空中贴落。命门是**同时贴合**：所有组件和文字 同帧起落、同帧贴合、软影同步消失——这是"整体登场"的语法 （判例：错峰版被裁"应该是所有组件和文字同时从空中往下贴合"）。 错峰贴落属于巡礼镜（graze-face-tour/runway），一页一次性亮相 必须齐落，节奏语义不能混用。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 贴落同时性 | 全元素同帧起落（零错峰） | **命门**；任何错峰都会读成巡礼语法（判例裁决原话见上） |
| 视角弧线 | rotateY +38°→-26°、透视原点随动 | 弧度小读作抖动；只转不落=空转 |
| 旋转×贴落耦合 | 贴落窗口居中于旋转行程 | 旋转完才落=两段戏；落完还在转=收不了尾 |
| 悬浮高度/软影 | 同 graze-face-tour（100–180px、影随高度） | 影不可感=没做（累计判例） |
| 描框 | ~14f 奔画 | 同 neon-frame-forerun |

## Known pitfalls

- 参数经占位素材两轮调校通过，非实战定稿，首次实战须以真实素材回验
- **贴落节奏语义判例**（本卡与 graze-face-tour 互为反例）：
- 与 neon-frame-forerun 分工：那张镜头固定、错峰贴落+页面点亮
- 弧线旋转是透视原点近似而非真实 3D 相机环绕，极端角度下框辉光

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/ui-entrance/neon-frame-orbit-drop/NeonFrameForerunOrbit.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
