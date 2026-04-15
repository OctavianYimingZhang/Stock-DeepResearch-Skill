# Report Format — Section-by-Section Guidance (Themed Structure)

This file defines the depth and content requirements for each section of the analyst-style research report. The report follows a **themed** structure, not numbered parts (第一/第二/第三/第四部分).

## Title Block

```
[Company Name]（[Ticker]）深度研究报告：
[Subtitle — one-line thesis, e.g., "AI 驱动下的业务逻辑重构与 2026 年市场估值展望"]
```

The subtitle should capture the SINGLE most compelling angle. Examples from real analyst reports:
- "从比特币矿工到AI云新秀" (IREN)
- "北美业务重组下的价值重估" (CSIQ)
- "困境反转的关键阶段" (COMM)
- "数据中心电力需求的隐形赢家" (SEI)
- "需求锁死再扩产的逻辑" (TSEM)
- "锑战略金属 + 白银副产品的双轮驱动" (UAMY)

## 公司简介 (Company Overview)

**Length**: 1-2 paragraphs, 100-200 words
**Purpose**: Set context. Reader should know what the company does in 30 seconds.

**Must include**:
- What the company does (one sentence)
- When founded, where headquartered
- Key stats: market cap, revenue, employees (approximate)
- Which exchange/ticker

**Must NOT include**:
- Detailed product descriptions (save for 运营逻辑)
- Financial analysis (save for 财务数据)
- Investment thesis (save for 业务逻辑)

## 业务逻辑 (Business Logic)

**Length**: 2-4 paragraphs, 400-800 words — THIS IS THE LONGEST AND MOST IMPORTANT SECTION
**Purpose**: Tell the transformation story that makes this stock interesting RIGHT NOW.

**Must answer four questions in narrative form** (not as a bullet list):
1. What was the OLD value driver? (with specific data — e.g., "主要赚手机周期的钱")
2. What is the NEW value driver? (with specific data — e.g., "AI 芯片复杂度提升带来的测试收入")
3. What structural change enabled or forced this transformation? (e.g., AI buildout, trade war, technology inflection)
4. If successful, what does the company look like in 3-5 years?

**Must include**:
- Specific data points showing the shift (e.g., "计算类从 SoC 收入 10%→80%")
- Management quotes with dates (e.g., "Greg Smith 在 Q4 2025 电话会中指出...")
- Industry chain context woven in naturally
- Governance observations (from risk sub-report) if structurally relevant — e.g., "公司将法人住所从蒙塔纳州变更为德克萨斯州，反映了其优化资本结构的治理逻辑"
- **TAM + market share framing (MANDATORY)**: For each key end market or product segment, state the TAM size (or relative size) and the company's estimated market share. Explain WHY the company wins design-ins vs. competitors (at least one specific technical or relational reason). Without this, business logic becomes assertion rather than analysis.
  - Example (TER pattern): "ATE 不是简单跟着半导体总收入走，而是更像'收入增量的导数市场'；真正驱动 ATE TAM 的，是客户为了支持更高收入增长而新增的测试产能。"
  - Example (TSEM pattern): "超大规模云服务商对 800G 及 1.6T 光收发器的迫切需求 — SiPho TAM 预计 2027 年达 $20B，公司作为主要代工商占据 ~40% 份额。"

**Must end with a section-closing summary sentence (MANDATORY)**: Every 业务逻辑 section must close with ONE bold conviction-level summary sentence in this format:

> **总结**: [Company] 的核心逻辑是 [X], 当前处于 [Y] 阶段，关键验证变量是 [Z]。

Examples from real analyst reports:
- "**业务总结**: TSEM 是做 AI 数据传输基础设施，RF Infrastructure 是容器，SiPho 是核心增量。"
- "**业务总结**: 这不是先扩产再找需求，而是需求锁死再扩产。"
- "**业务总结**: UAMY 从早期的锑冶炼厂进化为美国本土锑产业链的唯一整合者，叠加银和铜副产品回收。"

This crystallizing line forces the writer to commit to a thesis rather than leave the reader to infer one.

**Patterns from real analyst reports**:
> "TSEM 过去主要赚'传统成熟制程代工的钱'，现在主要赚'AI 基建复杂度提升的钱'。逻辑核心是：需求锁死再扩产，而不是先扩产再找需求。" (TSEM)

> "这不是一个单纯的反弹故事 —— UAMY 从早期的锑冶炼厂进化为美国本土锑产业链的唯一整合者，叠加银和铜副产品回收。" (UAMY)

**If no transformation is happening**: State "公司处于稳定运营模式" and focus on what's changing at the margin.

## 运营逻辑 (Operating Logic)

**Length**: 2-4 paragraphs + capacity-ramp table, 400-700 words
**Purpose**: HOW does the business logic convert into P&L, and when?

**Must include**:
- Capacity by named facility with ramp schedule (e.g., "Thompson Falls 产能从 100 吨/月扩至 300-500 吨/月，Q1 2026 投产")
- Capex cadence (quarterly or annual capex numbers with guidance)
- Utilization targets (e.g., "2026 末预计达到 85% 利用率")
- **Bottom-up unit economics for commodity/industrial names** — see `commodity-math-template.md`
- **Operating leverage decomposition** (incremental margin walk): "从 Q1 to Q4 收入 +$82M，净利润 +$41M，incremental margin ~50%"
- Specific product mix shifts (e.g., "SiPho 收入从 2024 年 $106M 增至 2025 年 $228M，+115%")

### MANDATORY Unit-to-EPS Derivation Chain

For any company whose thesis depends on margin expansion or capacity ramp, the 运营逻辑 section MUST walk from a physical input (utilization %, unit volume, ASP) all the way to EPS — with explicit numerical links at each step. Qualitative descriptions alone are NOT enough. This is the biggest gap between Claude reports and analyst reports.

**Required chain format (5 steps):**

```
Step 1 (PHYSICAL): Utilization 78% → 85% (or: Volume 1.0M lb → 2.0M lb)
    ↓
Step 2 (COST LEVERAGE): Fixed cost absorption improves by $XM (fixed cost base ~$YM × 7ppt uplift)
    ↓
Step 3 (GROSS MARGIN): GM expands from 31.2% → 34.0% (+280bp)
    Gross profit change: $1,680M × 280bp = +$47M
    ↓
Step 4 (EBIT / EBITDA): Operating leverage on SG&A (largely fixed) adds additional $YM
    EBIT change: +$47M + $YM = +$ZM
    EBIT margin: 15% → 18%
    ↓
Step 5 (EPS): After-tax (~21%) / diluted share count (46M)
    EPS change: $ZM × 0.79 / 46M = +$X per share
    2027E EPS: $1.42 + $X = $4.00
```

**Why this chain matters**: Without it, the analyst can't connect "利用率改善" (a vague claim) to "目标价 $100" (a specific number). Every step in the chain should be a math expression the reader can verify.

**Real analyst example (TSEM):**
> "25 年硅光子产能及相关收入 396.3M，未来产能扩大 5 倍…3275.9 × 0.264 = 864.84M…EPS 2025 是 1.93，到 2027 年 7.72，复合增长率是 100%."

This is exactly the level of arithmetic rigor required. The TSEM analyst derives 2027 EPS $7.72 from a physical capacity assumption — not from consensus.

**Pass condition**: If you cannot do the full 5-step chain (because the physical variable is unknown), explicitly state which variable is blocking and what data would unblock it. Do NOT silently use "consensus assumes X" — that hides the analyst's job.

**Capacity ramp table format**:
```
| Facility | Current | 2026 Target | 2027 Target | 投产日期 |
|----------|---------|-------------|-------------|---------|
| Thompson Falls | 100 t/mo | 300 t/mo | 500 t/mo | Q1 2026 |
```

**Patterns from analyst reports**:
> "2028 target table: revenue $15.66B → $28.4B, gross profit +207%, 假设 85% 利用率。" (TSEM)

> "2026 production → ~2 million lb U3O8 annually；April 2025 4,604 吨矿石 × 1.64% 品位 = 151,400 lb U3O8 产量。" (UUUU)

## 客户与订单 (Customers & Orders)

**Length**: 1-2 paragraphs + 1-2 tables, 300-500 words
**Purpose**: Who pays this company, and how locked-in is the revenue?

**Must include**:
- **Top-5 customers by NAME** with revenue share and strategic significance
- Contract/backlog walk with delivery cadence (contract-by-contract if disclosed)
- Customer CAPEX trends (are key customers in expansion mode?)
- If customer names are not disclosed, use segment or geography as proxy AND state the limitation explicitly

**Customer table format**:
```
| 客户 | 营收占比 | 趋势 | 战略意义 |
|------|---------|------|---------|
| NVIDIA | ~15% | 快速增长 | AI GPU 测试核心客户 |
| Samsung | 12% | 稳定 | 存储器测试 + SoC 双条线 |
```

**Contract walk format**:
```
| 合约 | 总额 | 2025 交付 | 2026 交付 | 状态 |
|------|------|----------|----------|------|
| DLA IDIQ | $245M | $10M | $50-60M | 首批发货 |
```

**Pattern from analyst reports**:
> "$351.7M 订单储备，其中 2025 年交付 $124M，2026 年交付 $185M，剩余在 2027 年。" (UAMY)

## 财务数据 (Financial Data)

**Length**: Tables + 2-3 paragraphs commentary, 400-600 words
**Purpose**: Show the numbers that support the thesis and flag any quality concerns.

**Must include**:
- **3-year financial comparison table**: Revenue, Gross Margin, EBITDA, Net Income, EPS, FCF
- **Forward model table** with explicit growth drivers in column headers (not just "consensus")
- Management guidance for next period (with date of guidance)
- 2-3 key earnings call quotes with dates and speakers
- **Short-seller risk grade embedded as one line**: "做空风险评级: [A/B/C/D/F]（[score]/100）— [one-line verdict]"
- If risk grade C+, expand to a full paragraph with named red flags

**Table format**:
```
| 指标 | FY2023 | FY2024 | FY2025 | 2026E | 趋势 |
|------|--------|--------|--------|-------|------|
| 收入 ($M) | 1,662 | 1,311 | 1,482 | ~1,680 | 周期底部回升 |
| 毛利率 | 39.6% | 33.2% | 31.2% | ~34% | 底部反转 |
| FCF ($M) | 130 | 46 | 137 | ~160 | 已恢复 |
```

**Forward model table** (MUST have drivers, not just "consensus"):
```
| 指标 | 2026E | 驱动力 |
|------|-------|-------|
| 收入 | $1,680M | 汽车 +24% YoY × 占比 19% + 计算 +25% × 27% + 其他持平 |
| 毛利率 | 34% | 内部晶圆厂利用率从 72% → 82%，摊销降 +300bp |
| EBITDA | $244M | 14.5% 利润率，上行 vs 2025 年 13.1% |
```

## 估值情况 (Valuation)

**Length**: 2-3 paragraphs + 1-2 tables, 400-700 words
**Purpose**: What is this stock worth, and WHY — based on ONE primary method, not an average of 9.

**Must include**:
- **ONE primary valuation method** chosen by company archetype:
  - Semiconductor cyclical → mid-cycle EPS × 10-year average P/E
  - Growth foundry / specialty semi → forward EV/EBITDA with multiple-expansion thesis
  - Mining/commodity → lb/ton × commodity price × margin → EBITDA × peer EV/EBITDA
  - Turnaround → P/FCF or replacement value
  - High-growth SaaS → EV/Revenue with Rule-of-40 check
- **Primary method derivation** with every input named: "2027E EPS $8.34 × 十年平均 PE 29x = 目标价 $242"
- Peer comparison table (3-5 peers, 4-6 columns max)
- Bull/base/bear in prose (one sentence each) — NOT a probability-weighted table
- **Multiple re-rating catalyst**: what moves the stock from current to target multiple?
- For commodity companies, unit-math appears BEFORE multiple work

**Peer table format**:
```
| 公司 | 市值 | 2026E EV/EBITDA | 2026E P/E | 核心差异 |
|------|------|----------------|-----------|---------|
| DIOD | $3.8B | 14.4x | 39.5x | 清洁资产负债表 |
| ON Semi | $28B | 11x | 22x | 规模经济 |
| Vishay | $2.5B | 9x | 18x | 成熟业务 |
```

**Key patterns from analyst reports**:
> "考虑到过去十年公司的平均 PE 是 29 倍，对应 EPS $8.34，目标价约 $242。" (TER)
> "最保守情况下，公司估值应该是 45 亿左右。" (CSIQ)
> "Gen3 BCD → 60% EBITDA margin target → $20B × 30x multiple → ~$60B 市值。" (TSEM)

**Kill these**:
- Do NOT run 9 methods and average them
- Do NOT create a "Probability-Weighted Fair Value" row
- Do NOT label methods as "supplementary / primary / secondary / tertiary" — it's ONE primary method, others are sanity checks at most

## 技术分析 (Technical Analysis)

**Length**: 1-2 paragraphs + one small price-level table, 150-200 words
**Purpose**: What does the chart say, and does it confirm or contradict the thesis?

**Must include**:
- Monthly / weekly / daily trend direction (one sentence each)
- Current primary pattern with breakout status
- 2-3 key support and 2-3 key resistance levels (in small table)
- Whether technicals confirm or contradict the fundamental thesis (one sentence)

**Price level table format**:
```
| 位置 | 价位 | 说明 |
|------|------|------|
| 即时阻力 | $85-88 | 当前突破区域 |
| 主要阻力 | $100 | 心理整数位 |
| 强支撑 | $72-75 | 财报后整理区间 |
```

**NO Wyckoff-phase table in the final report.** Translate to plain Chinese: 投降 → 反弹 → 回测 → 突破 → 上升趋势.

**Pattern from analyst reports**:
> "日线呈现牛旗结构，下方跌破 20 元可以考虑先出来。" (CSIQ)
> "一个不太规则的杯柄结构，同时周线突破。上方在 30 元位置是涨幅满足位。" (IREN)

**Do NOT re-explain the trade plan here** — that belongs in 交易计划 at the end.

## 风险提示 (Risk Summary)

**Length**: Bullet list, 3-5 items, 150-250 words
**Purpose**: What could go wrong?

Each bullet: risk name → severity → what to watch for.

**Kill these**:
- No scoring matrix
- No probability table
- No "Red Flag Inventory"
- No icons (✅/⚠️/⏳)
- No "数据充分性说明"

## 交易计划 (Trade Plan) — REQUIRED ENDING

**Length**: Prose, 200-350 words
**Purpose**: Tell the reader exactly what to DO.

See `trade-plan-template.md` for the exact format. Required fields in this exact order:

- **评级**: 买入 / 持有 / 观望 / 卖出
- **建议仓位**: X-Y% of portfolio (with reasoning)
- **入场区间**: $X-$Y (with reason)
- **止损位**: $Z (corresponding to what invalidates the thesis)
- **第一止盈位**: $A (method, e.g., "基于 2026E EPS × 历史平均 PE")
- **第二止盈位**: $B (method)
- **90 天内最重要催化剂**: single most important event with date
- **做空风险**: letter grade + one line
- Final line only: "本报告仅供研究参考，不构成投资建议。"

**Kill these endings**:
- Do NOT end with a 4-row "综合总结" matrix
- Do NOT end with multiple disclaimers
- Do NOT end with "基于多模型估值分析，概率加权公允价值..."

**Patterns from real analyst reports**:
> "仓位推荐 5% 到 10%。第一个止盈目标 45，第二个目标 55。止损位 18。关键催化剂：Q1 2026 财报验证 Thompson Falls 投产节奏。" (CSIQ-style)
> "先看 100 亿市值。止损 8.6 下方。第一波止盈 15。" (IREN-style)
> "目标价 300，推荐仓位 10-15%。" (DAVE)
