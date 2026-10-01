# glass-pill-dictation-typing

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/glass-pill-dictation-typing`.

## Identity

- **slug**: `glass-pill-dictation-typing` (join key across cards, demos, media and deep links)
- **category**: `interaction` — Interaction & Feature Demo / 交互与功能演示
- **energy**: `低` — rank 1/8
- **suggested duration**: 约1.7s（50f@30fps） → **50 frames @30fps = 1.7s**
- **cross-category tags**: `interaction`
- **upstream source**: references/shots/interaction/glass-pill-dictation-typing.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `glass-pill-dictation-typing` | 50f | A | `demos/interaction/glass-pill-dictation-typing/GlassPillDictationTyping.tsx` |

## What it does

纯黑底上一条定宽玻璃胶囊以约 1.25 倍略大弹出后缓落到位，内部自左暗到右亮铺一层强调色光；光标先行、随后打字出现占位句，光随打字进度渐渐熄灭，收尾成中性深色玻璃条

**When to use it.** 语音/AI 输入框的登场；"跟它说话"的交互提示镜头；高能段之间的一个安静过渡拍

**Why this shot earns its place.** 用"光随输入熄灭"讲一件很小的事：待命时它在发光（等你说话），你一开口 它就把光让给文字。1.7s 里只做三件事——弹出、打字、光退。任何额外动作 （弹跳、色变、图标动画）都会让这一拍不再是休止符。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 胶囊定宽 | 文本实测宽 + 168px（≈句宽 2 倍） | **定宽是关键**：随字伸缩会读作 chip 而不是输入条 |
| 出场缩放 | scale 1.25→1，t 0→0.22 outCubic | 1.25 倍是"从观众面前落回去"的量；1.5 倍就成了 pop 弹窗 |
| opacity 时序 | 前 0.025 跳满（早于缩放落位） | 同步淡入会让它像"渐渐出现"，失掉那一下轻微的实感 |
| 内嵌光 | 90deg、0 → .35@42% → .95@100% | 光必须在胶囊内部；改成外 glow 就成了"待通知"而不是"待输入" |
| 打字 | 18 字符，t 0.06→0.73 匀速 | 匀速 ≈ 3f/字符；加 ease 就读作"有人在犹豫" |
| 光熄灭 | 1 → 0，t 0.08→0.76 inOutQuad | 与打字同窗口是全片唯一的因果：光让位给文字 |
| 阴影收敛 | 内描边 0.16+0.1g / 内顶光 0.03+0.04g / 外泛光 26g px | 三层都挂在同一个 g 上，收尾自然落到"中性深色玻璃条" |
| 声波竖条 | 5 根、基准 [13,7,10,6,9]、±1.6px、频率 18 | 幅度到 4px 就成了"正在录音"的活跃态，与"待命"矛盾 |
| 光标 | t≈0.025 先行、0.75→0.8 撤 | 光标先于文字出现，是"输入框已就绪"的信号 |

## Known pitfalls

- 定宽靠一个 `visibility:hidden` 的测量节点算 `offsetWidth`，字体必须
- 声波竖条是持续呼吸（不受 t 分段控制），所以首尾帧的高度不同——
- 打字进度 `floor(seg(…)*len + 1e-6)`，那个 epsilon 是防止末字符在
- ACCENT_RGB（默认 `146,126,212` 紫）内嵌光与外泛光共用，
- 占位句 "Speak or type here"（18 字符）；换句要保持字符数接近，

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/interaction/glass-pill-dictation-typing/GlassPillDictationTyping.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
