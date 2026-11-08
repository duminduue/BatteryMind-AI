# Variable-current segmentation sensitivity audit

Date: 2026-11-08

## Purpose

Assess how the exploratory current-plateau detector changes when its current-deviation tolerance is varied. The same four randomized-dataset regular-group packs were processed with tolerances of 0.15 A, 0.30 A, and 0.50 A. The 0.30 A run is the default/reference setting used in the earlier audit.

## Results

Approximate plateau counts:

| Pack | 0.15 A | 0.30 A | 0.50 A |
|---|---:|---:|---:|
| 4.0 | 957 | 821 | 686 |
| 4.1 | 3,946 | 3,739 | 3,173 |
| 5.0 | 1,092 | 951 | 778 |
| 5.1 | 2,949 | 2,790 | 2,270 |
| **Total** | **8,944** | **8,301** | **6,907** |

Duration summaries reported by the script:

| Pack | Tolerance | Median estimated duration (s) | Estimated duration range (s) |
|---|---:|---:|---:|
| 4.0 | 0.15 A | 49.81 | 0.00–102.03 |
| 4.1 | 0.15 A | 50.93 | 0.00–132.19 |
| 5.0 | 0.15 A | 60.27 | 0.00–162.43 |
| 5.1 | 0.15 A | 41.04 | 0.00–137.98 |
| 4.0 | 0.30 A | 60.46 | 0.00–153.35 |
| 4.1 | 0.30 A | 47.47 | 0.00–233.07 |
| 5.0 | 0.30 A | 60.69 | 0.00–141.98 |
| 5.1 | 0.30 A | 41.02 | 0.00–340.99 |
| 4.0 | 0.50 A | 60.81 | 0.00–180.59 |
| 4.1 | 0.50 A | 60.22 | 0.00–344.72 |
| 5.0 | 0.50 A | 80.07 | 0.00–275.70 |
| 5.1 | 0.50 A | 60.26 | 0.00–346.19 |

## Interpretation

The total number of detected plateaus decreases as tolerance increases: 8,944 at 0.15 A, 8,301 at 0.30 A, and 6,907 at 0.50 A. This is consistent with a wider allowed current deviation merging some adjacent measurements into longer detected segments.

The median duration also changes by pack and tolerance. Therefore, detected segment counts and durations are not invariant properties of the dataset; they depend on the chosen segmentation parameter. The 0.30 A setting should not be described as objectively optimal based on these results alone.

Counts within ±5 seconds of 40, 60, and 80 seconds are also tolerance-dependent and should not be treated as proof of commanded mission timing.

## Limitations and next validation

- The detector identifies approximate plateaus from measured current; it does not recover confirmed commanded-load events.
- Results also depend on the script's discharge/mission filters, continuity-gap rule, day boundary handling, and duration estimator.
- Zero-length/very short and unusually long detections remain in the reported range; they require inspection rather than automatic deletion.
- No conclusion about SOH, capacity fade, EOL, or RUL label validity follows from this segmentation audit.
- Further work should inspect representative raw traces across tolerance settings and compare the detector against independently documented protocol or command records if available.

Conclusion: segmentation is measurably tolerance-sensitive. Treat the output as exploratory features pending validation, not ground-truth load-step labels.
