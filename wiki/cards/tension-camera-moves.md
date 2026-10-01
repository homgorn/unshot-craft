# tension-camera-moves

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/tension-camera-moves`.

## Identity

- **slug**: `tension-camera-moves` (join key across cards, demos, media and deep links)
- **category**: `camera` — Camera & Space / 运镜与空间
- **energy**: `A 高 / B 中 / C 低压升 / D 低收` — arc or n/a, not sortable
- **suggested duration**: 单式 4–5s；全片合计 ≤2 式（各 ≤1 次） → **150 frames @30fps = 5.0s**
- **cross-category tags**: `camera`
- **upstream source**: references/shots/camera/tension-camera-moves.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| A | `bullet-time-freeze-orbit` | —f | B | `demos/camera/tension-camera-moves/BulletTimeFreezeOrbit.tsx` |
| B | `dutch-roll-to-level` | —f | B | `demos/camera/tension-camera-moves/DutchRollToLevel.tsx` |
| D | `pull-back-isolation` | 16f | B | `demos/camera/tension-camera-moves/PullBackIsolation.tsx` |
| C | `slow-push-in` | —f | B | `demos/camera/tension-camera-moves/SlowPushIn.tsx` |

## What it does

情绪运镜四式——bullet-time 冻结环绕、dutch-roll 斜角滚正、slow-push 慢推压迫、pull-back 拉远孤立，相机替观众"感受"而非"看"

**When to use it.** 情绪节点（震撼/纠偏/积压/收束）的运镜语言；与 space-camera-moves 的"炫技大动作"互补——这四式动作小、情绪重

**Why this shot earns its place.** space-camera-moves 三式是"把页面当 3D 实体拍"的高光炫技；这四式相反—— 动作本身克制，全部劲道在情绪语义上：A 说"这一刻值得停下时间看" （运动中的元素被冻住、相机绕行审视）；B 说"问题解决了，世界被扶正" （斜角悬着的难受感在节拍上滚回水平）；C 说"有什么要发生了"（慢到 不自觉的推近积压张力，顶点硬切释放）；D 说"最后只剩这一件事" （后拉中周围逐层熄灭，孤悬一点收束全片）。四式各占一个情绪格， 是分镜阶段"这一段观众该感到什么"的直接词汇。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| A 双时钟 | 内容动画用 `effFrame = f<F1 ? f : f<F2 ? F1 : F1+(f-F2)` 驱动，相机用真实 f 驱动 | 命门：冻结期内容必须肉眼可见地完全静止，相机却在动——两个时钟各管各的 |
| A 环绕 | perspective 1600 下 rotateY 0→55°→0（两段 inOut cubic，顶点悬停 ~10f）+ scale 1→1.12→1 | 55° 是"绕到侧面看"的下限；>70° 面板变纸片穿帮 |
| B 斜置 | rotate -10° + ±0.8° 长周期正弦漂移 + 2px 纵漂；scale 1.15 防露边 | 漂移是"悬着难受"的活感，纯静止斜角读作构图错误 |
| B 滚正 | 14f ease-out 冲过 0 到 +1.2° → 10f 收回 0（单次过冲不振荡）；scale 同步 1.15→1.08 | 过冲即"扶正的手劲"；振荡两次以上读作弹簧玩具 |
| C 推近 | `scale [0,120f]→[1.00,1.14] Easing.in(quad)` + 暗角 opacity 0→0.5 同曲线 | 加速曲线是本体——匀速推读作普通 zoom；幅度 >1.2 变成普通推镜头 |
| C 硬切 | 顶点帧零过渡直切下一景；暗景 A→亮景 B 反差要大 | 切的一拍才是释放；加任何过渡等于把弓拉满又慢慢松掉 |
| D 后拉 | scale 2.2→0.62 / 110f Easing.out(cubic)，origin 锁主卡中心 | 前 20f 主卡仍占满画面，开场即特写不需要另加 hold |
| D 熄灭 | 兄弟卡按 hypot 距离排序，帧 30 起每 8f 一张，16f 内 opacity→0 + brightness→0.3；背景 60–110f 沉入 #141414 | 由近到远熄灭 = "世界向外塌暗"；乱序熄灭读作故障 |
| D 光晕 | 主卡双层白 box-shadow 60–100f 淡入 | 光晕是"只剩它"的视觉证词，与沉黑同步才成立 |
| 收尾 | 四式动作完毕真静止 ≥30f | R1；D 式是全片句号，静止给足 40f+ |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- C 式"前 2 秒不可察"是设计意图不是缺陷——裁决/验收看完整播放，抽帧
- A 式与 speed-ramp-freeze/impact-feedback 同为时间操纵，同一镜头别叠用
- B 式斜角只压"痛点"段——全片常态斜角是 MV 语言，产品片里读作镜头没扶稳
- C 式硬切后的亮景必须信息完整可读（它承接全部积压的注意力）；
- D 式放结尾时后接 outro-group-photo-launch 会打架（一收一放），二选一

## Card structure

`intention` | `variants` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/camera/tension-camera-moves/BulletTimeFreezeOrbit.tsx`
- `demos/camera/tension-camera-moves/DutchRollToLevel.tsx`
- `demos/camera/tension-camera-moves/PullBackIsolation.tsx`
- `demos/camera/tension-camera-moves/SlowPushIn.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
