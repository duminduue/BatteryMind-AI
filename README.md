# BatteryMind AI

**Physics-Guided and Uncertainty-Aware AI for Lithium-Ion Battery Health Prediction and Remaining Useful Life Estimation**

BatteryMind AI is a research and software project investigating reliable, data-efficient prediction of lithium-ion battery health and remaining useful life (RUL). The project focuses on physics-guided machine learning, evaluation under changing or unseen operating conditions, and uncertainty-aware predictions.

> **Research status:** This repository is an active research workspace. Research gaps, model choices, dataset suitability, and performance claims remain subject to literature review and experimental validation. No model performance or novelty claim is asserted at this stage.

## Research direction

The working research direction is:

**Physics-guided, data-efficient, and uncertainty-calibrated battery health prediction under unseen operating conditions.**

The project will investigate whether incorporating physically meaningful constraints and calibrated predictive uncertainty can improve the reliability and generalisation of data-driven battery health estimates. The precise contribution will be defined only after a critical review of existing work.

## Objectives

1. Review recent research on lithium-ion battery degradation, state-of-health (SOH) estimation, RUL prediction, physics-guided learning, domain generalisation, and uncertainty quantification.
2. Identify and document suitable public battery ageing datasets and their usage conditions.
3. Establish reproducible preprocessing and leakage-resistant evaluation protocols.
4. Implement and compare appropriate statistical and machine-learning baselines.
5. Investigate physics-guided approaches and uncertainty estimation methods where supported by the evidence and data.
6. Evaluate performance and reliability across cells and operating conditions, including carefully defined unseen-condition tests.
7. Develop a software platform for data exploration and model inference after the research pipeline is established.

## Planned outputs

- A traceable literature review and research-gap analysis.
- Dataset provenance, schema, and preprocessing documentation.
- Reproducible notebooks and experiment configurations.
- Baseline and proposed model implementations.
- Evaluation results, including point-error and uncertainty-calibration metrics where applicable.
- A software demonstration and research manuscript.

## Repository structure

```text
research/       Research proposal, questions, methodology, gap analysis
literature/     Literature matrix and individual paper notes
datasets/       Dataset documentation and download instructions (not raw data)
notebooks/      Reproducible exploratory and modelling notebooks
src/            Reusable research and modelling code
experiments/    Experiment configurations and run records
models/         Model definitions and documented artefacts
software/       Application and API implementation
results/        Generated metrics, figures, and analysis summaries
docs/           Technical and user documentation
```

## Candidate datasets

NASA lithium-ion battery ageing data and CALCE battery data are **candidate sources**, not yet final selections. Before using any dataset, record its exact source, version, licence/terms, cell identifiers, chemistry (where documented), test conditions, measurement schema, and suitability for SOH/RUL labelling. Do not assume datasets are interchangeable.

Raw datasets are not committed to this repository by default. Follow each provider's access and redistribution conditions. Use documented download instructions or an appropriate data-versioning mechanism when needed.

## Method overview

1. Literature review and research-gap verification.
2. Dataset provenance and exploratory analysis.
3. Data quality checks, preprocessing, and feature engineering.
4. Baseline implementation and leakage-resistant validation.
5. Physics-guided model investigation.
6. Predictive uncertainty and calibration investigation.
7. Cross-cell and operating-condition evaluation.
8. Reproducible reporting and software integration.

See [research/methodology.md](research/methodology.md) for the working protocol.

## Evaluation principles

- Split data at the cell or other scientifically defensible group level where appropriate; avoid leakage between training and test observations.
- Define SOH and end-of-life/RUL labels explicitly for each dataset.
- Report the evaluation split, cell identities, operating conditions, and preprocessing fit boundaries.
- Use metrics appropriate to the target, such as MAE and RMSE for point predictions and interval coverage/width or calibration diagnostics for uncertainty.
- Do not present results as evidence of real-world EV-pack performance without appropriate external validation.

## Reproducibility and research integrity

- Record random seeds, software versions, configuration files, and dataset versions.
- Keep raw data, processed data, and generated results distinguishable.
- Never fabricate experimental results, citations, dataset properties, or validation outcomes.
- Distinguish published evidence, experimental observations, and hypotheses.
- Document negative and inconclusive findings.

## Technology direction

The initial research stack is expected to use Python, NumPy, pandas, SciPy, scikit-learn, and appropriate deep-learning libraries such as PyTorch. XGBoost, SHAP, and uncertainty-quantification tools may be introduced when justified. The planned application stack may include FastAPI and a React/Next.js interface. Final choices will follow the research requirements rather than being treated as fixed commitments.

## Project status

**Current phase:** Research foundation and literature review.

The project is not yet at a stage where model accuracy, superiority, or publication readiness can be claimed.

## Licence

The repository currently includes the licence selected during repository creation. Dataset licences and third-party software licences remain separate and must be respected.
