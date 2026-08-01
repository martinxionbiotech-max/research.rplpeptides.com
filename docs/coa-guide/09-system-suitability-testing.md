---
title: "System Suitability Testing (SST) in Peptide HPLC Analysis"
description: "System suitability testing for peptide HPLC: parameter definitions, USP <621> acceptance criteria, SST failure investigation, and links to method validation."
slug: system-suitability-testing
category: Quality Control
tags: [System Suitability, SST, HPLC, USP 621, Quality Control]
author: RPL Peptides Research Team
published: 2026-08-01
---

# System Suitability Testing (SST) in Peptide HPLC Analysis

System suitability testing (SST) confirms that the entire chromatographic system — pump, injector, column, and detector — is performing correctly on the day of analysis, before any batch sample is run. SST is the bridge between a validated method and a reliable purity result.

## What SST Is and Why It Exists

A validated method (see [HPLC Method Validation](08-hplc-method-validation.md)) proves the procedure works under controlled conditions. But instruments drift: columns age, lamps dim, mobile phases evaporate. SST is a set of checks run immediately before (and sometimes during) a batch sequence to confirm the system is still within the operating envelope defined during validation.

Under [USP <621>](06-usp-621-chromatography-guide.md) and ICH guidance, SST is mandatory for compendial procedures and best practice for all quantitative assays.

## The Five Core SST Parameters

| Parameter | Definition | Typical Acceptance Criterion |
|-----------|------------|------------------------------|
| Injection precision (RSD of area) | Repeatability of replicate injections of the standard | $\le$ 1.0% (assay) |
| Retention time RSD | Repeatability of retention times | $\le$ 0.5% |
| Tailing factor $T$ | Peak symmetry of the main peak | $\le$ 1.5 (or 2.0 for low-level peaks) |
| Resolution $R_s$ | Separation between the main peak and the nearest impurity | $\ge$ 1.5 (baseline separation) |
| Plate count $N$ | Column efficiency | $\ge$ 5,000–10,000 (method-specific) |
| Capacity factor $k'$ | Retention relative to void volume | $\ge$ 2.0 |

The exact limits are set by each method's validation data — tighter or looser values are defensible if demonstrated.

## Standard Acceptance Criteria in Detail

### Injection Precision (RSD of Peak Area)

$$\text{RSD (\%)} = \frac{s}{\bar{x}} \times 100$$

For five or six replicate injections of the reference standard, RSD of area must be $\le$ 1.0%. Poor precision indicates autosampler problems, air bubbles, or an unstable detector.

### Tailing Factor

$$T = \frac{W_{0.05}}{2f}$$

Where $W_{0.05}$ is the peak width at 5% of peak height and $f$ is the distance from the leading edge to the peak apex at that height. $T = 1.0$ is a perfectly symmetrical peak; $T \le 1.5$ is the common acceptance limit. See [Tailing Factor Explained](12-tailing-factor-explained.md).

### Resolution

$$R_s = \frac{2(t_{R2} - t_{R1})}{W_1 + W_2}$$

Where $W_1$ and $W_2$ are peak widths at baseline. $R_s \ge 1.5$ indicates baseline separation. See [Resolution in Chromatography](13-resolution-in-chromatography.md).

### Plate Count

$$N = 16 \left(\frac{t_R}{W}\right)^2$$

Where $W$ is the baseline peak width. Plate count is a sensitive indicator of column health — a drop of more than 20% from the validated value signals column degradation.

## SST Run Design

A typical SST protocol for a peptide purity method:

1. **Blank injection** (diluent) — confirms a clean baseline and no ghost peaks.
2. **Five or six replicate injections of the reference standard** — establishes RSD of area, RT RSD, tailing, plate count, and $k'$.
3. **Resolution mixture injection** — the standard spiked with a known impurity (e.g., the $N-1$ deletion peptide) to verify $R_s$.
4. **Only then: batch samples**, with a standard injection every 10–20 samples and at the end of the sequence to bracket drift.

## SST Failure: Investigation and Actions

When an SST criterion fails, the batch must not be reported. Follow a structured investigation:

| Symptom | Likely Cause | First Action |
|---------|--------------|--------------|
| RSD of area fails | Autosampler needle issue, air bubble, injector leak | Re-prime injector; inspect needle seal; re-inject |
| Tailing factor exceeds limit | Column contamination, silanol interactions, overload | Column regeneration; check pH and ion-pairing |
| Resolution fails | Column efficiency loss, wrong mobile phase composition | Re-prepare mobile phase; check gradient |
| Plate count drops | Column aging or frit blockage | Measure backpressure; replace frit or column |
| RT drift beyond RSD | Temperature change, mobile phase evaporation | Verify column oven and mobile phase freshness |

Document the investigation in the batch record. Re-run SST after corrective action; results must pass before samples are processed.

## SST vs. Method Validation

SST and validation are complementary, not interchangeable:

| Aspect | Validation | System Suitability |
|--------|-----------|-------------------|
| When | Once per method (and on revalidation) | Every batch / run |
| Scope | All eight characteristics | Day-of-analysis system checks |
| Goal | Prove the method works | Prove the system works today |
| Limits | Establishes the acceptance criteria | Applies the acceptance criteria |

The SST limits must trace back to validation data — for example, the RSD limit is derived from the method's demonstrated repeatability.

## SST in the Batch Record: What the Paper Trail Should Show

When auditing a COA or a batch record, the SST evidence should be visible: (1) the SST injection sequence with date/time stamps; (2) the calculated values for each parameter; (3) the pass/fail verdict against the method's acceptance criteria; (4) the analyst's signature or electronic approval; (5) any corrective action taken when a criterion failed. Many laboratories also run a bracketing standard — a standard injection after every 10–20 samples — to demonstrate that the system did not drift during the batch. The bracketing standard's RSD is evaluated across the whole sequence, not just at the start.

## Automation, Data Systems, and SST Integrity

Modern chromatography data systems (CDS) can compute SST parameters automatically and even gate the sequence — samples are held until SST passes. This is good practice, but it introduces integrity considerations: (1) automated integration must use the same parameters as the validated method; (2) manual reintegration of SST injections must be flagged and justified; (3) audit trails must record any re-injection of standards after a failed run; (4) the CDS must prevent editing of SST results after approval. An SST record that was retroactively "fixed" is a data integrity red flag, not a quality signal.

## SST Frequency and Sequence Design Trade-offs

How often to run SST is a balance between assurance and throughput. Minimum practice: SST before each sequence. Better practice: SST at the start, plus bracketing standards every 10–20 injections and at the end. For long sequences (hundreds of injections), scheduled SST checkpoints prevent a failing system from generating hours of invalid data. The trade-off is real: each SST injection consumes time and column life. A risk-based approach sets SST frequency by the method's demonstrated robustness and the batch's criticality — release assays of finished peptides justify more frequent checks than early-development screening runs. Whatever the frequency, it must be defined in the SOP and followed; ad hoc SST is a data integrity concern.

## A Practical SST SOP Template for Peptide Methods

A concise SST SOP for a peptide purity method should specify: (1) **standard solution preparation** — concentration, solvent, storage and expiry; (2) **injection sequence** — blank, five replicate standards, resolution mixture, samples, bracketing standards; (3) **acceptance criteria** — RSD $\le$ 1.0%, tailing $\le$ 1.5, $R_s$ critical pair $\ge$ 1.5, plate count $\ge$ method minimum, RT RSD $\le$ 0.5%; (4) **failure handling** — stop, investigate, document, re-run after corrective action, and re-establish SST before continuing; (5) **data review** — who reviews the SST results and approves the batch. Adopting a written template removes ambiguity about what constitutes a passing system and makes the audit trail legible to both internal reviewers and external customers.

## SST and the Link to Buyer-Supplier Trust

For a peptide buyer, the presence of SST data on a COA is a fast signal of laboratory maturity: (1) SST values tell you the system was healthy when the sample ran; (2) the SST parameters chosen reveal what the laboratory considers important (a lab reporting only RSD, not resolution, may not be checking the critical pair); (3) SST reproducibility across batches reveals method stability — a lab whose tailing factor trends upward is watching its column age; (4) asking for SST raw data (injection list, calculated values, pass/fail) is a reasonable audit request that mature suppliers can satisfy immediately. A COA without any SST evidence is not necessarily wrong — but it offers the buyer no evidence that the measurement day was valid.

## Key Takeaways

- SST verifies the instrument and column are fit for use before every batch — never skip it.
- Core parameters: RSD of area $\le$ 1.0%, tailing $\le$ 1.5, resolution $\ge$ 1.5, plate count per method, RT RSD $\le$ 0.5%.
- A resolution mixture containing a real impurity (deletion peptide) is the most informative SST injection.
- SST failure stops the batch: investigate, correct, re-run, and document.
- SST limits come from validation data; they are not arbitrary defaults.
- A COA that reports purity without SST evidence has an unproven measurement day.

## References

1. [USP General Chapter <621> Chromatography](https://www.usp.org/harmonization-standards/pdg/general-chapter-chromatography)
2. [ICH Q2(R2) Validation of Analytical Procedures (International Council for Harmonisation)](https://www.ich.org/page/quality-guidelines)
3. [Snyder, L. R.; Kirkland, J. J.; Dolan, J. W. Introduction to Modern Liquid Chromatography, 3rd ed. Wiley 2010](https://www.wiley.com/en-us/Introduction+to+Modern+Liquid+Chromatography%2C+3rd+Edition-p-9780470167540)
4. [USP General Chapter <1225> Validation of Compendial Procedures](https://www.usp.org/)

Return to [How to Read a Peptide COA](index.md) or read [Analytical Method Transfer](10-analytical-method-transfer.md).
