# Research Gap — Evidence-Based Revision

**Status: preliminary candidate, not a novelty claim.** Last reviewed 8 November 2026.

## Original broad idea rejected

The original concept combined physics-guided SOH/RUL prediction, unseen-cell/condition generalisation, and uncertainty calibration. The 2023–2026 literature already contains hybrid Bayesian physics-informed prognosis, PINN SOH estimation, domain generalisation, cross-cell physics-guided SOH with conformal UQ, and RUL uncertainty-calibration studies. Simply combining these elements is not novel.

## Evidence

| Study | Evidence | Implication |
|---|---|---|
| Nascimento et al. (2023), https://doi.org/10.1038/s41598-023-33018-0 | Hybrid Bayesian physics-informed battery prognosis | Bayesian + physics-guided is prior art |
| Wang et al. (2024), https://doi.org/10.1038/s41467-024-48779-z | PINN SOH with multiple datasets, small-sample and transfer experiments | Physics-guided SOH transfer is prior art |
| Chen et al. (2024), https://doi.org/10.1016/j.jpowsour.2024.234696 | Domain-generalisation SOH on unknown domains | Unseen-domain SOH is prior art |
| Chen et al. (2026), https://doi.org/10.3390/batteries12090340 | Physics-guided/domain-aware cross-cell SOH plus split conformal UQ; LOCO on NASA B0005/B0006/B0007 | Very close overlap; original framing is not novel |
| Wu et al. (2026), https://doi.org/10.3390/a19070535 | Early-life RUL UQ, conformal methods and a later shifted test | Early RUL UQ under shift is already studied |
| Trustworthy RUL UQ (2026), https://doi.org/10.1016/j.est.2026.122408 | Evidential UQ and RUL prediction intervals | Generic trustworthy RUL UQ is prior art |
| Rizanov et al. (2026), https://doi.org/10.3390/batteries12070255 | Review of 176 works and multi-fidelity validation | Trustworthy/transferable validation is actively reviewed |

## Candidate gap to test

Conduct an independent, controlled benchmark of how physics-guided constraints and uncertainty-calibration strategies behave together under explicitly defined low-data and out-of-domain battery evaluation protocols.

Potential comparison:
- Matched data-driven baseline vs physically guided variant.
- Selected uncertainty methods (ensembles, quantile regression, split/adaptive conformal) after feasibility review.
- In-domain vs leave-one-cell-out and compatible cross-dataset/condition hold-outs.
- Pre-defined training-data budgets.
- Point error, interval coverage, interval width/sharpness, calibration diagnostics, and physically justified degradation-consistency metrics.

## Draft gap statement — not approved

"Although physics-guided battery health estimation, domain adaptation, and uncertainty quantification have each been investigated, recent studies indicate that predictive-interval calibration may remain sensitive to cell-level and operating-domain shift. This study will conduct a controlled, leakage-resistant evaluation of the interaction between physics-guided constraints, data availability, and uncertainty calibration across explicitly held-out cells and compatible datasets."

This must be revised or rejected after full-text screening and citation tracking. Do not claim novelty until the closest papers have been read in full and their splits, calibration sets, cell counts, and limitations compared.
