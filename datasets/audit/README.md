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
- Measurement-level inspection: Pending

The archive contains macOS `__MACOSX` sidecar entries. These are metadata/resource-fork files and should not be counted as additional battery datasets. The 26 battery CSV files are file-level observations only; their experimental independence, pack/cell lineage and measurement contents still need verification.

Inventory: [NASA_Randomized_inventory.csv](NASA_Randomized_inventory.csv)

## Next Step

Inspect representative CSV headers and sample rows, then determine the actual experimental units, measurements, cell/pack identifiers, operating conditions and EOL/RUL label availability.

**Important:** Archive file counts are not battery-cell counts. The inventory does not establish dataset suitability or scientific independence.
