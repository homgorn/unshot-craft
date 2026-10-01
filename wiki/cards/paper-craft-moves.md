# paper-craft-moves

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/paper-craft-moves`.

## Identity

- **slug**: `paper-craft-moves` (join key across cards, demos, media and deep links)
- **category**: `ui-entrance` — UI Entrance & Showcase / 界面登场与陈列
- **energy**: `A 中` — arc or n/a, not sortable
- **suggested duration**: A 3–4s / B 4–5.5s → **120 frames @30fps = 4.0s**
- **cross-category tags**: `ui-entrance`
- **upstream source**: references/shots/ui-entrance/paper-craft-moves.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| A | `masking-tape-slap` | 38f | B | `demos/ui-entrance/paper-craft-moves/MaskingTapeSlap.tsx` |
| B | `popup-book-rise` | 34f | B | `demos/ui-entrance/paper-craft-moves/PopupBookRise.tsx` |

## What it does

纸艺两式——masking-tape-slap 纸胶带拍定（悬浮微晃被"啪啪"按死）与 popup-book-rise 立体书立起（卡片沿底边错峰立墙）

**When to use it.** 纸墨主视觉片的实体材料语言：单卡定妆入场用 A、整版 dashboard 开场建立用 B；与纸墨+强调色的主视觉（模板片为纸/墨/琥珀）天然同源

**Why this shot earns its place.** Wes Anderson 手账美术与立体书纸艺的 UI 翻译。A：卡片轻飘入位后 悬着微晃（未固定的纸），两条撕边半透明胶带"啪、啪"先后拍在对角， 第二条拍下**同帧**卡片停晃、投影变薄、整卡下沉——"按死"的定妆 一瞬是主角，两声"啪"是天然音效点。B：整页平躺如摊开书页（俯视）， 卡片像贴在页上的纸片沿各自底边错峰立起成墙，立到 95° 回弹 90° （纸的韧性），根部投影随立起收窄。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| A 按死三件套 | 同帧：晃动 2f 归零 + 投影 34px→8px + 全卡下沉 2px | 三件拆帧就没有"按死"感；第一条胶带只把包络衰到 0.45（半死） |
| A 胶带质感 | 半透明 + 锯齿撕边 + 落点故意歪 2–3° | 歪斜是设计的手工感；直挺挺读作 UI 元素 |
| B 立起方向 | rotateX 0→**-90°**（向观众立起） | demo 判例：方向写反卡片往画面里倒被底板裁切 |
| B 根部投影 | blur 矩形不随卡立起，高 104→14px、透明度 0.26→0.1 随角度插值 | 无投影纸片浮空；投影跟着立起来穿帮 |
| B 收尾 | 全部站定后场景 75°→68° 轻回正（in-out cubic） | 直接定住少一口呼吸 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- A 的晃动是"未固定"的叙事铺垫不是手持抖动（Q3 边界）： _(rules Q3)_
- B 与 tilt-reveal 分工：tilt 是**机位**抬头看静止页面，
- B 立墙后卡片呈 90° 侧立态，文字不可读——立墙是构图动作，
- 声音：A 两声"啪"（纸拍击拟音）；B 每排立起一声轻纸响，

## Card structure

`intention` | `variants` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/ui-entrance/paper-craft-moves/MaskingTapeSlap.tsx`
- `demos/ui-entrance/paper-craft-moves/PopupBookRise.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
