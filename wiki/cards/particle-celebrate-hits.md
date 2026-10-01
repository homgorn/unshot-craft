# particle-celebrate-hits

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/particle-celebrate-hits`.

## Identity

- **slug**: `particle-celebrate-hits` (join key across cards, demos, media and deep links)
- **category**: `data` — Data & Metrics / 数据与指标
- **energy**: `高` — rank 6/8
- **suggested duration**: A 3–4s / B 4–5s → **120 frames @30fps = 4.0s**
- **cross-category tags**: `data`, `effects`
- **upstream source**: references/shots/data/particle-celebrate-hits.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| A | `confetti-crossfire` | —f | B | `demos/data/particle-celebrate-hits/ConfettiCrossfire.tsx` |
| B | `counter-tick-sparks` | 78f | B | `demos/data/particle-celebrate-hits/CounterTickSparks.tsx` |

## What it does

庆祝粒子两式——confetti-crossfire 双侧礼炮（里程碑揭晓帧双炮交叉彩屑弹幕）与 counter-tick-sparks 数字溅火（计数器每破整千顶部迸火星）

**When to use it.** 里程碑数字/KPI 揭晓/成就段落；A 一次性大庆祝，B 持续小打点

**Why this shot earns its place.** 给"数字揭晓"配可听感的视觉打点：A 是揭晓瞬间的句号——画面左下右下 两门炮同帧开火，上百颗翻转彩屑抛物线交叉飞过全屏再落出画外，纯庆祝 语义；B 是过程中的逗号——计数器每跳过一个整千，数字顶部"叮"地溅一撮 小火星坠落熄灭，终值那跳翻倍爆一大撮+数字弹 1.1x。两式都是闭式弹道 （初速+重力+衰减逐帧公式），免物理引擎、帧确定。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| A 初速 | 90–150px/f | 词汇原案 18px/f 在 decay 下只飞 180px 不可感——弹道类幅度按总位移倒推 |
| A 配色 | 灰阶为主 + 1/3 强调色 | 全彩读作 B 端不合品牌；全灰读不出庆祝 |
| B 火星量 | 常规 6–10、终值 20 | 默认档最含蓄，嫌弱可 3 倍量做极端版 |
| 弹道 | 闭式公式（seed 伪随机初速角度） | 每帧独立可算，禁 Math.random |
| 收尾 | 粒子寿命耗尽条件卸载 | 结尾必须真静止，残留粒子=脏帧 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 同批组合款 ring-confetti-blowout（合环×礼炮）、lights-out-tick-burst
- A 只配"值得开炮"的时刻，一片一次；连开读作廉价
- 声音：A 双炮"砰砰"错开 1–2f 更有层次；B 每 tick 一声细"叮"

## Card structure

`intention` | `variants` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/data/particle-celebrate-hits/ConfettiCrossfire.tsx`
- `demos/data/particle-celebrate-hits/CounterTickSparks.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
