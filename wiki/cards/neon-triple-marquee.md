# neon-triple-marquee

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/neon-triple-marquee`.

## Identity

- **slug**: `neon-triple-marquee` (join key across cards, demos, media and deep links)
- **category**: `outro` — Outro / 收尾
- **energy**: `中高` — rank 5/8
- **suggested duration**: 4–5s（demo 150f：10f 淡入 + 循环体 + 20f 淡出） → **150 frames @30fps = 5.0s**
- **cross-category tags**: `typography`, `outro`
- **upstream source**: references/shots/outro/neon-triple-marquee.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `neon-triple-marquee` | —f | B | `demos/outro/neon-triple-marquee/NeonTripleMarquee.tsx` |

## What it does

三行对向霓虹跑马灯 recap——BETTER/FASTER/STRONGER 空心描边巨字上中下排满全屏，奇偶行反向匀速无限横滚，三行按 1/3 相位轮流亮起，结尾整组淡出

**When to use it.** 片尾主题词复读机段落；三连词口号的"余韵"拍法（cel-flash-stomp 砸完之后的低一档收尾）；音乐段无旁白铺陈

**Why this shot earns its place.** 一行 marquee 只是网页装饰；三行叠起来、奇偶反向、再让亮度按相位轮流 走，就成了"主题词在观众眼前列队巡游"。命门是**明暗轮唱**：任一时刻 只有一行是霓虹主角，其余压暗成细描边背景——三行全亮是灯牌事故， 轮流亮才是 recap。反向对滚制造"包围感"：上下行向右、中行向左， 视线被夹在中间，词从两侧源源不断流过，读作"这三个词说不完"。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 字号/行距 | 300px，行距 350px 排满 1080 | 行间留白 >80px 读作三条横幅广告而非一面词墙 |
| 滚速 | 14/17/14 px/f，中行反向 | >25 读不清词只见光带；三行同速同向读作整版平移 |
| 脉冲周期 | 45f，相位差 15f | 周期 <30f 三行抢闪读作故障；>70f 轮唱感断掉 |
| 亮度区间 | opacity 0.35→1 + stroke 5→8px | 暗态 <0.25 暗行消失，"三行"结构丢了 |
| 辉光 | 双层 drop-shadow，亮态 30/70px | 单层或 <20px 读作普通描边字不读作霓虹 |
| 淡入淡出 | 入 10f / 出 20f 整组 opacity | 循环体无始无终，掐头去尾全靠这两端；硬切进出读作素材没铺满 |

## Known pitfalls

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
- 与 page-waterfall-wall 分工：那卡是页面截图纵向瀑布做"内容体量感"，
- 与 outro-group-photo-launch 分工：全家福是峰值终镜（元素合影+发布会收场），
- 与 cel-flash-stomp 同吃"三连词口号"文案：那卡逐词砸（高能宣告），
- 副本数按 `ceil(1920/unitW)+3` 留冗余——短词（≤4 字符）unitW 小，
- 实战品牌色版：三行可统一品牌色靠明暗区分，但辉光对比须 ≥ demo 的

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/outro/neon-triple-marquee/NeonTripleMarquee.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
