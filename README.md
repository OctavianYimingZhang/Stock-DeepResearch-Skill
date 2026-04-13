# Stock Research Report — Orchestration Skill

An orchestration skill for Claude Code that produces analyst-style deep research reports by running four specialized analysis skills in parallel and synthesizing results into one cohesive narrative.

## What It Does

Instead of outputting four separate reports (fundamentals → short-seller → technicals → valuation), this skill produces **one unified report** that matches the style of professional equity research analysts.

## Sub-Skills Required

This skill orchestrates these four skills (must be installed):

1. **[Stock-Analysis-Skill](https://github.com/OctavianYimingZhang/Stock-Analysis-Skill)** — Fundamental analysis
2. **[short-seller-risk-analysis](https://github.com/OctavianYimingZhang/short-seller-risk-analysis)** — Forensic risk assessment
3. **[technical-analysis-patterns](https://github.com/OctavianYimingZhang/technical-analysis-patterns)** — Chart pattern recognition
4. **[valuation-calculator](https://github.com/OctavianYimingZhang/valuation-calculator)** — Multi-model valuation

## Usage

```
Use $stock-research-report to analyze [TICKER]
```

Optional parameters:
- Focus areas: "focus on valuation" or "focus on business transformation"
- Bloomberg data: Attach screenshots for higher-precision analysis

## Output Format

Single .docx file with sections:
1. 公司简介
2. 业务运营
3. 行业地位
4. 业务逻辑重构 (core section)
5. 客户结构
6. 负债结构
7. 财务数据
8. 估值情况
9. 技术分析
10. 风险提示
11. 总结 (with verdict, position sizing, targets)

## Key Design Principles

- **Narrative-first**: Reads like one analyst wrote it, not four AI skills
- **Opinionated**: Clear investment conclusions, not hedged probabilities
- **Concise**: 8-12 pages, not 20+
- **Embedded analysis**: Short-seller risk = one line; technicals = 1-2 paragraphs
- **Actionable conclusion**: Position size, target price, stop-loss, catalyst

## License

MIT
