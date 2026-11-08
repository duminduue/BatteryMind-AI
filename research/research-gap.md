# Research Gap — Evidence Log

**Status: OPEN / NOT YET ESTABLISHED**

This file is a structured workspace, not a claim that a research gap has already been proven.

## Working problem area

Reliable battery SOH and RUL prediction when labelled data are limited and test cells or operating conditions differ from training data.

## Candidate gap dimensions to investigate

1. Whether reported improvements from physics-guided models persist under cell-held-out and condition-held-out tests.
2. Whether uncertainty estimates remain calibrated under cell or operating-condition distribution shift.
3. Whether physically motivated constraints improve data efficiency without imposing invalid assumptions on non-monotonic or protocol-dependent observations.
4. Whether studies compare methods using compatible datasets, label definitions, and leakage-resistant splits.
5. Whether a practical trade-off among accuracy, calibration, data needs, and computational cost is adequately quantified.

These are questions for investigation, not confirmed gaps.

## Evidence required before claiming novelty

For each relevant paper, record:
- Exact bibliographic reference and DOI or stable publisher URL.
- Publication status and year.
- Dataset(s), chemistry, cell count, and operating conditions.
- SOH/RUL label definitions.
- Train/validation/test split design.
- Whether cells and conditions are held out.
- Physics prior/constraint and how it is implemented.
- Uncertainty method and calibration evaluation.
- Main results and limitations.
- What remains untested relative to this project's proposed scope.

## Gap statement template

"Prior studies have investigated [verified methods] using [verified datasets/protocols]. However, the reviewed evidence indicates that [specific, bounded limitation], particularly under [clearly defined test setting]. This project therefore investigates [specific method/question] and evaluates it using [predefined protocol and metrics]."

Do not complete this statement until the literature matrix contains sufficient verified evidence.

## Decision log

| Date | Decision / observation | Evidence | Status |
|---|---|---|---|
| 2026-11-08 | Working direction selected: physics-guided, data-efficient, uncertainty-calibrated prediction under unseen conditions | Project planning discussion; literature verification pending | Provisional |
