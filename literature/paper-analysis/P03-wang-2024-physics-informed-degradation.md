# P03 — Wang et al. (2024)

**Title:** Physics-informed neural network for lithium-ion battery degradation stable modeling and prognosis  
**Venue:** Nature Communications, 15, 4332  
**DOI:** https://doi.org/10.1038/s41467-024-48779-z  
**Open access:** CC BY 4.0, subject to article-specific third-party material notices.  
**Status:** Publisher/PubMed metadata and abstract checked; detailed split audit pending.

## Method
The paper models degradation attributes using empirical degradation and state-space equations, with neural networks capturing degradation dynamics. It extracts statistical features from a short period before full charge.

## Data
The abstract reports 55 newly generated NCM batteries and a combined evaluation involving three other datasets, totalling 387 batteries and 310,705 samples.

## Reported results
The abstract reports MAPE of 0.87% and regular, small-sample and transfer experiments. These are author-reported values; do not compare them directly with other papers without matching target, split, chemistry and metrics.

## Critical questions
- Are cells independent across train/test in every experiment?
- How are the three external datasets partitioned?
- Is transfer adaptation supervised, unsupervised or label-free in each setting?
- Are prediction intervals produced or calibrated?
- How robust are results to chemistry and protocol changes?

## Relevance
Strong prior art for physics-guided SOH, small-sample experiments and transfer evaluation. It substantially narrows the novelty space.
