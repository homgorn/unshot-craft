# ai-stream-response

> One of 157 shot recipe cards in video-shotcraft. Machine index: `wiki/index.json#/cards/ai-stream-response`.

## Identity

- **slug**: `ai-stream-response` (join key across cards, demos, media and deep links)
- **category**: `interaction` — Interaction & Feature Demo / 交互与功能演示
- **energy**: `中高` — rank 5/8
- **suggested duration**: 约 4–5s（120–150f，含 ≥15f 完成态静止） → **150 frames @30fps = 5.0s**
- **cross-category tags**: `interaction`
- **upstream source**: references/shots/interaction/ai-stream-response.md

## Variants (styles)

| letter | style key | duration | family | demo |
|---|---|---|---|---|
| — | `stream-response` | —f | B | `demos/interaction/ai-stream-response/StreamResponse.tsx` |

## What it does

AI 响应面板先落一句可读摘要，再让带状态图标的证据行逐条汇入，最后统一收束成完成态

**When to use it.** AI 助手/agent/search/copilot 的结果生成镜头；强调“结论先到、证据随后、任务完成”

**Why this shot earns its place.** 把“AI 正在工作”拍成可读的因果链，而不是日志刷屏：观众先看懂答案摘要， 再看到证据/子任务逐条补齐，最后由完成态确认这轮工作结束。

## Parameters

| parameter | typical value | how to tune |
|---|---|---|
| 摘要 | cue 18，10–14f reveal；摘要落定后 hold ≥12f，首行 cue ≥42 | 摘要与首行粘连会失去“结论先到”的叙事；正常速度必须能先读到一句完整结论 |
| 行节拍 | `cue[i]=42+[0,11,21,30,38,45,51,56][i]`，每行 10–14f | 间隔 11→5f 逐渐收紧，表达工作加速；不要密到所有行同时糊成一团（R2） |
| 行入场 | y 18px→0，blur 6px→0，opacity 0→1，bezier(0.2,0.75,0.25,1) | 位移须过正常速度肉眼阈值；大幅横飞会像通知列表，不像证据归档 |
| 状态图标 | 比行体 cue 晚 3f；pending 环 → running 缺口环 → done 实心勾，6–8f | 图标是状态回执，不抢行文本；同帧切换全部图标会读作假 loading |
| 完成收束 | 末图标 done 后 6f，面板边框/摘要底色 opacity 0.25→0.55→0.25 共 10f | 只做面板级一次，不逐行发光（Q4）；完成脉冲后留 ≥15f 真静止（R1） |
| 相机 | 信息密集默认正视，zoom 1.04→1.0 微退；暗场斜拍仅作情绪变体 | Linear 参考片的斜拍不是通用命令；文字读不清时立即回正视（Q6） |

## Known pitfalls

- 逐字符流式打字会把视线困在字符层；宣传片时长里优先按“语义块”揭示摘要，
- 行体和状态图标若同帧落定，会像静态列表整体切换；保留 2–4f 拖拽层级
- 行终点必须是截图里真实列表槽位，不在面板上方悬浮；动态内容也必须用虚构数据
- 此卡借鉴 Linear Agent 发布片 t≈13–17s（进化轮 #3 breakdown #6），非用户判例；

## Card structure

`intention` | `motion` | `params` | `sound` | `pitfalls` | `impl`

**Implementations**
- `demos/interaction/ai-stream-response/StreamResponse.tsx`

---

Generated from `platform/db/shotcraft.db` @ `5ddbf521038b`. Do not edit: regenerate with `python platform/wiki/build_wiki.py`.
