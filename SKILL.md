---
name: stock-research-report
description: >
  Orchestrates four specialized analysis skills in parallel to produce a single,
  cohesive analyst-style deep research report. Dispatches fundamental analysis,
  short-seller risk assessment, technical analysis, and valuation calculation
  simultaneously, then synthesizes results into one narrative-driven report
  matching the style of professional equity research analysts. Preserves full
  sub-report content and ends with an opinionated trade plan.
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

Produce a single, cohesive deep research report that reads like it was written by **one analyst with conviction** — not four separate skills concatenated. This skill orchestrates `stock-analysis`, `risk-analysis`, `technical-analysis`, and `valuation-calculator` in parallel, then **WEAVES** their full outputs into one narrative-driven document with an opinionated trade plan at the end.

## Core Philosophy (Read This First)

The output must be an **opinionated trade memo**, not a forensic audit. Six principles govern this:

1. **PRESERVE ALL MATERIAL CONTENT** — Every specific data point, named customer, dated management quote, contract number, capacity figure, catalyst date, and valuation input from the four sub-reports **must survive** into the final report. The previous version of this skill "extracted top 3" items and destroyed most content. That is a BUG. The synthesis step is **reorganization**, not **reduction**.

2. **THEMED STRUCTURE, NOT NUMBERED PARTS** — No "第一部分/第二部分/第三部分/第四部分" structure. No visible skill seams. Sub-skill outputs become content *blocks* that get woven into themed sections (业务逻辑 / 运营逻辑 / 客户与订单 / 财务数据 / 估值 / 技术 / 交易计划).

3. **FIRST-PERSON ANALYST VOICE** — Use "我"/"我认为"/"我觉得"/"我们" at least **6 times per report** (mostly in 业务逻辑 / 估值 / 交易计划). Analysts plant themselves in the report; third-person summaries have no alpha. See `references/voice-and-conviction.md` for the full voice rule set.

4. **TRADER DECISIVENESS, NOT ACADEMIC HEDGING** — Take a side and commit. Single-posture ratings (买入 / 观望 / 回避), single-number target with upside multiple (`目标市值 100 亿,~2.5 倍`), declarative sentences. **Banned**: hedged stacks ("中性偏负,非高确信多头"), "on one hand / on the other", multi-method triangulation in the closing line, "概率加权公允价值", "数据充分性说明", mid-report disclaimers.

5. **BOTTOM-UP QUANTIFICATION WHERE POSSIBLE** — For commodity, industrial, and capacity-driven companies, the report must include **unit-volume × price × cost** math and **operating leverage decomposition** (incremental margin walk). Inline prose arithmetic ("390MW → 1700MW = 4.36×, 3200 万 × 4.36 = 1.36 亿/季度, 全年约 5.5 亿") wins over cold `Step 1 / Step 2 / Step 3` structured tables.

6. **ONE NON-CONSENSUS TAKE** — Every report must contain a `我与市场的分歧 (Where I Differ from Consensus)` paragraph (1-2 sentences): what the market is missing or mis-weighting. Reports that could be replaced by "market has priced it correctly" contain no alpha. See `references/voice-and-conviction.md` §Non-Consensus Discipline.

## When to Use

Activate when the user asks for a comprehensive research report, deep dive, or analyst-style analysis of a public company. This skill replaces the pattern of calling four skills sequentially and concatenating outputs.

## Supporting Files

- `references/report-format.md` — Section-by-section depth guidance (themed structure, not numbered parts)
- `references/style-guide.md` — Tone, voice, anti-patterns, and formatting rules
- `references/voice-and-conviction.md` — **NEW** First-person analyst voice rules, banned/encouraged phrase inventory, non-consensus discipline, "我与市场的分歧" protocol (read this before writing)
- `references/commodity-math-template.md` — Bottom-up unit-economics template for mining/energy/industrial names
- `references/trade-plan-template.md` — Required end-of-report trade plan format
- `references/thesis-cot-template.md` — **NEW** Three-layer Data-CoT → Concept-CoT → Thesis-CoT synthesis pattern (lifted from FinRobot, AI4Finance-Foundation)
- `references/debate-loop.md` — **NEW** Bull/bear/risk-manager adversarial resolution pattern (lifted from TauricResearch/TradingAgents v0.2)
- `references/companion-skills.md` — How to invoke 6 complementary Claude Skills from `anthropics/financial-services-plugins` (catalyst-calendar, thesis-tracker, earnings-preview, earnings-analysis, comps-analysis, dcf-model) + 3 newly added MIT skills (macro-regime-overlay, institutional-flow-tracker, pead-screener)
- `references/investor-council.md` — Optional multi-persona bull/bear debate phase (7 investor personas ported from `virattt/ai-hedge-fund`)

---

## COMPANION SKILLS (Optional Extensions)

Beyond the 4 core sub-skills (`stock-analysis`, `risk-analysis`, `technical-analysis`, `valuation-calculator`), this orchestrator can optionally dispatch 6 additional skills from `anthropics/financial-services-plugins` plus 1 multi-persona council pattern from `virattt/ai-hedge-fund`. Read `references/companion-skills.md` for full dispatch guidance and `references/investor-council.md` for the persona framework.

### When to Call Each Companion Skill

| User intent | Skill to invoke | Integration point |
|-------------|----------------|-------------------|
| Strengthen catalyst tracking | `catalyst-calendar` | Feeds into 催化剂 block of the final report |
| Follow up on a prior thesis | `thesis-tracker` | Standalone — produces a thesis-update memo, not a new deep research |
| Pre-earnings positioning | `earnings-preview` | Standalone — runs 1-2 weeks before earnings |
| Post-earnings assessment | `earnings-analysis` | Standalone — runs 0-3 days after earnings |
| Institutional peer comps | `comps-analysis` | Feeds into `valuation-calculator` Phase 4 (peer quartile table) |
| Excel-grade DCF model | `dcf-model` | Feeds into `valuation-calculator` DCF sanity check |
| Multi-persona second opinion | `investor-council` (in-file pattern) | Appended to report BEFORE 交易计划 |
| Bull/bear debate | `investor-council` with bull/bear split | Crux verdict feeds into 交易计划 stance |

### How to Dispatch Companion Skills

**Direct skill invocation** (use the Skill tool):

```
Skill tool with skill: "catalyst-calendar" and args describing ticker + horizon
Skill tool with skill: "thesis-tracker" and args describing prior thesis + new data point
Skill tool with skill: "earnings-preview" and args describing ticker + reporting date
Skill tool with skill: "earnings-analysis" and args describing ticker + reported results
Skill tool with skill: "comps-analysis" and args describing target + peer set
Skill tool with skill: "dcf-model" and args describing ticker + assumptions
```

These skills must be installed at `~/.claude/skills/` (one-time setup — see `references/companion-skills.md` §Installation).

**Council mode dispatch** (N parallel Agent calls):

When the user requests "council mode", "second opinion", "multi-persona", or "bull/bear debate", dispatch the investor council as an OPTIONAL additional parallel phase AFTER Phase 1 completes. Each persona runs as a separate `general-purpose` agent with the persona-specific checklist from `references/investor-council.md`. Output is a disagreement matrix + crux verdict, appended to the report BEFORE 交易计划. See `references/investor-council.md` §Council Workflow for exact dispatch pattern.

### Default Mode vs Extended Mode

- **Default mode** (99% of requests): Run only the 4 core sub-skills. Companion skills stay idle. Produce one deep research report.
- **Extended mode** (explicit user request): Run 4 core sub-skills + 1-2 companion skills inline (e.g., catalyst-calendar for richer events, or investor-council for contentious names). Composition time and cost increase, but output depth increases proportionally.

Do NOT default to extended mode — extra skill dispatches have meaningful cost and only pay off for complex or contentious situations.

---

## WORKFLOW

### Phase 1: Parallel Dispatch

Launch ALL FOUR analysis skills **simultaneously** as parallel agents. Each agent works independently with the same ticker, user-provided context (Bloomberg screenshots, focus areas, etc.), and an explicit instruction to **OUTPUT EVERYTHING THEY FOUND** — do not pre-compress.

Use the Agent tool with `subagent_type: "general-purpose"` for all four. Dispatch as one message with four tool calls.

**Agent 1 — Fundamental Analysis** (stock-analysis skill)
```
Analyze [TICKER] by invoking the stock-analysis skill. Output the FULL analysis — do NOT pre-compress or self-summarize. Required content blocks:

- Core thesis (one paragraph, opinionated)
- Business Logic Transformation (old → new, 2-4 paragraphs with specific data points)
- Operating Logic (capacity ramp, capex cadence, utilization targets, named facilities)
- Named customer list with revenue share and strategic significance
- Contract/backlog walk with delivery cadence (contract-by-contract if disclosed)
- Management quotes from recent 2-3 earnings calls WITH DATES AND SPEAKER NAMES
- 3-year P&L table + forward model with explicit growth drivers in column headers
- Bottom-up revenue bridge for next year (segment × growth rate = incremental)
- Competitive positioning (3-5 named peers, market share, differentiator)
- Macro-to-company transmission (top 3 factors with specific mechanism)
- Forward catalyst calendar with SPECIFIC DATES
- Unresolved items with impact level

Output everything in full prose and tables. I will re-organize — do not omit material content in an attempt to be "concise".
```

**Agent 2 — Short-Seller Risk** (risk-analysis skill)
```
Run the short-seller risk analysis skill on [TICKER] in EMBEDDED MODE (unless 3+ red flags fire, in which case use FULL AUDIT MODE).

Required output:
- Composite grade (A-F) with one-sentence verdict
- Named red flags with evidence (if any) — NOT a scored rubric, prose
- Named green flags with evidence
- Governance observations that belong in the business-logic or debt sections of the final report (e.g., "auditor upgraded Baker Tilly → PwC", "insider selling pattern", "state of incorporation change reflects capital structure optimization")

If EMBEDDED MODE: output as ~200 words of prose that can slot into the financial-quality section. If FULL AUDIT MODE: output full dashboard.

Do not output a "Risk Score Dashboard" table unless full audit mode is triggered.
```

**Agent 3 — Technical Analysis** (technical-analysis skill)
```
Run the technical-analysis skill on [TICKER]. Output:

- Monthly / weekly / daily trend in one line each
- Current primary pattern (from the 8 patterns) with breakout status
- 2-3 key support levels and 2-3 key resistance levels with brief reasoning
- Volume confirmation status at current or recent breakout
- Alignment with fundamental thesis in one sentence (aligned / divergent / neutral)
- **Trade plan: entry zone, stop loss, first take-profit, second take-profit** (CSIQ/UUUU/UAMY format)

Do NOT output a Wyckoff-phase table in the report — translate to plain Chinese (投降/反弹/回测/突破/上升). Do NOT use the "形态识别/突破成交量确认/关键价位/Wyckoff/综合判断" 5-subsection structure — that's for analysis, not for the final report.

Target length when synthesized: 150-200 words + one price-level table.
```

**Agent 4 — Valuation** (valuation-calculator skill)
```
Run the valuation-calculator skill on [TICKER]. CRITICAL RULES:

1. Pick ONE primary method appropriate for the company archetype:
   - Semiconductor cyclical → mid-cycle EPS × 10-year average P/E (TER pattern)
   - Growth foundry / specialty semi → forward EV/EBITDA with multiple-expansion thesis (TSEM pattern)
   - Mining/commodity → lb/ton × commodity price × margin → EBITDA × peer EV/EBITDA (UUUU/UAMY pattern)
   - Pipeline biotech / pre-revenue pharma / E&P reserves → risk-adjusted NPV (rNPV) with stage-specific PoS (see `references/rnpv-calculator.md` in valuation skill)
   - Turnaround → P/FCF or replacement value
   - High-growth SaaS → EV/Revenue with Rule-of-40 check
2. Show every input of the primary method with sources, with MATH DONE INLINE IN PROSE ("2027E EPS $X × 29x = $Y") not just in tables.
3. Other methods are at most a 2-line sanity check, NOT equal citizens.
4. Do NOT produce a "probability-weighted fair value" average across 9 methods.
5. State the catalyst that re-rates the multiple from current to target (earnings beat, contract win, capacity milestone, rate cut) with a SPECIFIC date or quarter.
6. For commodity companies, bottom-up unit math comes BEFORE any multiple work.
7. For multi-segment companies, do SOTP with geographic/political risk discounts where relevant.
8. **FINAL LINE REQUIREMENT**: Your output must end with a single-number target + upside multiple. Format: "目标价 $X (约 Y.Zx,对应 [method + input])。" or "目标市值 $X 亿,~Y 倍空间。" **Banned**: "三法收敛区间", "综合公允价值", "概率加权", any range-only closing line.

Output: primary method derivation with inline arithmetic, bull/base/bear in prose (one sentence each), single-number target, peer comparison table (3-5 peers), explicit multiple re-rating catalyst with date.
```

---

### Phase 2: Content Inventory (NOT Extraction)

After all four agents return, build a **content inventory** — a full list of every material fact, quote, number, date, customer name, competitor, catalyst, and valuation input from the four outputs. Think of this as indexing, not summarizing.

**Inventory checklist** — every item below must be collected from sub-reports into the final report:

**From Fundamental Analysis:**
- [ ] Core thesis sentence (verbatim or tightened, not rewritten)
- [ ] Business logic transformation narrative (full — 2-4 paragraphs)
- [ ] Every named customer with revenue share
- [ ] Every named competitor with comparison point
- [ ] Every dated management quote (speaker + date preserved)
- [ ] Revenue breakdown table (all segments, all years shown)
- [ ] Capacity/facility names with ramp schedules
- [ ] Backlog / contract numbers
- [ ] Every forward catalyst with date
- [ ] Every unresolved item
- [ ] Forward P&L model (all rows)

**From Short-Seller Risk:**
- [ ] Composite grade + one-line verdict
- [ ] Every named red flag with evidence
- [ ] Every named green flag with evidence
- [ ] Governance observations that belong in business / debt sections

**From Technical Analysis:**
- [ ] Monthly / weekly / daily trend assessment
- [ ] Primary pattern name + breakout status
- [ ] All support/resistance levels
- [ ] Volume confirmation status
- [ ] Alignment-with-fundamentals sentence
- [ ] Trade plan numbers (entry, stop, TP1, TP2)

**From Valuation:**
- [ ] Primary method name (verbatim)
- [ ] Every input of the primary method with source
- [ ] Target price number
- [ ] Bull/base/bear scenarios (one sentence each)
- [ ] Peer comparison table
- [ ] Multiple re-rating catalyst

**Anti-truncation rule (CRITICAL):** If any item from the checklist is missing, re-dispatch to the relevant sub-agent and ask for the specific missing item. Do NOT write the final report with gaps. If an item is legitimately unavailable ("customer names not disclosed in 10-K"), document that inline in the relevant section — do NOT silently drop it.

---

### Phase 3: Narrative Composition (Weave, Don't Staple)

Compose the final report using the **themed structure** in `references/report-format.md`. The sub-reports contribute content *blocks* that get woven into themed sections — they do NOT become standalone chapters with their own headers.

**Weaving rules:**

1. **ONE narrative voice throughout.** The report reads as if one analyst with conviction wrote all of it. First-person "我"/"我认为"/"我觉得"/"我们" must appear at least **6 times** across the report — mostly in 业务逻辑, 估值情况, 交易计划.

2. **Story-first structure.** Lead with the business logic transformation — this is what makes the report interesting. Financial tables support the story; they do not replace it.

3. **Narrative-tension opening (公司简介).** Open the report with the *narrative tension* in one sentence — the pivot, the inflection, the mispricing. Corporate genealogy (founding date, HQ, ticker) moves to sentence 3+. **Forbidden opener**: "XYZ 成立于 1912 年,总部位于..." **Required opener**: "这家源自澳洲的比特币矿工,正在把算力卖给 AI 客户" / "从车规 MCU 向 AI 电源转型中的 IDM" / similar.

4. **Inline prose arithmetic.** Valuation and operating leverage math must appear **inside prose sentences** with explicit operators and parenthetical asides:
   - GOOD: *"50 × 0.62 = 31 亿。然后因为现在这个 31 亿是按照 688472 当下市值计算的... 我们保守计算,直接把 31 亿的股权价值砍到 15 亿。(我认为这已经很保守了。)"*
   - BAD: `| 项目 | 计算 | 结果 |` (cold ledger table with no reasoning)
   
   Free-standing valuation tables are allowed ONLY with a prose paragraph that walks through the numbers inline. Operating leverage chains must be **inline sentences**, NOT `Step 1 / Step 2 / Step 3 / Step 4 / Step 5` structured enumerations.

5. **Embed, don't append.** Short-seller findings, technical analysis, and valuation are WOVEN INTO the narrative. They do NOT appear as separate appendices with "第一部分/第二部分" labels.
   - Short-seller risk becomes 1-2 sentences inside 财务数据 (if grade A-B) or a full paragraph (if grade C+).
   - Technical analysis becomes 1-2 paragraphs + one small price-level table inside 技术分析.
   - Valuation becomes 2-3 paragraphs + one peer table inside 估值情况.
   - Governance observations from risk analysis go into 业务逻辑重构 or 负债结构 where they make narrative sense.

6. **Mandatory "我与市场的分歧" (1-2 sentences, bolded).** Placed at the end of 业务逻辑 OR start of 估值情况. States explicitly what the market is missing or mis-weighting. Reports that could be replaced by "市场已正确定价" fail this check and must be revised.

7. **Single-number target in closing line.** The CLOSING LINE of 估值情况 must be one number + one upside multiple: `目前市值 40 亿,我们看到 100 亿,6 倍空间` or `目标价 ¥8,700 (~2.0×)`. Three-method triangulation is allowed in the body but NEVER in the closing sentence. **Banned closers**: `三法收敛区间 ¥7,230-8,700,主推基准 ¥8,700`, `综合 DCF/相对/SOTP 公允价值 $X-$Y`.

8. **Opinionated conclusion with explicit trade plan.** The report MUST end with a concrete trade plan. Use the format in `references/trade-plan-template.md`. Required fields:
   - 评级 (买入/持有/观望/卖出) — **one posture only, no stacked hedges**
   - 建议仓位 (X-Y% of portfolio) — single range, 5 percentage points max width
   - 入场区间 ($X-$Y with reason)
   - 止损位 ($Z with what invalidates thesis)
   - 第一止盈位 ($A with method)
   - 第二止盈位 ($B with method)
   - 90 天内最重要催化剂 (one event with specific date YYYY-MM or YYYY-Q#)
   - 做空风险 (one letter grade + one line)
   
   **Do NOT end with a summary matrix.** Prose only.

9. **Length target: 3,000-5,000 Chinese characters = 10-15 pages.** Do not compress below 3,000 characters — that means you lost content. Do not exceed 5,000 characters — that means you stapled sub-reports without weaving.

10. **Strip skill vocabulary AND templated phrases.** Before finalizing, scan for and remove ALL of:
    - Skill vocabulary: "数据充分性", "value_creating", "Claim Gate", "置信度", "Red Flag Inventory", "Commercial Evidence Table", "Conditional Judgment", "概率加权公允价值", "Meta-Question Self-Reflection", "第一部分/第二部分/第三部分/第四部分" headers, "本报告不构成投资建议" (except once at the very end), "Wyckoff Spring/SOS/LPS" (translate to plain Chinese).
    - **Templated transitions (NEW)**: "综上所述", "由此可见", "换言之", "综合来看", "值得关注的是", "读这个表的关键一句话：", "一句话总结：", "业务总结：", "综合评级", "核心判断：", "长话短说". These are Claude's tells — use plain prose or `总结：` + bullets.
    - **Hedge stacks (NEW)**: "中性偏负,非高确信多头", "持有偏积极买入", "观望 (Hold / Trade-Only)", "二元期权" as thesis descriptor, "非对称性极强" (overused), English-in-parens subsection labels ("Guidance", "Margin Story").

11. **Specific-date density.** Every major business driver paragraph must contain at least **one specific date (YYYY-MM or YYYY-Q#)**. Target: 10+ dated milestones across a report. Vague phrases like "in coming quarters" / "未来几个月" are BANNED.

12. **Risk section discipline.** 风险提示 is 2-4 items MAX in a named list. Each risk must link to an **observable signal to monitor**, not an abstract regulatory/FX/liquidity category. Drop symmetric 4-block Credit/Market/Operational/Regulatory templates — those are compliance output, not analyst output.

13. **Output format**: Default to markdown (.md) for easy review and diff. If the user asks for a Word document OR the task requires a shareable file for stakeholders, generate .docx using the `anthropic-skills:docx` skill as `[TICKER]_深度研究报告.docx`. Respect the user's requested format when specified.

---

## REPORT STRUCTURE (Themed — Not Numbered Parts)

The final report follows the themed structure below. Read `references/report-format.md` for per-section depth guidance. **There are NO "第一部分/第二部分" headers.**

```
[Company Name]（[Ticker]）深度研究报告
[Subtitle: one-line thesis positioning — e.g., "AI 驱动下的业务逻辑重构与 2026 年市场估值展望"]

## 公司简介
[80-150 words. OPEN with narrative tension (pivot, inflection, mispricing) in sentence 1 — NOT with founding date.
- GOOD opener: "这家源自澳洲的比特币矿工正在把算力卖给 AI 客户,一只脚在加密矿机上,另一只脚跨进 AI 算力云。"
- BAD opener: "XYZ 成立于 1912 年,总部位于岐阜县大垣市..."
Founding date, HQ, ticker, float can appear in sentence 3+ or a sidebar.
End with a one-line setup of what the report will argue.]

## 业务逻辑
[THE CORE SECTION — 2-4 paragraphs, 400-800 words.
Old logic → New logic → Why now → Endgame.
Include specific data points, management quotes with dates.
Weave in industry chain context naturally.
TAM + market share framing is MANDATORY for this section (even rough estimates).
First-person "我认为..." should appear at least once here.
This section should make the reader say "I get why this company is interesting RIGHT NOW."
Governance-change observations from risk analysis may appear here if structurally relevant.
**END this section with**: the `我与市场的分歧` mandatory 1-2 sentence paragraph (bolded) — OR place it at the start of 估值情况 if that fits better narratively. Pick ONE placement.]

## 运营逻辑
[2-4 paragraphs + capacity-ramp table, 400-700 words.
Capacity by facility, capex cadence, utilization targets.
Bottom-up unit economics for commodity/industrial names (use commodity-math-template.md).
Operating leverage decomposition: "from Q1 to Q4, revenue +$XM, net income +$YM, incremental margin ~Z%".
This section answers: "HOW does the business logic convert into P&L, and when?"]

## 客户与订单
[1-2 paragraphs + 1-2 tables, 300-500 words.
Named top-5 customers with revenue share and strategic significance.
Contract/backlog walk: $X backlog split by contract, with 2025 vs 2026 contribution.
Customer CAPEX cycle: are key customers in expansion mode?
If customer names are not disclosed, use segment or geography as proxy AND state the limitation.]

## 财务数据
[Tables + 2-3 paragraphs commentary, 400-600 words.
3-year financial comparison: Revenue, Gross Margin, EBITDA, Net Income, EPS, FCF.
Forward model table with explicit growth drivers in column headers.
Management guidance (with date of guidance).
2-3 key earnings call quotes with dates and speakers.
EMBED the short-seller risk grade as one-line: "做空风险评级: [A/B/C/D/F]—[one-line verdict]"
If risk grade C+, expand to a full paragraph with named red flags.]

## 估值情况
[2-3 paragraphs + tables, 400-700 words.
Lead with the ONE primary valuation method (chosen by archetype).
Derivation with every input named and **math done inline in prose**: "2027E EPS $X × 历史平均 P/E 29x = 目标价 $Y (我认为 29x 不激进因为 [reason])".
Parenthetical confidence asides are encouraged: "(我认为这已经很保守了)", "(按 250 亿整数估算,方便计算)", "(我不求吃完,只求 [reason])".
Peer comparison table (3-5 peers, 4-6 columns max).
Bull/base/bear in prose (one sentence each) — NOT a probability-weighted table, NOT a "综合公允价值" average.
Multiple re-rating catalyst: what moves the stock from current to target multiple?
For commodity companies, unit-math appears BEFORE multiple work.

**CLOSING LINE REQUIREMENT**: The final sentence of 估值情况 MUST be single-number + upside multiple format, on its own line (not buried inside a bull/base/bear paragraph):
- GOOD: "目前市值 40 亿,我们看到 100 亿,6 倍空间。" / "目标价 $140 (约 2.5×,对应 2026E EPS $5.6 × 25x)。"
- BAD: "三法收敛 ¥7,230-8,700,主推基准 ¥8,700。" / "DCF/EV-EBITDA/SOTP 综合公允价值区间 $X-$Y。"

**SCENARIO DISCIPLINE (NEW)**: Bull/base/bear scenarios are allowed BUT:
- Each scenario is ONE line max (never a 3-row table with bold headers)
- Scenarios appear in the MIDDLE of 估值情况, NOT at the end
- The final line of 估值情况 is ALWAYS the single-number target (not the bull/base/bear range)
- BAD: 牛市场景 $110亿 / 基准场景 $88亿 / 熊市场景 $65亿 presented as a formatted scenario block
- GOOD: "牛市 $110亿 (假设数据中心订单超预期), 熊市 $65亿 (执行滞后). 基准 $88亿,~4倍空间 — 这是我的目标。"]

## 技术分析
[1-2 paragraphs + one small price-level table, 150-200 words.
Monthly / weekly / daily trend.
Current primary pattern with breakout status.
Key support (2) and resistance (2) levels.
Alignment with fundamental thesis in one sentence.
NO Wyckoff vocabulary — translate to 投降 / 反弹 / 回测 / 突破 / 上升.
Do NOT re-explain the trade plan here — that's the final section.]

## 风险提示
[Bullet list, **2-4 items MAX**, 100-200 words. Fewer is better — only thesis-killers.
Each risk: what it is, **observable signal to monitor** (not abstract regulatory/FX/liquidity category).
Format: "风险：1, [specific thing], 2, [specific thing]。" is fine — analysts write it this short.
No scoring matrix. No probability table. No "Red Flag Inventory".
Do NOT include boilerplate "外汇风险/利率风险/地缘风险" unless they are genuine thesis-killers.]

## 交易计划
[Prose, 200-350 words. This replaces the old "总结" + "综合总结 matrix" ending.
REQUIRED fields, in this exact order:
- 评级: 买入 / 持有 / 观望 / 卖出
- 建议仓位: X-Y% of portfolio
- 入场区间: $X-$Y（理由）
- 止损位: $Z（对应[what invalidates the thesis]）
- 第一止盈位: $A（method, e.g., "基于 2026E EPS × 历史平均 PE"）
- 第二止盈位: $B（method）
- 90 天内最重要催化剂: [single most important event with date]
- 做空风险: [A/B/C] 级，[one line]
- 本报告仅供研究参考，不构成投资建议。（ONE line only, at the very end)]
```

---

## STYLE ENFORCEMENT

Read `references/style-guide.md` for the complete style guide. Key rules:

### DO (Analyst Patterns)
- Write as one analyst with conviction. Take a side.
- Use "我们"/"我认为"/"从数据我们看到" for opinions and observations.
- Reference Bloomberg screenshots naturally when provided.
- Use **bold** for key numbers and conclusions.
- Keep paragraphs to 3-5 sentences max.
- Use specific numbers, not ranges when possible.
- End with a trade plan that has entry / stop / TP1 / TP2 / position size.

### DO NOT (Claude Patterns to Avoid)
- Do NOT start with "数据充分性说明" (embed confidence inline).
- Do NOT use "概率加权公允价值" or average 9 methods to get a number.
- Do NOT create separate "Commercial Evidence Table" sections.
- Do NOT create formal "Wyckoff Phase" tables with SC/AR/ST/Spring/SOS labels in the final report.
- Do NOT create "Red Flag Inventory" tables with scores.
- Do NOT create "Financial Quality Sub-Components A/B/C/D/E" as separate sections.
- Do NOT use "本技术分析为基本面分析的补充附录" or any disclaimer mid-report.
- Do NOT hedge conclusions with "需要进一步验证" without specifying what and when.
- Do NOT use section numbering like "第一部分: ..., 第二部分: ..."
- Do NOT repeat the company name/ticker in every section header.
- Do NOT end with a 4-row evaluation matrix. End with a trade plan in prose.

---

## ANTI-TRUNCATION + VOICE VERIFICATION

Before finalizing the report, run this self-check. A "pass" is either (a) the item is present, OR (b) the item is legitimately unavailable AND the limitation is explicitly stated inline.

### Content checks (truncation prevention)

1. **Customer names** — Did I include every named customer from the fundamental sub-report?
   - **Pass condition (if not disclosed)**: Statement like "客户名称未在 10-K 中披露，使用终端市场作为代理" appears inline in Block C, optionally with Tier-1 or indirect customer context.

2. **Management quotes** — Did every dated, attributed quote from the fundamental sub-report appear in the final report?
   - **Pass condition (if transcripts unavailable)**: "电话会议 transcript 未获取 — 仅使用新闻稿和披露信息" stated inline.

3. **Forward catalysts** — Every dated catalyst from the fundamental sub-report: is it in 业务逻辑 / 运营逻辑 / 交易计划 somewhere?

4. **Valuation inputs** — Every input of the primary valuation method: is it visible in 估值情况?

5. **Trade plan numbers** — Does the final report have explicit entry zone, stop, TP1, TP2, position size?

6. **Technical levels** — Are the 2-3 support and 2-3 resistance levels all in the report?

7. **Green flags** — Did the named green flags from the risk sub-report make it into the final report (embedded in 财务数据 or 业务逻辑)?

8. **Data anomaly flags** — If the source data contains obvious anomalies (identical EPS two years in a row, negative margin percentages, share count discrepancies): is the anomaly flagged inline?
   - **Pass condition**: Anomaly noted in one sentence with "需用户确认数据准确性".

### Voice/conviction checks (analyst-output parity)

9. **First-person voice count** — Does "我"/"我认为"/"我觉得"/"我们" appear at least **6 times** across the report? Count them. If <6, rewrite 业务逻辑 and 估值情况 paragraphs to add conviction markers.

10. **Narrative-tension opener** — Does sentence 1 of 公司简介 start with the pivot/inflection/mispricing? If it starts with founding date, ticker, or HQ location, rewrite.

11. **Where-I-Differ paragraph** — Is there a `我与市场的分歧` paragraph (1-2 sentences, bolded) at the end of 业务逻辑 or start of 估值情况? If missing, the report has no alpha — add it.

12. **Single-number target** — Is the CLOSING LINE of 估值情况 a single number + upside multiple? If it's a range ("区间 ¥X-¥Y") or triangulation ("三法收敛"), rewrite.

13. **Inline arithmetic presence** — Does at least one valuation or operating-leverage calculation appear as inline prose arithmetic ("50 × 0.62 = 31 亿...") rather than a cold ledger table? If all math is in tables, rewrite one chain inline.

14. **Banned-phrase scan** — Run a find on: 综上所述 / 由此可见 / 换言之 / 综合来看 / 值得关注的是 / 读这个表的关键一句话 / 一句话总结 / 业务总结 / 综合评级 / 核心判断 / 长话短说 / 二元期权 / 非对称性极强 / 中性偏负 / 非高确信 / Step 1...Step 5 enumeration. All should be ZERO occurrences.

15. **Specific-date density** — Count specific dates (YYYY-MM or YYYY-Q# format) across the report. Target: **10+ dated milestones**. If fewer than 6, the report is too vague — add dates from sub-reports.

16. **Risk section length** — Is 风险提示 at most 4 items? If 5+, trim to the thesis-killers.

17. **Trade plan single-posture** — Is 评级 a single word (买入 / 持有 / 观望 / 卖出) with no stacked hedges? "中性偏负" / "观望 (Hold / Trade-Only)" / "持有偏积极买入" all FAIL.

If ANY of these fail the pass conditions, the synthesis is broken. Fix it by re-weaving, not by adding a new appendix. Voice checks #9-17 are non-negotiable — reports that fail them read like templated Claude output, not analyst output.

---

## OUTPUT

**Default format: Markdown (.md)** — easy to review, diff, and iterate. The filename should be `[TICKER]_深度研究报告.md`.

**When to switch to .docx**: The user explicitly asks for a Word document, the task requires a shareable stakeholder file, or the orchestrator is being run in production delivery mode. In that case, use the `anthropic-skills:docx` skill with filename `[TICKER]_深度研究报告.docx`.

If the user provides Bloomberg Terminal data (screenshots or text), integrate it directly into the relevant sections rather than listing it in an appendix.

## HANDLING MISSING OR AMBIGUOUS DATA

**Named customers not disclosed** (e.g., DIOD, most mature semiconductor companies, many industrial names): This is a legitimate disclosure pattern — NOT a skill failure. Pass condition: write "未在公开披露中提及具体客户名称 — 使用终端市场/地理作为代理" inline in Block C (客户与订单), and use end-market percentages or geographic split as proxy. Optionally list Tier-1 customers as indirect strategic context (e.g., "ODM 广达/纬创为主要间接客户", "Tier 1 博世/大陆/安波福为主要采购渠道"). The anti-truncation checklist passes for this item as long as the limitation is explicitly stated.

**Identical consecutive-year data points** (e.g., same EPS two years in a row): Flag inline with one sentence: "注意: FY2024 与 FY2025 GAAP EPS 同为 $X.XX — 需用户确认数据准确性，可能是数据源问题或真实平台期". Do not silently use potentially erroneous data as the basis for valuation.

**Missing Bloomberg terminal data** (consensus, peer multiples, ownership, debt pricing): Continue writing all non-blocked sections. Mark blocked sections inline with "因终端数据缺失，此处仅做框架性估算" — do NOT start the report with a "数据充分性说明" table.
