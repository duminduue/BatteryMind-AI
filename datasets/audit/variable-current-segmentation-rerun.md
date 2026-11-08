# Variable-current segmentation rerun

Date of local rerun: 2026-11-08

The updated `tools/audit_variable_current_segments.py` was pulled from GitHub commit `8e08fc4` and rerun against the local `battery_alt_dataset.zip` archive using its default settings.

## Observed output

| Pack | Approximate plateaus | Estimated duration range (s) | Median estimated duration (s) | Counts within ±5 s of 40/60/80 s |
|---|---:|---:|---:|---|
| 4.0 | 821 | 0.00–153.35 | 60.46 | 40: 137; 60: 176; 80: 256 |
| 4.1 | 3,739 | 0.00–233.07 | 47.47 | 40: 1,188; 60: 895; 80: 638 |
| 5.0 | 951 | 0.00–141.98 | 60.69 | 40: 147; 60: 188; 80: 319 |
| 5.1 | 2,790 | 0.00–340.99 | 41.02 | 40: 1,014; 60: 631; 80: 444 |

Total: 8,301 approximate detections.

## Interpretation

The rerun produced the same aggregate counts as the earlier run. The code change adds a guard that treats malformed or non-finite current measurements as a segment boundary. Identical aggregate counts do not prove that the guard was exercised; they may simply mean no such values affected these four inspected streams.

The output remains an exploratory segmentation result, not a reconstruction or validation of commanded load steps. Detections depend on the 0.30 A tolerance, the 2-second continuity-gap rule, filtering to regular-discharge mission rows, and the duration estimator. The very short and long detections remain in the output and must not be silently discarded.

## Next validation work

Before using segment duration or current level as model features:
1. Test sensitivity to more than one current tolerance.
2. Inspect representative detections from all duration bands and all four packs, including false-positive-looking cases.
3. Quantify transition alignment and segment stability from raw traces.
4. Compare against the documented protocol and any available experiment command logs, without treating the documentation alone as row-level ground truth.

This audit does not establish SOH labels, capacity fade, EOL labels, or RUL target validity.
