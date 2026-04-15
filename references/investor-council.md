# Investor Council — Multi-Persona Bull/Bear Debate

An optional parallel phase of the `stock-research-report` orchestrator. Runs 5-7 famous-investor personas in parallel, each applying its own checklist. The output is a confidence-weighted **disagreement matrix** that exposes which dimensions of the thesis are controversial.

**Source**: Persona frameworks extracted from `virattt/ai-hedge-fund` (54k⭐ on GitHub). Bull/bear debate structure from `TauricResearch/TradingAgents` (50k⭐).

**When to use**: Activate when the user wants a second opinion on an existing report, when the stock is genuinely controversial, or when the stock-research-report orchestrator is run in "council mode" (explicit user request). Do NOT run by default — it adds ~2x cost to a standard report.

**When to skip**: Routine deep research reports, small/illiquid names without enough public data for per-persona scoring, any pre-revenue company (most personas don't have a framework for it).

---

## The 7 Core Personas

### 1. Warren Buffett — "Wonderful Business at a Fair Price"

**Pillars (each scored 0-10, composite 0-70):**
- `moat`: Pricing power, brand, switching costs, network effects — qualitative + durable
- `consistency`: 10-year ROE, EPS, revenue stability — low variance preferred
- `pricing_power`: Can the company raise prices without losing volume?
- `book_value_growth`: 10-year book value per share CAGR
- `management_quality`: Capital allocation track record (buybacks, dividends, M&A)
- `intrinsic_value`: DCF + margin of safety (price < intrinsic × 0.7)
- `margin_of_safety`: Current price vs estimated fair value

**Bull signal**: moat ≥8 + consistency ≥7 + margin_of_safety ≥30%
**Bear signal**: moat ≤4 OR management quality ≤4 OR negative book value growth

**Voice**: Patient, long-term, quality-over-value. Famous quote: "It's far better to buy a wonderful company at a fair price than a fair company at a wonderful price."

### 2. Charlie Munger — "Circle of Competence + Predictability"

**Pillars:**
- `moat_analysis`: Same as Buffett but stricter on durability
- `management_analysis`: Track record of rational decisions under pressure
- `predictability_analysis`: How accurately can 10-year EPS be forecast? High predictability required
- `valuation_analysis`: Intrinsic value range with conservative assumptions

**Bull signal**: predictability ≥7 AND moat ≥7 AND reasonable valuation
**Bear signal**: Outside circle of competence OR predictability <5

**Voice**: Harsh, skeptical, multidisciplinary. Famous for "invert, always invert" — what would KILL this thesis?

### 3. Michael Burry — "Deep Value + Contrarian"

**Pillars:**
- `deep_value_multiples`: P/TBV, P/NCAV, EV/EBITDA at trough
- `balance_sheet_durability`: Net cash, working capital, maturity wall
- `insider_trades`: Recent insider buying (strong signal) vs selling (red flag)
- `contrarian_sentiment`: Market hates the name but fundamentals don't match
- `catalyst_timing`: What event forces a re-rating?

**Bull signal**: P/TBV <1.2 + net cash + insider buying + bearish consensus
**Bear signal**: Multiple expansion already priced in OR balance sheet leveraged

**Voice**: Contrarian, obsessive about balance sheet, suspicious of narratives. Famous for subprime short.

### 4. Aswath Damodaran — "Intrinsic Value via Disciplined DCF"

**Pillars:**
- `cost_of_equity_capm`: Rf + β × ERP, with country risk premium if applicable
- `growth_and_reinvestment`: Revenue growth × reinvestment rate × ROIC
- `fcff_dcf`: Full Damodaran FCFF-to-firm DCF with explicit / terminal phases
- `relative_valuation_crosscheck`: Fwd PE vs sector median, reconciliation of DCF and multiples

**Bull signal**: DCF > price AND reinvestment efficiency (ROIC > WACC)
**Bear signal**: Negative EVA (ROIC < WACC) OR terminal value > 70% of DCF

**Voice**: Academic, framework-driven, always shows the math. "Narrative is the story, numbers are the test."

### 5. Peter Lynch — "Invest in What You Know + Growth at Reasonable Price"

**Pillars:**
- `pe_to_growth` (PEG): <1.0 = cheap, 1-2 = fair, >2 = expensive
- `earnings_growth_rate`: Preferably 15-30%, "too fast is unsustainable"
- `story_simplicity`: Can the investment thesis be explained in 2 minutes?
- `category_fit`: Stalwart / Slow Grower / Fast Grower / Cyclical / Turnaround / Asset Play
- `balance_sheet_check`: Debt/equity, cash position

**Bull signal**: PEG <1 AND clear story AND growth 15-30%
**Bear signal**: "Diworsification" (unrelated M&A) OR unclear story OR PEG >2

**Voice**: Down-to-earth, story-driven, avoids hot tech. Famous for Fidelity Magellan's 29% CAGR.

### 6. Stanley Druckenmiller — "Macro-Driven Concentration + Asymmetric Bets"

**Pillars:**
- `macro_regime`: Rate environment, liquidity cycle, dollar strength
- `momentum`: Price + earnings trending aligned with macro
- `asymmetric_setup`: Downside bounded, upside uncapped
- `concentration_worthiness`: Conviction level — would you put 30% of book in this?

**Bull signal**: Macro tailwind + earnings acceleration + asymmetric payoff
**Bear signal**: Macro headwind OR symmetric payoff OR crowded trade

**Voice**: Macro-first, high-conviction, willing to concentrate. Famous for 1992 pound short.

### 7. Cathie Wood — "Innovation + Exponential TAM"

**Pillars:**
- `innovation_edge`: Disruptive tech (AI, genomics, robotics, blockchain, EVs)
- `tam_exponential`: Market size growing >30% annually for 5+ years
- `unit_economics_at_scale`: Path to positive contribution margin at N× current scale
- `optionality`: Multiple products/markets expanding from core

**Bull signal**: Disruptive position + large growing TAM + path to profitability
**Bear signal**: Incremental improvement OR shrinking TAM OR no path to profitability

**Voice**: Thematic, long-duration, thesis over multiples. Famous for ARK Innovation Fund.

---

## Council Workflow

### Phase 1: Parallel Dispatch

After the 4 core sub-agents return their content blocks, optionally dispatch N persona agents in parallel (one per persona). Each agent receives the same base facts (revenue, earnings, balance sheet, management commentary) plus the persona-specific pillar checklist.

**Dispatch pattern** (use Agent tool with `subagent_type: "general-purpose"`):

```
You are simulating [PERSONA] analyzing [TICKER]. Apply [PERSONA]'s framework strictly:
- Score each pillar 0-10 with specific evidence
- Assign overall signal: bullish / bearish / neutral
- Confidence: 0-100 (use analyst-style bands: 90-100 exceptional, 70-89 strong, 50-69 moderate, 30-49 weak, 10-29 poor)
- Reasoning: 2-3 sentences in [PERSONA]'s voice, citing at least 2 specific data points
- Output as JSON: {signal, confidence, pillar_scores, reasoning}

Pillars for [PERSONA]: [list from the persona definition above]

Base facts (shared across all personas): [insert base facts package from orchestrator]
```

### Phase 2: Disagreement Matrix

Build a 7-row × 5-column table:

```
| Persona | Signal | Confidence | Top Pillar (bullish) | Top Concern (bearish) |
|---------|--------|-----------|---------------------|----------------------|
| Buffett | Neutral | 55 | Management quality (8/10) | Margin of safety (4/10) |
| Munger | Bearish | 62 | — | Predictability (3/10) — cyclical |
| Burry | Bullish | 78 | Balance sheet (9/10) | — |
| Damodaran | Neutral | 58 | Reinvestment (7/10) | DCF 5% above price, tight |
| Lynch | Bullish | 70 | PEG 0.9 | — |
| Druckenmiller | Neutral | 48 | — | Macro regime uncertain |
| Wood | Bearish | 65 | — | No disruptive edge |
```

### Phase 3: Council Verdict — "What the Disagreement Tells Us"

The VALUABLE output is not "6 out of 7 personas are bullish" — it's **WHERE they disagree and WHY**. Write one paragraph synthesizing:

1. **Unanimous agreement on**: [dimensions where all personas land the same way]
2. **Major disagreement on**: [dimensions where personas split] — this is the crux of the investment question
3. **Crux**: The thesis hinges on [X]. If [X] is true → bullish consensus forms. If [X] is false → bearish consensus forms.

**Example council verdict (illustrative):**

> "The council unanimously agrees on balance sheet strength (Burry +9, Buffett +8, Munger +8) and cyclical recovery path (Lynch +7, Druckenmiller +6). Major disagreement is on **competitive moat durability**: Buffett sees brand and switching costs (+8), but Munger flags technology obsolescence risk as thesis-breaking (-7). **Crux**: If DIOD's internal fab utilization can sustain above 85% through 2027, the Buffett framing is correct and the stock re-rates to $100+. If margin recovery stalls at 33%, Munger's predictability concern kicks in and the stock trades back to $60."

This framing turns a 7-persona parallel dispatch into a sharper thesis than any single persona could produce — the disagreement IS the signal.

---

## Rules

### DO
- Run personas in parallel (one Agent call per persona, max 7 simultaneously)
- Use SAME base facts for all personas (fair comparison)
- Output each persona's score + reasoning + JSON for aggregation
- Produce a disagreement matrix, not just a "X out of 7 bullish" headline
- Extract the CRUX (the one variable the thesis hinges on) in the verdict paragraph

### DON'T
- Do NOT dispatch more than 7 personas — diminishing returns and cost
- Do NOT average persona scores into a single number — that hides the disagreement
- Do NOT use persona names outside their frameworks ("Buffett thinks X" requires actual Buffett pillars)
- Do NOT run council mode for every report — it's an OPTIONAL extension, not the default
- Do NOT skip the Crux sentence — without it, the council is just a list

---

## Integration with stock-research-report

When the user requests "council mode", "second opinion", "multi-persona", or "bull/bear debate":

1. Complete the standard 4-subagent workflow first (fundamental/valuation/technical/risk)
2. Compose the themed narrative report as normal
3. Append a "投资人议会" (Investor Council) section AT THE END of the report, BEFORE 交易计划
4. The council section is 300-500 words: disagreement matrix table + crux verdict paragraph
5. The 交易计划 section may cite the council crux: "本报告采纳 Burry 框架立场 — 反对 Munger 的周期可预测性担忧"

The council does NOT replace the trade plan. It supplements the thesis with dissenting voices.
