# marker-underline-title

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/marker-underline-title`.

## Identity

- **slug**: `marker-underline-title` (join key across cards, demos, media and deep links)
- **category**: `typography` — Typography & Title Cards / 文字与字卡
- **energy**: `低` — rank 1/8
- **suggested duration**: 标题落定 +4~8f 后起笔，划线 8–12f，总 1–1.5s → **12 frames @30fps = 0.4s**
- **cross-category tags**: `typography`
- **upstream source**: references/shots/typography/marker-underline-title.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `marker-underline-title` | —f | B | `demos/typography/marker-underline-title/MarkerUnderlineTitle.tsx` |

## What it does

大标题落定后，关键词下方马克笔下划线从左到右快速描画——变宽笔形、毛糙边缘、微上斜跟随斜体字势，贴着字底

**When to use it.** 标题里强调单个关键词（new/free/AI…）；手写感/人味的品牌调性；正文标注式强调

**Why this shot earns its place.** 打印体标题里突然出现一笔手绘马克笔，用材质反差把一个词从 排版里拎出来——像人拿笔在海报上圈重点。命门有三：**快** （8–12f 一笔呵成，慢了读作加载条）、**近**（贴着字底，离远了 读作分隔线不是强调）、**跟字势**（斜体词的划线必须左低右高 微上斜——斜向画反是最容易犯且一眼假的错，判例见已知坑）。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 划线时长 | 10f（原片实测节奏；14f 版被裁偏慢） | >14f 读作进度条；<6f 看不见笔迹方向 |
| 字底距离 | ≈-0.1em（从 -40 收到 -20@1080p 才贴住字势） | 离远读作分隔线；碰到字底降部又乱 |
| 斜向 | 左低右高微上斜（跟斜体） | **画反（左高右低）一眼假**——返工判例 |
| 笔宽 | 中段 ~0.12em，首尾 ~0.6x | 等宽读作机器线；差异>2x 读作书法 |
| 毛糙度 | 边缘轻噪声 | 太糙读作故障；全平滑读作 CSS border |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 与 draw-svg-trace 撞领域（有意单列为两卡）：那张是通用
- 斜向判例：v1 左高右低被比对环节抓出——划线斜向必须跟字势，
- 残余差距：原片（notion-ai）笔头飞白颗粒感更细碎，实战可加

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/typography/marker-underline-title/MarkerUnderlineTitle.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
