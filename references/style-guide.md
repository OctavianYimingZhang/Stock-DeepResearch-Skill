# Style Guide — Analyst Voice vs Claude Voice

This guide defines the voice, tone, and formatting that separates analyst-quality reports from AI-generated reports.

## Core Principle

**Write as an analyst who has conviction, not as an AI that has information.**

An analyst's report reflects a POINT OF VIEW formed through research. A Claude-generated report reflects COMPREHENSIVE COVERAGE of all possible angles. The difference is clarity of judgment.

---

## Voice & Tone

### DO: Analyst Voice
- "从数据我们看到，半导体测试收入占比一路上升，目前已经突破80%了。"
- "TER 过去主要赚'手机周期的钱'，现在主要赚'AI 芯片复杂度提升的钱'。"
- "目前估值还是比较贵，但这是因为他作为内存行业卖铲子的逻辑。"
- "我认为在这个位置从估值的角度说，100亿市值是非常安全的估值底位。"
- "简单的来说，就是原来公司美国的业务是通过中国的子公司进行运营的。"

### DO NOT: Claude Voice
- "基于多模型估值分析，概率加权公允价值约为$63.50。"
- "本技术分析为基本面分析的补充附录，不构成投资建议。"
- "需要注意的是，上述分析基于当前可获得的公开数据。"
- "综合考虑牛市（25%概率）、基准（50%概率）和熊市（25%概率）情景..."

---

## Structural Anti-Patterns

### Kill These Sections (merge into narrative)
| Claude Pattern | Analyst Alternative |
|---------------|-------------------|
| "第一部分：数据充分性说明" | Embed confidence notes inline where relevant |
| "商业证据表" with claim/source/form columns | Mention key contracts in business narrative |
| "Financial Quality Sub-Components A/B/C/D/E" | One "财务数据" section with key tables |
| "Wyckoff Phase Analysis" formal table | "从技术面看..." in 1-2 paragraphs |
| "Red Flag Inventory" with 20+ scored items | "做空风险评级: A级" in one line |
| "Risk Score Dashboard" with 7 categories | 3-5 bullet risk list |
| "Bloomberg Terminal Data Request" appendix | Note inline: "一致预期数据缺失，仅做情景分析" |
| "Section 8b: Negative Constraints" | Just follow the rules, don't list them |
| "Meta-Question Self-Reflection" | Skip in output (use during analysis, not in report) |

### Kill These Phrases
| Claude Phrase | Analyst Alternative |
|--------------|-------------------|
| "概率加权公允价值" | "合理估值区间" or "目标价" |
| "隐含上行/下行空间" | "涨幅空间" or "下行风险" |
| "估值判断: 合理估值" | "目前估值偏贵/便宜/合理" with reasoning |
| "本报告不构成投资建议" | Only at the very end, one line |
| "待Bloomberg终端数据" | "因数据限制，此处仅做框架性估算" |
| "免责声明：..." (mid-report) | Only at the very end |

---

## Formatting Rules

### Tables
- Use tables for data, not for analysis. Analysis goes in paragraphs.
- Max 6-8 columns. If wider, split into two tables.
- Include YoY change or trend column for time-series data.
- Bold the most important row or cell.

### Numbers
- Use **bold** for key numbers in text: "FY2025收入**$44.7亿** (同比+52%)"
- Use parentheses for year-over-year: "(+52% YoY)" or "(同比+52%)"
- Abbreviate: $M for millions, $B for billions
- Use ~ for approximate: "~$15亿" not "approximately $1.5 billion"

### Quotes
- Format management quotes with date and speaker inline:
  > CEO Vlad Tenev在2026年2月10日Q4电话会中指出："预测市场是公司历史上增长最快的业务"
- Do NOT create separate "Management Signal Extraction" tables in the report

### Section Length
- 公司简介: 100-200 words
- 业务运营: 300-600 words + tables
- 行业地位: 100-300 words
- 业务逻辑重构: 400-800 words (THE longest section)
- 客户结构: 100-300 words + table
- 负债结构: 50-200 words
- 财务数据: 200-400 words + tables
- 估值情况: 300-600 words + tables
- 技术分析: 100-200 words
- 风险提示: 100-200 words
- 总结: 150-300 words

Total: ~2,000-4,000 words = 8-12 pages

---

## Report Quality Checklist

Before delivery, verify:

- [ ] Report tells ONE cohesive story from start to finish
- [ ] Business Logic Transformation is the most compelling section
- [ ] Conclusion includes: verdict, position size, target, stop-loss, catalyst
- [ ] No separate "short-seller risk" section (embedded in one line)
- [ ] No separate "technical analysis appendix" (embedded in 1-2 paragraphs)
- [ ] No "数据充分性说明" section
- [ ] No "概率加权公允价值" language
- [ ] Total length ≤ 12 pages
- [ ] Management quotes have dates and speaker names
- [ ] Tables have bold emphasis on key rows/cells
- [ ] Reader can explain the investment thesis in one sentence after reading
