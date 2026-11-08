# Research Questions and Hypotheses

**Status:** Provisional; revise after literature and dataset audits.

## Research questions

- **RQ1:** How accurately do suitable baseline models estimate SOH and RUL on the selected battery ageing data under leakage-resistant evaluation?
- **RQ2:** Do selected physically motivated constraints improve performance, data efficiency, or generalisation in the defined evaluation setting?
- **RQ3:** How well do selected uncertainty methods calibrate predictive intervals for SOH and RUL?
- **RQ4:** How do models perform on cells or operating conditions excluded from model development?
- **RQ5:** What trade-offs exist among accuracy, uncertainty calibration, compute cost, and implementation complexity?

## Testable hypotheses (to refine)

- **H1:** A physically guided model may improve one or more predefined performance measures relative to a matched baseline under a specified data regime.
- **H2:** An uncertainty-aware approach can provide intervals with empirically measurable coverage and width on held-out data.
- **H3:** Performance and calibration may deteriorate under selected cell or operating-condition shifts; the extent must be measured.

These hypotheses are deliberately non-directional about guaranteed improvement. Null or negative results are valid research outcomes.

## Operational definitions needed

Before experiments, define:
- SOH reference capacity and calculation.
- RUL unit (cycles, time, or another unit).
- End-of-life criterion and its source-specific justification.
- Prediction horizon and available input window.
- Cell/condition grouping for each split.
- What constitutes an unseen condition.
- Calibration metric(s) and nominal interval levels.
