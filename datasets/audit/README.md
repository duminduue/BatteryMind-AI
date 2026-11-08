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

### First measurement-level inspection: regular battery00.csv

The first 3,000 characters of the CSV and a row-level completeness summary were inspected directly from the ZIP archive without extracting the full archive.

- Rows: 1,101,244
- Columns: 10
- Columns: `start_time`, `time`, `mode`, `voltage_charger`, `temperature_battery`, `voltage_load`, `current_load`, `temperature_mosfet`, `temperature_resistor`, `mission_type`.
- `start_time`, `time`, `mode`, `voltage_charger`, `temperature_battery`: non-empty in all 1,101,244 rows.
- `voltage_load`, `current_load`, `temperature_mosfet`, `temperature_resistor`, `mission_type`: non-empty in 106,006 rows each (about 9.63%).
- Observed mode codes: `-1.0`, `0.0`, `1.0`.
- Observed mission type codes: `0.0`, `1.0`.

#### Preliminary observed value ranges

From the user's local scan of `battery00.csv`:

| Column | Minimum | Maximum |
|---|---:|---:|
| `voltage_charger` | -0.060 | 9.176 |
| `temperature_battery` | 0.000 | 102.308 |
| `voltage_load` | -0.027 | 8.703 |
| `current_load` | 0.150 | 19.391 |

These are raw observed extrema, not validated physical operating limits. The small negative voltage values and the maximum battery-temperature reading of 102.308 require investigation against the data documentation and neighbouring samples before deciding whether they are sensor offsets, transient events, outliers or data-quality problems. Units should also be confirmed from the official documentation.

**Interpretation limits:** The meanings of mode and mission-type codes have not yet been verified. The first file inspection does not establish that all 26 files have the same schema, nor does it establish capacity, SOH, EOL or RUL labels. Sparse load-related columns may represent different phases of the mission or missing measurements; this needs investigation before imputation or feature selection.

## Next Step

Inspect the official documentation and representative CSV files from each battery group. Establish the meanings of coded fields, measurement units, pack/cell lineage, operating conditions and whether capacity/EOL labels can be derived defensibly.

**Important:** Archive file counts are not battery-cell counts. The inventory and single-file sample do not establish dataset suitability or scientific independence.
