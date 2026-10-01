# scanline-annotate-focus

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/scanline-annotate-focus`.

## Identity

- **slug**: `scanline-annotate-focus` (join key across cards, demos, media and deep links)
- **category**: `effects` — Light & Emphasis / 光效与强调
- **energy**: `中` — rank 4/8
- **suggested duration**: 约4.6s（138f@30fps） → **138 frames @30fps = 4.6s**
- **cross-category tags**: `effects`
- **upstream source**: references/shots/effects/scanline-annotate-focus.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `scanline-annotate-focus` | 138f | A | `demos/effects/scanline-annotate-focus/ScanlineAnnotateFocus.tsx` |

## What it does

一条亮扫描线自上而下掠过页面，扫过之处按先后顺序弹出相机取景框（1.75 倍收拢对准 + 轻微过冲），随后旁侧打出等宽小字标注，顶部状态行同步计数 00/06→06/06

**When to use it.** "AI 正在读你的页面/品牌"的分析镜头；设计系统/品牌规范的拆解介绍；产品能力的自我说明段

**Why this shot earns its place.** 把"分析"这件抽象事做成可见的因果链：扫描线走到哪，那块就被框住、被 命名。观众读的是"机器的视线"，所以扫描线必须匀速、标注必须严格滞后于 扫描线过境——**先扫到再弹框**，顺序一旦错乱就变成了预先编排的动画。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 扫描线 | t 0.06→0.66 匀速，y −30→300 | **零缓动**：加 ease 就读作"有人在拖进度条" |
| 触发换算 | ft = 0.06 + ((y+h+30)/330)·0.60 | 分母 330 = 扫描行程；改扫描窗口必须同改，否则框在扫描线到达前就弹 |
| 最小间隔 | prev + 0.05（≈1.5f） | 两个 y 接近的目标会同时弹；钳制后才逐个读得清 |
| 取景框收拢 | scale 1.75→1，outBack，0.13 | 1.75 倍是"从外面收进来"的下限；1.2 倍看不出对准动作 |
| 角标 | 臂长 9px、描边 1.5px | 臂长超过目标短边 1/3 就变成完整边框，丢掉"取景"语义 |
| 对焦闪 | fill opacity 峰值 0.07 | 超过 0.15 就盖住内容，读作"选中高亮"而非对焦确认 |
| 标注 | ft+0.05 起、0.11 走完、translateY 4→0 | 滞后 0.05 是"框稳了才命名"的因果；同时出现就乱 |
| 计数行 | 按 fired 实时统计，7px MONO，2px 字距 | 写死时间轴的计数一改 bbox 就对不上；必须实时数 |

## Known pitfalls

- **扫描线触发时刻与目标 bbox 强绑定**：换页面内容后 targets 的
- bbox 是手动微调留边的（不是自动量元素），改页面模板不会自动跟随
- 标注用 `white-space:nowrap` + 手写 `lx/ly`，词变长会顶出画外；
- 与 `scanline-assemble-flyin` 分工：那张是"扫到即装配"（页面从空到有），
- ACCENT（`#9fb6e8`）与 `A_RGB` 是同一个色的两种写法，换肤要同改两处

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/effects/scanline-annotate-focus/ScanlineAnnotateFocus.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
