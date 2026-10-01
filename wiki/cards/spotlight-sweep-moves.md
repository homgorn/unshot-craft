# spotlight-sweep-moves

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/spotlight-sweep-moves`.

## Identity

- **slug**: `spotlight-sweep-moves` (join key across cards, demos, media and deep links)
- **category**: `effects` — Light & Emphasis / 光效与强调
- **energy**: `中低` — rank 3/8
- **suggested duration**: 单式 3.5–4.5s；A/B 可串联成巡礼段 → **135 frames @30fps = 4.5s**
- **cross-category tags**: `ui-entrance`, `transition`, `effects`
- **upstream source**: references/shots/effects/spotlight-sweep-moves.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `corner-spotlight-reveal` | —f | B | `demos/effects/spotlight-sweep-moves/CornerSpotlightReveal.tsx` |
| — | `glow-wake-sleep-panel` | —f | B | `demos/effects/spotlight-sweep-moves/GlowWakeSleepPanel.tsx` |
| — | `slide-spotlight-pan` | —f | B | `demos/effects/spotlight-sweep-moves/SlideSpotlightPan.tsx` |

## What it does

暗场聚光显影三式——A 醒睡扫过（光到即亮光走即暗）、B 贴边泛光横摇（紫光贴 UI 边缘渗入+聚光匀速右移）、C 角落匀速显影（径向聚光从角落匀速扩张点亮全屏）；黑场里"光即叙事"的 UI 展示

**When to use it.** 暗色调品牌片里逐个介绍 UI 面板/功能区；黑场开场把界面"点亮"登场；段落间光转场

**Why this shot earns its place.** 黑场里观众只能看见光给看的东西——聚光既是照明也是运镜和剪辑： 光到哪里哪里登场，光走即谢幕。三式共用"贴边紫色辉光光线"这个 身份元素（光线贴着 UI 边框/logo/顶边走，辉光要亮要糊，是光在 "抚摸"界面而不是描边动画）。命门是**匀速**：聚光的移动/扩张 严格 linear——缓动会让光有"意图"，匀速才读作探照灯的机械扫掠 （C 式判例：linear 但半径终值过大＝前 1/4 就饱和，观感照样不匀速）。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 聚光移动/扩张 | 全程 linear、零缓动 | **匀速是命门**——全程零缓动；加 ease 读作光有主观意图 |
| C 式半径终值 | 恰好在片尾覆盖全屏（1300@1080p/100f） | 终值过大＝提前饱和假匀速：亮度采样须全程平滑爬升（实测 8/46/101/…/238） |
| 贴边光线辉光 | 3–4 层（blur26+blur9+亮芯+粉偏移） | 层少读作细线描边；辉光要够亮够糊才是"光" |
| 光线锚定 | 严格贴 UI 边缘/顶边/logo | 光线脱离边缘漂浮＝失去"抚摸界面"语义（A 式返工判例：定位丢失紫光跑到底边） |
| 显影罩 | radial 渐变硬边略糊（feather ~15%） | 边太硬像圆形遮罩；太糊没有"照到/照不到"的界线 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 与 light-play-moves 分工：那张是元素/文字上的
- 三式重做判例：聚光扫过必须带贴边光线同行（v1 只有显影罩被裁
- 原片（clickup-30）光线转角有一瞬彩虹色散，demo 未做；实战可

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/effects/spotlight-sweep-moves/CornerSpotlightReveal.tsx`
- `demos/effects/spotlight-sweep-moves/GlowWakeSleepPanel.tsx`
- `demos/effects/spotlight-sweep-moves/SlideSpotlightPan.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
