# Research Proposal — BatteryMind AI

## Working title

**Physics-Guided and Uncertainty-Aware Artificial Intelligence for Lithium-Ion Battery Health Prediction and Remaining Useful Life Estimation**

## 1. Background

Lithium-ion batteries are widely used in electric vehicles, stationary energy storage, and portable systems. Their capacity and power capability change with use and environmental conditions. Estimating battery state of health (SOH) and remaining useful life (RUL) is therefore important for maintenance, control, safety management, and lifecycle planning.

Data-driven approaches can learn degradation patterns from cycling and diagnostic data. However, their reliability may be affected by limited labelled data, differences between cells, changing operating conditions, measurement noise, and distribution shifts between training and deployment environments. A point prediction alone does not communicate how uncertain an estimate is.

Physics-guided machine learning and uncertainty quantification are active research areas. Their combination is not assumed to be novel by itself. The specific research contribution must be established through a critical and up-to-date literature review.

## 2. Problem statement

A model trained on a limited collection of laboratory battery ageing observations may produce unreliable SOH or RUL estimates when applied to different cells or operating conditions. There is a need to investigate methods that use physically meaningful information, make efficient use of available data, and communicate predictive uncertainty while being evaluated with rigorous leakage-resistant protocols.

The exact scope of the generalisation problem (for example, unseen cells, unseen temperatures, or unseen cycling regimes) will be selected after inspecting the candidate datasets and prior research.

## 3. Aim

To investigate and evaluate physics-guided and uncertainty-aware machine-learning methods for lithium-ion battery SOH and RUL prediction, with emphasis on data efficiency and reliability under appropriately defined unseen operating conditions.

## 4. Objectives

1. Conduct a critical literature review of battery degradation, SOH estimation, RUL prediction, physics-guided ML, domain generalisation, and uncertainty calibration.
2. Verify candidate datasets, data access conditions, measurement variables, cell identities, and target-label definitions.
3. Design reproducible preprocessing, feature engineering, and data-splitting procedures that minimise leakage.
4. Establish suitable baseline models.
5. Investigate physically motivated constraints or hybrid approaches that are supported by the data and literature.
6. Investigate predictive uncertainty methods and assess their calibration.
7. Compare approaches using transparent, repeatable experiments across selected cells and conditions.
8. Build a software demonstrator based on validated research components.
9. Prepare a research manuscript that reports methods, results, limitations, and reproducibility information.

## 5. Research questions

- **RQ1:** How well do suitable baseline models estimate SOH and RUL on the selected battery ageing datasets under leakage-resistant evaluation?
- **RQ2:** Under what conditions, if any, do physically motivated constraints improve prediction accuracy, data efficiency, or generalisation?
- **RQ3:** How reliably can selected uncertainty-estimation methods quantify prediction uncertainty for SOH and RUL?
- **RQ4:** How do the investigated methods perform when evaluated on cells or operating conditions excluded from model development?
- **RQ5:** What are the practical trade-offs among predictive performance, calibration, computational cost, and implementation complexity?

These questions are provisional and will be refined after dataset inspection and literature review.

## 6. Scope

The initial study is a computational investigation using appropriately documented public battery ageing datasets. It will focus on cell-level SOH and RUL estimation. Pack-level deployment, online BMS integration, safety certification, and claims about field performance are outside the initial scope unless separately validated.

## 7. Candidate datasets

- NASA lithium-ion battery ageing data.
- CALCE battery data from the University of Maryland.

These are candidate sources only. Dataset selection requires checking the exact downloadable files, terms of use, chemistry, cell IDs, test profiles, sensor/measurement fields, capacity or health labels, and whether a defensible RUL target can be derived.

## 8. Proposed methodology

1. **Literature review:** Search and screen relevant peer-reviewed studies; verify bibliographic metadata and group work by research question and method.
2. **Dataset audit:** Document provenance, access terms, cell-level structure, operating conditions, measurement quality, and target construction.
3. **Exploratory analysis:** Inspect cycling trajectories, capacity trends, missing data, irregular sampling, and between-cell variation.
4. **Preprocessing:** Build reproducible transformations. Fit data-dependent transformations on training data only.
5. **Baselines:** Select simple and competitive models based on the dataset structure. Possible candidates include linear regression, random forests, support vector regression, gradient boosting, and neural sequence models where data volume supports them.
6. **Physics-guided investigation:** Evaluate explicit physical priors or constraints, for example physically plausible degradation trends, only where assumptions are defensible for the selected data and target. Document cases where monotonic constraints are not appropriate.
7. **Uncertainty investigation:** Consider ensembles, quantile regression, or conformal methods. Assess interval coverage and width and discuss calibration under distribution shift.
8. **Evaluation:** Use cell-aware or condition-aware splits. Report MAE/RMSE and suitable R² usage for point predictions; report interval coverage, width, and calibration measures for uncertainty. Include baselines and ablation studies.
9. **Software demonstrator:** Integrate validated preprocessing and inference into an application with clear provenance and model-version information.
10. **Reporting:** Publish reproducible configurations, limitations, and results without overstating generalisation.

## 9. Expected contributions

The intended outputs are:
- A reproducible comparison of selected SOH/RUL methods on clearly documented datasets.
- Evidence about the effect of selected physics-guided choices under the chosen experimental protocol.
- An evaluation of uncertainty quality, not only point-prediction error.
- An openly documented research pipeline and software demonstrator, subject to dataset and dependency licences.

These are intended contributions, not established findings.

## 10. Limitations and risk management

- Public laboratory datasets may not represent real-world EV pack behaviour.
- Some datasets may lack the variables needed for the intended physical constraints or uncertainty evaluation.
- Different datasets may use different chemistries, protocols, and end-of-life definitions.
- RUL labels can depend strongly on the chosen end-of-life threshold and available future observations.
- Small numbers of cells can make generalisation conclusions statistically weak.
- Model selection and tuning can cause leakage if cell or temporal boundaries are not respected.
- No physical battery experiments will be attempted without suitable supervision, safe equipment, and a documented test plan.

## 11. Indicative work plan

| Stage | Main activity | Exit evidence |
|---|---|---|
| 1 | Literature review | Verified literature matrix and gap statement |
| 2 | Dataset audit | Documented selected dataset and label definitions |
| 3 | Exploratory analysis | Reproducible data-quality and EDA report |
| 4 | Baseline models | Reproducible baseline metrics |
| 5 | Physics-guided methods | Defined method and ablation results |
| 6 | Uncertainty methods | Calibration and interval evaluation |
| 7 | Generalisation tests | Cell/condition hold-out results |
| 8 | Software demonstrator | Tested inference workflow |
| 9 | Research writing | Draft manuscript with limitations and reproducibility details |

The schedule will be converted to dated milestones after the dataset and research scope are fixed.

## 12. Research integrity

No novelty, model superiority, or publication outcome is guaranteed. Every citation must be checked against its original source. Every reported metric must be generated by a recorded experiment. Distinguish hypotheses, published findings, and this project's measured results.
