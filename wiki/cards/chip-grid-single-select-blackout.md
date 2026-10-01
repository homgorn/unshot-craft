# chip-grid-single-select-blackout

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/chip-grid-single-select-blackout`.

## Identity

- **slug**: `chip-grid-single-select-blackout` (join key across cards, demos, media and deep links)
- **category**: `interaction` — Interaction & Feature Demo / 交互与功能演示
- **energy**: `中低` — rank 3/8
- **suggested duration**: 约5.0s（150f@30fps） → **150 frames @30fps = 5.0s**
- **cross-category tags**: `interaction`
- **upstream source**: references/shots/interaction/chip-grid-single-select-blackout.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `chip-grid-single-select-blackout` | 150f | A | `demos/interaction/chip-grid-single-select-blackout/ChipGridSingleSelectBlackout.tsx` |

## What it does

五个选项 chip 以 3+2 居中排布逐个淡入；选中帧先插一帧灰色按压块，紧接数帧内底色变纯黑、文字变白并做 1→1.04→1 极轻回弹，其余 chip 淡到 18% 但位置锁死；随后余项归零，黑 chip 上移收窄，下方浮现算式行

**When to use it.** 单选/套餐/档位选择的交互演示；"选了它之后会怎样"的因果镜头；价格/参数结算类链路

**Why this shot earns its place.** 一帧灰闪 + 三帧反黑，是把真实 UI 的 `:active → :selected` 两级状态 拆开演。观众看到的是"手指按下"再"系统确认"，而不是一次渐变。其余 chip 降到 18% 而**位置绝不移动**：一旦重排，观众会以为页面刷新了， "单选"的语义就丢了。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 入场 | 间隔 0.028、各 0.04、outQuad | 5 个 chip 在前 0.2 铺完，把时间留给选中段 |
| 选中时刻 | FS = 0.44（约全片中点） | 前半读题、后半看结果；FS 早于 0.3 观众还没读完选项 |
| 灰闪 | 0.006 亮 + 0.008 落，rgba(120,120,120,.5) | **就一帧**：给 2 帧以上就读作 hover 高亮，不是按下 |
| 反黑 | FS+0.008→FS+0.04 linear（≈5f） | linear 是故意的：加 ease 会让"变黑"这件事有过程感，太软 |
| 按压回弹 | 1 + sin(pr·π)·0.04，跨 0.067 | 0.04 是极轻；到 0.1 就成了弹跳按钮，抢戏 |
| 余项降级 | 降到 18%，位置 transform:none | **位置锁死是命门**：降到 18% 仍在原位，才读作"没被选中"而非"消失了" |
| 收束时刻 | FS+0.30（选中后≈1.5s）起，0.12 inOutCubic | 1.5s 是让观众看清选中态的最短驻留；缩到 0.5s 就赶 |
| 上移收窄 | translateY −46px、scale→0.82，横向补 cx 回中线 | 不补 cx 的话上移后会偏在左边，读作"被拖走" |

## Known pitfalls

- `cx` 用 `measured` 标志只测一次（首帧 `offsetWidth` 可能为 0 所以要
- 其余 chip 的 `transform` 必须显式写 `'none'`，靠 flex 自动重排会让
- 选中项要在同一个 flex 行里做 translate，不能改 `position`，
- 占位内容：5 条 "Option … plan" 选项名 + 算式行
- 与 `chip-lift-to-user-pill` 分工：那张选中后**横向生长成新对象**，

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/interaction/chip-grid-single-select-blackout/ChipGridSingleSelectBlackout.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
