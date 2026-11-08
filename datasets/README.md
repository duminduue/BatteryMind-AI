# Dataset Register and Data Governance

**No raw dataset is currently approved or stored in this repository.**

## Candidate-source register

| Candidate source | Initial purpose | Status |
|---|---|---|
| NASA lithium-ion battery ageing data | Candidate for cycling-based degradation and RUL/SOH investigation | Audit required |
| CALCE battery data (University of Maryland) | Candidate for complementary battery ageing data and operating-condition analysis | Audit required |

## Required audit fields

For every downloaded collection, record:
- Official dataset landing page and direct file/source reference.
- Provider, version, access/download date.
- Licence, terms of use, redistribution restrictions, and required citation.
- File inventory and checksums where practical.
- Chemistry and cell identifiers, only as explicitly documented.
- Temperature, current, voltage, cycle protocol, and diagnostic measurements.
- Units, sampling rules, missingness, and known limitations.
- Capacity reference, SOH formula, and RUL/EOL definition.
- Which cells and conditions are suitable for each evaluation split.

## Data handling rules

- Do not commit large raw files to Git by default.
- Do not upload data whose licence or terms do not permit redistribution.
- Keep raw, processed, and generated result data separate.
- Keep scripts and metadata needed to reproduce preprocessing.
- Store download instructions and checksums where permitted.
- Consider Git LFS or DVC only after the storage, privacy, licensing, and reproducibility requirements are clear.

## Dataset decision record

Do not select a primary dataset until the audit confirms that its data fields and test structure support the research questions.
