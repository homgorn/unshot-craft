# logo-shrink-wordmark-lockup

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/logo-shrink-wordmark-lockup`.

## Identity

- **slug**: `logo-shrink-wordmark-lockup` (join key across cards, demos, media and deep links)
- **category**: `outro` — Outro / 收尾
- **energy**: `中` — rank 4/8
- **suggested duration**: 约 4.4s（132f@30fps；收束 0.1–1.2s · 让位 1.5–2.1s · 字母 2–2.7s · 标语 3.2–3.7s） → **132 frames @30fps = 4.4s**
- **cross-category tags**: `outro`
- **upstream source**: references/shots/outro/logo-shrink-wordmark-lockup.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `logo-shrink-wordmark-lockup` | 132f | A | `demos/outro/logo-shrink-wordmark-lockup/LogoShrinkWordmarkLockup.tsx` |

## What it does

霓虹切口大环快速收束成中央实心小白 O 并带过冲刹车，图标左移让位，字母逐个滑入完成 lockup，强调色标语收尾

**When to use it.** 片尾品牌定妆：从满屏图形能量收束到"图标+字标+标语"的标准 lockup

**Why this shot earns its place.** 片尾的"盖章"动作：满屏的霓虹大环携能量坍缩成一枚小图标，愈合缺口、转为纯白（从演出态到标准态），然后按品牌 lockup 的规范一步步落位——图标让位、字标进场、标语押尾。观众看到的是品牌从动态里"站定"。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 收束幅度 | scale 5.4→1 | 起始倍率决定"从多满收到多小"；<3 冲击力不足，>7 初始态糊出画 |
| 刹车过冲 | +6%，sin 包络 0.26–0.37 | 砍掉读作硬冻结；>10% 变果冻 |
| 愈合窗口 | 0.10–0.28（与收束同步） | 愈合必须在落位前完成——落位后还在变色读作"没准备好" |
| 左移让位 | −68px，0.34–0.47 | 与字母首入（0.46）几乎无缝衔接，拉开间隔会有"空等"感 |
| 字母 stagger | 0.035/字，各 0.10 时长 | 5 字母合计约 0.28；字更多时按 `(0.7-0.46)/n` 反算间隔保证 0.7 前进完 |
| 标语入场 | 0.72–0.84 整行淡入 | 有意不逐字：标语是注脚不是主角；`ACCENT` 常量换项目色 |

## Known pitfalls

- `WORDMARK`（5 字母）与标语 `BUILD. SHIP. REPEAT.`（20 字符）都是占位；换品牌词时字母 stagger 节奏依赖字数，标语保持近似字符数否则宽字距排版会溢出或过疏
- 图标是 SVG 双弧切口环（抽象几何 mark），替换为真实品牌 logo 时保留"演出态→标准态"两层结构：一层带效果（辉光/彩色），一层纯净态，用同一条 heal 曲线交叉
- 左移量 −68px 与字标宽度耦合（row 定位在 `50%-40px`）——字数变化时两处一起调，让 lockup 整体在画面居中
- 收尾后无循环回位设计，作 outro 最后一镜使用；需要循环时在 t=1 后接 1s 静帧

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/outro/logo-shrink-wordmark-lockup/LogoShrinkWordmarkLockup.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
