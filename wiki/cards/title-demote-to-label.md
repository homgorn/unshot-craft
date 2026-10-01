# title-demote-to-label

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/title-demote-to-label`.

## Identity

- **slug**: `title-demote-to-label` (join key across cards, demos, media and deep links)
- **category**: `typography` — Typography & Title Cards / 文字与字卡
- **energy**: `低中` — rank 2/8
- **suggested duration**: A ~3s（92f）/ B ~3.5s（104f）；demo 两式串播 196f → **92 frames @30fps = 3.1s**
- **cross-category tags**: `typography`, `transition`
- **upstream source**: references/shots/typography/title-demote-to-label.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `title-demote-to-label` | —f | B | `demos/typography/title-demote-to-label/TitleDemoteToLabel.tsx` |

## What it does

大标题降格为节标签两式——A 大标题居中显影站稳一拍后连续缩小 0.3x 平移到左上角落成小节标签、内容区在其下生长；B 同套路但登场时带文本选中态高亮块扫入再撤掉

**When to use it.** 章节开场（标题先当主角再让位给内容）；教程/功能演示片的小节交接；B 式给"文字/编辑"类产品加身份暗示

**Why this shot earns its place.** 章节标题的常规命运是"出现→消失→内容登场"，标题和内容互不认识。 本卡让标题**降格而不退场**：居中大字站稳一拍宣告主题，然后一次连续 补间缩到 0.3x 飞到左上角，落成这一节的栏目标签——它还在屏幕上， 只是从主角变成了门牌。观众获得免费的空间记忆：刚才那个大词就是 现在左上角那个小词，本节讲的就是它。内容骨架在降格进行中就开始 生长，交接零空档。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 降格补间 | 20f inOut(cubic)，scale→0.3 | <14f 读作标题被弹走；终点 >0.45 标签太大压内容 |
| 站稳拍 | 显影后 ≥18f 静置 | 省掉这拍，观众没读完标题它就跑了，降格白做 |
| 骨架错峰 | 块间 0.16t，宽 0.35→1 | 全部同时长出读作页面刷新而非"生长" |
| 生长起点 | 降格开始后 +12f | 等标题完全落位才生长会空 8f 冷场 |
| 选中高亮 | 扫入 10f / hold ~8f / 撤 8f，35% 透明蓝 | 高亮 hold <5f 读作闪烁 bug；不撤干净就降格，蓝块跟着飞很脏 |
| 白闪转场 | 4f opacity 1→0 | 仅两式串播用；>6f 读作曝光事故 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 与"标题钉进 3D 空间随相机透视变形"的场景锁定拍法（已退役）分工
- 降格路径上不许有其他元素动——标题飞行是全屏唯一焦点，骨架生长
- 多节连用（每节一次降格）时左上角标签要**换行不叠放**：新标签落位
- B 式的选中高亮是"文字可被选中"的产品暗示，非编辑器/文档类产品
- 标题文案 ≤3 个词——降格到 0.3x 后还要当可读标签，长句缩完就是一条灰线

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/typography/title-demote-to-label/TitleDemoteToLabel.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
