# doc-park-left-pill-deal

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/doc-park-left-pill-deal`.

## Identity

- **slug**: `doc-park-left-pill-deal` (join key across cards, demos, media and deep links)
- **category**: `ui-entrance` — UI Entrance & Showcase / 界面登场与陈列
- **energy**: `低` — rank 1/8
- **suggested duration**: 约 5.8s（174f@30fps） → **174 frames @30fps = 5.8s**
- **cross-category tags**: `ui-entrance`
- **upstream source**: references/shots/ui-entrance/doc-park-left-pill-deal.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `doc-park-left-pill-deal` | 174f | A | `demos/ui-entrance/doc-park-left-pill-deal/DocParkLeftPillDeal.tsx` |

## What it does

文档不淡出而是向左滑出只露约 35% 宽并微缩到 0.92，右侧按旁白节奏慢速发牌三张白底描边药丸（outBack 弹入），每张落定后其下方字幕逐词加深、下一张到来前整句淡出，左侧文档全程极缓慢自动滚动保持"正在被读"

**When to use it.** 旁白驱动的"分析结论逐条给出"段落；文档理解、推荐理由、审阅意见类产品的核心说明镜头

**Why this shot earns its place.** 结论要一条一条给，观众才记得住。但如果把来源文档淡出，结论就变成了空中楼阁——观众 不知道这些话从哪来。这张卡的解法是**让来源留在画面里**：文档靠左驻留只露一截，还在 缓慢滚动（说明它正在被读），右侧的每条结论都是从这份文档里长出来的。发牌节奏刻意慢， 是为了给旁白留出说完一句的时间。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 发牌起点 | `T0 = [0.26, 0.48, 0.70]`，间隔 0.22（≈38f） | 间隔就是旁白句长；压到 0.12 以下字幕的"逐词加深"来不及走完，读作字幕闪一下就没了 |
| 驻留窗 | 0.06→0.24（inOutCubic） | 必须在首张药丸（0.26）之前收住；重叠会出现"文档还在滑、药丸已在发"的浑浊 |
| 驻留幅度 | `translateX -55%` + `scale 0.92`，露约 35% | 露太少（<25%）文档变成装饰失去"来源"语义；露太多右侧放不下 172px 宽的药丸 |
| 药丸透明度窗 | 0.035（≈6f，outQuad） | 比位移窗短是有意的——先实后稳；两窗等长会读作普通淡入 |
| 药丸位移窗 | 0.062（≈11f，outBack），y 14→0、scale 0.94→1 | outBack 的过冲是"发牌落桌"的手感；换 outCubic 会变成平淡的浮上来 |
| 字幕延迟 | `cs = f + 0.05`（≈9f） | 药丸落定（0.062）之后才起字幕；提前会出现字幕先于结论出现 |
| 字幕加深行程 | `(ce-cs)*0.7` | 占该句可见时长的 70%，末 30% 是全实态的静置阅读时间；调到 1.0 则字幕刚读完就被淡出 |
| 自动滚动 | `t*3 % 1` × 40px（3 个整数周期） | 3 周期在 5.8s 上约 0.7px/f，是"正在读"的暗示级速度；>3px/f 会抢注意力变成滚动展示 |

## Known pitfalls

- 自动滚动的周期数必须是整数，否则末帧文档停在半个周期上，接下一镜时位置对不上；
- 末张字幕的 `ce = 0.98` 意味着它在 0.93→0.98 淡出，末帧只剩三张药丸没有字幕。若要
- 药丸位置写死为 `left:214px, top:54+k*48`、宽 172px，是 480 宽画布下与驻留后文档
- 三条药丸文案（Quick Start / Bundle Plan / Starter Kit）与三句字幕都是占位，且字幕
- 药丸数写死为 3（`T0` 的长度）。加到 4 条时间就不够：末张起点会超过 0.9，字幕根本
- 字幕的 `ce` 依赖 `T0[k+1]`，改任一张的起点都会连带改变前一张字幕的可见时长——这

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/ui-entrance/doc-park-left-pill-deal/DocParkLeftPillDeal.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
