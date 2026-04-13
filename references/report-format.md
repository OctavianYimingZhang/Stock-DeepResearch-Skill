# Report Format — Section-by-Section Guidance

This file defines the depth and content requirements for each section of the analyst-style research report.

## Title Block

```
[Company Name]（[Ticker]）深度研究报告：
[Subtitle — one-line thesis, e.g., "AI 驱动下的业务逻辑重构与 2026 年市场估值展望"]
```

The subtitle should capture the SINGLE most compelling angle. Examples from real reports:
- "从比特币矿工到AI云新秀" (IREN)
- "北美业务重组下的价值重估" (CSIQ)
- "困境反转的关键阶段" (COMM)
- "数据中心电力需求的隐形赢家" (SEI)

## 公司简介 (Company Overview)

**Length**: 1-2 paragraphs
**Purpose**: Set context. Reader should know what the company does in 30 seconds.

**Must include**:
- What the company does (one sentence)
- When founded, where headquartered
- Key stats: market cap, revenue, employees (approximate)
- Which exchange/ticker

**Must NOT include**:
- Detailed product descriptions (save for 业务运营)
- Financial analysis (save for 财务数据)
- Investment thesis (save for 业务逻辑重构)

## 业务运营 (Business Operations)

**Length**: 2-4 paragraphs + 1-2 embedded tables
**Purpose**: Explain HOW the company makes money.

**Must include**:
- Business segments with revenue contribution
- Revenue structure table (segment × revenue × YoY growth × % of total)
- Key products/services in each segment
- Geographic revenue distribution if material

**Table format** (example from TER report):
```
| 收入类别 | FY2025 ($M) | FY2024 ($M) | YoY | 占比 |
|---------|------------|------------|-----|------|
| 半导体测试 | 2,400 | 1,800 | +33% | 80% |
| 机器人 | 600 | 550 | +9% | 20% |
```

## 行业地位 (Industry Position)

**Length**: 1-2 paragraphs
**Purpose**: Where does this company sit in the competitive landscape?

**Must include**:
- Market structure (monopoly/duopoly/oligopoly/fragmented)
- Key competitors (3-5) with brief positioning
- Market share if available
- Third-party validation (Gartner, Forrester, industry rankings) if applicable

**Pattern from analyst reports**:
> "在测试设备这个关键环节，市场长期被Teradyne和Advantest高度垄断。" (TER)

## 业务逻辑重构 (Business Logic Transformation)

**Length**: 2-4 paragraphs — THIS IS THE CORE SECTION
**Purpose**: Tell the transformation story that makes this stock interesting RIGHT NOW.

**Must answer four questions in narrative form**:
1. What was the old value driver? (with specific data)
2. What is the new value driver? (with specific data)
3. What structural change enabled/forced the transformation?
4. If successful, what does the company look like in 3-5 years?

**Must include**:
- Specific data points showing the shift (e.g., "计算类从SoC收入10%→80%")
- Management quotes with dates (e.g., "Greg Smith在Q4电话会中指出...")
- Industry chain context woven in naturally

**If no transformation is happening**: State "公司处于稳定运营模式" and focus on what's changing at the margin.

## 客户结构 (Customer Structure)

**Length**: 1-2 paragraphs + table
**Purpose**: Who pays this company, and is it concentrated?

**Must include**:
- Top 5 customers (or top customer concentration %)
- Customer CAPEX trends if relevant
- Whether customer base is diversifying or concentrating

**Table format**:
```
| 客户 | 营收占比 | 趋势 | 战略意义 |
|------|---------|------|---------|
| 三星 | 12.5% | 稳定 | 内存测试核心客户 |
```

## 负债结构 (Debt Structure)

**Length**: 1 paragraph for clean balance sheets; 2-3 paragraphs for leveraged companies
**Purpose**: Can this company survive a downturn?

**For clean companies** (net cash): One paragraph stating cash position, no debt, done.
**For leveraged companies**: Debt maturity schedule, interest coverage, refinancing risk.

## 财务数据 (Financial Data)

**Length**: Tables + 2-3 paragraphs of commentary
**Purpose**: Show the numbers that support the thesis.

**Must include**:
- 3-year financial comparison table (Revenue, Gross Margin, EBITDA, Net Income, EPS, FCF)
- Management guidance for next period (with date of guidance)
- 2-3 key earnings call quotes with dates and speakers
- Short-seller risk grade embedded as one line

**Table format**:
```
| 指标 | FY2023 | FY2024 | FY2025 | 趋势 |
|------|--------|--------|--------|------|
| 收入 ($M) | 1,662 | 1,311 | 1,482 | 恢复中 |
| 毛利率 | 39.6% | 33.2% | 31.2% | 仍在底部 |
```

## 估值情况 (Valuation)

**Length**: 2-3 paragraphs + tables
**Purpose**: What is this stock worth, and why?

**Must include**:
- Lead with the valuation method most relevant to how market prices this stock
- If applicable: SOTP, per-unit ($/GW, $/MW), comparable transactions
- Peer comparison table (brief, 3-5 peers)
- Clear target price or range with reasoning
- Davis Double Play analysis if applicable
- NAD floor references woven into narrative

**Key pattern from analyst reports**:
> "考虑到过去十年公司的平均PE是29倍，对应EPS $8.34，目标价约$242。" (TER)
> "最保守情况下，公司估值应该是45亿左右。" (CSIQ)

## 技术分析 (Technical Analysis)

**Length**: 1-2 paragraphs, NO TABLES
**Purpose**: What does the chart say?

**Must include**:
- Current chart pattern (from the 8 recognized patterns)
- Key support and resistance levels (2-3 each)
- Trend direction and Wyckoff phase
- Whether technicals confirm or contradict the fundamental thesis

**Pattern from analyst reports**:
> "日线呈现牛旗结构，下方跌破20元可以考虑先出来。" (CSIQ)
> "一个不太规则的杯柄结构，同时周线突破。上方在30元位置是涨幅满足位。" (IREN)

## 风险提示 (Risk Summary)

**Length**: Bullet list, 3-5 items
**Purpose**: What could go wrong?

Each bullet: risk name → severity → what to watch.
No scoring matrices. No probability tables. Brief and actionable.

## 总结 (Conclusion)

**Length**: 1-2 paragraphs
**Purpose**: Tell the reader what to DO.

**MANDATORY fields**:
- Investment verdict (买入/持有/观望)
- Position sizing (X-Y% of portfolio)
- Target price(s) with method
- Stop-loss level with invalidation logic
- Key catalyst (next 90 days)
- Short-seller risk level (one sentence)

**Pattern from analyst reports**:
> "仓位推荐5%到10%。第一个止盈目标45。" (CSIQ)
> "先看100亿市值。" (IREN)
> "目标价300，推荐仓位10-15%。" (DAVE)
