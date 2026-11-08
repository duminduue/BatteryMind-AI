# Comparative Critical Analysis — Papers 01–03

**Project:** BatteryMind AI  
**Research focus:** Physics-guided, data-efficient and uncertainty-calibrated battery health prediction under unseen operating conditions  
**Status:** Preliminary evidence-based comparison. This is not a full-text systematic review and none of the methods has been independently reproduced.

## 1. Purpose

This comparison examines three recent approaches to battery prognostics:

1. Oyewole et al. (2025): uncertainty-aware deep learning with physics-informed Bayesian sampling.
2. Wang et al. (2026): physics-driven capacity prior with heteroscedastic Gaussian process regression.
3. Zhao et al. (2026): sparsely-gated mixture-of-experts LSTM with deep evidential regression.

The objective is not to select a winner from headline metrics. It is to identify what each architecture attempts to solve, what evidence is currently available, and which methodological questions remain unresolved.

## 2. Side-by-side comparison

| Dimension | Paper 01 — Oyewole et al. (2025) | Paper 02 — Wang et al. (2026) | Paper 03 — Zhao et al. (2026) |
|---|---|---|---|
| Main task | SOH estimation and RUL prediction | Battery prognostics using capacity degradation | RUL prediction |
| Main architecture | Bayesian multi-source domain adaptation; physics-informed NUTS; standalone GRU for RUL | Three-segment empirical capacity prior; two-stage heteroscedastic GPR; TreeBagger mean refinement | Sparsely-gated Mixture-of-Experts LSTM (SMoE-LSTM) |
| Physics / domain knowledge | Physics-informed Bayesian sampling; charge-data health indicators | Explicit empirical capacity-trend prior representing degradation stages | Adaptive expert fusion for multi-stage patterns; no explicit electrochemical constraint established from accessible text |
| Uncertainty approach | Bayesian sampling / posterior inference | Input-dependent variance from heteroscedastic GPR; beta calibration reported | Deep evidential regression with Normal-Inverse-Gamma (NIG) prior |
| Dataset evidence | Multiple public accelerated-aging datasets; exact dataset inventory needs full-paper verification | NASA cells B0005, B0006, B0007 and B0018 | MIT–Stanford dataset |
| Evaluation evidence | Abstract-level claims of robustness across conditions and chemistries; exact split protocol not yet verified | Leave-one-battery-out (LOBO) reported | Dataset validation reported; exact independent-cell split protocol requires full-text verification |
| Reported metrics | Exact comparable headline metrics not extracted in this review | R² > 0.93; nominal 90% PICP reported as 70–92%; MPIW 0.085–0.10 Ah | Average RMSE 16.11; R² = 0.9821 |
| Key strength | Explicitly targets domain adaptation and uncertainty under heterogeneous conditions | Transparent degradation prior and a cross-battery evaluation design | Models multi-stage degradation and produces two uncertainty components in one forward pass |
| Main unresolved issue | Whether posterior uncertainty remains calibrated under genuinely unseen chemistries/conditions and limited target-cell data | Reported 90% interval coverage varies down to 70%; calibration and small-sample reliability need scrutiny | Evidential uncertainty decomposition does not by itself establish empirical calibration; cell-wise independence and OOD performance need verification |

## 3. Critical analysis by paper

### Paper 01 — Oyewole et al. (2025)

**What it contributes**

The paper combines Bayesian multi-source domain adaptation with physics-informed NUTS sampling. The abstract describes health indicators extracted from charge-data segments and a standalone GRU used for RUL prediction from estimated SOH and health indicators. Its stated motivation is to improve prognostics when in-service batteries have limited historical data and when training data vary across operating conditions and chemistries.

**Questions that must be checked in the full paper**

- Which exact datasets, cell chemistries, cell counts and operating profiles were used?
- Are test cells completely excluded from pre-training and source-domain training?
- How is target-domain information used during adaptation? Is it available at deployment?
- Does the evaluation include a genuinely unseen chemistry, or only a different profile within represented chemistries?
- How is uncertainty calibrated and evaluated (coverage, interval width, calibration error, or proper scoring rules)?
- What is the computational cost of NUTS and is it compatible with the claimed online use case?

**Preliminary assessment**

This is the most directly relevant of the three papers to domain adaptation under heterogeneous battery populations. However, claims of generalisation should not be accepted until the split design and target-domain access are known. Bayesian sampling provides a principled posterior representation, but a posterior distribution is not automatically calibrated under distribution shift.

### Paper 02 — Wang et al. (2026)

**What it contributes**

The method first fits a three-segment empirical capacity model corresponding to early, accelerated and linear degradation stages. It models residuals using a two-stage heteroscedastic GPR, adds a TreeBagger refinement to the mean prediction, and reports beta calibration of predictive intervals. The abstract reports LOBO evaluation on NASA cells B0005, B0006, B0007 and B0018.

**Important evidence**

The abstract reports R² above 0.93 for all four cells. It also reports a nominal 90% prediction-interval coverage probability (PICP) between 70% and 92%, with MPIW between 0.085 and 0.10 Ah.

**Critical interpretation**

- LOBO is a stronger test of cell-level transfer than randomly splitting cycle records, provided all preprocessing and calibration are fitted without access to the held-out battery.
- A 90% interval achieving only 70% empirical coverage on some evaluation cases is evidence of under-coverage, not uniformly reliable 90% coverage.
- The abstract says beta calibration is applied on the training set. The exact calibration protocol and whether a separate calibration set is used must be inspected.
- The NASA set contains a small number of cells in this experiment. Four-cell LOBO evidence cannot establish broad generalisation across chemistries, manufacturers or real-world operating profiles.
- The target definition and exact RUL conversion procedure must be verified before comparing its metrics with deep-learning papers.

**Preliminary assessment**

This paper provides a useful, relatively interpretable baseline for BatteryMind AI. Its reported coverage range also motivates a rigorous calibration audit rather than relying on a single average metric.

### Paper 03 — Zhao et al. (2026)

**What it contributes**

The paper combines a sparsely-gated mixture of LSTM experts to model multi-stage degradation with deep evidential regression using a Normal-Inverse-Gamma prior. The publisher text describes a single forward pass that estimates RUL and decomposes uncertainty into aleatoric and epistemic components. The reported MIT–Stanford dataset results are average RMSE 16.11 and R² 0.9821.

**Questions that must be checked in the full paper**

- What is the exact number of cells, chemistry, operating conditions and RUL label definition?
- Are data partitions separated by cell, rather than by overlapping rolling windows or cycles from the same cell?
- Are reported uncertainty intervals evaluated using empirical coverage and width across cells and operating regimes?
- Is calibration assessed on held-out calibration data, or only on the test set used for reporting?
- Are expert activations stable and meaningfully associated with degradation regimes, or are they only internal routing weights?
- Does the model retain calibration when tested on unseen cells or operating conditions?

**Preliminary assessment**

The architecture offers an attractive efficiency argument compared with repeated sampling or multiple-model ensembles. Nevertheless, single-pass inference is a computational advantage, not proof of calibrated uncertainty. Likewise, expert routing can be inspected, but it should not be described as a physical explanation without independent evidence.

## 4. Cross-paper synthesis: what can fail, and why?

| Potential failure condition | Paper 01: Bayesian adaptation | Paper 02: Phys + GPR | Paper 03: SMoE-LSTM + evidential UQ |
|---|---|---|---|
| New chemistry absent from training | Domain adaptation may help, but posterior and transfer evidence must be verified | Empirical prior may not transfer if degradation shape changes | Expert network may extrapolate poorly outside learned degradation patterns |
| Very few early-life cycles | Transfer learning is designed for limited target history; minimum required history needs quantification | Prior may help constrain extrapolation, but uncertainty may remain large | Sequence model may be sensitive to short or incomplete histories; verify early-cycle results |
| Abrupt operating-condition shift | Bayesian adaptation may respond if target observations are available | Heteroscedastic variance may reflect input-dependent noise but does not guarantee OOD detection | Evidential uncertainty may become overconfident under shift unless explicitly tested |
| Poor interval calibration | Bayesian posterior needs empirical calibration checks | Abstract-reported 90% PICP spans 70–92% | NIG evidential output requires empirical coverage and calibration testing |
| Small number of independent cells | Multi-source training could help, depending on source diversity | Four NASA cells limit external validity | Dataset cell count and cell-independent split need verification |
| Real-time deployment | NUTS sampling may be computationally demanding; measure latency | GPR and ensemble refinement may scale with training size; measure latency | Single-pass inference is promising, but measure end-to-end latency and memory |

This table is a set of methodological risks to test, not a claim that each method has already been shown to fail in every listed condition.

## 5. Implications for BatteryMind AI

The comparison suggests that simply combining physics guidance, uncertainty quantification and a neural network would not be a defensible novelty claim. Each of these elements already appears in recent battery prognostics literature.

A stronger research direction is to investigate the **reliability of uncertainty estimates under strict cell-level and operating-condition shift**, while explicitly controlling data access and calibration.

Candidate experimental questions:

1. Does uncertainty remain calibrated when the test cell is fully excluded from model fitting, preprocessing, feature selection and calibration?
2. How does calibration degrade as the amount of early-life data is reduced?
3. Can a lightweight calibration or selective-prediction mechanism reduce unsafe overconfidence under unseen operating conditions?
4. Does physics-guided trend information improve worst-cell performance, not merely average accuracy?
5. What is the trade-off between prediction accuracy, interval coverage, interval width, abstention rate and inference cost?

These are candidate questions, not yet a confirmed research gap. A broader literature and dataset audit is still required.

## 6. Proposed minimum evaluation protocol

For a credible study, consider the following protocol after dataset feasibility is confirmed:

- **Unit of separation:** split by complete battery cell, never by randomly mixing cycles/windows from the same cell across train and test.
- **Outer evaluation:** leave-one-cell-out or grouped cell-level testing, subject to sufficient independent cells.
- **Condition shift:** where metadata permits, hold out an operating condition or profile as an additional test domain.
- **Calibration separation:** use training cells for model fitting, separate calibration cells for calibration, and untouched test cells for final evaluation. If the dataset is too small, report this limitation and use nested/grouped validation without leaking test information.
- **Accuracy:** MAE, RMSE and R², reported per cell and as aggregate statistics.
- **Uncertainty:** empirical PICP/coverage at multiple nominal levels, mean interval width, calibration curves and a proper probabilistic score where appropriate.
- **Robustness:** evaluate early-history length, noise, missing measurements and condition shift separately.
- **Efficiency:** report inference latency, peak memory and model size under a stated hardware environment.
- **Reproducibility:** publish cell IDs, split manifests, preprocessing rules, random seeds and metric code.

## 7. Current conclusion and next research task

No final research gap should be claimed from these three papers alone. The most useful next step is to obtain and audit the full experimental details of all three papers, then conduct a dataset feasibility audit. In particular, verify the exact split and calibration protocols before designing a new model.

**Evidence limitation:** Paper 01 and Paper 03 comparisons currently rely on publisher abstracts and accessible publisher text. Paper 02 details currently rely mainly on the publisher abstract and issue record. Full-text extraction and independent reproduction have not been completed.

## References

1. Oyewole, I., Hassanieh, W., Chelbi, M. and Chehade, A. (2025). *Uncertainty-aware deep learning with physics-informed bayesian sampling for lithium-ion battery prognostics*. Applied Energy, 402, 126880. https://doi.org/10.1016/j.apenergy.2025.126880
2. Wang, J., He, Y., Pu, D. and Wang, X. (2026). *Lithium-ion battery remaining useful life prediction via physics-driven prior and heteroscedastic Gaussian process regression*. Journal of Electronic Measurement and Instrumentation, 40(1), 102–109. Publisher record: https://jemi.etmchina.com/jemien/article/abstract/B2508549
3. Zhao, Z., Feng, M., Yu, Q., Yuan, H., Wang, F. and Zhai, Z. (2026). *Towards trustworthy lithium-ion battery remaining useful life prediction with uncertainty quantification*. Journal of Energy Storage, 167, 122408. https://doi.org/10.1016/j.est.2026.122408
