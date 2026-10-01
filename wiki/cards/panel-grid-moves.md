# panel-grid-moves

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/panel-grid-moves`.

## Identity

- **slug**: `panel-grid-moves` (join key across cards, demos, media and deep links)
- **category**: `rhythm` — Rhythm & Montage / 节奏与蒙太奇
- **energy**: `A 高 / B 中 / C 中高` — arc or n/a, not sortable
- **suggested duration**: A ~4.7s / B ~4.8s / C ~5s → **141 frames @30fps = 4.7s**
- **cross-category tags**: `ui-entrance`, `rhythm`
- **upstream source**: references/shots/rhythm/panel-grid-moves.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| C | `comic-panel-split` | 45f | B | `demos/rhythm/panel-grid-moves/ComicPanelSplit.tsx` |
| B | `flip-grid-reflow` | —f | B | `demos/rhythm/panel-grid-moves/FlipGridReflow.tsx` |
| A | `grid-flash-mosaic` | 14f | B | `demos/rhythm/panel-grid-moves/GridFlashMosaic.tsx` |

## What it does

分格节奏三式——grid-flash-mosaic 九宫格闪切填墙吞屏、flip-grid-reflow 网格集体重排、comic-panel-split 漫画斜格三机位并列

**When to use it.** 把"格子"当节奏器：逐格踩拍亮相（A）、节拍点集体换位（B）、同主体多机位定格并列（C）；三式都吃拍点

**Why this shot earns its place.** 与 wall-reveal-moves 的区别是本卡的定位锚：那是"整墙怎么入场" （一次性揭示），这是"格子怎么当节奏器"——分格、重排、并列都发生 在节拍上，格变即鼓点。A 是填：3×3 格按十六分音符乱序逐格啪啪硬入， 填满停一拍，中心格放大吞掉全屏——功能矩阵一秒全亮相；B 是移：6 张卡 在节拍点集体直线换位（横排→3×2 网格），半秒落定 + 加深脉冲收束—— 布局重排本身当一个鼓点；C 是并：画面咔咔切成 3 个斜线分格，同一产品 三种机位同时定格，停半拍后一格斜边扩张吃掉全屏——Scott Pilgrim 的 分屏语言。按需选：多功能亮相用 A，布局叙事用 B，单品多视角用 C。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| A 硬入 | 未到拍点直接不渲染（条件挂载），零淡化 | 逐格硬入无淡化——命门；淡入就不是"啪" |
| A 描边 | 每格 3px 深色描边（border-box） | 白底提亮不可见判例的反向应用：白卡靠描边分格 |
| A 吞屏 | 中心格塞 0.3125x 整页，放大 3.28（>3.2）让描边滑出画外 | 描边残在收尾满屏上就穿帮 |
| B 坐标 | 两套表预写（行 y=330 / 网格列 571.6/960/1348.4、行 416.2/663.8），纯 transform | 免真 FLIP 量测；帧确定无随机 |
| B 交错 | 偶数索引上排、奇数下排，轨迹互不对穿 | 乱排轨迹会恶性穿帮 |
| B 脉冲 | f58–64 brightness 0.78，filter 仅窗口内条件挂载 | 摘罩判例；窗口外挂 filter 毁真静止 |
| C 斜缝 | SVG 双线：16px 墨 #2f2f2f 底 + 10px 白核，12° 斜角 | 斜缝白线是漫画感命门；直缝读作分屏工具 |
| C 保活 | 定格 18f 各格 scale 缓推 +3%/+5.5%/+8% | 三格全静读作截图拼贴 |
| 收尾 | A 68f / B 81f / C 93f 真静止（≥40f） | R1；C 摘罩帧与扩张终值对齐防跳变 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- C 三格必须是**同一主体的不同机位**——三格塞不同内容读作 bento
- 三式都吃拍点、声音强依赖：A 逐格一声啪、B 起飞与脉冲各一声、
- 同片分格系 ≤1 段——格子语言辨识度太强，两段就撞
- A 与 wall-reveal-moves 别同片连用（都是"墙"，观众分不出

## Card structure

`intention` | `variants` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/rhythm/panel-grid-moves/ComicPanelSplit.tsx`
- `demos/rhythm/panel-grid-moves/FlipGridReflow.tsx`
- `demos/rhythm/panel-grid-moves/GridFlashMosaic.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
