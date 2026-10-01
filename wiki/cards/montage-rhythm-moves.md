# montage-rhythm-moves

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/montage-rhythm-moves`.

## Identity

- **slug**: `montage-rhythm-moves` (join key across cards, demos, media and deep links)
- **category**: `rhythm` — Rhythm & Montage / 节奏与蒙太奇
- **energy**: `高` — rank 6/8
- **suggested duration**: A 4.3s / B 4.3s / C 5s → **129 frames @30fps = 4.3s**
- **cross-category tags**: `rhythm`
- **upstream source**: references/shots/rhythm/montage-rhythm-moves.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| C | `domino-cascade` | 12f | B | `demos/rhythm/montage-rhythm-moves/DominoCascade.tsx` |
| A | `drop-blackout-slam` | —f | B | `demos/rhythm/montage-rhythm-moves/DropBlackoutSlam.tsx` |
| B | `wright-triple-cut` | 25f | B | `demos/rhythm/montage-rhythm-moves/WrightTripleCut.tsx` |

## What it does

蒙太奇节奏三式——drop-blackout-slam 黑场蓄爆、wright-triple-cut 三连咔哒特写、domino-cascade 多米诺连锁入场

**When to use it.** 段落级节奏设计：蓄力爆发（A）、流程速写（B）、开场连锁（C）；与 beat-cut-moves（切点排布）互补——这三式管"段落的呼吸形状"

**Why this shot earns its place.** beat-cut-moves 管切点间隔怎么排，这三式管更大一层的节奏叙事： A 是"静默即蓄力"——drop 前一拍切全黑死寂憋一整拍，爆开才够响 （EDM 演出 blackout 惯例），给全片最高潮的前一秒用；B 是"流程三连" ——三个超近特写咔哒咔哒咔哒连打（按下/拨动/翻牌），第三声甩回全景 亮结果，Edgar Wright 式把"操作很简单"剪成肌肉记忆；C 是"动量传递" ——标题砸落震起卡片、卡片落地撞进侧边栏，每个元素的入场由上一个的 撞击触发，Rube Goldberg 式把一页内容的入场讲成连锁反应。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| A 铺垫 | 前段画面轻微 scale 呼吸 1.0↔1.02 + 节拍点每 12f 闪 | 必须先让"片子在正常播"可感，黑掉才有落差 |
| A 黑场 | 一帧直切纯黑（#0c0c0c），12f **完全无物** | 命门：黑场里放任何东西（logo/微光）都在泄压——死寂才是蓄力 |
| A 爆入 | 主视觉 scale 1.35→1.0（5f out cubic）+ 10px 震屏 exp(-t/2.5) 12f 收干 + 亮环 80→900px 16f 消散 | 三件事同帧起爆；震屏 t≥14 强制归零保真静止 |
| B 特写结构 | 每个 10f：静 4f + 动作 3f + 静 3f；动作用 p<0.5 二值跳变保干脆 | 动作 3f 是"咔哒"的物理时长；拉长成 6f 就是普通交互动画 |
| B 构图统一 | 三特写同倍率感、主体都在屏心 | 构图乱跳读作三段素材硬拼，连切节奏散 |
| B 甩回 | 6f whip（Easing.poly(5) out）+ 2 层错帧副本（opacity 0.35/0.18）模拟糊 | 甩回落点的"结果"要提亮泛光——三连咔哒的答案必须亮着 |
| C 动量链 | 每级 startFrame = 上一级 impact 帧；初速方向继承上一撞击方向 | 命门：竖砸→竖弹→（末卡歪 3° 给出横向）→横滑，方向没有出处则"连锁"读作巧合 |
| C 撞击震动 | 4f 衰减序列 [A,-0.6A,0.3A,-0.12A,0]，两次幅度 10/6px 递减 | 幅度递减表现能量损耗；等幅两震读作重复播放 |
| C 卡片弹跳 | 依次隔 5f 各弹 60px 抛物线 12f | 40px/3f 间隔在正常速度下读不清传递感（本批实渲加码） |
| 收尾 | A 爆入后 ≥50f / B 甩回后 ≥45f / C 全链落定后 ≥50f 真静止 | 三式都是重拳，hold 按平常两倍给（同 beat-cut B 判例） |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- A 式全片 ≤1 次且必须配声design：黑场同帧音频也切静、爆开同帧音爆
- A 的震屏与 impact-feedback、C 的震动与 domino 内部震动都属震屏族，
- B 式三个特写 10f/个节奏很快是设计意图（已验证可读），但特写内容换成
- B 式甩回与 shot-transitions E 式甩镜同技术根——B 的 whip 是镜内收尾
- C 式链最多三级（标题→卡片→侧栏）；四级以上观众跟不住因果链，

## Card structure

`intention` | `variants` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/rhythm/montage-rhythm-moves/DominoCascade.tsx`
- `demos/rhythm/montage-rhythm-moves/DropBlackoutSlam.tsx`
- `demos/rhythm/montage-rhythm-moves/WrightTripleCut.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
