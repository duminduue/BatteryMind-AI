# Research Gap — Evidence Log

**Status: OPEN / NOT ESTABLISHED (updated 2026-11-08)**

## Working problem area

Reliable lithium-ion battery SOH/RUL prediction with limited labelled ageing data and transfer to cells or operating conditions not represented during model development.

## 1. Findings from initial literature screening

The following research components already exist in the 2022–2026 literature:

- Physics-informed ML for capacity estimation and degradation-mode diagnosis (2022): https://doi.org/10.1016/j.ensm.2022.05.047
- Early-life RUL prediction with Transformer ensembles and quantile uncertainty (2024): https://doi.org/10.1109/TTE.2024.3354302
- Physics-informed Bayesian sampling, domain adaptation, and UQ (2025): https://doi.org/10.1016/j.apenergy.2025.126880
- Physics-driven capacity prior + heteroscedastic GPR + interval calibration + NASA leave-one-battery-out testing (2026): Journal of Electronic Measurement and Instrumentation 40(1), 102–109.
- Bayesian neural network SOH/RUL from single-cycle health indicators (2026): https://doi.org/10.1049/rpg2.70297
- SMoE-LSTM with evidential uncertainty decomposition (2026): https://doi.org/10.1016/j.est.2026.122408
- Physics-informed explainable hybrid SOH/RUL and cell-wise validation (2026): https://doi.org/10.3390/batteries12100401
- Short-transient SOH with physics-informed probabilistic trend, OOD interval inflation, and leakage-safe cross-cell tests (2026): https://doi.org/10.1016/j.est.2026.122763

## 2. Implication

The original combination "physics-guided AI + uncertainty quantification + unseen operating conditions" is too broad to be presented as novel. Several studies already address close combinations. The project must not claim novelty from combining these labels.

## 3. Candidate directions requiring further verification

| Candidate | What must be tested in literature | Feasibility concern |
|---|---|---|
| Calibration under strict cell/condition shift | Whether recent methods use independent calibration cells and genuinely unseen conditions; compare calibration validity and coverage-risk | Public datasets may contain too few independent cells |
| Data-efficiency versus uncertainty calibration | Whether studies jointly vary training-cell count / early-life window and report calibration, not only point error | Number of independent cells may be small |
| Selective prediction / abstention | Whether battery SOH/RUL models quantify reliability when abstaining on OOD or high-risk inputs | Requires defensible OOD definition and availability metrics |
| Cross-dataset transfer and label harmonisation | Whether differences in chemistry, protocol, capacity reference, and EOL thresholds are handled consistently | Datasets may not be directly comparable |

These are research hypotheses, not confirmed gaps.

## 4. Evidence required before claiming novelty

For every close paper, verify:
- Full bibliographic metadata and publication status.
- Dataset(s), chemistry, number of independent cells, and operating conditions.
- SOH and RUL definitions, including EOL threshold and censoring.
- Training, validation, calibration, and test split units.
- Whether cells and conditions are truly unseen.
- Whether calibration is performed without test-set leakage.
- Uncertainty method, nominal levels, empirical coverage, interval width, and calibration diagnostics.
- Ablation results, computational cost, and limitations.

## 5. Provisional gap statement template

"Although prior work has investigated [verified methods], it remains unclear whether [precisely bounded issue] holds under [specific, independently defined evaluation setting]. This study therefore tests [specific hypothesis] using [dataset and split protocol], measuring [predefined point and uncertainty metrics]."

Do not complete this statement until the full-paper and dataset audits are complete.

## 6. Decision log

| Date | Decision / observation | Evidence | Status |
|---|---|---|---|
| 2026-11-08 | Generic physics-guided + UQ + cross-cell combination is not a defensible novelty claim | Initial screening of 2022–2026 studies listed in literature-review.md | Confirmed by screened overlap; broader search pending |
| 2026-11-08 | Candidate gap directions: strict-shift calibration, data-efficiency/calibration trade-off, selective prediction, cross-dataset label harmonisation | Initial paper and dataset screening | Hypotheses only |
