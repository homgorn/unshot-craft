# overhead-camera-moves

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/overhead-camera-moves`.

## Identity

- **slug**: `overhead-camera-moves` (join key across cards, demos, media and deep links)
- **category**: `camera` — Camera & Space / 运镜与空间
- **energy**: `A 中 / B 中高` — arc or n/a, not sortable
- **suggested duration**: A ~4.8s / B ~4.7s → **144 frames @30fps = 4.8s**
- **cross-category tags**: `opening`, `camera`, `transition`
- **upstream source**: references/shots/camera/overhead-camera-moves.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| B | `overhead-tabletop-drop` | 55f | B | `demos/camera/overhead-camera-moves/OverheadTabletopDrop.tsx` |
| A | `tilt-reveal` | —f | B | `demos/camera/overhead-camera-moves/TiltReveal.tsx` |

## What it does

俯拍揭示两式——tilt-reveal 俯仰抬正揭示、overhead-tabletop-drop 桌面卡阵横滑骤降扎入

**When to use it.** 用"俯仰角"讲故事的开场/转场：单页 establishing 用 A，多页巡视择一扎入用 B

**Why this shot earns its place.** 库内俯拍视角一直空缺——crane-rise 是"平移+缩放"的升起（俯仰角 不动），space-camera C 式 drone-dive 是俯冲降落一镜到底；这两式让 **俯仰角本身讲故事**：A 是揭示——整页 rotateX 平躺、开场只见上缘 一条透视窄带，机位"抬头"回正，内容一排排涌入视野，像掀开桌上的 图纸；B 是选择——三张页面卡平躺成桌面卡阵，相机俯拍横向滑过依次 掠过（韦斯·安德森 tabletop），滑到目标页猛地俯冲扎入、抬正成满屏， "巡视一圈，就选这张"。选型：单页开场用 A，多页转场/开场用 B。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| A 俯角 | rotateX 关键帧 [-80, 2.6, -0.9, 0]（f25→68→72→76），transformOrigin 50% 0% | 首版 -55° 太弱：f0 仍见半页，无"窄带"悬念（实渲判例） |
| A 联动 | perspective 600→1200、perspectiveOrigin 5%→40% 随进度插值；scale 3.2→1 + translateY 200→0 | perspective 不联动则俯角初始见不到"只露顶栏" |
| A 收尾 | 全部动画 f76 结束，145f 留 69f 真静止 | 过冲幅度 ≤3°，再大读作弹簧不是机位 |
| B pan 段 | 0–55f 只改 translateX +700→-650（in-out cubic），角度不动 | pan 段动角度 = 两段职责糊掉（判例：pan 巡视、drop 表态） |
| B drop 段 | 55–85f 三通道同跑：rotateX 62→-1.8→0.6→0（out-cubic 过冲）、scale 1→2.04→2.0、translateX -650→0 | 三通道必须同跑；分先后读作两个动作 |
| B 卡阵 | 卡片 996×560（16:9 精确比），落版 scale 2.0 恰满屏正视；transform 顺序 translateX→rotateX→scale | 顺序错了 pan 会带出弧线轨迹 |
| B 地板 | 浅灰网格地板 | 无地板参照，横滑段读不出"相机在动" |
| B 收尾 | 全部动画 f93 结束，140f 留 47f 真静止 | — |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 大角度透视下卡片必须 backfaceVisibility hidden + translateZ(4px)
- A 与 crane-rise-reveal 同片二选一——都是开场揭示，两个"揭示开场"
- B pan 段角度锁死是命门（两段职责分离判例）：巡视归巡视、扎入归 **[命门]**
- 两式都是"相机大动作"，与 space-camera/crane-rise 同屏段落互斥，

## Card structure

`intention` | `variants` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/camera/overhead-camera-moves/OverheadTabletopDrop.tsx`
- `demos/camera/overhead-camera-moves/TiltReveal.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
