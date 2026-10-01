# picker-carousel-feature-cycle

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/picker-carousel-feature-cycle`.

## Identity

- **slug**: `picker-carousel-feature-cycle` (join key across cards, demos, media and deep links)
- **category**: `interaction` — Interaction & Feature Demo / 交互与功能演示
- **energy**: `中` — rank 4/8
- **suggested duration**: 约3.6s（108f@30fps） → **108 frames @30fps = 3.6s**
- **cross-category tags**: `interaction`
- **upstream source**: references/shots/interaction/picker-carousel-feature-cycle.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `picker-carousel-feature-cycle` | 108f | A | `demos/interaction/picker-carousel-feature-cycle/PickerCarouselFeatureCycle.tsx` |

## What it does

移动端风竖向选择器——焦点药丸不动、内容穿过它，每项带明显 outQuint 减速吸附后完全静止，按到中心距离分层控制透明度/字号/灰度，落定时药丸做 scaleY 极轻呼吸

**When to use it.** 逐个念出功能名/场景名的列表镜头；"选一个"的交互演示；移动端产品的 picker 类控件展示

**Why this shot earns its place.** 把"选择"这件事的物理感做出来：焦点框是固定的，是内容在滚动并被吸住。 每项停下后必须**真的静止几帧**——连续滚动读作 loading 动画，停顿才读作 "这一项被选中了"。距离衰减（透明度 + 字号 + 灰度三通道同时衰减）是让 观众视线始终锁在中间那一行的唯一手段。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 行高/可见行数 | rowH 34px × 5 行，焦点在第 3 行 | 可见行数必须是奇数，否则焦点行不在视觉正中 |
| 步数 | STEPS=5，窗口 t 0.05→0.95 匀速 | 5 拍是 3.6s 的舒适上限；7 拍每拍就压到 0.46s 读不清 |
| HOLD | 5/14 ≈ 0.357（每步尾段静止≈0.23s） | **命门**：HOLD 归零就变成匀速滚动，完全丢掉"吸附"语义 |
| 吸附缓动 | outQuint（作用在 local/(1−HOLD) 上） | outQuint 的急减速就是"被磁铁吸住"的手感，outCubic 太软 |
| opacity 衰减 | 1 → 0.55（d≤1）→ 0.18（d≤2） | 相邻行留 0.55 是让观众感知"上下还有内容"；降到 0.3 就孤立了 |
| fontSize 衰减 | 17→14px，按 min(1, d/2) | 字号差是第二重景深；只做透明度会显得扁 |
| 图标可见性 | max(0, 1 − d·1.6) | 只有焦点行带图标，是"当前项"的额外标记 |
| 药丸呼吸 | scaleY 1→1.06→1，落定后 0.6·HOLD 内走完 | 0.06 已到上限；再大就读作药丸自己在动，抢了内容的戏 |

## Known pitfalls

- 药丸必须是 **`translateY` 零位移的固定层**，`scaleY` 呼吸也不能带
- 距离衰减写在 `fontSize` 上会触发逐帧重排（行高固定所以布局不跳），
- 渐变遮罩的颜色要与背景 PAPER 完全一致，差一档就露出边界带
- 左外侧 26×22 的方形 AI 徽标用 `margin:-11px 0 0 -186px` 相对画面中心
- ITEMS 是 7 条占位功能名（"Data Cleanup" 等），落地换真实功能名时

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/interaction/picker-carousel-feature-cycle/PickerCarouselFeatureCycle.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
