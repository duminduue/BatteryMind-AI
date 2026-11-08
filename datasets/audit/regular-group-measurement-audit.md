# Regular Battery Group: Measurement Audit and Variable-Current Validation

**Repository:** BatteryMind-AI  
**Dataset:** NASA randomized and recommissioned lithium-ion battery dataset  
**Audit status:** Exploratory measurement audit; not a validation of SOH/RUL labels.

## Scope

This note records the local measurements and command outputs supplied during the audit of all 15 CSV files in `regular_alt_batteries`. Daily summaries use regular-discharge records only:

- `mode` equal to `-1` or `-1.0` (the categorical representation varies by file);
- `mission_type=1.0`;
- non-empty `current_load`.

The values below are measured daily median currents, not nominal commanded currents. The number of represented discharge dates is not necessarily the total number of calendar days on which the pack was active.

## Regular-pack daily summary

| Pack | CSV | Represented discharge dates | Date range | Daily median current range (A) | Documented nominal group |
|---|---|---:|---|---:|---|
| 0.0 | battery00.csv | 14 | 2022-07-22 to 2022-08-09 | 16.306–16.918 | Constant, approx. 16 A |
| 1.0 | battery10.csv | 11 | 2022-07-22 to 2022-08-06 | 16.256–16.788 | Constant, approx. 16 A |
| 3.1 | battery31.csv | 49 | 2022-08-01 to 2022-10-12 | 12.678–13.759 | Constant, approx. 12.9 A |
| 2.2 | battery22.csv | 40 | 2022-08-06 to 2022-10-06 | 12.987–13.812 | Constant, approx. 12.9 A |
| 2.3 | battery23.csv | 19 | 2022-10-08 to 2022-10-26 | 14.845–15.169 | Constant, approx. 14.3 A |
| 5.2 | battery52.csv | 22 | 2022-09-15 to 2022-10-16 | 14.545–15.168 | Constant, approx. 14.3 A |
| 0.1 | battery01.csv | 70 | 2022-08-12 to 2022-11-13 | 9.290–9.795 | Constant, approx. 9.30 A |
| 1.1 | battery11.csv | 71 | 2022-08-09 to 2022-11-11 | 9.257–9.877 | Constant, approx. 9.30 A |
| 2.0 | battery20.csv | 3 | 2022-07-22 to 2022-07-24 | 19.516–19.608 | Constant, approx. 19.0 A |
| 3.0 | battery30.csv | 7 | 2022-07-22 to 2022-07-31 | 19.466–19.894 | Constant, approx. 19.0 A |
| 2.1 | battery21.csv | 6 | 2022-07-27 to 2022-08-04 | 19.523–19.914 | Constant, approx. 19.0 A |
| 4.1 | battery41.csv | 43 | 2022-08-06 to 2022-10-09 | 13.987–16.248 | Variable, approx. 14.3 A average |
| 5.1 | battery51.csv | 26 | 2022-08-07 to 2022-09-04 | 13.876–15.439 | Variable, approx. 14.3 A average |
| 4.0 | battery40.csv | 9 | 2022-07-22 to 2022-08-03 | 17.172–17.930 | Variable, approx. 17.0 A average |
| 5.0 | battery50.csv | 10 | 2022-07-22 to 2022-08-04 | 17.320–17.914 | Variable, approx. 17.0 A average |

### Interpretation and data-quality notes

- The daily medians broadly occupy the documented nominal current groups, but measured values are not identical to nominal protocol values. Do not substitute one for the other.
- The variable-current packs require segment-level analysis; daily medians alone cannot verify the documented 40/60/80-second load durations.
- Pack 2.1 (`battery21.csv`) uses integer-like mode strings (`-1`, `0`, `1`) rather than decimal-form strings in several other files. A filter that checks only `"-1.0"` silently misses its discharge rows. Parsing categorical values robustly is required.
- Some packs have only a few represented discharge dates in the supplied filtered output. This is not evidence that their complete life consists only of those dates.
- These summaries do not establish capacity fade, SOH ground truth, failure/EOL labels, or RUL target validity.

## Exploratory variable-current segmentation

The local first-pass segmentation tool was run on variable-current regular packs 4.0, 4.1, 5.0 and 5.1 using a current tolerance of 0.30 A. It detected 8,301 approximate plateaus.

| Pack | Detected plateaus | <5 s | 5–20 s | 20–35 s | 35–45 s | 45–55 s | 55–65 s | 65–75 s | 75–85 s | >85 s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4.0 | 821 | 149 | 8 | 21 | 137 | 12 | 176 | 13 | 256 | 49 |
| 4.1 | 3,739 | 493 | 98 | 79 | 1,188 | 52 | 895 | 36 | 638 | 260 |
| 5.0 | 951 | 128 | 21 | 28 | 147 | 23 | 188 | 32 | 319 | 65 |
| 5.1 | 2,790 | 308 | 64 | 54 | 1,014 | 41 | 631 | 27 | 444 | 207 |

The concentrations near 40, 60 and 80 seconds are broadly compatible with the durations described in the dataset documentation. However, the detections are algorithm-dependent candidates, not verified commanded-load segments. Short and long detections also occur. The counts depend on tolerance, gap handling, filtering and duration estimation.

### Segmentation tolerance sensitivity check

The same first-pass segmentation script was rerun at three current tolerances (0.15 A, 0.30 A and 0.50 A) for packs 4.0, 4.1, 5.0 and 5.1. The script defines a candidate plateau relative to its first measured current sample, and also splits at a time gap greater than 2 seconds or a change of recorded date.

| Pack | Tolerance 0.15 A: detections | Tolerance 0.30 A: detections | Tolerance 0.50 A: detections |
|---|---:|---:|---:|
| 4.0 | 957 | 821 | 686 |
| 4.1 | 3,946 | 3,739 | 3,173 |
| 5.0 | 1,092 | 951 | 778 |
| 5.1 | 2,949 | 2,790 | 2,270 |

The approximate-duration summaries also changed with tolerance:

| Pack | Tolerance | Median estimated duration (s) | Counts within ±5 s of 40 s | Counts within ±5 s of 60 s | Counts within ±5 s of 80 s |
|---|---:|---:|---:|---:|---:|
| 4.0 | 0.15 A | 49.81 | 183 | 177 | 269 |
| 4.0 | 0.30 A | 60.46 | 137 | 176 | 256 |
| 4.0 | 0.50 A | 60.81 | 47 | 146 | 164 |
| 4.1 | 0.15 A | 50.93 | 1,257 | 1,044 | 718 |
| 4.1 | 0.30 A | 47.47 | 1,188 | 895 | 638 |
| 4.1 | 0.50 A | 60.22 | 748 | 742 | 650 |
| 5.0 | 0.15 A | 60.27 | 191 | 214 | 341 |
| 5.0 | 0.30 A | 60.69 | 147 | 188 | 319 |
| 5.0 | 0.50 A | 80.07 | 40 | 157 | 194 |
| 5.1 | 0.15 A | 41.04 | 1,050 | 713 | 514 |
| 5.1 | 0.30 A | 41.02 | 1,014 | 631 | 444 |
| 5.1 | 0.50 A | 60.26 | 567 | 502 | 462 |

The number of detected candidates decreases as tolerance increases for all four packs, while the duration distribution and counts near the documented 40/60/80-second values also shift. This confirms that the present segmentation output is materially parameter-sensitive. A tighter tolerance fragments some traces into more candidates; a wider tolerance can merge current levels that should be treated as separate regimes. The median duration and near-target counts therefore cannot be interpreted independently of the tolerance setting.

The ±5-second counts include only detections whose estimated duration is within 5 seconds of 40, 60 or 80 seconds; they do not sum to the total detections. Very short and very long detections remain in the output. The reported overall duration ranges also include near-zero candidates and unusually long candidates, which require separate review rather than automatic exclusion.

No tolerance is selected as scientifically correct at this stage. The 0.30 A result is retained as the initial exploratory reference because it was the first-pass setting, not because it has been validated. Further refinement should compare candidate boundaries with raw traces and protocol records, quantify sensitivity to the time-gap rule, and use systematic rather than first-match spot checks.

### Refined segmentation boundary-reason audit

The refined segmentation run was executed locally on the randomized NASA archive for packs 4.0, 4.1, 5.0 and 5.1 using a current tolerance of 0.30 A and a maximum adjacent-sample time gap of 2.0 s. The resulting CSV contained 8,301 candidate segments.

| Pack | Total candidate segments | Ended by current change beyond tolerance | Ended by mission or mode change |
|---|---:|---:|---:|
| 4.0 | 821 | 685 | 136 |
| 4.1 | 3,739 | 3,273 | 466 |
| 5.0 | 951 | 827 | 124 |
| 5.1 | 2,790 | 2,498 | 292 |
| **Total** | **8,301** | **7,283** | **1,018** |

For this run, all reported segment endings were attributed to either a measured-current change beyond the configured tolerance or a mission/mode change. No time-gap, date-change, missing-current/time, non-finite-current, or end-of-file boundary was reported in the displayed boundary-reason counts.

These are algorithmic boundary labels, not verified physical load-command transitions. In particular, the large number of current-change boundaries may reflect genuine load-level changes, measurement variation, or segmentation sensitivity. The result alone cannot distinguish these explanations or establish the intended 40/60/80-second schedule.

### Selected trace checks

**Pack 5.0, 2022-07-22:** A detected interval from 7671.360 to 7752.344 s was estimated at 81.932 s. The wider raw trace and 20-second bins show a gradual rise in median current from approximately 23.79 A to 24.23 A across the combined 7668–7952 s interval. Three consecutive detections in this region (81.932, 94.273 and 105.211 s) do not correspond to three clearly separated, stable current plateaus. This is an example of over-segmentation/merging behaviour that requires algorithm refinement.

**Pack 4.0, 2022-07-22:** A detected interval from 10151.363 to 10230.688 s was estimated at 80.279 s. The raw trace and 20-second-bin medians show a step from approximately 17.64 A to 18.31 A at the interval start and a step down to approximately 16.69 A near its end. This selected example is consistent with a distinct, approximately stable measured-current plateau.

**Pack 4.1, 2022-08-06:** A detected interval from 12915.820 to 12955.701 s was estimated at about 40 s. The 20-second-bin medians show approximately 14.30 A, followed by 13.98 A, then 15.09 A in subsequent bins. Therefore, this detected interval should not be accepted as a validated single plateau without checking exact boundaries and the segmentation logic.

Manual examples selected from the 35–45 s, 55–65 s and 75–85 s duration bands in all four packs had sample counts and current ranges broadly consistent with stable measured-current intervals in those selected cases. These are selection-biased spot checks; they do not validate all detections or prove the commanded-load schedule.

### Required refinement before using segment features

1. Validate time ordering, sampling intervals, missing samples and discharge-session boundaries.
2. Detect transitions using explicit change-point logic or a documented tolerance rule, and prevent candidate plateaus from spanning clear internal current steps.
3. Quantify sensitivity to current tolerance and allowed time gaps.
4. Select representative examples across packs, dates, duration bands and current amplitudes, not only the first matching detections.
5. Compare detected measured-current intervals with experimental command/protocol records where available.
6. Preserve raw values and all rejected/ambiguous candidates with reasons; do not silently discard them.

## Current conclusion

The regular-group audit now includes a daily-summary inspection of all 15 pack CSVs and exploratory trace checks for selected variable-current examples. It establishes that the archive contains measurable differences in operating-current regimes and that some selected traces contain stable current plateaus. It also exposes limitations in the current segmentation method.

It does **not** yet establish that the 40/60/80-second protocol has been fully reconstructed, nor that the dataset has validated SOH labels or a suitable RUL target. EOL/failure definition, capacity reference data, pack lineage, and label construction remain open feasibility questions. No AI model has been trained or evaluated from this audit.

## Reproducibility note

The raw ZIP archive and locally generated segment CSV/PNG outputs remain outside this repository. The numerical summaries in this document are transcribed from local audit outputs supplied during the project workflow. The local tool versions and exact command parameters should be committed or recorded before treating this audit as a fully reproducible pipeline.


### Duration-band current comparison

For the refined segmentation CSV generated with a current tolerance of 0.30 A and maximum adjacent-sample gap of 2.0 s, candidate segments were grouped into duration bands of 35–<45 s, 55–<65 s and 75–<85 s. The table reports the number of candidate segments in each band and the median of their per-segment measured-current medians.

| Pack | Duration band | Candidate segments | Median segment current (A) |
|---|---:|---:|---:|
| 4.0 | 40 s | 137 | 17.7429 |
| 4.0 | 60 s | 176 | 18.2848 |
| 4.0 | 80 s | 256 | 17.3831 |
| 4.1 | 40 s | 1,188 | 14.7355 |
| 4.1 | 60 s | 895 | 14.8950 |
| 4.1 | 80 s | 638 | 15.4085 |
| 5.0 | 40 s | 147 | 17.7069 |
| 5.0 | 60 s | 188 | 18.1919 |
| 5.0 | 80 s | 319 | 17.4133 |
| 5.1 | 40 s | 1,014 | 14.5724 |
| 5.1 | 60 s | 631 | 14.6815 |
| 5.1 | 80 s | 444 | 15.1892 |

The pack-level current distributions differ: packs 4.0 and 5.0 have higher segment-current medians than packs 4.1 and 5.1 in these selected duration bands. Within packs 4.1 and 5.1, the median segment current increases across the 40 s, 60 s and 80 s bands in this output. Packs 4.0 and 5.0 do not show the same monotonic pattern.

These are descriptive summaries of algorithmically detected candidate segments. The median is calculated across candidate-segment medians, not across all raw samples, and candidate counts are not independent experimental replicates. Because the segmentation is parameter-sensitive and some selected intervals contain internal current changes, these results must not be interpreted as confirmed commanded-load levels or causal effects of duration on current.
