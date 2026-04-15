# Trade Plan Template — Required Report Ending

Every stock research report MUST end with a concrete trade plan in this exact format. This replaces the old "总结" section and the "综合总结 matrix" ending.

## The Template

```
## 交易计划

评级: [买入 / 持有 / 观望 / 卖出]
建议仓位: [X-Y]% of portfolio
  （reasoning: 一句话解释为什么是这个仓位大小 —— 例如 "因为波动率高但确定性强，中等仓位匹配风险回报"）
  （MANDATORY loss-budget math:
    最大持仓 [X]% × 止损距离 [Y]% = 组合最大亏损 [X × Y / 100]%
    例如: 4% 仓位 × 18% 止损距离（$83→$68）= 0.72% 组合亏损
    确认该亏损额在投资者可接受范围内）

入场区间: $[X] - $[Y]
  （理由: 一句话解释为什么在这个区间入场 —— 例如 "基于 W 底颈线回踩，技术面 + 基本面支撑重合"）

止损位: $[Z]
  （对应 [what invalidates the thesis] —— 例如 "若跌破 $Z，W 底结构失效，业务逻辑也需要重新验证"）

第一止盈位: $[A]
  （method —— 例如 "基于 2026E EPS × 历史平均 PE"）
第二止盈位: $[B]
  （method —— 例如 "基于 2027E EBITDA × 行业中位数 EV/EBITDA"）

90 天内最重要催化剂: [single most important event with date]
  （例如: "2026 年 2 月 Q4 电话会议 —— 确认毛利率回升路径和 2026 年 guidance"）

做空风险: [A / B / C / D / F] 级 —— [one line verdict]
  （例如: "A 级 —— 清洁资产负债表、简单 US 公司结构、审计师升级至 Big 4，无重大红旗"）

---
本报告仅供研究参考，不构成投资建议。
```

## Real Analyst Examples (Study These)

**CSIQ-style (recovery name):**
```
评级: 买入
建议仓位: 5% - 10%
入场区间: $16 - $18
  （因 W 底颈线 $17 回踩，财报反弹确认形态）
止损位: $14
  （跌破则 W 底失效，公司重组故事需要重新评估）
第一止盈位: $45
第二止盈位: $55
90 天内最重要催化剂: Q1 2026 财报 —— 确认北美业务重组进度和 2026 年 CapEx 指引
做空风险: B 级 —— 资产负债表仍有杠杆，但无重大会计红旗
```

**IREN-style (thesis name):**
```
评级: 买入
建议仓位: 10% - 15%
入场区间: $9 - $11
止损位: $8.6
  （跌破则 AI cloud 转型叙事受挫，回归比特币矿工估值框架）
第一止盈位: $15
  （对应 100 亿市值）
第二止盈位: $25
90 天内最重要催化剂: 下一份 Q 报 —— AI 云收入占比是否突破 30%
做空风险: B 级 —— 行业叙事风险，但无欺诈迹象
```

**DAVE-style (growth name):**
```
评级: 买入
建议仓位: 10% - 15%
入场区间: $220 - $250
止损位: $200
第一止盈位: $300
第二止盈位: $400
90 天内最重要催化剂: Q4 财报，重点看 ARPU 和 CashAI 采用率
做空风险: C 级 —— 估值高且消费信贷周期风险存在
```

## Rules

### DO

- Use specific dollar numbers. "大约 20 元附近" is acceptable but specific numbers preferred.
- Give a position sizing range (5-10%, 10-15%, etc.) — not a single number.
- State WHY at each level (why this entry, why this stop, why this target, what method the target came from).
- Pick ONE primary catalyst within 90 days. If nothing in 90 days, state "无临近催化剂" and expand stop-loss tolerance.
- Keep the whole section under 350 words.

### DON'T

- Do NOT use "概率加权公允价值" anywhere.
- Do NOT provide "目标价: $72-100 (合理区间)" without committing to ONE primary target.
- Do NOT skip stop-loss. Every trade plan must have a stop.
- Do NOT list 5 catalysts. Pick ONE.
- Do NOT add a multi-row disclaimer. ONE line only.
- Do NOT end with a matrix. End with prose, even if bulleted.

## Integration Check

Before finalizing, verify:

- [ ] All 8 required fields (评级, 仓位, 入场, 止损, 止盈1, 止盈2, 催化剂, 做空风险) are present
- [ ] Stop-loss has a thesis-invalidation reason attached
- [ ] Targets have methods attached
- [ ] Catalyst has a specific date
- [ ] Position size has a reasoning sentence
- [ ] Total trade plan section is 200-350 words
- [ ] No tables in this section (prose + bulleted fields only)
