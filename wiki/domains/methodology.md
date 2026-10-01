# Methodology

The part of the repo that makes it a production discipline rather than a component library. Four documents plus the ruling law.

## Documents

### `aesthetic-rules.md` — The ruling law: 26 numbered precedents in five families (R rhythm, Q quality, S sound, C copy, P process)

Sections: `目录`, `节奏（R）`, `R1. 关键信息落定后必须呼吸，品牌字标 hold 满 1 秒`, `R2. 速度感来自加速度，不是匀速快；群体运动挂物理隐喻，收尾留 0.5s 停顿`, `R3. 节奏宁慢勿快：初版默认放慢一档，主体动作弧 ≥3s，交互演示按真人操作速度`, `R4. 卡点约束时机不放大幅度：全画面级节拍冲击全片 ≤3 处，默认只动元素层`, `质感·运镜·构图（Q）`, `Q1. 复刻既有页面必须真实截图；手搓 UI 限非复刻场景且质量/表达达标；数据按风险口径处理`, `Q2. 3D 透视下 UI 纹理按原生尺寸 rasterize 后缩小使用；文字发糊先查纹理分辨率链路`, `Q3. 镜头要稳：产品宣传片默认不加手持抖动`, `Q4. 高光/扫光特效宁缺毋滥：不群发，一个镜头最多给主角一次，且必须裁进圆角边界`, `Q5. 开场只给一个主角：单主体 + 完整动作弧，胜过群体群舞`, `Q6. 机位服务可读性：信息密集镜头正视，文字特写侧向水平，风格化倾斜逐镜头验证`, `Q7. 物件特写四件套：侧面倾斜角 + 可感知高度 + orbit 环绕 + 反差深色材质背景`…

### `final-review.md` — Clean-context subagent acceptance checklist, eight groups, frame-numbered evidence required

Sections: `审查输入`, `检查项`, `P — 产品目标`, `F — 功能完整性`, `V — 视觉方向`, `S — 镜头卡与 Gallery 变体`, `B — 分镜一致性`, `D — 数据与素材安全`, `A — 音频与节奏`, `Q — 视觉技术质量`, `报告格式`

### `guided-free-creation.md` — Co-creation mode: five user confirmation gates plus the Gallery shot-name resolution protocol

Sections: `目录`, `1. 产品简报`, `2. 需求到执行决策表`, `3. 视觉方向`, `4. 功能到镜头映射`, `5. Gallery 镜头名称解析`, `6. 分镜确认`, `默认与跳过规则`, `每轮回复格式`

### `jianying-export.md` — Export a Remotion timeline to an editable JianYing (CapCut CN) draft

Sections: `1. 分层原则：什么可编辑、什么烘焙`, `2. plate 底片渲染`, `3. 时间线数据提取`, `4. 建轨（pyJianYingDraft 0.3.x）`, `5. 装进剪映草稿库`, `6. 验收`

### `music-beat-sync.md` — BGM beat-grid methodology: least-squares fit, transient classification, beatF(n) timeline, 3-frame tolerance

Sections: `目录`, `0. 何时启用`, `1. 节拍网格测定（不要相信 beat_track 的 tempo 标量）`, `2. 鼓点分类与能量结构（决定什么钉在哪一拍）`, `2a. 三分类瞬态检测`, `2b. RMS 能量曲线与结构表`, `3. 网格验收与产物（先验收，后分镜）`, `4. 时间线用拍号写，不用帧号写`, `5. 渲后回测（闭环，必做）`, `5a. 两种误差分开报，不混为一谈`, `5b. 渲出成片抽音轨回测`, `6. 工具备忘`

### `pipeline.md` — Eight-stage production pipeline, stage 0 product understanding to stage 7 independent final review

Sections: `目录`, `阶段 0：产品理解与执行约束`, `阶段 1：视觉方向与 styleframe`, `阶段 2：功能到镜头映射`, `阶段 3：分镜与制作放行`, `阶段 4：最终素材采集`, `阶段 5：逐镜头实现`, `阶段 6：声音设计`, `阶段 7：验收`

### `sound-design.md` — SFX methodology: BGM energy skeleton, genre vocabulary, declarative cue table, exclusion lists

Sections: `目录`, `1. 方法`, `2. BGM 选型`, `演进：三易其稿（34 分钟）`, `选型判据（从用户原话反推）`, `免费授权来源清单`, `3. SFX 词汇表`, `3.0 目录结构与找音路径`, `3.1 基础层：模板片实际使用的 14 个`, `3.2 同素材重名：4 对文件字节完全相同`, `3.3 `ui/` 目录必须逐个试听，不能整目录放行`, `4. 对齐技巧`, `4.1 钉帧方法`, `4.2 变调与防机枪感`…

### `workbench.md` — Integration contract for the post-delivery browser workbench: manifest shape and the fixed-vs-exposed parameter rule

Sections: `1. 三层可编辑度：什么能改、代码要满足什么`, `2. 成片工程接入清单 `src/workbench.ts``, `3. 制作新片时怎么写镜头（让它"未来可编辑"）`, `4. 动效库（demos/）在工作台里的形态`, `5. 导出、Studio 与无损校验`, `6. 已知边界`

## The ruling law: aesthetic-rules.md

27 numbered precedents in five families. IDs are append-only upstream and must never be renumbered — they are cited from the shot cards, so a renumber silently breaks every cross-reference.

### Family C — copy (3 rules)

| id | title |
|---|---|
| `C1` | 规则：初稿文案只是占位——画面定稿后对照成片逐镜头重写；纯动画镜头配短解说 caption，不留"哑巴段落"（品牌收尾镜头除外，保持干净）。 |
| `C2` | 规则：标语要具体、带产品功能名（Paper Radar / weekly report），避免抽象隐喻词（board/place 类泛化口号）；重要功能出场前加一张引导字卡。 |
| `C3` | 规则：给 3D 场景中的主体配画内注记时，文字必须进同一 3D 空间（页面坐标系、同一台相机透视、translateZ 悬浮 + 落影），平面叠字与场景脱节；样式用大衬线字 + 马克笔 highlight 关键词。 |

### Family P — process (4 rules)

| id | title |
|---|---|
| `P1` | 规则：每轮修改后先自行渲染关键帧截图逐一检查（构图/抖动/文字锐度/穿帮），必要时用像素级工具（裁剪放大/两帧 diff）自证，再交用户。 |
| `P2` | 规则：有参考片先抽帧做 motion breakdown（每个动画/转场/特效的实现方式清单）写进 spec，按项目适配性取舍；图片参考描述的是"某一类镜头"的感觉而非全片风格令——落地前逐镜头判断适不适用，改完自查再交。 |
| `P3` | 规则："第一个标题"式模糊反馈先确认所指再动手；落错对象立即整 commit revert 重来；每个改动保持独立 commit 以便干净回滚。 |
| `P4` | 规则：开拍前列产品功能清单（dashboard/详情/论文/周报/品牌）逐一映射镜头，核心功能漏拍等于返工；一种手法（飞入/堆叠/翻页）全片只当一次主角；剪辑自查按"这个镜头给了什么新信息"过滤，同一素材/信息全片只出现一次，重复即删。 |

### Family Q — texture, camera, composition (11 rules)

| id | title |
|---|---|
| `Q1` | 规则：凡是表现产品既有页面的镜头，第一步就用无头浏览器截真实页面（整页纹理 + 元素级抠图 + 坐标 json），不手搓仿真贴图复刻；非复刻场景（抽象开场/品牌段/页面上不存在的独立展示组件）允许手搓 UI，但质量（出版级质感，对照 Q10 标准）与表达明确性（观众一眼看懂它是什么）是硬门槛，达不… |
| `Q10` | 规则：观众会读清屏幕上每个字——文档/报告类镜头的 mock 必须用产品原生排版灌满真实密度的假内容，侧栏/评论栏等版式元素完整入镜；"贴图+标语"级别的假文档整镜头返工。 |
| `Q11` | 规则：1080p 成片按手机/内嵌小窗播放校准可读性——镜头叙事字幕**有效字高 ≥56px（≥5.2% 帧高，推荐 60px 档）**，副标题/统计/URL 等辅助文字 ≥32px（≥3%）；有效字高 = fontSize × 全部祖先 scale × 透视压缩（3D 镜头按 `cos(rotY… |
| `Q2` | 规则：3D 场景里的 UI 纹理按显示尺寸的 2–4 倍原生栅格化、在 3D 里向下采样（放大走布局级 CSS zoom 而非 transform scale）；文字模糊先查栅格化路径，别先动相机/DoF。 |
| `Q3` | 规则：亮场 UI 宣传片禁用 handheld shake；相机噪声只在暗场氛围片明确追求纪实感时用极小值，且必须自查渲染帧确认无意外抖动。 |
| `Q4` | 规则：glint/泛光划过类特效不做群发——批量元素入场靠运动本身而非逐个发光；保留的光效必须被承载元素的 border-radius/overflow 裁剪，光溢出圆角是廉价感的典型来源。光效类技术路径本身不封杀：单点、给主角、实现质量过硬的 sheen/泛光可以做，做完对着渲染帧自问"好看吗"… |
| `Q5` | 规则：开场信息宁少而聚焦——一个主角元素、一条完整弧线（聚光→推近→悬浮→描边光→归位），多元素并舞撑不起第一印象。 |
| `Q6` | 规则：风格化机位按镜头逐个决定——叙事/情绪镜头可倾斜，列表/堆叠等信息密集镜头保持正视；含文字的卡片特写用侧向水平机位，避免大角度仰拍/俯拍破坏文字可读性；禁止全局一刀切套用某种机位风格。 |
| `Q7` | 规则：物件/资产特写镜头做足环境戏——侧面倾斜机位、堆叠出可感知的体积高度、镜头绕主体环绕，背景用与主场景反差的深色材质（如拉丝金属），再用拉远同步过渡回主场景。 |
| `Q8` | 规则：多功能产品的收尾用"全家福"结构——每个已展示过的功能抽一个代表元素多方向飞入定格；规格匹配全片能量峰值（crane 运镜 + 舞台光 + 粒子），初版收尾几乎总是偏保守，默认加码一档。 |
| `Q9` | 规则：元素飞入后要"嵌入"页面（归位到真实格位、扩展滚动流），不落地悬浮其上会显得假。 |

### Family R — rhythm and holds (4 rules)

| id | title |
|---|---|
| `R1` | 规则：承载信息的元素（字卡/数字/网格全貌）落定后静止 ≥1s 再切镜；呼吸感停顿优先给品牌记忆点（wordmark 落定时刻），不给普通内容卡片。 |
| `R2` | 规则：飞入/滚动一律非线性缓动 + 非均匀错峰，匀速运动读作廉价 PPT；大量同类元素入场用"越来越快"的硬加速节拍，最好绑一个物理隐喻（如牌堆发牌），满板后静止 0.5s 再切下一拍。 |
| `R3` | 规则：开场主体动作（聚焦→悬浮→归位一条完整弧线）至少 3 秒；模拟真实交互（打字、筛选、点击）按人真实操作的速度走，观众要能跟着做一遍；排时间线时预留 hold/rest 帧预算——第一版几乎总是偏快。 |
| `R4` | 规则：强节奏 BGM 片"切点落拍"不等于"逐拍打画面"——作用于整画面/相机层的冲击（整画面 scale 泵/震屏/闪帧/负片帧）视同大 slam 管理：全片 ≤3 处、钉 music-beat-sync §2b 的最强 hit 清单、相邻两处间隔 ≥16 拍；其余拍点动效只作用主角元素层；节拍… |

### Family S — sound (5 rules)

| id | title |
|---|---|
| `S1` | 规则：产品宣传片 SFX 词汇表 = whoosh(运镜)/impact(落地)/riser(铺垫)/sparkle(光效)/transition(转场)，禁用游戏音包音色；BGM 选强鼓点、强节奏的电子底（tech-house 类），候选曲必须垫进成片试听——单听曲子无法判断气质。 |
| `S2` | 规则：SFX 用"帧号 + 音源 + 音量"的声明式表集中管理，逐条注释对应的画面动作，杜绝凭感觉铺音效；同类元素连发时防机枪感靠三招——双样本交替、沿序列音量阶梯递减（如 0.40→0.25 六级）、间隔跟随动画曲线加速，密到糊成一片时让声音淡出成 swoosh（本仓库实证无 playbackR… |
| `S3` | 规则：BGM/SFX 排在画面结构基本锁定之后；任何改变镜头时长/顺序的修改，收尾动作固定包含"全表 SFX 帧号重对"——音画错位是交付前必查项。 |
| `S4` | 规则：画面里发生什么动作就配什么声音（打字画面配键盘声、逐条落入配逐个 pop），泛用 swoosh 盖不住有辨识度的画面动作；长样本按画面段落裁剪（Sequence 截断），时长与动作严格等长。 |
| `S5` | 规则：渲出成片的整条音轨相对视频有固定滞后，根因在输出编码/封装链路（AAC encoder priming，48kHz 典型 2048 samples ≈1.28f@30fps；Remotion 跟踪 remotion-dev/remotion#7099），不是 `<Audio>`/`Seque… |

## The energy arc

`references/sequences/promo-energy-arc.md` is the default whole-film skeleton for a 30–60s multi-feature web product promo:

| stage | share | energy | duty |
|---|---|---|---|
| ① Brand open | — | — |  |
| ② Single-hero portrait | — | — |  |
| ③ Feature climb | — | — |  |
| ④ Launch finale | — | — |  |

Rule of thumb the cards repeat: **open low, alternate mid-high with breath beats, peak at the outro.** Historical feedback in the repo only ever asked for slower/hold longer; there is no 'too slow' precedent.
