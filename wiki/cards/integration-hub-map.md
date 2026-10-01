# integration-hub-map

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/integration-hub-map`.

## Identity

- **slug**: `integration-hub-map` (join key across cards, demos, media and deep links)
- **category**: `ui-entrance` — UI Entrance & Showcase / 界面登场与陈列
- **energy**: `中高` — rank 5/8
- **suggested duration**: 前摇 ~0.5s + 快翻 ~1.2s + 图标齐现 → 光管齐连两拍 ~0.7s + 输送呼吸 ≥1.5s；全段 4.5–5s → **15 frames @30fps = 0.5s**
- **cross-category tags**: `ui-entrance`, `effects`
- **upstream source**: references/shots/ui-entrance/integration-hub-map.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `integration-hub-map` | —f | B | `demos/ui-entrance/integration-hub-map/IntegrationHubMap.tsx` |

## What it does

旧页面一次性快翻 180°（侧棱瞬间亮闪）落成新中枢页，五个集成 app 图标同帧弹现、随即五条彩虹光管同帧齐连，光管内输送脉冲持续流动——"翻开新一页，生态一齐接入"

**When to use it.** 集成/生态能力段（一个产品连一切）；版本翻新叙事（旧页翻成新页）；暗场霓虹调性的功能高潮

**Why this shot earns its place.** 翻面是"换时代"：旧文档页整个翻转 180° 得到新中枢页——必须是 完整翻面不是转个角度（判例），翻的动作**快翻+尾段减速**、一口气 完成无分段停顿（"匀速"判例：用户说的匀速=无停顿，不是字面 linear；90° 侧棱停顿版被裁）。侧棱时刻只"闪一下"（1–3f 脉冲， 长光晕平台被裁）。接入是**两拍制**：五图标同帧弹现（第一拍）→ 五管同帧起画齐连（第二拍）——齐，才读作"生态一次到位"；错峰 逐个连读作逐个谈判（两轮被裁）。连通后光管内亮脉冲沿图标→中枢 方向持续循环，"输送感"是终态的生命。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 翻面时长 | 35f（曾 70f 被裁"再快1倍"） | <24f 读不出双面；尾段减速比例 ~60% 时间走 20% 角度 |
| 翻面曲线 | ease-out 单调无停顿 | 侧棱停顿/分段被裁；严格 linear 起停生硬也被裁——快翻尾缓 |
| 侧棱闪 | 2f 脉冲、4f 归零 | 长光晕平台被裁"闪一下就行" |
| 接入节奏 | 两拍制：图标同帧 → +10f 光管同帧 | 错峰逐连两轮被裁"同时出现，然后同时连接"；两拍间隔 <6f 读作一拍 |
| 光管生长 | 9f 齐长 | 18f 版偏慢；各管长度不同但同帧到达（按各自 len 归一） |
| 输送脉冲 | ~4.6px/f 循环、相位错开 | 静态连线=没有"输送的感觉"（判例）；同相位读作闪烁 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 时序判例链完整记录在案：错峰连入 ×2 被裁 → 管齐图标错峰被裁 →
- 与 glow-flyline-moves 分工：那张是飞线本身的光效戏；本卡是
- 与 canvas-materialize-moves 分工：那张是画布元素实体化；本卡
- 双面卡实现：水平/垂直线 bbox=0 会使 SVG filter/渐变失效（三管

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/ui-entrance/integration-hub-map/IntegrationHubMap.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
