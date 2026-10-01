# beat-step-list-theme-cycle

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/beat-step-list-theme-cycle`.

## Identity

- **slug**: `beat-step-list-theme-cycle` (join key across cards, demos, media and deep links)
- **category**: `rhythm` — Rhythm & Montage / 节奏与蒙太奇
- **energy**: `高` — rank 6/8
- **suggested duration**: 铺垫 30f + 每拍 18f × 拍数 + 收尾 hold；3 拍约 3.5s（demo 110f） → **30 frames @30fps = 1.0s**
- **cross-category tags**: `typography`, `rhythm`
- **upstream source**: references/shots/rhythm/beat-step-list-theme-cycle.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `beat-step-list-theme-cycle` | —f | B | `demos/rhythm/beat-step-list-theme-cycle/BeatStepListThemeCycle.tsx` |

## What it does

三通道节拍器——深色场形容词列表逐拍上移一行，视口中央固定胶囊"接住"下一个词并换色，整场底色同拍跟换；行、色、场三通道锁死同一拍点

**When to use it.** "同一产品多种气质/多主题展示"段落（modern/playful/expressive 式形容词连打）；全片节奏最密的一段；音乐段对拍

**Why this shot earns its place.** 换一次主题色是功能演示；0.6 秒换一次、连换三次、每次"选中行+胶囊色 +全场底色"三件事同帧齐跳——就成了节拍器。用最便宜的变量切换做出 全片最高的节奏密度。命门有二：一是**三通道必须锁同一拍点**，任何 一通道慢半拍，"齐跳"退化成三个各自为政的动画；二是**跳与滑的分界** ——跳变只占拍头 6f，其余 12f 完全静置，拍点要"跳"不要"滑"， 匀速滚动的列表就只是列表。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 拍长 | 18f（BEAT_LEN，改它即改 BPM 对音轨） | <12f 观众来不及读词只见闪色；>26f 拍感散成逐个展示 |
| 跳变窗 | 拍头 6f，ease-out 指数 3.2 | 窗 >10f 或缓曲线，"跳"变"滑"，节拍器塌成滚动列表 |
| 拍数 | 3–4 拍 | 5+ 拍观众适应了节奏开始走神；1–2 拍立不起"节拍器"人设 |
| squash | 1.12→0.97→1 | 去掉它胶囊像贴图换色；>1.2 弹跳抢了换色的戏 |
| 底色跨度 | 相邻主题底色须同明度不同色相（都深色） | 明度跳变（深→浅）会读作闪屏而非换肤 |
| 铺垫/收尾 | 前 30f 静置；末拍后 hold ≥30f | 没铺垫第一拍读作 bug；末拍即切没有"停在最终色"的确认 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 与 theme-switch-moves 分工：那卡是单次换肤的仪式（扫场/涟漪，换一次
- 与 cel-flash-stomp 同为高密度拍点段，同片二选一或隔远——都是
- **声音强依赖**：拍点对齐鼓点（换 BEAT_LEN 对 BPM），无声版三通道
- 词表长度 ≥ 拍数+2——列表底部要留未选中的词垫着，最后一拍就停在
- 反白判定跟 beat 整数走、颜色跟 tInBeat 小数走（demo 即如此）——

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/rhythm/beat-step-list-theme-cycle/BeatStepListThemeCycle.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
