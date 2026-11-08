# Literature Review — Initial Evidence Synthesis (2022–2026)

**Search snapshot:** 8 November 2026  
**Status:** Initial scoping review, not yet a PRISMA systematic review. Search strings, screening criteria, and full-text extraction still need to be completed.  
**Evidence rule:** The notes below distinguish publisher/index metadata and abstract-level claims from full-text methodological appraisal. Where full text was inaccessible, details are explicitly marked as requiring verification.

## 1. Search scope

Core themes:
- Lithium-ion battery state-of-health (SOH) estimation and remaining useful life (RUL) prediction.
- Physics-informed / physics-guided machine learning and hybrid degradation models.
- Small-sample and transfer/domain adaptation/generalisation.
- Predictive uncertainty quantification (UQ), calibration, and prediction intervals.
- Validation across held-out cells, operating conditions, and datasets.

Searches used combinations of these terms across publisher pages, PubMed/PMC, IEEE Xplore, and scholarly search indexing. This is an initial discovery pass; it is not an exhaustive database search.

## 2. Initial paper set and synthesis

### A. Foundations: Bayesian prognosis and physics-informed learning

**Pugalenthi et al. (2022), “Remaining Useful Life Prediction of Lithium-Ion Batteries Using Neural Networks with Adaptive Bayesian Learning.”**  
DOI: https://doi.org/10.3390/s22103803  
The paper is an early relevant UQ/prognostics reference using neural networks with adaptive Bayesian learning for battery RUL. It provides a useful pre-2024 baseline for probabilistic battery prognosis. The exact network design, uncertainty outputs, dataset split, and calibration evaluation must be extracted from the full text before making detailed comparisons.

**Nascimento et al. (2023), “A framework for Li-ion battery prognosis based on hybrid Bayesian physics-informed neural networks.”**  
DOI: https://doi.org/10.1038/s41598-023-33018-0  
This work explicitly combines Bayesian and physics-informed neural-network ideas for battery prognosis. It is important evidence that physics-informed modelling and Bayesian uncertainty are not a new combination in this domain. Full-text extraction is required for the governing equations, uncertainty treatment, dataset and validation protocol.

**Wang et al. (2024), “Physics-informed neural network for lithium-ion battery degradation stable modeling and prognosis.” Nature Communications, 15, 4332.**  
DOI: https://doi.org/10.1038/s41467-024-48779-z  
The authors describe empirical degradation and state-space equations combined with neural networks to capture degradation dynamics. Their feature extraction uses a short pre-full-charge period. The paper reports a dataset of 55 NCM batteries and validation combined with three other datasets, totalling 387 batteries and 310,705 samples; reported MAPE is 0.87%. The article reports regular, small-sample and transfer experiments. This is a major prior-art reference: a generic “physics-informed battery SOH model that generalises” is not a defensible novelty claim. Full-text review is needed to understand exact split independence, transfer settings, and uncertainty coverage (not established by the abstract).

**“Physics-informed machine learning for battery degradation diagnostics: A comparison of state-of-the-art methods.” Energy Storage Materials, 68 (2024), 103343.**  
DOI: https://doi.org/10.1016/j.ensm.2024.103343  
The paper compares physics-informed ML methods for battery degradation diagnostics and discusses use of short-term ageing data to predict long-term degradation/component behaviour. It is a key review/comparison source for defining what counts as physics-informed guidance. The exact compared methods, data and evaluation should be extracted from the full text.

### B. Generalisation, transfer, and small-data methods

**Chen et al. (2024), “Domain generalization-based state-of-health estimation of lithium-ion batteries.” Journal of Power Sources, 610, 234696.**  
DOI: https://doi.org/10.1016/j.jpowsour.2024.234696  
The paper explicitly trains on known domains and predicts on an unknown domain, using source-domain mixing to increase diversity. This directly overlaps with the proposed unseen-domain evaluation. It means domain generalisation cannot be presented as a new idea in this project. Full-text extraction must establish the domain definitions, split protocol, and limits.

**Chen et al. (2024), “A self-attention knowledge domain adaptation network for commercial lithium-ion batteries state-of-health estimation under shallow cycles.” Journal of Energy Storage, 86, 111197.**  
DOI: https://doi.org/10.1016/j.est.2024.111197  
The publisher record describes a shallow-cycle SOH method using self-attention knowledge-domain adaptation and a domain-invariant feature module. This is relevant to partial/limited observations and transfer between domains. Dataset details and the exact adaptation protocol need full-text verification.

**“Physics-informed neural networks for small sample state of health estimation of lithium-ion batteries.” Journal of Energy Storage, 122 (2025), 116559.**  
DOI: https://doi.org/10.1016/j.est.2025.116559  
The publisher abstract describes a dynamic physical degradation model fused with a neural network (SPINN), with Huber loss and adaptive loss weighting, targeting small-sample SOH estimation. This directly overlaps with data-efficient physics-guided SOH modelling. Extract the precise sample budgets, comparison fairness, and validation splits before drawing conclusions.

**Li et al. (2025), “A cross-material lithium-ion battery state of health estimation method based on three-stage domain adaptation.” Energy (2025), 139376.**  
DOI: https://doi.org/10.1016/j.energy.2025.139376  
The publisher record describes a three-stage transfer-learning framework, health features from 25% SOC segments, and an interpolated domain for adaptation. It reports 0.75% RMSE with 5% target-domain labels. This is relevant evidence for cross-material transfer and low-label adaptation; exact test conditions and reproducibility need full-text checking.

### C. Joint SOH/RUL and multi-task physics-informed modelling

**“Physics-informed neural network for co-estimation of state of health, remaining useful life, and short-term degradation path in Lithium-ion batteries.” Applied Energy, 398 (2025), 126427.**  
DOI: https://doi.org/10.1016/j.apenergy.2025.126427  
The publisher record describes a gated multi-task framework for SOH, RUL and short-term degradation-path prediction, using a simplified transformer and output derivatives for physical insight. Joint SOH/RUL physics-informed prediction is therefore already represented in recent work. The exact dataset and validation design need full-text extraction.

**Zhang et al. (2026), “A time series physics-informed neural network framework for the state of health estimation of lithium-ion batteries.” Journal of Energy Storage (article 119549; published 10 January 2026).**  
DOI: https://doi.org/10.1016/j.est.2025.119549  
The abstract describes a dual-network time-series PINN, time-series feature extraction, and adaptive weighting of loss terms, evaluated on three public datasets. This reinforces that time-series PINN SOH estimation is established prior art.

### D. Uncertainty quantification and calibration under shift

**“Remaining Useful Life Prediction and Uncertainty Quantification with Multi-Branch Deep Networks and Probabilistic Calibration.” 2025 IEEE International Conference on Sensing, Diagnostics, Prognostics, and Control (conference held 21–23 November 2025; IEEE record added 28 January 2026).**  
DOI: https://doi.org/10.1109/SDPC68151.2025.11347806  
The IEEE abstract describes CNN/BiLSTM/Transformer feature fusion, snapshot ensembles and Monte Carlo dropout for uncertainty, and conformal prediction intervals. It reports experiments on C-MAPSS and A123 lithium-ion battery data. This is direct evidence that deep-network UQ and conformal intervals have already been applied to battery RUL. Full-text review is required to inspect battery-specific results and calibration assumptions.

**“Towards trustworthy lithium-ion battery remaining useful life prediction with uncertainty quantification.” Journal of Energy Storage, 167 (2026), 122408.**  
DOI: https://doi.org/10.1016/j.est.2026.122408  
The abstract describes an SMoE-LSTM approach with evidential regression using a normal-inverse-gamma prior, uncertainty decomposition and prediction intervals, validated on the MIT-Stanford dataset. This directly overlaps with trustworthy RUL prediction and UQ. Exact calibration protocol and any distribution-shift evaluation require full-text review.

**Wu et al. (2026), “Uncertainty-Aware Early Battery Life Prediction with Composite-Kernel Gaussian Process Regression and Conformalized Adaptive Intervals.” Algorithms, 19(7), 535.**  
DOI: https://doi.org/10.3390/a19070535  
The paper evaluates ten UQ configurations for early-cycle RUL prediction using 124 MIT-Stanford cells. It compares Bayesian UQ, split conformal prediction, jackknife+, bootstrap and conformalized adaptive intervals. The abstract reports a primary test and a secondary test collected one year later, with empirical interval coverage under the shift. This is particularly relevant to early-life, small-data uncertainty evaluation. Full-text review must verify whether the shifted test protocol is strictly independent and how calibration data are allocated.

**“A Probabilistic Data-Driven Ensemble Approach for Battery Remaining Useful Life (RUL) Prognostics.” Batteries (2026), 12(10), 390.**  
Publisher page: https://www.mdpi.com/2313-0105/12/10/390  
The abstract describes adaptive ensemble weighting and epistemic/aleatoric uncertainty across NASA PCoE, CALCE, MIT and XJTU data. It reports that temperature-scaling calibration transferred imperfectly to unseen cells (reported PICP@95% falling to 78.1% in that experiment). This is especially relevant evidence that calibration can deteriorate across cells. Verify full metadata and detailed protocol before citing specific numeric claims in a manuscript.

### E. Very recent direct overlap with the original project idea

**Chen et al. (2026), “Physics-Consistent Domain-Aware SOH Estimation for Cross-Cell Battery Health Prediction.” Batteries, 12(9), 340.**  
DOI: https://doi.org/10.3390/batteries12090340  
This paper combines physics-guided features, domain-aware alignment, monotonicity-constrained LightGBM and split conformal uncertainty quantification. It uses NASA B0005, B0006 and B0007 with leave-one-cell-out evaluation. Importantly, the abstract itself notes that uncertainty intervals are not fully calibrated under severe domain shift and calls for broader validation on larger, more heterogeneous datasets. This is a very close overlap with the originally proposed combination of physics guidance, cross-cell generalisation and conformal UQ. Therefore the original broad project framing is not novel.

**Rizanov et al. (2026), “Toward Trustworthy and Transferable SOH/RUL Estimation for Lithium-Ion Batteries: A Critical Review and Multi-Fidelity Validation Framework from Laboratory Cells to Real-World Packs.” Batteries, 12(7), 255.**  
DOI: https://doi.org/10.3390/batteries12070255  
This review synthesizes 176 works and frames trustworthiness in terms of observability, robustness, uncertainty calibration, transferability and deployment feasibility. It proposes a multi-fidelity validation path from cells to packs and fleet operation. Its existence means the project must not claim that trustworthy/transferable validation or cell-to-pack validation is itself an unexplored topic. The specific review taxonomy and proposed framework should be extracted in detail.

## 3. What the evidence says so far

1. Physics-informed battery SOH and degradation modelling is well established by 2023–2026.
2. Cross-cell/domain generalisation and transfer learning are already active research directions.
3. Bayesian, ensemble, evidential, Gaussian-process and conformal uncertainty methods have already been applied to battery SOH/RUL tasks.
4. Some 2026 studies directly combine physics-guided estimation, domain adaptation/generalisation and uncertainty quantification.
5. Recent evidence explicitly reports calibration weaknesses under severe cell/domain shift. This is a promising *specific evaluation problem*, not proof that no one has solved it.
6. A broad proposal to “combine physics-guided AI + uncertainty + unseen operating conditions” would be insufficiently differentiated.

## 4. Candidate refined research direction

A defensible next step is to investigate an **independent, controlled benchmark of predictive-interval calibration and degradation-physics consistency under cell-held-out and cross-dataset shift, with explicit low-data budgets**.

Potential research question:
> How do physics-guided constraints and alternative uncertainty-calibration strategies affect SOH/RUL error, interval coverage, interval width, and physical consistency when training data are limited and evaluation cells or datasets are held out?

This should initially be treated as an empirical benchmarking question, not as a claim of a new algorithm. A methodological contribution can be proposed only after full-text review establishes a precise unresolved limitation.

## 5. Major limitations of this initial review

- Discovery searches are not exhaustive and have not yet been run as a documented multi-database systematic search.
- Some papers were assessed from publisher abstracts or indexed records because full text was inaccessible.
- The 2026 literature is rapidly developing; online-first and issue publication dates can differ.
- Numeric results are author-reported and are not directly comparable across datasets, labels, splits or metrics.
- No paper should be used to substantiate a detailed implementation claim until its full methods and supplementary information are checked.

## 6. Next review tasks

1. Retrieve and read full text for the highest-priority papers: Wang et al. (2024); Chen et al. (2024, domain generalisation); Nascimento et al. (2023); Chen et al. (2026, physics-consistent domain-aware); Wu et al. (2026, conformal adaptive intervals); and the 2026 trustworthy RUL UQ paper.
2. Populate every row of the literature matrix with exact datasets, chemistry, cell counts, split protocol, UQ method, and metrics.
3. Search Scopus/Web of Science/IEEE Xplore/ScienceDirect/SpringerLink/Google Scholar with a saved search protocol and date.
4. Trace references and citations backward/forward to identify omitted studies from 2022 and 2023.
5. Only then freeze the research gap and experimental protocol.
