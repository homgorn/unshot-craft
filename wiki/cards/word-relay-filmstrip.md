# word-relay-filmstrip

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/word-relay-filmstrip`.

## Identity

- **slug**: `word-relay-filmstrip` (join key across cards, demos, media and deep links)
- **category**: `typography` — Typography & Title Cards / 文字与字卡
- **energy**: `中低` — rank 3/8
- **suggested duration**: 每词期 ~1.5–2s × 3–4 词；全段 5–7s → **60 frames @30fps = 2.0s**
- **cross-category tags**: `typography`, `ui-entrance`
- **upstream source**: references/shots/typography/word-relay-filmstrip.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `word-relay-filmstrip` | 16f | B | `demos/typography/word-relay-filmstrip/WordRelayFilmstrip.tsx` |

## What it does

左列黑白相间等高页面卡步进滚动、右侧衬线大词原位接力（名词恒定+动词轮换）——切词瞬间才滚动一格，词块垂直中心与当前页面卡中点精确对齐

**When to use it.** "一个主体 × 多种能力"的枚举段（Computer researches/builds/codes…）；作品集/案例流展示；产品多场景巡礼

**Why this shot earns its place.** 左边是证据（页面截图胶片），右边是论点（大词）：动词换一次， 胶片就步进一格给出新证据——文字与画面互为注脚。命门是**步进制**： 左列平时完全静止，只在切词瞬间滚动一格（滚动=换证据的机械动作）， 持续滚动会让左列沦为背景装饰、切词失去"咔哒"感。第二命门是 **对齐**：大词块垂直中心必须与当前页面卡中点精确对齐（像素级）， 歪了整个版式的"编辑部严谨感"就塌了。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 页面卡 | 等高（530px@1080p）、黑白相间、约半屏宽 | 不等高/同色系读不出步进；卡太窄失去"证据"分量 |
| 词期 | ~45–60f/词 | <40f 读不完词+胶片看不清；词期不必均匀 |
| 滚动窗口 | ~12f ease-in-out，恰一卡高 | 持续滚动=命门违例；滚过头/不足读作机械故障 |
| 词接力 | 旧词 4–6f 灰化淡出 → 新词 6–8f 落位 | 同帧交叉必叠影；间隙 >10f 读作断片 |
| 垂直对齐 | 词块中心=当前卡中点（像素级） | 用户单点意见"文字高度和中间的页面中点要对齐"；差 >8px 可感 |
| 字体 | 衬线 Didot 类、动词字重比名词轻或同 | 无衬线会丢"编辑部"气质 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 与 text-column-converge 分工：那张是左右对峙合拢的揭晓戏；
- 与 pill-slot-cycle 分工：那张是胶囊槽位轮换 UI 元素；
- 实战素材：页面卡应使用真实截图（demo 为灰条示意，残余差距

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/typography/word-relay-filmstrip/WordRelayFilmstrip.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
