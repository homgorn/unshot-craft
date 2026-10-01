# runway-ground-skim

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/runway-ground-skim`.

## Identity

- **slug**: `runway-ground-skim` (join key across cards, demos, media and deep links)
- **category**: `ui-entrance` — UI Entrance & Showcase / 界面登场与陈列
- **energy**: `高` — rank 6/8
- **suggested duration**: 悬空展示 ~0.4s + 贴落 ~1.2s + 立起转正 ~1.8s；全段 4s → **12 frames @30fps = 0.4s**
- **cross-category tags**: `ui-entrance`, `camera`
- **upstream source**: references/shots/ui-entrance/runway-ground-skim.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `runway-ground-skim` | —f | B | `demos/ui-entrance/runway-ground-skim/RunwayGroundSkim.tsx` |

## What it does

低角度掠地机位下 UI 卡片群从空中一阵急雨式快速贴落（起点微错、下落大量重叠并行、着地即停零回弹），落齐后整页立起、视角转正收尾

**When to use it.** 仪表盘/卡片流界面的登场（内容"从天而降完成自己"）；低角度炫技段后的收正；clickup 系悬空贴落语言的"齐落"重型版

**Why this shot earns its place.** 把界面拍成跑道：低角度透视里 UI 卡片悬空在不同高度，随后按界面 位置顺序（行优先左→右）一阵急雨式贴落——掉落感=干脆利落。 三个命门：**重叠并行**（起点只错 1.5f、下落 9f ⇒ 空中恒有 5–6 张 同时在落，"几乎一起但有涟漪感"；串行等待两轮被裁）、**零回弹** （着地即停，弹起被裁）、**快**（下落 9f，15f 版被裁"快一点"）。 落齐后页面从躺倒立起（rotateX 66°→0°）、镜头拉远居中，观众从 "看戏"回到"看界面"。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 起点差 | 1.5f/张（jitter ≤1.2f 不乱序） | 3f 版被裁"不需要一个落下了再启动第二个"；0 差读作开关（那是 orbit 的同帧语法） |
| 下落时长 | 9f 重力加速 | 15f 被裁慢；<6f 读不出下落方向 |
| 回弹 | 零（着地即停） | 压弹 4.5% 版被裁"去掉弹起"——掉落感=干脆利落 |
| 悬浮高度 | 560–880px 错落 | 同高读作阅兵；>1000px 落地时间拉长 |
| 空中提亮 | ~1.35x 追光 | 不提亮悬空不可感（返工判例） |
| 立起段 | rotateX 66→0 + 拉远，~56f | 只落不立起=没有收束；立起太快读作弹板 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 贴落节奏语义（三卡判例族）：本卡=急雨式重叠错峰；
- 与 deck-deal-flyin 分工：那张是卡片飞入列队（水平方向运动）；
- 立起段原片无对应参考（用户口述新增），终态版式对齐 clickup11

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/ui-entrance/runway-ground-skim/RunwayGroundSkim.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
