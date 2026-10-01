# avatar-bracket-carousel

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/avatar-bracket-carousel`.

## Identity

- **slug**: `avatar-bracket-carousel` (join key across cards, demos, media and deep links)
- **category**: `ui-entrance` — UI Entrance & Showcase / 界面登场与陈列
- **energy**: `中` — rank 4/8
- **suggested duration**: 约 5.2s（156f@30fps） → **156 frames @30fps = 5.2s**
- **cross-category tags**: `ui-entrance`
- **upstream source**: references/shots/ui-entrance/avatar-bracket-carousel.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `avatar-bracket-carousel` | 156f | A | `demos/ui-entrance/avatar-bracket-carousel/AvatarBracketCarousel.tsx` |

## What it does

"Your ___ teammates" 填空排版，四角对焦框钉在句中不动，头像队列在框内垂直 spring 轮换三次，入框放大清晰、出框按距离缩小淡化模糊，角色标签同步更换，切换瞬间对焦框呼吸 7%

**When to use it.** "一个位置，多种角色"的能力枚举；团队/身份/预设/人格类产品的核心一句话镜头

**Why this shot earns its place.** "我们有设计师、客服、分析师、写手"列成四行就是一张清单。塞进一句话的一个槽位里， 它变成一个承诺加四次证明：句子不动，只有槽里的人在换。四角对焦框是这个手法的关键 ——它不参与轮换，但它把观众的眼睛钉死在那 92×92 的方框里，所以四次更换才读作 "同一个位置"而不是"四张头像飘过"。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 切换点 | 0.24 / 0.46 / 0.68，间隔 0.22（≈34f / 1.14s） | 间隔就是"读得完一个角色"的时长；<0.12 观众来不及看标签，>0.3 节拍器感散掉 |
| 切换行程 | 窗 0.14（≈22f），`E.spring(k, 0.25)` | 行程占间隔的 64% → 静置时间约 12f；阻尼 0.25 是明确一次回弹，调小会抖两下与相邻切换互相干扰 |
| 步距 | STEP=76px（框 92px、头像 58px） | 步距必须大于头像直径否则相邻两张会咬边；76/92 意味着出框的头像仍露出一角，队列的存在被暗示 |
| 缩放衰减 | `1 - d*0.38`，下限 0.5 | 一格距离缩到 0.62；斜率调大出框更决绝，但下限 0.5 会更早触顶，队列变成"两档尺寸" |
| 透明度衰减 | `1 - d*0.62` | 1.6 格距离外完全消失 → 画面里始终有约 3 张可见；斜率降到 0.3 会看到整列四张都在，取景框的"锁定"语义被削弱 |
| 模糊衰减 | `d*2.4`，上限 3px | 模糊是景深暗示，2.4 的斜率让邻位约 2.4px；>4px 邻位糊成色块，队列读不出是头像 |
| 标签衰减 | `1 - d*2.2` | 斜率必须显著大于头像的 0.62——标签是文字，两句同时半透明叠着最难读 |
| 框脉冲 | 窗 0.1，`sin(·π)` × 0.07 | 7% 是"咬合了一下"的量；>15% 框自己变成主角，抢过头像更换 |

## Known pitfalls

- 四张头像对三次切换：`pos` 最终停在 3，正好是末位。加第五张必须加第四次切换（且
- 切换点是硬编码数组，出现两处（`pos` 累加与 `breath` 累加）。改节拍必须同时改两处，
- 入场 stagger 与首次切换的间隔只有 0.09（入场末 0.15 → 切换 0.24）。加头像数会推后
- 头像是 emoji + 中性灰阶底色圆（灰度分层仅用于区分队列项），强调色只用在对焦框的
- 对焦框 SVG 的四条 path 与 92×92 viewBox 是写死的坐标（`M4,26 L4,4 L26,4` 等）。改
- 句子 "Your ___ teammates" 用 flex + gap:22px 居中，槽宽固定 92px 所以句干不会因

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/ui-entrance/avatar-bracket-carousel/AvatarBracketCarousel.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
