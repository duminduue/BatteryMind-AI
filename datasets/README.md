# Dataset Audit — NASA and CALCE Candidates

**Status:** Preliminary source audit completed 2026-11-08. No primary dataset is locked yet.

## 1. NASA Li-ion Battery Aging Dataset

**Official catalogue:** https://catalog.data.gov/dataset/li-ion-battery-aging-datasets  
**Original landing page:** https://c3.nasa.gov/dashlink/resources/133/

### Provider-documented characteristics
- Data generated on a NASA Ames Prognostics Center of Excellence battery prognostics testbed.
- Commercial Li-ion 18650 cells.
- Charge, discharge, and electrochemical impedance spectroscopy (EIS) operation profiles.
- Testing at different temperatures and discharge loads.
- Repeated cycling to end of life.
- The catalogue describes EOL as 30% fade from rated 2 Ah capacity to 1.4 Ah (70% of rated capacity).
- Discharge records include voltage, current, temperature, time, and capacity.
- Impedance records include battery impedance, rectified impedance, electrolyte resistance (Re), and charge-transfer resistance (Rct).
- The catalogue describes the dataset as run-to-failure time series and notes cell-to-cell variation in DOD, rest duration, and state-of-life.

### Strengths for this project
- Explicit provider-described EOL criterion and capacity field support a clearly defined capacity-based SOH/RUL study.
- Multiple measured signals may support feature engineering and physically motivated health indicators.
- Run-to-failure structure is useful for prognostics.

### Risks / limitations to audit
- The number of independent cells is limited; cycle observations must not be treated as independent samples.
- Confirm exact cell identifiers, test temperatures, profiles, and missing records from the actual files.
- Confirm whether every selected cell has comparable protocol and complete capacity data.
- Do not assume all NASA subsets or commonly circulated versions are identical.
- EOL at 70% of rated capacity must be kept distinct from studies using 80% retention.

### Preliminary suitability
**Strong candidate for an initial benchmark**, especially for capacity-based SOH/RUL with a provider-documented 70% rated-capacity EOL criterion. It may be too small to support broad statistical claims about generalisation; cell-level sample size must be reported.

## 2. CALCE Battery Research Data

**Official provider page:** https://calce.umd.edu/data

### Provider-documented characteristics
CALCE describes open-access experimental data covering full and partial cycling, storage, dynamic driving profiles, OCV, and impedance measurements. It includes cylindrical, pouch, and prismatic formats and LCO, LFP, and NMC chemistries. CALCE requests citation of the articles describing the experiments when its data are used in publications.

The page documents multiple distinct collections. Examples include:
- INR 18650-20R cylindrical cell: 2000 mAh, LiNiMnCo/graphite.
- A123 cylindrical cell: 1110 mAh, LiFePO4.
- CS2 prismatic cells: 1100 mAh, LiCoO2 cathode (trace manganese also reported).
- CS2 cells include different current cycling regimes, including 0.5C, 1C, alternating discharge currents, and partial cycling regimes.
- CX2 cells include constant-current, pulsed, and temperature-varying test cases.
- PL pouch cells include partial cycling under different SOC ranges and discharge rates.

### Strengths for this project
- More diversity in chemistry, form factor, and cycling protocol than a single narrowly defined cell group.
- CS2/CX2 and PL experiments may support investigations of protocol and operating-condition effects.
- Provider documentation links datasets to experiment-description papers.

### Risks / limitations to audit
- CALCE is not one homogeneous dataset. Do not combine cells or collections without checking chemistry, protocol, tester, file structure, and target compatibility.
- The landing page does not establish one universal EOL definition for every collection.
- Some collections are SOC/dynamic-profile experiments, not necessarily run-to-failure ageing data suitable for direct RUL labels.
- Some cells use different battery testers and file formats.
- Publication requires appropriate CALCE experiment citations.

### Preliminary suitability
**Potential secondary validation source**, but only after selecting a specific ageing collection and verifying that its capacity trajectory and EOL definition support the same target as the primary dataset. CALCE should not be described as a single interchangeable benchmark.

## 3. Recommended staged dataset strategy

1. Start with an exact NASA file inventory and audit cell-level capacity trajectories.
2. Implement a baseline SOH/RUL pipeline using a predeclared NASA cell-held-out split, if the available cell count permits a defensible test.
3. Select one specific CALCE ageing collection (not the entire CALCE portal) for an external transfer experiment only if its capacity measurements, cell count, and EOL definition can be harmonised or explicitly treated as a different target.
4. If target definitions differ, report separate dataset-specific experiments rather than silently converting them into a common target.

## 4. Operational definitions to freeze before training

- **SOH:** Choose and justify the reference capacity (rated or measured beginning-of-life capacity). Document formula and units.
- **EOL:** Use provider-defined thresholds when available; otherwise justify a task-specific threshold and mark it as a project definition.
- **RUL:** Number of future cycles until the chosen EOL threshold, measured from the prediction cycle. Define treatment of cells that do not reach EOL (right-censoring).
- **Split:** Group by cell; do not randomly split cycle rows across train and test.
- **Calibration:** Keep calibration data separate from model training and final test data. State the unit of grouping.

## 5. Sources

- NASA / Data.gov: https://catalog.data.gov/dataset/li-ion-battery-aging-datasets
- CALCE: https://calce.umd.edu/data
