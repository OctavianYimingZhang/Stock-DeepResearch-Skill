---
name: stock-research-report
description: >
  Orchestrates four specialized analysis skills in parallel to produce a single,
  cohesive analyst-style deep research report. Dispatches fundamental analysis,
  short-seller risk assessment, technical analysis, and valuation calculation
  simultaneously, then synthesizes results into one narrative-driven report
  matching the style of professional equity research analysts.
triggers:
  - 深度研究报告
  - 研究报告
  - stock research report
  - deep dive report
  - analyst report
  - 分析报告
---

# Stock Research Report — Orchestration Skill

## Purpose

Produce a single, cohesive deep research report that reads like it was written by one analyst — not four separate skills. This skill orchestrates `stock-analysis`, `risk-analysis`, `technical-analysis`, and `valuation-calculator` in parallel, then synthesizes their outputs into one narrative-driven document.

## When to Use

Activate when the user asks for a comprehensive research report, deep dive, or analyst-style analysis of a public company. This skill replaces the pattern of calling four skills sequentially and concatenating outputs.

## Supporting Files

- `references/report-format.md` — Section-by-section report template with depth guidance
- `references/style-guide.md` — Tone, voice, anti-patterns, and formatting rules

---

## WORKFLOW

### Phase 1: Parallel Dispatch

Launch ALL FOUR analysis skills simultaneously as parallel agents. Each agent works independently with the same ticker and any user-provided data (Bloomberg screenshots, focus areas, etc.).

**Agent 1 — Fundamental Analysis** (stock-analysis skill)
```
Analyze [TICKER] using the stock-analysis skill. Complete all mandatory sections:
- Business Logic Transformation narrative
- Management Signal Extraction (recent 2-3 earnings calls)
- Customer and Supply Chain Deep Dive
- Competitive Positioning matrix
- Macro-to-Company Transmission
- Market Pricing Mechanism Analysis
- Financial Quality sub-components (Revenue, Earnings, Cash Flow, Returns, Variance)
- Forward Catalyst Calendar
- Conditional Judgment with falsification conditions
- Unresolved Items

Output the FULL analysis. I will synthesize it into a narrative report.
```

**Agent 2 — Short-Seller Risk** (risk-analysis skill)
```
Analyze [TICKER] using the short-seller risk analysis skill. Complete:
- Initial screening (financial, management, structure)
- Deep dive modules as triggered
- Positive signal inventory (green flags)
- Composite risk score and letter grade
- Top 3 red flags and top 3 green flags

Output the FULL analysis. I will synthesize it into a narrative report.
```

**Agent 3 — Technical Analysis** (technical-analysis skill)
```
Analyze [TICKER] using the technical analysis skill. Identify:
- Current trend (daily, weekly) and Wyckoff phase
- Primary chart pattern (from the 8 patterns) with breakout status
- 3 key support levels and 3 key resistance levels
- Volume-price alignment assessment
- Technical-fundamental resonance assessment
- Overall technical posture

Output the FULL analysis. I will synthesize it into a narrative report.
```

**Agent 4 — Valuation** (valuation-calculator skill)
```
Calculate comprehensive valuation for [TICKER] using the valuation-calculator skill. Run:
- Market Pricing Mechanism pre-check
- All applicable relative valuation multiples
- DCF (FCFF and/or FCFE)
- SOTP if multi-segment company
- NAD Price Decomposition (floor analysis)
- Davis Double Play analysis
- Comparable company analysis
- Scenario analysis (bull/base/bear)
- Bottom-up capacity-to-EBITDA projection if applicable

Output the FULL analysis. I will synthesize it into a narrative report.
```

### Phase 2: Synthesis — Extract Key Elements

After all four agents complete, extract and organize the key elements:

**From Fundamental Analysis:**
- Company description (1-2 sentences)
- Business Logic Transformation narrative (the CORE story)
- Revenue breakdown table
- Management quotes (top 3-5 most impactful, with dates)
- Customer concentration data
- Competitive positioning summary
- Macro-to-company transmission (top 3 factors)
- Forward catalyst calendar (top 5 events)
- Conditional judgment (core thesis + if-then-else)
- Unresolved items (top 3)

**From Short-Seller Risk:**
- Composite score and letter grade
- One-sentence verdict
- Top 3 green flags
- Top 3 red flags (if any material ones exist)
- Decision: if grade A-B, embed as 1-2 sentences in risk section; if grade C+, expand to 1-2 paragraphs

**From Technical Analysis:**
- Technical posture (one word: bullish/neutral/bearish)
- Primary pattern name and status
- 3 key price levels (most important support, resistance, inflection)
- Wyckoff phase (one word)
- Technical-fundamental resonance (aligned/divergent)

**From Valuation:**
- Best single fair value estimate (the method most aligned with how market prices the stock)
- Fair value range (low to high across methods)
- Scenario analysis summary (bull/base/bear prices with probabilities)
- NAD floor summary (which floor is most vulnerable, which could thicken)
- One key valuation insight (what's the most interesting finding)

### Phase 3: Narrative Composition

Compose the final report using the format in `references/report-format.md` and the style rules in `references/style-guide.md`.

**Critical Composition Rules:**

1. **ONE narrative voice throughout.** The report should read as if written by one analyst who deeply understands this company. No section should feel like it was written by a different skill.

2. **Story-first structure.** Lead with the business logic transformation — this is what makes the report interesting. Financial tables support the story, they don't replace it.

3. **Embed, don't append.** Short-seller findings, technical analysis, and valuation are WOVEN INTO the narrative. They do NOT appear as separate appendices.

4. **Opinionated conclusion.** The report MUST end with a clear verdict: position sizing, target price(s), stop-loss, and the single most important catalyst to watch in the next 90 days.

5. **8-12 pages maximum.** Ruthlessly cut anything that doesn't directly serve the investment thesis. If a section doesn't change the reader's mind about buying or selling, remove it.

6. **Generate .docx file.** Use the docx skill to output the final report as a Word document.

---

## REPORT STRUCTURE (Mandatory Sections)

The final report MUST follow this structure. Read `references/report-format.md` for section-by-section depth guidance.

```
[Company Name]（[Ticker]）深度研究报告
[Subtitle: one-line thesis positioning]

## 公司简介
[1-2 paragraphs. What it does, when founded, key stats. Context-setting only.]

## 业务运营
[2-4 paragraphs. Segments, revenue breakdown, products.
Embed revenue structure table here.]

## 行业地位
[1-2 paragraphs. Competitive landscape, market position, third-party validation.]

## 业务逻辑重构
[THE CORE SECTION — 2-4 paragraphs.
Old logic → New logic → Why now → Endgame.
Include specific data points, management quotes with dates.
Weave in industry chain context naturally.
This section should make the reader say "I get why this company is interesting RIGHT NOW."]

## 客户结构
[1-2 paragraphs + table. Top customers, concentration, trends.]

## 负债结构
[1 paragraph + table. Brief for clean balance sheets.
For turnarounds or leveraged companies, expand to 2-3 paragraphs.]

## 财务数据
[Tables + commentary.
3-year financial comparison: revenue, margins, EPS, FCF.
Management guidance.
Key earnings call quotes (2-3 most important, with dates/speakers).
Embed the short-seller risk grade here as one line:
"做空风险评级: [A/B/C/D/F]（[score]/100）— [one-line verdict]"]

## 估值情况
[2-3 paragraphs + tables.
Lead with the valuation method most relevant to how market prices this stock.
Include creative valuation (SOTP, per-unit, comparable transactions) if applicable.
Peer comparison table.
Clear target price or fair value range.
Embed Davis Double Play analysis if applicable.
Reference NAD floors naturally: "当前股价中，约$X来自核心业务估值，$Y来自增长溢价..."]

## 技术分析
[1-2 paragraphs. NO tables.
Current pattern, key levels, trend assessment.
Technical-fundamental resonance.
Example: "从技术面看，股价自$48低点形成W底结构，颈线$65已突破放量确认，
目标位$82已达成。目前处于Wyckoff markup阶段，Bull Flag正在形成中，
若突破$85-88区域，上方打开至$100的空间。"]

## 风险提示
[Bullet list, 3-5 items. Brief and actionable.
Each risk: what it is, how severe, what to watch for.]

## 总结
[1-2 paragraphs. Clear investment verdict.
MUST include:
- 投资评级: 买入/持有/观望/卖出
- 仓位建议: X-Y% of portfolio
- 目标价: $X (基于[method]) / 第二目标: $Y
- 止损位: $Z (对应[what invalidates the thesis])
- 关键催化剂: [next 90 days, single most important event]
- 做空风险: [A/B/C] 级，[one-line]

免责声明: 本报告仅供研究参考，不构成投资建议。]
```

---

## STYLE ENFORCEMENT

Read `references/style-guide.md` for the complete style guide. Key rules:

### DO (Analyst Patterns)
- Write as one analyst with a clear point of view
- Use "我们" (we) or "我认为" (I believe) for opinions
- Use "从数据我们看到" (from the data we see) for observations
- Reference Bloomberg screenshots naturally when provided
- Use bold for key numbers and conclusions
- Keep paragraphs to 3-5 sentences max
- Use specific numbers, not ranges when possible

### DO NOT (Claude Patterns to Avoid)
- Do NOT start with "数据充分性说明" (embed confidence inline)
- Do NOT use "概率加权公允价值" (use "合理估值区间" or "目标价")
- Do NOT create separate "Commercial Evidence Table" sections
- Do NOT create formal Wyckoff Phase tables
- Do NOT create "Red Flag Inventory" tables with scores
- Do NOT create "Financial Quality Sub-Components A/B/C/D/E" as separate sections
- Do NOT use "本技术分析为基本面分析的补充附录" disclaimers mid-report
- Do NOT hedge conclusions with "需要进一步验证" without specifying what and when
- Do NOT use section numbering like "第一部分: ..., 第二部分: ..."
- Do NOT repeat the company name/ticker in every section header

---

## OUTPUT

Generate the final report as a .docx file using the docx skill. The filename should be:
`[TICKER]_深度研究报告.docx`

If the user provides Bloomberg Terminal data (screenshots or text), integrate it directly into the relevant sections rather than listing it in an appendix.
