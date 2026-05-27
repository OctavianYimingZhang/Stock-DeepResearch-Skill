# Technical Analysis Framework

This reference defines the K-line analysis module. It combines classical
technical-analysis logic with report-ready trade planning. Keep the final output
short and decision-oriented.

## Required Inputs

Use daily, weekly, and monthly OHLCV data or chart screenshots. Record the
chart date. Prefer split-adjusted and dividend-adjusted OHLCV when using historical
prices. The chart date must be visible. If chart data is unavailable, stale, or not adjusted when adjustment
matters, do not invent levels. Ask for data or state that the technical section
is blocked.

## Three-Layer Internal Framework

### Murphy Layer: Trend And Structure

Use:

- monthly trend for primary direction
- weekly trend for intermediate confirmation
- daily trend for execution
- support/resistance from prior highs/lows, gaps, consolidations, moving
  average zones, and high-volume nodes
- measured move for target levels

### Wyckoff Layer: Supply And Demand

Use internally:

- selling climax or capitulation
- automatic rally
- secondary test
- false breakdown/spring
- breakout and retest
- supply expansion after failed breakout

Translate these into normal investor language in the final report:

- capitulation
- rebound
- retest
- breakout
- uptrend
- failed breakout

Do not output Wyckoff jargon tables in the final report.

### Nison Layer: Candle Confirmation

Use candlesticks only at decision points:

- hammer or long lower shadow near support
- bullish engulfing at breakout or support
- bearish engulfing or long upper shadow at resistance
- gap and gap-fill behavior

Candlestick names should not dominate the report. They support price levels.

## Primary Patterns

Recognize these patterns:

1. bull flag breakout
2. W bottom/double bottom breakout
3. inverse head and shoulders
4. false breakdown/spring reversal
5. monthly break above previous high
6. cup and handle
7. descending/falling wedge breakout
8. symmetrical triangle

For each pattern, determine:

- forming, confirmed, failed, or no clear pattern
- breakout level
- volume confirmation
- measured target
- invalidation level

## Volume Rules

- For breakout patterns, volume matters at breakout.
- Breakout volume should be meaningfully above recent average volume.
- Low-volume pullback after breakout can be constructive.
- High-volume rejection after breakout is a warning.
- Do not over-interpret ordinary volume noise outside key levels.

## Final Output Contract

The technical section must include:

```markdown
## Technical Analysis

[One compact paragraph.]

| Level | Price | Reason |
|---|---:|---|
| Support/Resistance | [price] | [reason] |

Trade Plan:
- Entry zone: [price range or observe]
- Stop loss: [price]
- First take-profit: [price]
- Second take-profit: [price]
```

Required content:

- chart data date and adjusted/unadjusted status
- monthly trend
- weekly trend
- daily trend
- primary pattern
- support and resistance
- volume confirmation
- technical/fundamental alignment
- entry, stop, TP1, TP2

If the setup is not actionable:

```text
No clear entry point is available. The condition that would change the view is [price/catalyst].
```

## Optional Sequence-Model Tooling Idea

External OHLCV sequence models can be used as optional future tooling:

- use OHLCV sequence models as a secondary signal
- compare model-implied direction with classical pattern analysis
- never let a model forecast override verified fundamental valuation or risk
  gates

Do not copy external model code into this repository. If a user explicitly asks
to run a model, use it as a separate external dependency and disclose
assumptions.

## Technical Risk Management

Position sizing must link to the stop:

```text
maximum loss = position size x (entry price - stop price) / entry price
```

If the stop is far from entry, reduce position size or wait for a better entry.
Do not recommend a large position when the technical invalidation point creates
excessive downside.

## Trade-Execution Calibration

Reference-caliber reports use the chart to decide what to do with a fundamentally
attractive but volatile stock. Apply this sequence:

1. Identify whether the monthly structure is base-building, breakout,
   overextended, or broken.
2. Use the weekly chart for the real decision level: cup-and-handle neckline,
   W-bottom breakout, prior high, gap zone, or failed breakout.
3. Use the daily chart only for execution timing near the weekly level.
4. If the first target is near a major resistance zone, explicitly state whether
   to trim, hold, or wait for a retest.
5. Position size must shrink when valuation is stretched, short-risk grade is
   elevated, chart is extended, or the stop is far from entry.

For speculative or high-volatility names, the default trade plan should favor
smaller initial size, partial profit-taking at TP1, and adding only after a
confirmed retest or catalyst.
