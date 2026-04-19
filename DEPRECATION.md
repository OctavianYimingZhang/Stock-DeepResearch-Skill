# This repository has been archived

This skill has been consolidated into **[equity-research-suite](https://github.com/OctavianYimingZhang/equity-research-suite)** as of **2026-04-19**.

No further updates will be made here. Full commit history is preserved in the monorepo at `skills/stock-research-report/` via `git subtree`.

## Where it lives now

- **Monorepo**: https://github.com/OctavianYimingZhang/equity-research-suite
- **This skill's new path**: [`skills/stock-research-report/`](https://github.com/OctavianYimingZhang/equity-research-suite/tree/main/skills/stock-research-report)
- **Migration guide**: [`docs/UPGRADING.md`](https://github.com/OctavianYimingZhang/equity-research-suite/blob/main/docs/UPGRADING.md)

## Why consolidated

Five related skills now ship together with one `install.sh`, one README, one LICENSE, unified documentation, and sample end-to-end reports. The monorepo also vendors 3 MIT companion skills from `tradermonty/claude-trading-skills` and integrates 6 optional Apache-2.0 companions from `anthropics/financial-services-plugins`.

## Quick migrate

```bash
curl -fsSL https://raw.githubusercontent.com/OctavianYimingZhang/equity-research-suite/main/install.sh | bash -s -- --profile full
```
