# Individual Paper Analysis Notes

This index summarises the first eight screened studies. These are structured screening notes, not substitutes for reading and annotating each complete paper. Where only the publisher abstract or highlights were accessible, that limitation is stated.

## Detailed critical appraisals

- [Oyewole et al. (2025) — DG-PNUTS](2025-oyewole-dg-pnuts.md)
- [Physics-driven prior + heteroscedastic GPR (2026)](2026-physics-prior-heteroscedastic-gpr.md)
- [SMoE-LSTM + deep evidential regression (2026)](2026-smoe-lstm-evidential-uq.md)

These two records are **abstract-level analyses** because full text was not accessible during this review. They identify what must be checked in the full article; they are not full-text reviews or reproductions.

## P01 — 2022: Physics-based modelling + ML for degradation diagnostics

**Title:** Integrating physics-based modeling and machine learning for degradation diagnostics of lithium-ion batteries  
**Venue:** Energy Storage Materials, 50 (2022), 668–695  
**DOI:** https://doi.org/10.1016/j.ensm.2022.05.047

**Problem:** Capacity-only SOH estimates do not necessarily identify lifecycle stage or the degradation modes causing capacity fade. Detailed physics-based diagnostics can require long-term data and be computationally expensive.

**Method (publisher abstract):** Two lightweight physics-informed ML methods for online capacity estimation and primary degradation-mode diagnosis using limited early-life experimental degradation data.

**Dataset/splits/results:** Exact dataset, chemistry, cell count, split, and detailed metrics were not exposed in the accessible abstract. Full-text extraction required.

**Relevance:** Physics-informed ML for battery degradation diagnostics predates this project; "physics + ML" is not a sufficient novelty claim.

**Evidence:** Publisher abstract and metadata only.

## P02 — 2024: Early RUL uncertainty with Transformer ensemble

**Authors:** Jijuan Hu; Lifeng Wu  
**Title:** Early Uncertainty Quantification Prediction of Lithium-Ion Battery Remaining Useful Life With Transformer Ensemble Model  
**Venue:** IEEE Transactions on Transportation Electrification, 10(4), 8618–8629 (2024)  
**DOI:** https://doi.org/10.1109/TTE.2024.3354302

**Problem:** Early-life RUL estimation has weak degradation signals and deterministic estimates may be overconfident.

**Method (IEEE abstract):** CNN + denoising-autoencoder Transformer features; two-stage ensemble training; stochastic weight averaging with cosine annealing; quantile regression for uncertainty.

**Results:** Using the first 80 cycles, reported MAPE is 9.23% on a similar-distribution primary test set and 10.52% on a dissimilar-distribution secondary test set.

**Dataset/splits still to verify:** Dataset identity, cell count, cell grouping, interval coverage, and calibration protocol are not available in the accessible abstract.

**Relevance:** Early-life prediction, quantile UQ, and distribution-mismatch testing already exist.

**Evidence:** Publisher abstract and metadata.

## P03 — 2025: Physics-informed Bayesian sampling

**Title:** Uncertainty-aware deep learning with physics-informed bayesian sampling for lithium-ion battery prognostics  
**Venue:** Applied Energy, 402, Part A, 126880 (15 December 2025)  
**DOI:** https://doi.org/10.1016/j.apenergy.2025.126880

**Method (publisher highlights/abstract):** Bayesian multi-source domain adaptation; physics-informed NUTS sampling to adapt to operational changes; explainable health indicators from selected charge-data segments; addresses heterogeneous data and different chemistries.

**Full-text extraction required:** Authors, exact datasets, chemistry, cell counts, source domains, split protocol, uncertainty calibration, ablations, and compute cost.

**Relevance:** Close overlap with the initial broad proposal combining physics, Bayesian UQ, domain adaptation, and heterogeneous conditions.

**Evidence:** Publisher abstract/highlights.

## P04 — 2026: Physics prior + heteroscedastic GPR

**Authors:** Jianqiu Wang; Yongtai He; Dongling Pu; Xiaodan Wang  
**Title:** Lithium-ion battery remaining useful life prediction via physics-driven prior and heteroscedastic Gaussian process regression  
**Venue:** Journal of Electronic Measurement and Instrumentation, 40(1), 102–109 (2026)  
**Journal issue record:** https://jemi.etmchina.com/jemien/article/issue/2026_40_1  
**Online date:** 27 March 2026

**Method (journal abstract):** Three-segment empirical capacity prior; two-stage heteroscedastic GPR for residual mean and input-dependent variance; TreeBagger random forest mean refinement; beta calibration for prediction intervals.

**Dataset/split:** NASA cells B0005, B0006, B0007, B0018; leave-one-battery-out cross-validation.

**Results:** R² above 0.93 for all four cells; PICP reported from 70% to 92% for nominal 90% intervals; MPIW 0.085–0.10 Ah.

**Critical interpretation:** The coverage range includes undercoverage relative to nominal 90%. Full calibration method and separation of calibration/test cells must be checked.

**Relevance:** Direct overlap with physics priors, heteroscedastic uncertainty, NASA cells, and cross-battery validation.

**Evidence:** Journal abstract and issue metadata.

## P05 — 2026: History-agnostic Bayesian SOH/RUL

**Authors:** Elaheh Sadat Ahmadi Mousavi; Farzaneh Abdollahi; Farshad Barazandeh; Farschad Torabi; Amin Hajizadeh  
**Title:** History-Agnostic Lithium-Ion Batteries State of Health and Remaining Useful Life Estimation Using Fusion-Based Bayesian Neural Network  
**Venue:** IET Renewable Power Generation; first published 22 June 2026  
**DOI:** https://doi.org/10.1049/rpg2.70297

**Method (publisher page):** Four dV/dt-derived health indicators fused with six established indicators from a single charge-discharge cycle; separate BNNs directly predict SOH and RUL with UQ.

**Dataset/split:** Oxford battery degradation dataset; leave-one-out cross-validation.

**Results:** Abstract reports SOH R² > 0.998 and MAE < 0.002; direct RUL R² > 0.97 and MAPE as low as 8.5%.

**Critical interpretation:** Need exact cell count, target definition, leave-one-out unit, feature availability, and calibration metrics to interpret high scores.

**Relevance:** Single-cycle health indicators and history-agnostic Bayesian prediction are established alternatives to long-history sequence models.

**Evidence:** Publisher full-text page, abstract and introduction; detailed extraction pending.

## P06 — 2026: SMoE-LSTM with evidential uncertainty

**Title:** Towards trustworthy lithium-ion battery remaining useful life prediction with uncertainty quantification  
**Venue:** Journal of Energy Storage, 167, 122408 (30 July 2026)  
**DOI:** https://doi.org/10.1016/j.est.2026.122408

**Method (accessible article text):** Sparsely gated mixture-of-experts LSTM for multi-stage degradation; deep evidential regression with Normal-Inverse-Gamma prior; one-pass RUL and aleatoric/epistemic uncertainty estimates.

**Dataset/results:** MIT-Stanford dataset; publisher record reports average RMSE 16.11 and R² 0.9821.

**Full-text extraction required:** Cell count, chemistry, split, RUL definition, calibration metrics, interval coverage, and compute comparisons.

**Relevance:** Efficient uncertainty estimation and uncertainty decomposition are already studied.

**Evidence:** Publisher record and accessible article text; full experiment extraction pending.

## P07 — 2026: Physics-informed explainable hybrid SOH/RUL

**Authors:** Plamen Stanchev; Nikolay Hinov  
**Title:** Physics-Informed Explainable Machine Learning for Hybrid State of Health and Remaining Useful Life Estimation of Lithium-Ion Batteries  
**Venue:** Batteries, 12(10), 401 (published 6 October 2026)  
**DOI:** https://doi.org/10.3390/batteries12100401

**Method (publisher abstract):** Multi-cell degradation simulation with capacity fade, resistance growth, thermal/operational stress and nonlinear ageing; hybrid capacity/resistance SOH; 80% capacity-retention EOL; cell-wise and leave-one-cell-out evaluation; right-censoring treatment; bootstrap and simulated distribution-shift tests; explainability.

**Results:** Gradient Boosting SOH RMSE 0.340 percentage points and R² 0.9979; Random Forest RUL RMSE 239.5 cycles and R² 0.9278.

**Critical limitation:** The authors explicitly state independent experimental validation is needed for transferability to physical systems. These are simulation-based results and should not be directly compared with experimental NASA/CALCE results.

**Evidence:** Publisher abstract.

## P08 — 2026: Short-transient probabilistic SOH under shift

**Title:** A two-stage probabilistic framework with validity screening and physics-informed trend modeling for lithium-ion battery health estimation from short discharge transients  
**Venue:** Journal of Energy Storage, 169, 122763 (15 August 2026)  
**DOI:** https://doi.org/10.1016/j.est.2026.122763

**Method (publisher abstract):** Short initial discharge-transient windows; two-stage validity screening; physics-informed Gaussian process with linear trend plus residual process; OOD interval inflation; leakage-safe cross-cell testing with accuracy, uncertainty, and availability.

**Full-text extraction required:** Dataset, chemistry, cell count, validity rules, split and calibration separation, OOD construction, interval metrics, and ablations.

**Relevance:** Very close overlap with short-window SOH, probabilistic physics-guided modelling, cross-cell evaluation, and OOD-aware intervals.

**Evidence:** Publisher abstract/highlights.

---

## Cross-paper synthesis

The screened evidence shows that physics-guided learning, Bayesian/GPR/quantile/evidential UQ, early-life prediction, cross-cell validation, domain adaptation, and OOD interval handling are all already represented in recent battery prognostics literature.

The project must therefore identify a narrower, measurable limitation. Candidate directions are strict calibration under independent cell/condition shift, data-efficiency versus calibration trade-offs, selective prediction/abstention, and cross-dataset label harmonisation. None is confirmed novel yet.

## Required next step

Retrieve full texts and extract exact datasets, independent cell counts, chemistry, EOL/SOH definitions, training/calibration/test split units, calibration metrics, ablations, and limitations. Do not treat abstract-only information as a complete methodological review.
