# Research Questions — Revised Working Set

**Status:** Provisional; subject to full-text screening and dataset feasibility.

## Main question

How do physics-guided constraints and predictive-uncertainty methods affect the accuracy, calibration, and physical consistency of lithium-ion battery SOH/RUL estimates when training data are limited and evaluation cells or datasets are held out?

## Sub-questions

- **RQ1 — Baselines:** How do selected baseline SOH/RUL models perform under cell-aware and out-of-domain evaluation?
- **RQ2 — Physics guidance:** Does a clearly specified, physically justified constraint improve accuracy or degradation consistency against a matched data-driven baseline?
- **RQ3 — Uncertainty:** How do selected uncertainty methods compare in interval coverage, interval width/sharpness, and calibration?
- **RQ4 — Shift:** How do point prediction and uncertainty calibration change between in-domain, leave-one-cell-out, and compatible cross-dataset/condition-held-out settings?
- **RQ5 — Data efficiency:** How sensitive are these outcomes to pre-defined training-data budgets?

## Candidate hypotheses

- H1: The effect of physics guidance depends on dataset and evaluation domain; improvement must not be assumed.
- H2: Nominal uncertainty coverage may deteriorate under cell/domain shift, with variation across methods.
- H3: Lower training-data budgets may change the relative performance of physics-guided and data-driven models.
- H4: Better point accuracy does not necessarily imply better uncertainty calibration.

## Operational definitions required before experiments

SOH reference capacity and formula; RUL unit and EOL threshold; input window and prediction horizon; cell/domain split; data-budget levels; calibration-data availability; nominal interval levels and metrics; and a physically justified degradation-consistency metric.

Null, negative, and dataset-dependent results are valid outcomes.
