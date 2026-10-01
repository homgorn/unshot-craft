# type-entrance-moves

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/type-entrance-moves`.

## Identity

- **slug**: `type-entrance-moves` (join key across cards, demos, media and deep links)
- **category**: `typography` — Typography & Title Cards / 文字与字卡
- **energy**: `中高` — rank 5/8
- **suggested duration**: 单式 4–5s（含 hold 与静止收尾；动作段 A ~66f / B ~106f） → **66 frames @30fps = 2.2s**
- **cross-category tags**: `typography`
- **upstream source**: references/shots/typography/type-entrance-moves.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| B | `letter-drop-physics` | —f | B | `demos/typography/type-entrance-moves/LetterDropPhysics.tsx` |
| A | `scramble-decode` | —f | B | `demos/typography/type-entrance-moves/ScrambleDecode.tsx` |

## What it does

标题文字入场两式——scramble-decode 乱码解码（噪声里长出答案）与 letter-drop-physics 字符坠落（重力砸落弹跳归位），按调性二选一

**When to use it.** 大标题/章节字卡的入场；与 split-flap-title（机械翻牌）、document-typewriter-reveal（打字机）同品类互斥选用

**Why this shot earns its place.** 标题入场库内已有打字机（沉稳文档感）和翻牌屏（机械仪式感），这两式补 另外两种性格：A 是终端黑客感——字符先是一片高速噪声，从左到右逐个 "解码"锁定，观众看着答案从乱码里长出来，适合技术产品的自信亮相； B 是物理喜剧感——字符从天而降、砸地弹跳、歪歪扭扭站定，最后一拍 集体立正归位，适合轻松调性的开场破冰。四种标题入场同片 ≤2 种（P4）。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| A 乱码期 | 0–20f 全员每 2f 跳一个随机字符（字符集 A–F/0–9/#$%&），字色 G.mid | 必须用等宽字体 + 固定 1ch 槽宽，比例字体每跳一下整行抖动 |
| A 解码节拍 | 第 i 字符帧 20+i×6 锁定为真字符转深色；锁定后前 2f 反色闪（深底白字） | 6f/字是"逐个可辨"的下限；上限 10f，再慢读作卡住 |
| A 伪随机 | `CHARSET[floor(h(i*101+floor(f/2)*7+13)*len)]`，h = sin hash | 严禁 Math.random——跳动必须随帧确定，否则渲染不可复现 |
| B 坠落 | 第 i 字符帧 10+i×5 起跳；y = −DROP + DROP·(t/24)²（重力）→ 4u(1−u) 抛物线弹跳 30% → 二跳 9% | 弹跳衰减比 30%/9% 是"有弹性但不闹"的甜点；三跳以上读作果冻 |
| B 歪斜 | 落地瞬间 rotate 到 seed hash ±6° 并保持 | 歪角是"物理感"的一半；全体笔直落地读作普通位移入场 |
| B 归位一拍 | 全员落定后（如帧 110）6f ease-out 集体 rotate→0 + scale 1.06→1 | 集体归位是句号——错峰归位会把"立正"的仪式感拆散 |
| 收尾 | 两式动作完毕真静止 ≥20f | R1：静止期所有属性锁死（含 B 的歪角归零后） |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- A 式是声音强依赖候选位：锁定的"嗒"声逐字钉帧（sound-design §4.5）
- A 式字符集别混入与真字符太像的字形（如 O/0 连跳）——观众会误判已锁定
- B 式字符间不做真实碰撞（demo 为各字符独立轨迹）——字距排开即可；
- 标题入场品类已四式（本卡两式 + split-flap-title + document-typewriter-reveal），

## Card structure

`intention` | `variants` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/typography/type-entrance-moves/LetterDropPhysics.tsx`
- `demos/typography/type-entrance-moves/ScrambleDecode.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
