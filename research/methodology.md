# Working Methodology

**Status:** Provisional protocol. Final decisions depend on literature review and dataset audit.

## Phase 1 — Literature review

Review work on:
- Lithium-ion degradation mechanisms and measurable ageing indicators.
- SOH estimation and RUL prediction.
- Physics-informed / physics-guided machine learning for battery systems.
- Generalisation across cells, temperatures, and cycling regimes.
- Predictive uncertainty, calibration, and distribution shift.
- Evaluation protocols and data leakage in time-series and grouped data.

For each paper, record the research question, data, chemistry (if stated), split strategy, method, metrics, limitations, and relevance. Verify DOI and publication metadata from publisher or trusted indexing records. Do not infer details from abstracts where the full method is needed.

## Phase 2 — Dataset audit

For each candidate source:
1. Record source URL, download date, version/file name, licence or terms, and citation requirements.
2. Identify cell IDs, chemistry where documented, temperature, current, voltage, cycle count, and capacity/diagnostic fields.
3. Inspect missingness, sampling frequency, inconsistent units, and data quality.
4. Establish whether SOH is directly supplied or must be derived. Document the reference capacity and formula.
5. Establish an RUL definition and end-of-life threshold only where justified by the source and research question.
6. Decide whether a meaningful cell-held-out or condition-held-out test can be created.

Do not combine datasets until compatibility is demonstrated and justified.

## Phase 3 — Data preparation

- Preserve raw source data unchanged outside version control.
- Keep a data dictionary and transformation log.
- Create deterministic preprocessing scripts.
- Split by cell or another defensible grouping unit before fitting scalers, imputers, feature selectors, or other learned transforms.
- Prevent future-cycle information from leaking into features for a prediction made at an earlier cycle.
- Record exclusions and missing-data handling.

## Phase 4 — Baselines

Choose baselines after the data audit. Candidate families may include:
- Persistence or simple trend baseline, where meaningful.
- Linear or regularised regression.
- Random forest / gradient boosting.
- SVR.
- Neural sequence methods only if data volume and split size justify them.

Tune models using training/validation data only. Keep a final test set untouched until evaluation.

## Phase 5 — Physics-guided modelling

Translate any physical assumption into a clearly stated mathematical or algorithmic constraint. Check that the assumption is valid for the chemistry, operating regime, target, and temporal window. Consider a baseline-versus-guided ablation. Report whether the constraint improves or harms performance; do not assume improvement.

## Phase 6 — Uncertainty estimation

Possible methods include:
- Ensembles.
- Quantile regression.
- Conformal prediction.

Select methods based on the prediction task and available validation data. Evaluate empirical coverage and interval width on held-out data. Discuss whether calibration holds under cell or operating-condition shifts. State any assumptions required by each method.

## Phase 7 — Evaluation

### Point prediction
Report MAE and RMSE. Use R² only with clear definition and appropriate interpretation for the target and split.

### Uncertainty
Report prediction interval coverage and width, and appropriate calibration diagnostics. Include sample counts and subgroup breakdowns where possible.

### Generalisation
Define the hold-out protocol before model fitting. Potential settings include:
- Unseen-cell evaluation.
- Unseen-temperature evaluation.
- Unseen cycling-profile evaluation.

Do not claim a condition is unseen if related observations or derived statistics were used during training or model selection.

### Reproducibility
Record:
- Dataset version and provenance.
- Cell IDs and split assignments.
- Feature definitions and preprocessing.
- Model/configuration and hyperparameters.
- Random seeds and software environment.
- Metrics, plots, and run identifiers.

## Phase 8 — Software demonstrator

Only integrate methods that have reproducible implementations. The application should expose dataset/model provenance, input validation, predictions, and uncertainty information where supported. Clearly label estimates as research outputs, not safety-certified BMS decisions.

## Decision gates

- **Gate A:** Research gap supported by a verified literature matrix.
- **Gate B:** Dataset and target definitions documented and defensible.
- **Gate C:** Leakage-resistant baseline evaluation completed.
- **Gate D:** Proposed method and ablations specified before final testing.
- **Gate E:** Uncertainty and generalisation claims supported by measured evidence.
- **Gate F:** Software demonstrator tested on documented examples.
