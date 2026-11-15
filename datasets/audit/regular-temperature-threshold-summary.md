# Regular-Pack Battery Temperature Threshold Summary

## Scope

A local threshold-sensitivity audit was run for all 15 CSV files in `regular_alt_batteries`. The analysis filtered to regular-discharge records and used the same exploratory battery-temperature thresholds (85, 90 and 95 °C) and episode gap rule (>2.5 seconds).

The consolidated local output was `outputs/regular_group_temperature_summary.csv`.

## Consolidated results

The summary contains 15 unique packs and 45 rows (15 packs × 3 thresholds).

| Temperature threshold | Total detected episodes across 15 packs |
|---:|---:|
| 85 °C | 815 |
| 90 °C | 648 |
| 95 °C | 367 |

## Packs with the highest detected episode counts

| Threshold | Pack | Qualifying records | Detected episodes |
|---:|---:|---:|---:|
| 85 °C | 5.2 | 5,250 | 190 |
| 85 °C | 0.0 | 15,861 | 160 |
| 85 °C | 1.0 | 10,313 | 138 |
| 85 °C | 5.0 | 19,123 | 121 |
| 85 °C | 4.0 | 14,760 | 100 |
| 90 °C | 0.0 | 8,185 | 164 |
| 90 °C | 1.0 | 3,436 | 135 |
| 90 °C | 5.0 | 12,908 | 123 |
| 90 °C | 4.0 | 9,624 | 100 |
| 90 °C | 3.0 | 1,320 | 66 |
| 95 °C | 5.0 | 6,769 | 121 |
| 95 °C | 0.0 | 1,550 | 108 |
| 95 °C | 4.0 | 4,674 | 98 |
| 95 °C | 2.0 | 2,353 | 27 |
| 95 °C | 1.0 | 36 | 11 |

## Preliminary observations

- The total number of detected episodes decreases as the screening threshold increases: 815 at 85 °C, 648 at 90 °C, and 367 at 95 °C.
- The pack ranking changes with threshold. Pack 5.2 has the most detected episodes at 85 °C, while pack 0.0 leads at 90 °C and pack 5.0 leads at 95 °C.
- Episode counts are threshold- and segmentation-dependent. A qualifying episode is a group of threshold-exceeding records separated from the next group by a time gap greater than 2.5 seconds.
- These are pack-specific observations. Episodes from the same pack are not independent battery-level experimental replicates.

## Limitations and interpretation

The 85, 90 and 95 °C values are exploratory screening thresholds, not validated safety limits, failure labels or thermal-runaway criteria. A detected episode does not by itself establish a fault, degradation mechanism, or causal relationship with current, voltage, age or loading protocol.

The summary is an aggregate of the locally generated per-pack outputs. It does not provide a matched comparison adjusted for operating conditions, pack history, ambient temperature, or measurement uncertainty. Pack rankings must not be interpreted as health or safety rankings.

No measurements were removed, altered or imputed in this screening analysis. Further interpretation requires trace-level contextual review, validation of sensor behaviour and operating conditions, and confirmation of the experimental protocol.

## Reproducibility note

The aggregate was generated locally from the 15 per-pack threshold-sensitivity CSV outputs. The consolidated CSV is not included in this commit; raw archives and generated analysis outputs remain local. The reported values are transcribed from the user's terminal output and should be regenerated from the source outputs before publication or formal reporting.
