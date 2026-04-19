# Voice and Conviction Protocol

The single largest remaining gap between Claude-generated reports and professional analyst reports is **voice** — specifically, whether the writer has planted themselves in the report as an authority with a view. This file codifies that voice.

---

## The "I" Rule (First-Person Discipline)

Professional analyst reports use first-person pronouns at strategic moments: when asserting a forecast, when rounding for legibility, when admitting what they don't know, and when closing with a target.

### Required markers per report

- **"我认为"** / **"我觉得"** / **"我"** / **"我们"** — at least **6 total uses** across the full report
- Placement bias: **业务逻辑 (1-2x)**, **估值情况 (2-3x)**, **交易计划 (1-2x)**. Not in 公司简介, not in financial tables.

### Good examples (lifted from real analyst reports)

```
"而我认为比特币这里会涨到 140000 左右那么 EBITDA 就是 9.43 亿。"  — IREN
"我认为这已经很保守了。"  — CSIQ (parenthetical after a cut-in-half valuation)
"我是想说明白,从这一点上来看,PGY 是被低估了。"  — PGY
"我们不求吃完,只求 [X]。"  — common analyst trader vernacular
"我和我的高管团队对..."  — quoted management, framed by analyst
"这家公司原本以 X 闻名,但在 Y 浪潮兴起之际选择了战略转型..."  — IREN opener
```

### Anti-examples (Claude's default voice to replace)

```
"值得关注的是,该公司..."   → drop entirely, just state the observation
"综合来看,估值区间为..."   → 我们看到 $X,X 倍空间
"报告认为目标价为..."     → 我认为目标价 $X (因 [reason])
"市场对该名的定价存在分歧" → 我与市场的分歧在于 [specific disagreement]
"数据显示..."             → 从 [specific source] 我们看到...
```

---

## Non-Consensus Discipline (Where I Differ from Consensus)

Every report must contain a 1-2 sentence paragraph (**bolded**) titled `我与市场的分歧` or woven inline, placed at the end of 业务逻辑 OR start of 估值情况.

### What it must say

State EXPLICITLY one of:
1. **Missing linkage**: "市场尚未意识到 X 事件会传导到 Y 收入段 (因为 [mechanism])"
2. **Mispricing of probability**: "市场给了 X 场景 30% 权重,我认为应该是 60% 因为 [evidence]"
3. **Wrong multiple**: "市场按 [X 业务] 估值,但 [Y 业务] 即将主导 EBITDA,应按 [Y 业务] 的 [Z 倍] 估值 —— 这是多重扩张的核心"
4. **Catalyst timing misread**: "市场预期 X 在 Q4 发生,数据显示 Q2 就会 tip — 提前 2 个季度定价"
5. **Structural vs cyclical misdiagnosis**: "市场把 X 归因于周期性下滑,但我认为是结构性重估的起点 (因 [evidence])"

### Anti-examples (BANNED)

- "当前股价已 price in FY2028+ 激进产能..." → 这是在叙述市场共识,不是反共识
- "市场对该名存在分歧" → 不具体,没 alpha
- "估值中性,观望" → 没 view,没 report
- 任何可以被 "市场已正确定价" 替换的段落

### Good examples

```
「我与市场的分歧：市场把 IREN 按照矿工估值(EV/EBITDA 5x),
但 2026 年 Prince George 800MW 放量后 AI 云业务 EBITDA 将占 60% —
那时候应该按 EV/EBITDA 15x 估值 (参考 CoreWeave/Applied Digital),
这是 3 倍多重扩张,叠加 EBITDA 本身翻倍,股价至少 250 亿市值,~6 倍空间。」
```

---

## Trader Vernacular (Rough Numbers > Precise Numbers)

Analysts intentionally round for legibility. Claude over-precises.

### Good (lifted from reports)

- "按照 250 看待,整数好计算" — SEI
- "翻倍就可以" — COMM
- "6 倍空间" — IREN (not "约 540-620% 的 upside")
- "直接把 31 亿的股权价值砍到 15 亿" — CSIQ
- "这里做多盈亏比巨大" — general
- "我不求吃完,只求..." — discipline marker

### Bad (Claude's precision tell)

- "EUR 12.10" (2 decimal prices for $3 stocks)
- "约 540.6%—620.4% 的上行空间"
- "2.37 倍 PE 估值的公允区间为..."
- "12 个月概率加权公允价值 $15.23-16.87"

### Rule

For targets, upside, multiples: round to **integer or single decimal** when the absolute value is >$5. If actual price is $12.10, valuation target prose says "$20" or "$25", not "$21.37". Tables can carry precision; prose cannot.

---

## Banned Phrase Inventory (Scan & Remove Before Finalizing)

Run a find-and-replace pass before any output. ALL occurrences of the following must be zero:

### Templated transitions

- 综上所述
- 由此可见
- 换言之
- 综合来看
- 值得关注的是
- 值得注意的是 (note: this is ALSO banned — analysts do not throat-clear with this phrase)
- 读这个表的关键一句话
- 一句话总结
- 业务总结：
- 综合评级
- 核心判断：
- 长话短说
- 核心逻辑是

### Soft-banned: "核心" overuse

**"核心"** as a modifier ("核心驱动力", "核心机会所在", "核心逻辑", "核心产品", "核心竞争壁垒", "核心战略转型") is one of Claude's tell-phrases. Analysts use it sparingly — typically ≤2 times per report.

**Rule**: Max **2 occurrences** of "核心" across the full report. Prefer specific terms instead:
- "核心驱动力" → "最重要的驱动" OR "决定性的驱动"
- "核心机会所在" → "机会在于" OR "这就是 alpha 来源"
- "核心逻辑" → "逻辑是" OR "要点在于"
- "核心产品" → specific product name
- "核心竞争壁垒" → specific moat type (客户锁定/规模/许可证/等)

### Defensive hedges on conviction statements

When asserting a multiple, a target, or a rating, **do NOT follow it with a defensive parenthetical** that apologizes for the assertion. Conviction means taking the number without hedging.

**BANNED parentheticals after conviction statements**:
- "（远非激进）"
- "（相对保守）"
- "（并不夸张）"
- "（符合历史水平）" (when the historical comparison is vague)
- "（与同业相当）" (when the peer comparison isn't shown)
- "（我认为这并不激进）"

**Good alternatives**: State the reasoning inline without apologizing.
- BAD: "我认为给予 15 倍是中性偏保守的假设（远非激进）" 
- GOOD: "我认为给予 15 倍 — 对标 CoreWeave 的 20×,基础设施同业的 18×,我这里留了缓冲" OR "15 倍 — 参照 [X] 的 18×,我更倾向保守"

The difference: the BAD version apologizes for the number; the GOOD version gives the peer benchmark that justifies the number.

### Stacked hedges

- 中性偏负,非高确信多头
- 持有偏积极买入
- 观望 (Hold / Trade-Only)
- 二元期权 (as thesis descriptor — fine as a technical pattern)
- 非对称性极强 (overused)
- 区间 + 中间值 + 多重triangulation closers

### Bureaucratic voice

- "本报告不构成投资建议" (except once, at the very end)
- "本技术分析为基本面分析的补充附录"
- "需要进一步验证" (without specifying what and when)
- "数据充分性说明"
- "风险回报比在当前位置 1:X,不适合 [hedge]" (declarative please)

### English-in-Chinese subsection labels

- (Guidance)
- (Margin Story)
- (Pro Forma)
- (SOTP Summary)
- (Risk Factors)

Use plain Chinese subsection labels. Structural English in Chinese prose is a template tell.

### Step-enumeration in operating leverage

- "Step 1: 收入 × 利润率 = ..."
- "Step 2: 叠加 [X] → ..."
- "Step 3: 运营杠杆 Y% → ..."
- "Step 4: ..."
- "Step 5: ..."

Replace with inline prose: *"390MW → 1700MW = 4.36×, 3200 万季度 EBITDA × 4.36 = 1.36 亿/季度, 全年约 5.5 亿"*

---

## Encouraged Phrase Inventory (Use Naturally)

### First-person conviction

- **我认为...** / **我觉得...**
- **我们看到...**
- **从 [source] 我们知道...**
- **按 [X] 看待,整数好计算**

### Decisiveness

- **翻倍就可以**
- **6 倍空间** / **3-5 倍空间**
- **直接砍到 $X**
- **做多盈亏比巨大**
- **这里 [X] 出来后,就要跑**

### Humility / discipline

- **我不求吃完,只求 [X]**
- **(我认为这已经很保守了)** — parenthetical aside after a cut
- **买在谣言四起时,卖在新闻落地日**
- **一箭双雕** — only when genuinely applicable

### Causal clarity

- **从 [X] 就可以看出来 [Y]** (replace "显示/表明/暗示")
- **[X] 出来后,[Y] 就会兑现**
- **因为 [A],所以我们按 [B] 估值而不是 [C]**

---

## Specific-Date Density Rule

Every major business driver paragraph must contain at least one specific date in **YYYY-MM** or **YYYY-Q#** format.

### Target density
- 公司简介: 0-1 dates
- 业务逻辑: 2-3 dates
- 运营逻辑: 2-3 dates
- 客户与订单: 1-2 dates
- 财务数据: 1-2 dates (guidance date)
- 估值情况: 1-2 dates (re-rating catalyst)
- 技术分析: 0 dates (not applicable)
- 风险提示: 0-1 dates
- 交易计划: 1 date (90-day catalyst)

**Total target: 10+ dated milestones per report.**

### Banned substitutes

- "in coming quarters" / "未来几个月"
- "近期" / "最近" / "短期内"
- "预计 2026 年某个时候"
- "中期内 (2-3 年)" — use a specific year or range

---

## Section-Closing Summary Sentences

Each themed section should end with a one-sentence takeaway that conveys the analyst's view on that section's material. This is NOT "综上所述 [section body rephrased]" — it's a fresh, opinionated conclusion.

### Good examples

- (End of 业务逻辑): **"我认为这不是周期性反弹,是结构性重估的起点。"**
- (End of 运营逻辑): **"运营杠杆兑现时点在 2026 Q4,早于市场的 2027 假设。"**
- (End of 客户与订单): **"单一客户集中度 88% 是显性风险,但我更担心的是他们的采购节奏,而非质量。"**
- (End of 财务数据): **"账上现金只够烧 4 个季度,这个季度的融资公告就是最重要的催化剂。"**

### Bad examples

- "综上所述,业务逻辑支持正面观点。" — 空话,零信息
- "该公司的财务状况整体健康,存在改善空间。" — 没 view
- "一句话总结:估值偏低。" — 没具体数字,没机制

---

## Quick Self-Audit (Pre-Ship Checklist)

Before shipping a report, confirm:

- [ ] 6+ "我"/"我认为"/"我们" uses (count them)
- [ ] 公司简介 opens with narrative tension (not founding date)
- [ ] `我与市场的分歧` paragraph exists, is specific, and is bolded
- [ ] 估值情况 closing line is single-number + upside multiple (not range/triangulation)
- [ ] At least one inline prose arithmetic chain in 运营逻辑 or 估值情况
- [ ] 10+ specific dates (YYYY-MM or YYYY-Q#)
- [ ] 风险提示 is 2-4 items, not 5+
- [ ] 评级 is one word (not stacked)
- [ ] All banned phrases absent (grep the inventory above)
- [ ] Each themed section ends with an opinionated takeaway sentence

If any check fails, the report reads as templated Claude output, not analyst output.
