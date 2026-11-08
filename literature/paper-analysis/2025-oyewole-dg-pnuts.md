# Paper Analysis: DG-PNUTS for Battery Prognostics (2025)

## Bibliographic record
- **Title:** Uncertainty-aware deep learning with physics-informed bayesian sampling for lithium-ion battery prognostics
- **Authors:** Isaiah Oyewole, Wael Hassanieh, Meriam Chelbi, Abdallah Chehade
- **Venue:** Applied Energy, Volume 402, article 126880 (15 December 2025)
- **DOI:** https://doi.org/10.1016/j.apenergy.2025.126880
- **Evidence status:** Publisher metadata and abstract inspected. Full text could not be retrieved in this review session (publisher access returned HTTP 403). The detailed points below are therefore limited to publisher abstract/highlights and corroborating bibliographic metadata.

## Research problem
The authors identify challenges in data-driven SOH/RUL prognostics under dynamic operating conditions, heterogeneous degradation patterns, limited historical data, and inadequate uncertainty quantification.

## Method reported by the source
1. A dual-GRU architecture is used for SOH-related modelling.
2. Multiple GRUs are trained on subgroups of aged battery data (divide-and-conquer) to capture heterogeneous degradation.
3. Bayesian multi-source domain adaptation transfers pretrained knowledge to in-service batteries with limited history.
4. A physics-informed No-U-Turn Sampler (NUTS), an adaptive MCMC algorithm, is used for posterior inference and uncertainty quantification.
5. A standalone GRU predicts RUL using estimated SOH and extracted health indicators.

**Important:** The abstract does not expose the exact physics-informed likelihood/prior equations, network dimensions, feature list, optimiser, hyperparameters, calibration procedure, or detailed split protocol. These must be checked in the full paper before reproducing the method.

## Dataset and evaluation
- The abstract states validation on multiple publicly available accelerated-ageing datasets.
- Exact dataset names, cell counts, chemistry, train/validation/test assignments, and metrics are not specified in the accessible abstract.
- Do not infer these details or claim cross-chemistry performance independently verified until the full paper is inspected.

## Reported contribution
The paper combines subgroup-specific GRU modelling, Bayesian multi-source domain adaptation, and physics-informed NUTS-based posterior inference for uncertainty-aware SOH/RUL prognostics.

## Critical appraisal — what remains to verify
1. What physical knowledge is encoded in NUTS (prior, likelihood, constraints, or another mechanism)?
2. Are uncertainty intervals evaluated for empirical coverage and sharpness, and on genuinely held-out cells/conditions?
3. How is domain adaptation performed without target-test leakage?
4. How many cells and independent ageing trajectories support each subgroup?
5. Are chemistry and operating-condition transfers evaluated separately?
6. What is the computational cost of MCMC at inference time?
7. Are ablations reported for physics-informed sampling, domain adaptation, and subgroup GRUs independently?

## Relevance to BatteryMind AI
This paper is directly relevant and prevents us from claiming that physics-informed Bayesian inference plus domain adaptation and UQ is itself novel.

## Possible distinction to investigate (not an established gap)
A rigorous, controlled comparison of uncertainty calibration and selective prediction under predefined cell-held-out and operating-condition-shift protocols, with strict separation of adaptation, calibration, and final test data. This must first be checked against the full paper and related literature.

## Reproduction status
**Not reproduced.** Full text and exact experimental details are still required.

## Sources
- Publisher page: https://www.sciencedirect.com/science/article/pii/S0306261925016101
- DOI: https://doi.org/10.1016/j.apenergy.2025.126880
