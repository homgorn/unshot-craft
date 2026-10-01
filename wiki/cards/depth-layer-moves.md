# depth-layer-moves

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/depth-layer-moves`.

## Identity

- **slug**: `depth-layer-moves` (join key across cards, demos, media and deep links)
- **category**: `camera` — Camera & Space / 运镜与空间
- **energy**: `视差=中` — arc or n/a, not sortable
- **suggested duration**: 视差滑轨 4–5s 持续；dolly-zoom 3–4s 单向行程 → **150 frames @30fps = 5.0s**
- **cross-category tags**: `camera`
- **upstream source**: references/shots/camera/depth-layer-moves.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `dolly-zoom-real` | 135f | B | `demos/camera/depth-layer-moves/DollyZoomReal.tsx` |
| — | `multiplane-real` | 135f | B | `demos/camera/depth-layer-moves/MultiplaneReal.tsx` |

## What it does

分层深度两款运镜——多层视差滑轨（3 层速度梯度横移出纵深）与伪 dolly-zoom（主体钉死、背景膨胀压来）

**When to use it.** 平面截图要"有厚度"的段落；戏剧性蓄力时刻用 dolly-zoom（一支片 ≤1 次）

**Why this shot earns its place.** 整页平移是"看页面"，分层深度是"在页面的空间里"。视差滑轨给横移 加纵深（迪士尼多平面摄影机原理，Linear 片同款质感）；伪 dolly-zoom 反过来——主角纹丝不动、全世界压过来，给戏剧性时刻蓄力。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 视差层系数 | 0.35 / 0.7 / 1.4 | 梯度 ≥2 倍层间才可辨；层数 ≤4 防过载 |
| 层次锚 | 前后景 blur + 背景降饱和 | 没有 blur/饱和锚，读作"贴片乱飞" |
| dolly 膨胀行程 | scale 1→2.0–2.5 | 行程小了压迫感不足；背景 opacity ≤0.6 防读作故障 |

## Known pitfalls

- 主阅读层/主体必须高清纹理且无 blur——观众在读它
- 视差与 PageCam rot 3D 的组合（斜拍视差）未验证，实战先渲 still 确认
- dolly-zoom 是"戏剧调料"：一支片 ≤1 次，日常段落用视差滑轨
- 参数经占位素材调校转正，非实战定稿，首次实战后回验

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/camera/depth-layer-moves/DollyZoomReal.tsx`
- `demos/camera/depth-layer-moves/MultiplaneReal.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
