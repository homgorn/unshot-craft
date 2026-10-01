# cursor-flyover

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/cursor-flyover`.

## Identity

- **slug**: `cursor-flyover` (join key across cards, demos, media and deep links)
- **category**: `camera` — Camera & Space / 运镜与空间
- **energy**: `中` — rank 4/8
- **suggested duration**: 约 6.0s（180f@30fps；俯瞰 0–1.2s · 四步各 0.7s 过渡 + 0.5s 停留） → **180 frames @30fps = 6.0s**
- **cross-category tags**: `camera`
- **upstream source**: references/shots/camera/cursor-flyover.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `cursor-flyover` | 180f | A | `demos/camera/cursor-flyover/CursorFlyover.tsx` |

## What it does

整页俯瞰淡入后，相机依次飞到四个角落 zoom-in 特写，SVG 光标同步跟到位指点并留下点击涟漪

**When to use it.** 单页产品的功能巡览：一镜带观众看完四个功能区，光标当"导游手指"

**Why this shot earns its place.** 替代"四个功能四段剪辑"的省镜方案：一个连续相机把四个角串成一条参观动线，光标是观众的注意力代理——它到哪、点哪，观众就看哪。空间连续让功能之间的位置关系也被顺带记住。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 特写倍率 | s=1.72（俯瞰 0.8） | >2.2 时占位截图纹理会糊，换真实高分截图后可推到 2.5 |
| 步进节奏 | 过渡 0.12 / 停留 0.08 | 停留是读功能位，短于 0.05 变"扫过"没有"参观" |
| 点击涟漪 | 0.055 时长，scale 0.3→1.9 | 涟漪是节拍器，四次点击均匀落在 0.32/0.52/0.72/0.91——配 SFX click 四连 |
| 光标补偿 | scale(1/s) | 砍掉则特写时光标巨大化；保持"光标是 UI 层"的错觉必需 |
| 巡览顺序 | 左上→右上→右下→左下（Z 形反向） | 改 CAM 表即换路线；保持相邻角相邻访问，对角跳跃会晕 |
| 开场聚焦 | 0–0.14 blur 5px→0 | 与俯瞰同拍完成"这是全景"的交代；直接从特写开跳过它 |

## Known pitfalls

- 占位截图（窗口 chrome+侧栏+四象限控件）必须换成真实产品截图，四个 cx/cy 光标落点要重新标到真实控件中心
- 相机表的 tx/ty 是内容百分比坐标，截图宽高比变了（如换竖屏）需整表重标
- 光标与相机绑定同一插值意味着"光标先飞相机后到"这类编排做不了——需要解耦时给光标单独一张同结构的表
- 停留段完全静止，1080p 大屏下会显得"卡住"——可给 world 加 ±0.5px 的呼吸位移（确定性 sin），但幅度别过 1px

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/camera/cursor-flyover/CursorFlyover.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
