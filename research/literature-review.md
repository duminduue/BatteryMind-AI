# Literature Review — Battery SOH and RUL Prediction (2022–2026)

**Review status:** Initial evidence-based screening, 8 November 2026. This is not yet a completed systematic review. Some publisher pages provide abstracts and selected full-text sections; where the full methods or supplementary files were not inspected, the record is explicitly marked as abstract-level.

## 1. Scope and search concepts

The review focuses on:
- Lithium-ion battery state-of-health (SOH) estimation and remaining useful life (RUL) prediction.
- Physics-informed / physics-guided and hybrid physics-data methods.
- Predictive uncertainty quantification (UQ), interval calibration, and uncertainty decomposition.
- Early-life prediction, data efficiency, cross-cell evaluation, and operating-condition shift.

Search concepts included combinations of: lithium-ion battery, SOH, RUL, physics-informed, physics-guided, Bayesian, Gaussian process, uncertainty quantification, conformal prediction, calibration, cross-cell, domain adaptation, and distribution shift.

## 2. Screened studies

### 2.1 Physics-based modelling + ML for degradation diagnostics (2022)

**Title:** Integrating physics-based modeling and machine learning for degradation diagnostics of lithium-ion batteries.  
**Venue:** Energy Storage Materials, 50 (2022), 668–695.  
**DOI:** https://doi.org/10.1016/j.ensm.2022.05.047

**Evidence from publisher abstract:** The study proposes and tests two lightweight physics-informed ML methods for online capacity estimation and diagnosis of primary degradation modes, using limited early-life experimental degradation data. The motivation is that capacity-only SOH does not identify lifecycle stage or degradation modes, while detailed physics-based diagnostics can require long-term cycling data and high computation.

**Methodology known from accessible record:** Two lightweight physics-informed ML approaches; degradation-mode diagnosis and capacity estimation. Exact architecture, dataset split, chemistry/cell count, and detailed metrics require full-text extraction.

**Research relevance:** Establishes that combining physics-based information and ML for battery degradation diagnosis predates the current project. Generic "physics + ML" novelty is therefore not defensible.

**Evidence level:** Publisher abstract / metadata.  
**Source:** https://www.sciencedirect.com/science/article/pii/S2405829722002999

### 2.2 Early RUL uncertainty with Transformer ensemble (2024)

**Authors:** Jijuan Hu and Lifeng Wu.  
**Title:** Early Uncertainty Quantification Prediction of Lithium-Ion Battery Remaining Useful Life With Transformer Ensemble Model.  
**Venue:** IEEE Transactions on Transportation Electrification, 10(4), 8618–8629 (2024).  
**DOI:** https://doi.org/10.1109/TTE.2024.3354302

**Evidence from IEEE abstract:** CNN and denoising-autoencoder Transformer features are combined to learn local and global degradation information. A two-stage ensemble training strategy uses stochastic weight averaging and cosine annealing. Quantile regression is used for RUL uncertainty estimation. With the first 80 cycles, the reported MAPE is 9.23% on a similar-distribution primary test set and 10.52% on a dissimilar-distribution secondary test set.

**Important limitation for our review:** The accessible IEEE record does not expose the complete dataset identity, detailed split design, interval calibration metrics, or full ablation tables. These must be checked in the full paper before making stronger claims.

**Research relevance:** Early-life RUL, distribution mismatch, and quantile-based uncertainty are already studied. Our work must go beyond simply applying quantile regression to battery RUL.

**Evidence level:** Publisher abstract and metadata.  
**Source:** https://ieeexplore.ieee.org/document/10400491/

### 2.3 Physics-guided prior + heteroscedastic GPR (2026)

**Authors:** Jianqiu Wang, Yongtai He, Dongling Pu, and Xiaodan Wang.  
**Title:** Lithium-ion battery remaining useful life prediction via physics-driven prior and heteroscedastic Gaussian process regression.  
**Venue:** Journal of Electronic Measurement and Instrumentation, 40(1), 102–109 (2026); online 27 March 2026 according to the journal record.

**Evidence from journal abstract:** A three-segment empirical capacity-degradation model supplies a physics-based prior. A two-stage heteroscedastic GPR models residual mean and input-dependent variance. A TreeBagger random-forest regressor refines the mean, and beta calibration scales prediction intervals. The study reports leave-one-battery-out evaluation on NASA B0005, B0006, B0007, and B0018; reported R² exceeds 0.93 for all cells, while nominal 90% interval coverage is reported between 70% and 92%, with MPIW 0.085–0.10 Ah.

**Critical interpretation:** The reported 70–92% coverage range is not uniformly equal to the nominal 90% level. The exact calibration procedure, whether calibration data are independent of test cells, and per-cell results must be checked in the full paper. The abstract's claim of "reliable 90% coverage" should not be repeated without that check.

**Research relevance:** This is a direct and recent overlap with physics priors, heteroscedastic uncertainty, and leave-one-battery-out validation on NASA cells. It strongly narrows the space for a generic physics-guided + UQ contribution.

**Evidence level:** Journal abstract and issue metadata.  
**Source:** https://jemi.etmchina.com/jemien/article/issue/2026_40_1

### 2.4 Physics-informed Bayesian sampling for battery prognostics (2025)

**Title:** Uncertainty-aware deep learning with physics-informed bayesian sampling for lithium-ion battery prognostics.  
**Venue:** Applied Energy, 402, Part A, article 126880 (15 December 2025).  
**DOI:** https://doi.org/10.1016/j.apenergy.2025.126880

**Evidence from publisher abstract/highlights:** The work combines Bayesian multi-source domain adaptation with a physics-informed NUTS sampling algorithm to respond to operational changes. It reports explainable health indicators from selected charge-data segments and addresses heterogeneous training data and different battery chemistries.

**Information still required:** Authors, exact dataset names and sizes, split protocol, chemistry-specific results, uncertainty calibration metrics, computational cost, and ablation details must be verified from the full article.

**Research relevance:** Physics-informed Bayesian UQ and domain adaptation across chemistry/operating variation are already active topics by 2025. A proposal to merely combine those components would overlap substantially.

**Evidence level:** Publisher abstract/highlights.  
**Source:** https://www.sciencedirect.com/science/article/pii/S0306261925016101

### 2.5 History-agnostic Bayesian neural network for SOH/RUL (2026)

**Authors:** Elaheh Sadat Ahmadi Mousavi, Farzaneh Abdollahi, Farshad Barazandeh, Farschad Torabi, and Amin Hajizadeh.  
**Title:** History-Agnostic Lithium-Ion Batteries State of Health and Remaining Useful Life Estimation Using Fusion-Based Bayesian Neural Network.  
**Venue:** IET Renewable Power Generation; first published 22 June 2026.  
**DOI:** https://doi.org/10.1049/rpg2.70297

**Evidence from publisher full-text page (abstract):** Four new dV/dt-based health indicators are fused with six established indicators from a single charge-discharge cycle. Two BNNs separately predict SOH and RUL and provide uncertainty estimates. Validation uses the Oxford battery degradation dataset and leave-one-out cross-validation. The abstract reports SOH R² above 0.998 and MAE below 0.002 across test cells, and direct RUL R² above 0.97 with MAPE as low as 8.5%.

**Research relevance:** Single-cycle / history-agnostic prediction and Bayesian uncertainty are relevant alternatives to long-history sequence models. The Oxford dataset and leave-one-out protocol are important to examine. The reported scores must be interpreted in light of sample size, cell count, target definition, and split design.

**Evidence level:** Publisher full-text page, including abstract and introduction; complete method/results still need detailed extraction.  
**Source:** https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/rpg2.70297

### 2.6 Trustworthy RUL with SMoE-LSTM and evidential uncertainty (2026)

**Title:** Towards trustworthy lithium-ion battery remaining useful life prediction with uncertainty quantification.  
**Venue:** Journal of Energy Storage, volume 167, article 122408 (30 July 2026).  
**DOI:** https://doi.org/10.1016/j.est.2026.122408

**Evidence from publisher record and accessible article text:** A sparsely gated mixture-of-experts LSTM (SMoE-LSTM) models multi-stage degradation. Deep evidential regression with a Normal-Inverse-Gamma prior is used to produce RUL and separate aleatoric/epistemic uncertainty in one forward pass. The study reports validation on the MIT-Stanford dataset, average RMSE 16.11 and R² 0.9821, and compares its efficiency with sampling/ensemble UQ approaches.

**Research relevance:** Efficient uncertainty decomposition and adaptive expert models are already explored. A proposed contribution based solely on fast uncertainty output or aleatoric/epistemic decomposition would not be novel.

**Evidence level:** Publisher record and accessible article text; complete experimental tables and dataset details still need verification.  
**Source:** https://www.sciencedirect.com/science/article/pii/S2352152X26020724

### 2.7 Physics-informed explainable hybrid SOH/RUL (2026)

**Authors:** Plamen Stanchev and Nikolay Hinov.  
**Title:** Physics-Informed Explainable Machine Learning for Hybrid State of Health and Remaining Useful Life Estimation of Lithium-Ion Batteries.  
**Venue:** Batteries, 12(10), 401 (published 6 October 2026).  
**DOI:** https://doi.org/10.3390/batteries12100401

**Evidence from publisher abstract:** A multi-cell degradation simulation represents capacity fade, resistance growth, thermal/operational stress, and nonlinear ageing acceleration. Hybrid SOH combines capacity- and resistance-related health information. EOL/RUL use an 80% capacity-retention criterion. Evaluation includes cell-wise and leave-one-cell-out validation; right-censored cells are excluded from exact RUL error calculations. The paper reports simulation-based results and explicitly states that independent experimental validation is still needed.

**Research relevance:** Hybrid SOH, physics-informed explainability, leave-one-cell-out tests, and simulated distribution shift are already covered. The simulation-only nature and lack of independent experimental validation are explicit limitations, but do not by themselves establish a new research gap for our project.

**Evidence level:** Publisher abstract.  
**Source:** https://www.mdpi.com/2313-0105/12/10/401

### 2.8 Short-transient SOH with probabilistic physics-informed trend model (2026)

**Title:** A two-stage probabilistic framework with validity screening and physics-informed trend modeling for lithium-ion battery health estimation from short discharge transients.  
**Venue:** Journal of Energy Storage, volume 169, article 122763 (15 August 2026).  
**DOI:** https://doi.org/10.1016/j.est.2026.122763

**Evidence from publisher abstract:** The framework estimates SOH from short initial discharge-transient windows. It uses a two-stage validity screen and a physics-informed Gaussian process with a linear trend plus residual process. Out-of-distribution inflation widens uncertainty intervals under distribution shift. The publisher highlights leakage-safe cross-cell testing and reports accuracy, uncertainty, and prediction availability.

**Research relevance:** Short-window SOH estimation, validity screening, physics-informed probabilistic trends, OOD interval widening, and leakage-safe cross-cell evaluation are already being addressed. This is a particularly close overlap with a generic proposal about cross-cell calibrated uncertainty.

**Evidence level:** Publisher abstract/highlights.  
**Source:** https://www.sciencedirect.com/science/article/pii/S2352152X26024278

## 3. Synthesis: what is already established

The screened evidence indicates that the following are not novel in isolation:
- Physics-informed / physics-guided ML for battery capacity, SOH, degradation diagnosis, or RUL.
- Bayesian, Gaussian-process, ensemble, quantile, and evidential uncertainty methods.
- Early-life battery RUL prediction with uncertainty.
- Cross-cell or leave-one-cell/battery-out evaluation.
- Domain adaptation or evaluation under distribution mismatch.
- Physics-guided probabilistic trend models and interval widening under OOD conditions.
- Explainable and hybrid SOH/RUL frameworks.

## 4. Candidate research opportunities — hypotheses, not established gaps

Potentially worthwhile directions to test against a broader review include:

1. **Calibration under realistic grouped shift:** Compare uncertainty methods using strict cell-held-out and condition-held-out protocols, while distinguishing interpolation, extrapolation, and cross-dataset transfer. Check whether the calibration data are genuinely independent of test cells.
2. **Data-efficiency versus calibration trade-off:** Measure how performance and interval calibration change as the number of training cells or early-life cycles is reduced. This requires enough independent cells; a large number of cycles from a few cells is not a substitute.
3. **Selective prediction / abstention:** Investigate whether models can identify inputs for which estimates are unreliable and abstain or widen intervals, evaluated with coverage-risk and availability measures. First establish how recent battery papers handle this.
4. **Dataset shift and label harmonisation:** Study how differing chemistry, protocol, sampling, and EOL definitions affect claims of cross-dataset generalisation. This may be a methodological contribution if it exposes a reproducible evaluation failure.

None of these is claimed as novel yet. Search more broadly and inspect full papers before selecting one.

## 5. Major review limitations

- This is a targeted initial screening, not a PRISMA-compliant systematic review.
- Search results and accessible publisher pages were used; some publisher full texts were blocked or only abstracts were accessible.
- Several papers require full-text extraction of datasets, cell counts, splits, metrics, calibration protocols, and ablations.
- No claim is made that all relevant 2022–2026 papers have been found.
- The research gap remains **open**.

## 6. Immediate next actions

1. Obtain and read full texts for the eight screened studies where accessible.
2. Extract exact dataset identities, cell counts, chemistry, target definitions, train/validation/test protocol, and calibration metrics.
3. Search additional 2022–2026 studies on conformal prediction, domain generalisation, early-life RUL, and cross-dataset validation.
4. Audit NASA and CALCE files before locking the experimental design.
5. Write a bounded gap statement only after evidence comparison is complete.


### 2.9 SMoE-LSTM with deep evidential uncertainty (2026)

**Authors:** Zhibin Zhao, Mingqi Feng, Qiuyu Yu, Hongming Yuan, Fujin Wang, and Zhi Zhai.  
**Title:** Towards trustworthy lithium-ion battery remaining useful life prediction with uncertainty quantification.  
**Venue:** Journal of Energy Storage, 167, article 122408 (30 July 2026).  
**DOI:** https://doi.org/10.1016/j.est.2026.122408

**Evidence from publisher abstract and accessible introductory/contribution text:** A sparsely-gated mixture-of-experts LSTM (SMoE-LSTM) is used to model multi-stage degradation. Deep evidential regression with a Normal-Inverse-Gamma (NIG) prior outputs RUL and decomposed aleatoric/epistemic uncertainty in one forward pass. The paper reports validation on the MIT-Stanford dataset, average RMSE 16.11 and R² 0.9821, and claims improved calibration and inference efficiency relative to MC Dropout and ensemble methods.

**Critical questions:** The accessible record does not fully establish independent cell counts, chemistry, EOL/RUL units, cell-wise split design, nominal interval coverage, calibration metrics, OOD testing, or per-condition results. A single-pass evidential output does not by itself prove calibration. Expert activation is a diagnostic view, not automatically a causal explanation.

**Research relevance:** Mixture-of-experts sequence modelling, NIG evidential regression, aleatoric/epistemic decomposition, and sampling-free UQ are already applied to battery RUL. These components alone cannot be claimed as novel.

**Evidence level:** Publisher abstract and accessible introductory/contribution text; full experimental tables and supplementary material still require extraction.  
**Detailed analysis:** [Paper 03 analysis](../literature/paper-analysis/2026-smoe-lstm-evidential-uq.md)  
**Source:** https://www.sciencedirect.com/science/article/pii/S2352152X26020724

