# Dataset Feasibility Audit — BatteryMind AI

**Audit date:** 8 November 2026  
**Status:** Preliminary desk audit; raw files have not yet been downloaded or programmatically inspected.  
**Research focus:** Physics-guided, data-efficient and uncertainty-calibrated battery health prediction under unseen operating conditions.

## 1. Audit objectives

A candidate dataset must be assessed for:

- Independent battery-cell count and unique cell identifiers.
- Chemistry, form factor, manufacturer and nominal capacity.
- Charge/discharge protocols, current rates, temperature and operating-condition diversity.
- Cycle-level capacity or other defensible SOH reference labels.
- A defensible RUL/EOL definition and sufficient run-to-failure observations.
- Metadata needed to construct cell-level and condition-level test splits.
- Download accessibility, citation requirements and reuse terms.
- Missingness, irregular sampling, data quality and preprocessing burden.

A large number of cycle records is not equivalent to a large number of independent batteries. The independent cell (or pack, where pack is the experimental unit) is the critical unit for assessing generalisation.

## 2. Candidate dataset register

### Candidate A — NASA Ames Li-ion Battery Aging Dataset (legacy PCoE)

**Official records**
- NASA Open Data: https://data.nasa.gov/dataset/li-ion-battery-aging-datasets
- NASA PCoE repository: https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/
- Direct archive listed by NASA: https://phm-datasets.s3.amazonaws.com/NASA/5.+Battery+Data+Set.zip

**What the official description supports**
- Run-to-failure lithium-ion battery experiments.
- Charge, discharge and electrochemical impedance spectroscopy (EIS) operations.
- Tests at different temperatures and current loads.
- Capacity is recorded for discharge to 2.7 V.
- The stated EOL criterion is 30% capacity fade from 2 Ah to 1.4 Ah.
- Voltage, current, temperature, time, capacity and impedance-related measurements are described.

**Potential research value**
- Capacity degradation trajectories and a stated EOL threshold are useful for SOH/RUL baseline experiments.
- The range of operational profiles and temperatures may support condition-aware evaluation, subject to confirming the actual cell-to-condition mapping.

**Risks / unresolved**
- The NASA Open Data catalogue record states that it has no data resource attached and the legacy dataset record does not specify a licence in that catalogue. NASA's PCoE page separately lists a direct archive. Confirm actual access and applicable reuse terms before redistribution.
- Verify exact cell IDs, chemistry, number of independent cells, per-cell temperature and load profiles, missing cycles and whether all cells have complete run-to-failure records.
- Do not assume the commonly used B0005/B0006/B0007/B0018 cells alone provide enough independent units for a broad generalisation claim.

**Preliminary status:** High-priority baseline candidate; not yet approved as the sole dataset.

### Candidate B — NASA Randomized and Recommissioned Battery Dataset

**Official record**
- https://data.nasa.gov/dataset/randomized-and-recommissioned-battery-dataset
- Dataset archive: https://data.nasa.gov/docs/legacy/battery_alt_dataset.zip

**What the official description supports**
- Accelerated life testing under constant and variable loading conditions.
- 26 battery packs, each composed of two 18650 cells.
- Packs grouped by constant and random loading conditions, load levels and number of load-level changes.
- Second-life packs were assembled from surviving cells of previously aged packs.
- NASA catalogue metadata links to the USA Government Works licence.

**Potential research value**
- Variable and random loading conditions are directly relevant to condition-shift and robustness questions.
- 26 packs may provide more independent experimental units than the small legacy NASA set, although packs are not necessarily independent individual-cell trajectories.
- Second-life data may enable an interesting transfer or history-variation analysis if the records and lineage are sufficiently documented.

**Risks / unresolved**
- The experimental unit is a two-cell pack; do not treat the 52 constituent cells as 52 independent trajectories unless separate cell measurements and independence are established.
- Inspect whether capacity/SOH can be measured or derived consistently at pack level.
- Verify pack IDs, loading schedules, cell lineage, sampling frequency, EOL definitions, completeness and data format.
- Confirm the licence and attribution requirements from the dataset record before using or redistributing data.

**Preliminary status:** High-priority candidate for variable-load robustness; inspect archive before selection.

### Candidate C — CALCE Battery Research Data

**Official source**
- https://calce.umd.edu/data

**What the official description supports**
- Open-access experimental lithium-ion battery data.
- Continuous full and partial cycling, storage, dynamic driving profiles, OCV and impedance measurements.
- Cylindrical, pouch and prismatic form factors.
- LCO, LFP and NMC chemistries are represented across the collection.
- The page lists multiple battery families and test descriptions, including INR 18650-20R, A123, CS2, CX2 and PL samples.
- CALCE asks publications using the data to cite the relevant CALCE article(s) describing the experiments.

**Potential research value**
- Multiple chemistries, form factors and test protocols could support external validation or cross-domain transfer.
- Partial cycling and dynamic profiles may be useful for data-efficiency and operational robustness questions.

**Risks / unresolved**
- CALCE is a collection, not one uniform run-to-failure dataset. Each battery family and experiment must be audited separately.
- Some records may be designed for SOC/OCV estimation rather than complete degradation-to-EOL studies.
- Verify which specific cells have sufficient cycle-life records, capacity reference measurements, EOL labels and condition metadata.
- Record publication citation requirements for every selected experiment.

**Preliminary status:** High-priority source for a second dataset or external validation; select specific sub-datasets only after file-level inspection.

### Candidate D — Battery Data Commons catalogue

**Official source**
- https://batterydatacommons.org/find-data/

**What the catalogue supports**
- A curated metadata commons designed to make battery datasets discoverable, comparable and citable.
- Search and filter across a large collection of dataset records. The catalogue search result observed during this audit reported 373 datasets.
- Search results include examples such as Stanford Long Term Calendar Aging (232 cells across eight cell types) and Battery Aging Matrix (363 cylindrical 21700 cells across many protocols).

**Potential research value**
- Can identify larger, more diverse datasets that may overcome the small-cell-count limitation of traditional benchmark datasets.
- Useful for discovering external validation candidates and documenting dataset provenance.

**Risks / unresolved**
- Battery Data Commons is a discovery catalogue, not a guarantee that all listed raw data are downloadable or licensed for unrestricted reuse.
- The 373 figure is a catalogue count, not a count of datasets suitable for this specific SOH/RUL task.
- Each record must be inspected for access conditions, raw data availability, labels, cell-level identifiers, protocols and licence.

**Preliminary status:** Discovery resource; shortlist specific records only after checking their original repositories.

## 3. Preliminary comparison

| Candidate | Experimental diversity | Independent-unit evidence from catalogue | SOH/RUL suitability | Current role |
|---|---|---|---|---|
| NASA legacy aging | Multiple temperatures and load profiles | Exact cell inventory still to verify | Capacity and stated EOL criterion described | Baseline benchmark |
| NASA randomized/recommissioned | Constant and variable/random loads; second-life packs | 26 two-cell packs | Lifecycle dataset; exact labels and EOL protocol to inspect | Condition-shift candidate |
| CALCE | Multiple chemistries, formats and protocols | Varies by sub-dataset | Some degradation datasets; collection also includes SOC-focused tests | External validation / selected sub-dataset |
| Battery Data Commons | Potentially broad | Varies by record; examples include 232-cell and 363-cell datasets | Must filter for degradation and RUL labels | Dataset discovery |

## 4. Important methodological rules

1. **Split by independent unit.** Keep all cycles/windows from one cell or pack in only one partition.
2. **Do not leak calibration data.** Calibration cells must be separate from model-fitting cells and final test cells whenever dataset size permits.
3. **Document the unit.** A two-cell pack is a pack-level observation unless separate cell-level measurements justify another interpretation.
4. **Harmonise labels carefully.** SOH may be defined as measured capacity divided by nominal/reference capacity. Record the exact denominator and measurement protocol.
5. **Define RUL explicitly.** State the EOL threshold, cycle/time unit and how future life is calculated. Do not assume every dataset uses the same EOL criterion.
6. **Separate interpolation from extrapolation.** Random cycle splits mostly measure interpolation and can leak cell identity; they do not establish unseen-cell generalisation.
7. **Audit conditions.** Build a cell/pack-to-condition table before claiming an unseen-temperature, unseen-load or unseen-chemistry test.
8. **Respect data terms.** Store provenance, source links, citations and licence notes. Do not commit raw archives to GitHub unless their terms and repository size make that appropriate.

## 5. Current recommendation

Do not lock a single dataset yet.

The strongest initial plan is to inspect:
- NASA legacy aging data for a reproducible baseline and capacity/EOL definitions.
- NASA randomized/recommissioned data for variable-load robustness, if pack-level labels and lineage are usable.
- One carefully selected CALCE or Battery Data Commons dataset for external validation, preferably with a clearly documented chemistry or protocol difference.

The dataset selection should be driven by the final evaluation design and independent-unit count, not by which dataset is easiest to download.

## 6. Next action — file-level audit

For each shortlisted archive or dataset record, create a manifest with:

- Filename and source URL.
- Cell/pack IDs and count.
- Chemistry and form factor.
- Temperature and load profiles.
- Number of cycles / test duration per unit.
- Capacity/SOH availability and definition.
- EOL criterion and RUL derivation feasibility.
- Missingness and data quality.
- Licence and required citation.
- Proposed train/calibration/validation/test grouping.

**Current evidence limitation:** This document is a desk audit based on official catalogue and repository descriptions. No raw dataset archive has yet been downloaded, parsed, counted or experimentally evaluated. Dataset suitability and final selection remain unconfirmed.

## 7. Sources

1. NASA, Li-ion Battery Aging Datasets: https://data.nasa.gov/dataset/li-ion-battery-aging-datasets
2. NASA, PCoE Data Set Repository: https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/
3. NASA, Randomized and Recommissioned Battery Dataset: https://data.nasa.gov/dataset/randomized-and-recommissioned-battery-dataset
4. CALCE, Battery Research Data: https://calce.umd.edu/data
5. Battery Data Commons, Find Data: https://batterydatacommons.org/find-data/
