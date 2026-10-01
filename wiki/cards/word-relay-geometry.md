# word-relay-geometry

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/word-relay-geometry`.

## Identity

- **slug**: `word-relay-geometry` (join key across cards, demos, media and deep links)
- **category**: `typography` — Typography & Title Cards / 文字与字卡
- **energy**: `中高` — rank 5/8
- **suggested duration**: 约 6.0s（180f@30fps：三段各 0.36 时长窗，段间重叠 0.04） → **180 frames @30fps = 6.0s**
- **cross-category tags**: `typography`
- **upstream source**: references/shots/typography/word-relay-geometry.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `word-relay-geometry` | 180f | A | `demos/typography/word-relay-geometry/WordRelayGeometry.tsx` |

## What it does

三个利益词各带一套专属几何接力——虚线大圆自转收缩 → 三实线圆 trim 依次生长（相位差 0.06）→ 金属 sheen 扫过后一拍收成纯白；旧词缩到 0.86 淡出，新词描边→填充揭示

**When to use it.** 三点式利益陈述（更快/更好/更强）；品牌价值观段落；需要"一词一世界"的中段推进

**Why this shot earns its place.** 三点式利益陈述最容易做成三张字卡硬切。接力的做法是给每个词配一套 **只属于它的几何**：虚线圆是"在转"（快）、三圆相扣是"互相咬合"（好）、 金属扫光是"材质硬"（强）——几何本身就在替形容词做论证。第三个词 留了升格待遇（sheen 扫光 + 收白），因为它是结论。背景 20 颗微尘上浮 把三拍缝成一个连续空间，不然还是三张卡。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 三段时段 | 各 0.36（≈65f），重叠 0.04（≈7f） | 每词约 2s 是"读词 + 看几何"的下限；重叠 <0.02 读作硬切，>0.08 两词同屏打架 |
| 入/出场窗 | 入 0.07 outCubic / 出 0.05 inQuad | 出场比入场短是对的（退场要决绝）；出场用 out 曲线会读作"舍不得走" |
| outline→fill | 窗 0.12（≈22f）inOutCubic，outline 留 0.25 | 留一点描边做重影是质感来源，降到 0 字变扁；窗 >0.25 擦入慢得像加载条 |
| 虚线圆 | r=100、`dash 5 7`、scale 0.4→1、自转 `t·30`° | 自转绑全片 t 所以永不停——这是"快"的证据；scale 起点 >0.7 就没有"长出来" |
| trim 生长 | `pathLength=1` + dashoffset 1→0，相位差 0.06 | 相位差是"依次相扣"的关键，同时生长读作三个独立圆；窗 0.12 与 fill 同步收敛 |
| sheen 扫光 | `100deg` 渐变、`background-size:280%`、位置 100%→0% | 280% 保证白带只占字宽一小段（=金属高光）；100% 时整字一起变亮，不是扫光 |
| 收白 | `seg(t0+0.27, t0+0.34)` ≈13f + 18px 辉光 | 这一下是全片唯一的"结论"待遇；删了三个词就是平级，第三点没有落点 |
| 字号配色 | 56px/800、描边 `#6a7186`、几何 `#565e78`、底 `#07080c`，微尘 20 颗 | 几何色比描边略暗一档是层级，几何比字亮就抢主角；微尘是把三拍缝成一个空间的胶水，>40 颗读作雪 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- **三个词必须是同一句法的三点（demo 都是比较级单词，6–8 字母）**：
- `-webkit-text-stroke` 是前缀属性：Chromium/WebKit 才有，Firefox 下描边层
- SVG trim 用的 `pathLength=1` 归一化在部分老版本浏览器上对 `<circle>`
- 出场 trim 是"入场 trim 减出场 seg"直接相减：两段窗若靠得太近
- sheen 层与 fill 层是叠着的两个 DOM：切换靠透明度交叉，若把 `white` 窗
- 第三个词的升格待遇只能给一次：全片三个词都上 sheen 就没有结论感

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/typography/word-relay-geometry/WordRelayGeometry.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
