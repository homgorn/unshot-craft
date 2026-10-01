# radial-ripple-phone-chips

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/radial-ripple-phone-chips`.

## Identity

- **slug**: `radial-ripple-phone-chips` (join key across cards, demos, media and deep links)
- **category**: `effects` — Light & Emphasis / 光效与强调
- **energy**: `低` — rank 1/8
- **suggested duration**: 约5.6s（168f@30fps） → **168 frames @30fps = 5.6s**
- **cross-category tags**: `effects`
- **upstream source**: references/shots/effects/radial-ripple-phone-chips.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `radial-ripple-phone-chips` | 168f | A | `demos/effects/radial-ripple-phone-chips/RadialRipplePhoneChips.tsx` |

## What it does

浅灰底四层同心圆错相呼吸如水波，中央手机 mockup 屏内 feed 自动缓滚，两侧白色 chip 先后 spring pop 入场并悬浮

**When to use it.** 移动端产品的"这就是它"定格镜头；功能点分列两侧的介绍段；片头/片尾的产品全景

**Why this shot earns its place.** 用最少的动作把手机放在画面正中并让它"活着"：同心圆负责氛围呼吸， 屏内自动滚屏负责证明"里面有内容在跑"，两侧 chip 负责点出功能名。 三层动作各自极慢，叠起来才不会显得静止——这是产品定格镜头的标准配法。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 同心圆层数/尺寸 | 4 层 560/440/320/210px | 3 层撐不满画面，5 层以上最外层被裁掉只剩色带 |
| 呼吸幅度 | scale 1±0.06，1.5 周期/全片 | 0.06 已是上限；到 0.1 就读作"脉冲动画"而非水波 |
| 相位差 | 相邻层 1.7 rad | 相位全同 = 整块放大缩小；差 1.7 才有波从中心荡开的错觉 |
| 手机投影 | 0 24px 50px rgba(58,64,74,.35) | 投影是手机"浮在波上"的唯一依据，去掉就贴平了 |
| 自动滚屏 | translateY 0→−150px，t 0.08→0.98 匀速 | 加 ease 立刻读作"有人在滑"；匀速才是自动播放 |
| chip pop | outBack、0.12 时长、scale 0.8→1 | outBack 的过冲量是"弹出"的全部质感，换 outCubic 就平了 |
| chip 时序 | 左 0.22 / 右 0.40（≈0.6s 差） | 同时出现读作两个标签；错开才有"一个一个说"的节奏 |
| chip 悬浮 | ±3px、2 周期，pop 后 0.18 内渐入 | 幅度超过 5px 就和同心圆的呼吸抢戏 |

## Known pitfalls

- chip 用 `calc(50% + 86px)` 贴着手机边缘定位；改手机宽度必须同步改
- 屏内 feed 是 8 张骨架卡的占位内容，落地换真实截图时总高必须
- 同心圆是实色叠放（不是描边圆环），层序必须由大到小 append，
- ACCENT_RGB（默认 `122,134,153` 中性灰蓝）只作用于屏内缩略图渐变，

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/effects/radial-ripple-phone-chips/RadialRipplePhoneChips.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
