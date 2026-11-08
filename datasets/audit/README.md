# Dataset Audit

This folder contains dataset audit documentation and lightweight inventory outputs. Raw dataset archives remain local and are not committed to GitHub.

## NASA Legacy Battery Aging Dataset

- Downloaded: Yes
- Archive inventory: Complete
- Files indexed (including nested ZIP contents): 54
- MATLAB `.mat` files: 38
- TXT files: 10
- ZIP files: 6
- Measurement-level inspection: Pending

Inventory: [NASA_Legacy_inventory.csv](NASA_Legacy_inventory.csv)

## NASA Randomized and Recommissioned Dataset

- Downloaded: Yes
- Archive inventory: Complete
- Files indexed: 66
- CSV entries in archive inventory: 52
- Actual battery CSV files (excluding `__MACOSX/._*` metadata sidecars): 26
  - Regular batteries: 15
  - Recommissioned batteries: 8
  - Second-life batteries: 3
- TXT files: 10
- Files without an extension: 4
- MATLAB `.mat` files: 0

Inventory: [NASA_Randomized_inventory.csv](NASA_Randomized_inventory.csv)

### Dataset documentation findings

The archive's `README.txt` describes an accelerated life-testing dataset of lithium-ion **battery packs** under constant and variable loading conditions. Each pack has a dedicated CSV containing continuous data logging.

The three groups are:
- `regular_alt_batteries`: packs cycled at the same load level or load range throughout life.
- `recommissioned_batteries`: packs whose constant loading level changes at different life stages.
- `second_life_batteries`: packs assembled from cells that survived previous cycling and then tested through a second life.

The README specifies these column definitions and units:

| CSV field | Documentation definition |
|---|---|
| `start_time` | Start time of each cycle day; format `mm:dd:yyyy hh:mm:ss`; usually approximately 24 hours |
| `time` | Continuous relative time from the beginning of the entire life cycle to pack failure, in seconds |
| `mode` | -1 = discharge; 0 = rest; 1 = charge |
| `voltage_charger` | Battery pack voltage measured after connection to the charger board, in V |
| `temperature_battery` | Continuous temperature measurement on the battery cell electrode surface, in °C |
| `voltage_load` | Battery pack voltage measured on the load board, in V; populated during discharge missions |
| `current_load` | Discharge current measured on the load board using current-sense resistors, in A; populated during discharge missions |
| `temperature_mosfet` | Load-board MOSFET temperature, in °C; populated during discharge missions |
| `temperature_resistor` | Load-board current-sense resistor temperature, in °C; populated during discharge missions |
| `mission_type` | 0 = reference discharge (constant current at 2.5 A); 1 = regular mission; populated during discharge missions |

This documentation explains why load-related columns and `mission_type` are populated only during discharge missions. Their lower non-empty count in the inspected CSV should not automatically be treated as random missingness.

#### Loading protocols documented for the three groups

**Regular packs**
- Constant-current groups (approximate average current levels): 9.30 A (packs 0.1, 1.1); 12.9 A (3.1, 2.2); 14.3 A (2.3, 5.2); 16.0 A (0.0, 1.0); 19.0 A (2.0, 3.0, 2.1).
- Variable-current groups: current segments remain constant for 40, 60 or 80 seconds, with randomly selected amplitudes and segment lengths. Approximate average 14.3 A (12.9–16 A range; packs 4.1, 5.1) and 17.0 A (16–19 A range; packs 4.0, 5.0).

**Recommissioned packs**
- Two-stage tests switch current after capacity reaches approximately 2.2 Ah.
- Three-stage tests switch at approximately 2.2 Ah and 2.0 Ah.
- The README lists the current sequences and pack IDs; see the original folder README for the exact sequences.

**Second-life packs**
- Packs consist of cells that survived earlier cycling. Survivor cells are reused and subjected to a second current level until EOL.
- Documented lineage: pack 1.3 from first-life packs 0.0 and 1.1; pack 3.6 from 2.3 and 5.2; pack 5.4 from 2.2 and 3.1.
- The README lists first- and second-life average current levels for each pack.

### First measurement-level inspection: regular battery00.csv

The CSV was sampled and scanned directly from the ZIP archive without extracting the full archive.

- Rows: 1,101,244
- Columns: 10
- `start_time`, `time`, `mode`, `voltage_charger`, `temperature_battery`: non-empty in all 1,101,244 rows.
- `voltage_load`, `current_load`, `temperature_mosfet`, `temperature_resistor`, `mission_type`: non-empty in 106,006 rows each (about 9.63%); the dataset README says these are only populated during discharge missions.
- Observed mode codes: `-1.0`, `0.0`, `1.0`; meanings are documented above.
- Observed mission type codes: `0.0`, `1.0`; meanings are documented above.

#### Preliminary observed value ranges

From the local scan of `battery00.csv`:

| Column | Minimum | Maximum |
|---|---:|---:|
| `voltage_charger` | -0.060 V | 9.176 V |
| `temperature_battery` | 0.000 °C | 102.308 °C |
| `voltage_load` | -0.027 V | 8.703 V |
| `current_load` | 0.150 A | 19.391 A |

These are raw observed extrema, not validated physical operating limits.

#### Investigation of the maximum battery-temperature event

The maximum `temperature_battery` value (102.308 °C) was not an isolated single-row spike. The neighbouring records show a sustained sequence from approximately 101.4 to 102.3 °C, then a gradual decrease after the maximum. During the rising sequence, `current_load` is approximately 16.3–16.5 A and `voltage_load` declines from about 5.34 to 4.92 V. The MOSFET and resistor temperatures in the same records are around 31–33 °C.

This co-occurrence is an observation, not a confirmed physical explanation. The dataset README identifies the battery temperature sensor as measuring the cell electrode surface, while MOSFET and resistor temperatures are measured on the load board. The high reading must be retained for investigation, not silently removed or capped. Verify the experiment context and sensor behaviour before interpreting it as a failure or thermal event.

### Licence and citation

The archive includes a `LICENSE.txt` stating the MIT License, copyright (c) 2019 PML @ UCF. Preserve the copyright and permission notice when redistributing the software or substantial portions covered by that licence. Confirm the data citation separately.

The dataset README requests citation as:
- Fricke, Kajetan; Nascimento, Renato G.; Viana, Felipe A. C. (2023). *An accelerated Life Testing Dataset for Lithium-Ion Batteries with Constant and Variable Loading Conditions*, version 0.0.1.
- It also lists related publications by Fricke et al., including *Prognosis of Li-ion Batteries Under Large Load Variations Using Hybrid Physics-Informed Neural Networks*.

The README's BibTeX template has blank DOI and URL fields; do not invent them.

### Current interpretation and limitations

- The documentation explicitly states that relative time runs from the beginning of each pack's life cycle to pack failure. This makes the time axis potentially useful for prognostics, but the exact operational EOL/failure definition and label-generation procedure still need verification.
- The README provides approximate capacity thresholds for recommissioning transitions (about 2.2 Ah and 2.0 Ah), not a complete cycle-by-cycle capacity-fade/SOH reference series.
- The data unit described in the README is a battery pack. Do not count each pack CSV as an independent individual cell. Second-life pack lineage explicitly links reused cells to earlier packs, so these records are not independent across life stages.
- Confirm all 26 files' schemas, time continuity, data quality, pack lineage and condition mapping before building splits.
- Avoid random row/window splits. Keep related life stages and lineage groups together when designing cell/pack-level validation to prevent leakage.

## Next Step

Audit the complete CSV inventory at pack level: parse pack IDs from filenames, map each pack to its documented load protocol and lineage, inspect the remaining two battery groups, and investigate how pack failure/EOL is operationally defined. Then determine whether the dataset supports SOH prediction, RUL prediction, or only selected prognostic tasks.

**Important:** Archive file counts and a single-file sample do not establish dataset suitability or scientific independence.


### Second measurement-level inspection: recommissioned battery03.csv

The local scan of `recommissioned_batteries/battery03.csv` found:

- Rows: 2,161,444.
- Relative time: 0 to 2,210,055.058 seconds.
- Recorded date range: 4 February 2023 to 13 March 2023.
- Mode counts: charge (`1.0`) 1,163,402; rest (`0.0`) 654,715; discharge (`-1.0`) 343,327.
- Discharge mission counts: reference (`mission_type=0.0`) 60,954; regular (`mission_type=1.0`) 282,373.
- Observed ranges: charger voltage 0–8.776 V; battery temperature 0–80.314 °C; load voltage -0.027–9.058 V; load current 0.15–16.825 A.

#### Observed regular-discharge current by date

Daily statistics were calculated only from rows where `mode=-1.0`, `mission_type=1.0`, and `current_load` was non-empty.

- 4–14 February: daily median current approximately 16.28–16.69 A.
- 15–19 February: daily median approximately 14.95–15.08 A.
- 20 February: median 7.510 A and mean 9.865 A, consistent with a mixed/transition day.
- 21 February–13 March: daily median approximately 7.39–7.57 A.

The observed stages broadly support the documented three-stage protocol for pack 3.2 (nominal sequence 16 A → 14.3 A → 7.5 A). However, measured daily medians are not identical to nominal protocol values. This is an empirical correspondence, not proof of the exact transition trigger or capacity threshold. The transition dates should be checked against the original protocol and capacity records before making stronger claims.

The daily aggregation is descriptive. It does not establish SOH, capacity fade, or EOL labels, and the 20 February mean is influenced by the transition between current regimes.


#### Closer inspection of the 20 February load-stage change

A follow-up scan of regular discharge records (`mode=-1.0`, `mission_type=1.0`) on 20 February found:

- The final observed high-load session before the lower-current regime included readings around 14.91 A, ending at relative time 1,052,033.776 s.
- The next observed discharge session began at relative time 1,063,033.437 s with 7.616 A; subsequent samples were around 7.60 A.
- The records between these sessions include low-current/near-zero-voltage transition or connection readings (approximately 0.46–0.50 A with -0.026 V), which should not be treated as the new sustained load level.

This supports a change between discharge sessions from the approximately 15 A measured regime to the approximately 7.6 A measured regime. It does not show an instantaneous current step within one continuous discharge session. The exact operational trigger for the change (including whether it occurred at the documented capacity threshold) is not established by this daily current scan alone.


### Third measurement-level inspection: recommissioned battery02.csv

The local daily aggregation of regular discharge records (`mode=-1.0`, `mission_type=1.0`, non-empty `current_load`) for `recommissioned_batteries/battery02.csv` produced:

- 26 November–3 December 2022: daily median current 16.303–16.526 A.
- 4–11 December 2022: daily median current 13.484–13.644 A.
- 11–22 January 2023 (dates with records shown in the supplied output): daily median current 13.658–13.719 A.

The observed pattern is consistent with a change from a higher-current stage to a lower-current stage. The dataset documentation lists pack 2.2 among the two-stage recommissioned packs with nominal sequence 16 A → 12.9 A. The measured medians (about 13.5–13.7 A in the lower stage) do not exactly equal the nominal protocol value; report nominal protocol and measured current separately.

The supplied daily summary contains no listed discharge dates between 12 December 2022 and 10 January 2023. This is a gap in the displayed daily discharge records, not evidence that the pack was inactive throughout that interval. This summary alone does not establish transition trigger, capacity threshold, SOH, or EOL labels.


A subsequent date-coverage check for `battery02.csv` confirmed that regular-discharge records occur on 27 distinct dates, with first date 26 November 2022 and last date 22 January 2023. The interval between these endpoints is therefore not continuously represented by regular-discharge dates in this filtered summary.


### Fourth measurement-level inspection: recommissioned battery12.csv

The local daily aggregation of regular discharge records (`mode=-1.0`, `mission_type=1.0`, non-empty `current_load`) for `recommissioned_batteries/battery12.csv` produced:

- 23–29 November 2022: daily median current approximately 16.288–16.497 A.
- 30 November 2022: mean 12.732 A and median 9.595 A, indicating a mixed/transition day in this daily aggregation.
- 1–11 December 2022: daily median current approximately 9.484–9.785 A.
- 11 January–4 February 2023 (dates represented in the supplied output): daily median current approximately 9.808–9.881 A.

The filename `battery12.csv` corresponds to pack 1.2 in the documented naming convention. The dataset README lists pack 1.2 among two-stage recommissioned packs with nominal current sequence 16 A → 9.30 A. The observed daily medians broadly support a change from the approximately 16.3–16.5 A regime to the approximately 9.5–9.9 A regime. The measured values are not identical to the nominal protocol current and should be reported separately.

The supplied daily summary has a gap in represented discharge dates between 12 December 2022 and 10 January 2023; this does not establish that the pack was inactive during that interval. The 30 November daily mean is elevated relative to its median, consistent with mixed current regimes or transitional samples, but the exact transition timing requires session-level inspection. This summary alone does not establish the capacity trigger, SOH, or EOL labels.


A session-level follow-up for 30 November 2022 in `battery12.csv` counted 9,245 regular-discharge samples: 30 below 1 A, 4,257 at or above 16 A, and 4,958 between 8 and 11 A. The first displayed records include approximately 16.52 A after low-current connection readings; the final displayed records are approximately 9.75–9.81 A. This confirms that the daily mean (12.732 A) combines two distinct current regimes rather than representing a single operating current. The count distribution supports a mixed/transition-day interpretation; it does not by itself identify the exact transition time or capacity trigger.


### Fifth measurement-level inspection: recommissioned battery33.csv

The local daily aggregation of regular discharge records (`mode=-1.0`, `mission_type=1.0`, non-empty `current_load`) for `recommissioned_batteries/battery33.csv` produced:

- 25 November–2 December 2022: daily median current approximately 16.332–16.628 A.
- 3–11 December 2022: daily median current approximately 13.497–13.676 A.
- 11–26 January 2023 (dates represented in the supplied output): daily median current approximately 13.669–13.855 A.

The dataset documentation lists pack 3.3 among the two-stage recommissioned packs with nominal current sequence 16 A → 12.9 A. The observed pattern is consistent with a transition from a higher-current regime to a lower-current regime. The lower-stage daily medians (about 13.5–13.9 A) are higher than the nominal 12.9 A; preserve this distinction rather than relabeling measured current as nominal protocol current.

The supplied output contains a gap in represented discharge dates between 12 December 2022 and 10 January 2023. This is a gap in the filtered daily summary, not evidence that the pack was inactive throughout that interval. This aggregation does not establish the transition trigger, capacity threshold, SOH, or EOL labels.


### Sixth measurement-level inspection: recommissioned battery32.csv

The supplied daily aggregation of regular discharge records (`mode=-1.0`, `mission_type=1.0`, non-empty `current_load`) for `recommissioned_batteries/battery32.csv` shows:

- 19–25 October 2022: daily median current approximately 16.279–16.679 A.
- 26 October 2022: median 14.818 A, consistent with a mixed/transition day.
- 27 October–14 November 2022 (dates represented in the supplied output): daily median current approximately 14.919–15.322 A.

The dataset documentation lists pack 3.2 among the two-stage recommissioned packs with nominal sequence 16 A → 14.3 A. The observed daily pattern broadly supports a shift from a higher-current regime to a lower-current regime, although the lower-stage measured medians are approximately 14.8–15.3 A rather than exactly 14.3 A. Nominal protocol values and measured current statistics must remain distinct.

The supplied output ends on 14 November 2022; it does not establish the pack's final discharge date or full lifetime. The 26 October daily median suggests a mixed/transition day but does not identify the exact transition time or capacity trigger. This daily summary does not establish SOH or EOL labels.


### Seventh measurement-level inspection: recommissioned battery24.csv

The supplied daily aggregation of regular discharge records (`mode=-1.0`, `mission_type=1.0`, non-empty `current_load`) for `recommissioned_batteries/battery24.csv` shows:

- 4–12 November 2022 (dates represented): daily median current approximately 16.300–16.578 A.
- 13 November: median 9.740 A.
- 14 November: median 16.578 A.
- 15 November: median 9.760 A.
- 16 November–18 January 2023 (dates represented): daily median current approximately 9.553–9.708 A.

The dataset documentation lists pack 2.4 among the two-stage recommissioned packs with nominal current sequence 16 A → 9.30 A. Most of the supplied daily summaries are consistent with a higher-current regime followed by a lower-current regime. However, the 14 November daily median returns to approximately 16.58 A between lower-current dates (13 and 15 November). This non-monotonic daily pattern must not be smoothed away or assumed to be an error. It may reflect distinct discharge sessions, a change in operating mission, or another protocol/data feature; session-level inspection and the original experiment log are needed before interpreting the sequence.

The lower-stage measured medians (about 9.55–9.71 A) are above the nominal 9.30 A protocol value. Nominal protocol and measured current must be reported separately. The supplied output ends on 18 January 2023 and does not establish the full lifetime, EOL label, or capacity trigger.


A focused first/last-record check of `battery24.csv` on 13–15 November 2022 confirms the unusual daily pattern:

- 13 November: 11,117 regular-discharge samples; first displayed valid load readings are approximately 9.59–9.60 A and final readings approximately 9.93–9.95 A.
- 14 November: 4,583 samples; first displayed valid load readings are approximately 16.68 A and final readings approximately 16.15 A.
- 15 November: 11,926 samples; first displayed valid load readings are approximately 9.61 A and final readings approximately 9.96 A.

Thus, the high-current regime is present across the displayed beginning and end of 14 November, while 13 and 15 November show the lower-current regime. This is stronger evidence of a day/session-level return to the high-current regime than the daily median alone, but it still does not establish why the protocol alternated or whether this reflects planned mission scheduling, recommissioning procedure, or another experiment-specific factor. Do not assume a single monotonic 16 A → 9.3 A transition for this pack without checking the original experiment log and all session boundaries.


### Eighth measurement-level inspection: recommissioned battery25.csv

The supplied daily aggregation of regular discharge records (`mode=-1.0`, `mission_type=1.0`, non-empty `current_load`) for `recommissioned_batteries/battery25.csv` shows three apparent current regimes:

- 4–14 February 2023 (dates represented): daily median current approximately 16.173–16.401 A.
- 15–28 February 2023: daily median current approximately 6.975–7.433 A, broadly consistent with the documented intermediate nominal stage of 7.5 A.
- 1–2 March 2023: mixed daily summaries (1 March mean 12.337 A, median 14.971 A; 2 March mean 9.962 A, median 7.505 A), consistent with a transition/mixed-regime period that requires session-level inspection.
- 3–13 March 2023 (dates represented): daily median current approximately 14.993–15.018 A.

The dataset documentation lists pack 2.5 among the three-stage recommissioned packs with nominal sequence 16 A → 7.5 A → 14.3 A, with stage changes associated with approximate capacity thresholds of 2.2 Ah and 2.0 Ah. The observed sequence (about 16.2 A → 7.4 A → 15.0 A) broadly corresponds to those three nominal stages, but the measured medians differ from nominal values, especially in the final stage. Keep protocol currents and measured currents distinct.

The daily aggregation suggests transition periods around 15 February and 1–3 March, but it does not establish exact transition times or verify the capacity thresholds. The 1–2 March means/medians differ substantially, showing why daily means alone can conceal mixed regimes. Session-level analysis and capacity/experiment logs are needed before attributing the transitions to the documented capacity triggers. This summary does not establish SOH or EOL labels.


### Ninth measurement-level inspection: recommissioned battery53.csv

The supplied daily aggregation of regular discharge records (`mode=-1.0`, `mission_type=1.0`, non-empty `current_load`) for `recommissioned_batteries/battery53.csv` shows:

- 24 October–4 November 2022: daily median current approximately 14.712–15.104 A.
- 19–22 November 2022: daily median current approximately 16.667–16.884 A.

The dataset documentation lists pack 5.3 among two-stage recommissioned packs with nominal sequence 14.3 A → 16 A. The supplied measurements broadly support a change from the lower-current regime (about 14.7–15.1 A measured) to the higher-current regime (about 16.7–16.9 A measured), consistent with the documented direction of change. The measured daily medians are not identical to nominal protocol values and should be reported separately.

The supplied daily summary has no listed regular-discharge dates between 5 and 18 November 2022. This is a gap in the supplied filtered dates, not evidence that the pack was inactive throughout the interval. The summary does not establish the exact transition time, capacity trigger, SOH, or EOL labels. Session-level and experiment-log checks remain necessary.


## Recommissioned group: consolidated pack-level comparison

The eight actual CSV filenames in the recommissioned folder encode pack IDs with the decimal point omitted (for example, `battery03.csv` represents pack 0.3). The table below combines the official protocol descriptions supplied in the dataset README with the daily measured-current summaries inspected locally. Nominal currents are protocol values; observed currents are daily medians from regular discharge rows only (`mode=-1.0`, `mission_type=1.0`).

| CSV file | Pack ID | Documented nominal sequence (A) | Observed measured-current regimes (A, approximate daily medians) | Initial interpretation / caveat |
|---|---:|---:|---|---|
| `battery03.csv` | 0.3 | 16 → 14.3 → 7.5 | 16.3–16.7 → 15.0 → 7.4–7.6 | Three regimes broadly correspond; 20 Feb is a mixed/session-transition day. |
| `battery02.csv` | 0.2 | 16 → 12.9 | 16.3–16.5 → 13.5–13.7 | Two regimes broadly correspond; measured lower stage is above nominal. |
| `battery12.csv` | 1.2 | 16 → 9.3 | 16.3–16.5 → 9.5–9.9 | Two regimes broadly correspond; 30 Nov combines both regimes. |
| `battery33.csv` | 3.3 | 16 → 12.9 | 16.3–16.6 → 13.5–13.9 | Two regimes broadly correspond; measured lower stage is above nominal. |
| `battery32.csv` | 3.2 | 16 → 14.3 | 16.3–16.7 → 14.8–15.3 | Two regimes broadly correspond; measured lower stage is above nominal. |
| `battery24.csv` | 2.4 | 16 → 9.3 | 16.3–16.6 and 9.5–9.7 | Alternating daily regimes were observed around 13–15 Nov; do not force a monotonic transition interpretation. |
| `battery25.csv` | 2.5 | 16 → 7.5 → 14.3 | 16.2–16.4 → 7.0–7.4 → 15.0 | Three regimes broadly correspond; 1–2 Mar are mixed/transition days. |
| `battery53.csv` | 5.3 | 14.3 → 16 | 14.7–15.1 → 16.7–16.9 | Direction of two-stage change broadly corresponds; discharge-date gap 5–18 Nov. |

### Interpretation boundaries

- This comparison is a screening summary based on the daily outputs supplied in this audit, not a full re-computation of all CSVs or a validation of the experiment protocol.
- Measured current medians are not the same as nominal protocol currents. Do not replace one with the other or treat the differences as errors without investigating sensor calibration, load control, and measurement context.
- Daily means can be misleading on mixed days; medians and session-level summaries are more informative for identifying multiple regimes.
- Missing dates in these filtered daily summaries mean no qualifying regular-discharge rows were shown for those dates. They do not prove that a pack was inactive.
- The pack IDs above correct any ambiguity between filenames and pack labels: `battery03.csv` is pack 0.3, `battery02.csv` is pack 0.2, and so on. In particular, `battery03.csv` is the documented three-stage pack 0.3 (16 → 14.3 → 7.5 A), not pack 3.2.
- These current-regime observations do not establish capacity-fade labels, SOH ground truth, exact recommissioning thresholds, or EOL/RUL target validity.

### Recommended next audit actions

1. Complete the regular-pack and second-life pack daily protocol audits.
2. Inspect capacity/failure definitions and determine whether capacity reference measurements are available in the archives.
3. Audit second-life lineage and design pack-level splits that keep related first-life and second-life records together.
4. Only after these checks, decide which supervised tasks (SOH, RUL, or another prognostic target) are defensible.


### Tenth measurement-level inspection: regular battery00.csv (pack 0.0)

The local daily aggregation of regular discharge records (`mode=-1.0`, `mission_type=1.0`, non-empty `current_load`) for `regular_alt_batteries/battery00.csv` produced:

- 14 represented discharge dates.
- Date range: 22 July 2022 to 9 August 2022.
- Daily median current range: approximately 16.306–16.918 A.
- First three represented dates: 22 July (1,668 samples; median 16.306 A), 23 July (8,544; 16.343 A), and 24 July (5,122; 16.406 A).
- Last three represented dates: 7 August (4,385; 16.918 A), 8 August (3,795; 16.906 A), and 9 August (259; 16.871 A).

The dataset documentation lists regular pack 0.0 in the nominal 16.0 A constant-current group. The observed daily medians are consistently above 16 A in the supplied summary. Preserve the distinction between the documented nominal protocol and measured current; this difference alone does not establish a protocol deviation, sensor error, or abnormal operating condition.

This is a daily-summary audit of qualifying regular-discharge records only. The 14 represented dates do not establish that no other activity occurred on dates absent from this filtered summary. The output does not establish capacity fade, SOH ground truth, failure/EOL labels, or RUL target validity.


### Eleventh measurement-level inspection: regular battery10.csv (pack 1.0)

The local daily aggregation of regular discharge records (`mode=-1.0`, `mission_type=1.0`, non-empty `current_load`) for `regular_alt_batteries/battery10.csv` produced:

- 11 represented discharge dates.
- Date range: 22 July 2022 to 6 August 2022.
- Daily median current range: approximately 16.256–16.788 A.
- First three represented dates: 22 July (1,676 samples; median 16.256 A), 23 July (8,557; 16.279 A), and 24 July (5,140; 16.340 A).
- Last three represented dates: 3 August (5,343; 16.770 A), 4 August (5,407; 16.788 A), and 6 August (3,677; 16.782 A).

The dataset documentation lists regular pack 1.0 in the nominal 16.0 A constant-current group. The observed daily medians are above 16 A in the supplied summary. Preserve the distinction between documented nominal protocol and measured current; this difference alone does not establish a protocol deviation, sensor error, or abnormal operating condition.

This is a daily-summary audit of qualifying regular-discharge records only. The 11 represented dates do not establish that no other activity occurred on dates absent from this filtered summary. The output does not establish capacity fade, SOH ground truth, failure/EOL labels, or RUL target validity.


### Twelfth measurement-level inspection: regular battery31.csv (pack 3.1)

The local daily aggregation of regular discharge records (`mode=-1.0`, `mission_type=1.0`, non-empty `current_load`) for `regular_alt_batteries/battery31.csv` produced:

- 49 represented discharge dates.
- Date range: 1 August 2022 to 12 October 2022.
- Daily median current range: approximately 12.678–13.759 A.
- First three represented dates: 1 August (4,159 samples; median 12.678 A), 3 August (7,859; 13.003 A), and 4 August (7,509; 12.854 A).
- Last three represented dates: 10 October (7,229; 13.756 A), 11 October (4,317; 13.759 A), and 12 October (4,731; 13.753 A).

The dataset documentation lists regular pack 3.1 in the nominal 12.9 A constant-current group. Most of the observed daily medians are near this nominal value, with the supplied daily range extending to approximately 13.76 A. Preserve the distinction between documented nominal protocol and measured current; the observed variation alone does not establish a protocol deviation or sensor issue.

This is a daily-summary audit of qualifying regular-discharge records only. The 49 represented dates do not establish that no other activity occurred on dates absent from this filtered summary. The output does not establish capacity fade, SOH ground truth, failure/EOL labels, or RUL target validity.


### Thirteenth measurement-level inspection: regular battery22.csv (pack 2.2)

The local daily aggregation of regular discharge records (`mode=-1.0`, `mission_type=1.0`, non-empty `current_load`) for `regular_alt_batteries/battery22.csv` produced:

- 40 represented discharge dates.
- Date range: 6 August 2022 to 6 October 2022.
- Daily median current range: approximately 12.987–13.812 A.
- First three represented dates: 6 August (8,857 samples; median 12.987 A), 7 August (6,167; 13.008 A), and 8 August (6,584; 13.025 A).
- Last three represented dates: 26 September (5,148; 13.777 A), 27 September (2,583; 13.787 A), and 6 October (4,227; 13.812 A).

The dataset documentation lists regular pack 2.2 in the nominal 12.9 A constant-current group. The observed daily medians are close to 12.9 A at the start of the represented period and rise to approximately 13.8 A in the later represented dates. Preserve these as measured daily statistics; this summary alone does not establish a change in the documented operating protocol, its cause, or a sensor issue.

This is a daily-summary audit of qualifying regular-discharge records only. The 40 represented dates do not establish that no other activity occurred on dates absent from this filtered summary. The output does not establish capacity fade, SOH ground truth, failure/EOL labels, or RUL target validity.


### Fourteenth measurement-level inspection: regular battery23.csv (pack 2.3)

The local daily aggregation of regular discharge records (`mode=-1.0`, `mission_type=1.0`, non-empty `current_load`) for `regular_alt_batteries/battery23.csv` produced:

- 19 represented discharge dates.
- Date range: 8 October 2022 to 26 October 2022.
- Daily median current range: approximately 14.845–15.169 A.
- First three represented dates: 8 October (5,420 samples; median 14.845 A), 9 October (8,341; 14.856 A), and 10 October (8,548; 14.885 A).
- Last three represented dates: 24 October (7,058; 15.116 A), 25 October (5,326; 15.146 A), and 26 October (2,869; 15.169 A).

The dataset documentation lists regular pack 2.3 in the nominal 14.3 A constant-current group. The observed daily medians are approximately 14.85–15.17 A, above the nominal protocol value. Preserve the distinction between documented nominal protocol and measured current; this difference alone does not establish a protocol deviation, sensor error, or abnormal operating condition.

This is a daily-summary audit of qualifying regular-discharge records only. The 19 represented dates do not establish that no other activity occurred on dates absent from this filtered summary. The output does not establish capacity fade, SOH ground truth, failure/EOL labels, or RUL target validity.


### Fifteenth measurement-level inspection: regular battery52.csv (pack 5.2)

The local daily aggregation of regular discharge records (`mode=-1.0`, `mission_type=1.0`, non-empty `current_load`) for `regular_alt_batteries/battery52.csv` produced:

- 22 represented discharge dates.
- Date range: 15 September 2022 to 16 October 2022.
- Daily median current range: approximately 14.545–15.168 A.
- First three represented dates: 15 September (1,249 samples; median 14.545 A), 16 September (8,666; 14.618 A), and 17 September (5,372; 14.651 A).
- Last three represented dates: 14 October (4,497; 15.098 A), 15 October (6,726; 15.124 A), and 16 October (6,353; 15.168 A).

The dataset documentation lists regular pack 5.2 in the nominal 14.3 A constant-current group. The observed daily medians are approximately 14.55–15.17 A, above the nominal protocol value. Preserve the distinction between documented nominal protocol and measured current; this difference alone does not establish a protocol deviation, sensor error, or abnormal operating condition.

This is a daily-summary audit of qualifying regular-discharge records only. The 22 represented dates do not establish that no other activity occurred on dates absent from this filtered summary. The output does not establish capacity fade, SOH ground truth, failure/EOL labels, or RUL target validity.


### Sixteenth measurement-level inspection: regular battery01.csv (pack 0.1)

The local daily aggregation of regular discharge records (`mode=-1.0`, `mission_type=1.0`, non-empty `current_load`) for `regular_alt_batteries/battery01.csv` produced:

- 70 represented discharge dates.
- Date range: 12 August 2022 to 13 November 2022.
- Daily median current range: approximately 9.290–9.795 A.
- First three represented dates: 12 August (1,913 samples; median 9.290 A), 13 August (5,731; 9.290 A), and 14 August (5,663; 9.294 A).
- Last three represented dates: 11 November (10,934; 9.767 A), 12 November (8,170; 9.764 A), and 13 November (9,378; 9.753 A).

The dataset documentation lists regular pack 0.1 in the nominal 9.30 A constant-current group. The observed daily medians are close to the documented nominal current, with a gradual increase in the measured daily medians over the represented period. This is a descriptive trend only; it does not establish a change in the operating protocol or its cause.

This is a daily-summary audit of qualifying regular-discharge records only. The 70 represented dates do not establish that no other activity occurred on dates absent from this filtered summary. The output does not establish capacity fade, SOH ground truth, failure/EOL labels, or RUL target validity.


### Seventeenth measurement-level inspection: regular battery11.csv (pack 1.1)

The local daily aggregation of regular discharge records (`mode=-1.0`, `mission_type=1.0`, non-empty `current_load`) for `regular_alt_batteries/battery11.csv` produced:

- 71 represented discharge dates.
- Date range: 9 August 2022 to 11 November 2022.
- Daily median current range: approximately 9.257–9.877 A.
- First three represented dates: 9 August (9,820 samples; median 9.257 A), 10 August (9,590; 9.291 A), and 11 August (12,527; 9.287 A).
- Last three represented dates: 7 November (10,414; 9.849 A), 8 November (6,020; 9.857 A), and 11 November (1,508; 9.846 A).

The dataset documentation lists regular pack 1.1 in the nominal 9.30 A constant-current group. The observed daily medians begin close to 9.30 A and rise to approximately 9.85 A in the last represented dates. This is a descriptive measured-current trend only; it does not establish a change in the operating protocol or its cause.

This is a daily-summary audit of qualifying regular-discharge records only. The 71 represented dates do not establish that no other activity occurred on dates absent from this filtered summary. The output does not establish capacity fade, SOH ground truth, failure/EOL labels, or RUL target validity.


### Eighteenth measurement-level inspection: regular battery20.csv (pack 2.0)

The local daily aggregation of regular discharge records (`mode=-1.0`, `mission_type=1.0`, non-empty `current_load`) for `regular_alt_batteries/battery20.csv` produced:

- 3 represented discharge dates.
- Date range: 22 July 2022 to 24 July 2022.
- Daily median current range: approximately 19.516–19.608 A.
- 22 July: 1,399 samples; median 19.516 A.
- 23 July: 7,128 samples; median 19.551 A.
- 24 July: 3,296 samples; median 19.608 A.

The dataset documentation lists regular pack 2.0 in the nominal 19.0 A constant-current group. The observed daily medians are approximately 19.52–19.61 A, above the nominal protocol value. This is a measured-current observation only; the short three-date summary does not establish a protocol deviation, sensor issue, or the pack's complete lifetime.

This is a daily-summary audit of qualifying regular-discharge records only. The output does not establish capacity fade, SOH ground truth, failure/EOL labels, or RUL target validity.
