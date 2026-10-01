# stroke-segment-build

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/stroke-segment-build`.

## Identity

- **slug**: `stroke-segment-build` (join key across cards, demos, media and deep links)
- **category**: `opening` — Opening & Brand / 开场与品牌
- **energy**: `低起中收` — arc or n/a, not sortable
- **suggested duration**: 4–5s → **150 frames @30fps = 5.0s**
- **cross-category tags**: `opening`, `typography`
- **upstream source**: references/shots/opening/stroke-segment-build.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `stroke-segment-build` | —f | B | `demos/opening/stroke-segment-build/StrokeSegmentBuild.tsx` |

## What it does

断笔成字——标题拆成十几段互不相连的笔画乱序逐段点亮，前 70% 不可读，末段落位瞬间语义"啪"地成立

**When to use it.** 开场吊悬念的产品名/大数字揭晓；一支片 ≤1 次；与 type-assembly/draw-svg-trace 分工：那些是"看着字被组装/描画"，本卡是"意义延迟揭晓"

**Why this shot earns its place.** 《异形》片头判例：标题不是被画出来的，是"显影"出来的——拆成离散 笔画段乱序点亮，观众前 70% 时间只看到神秘碎段，最后几段落位的瞬间 突然读出是什么字。"认出的那一刻"就是钩子，钩子的强度取决于 不可读期撑多久、钥匙段压多晚。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 拆段粒度 | 4 字母 ~16 段（SVG line 粗方端帽，44px 级线宽） | 段太少悬念期短；太碎读作噪点 |
| 乱序表 | 手工排：跨字母乱跳，"可读性钥匙段"（如 H 中横）压到最后 2–3 段 | 顺序点亮 = 没有悬念；钥匙段早出 = 提前泄底 |
| 不可读期 | 总时长的 60–70% 处仍应读不出字 | QA 抽中段帧自问"能猜出来吗"，能猜出就重排 |
| 落位脉冲 | scale 1.06 / 8f | demo 自评 6% 偏含蓄，实战可加大到 1.10 |
| 未亮段 | 条件不渲染（非 opacity 0） | 收尾真静止的前提 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 暗底上的辅助文字用亮灰——demo 首版顶部标题深灰压深底不可见（P1 自检抓到） _(rules P1)_
- 字数上限：4–6 字母词最佳；长词不可读期难控制，段数爆炸
- 本卡吃"识别瞬间"，标题必须是观众认识的词（产品名/SHIP/LIVE 类），
- 声音：逐段点亮稀疏轻拟音或无声，落位帧一声 impact + 可接 riser 铺底

## Card structure

`intention` | `phases` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/opening/stroke-segment-build/StrokeSegmentBuild.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
