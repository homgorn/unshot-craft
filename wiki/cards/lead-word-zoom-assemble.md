# lead-word-zoom-assemble

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/lead-word-zoom-assemble`.

## Identity

- **slug**: `lead-word-zoom-assemble` (join key across cards, demos, media and deep links)
- **category**: `typography` — Typography & Title Cards / 文字与字卡
- **energy**: `中高` — rank 5/8
- **suggested duration**: 约 2.8s（84f@30fps；组句 f32 完成、上移与副行 f34–50、静止 22f、末 12f crash） → **84 frames @30fps = 2.8s**
- **cross-category tags**: `opening`, `typography`
- **upstream source**: references/shots/typography/lead-word-zoom-assemble.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `lead-word-zoom-assemble` | 84f | B | `demos/typography/lead-word-zoom-assemble/LeadWordZoomAssemble.tsx` |

## What it does

首词以 2.3 倍字号占据画面中央、hold 期间继续推近 6%，随后一条曲线同时完成「缩回终字号」与「整行左滑归位」，后续词各自从槽位右侧 0.5em 被推进来；支点横向钉首词中心、纵向钉基线（挂载时实测），整行上移的同一时窗副行浮出，停一拍后整幕 crash-zoom 推近失焦交棒

**When to use it.** 品牌名/产品名的 Introducing 字卡；发布会式开场第二镜；一句话主张需要"先让一个词占满画面、再把整句补齐"的场合

**Why this shot earns its place.** 字卡最容易犯的错是"整句一起淡入"——观众同时收到 5 个词，一个都没记住。这张卡把 阅读顺序做成**物理顺序**：先只给一个词，而且大到占满画面、还在继续朝观众推近，观众 被迫先读它；然后这个词退回自己在句子里的尺寸和位置，整句围绕它长出来。落定时观众 已经读过两遍主词。 真正的手感命门不是缩放曲线，而是**支点**。首词从"画面正中"走到"行内第三个字符的 位置"，如果支点取行盒中心，缩放和左滑会各自把字往两边拽，末尾几帧基线抖得肉眼可见。 把 `transform-origin` 横向钉在首词中心、纵向钉在基线，这两点全程不动，整行就只是 "收小"，没有任何漂移。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 首词起手倍数 | initialScale 2.3 | 2.3 让首词横向溢出画面一点点（读作"太大了装不下"）；<1.8 只是"稍大的字"，冲击消失 |
| 推近 | pushScale 1.06，占满 hold 12f | 6% 是"还在朝观众来"的最小可感量；>1.15 会在缩回时读作反向弹跳 |
| hold | 12f | 首词独占画面的时长；<8f 观众读不完一个长单词，>20f 整句节奏塌 |
| 缩回 | 12f，ZOOM_EASE | 与左滑同曲线；单独给缩回一条更快的曲线会让整行"先缩完再滑"，断成两拍 |
| 左滑 | assembleDuration 24f | 比缩回长一倍：字号已经落定、位置还在走，这段"滑行尾巴"是电影感的来源 |
| 后续词延迟 | wordDelay 6f（缩回起点之后） | 首词开始缩回才放后续词；同帧放会挤在一起看不清谁在动 |
| 词间错峰 | wordStagger 4f | 4f 读作"依次被推进"；0 则整段后缀一起进，回到"整句淡入" |
| 单词推入 | wordDuration 12f，wordPush 0.5em | 0.5em 是"刚从槽位外面"；>1em 会读作从画外飞入，与首词的收束方向打架 |
| 词淡入 | wordFade 2f | 刻意极短。>6f 词会读作"浮现"，推入的力学感消失 |
| 字号/字重/字距 | 96px / 600 / −0.03em | 负字距在放大 2.3 倍时才不会散架；正字距的大字会读作"标语横幅" |
| 上移 + 副行 | f34–50，−56px，副行同窗 | 两件事必须同窗：先上移再出副行会多出一个空当拍 |
| 静止 | 22f | 落定后的可读时间，低于 15f 观众来不及读副行 |
| crash | 末 12f，scale→1.2，blur→9px | 这是转场的**前半**，动机要和下一镜的第一帧对上；单独播时看起来像"没结束"是正常的 |

## Known pitfalls

- **支点错了就抖基线**。`transform-origin` 必须是「首词中心 % + 基线 px」这一对。
- 基线别估算。`lineHeight × 0.8` 这类经验值在不同字体上差几像素，放大 2.3 倍后就是
- `delayRender` 期间整行 `opacity: 0`——**必须**如此。否则未量到支点的第一帧会闪一下
- 布局是挂载时实测的，所以**结果随渲染环境的字体而变**：跨平台字体回退不同时整行宽度
- `scale` / `translate` 用的是独立 CSS 属性（不是 `transform` 简写）。混用会让其中一个
- 词间空格放进词 span 内部会被行盒裁掉（见上）。这个 bug 在小字号下不明显，96px 时
- 首词必须是**短词**。"Introducing" 这类 10 字符左右刚好；首词超过 14 字符时 2.3 倍
- 强调色只给一个词。两个词都上色时观众不知道该记哪个，而且推入落位的高亮变成了
- 末段 crash 是转场的前半式，不是收尾。单独当片尾用会显得"断了"——要收尾就把

## Card structure

`intention` | `motion` | `params` | `pitfalls` | `impl`

**Implementations**
- `demos/typography/lead-word-zoom-assemble/LeadWordZoomAssemble.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
