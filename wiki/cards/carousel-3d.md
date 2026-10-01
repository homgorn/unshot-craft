# carousel-3d

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/carousel-3d`.

## Identity

- **slug**: `carousel-3d` (join key across cards, demos, media and deep links)
- **category**: `ui-entrance` — UI Entrance & Showcase / 界面登场与陈列
- **energy**: `中` — rank 4/8
- **suggested duration**: 约 5.6s（168f@30fps） → **168 frames @30fps = 5.6s**
- **cross-category tags**: `ui-entrance`
- **upstream source**: references/shots/ui-entrance/carousel-3d.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `carousel-3d` | 168f | A | `demos/ui-entrance/carousel-3d/Carousel3D.tsx` |

## What it does

8 张卡按 sin/cos 排成半径 190px 的圆环并匀速整环自转一圈，每卡只绕 Y 公转、自身 billboard 朝外，正反两层同向贴图配 backface-visibility:hidden 保证任何时刻都正立不倒置，相机全程钉在浅俯角近景

**When to use it.** 作品集/模板库/集成清单的循环展示；需要无缝 loop 的背景拍或落地页 hero

**Why this shot earns its place.** 展示"一组东西"最省事的办法是排成一排横滑，但横滑有起点和终点。环形没有——它天然 循环，观众看多久都不会觉得"放完了"。这张卡真正要解决的是环形 carousel 最容易翻车 的点：卡片背面。方案是双面同向贴图，所以从环内看和从环外看是同一张正立的卡，环转一圈 不会有任何一帧出现镜像或倒置。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 卡数 | N=8（方位角间隔 45°） | 8 张在 190px 半径上前后互不遮挡；>12 张卡会互相压边，需要同步加大 RADIUS |
| 半径 | RADIUS=190px（卡 92×124） | 半径/卡宽 ≈2 是疏密甜点；<1.5 倍时环背面的卡从正面卡的缝里挤出来，画面变乱 |
| 自转速度 | `t*360` = 全片 1 圈 | 圈数必须是整数才能 loop；改成 2 圈会快一倍但仍无缝，非整数则末帧跳变 |
| 透视 | `perspective: 950px` | 950 相对 190 半径是较平的透视；调到 500 以下近处卡会夸张放大，读作鱼眼 |
| 相机俯角 | `rotateX(-8deg)` | -8° 只是"略微俯视"，刚好露出地面盘；>-20° 环会压扁成椭圆，卡的正立感被透视削弱 |
| 相机推近 | `translateZ(-90px)` | 负值是把相机拉后（环显小）；正值推近会让近处卡撞出画框 |
| 卡尺寸 | 92×124（`left:-46px, top:-62px` 自居中） | 尺寸与负偏移是绑定的一对，改尺寸必须同改偏移，否则整环偏心 |
| 地面盘 | 460×460，`rotateX(90deg)`，14% 透明度 | 直径约 2.4 倍半径才能兜住整环；透明度 >30% 会读作实体地板而不是反光 |

## Known pitfalls

- 匀速无变化是这张卡的特性也是限制：**它没有开头也没有结尾**。当主镜用会显得平，
- 每帧都重设了 8 张卡的 transform 但值是恒定的（`rotateY(c.base) translateZ(RADIUS)`）
- `backface-visibility:hidden` 在部分 WebKit 下需要 `-webkit-` 前缀（代码里已双写）。
- 卡面是几何字符 + `CARD 0X` 编号 + 两条骨架条的占位，hue 从 200 起每张 +22 是演示用
- 环转到背面时卡是"背对观众的正面"（看的是 back 层），所以内容始终可读——但也意味着
- 深色径向背景（`#131120`→`#0a0b10`）+ 卡的内阴影高光是一套；换白底后 `0 12px 34px

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/ui-entrance/carousel-3d/Carousel3D.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
