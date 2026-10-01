# scan-bracket-sweep

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/scan-bracket-sweep`.

## Identity

- **slug**: `scan-bracket-sweep` (join key across cards, demos, media and deep links)
- **category**: `effects` — Light & Emphasis / 光效与强调
- **energy**: `中低` — rank 3/8
- **suggested duration**: 约5.0s（150f@30fps） → **150 frames @30fps = 5.0s**
- **cross-category tags**: `effects`
- **upstream source**: references/shots/effects/scan-bracket-sweep.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `scan-bracket-sweep` | 150f | A | `demos/effects/scan-bracket-sweep/ScanBracketSweep.tsx` |

## What it does

骨架文档弹到中央，四角落下 L 形取景括号，一条 2.5px 实线带渐变拖尾在文档上往复扫 5 趟——文档全程静止，只有光在读它

**When to use it.** "正在解析/校验这份内容"的过程镜头；文档类产品的能力演示；上传→分析链路的中段

**Why this shot earns its place.** 让观众看懂"这份东西正在被机器逐行读过"。取景括号先把目标框住（宣布检查 对象），扫描光带再往复走完全篇（宣布检查过程）。命门是**文档本身完全静止**： 一旦文档也在动，观众就分不清是"被检查"还是"在加载"。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 文档弹入 | scale 0.86→1，t 0→0.11 outCubic | 起始值低于 0.8 就成了"从远处飞来"，弹入要小幅度才像 UI |
| 取景括号 | 臂长 34px、描边 2px、外扩 −7px；stagger 0.022 / 各 0.055 | 四角同时出现读作静态边框；差 0.022 就够读出"依次落下" |
| 扫描趟数 | PASSES=5，窗口 t 0.17→0.95 linear | 3 趟不够读作"往复"，7 趟以上在 5s 内每趟太快 |
| 趟内缓动 | inOutSine + 末尾 12% 停顿 | 停顿是"看清了这一趟"的换气位；去掉就成了匀速来回摆 |
| 光带 | 2.5px 实线 + 82px 拖尾 rgba(20,20,22,.5)→0 | 线太粗（>4px）读作遮罩边缘而不是光 |
| 拖尾方向 | 下行 top:−82px / 上行 top:2.5px，渐变一并翻转 | 只翻其一 → 拖尾跑到运动前方，读作"光在往回吸" |
| 裁切层 | 与文档同 10px 圆角 overflow:hidden | 漏到文档外就是"扫画面"不是"扫文档" |

## Known pitfalls

- 光带必须裁在文档 bbox 内，且圆角与文档一致——漏出一点就丢掉"扫描
- 拖尾的 `top` 和 gradient 方向是两处独立写法，改扫描方向时必须同改，
- 括号的 34px 臂长与 −7px 外扩是按 300×178 的文档尺寸配的；换真实截图
- INK 是唯一的颜色变量（括号 + 光带 + 拖尾共用），换肤只改它

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/effects/scan-bracket-sweep/ScanBracketSweep.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
