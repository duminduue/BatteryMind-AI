# P10 — Wu et al. (2026)

**Title:** Uncertainty-Aware Early Battery Life Prediction with Composite-Kernel Gaussian Process Regression and Conformalized Adaptive Intervals  
**Venue:** Algorithms, 19(7), 535  
**DOI:** https://doi.org/10.3390/a19070535  
**Status:** Publisher page and abstract checked; full-text protocol extraction pending.

## Method reported
The study compares ten uncertainty-quantification configurations for early-cycle RUL prediction. Methods include Bayesian-native uncertainty, split conformal prediction, jackknife+, bootstrap and conformalized adaptive intervals. The core predictor is a composite-kernel Gaussian process using RBF and white-noise kernels.

## Data and evaluation reported
MIT-Stanford dataset with 124 cells. The abstract describes a primary test set and a secondary test set collected one year later.

## Critical questions
- Is the secondary test a genuine cell-held-out, temporal, or acquisition-domain shift?
- Which cells are used to fit calibration parameters?
- Is coverage evaluated per cell or only pooled?
- Are intervals calibrated under each domain or transferred from source calibration?

## Relevance
Directly relevant to early-life RUL and calibration under distribution shift. This topic already has 2026 prior art.
