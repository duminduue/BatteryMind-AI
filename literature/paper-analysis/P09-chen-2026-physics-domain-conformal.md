# P09 — Chen et al. (2026)

**Title:** Physics-Consistent Domain-Aware SOH Estimation for Cross-Cell Battery Health Prediction  
**Venue:** Batteries, 12(9), 340  
**DOI:** https://doi.org/10.3390/batteries12090340  
**Status:** Publisher page and abstract checked; full-text extraction still required.

## Method reported by the publisher
- Physics-guided health-indicator feature screening.
- Cycle-aware soft covariance alignment.
- Monotonicity-constrained LightGBM regression.
- Split conformal uncertainty quantification.

## Data and evaluation reported
NASA B0005, B0006 and B0007; leave-one-cell-out cross-cell evaluation.

## Reported findings
The abstract reports average RMSE improvement across tested cells and a stronger improvement on the more difficult B6 target. It also explicitly states that uncertainty intervals are not fully calibrated under severe domain shift and that broader validation on larger, more heterogeneous datasets is required.

## Critical appraisal
This is very close to the original BatteryMind AI concept. Its three-cell NASA evaluation is a narrow basis for broad claims, but this must be checked in the full article. Determine whether its conformal calibration set is drawn from source or target cells, whether coverage is marginal or conditional, and how severe shift is defined.

## Relevance
Essential closest-prior-art paper. It invalidates a broad novelty claim around simply combining physics-guided cross-cell SOH with conformal UQ.
