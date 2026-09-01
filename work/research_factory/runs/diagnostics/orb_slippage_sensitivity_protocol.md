# Frozen post-hoc slippage sensitivity protocol

## Status

Frozen on `2026-08-30` after the point estimates and reviewer request were known.

This is a hostile implementation sensitivity, not an execution reconstruction and not confirmatory evidence.

## Universe

Use the exact uncapped, complete-session headline trades for `NQ` and `ES`.

Report large-contract economics and the micro-scale counterfactual separately.

## Cost grid

Retain the declared fixed round-trip charge of `$4`.

Add adverse slippage of `0`, `1`, `2`, or `4` minimum ticks per side.

The minimum tick is `0.25` index points in both mapped markets.

For slippage level `s`, point value `V`, and risk width `W_i`, total cost drag is:

```text
($4 + 2 s × 0.25 × V) / (W_i V)
```

## Outputs

For every market, mapping, period, and slippage level, report trade count, gross mean R, cost drag R, and net mean R.

For each post-baseline period, also report the change in net mean R relative to `2011-2017` under the same slippage level.

## Interpretation

The surcharge is deliberately adverse and symmetric across all trades.

It does not reconstruct bid/ask history, queue position, partial fills, gap-through-stop losses, or state-dependent liquidity. Passing it is robustness to a fixed tick surcharge only.
