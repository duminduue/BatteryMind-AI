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
