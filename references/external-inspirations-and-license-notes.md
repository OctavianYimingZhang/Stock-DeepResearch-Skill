# External Inspirations And License Notes

This repository borrows workflow ideas from public projects, not code.

## Rule

Do not copy third-party source code, long prompt text, images, model weights, or
datasets into this Skill. Use ideas only at the abstraction level of workflow,
quality gates, role separation, and output contracts.

## Referenced Projects

| Project | Verified license/status | Ideas used |
|---|---|---|
| [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | MIT license in repository | K-line model as optional future technical-analysis aid; no code copied |
| [AI4Finance-Foundation/FinRobot](https://github.com/AI4Finance-Foundation/FinRobot) | Apache-2.0 license in repository | financial-agent workflow, equity research data-to-report structure |
| [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | Apache-2.0 license in repository | analyst/researcher/trader/risk-manager role separation and debate idea |
| [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | README states MIT; GitHub API did not expose a license object during inspection | investor persona framing as optional mental checklist; no code copied |
| [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | Apache-2.0 license in repository | professional finance workflow patterns, DCF/comps/catalyst workflow ideas |
| [tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills) | MIT license in repository | market-regime, institutional-flow, and trading-process quality gates as optional ideas |
| [OctagonAI/skills](https://github.com/OctagonAI/skills) | MIT license in repository | modular SEC/financial/market-data skill taxonomy ideas |
| [Palantir Foundry Ontology documentation](https://www.palantir.com/docs/foundry/ontology/overview/) | Public documentation | ontology workflow inspiration: objects, properties, links, actions, functions, and gates; no code copied |
| [Databricks Lakehouse and Delta Lake documentation](https://docs.databricks.com/) | Public documentation | research lakehouse layering, source snapshot lineage, and data-quality expectation ideas; no code copied |
| [Snowflake architecture documentation](https://docs.snowflake.com/) | Public documentation | metadata pruning, dynamic refresh, and compute/control separation ideas; no code copied |

## Attribution Standard

When the Skill mentions external projects in docs, link to the source
repository. Do not imply endorsement or dependency.

## Dependency Standard

The current Skill has no runtime dependency on these projects. If future work
adds code, scripts, models, datasets, or copied text from any external project:

1. verify the license again at implementation time
2. preserve required notices
3. include source attribution
4. isolate third-party code from original Skill instructions
5. document installation and security implications

## Book And CFA Material

Valuation and technical-analysis methods are described as standard formulas and
method-selection rules. Do not copy protected textbook prose from CFA materials,
John Murphy, Steve Nison, Wyckoff literature, or any other book. If a user asks
for exact textbook language, summarize instead and cite the book title.
