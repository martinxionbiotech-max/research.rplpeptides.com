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

## Executive Summary

System suitability testing (SST) is the gate between a validated analytical method and a defensible purity result. It confirms that the entire chromatographic system — pump, injector, column, detector, and data system — operates within the validated performance envelope on the day of analysis, before any sample injection proceeds. For peptide manufacturers and the research laboratories that depend on their COAs, SST is the only contemporaneous proof that a purity number was generated under controlled, verifiable conditions.

For laboratory managers and QC directors, the practical significance of SST cannot be overstated. A batch of 200 vials released against a COA with a failing or absent SST carries no weight under audit — the measurement day was never qualified. Regulatory frameworks from USP <621> to ICH Q2(R2) require SST as a component of analytical procedure performance verification, and in peer-reviewed practice, SST parameters such as injection precision, tailing factor, resolution, and plate count trend data constitute the earliest warning system for column aging, instrument drift, and method degradation. Laboratories that treat SST as a box to check miss the opportunity to prevent batch failures; laboratories that treat SST as a diagnostic tool protect their data integrity and their reputation.

The key takeaway for any stakeholder reading a peptide COA: SST evidence separates a measurement from an assertion. A COA that lists the calculated SST values with their acceptance criteria — RSD, tailing, resolution, plate count — provides the reader with the confidence that the chromatographic system performed as intended on the day the sample was run. A COA that replaces SST evidence with silence offers no such assurance.

## Background

### What SST Is and Why It Exists

A validated method (see [HPLC Method Validation](../coa-guide/08-hplc-method-validation.md)) proves the procedure works under controlled conditions. But instruments drift: columns age, detector lamps dim, mobile phases evaporate or acidify over time, and autosampler seals degrade. SST is a defined set of checks run immediately before — and often during — a batch sequence to confirm the chromatographic system is still operating within the envelope established during method validation. It answers the question: "Is this instrument fit for purpose right now?"

Under [USP <621>](../coa-guide/06-usp-621-chromatography-guide.md) and ICH Q2(R2) guidance, SST is mandatory for compendial procedures and is established best practice for all quantitative HPLC assays in peptide quality control. The European Pharmacopoeia (Ph. Eur.) likewise mandates system suitability as part of method verification in chapter 2.2.46, and the FDA's guidance on analytical procedures in CGMP environments explicitly ties SST to data integrity expectations under 21 CFR Part 11 and Part 211. The principle is universal: before a system reports a number, it must prove it can report it accurately.

### The Regulatory and Scientific Rationale

SST exists at the intersection of three regulatory concepts: method validation (proving the method can work), method verification (proving it works in this laboratory), and system qualification (proving the instrument works today). Validation establishes the method's performance characteristics — accuracy, precision, specificity, linearity, range, detection limit, quantitation limit, and robustness — under controlled conditions. But validation is a snapshot taken once, or periodically; it does not vouch for the column that has aged six months since that snapshot, nor for the mobile phase prepared this morning by a different analyst. SST fills that temporal gap by re-checking the parameters most sensitive to instrument condition on every batch.

This rationale is explicitly acknowledged in the pharmaceutical peer-reviewed literature. In a widely cited review in the *Journal of Pharmaceutical and Biomedical Analysis*, Ermer and Miller (2005) positioned SST as the practical implementation of the "fit-for-purpose" concept that runs through ICH Q2 and Q7 guidance. Their framework — which has become the standard reference for SST design in the peptide and small-molecule fields — treats SST parameters as continuous process variables whose trends are more informative than their pass/fail snapshots.

## Core Science

### The Five Core SST Parameters

Six parameters form the standard SST panel for peptide purity methods. Each responds to a different failure mode, and together they provide a comprehensive diagnostic of chromatographic health:

| Parameter | Definition | Typical Acceptance Criterion |
|-----------|------------|------------------------------|
| Injection precision (RSD of area) | Repeatability of replicate injections of the reference standard | ≤ 1.0% (assay) |
| Retention time RSD | Repeatability of retention times | ≤ 0.5% |
| Tailing factor T | Peak symmetry of the main peak | ≤ 1.5 (or 2.0 for low-level peaks) |
| Resolution Rs | Separation between the main peak and the nearest critical impurity | ≥ 1.5 (baseline separation) |
| Plate count N | Column efficiency | ≥ 5,000–10,000 (method-specific) |
| Capacity factor k' | Retention relative to void volume | ≥ 2.0 |

The exact limits are not arbitrary industry defaults — they are derived from each method's validation data. A method that demonstrated an RSD of 0.3% during validation might set the SST RSD limit at 1.0% to allow practical operating margins; a method that barely achieved 1.0% during validation cannot set the same limit without absorbing a high failure rate. The relationship between validation performance and SST limits is a direct traceability chain that should be documented in the method's validation report and referenced in the SOP.

### Injection Precision (RSD of Peak Area)

$$\text{RSD (\%)} = \frac{s}{\bar{x}} \times 100$$

For five or six replicate injections of the reference standard, the RSD of peak area must not exceed the method's established limit, commonly 1.0% or tighter. In research peptide analysis at 214 nm, precision depends on stable detector response, consistent injection volume, and proper column equilibration.

Poor injection precision diagnoses autosampler problems — a failing needle seal, an air bubble in the sample loop, incomplete loop filling in partial-loop mode — or detector instability. The failure pattern matters: a single outlier among five injections suggests an autosampler transient; progressively rising or falling area suggests detector drift; high RSD without trend suggests random noise, possibly from mobile phase degassing or pump pulsation. Each pattern directs the investigation to a different root cause.

### Tailing Factor

$$T = \frac{W_{0.05}}{2f}$$

Where W₀.₀₅ is the peak width at 5% of peak height and f is the distance from the leading edge to the peak apex at that height. T = 1.0 is a perfectly symmetrical peak; T ≤ 1.5 is the common acceptance limit for pharmaceutical methods. Peptide-specific considerations: basic residues (Lys, Arg, His) interact with residual silanols on the silica support, and this secondary ion-exchange retention mechanism produces tailing that worsens at neutral pH and improves at the low pH (2–3) typical of TFA-based mobile phases. See [Tailing Factor Explained](../coa-guide/12-tailing-factor-explained.md) for a detailed treatment.

### Resolution

$$R_s = \frac{2(t_{R2} - t_{R1})}{W_1 + W_2}$$

Where W₁ and W₂ are baseline peak widths. Rs ≥ 1.5 indicates baseline separation — the valley between the peaks reaches the baseline and area integration is reliable. For peptide purity methods, the critical pair is almost always the main peptide versus its nearest-eluting impurity, which is frequently a deletion analog or an oxidized species. See [Resolution in Chromatography](../coa-guide/13-resolution-in-chromatography.md) for the optimization framework.

### Plate Count

$$N = 16 \left(\frac{t_R}{W}\right)^2$$

Where W is the baseline width. Plate count is a sensitive, non-specific indicator of column health. A drop of more than 20% from the value recorded during method validation signals column degradation — bonded-phase hydrolysis, frit blockage, or void formation at the column head. Plate count is also influenced by extra-column band broadening, so a sudden drop in plate count on an otherwise healthy column should trigger an inspection of tubing connections, injection volume, and detector flow-cell integrity.

### Capacity Factor

$$k' = \frac{t_R - t_0}{t_0}$$

Where t₀ is the column void time (measured by an unretained marker such as uracil or thiourea). k' ≥ 2.0 ensures the main peak is adequately retained and is not eluting in the void volume region where resolution is poor and integration is unreliable. For gradient methods, k' is less directly interpretable than for isocratic methods, but a steep drop in k' across sequences indicates mobile phase composition drift, most often from solvent evaporation or improper gradient proportioning.

### The Resolution Mixture: The Most Informative SST Injection

A resolution mixture — the reference standard spiked with a known critical impurity at a known concentration — is the single most informative SST injection for peptide methods. Typically, the spike is a deletion peptide impurity (e.g., the N-1 des-amino acid analog) or an oxidized form at a concentration of 0.5–2.0% relative to the main peak. Running this mixture in SST confirms three things simultaneously: the critical-pair resolution, the retention-time stability of both species, and the detector's ability to see the low-level impurity in the presence of the high-concentration main peak. A method whose SST protocol omits the resolution mixture is forfeiting its best diagnostic tool — a standard-alone SST can pass RSD and tailing checks while a co-elution problem silently persists.

## Research Evidence

The following table consolidates the regulatory, pharmacopeial, and peer-reviewed evidence base that underpins SST practice for peptide HPLC:

| Finding | Data | Source |
|---------|------|--------|
| SST is mandatory for compendial procedures and includes RSD, tailing, resolution, and plate count | USP <621> specifies SST requirements including injection precision (RSD ≤ 1.0–2.0%), tailing factor (T ≤ 1.5–2.0), resolution (Rs ≥ 1.5) | USP General Chapter <621>, Chromatography (2023) |
| European Pharmacopoeia mandates system suitability with analogous parameters measured at half-height | EP 2.2.46 specifies resolution calculation using peak widths at half-height and tailing through the symmetry factor at 10% height | Ph. Eur. 11th Edition, Chapter 2.2.46 (2023) |
| ICH Q2(R2) requires system suitability as part of analytical procedure performance verification | Q2(R2) Section 3.1 mandates that system suitability criteria be established from validation data and verified before each analytical run | ICH Q2(R2), International Council for Harmonisation (2024) |
| FDA CGMP guidance ties SST to data integrity and laboratory records under 21 CFR Part 211 | FDA Guidance for Industry: Analytical Procedures and Methods Validation (2015) |
| SST parameter trends are more informative than pass/fail snapshots for predicting column failure | Ermer, J.; Miller, J. H. McB. *J. Pharm. Biomed. Anal.* 2005, 38, 653–663 |
| Column plate count degradation of >20% from baseline signals column retirement independent of other parameters | Snyder, L. R.; Kirkland, J. J.; Dolan, J. W. *Introduction to Modern Liquid Chromatography*, 3rd ed., Wiley, 2010, Ch. 11 |
| Resolution-mixture SST injections detect co-elution problems invisible to standard-alone SST | Dong, M. W. *LCGC North America* 2019, 37(5), 324–332 |
| Autosampler precision failures trace to needle-seal leaks, air in the sample loop, or partial-loop injection errors in >80% of cases | Dolan, J. W. *LCGC North America* 2013, 31(8), 618–624 |
| Mobile phase evaporation and column oven temperature drift are the leading causes of RT RSD failures in gradient peptide methods | Neue, U. D. *HPLC Columns: Theory, Technology, and Practice*, Wiley-VCH, 1997 |
| Bracketing standards every 10–20 injections provide run-length drift evidence superior to start-only SST | ICH Q2(R2) Section 3.3 recommends system suitability checks at intervals throughout long sequences |

## SST Run Design

A well-designed SST protocol for a peptide purity method includes the following injection sequence, executed before any sample vial is uncapped:

1. **Blank injection** (diluent only) — confirms a clean baseline, no ghost peaks, and no carryover from previous sequences. The blank injection should be the same diluent used for sample preparation and should be integrated with the same parameters as the sample.
2. **Five or six replicate injections of the reference standard** — establishes RSD of area, retention time RSD, tailing factor, plate count, and capacity factor. Six replicates provide a more robust RSD estimate, but five is the minimum accepted under USP <621> and is sufficient for most peptide methods.
3. **Resolution mixture injection** — the standard spiked with the critical impurity (deletion peptide, oxidized form) to verify Rs ≥ 1.5 for the critical pair. The impurity concentration should match the reporting threshold (0.5% or 1.0%) to confirm the detector response at the specification limit.
4. **Only after all three injections pass their criteria: batch samples**, with a bracketing standard injection every 10–20 samples and a final standard injection at the end of the sequence to bracket any instrument drift across the run.

### SST Frequency and Sequence Design Trade-offs

How often to run SST is a balance between analytical assurance and throughput. The minimum acceptable practice is SST before each sequence. Better practice adds bracketing standards every 10–20 injections and a final standard at the sequence end. For long sequences spanning hundreds of injections across multiple batches, scheduled SST checkpoints — a full repeat of the standard injections at defined intervals — prevent a silently failing system from generating hours of invalid data.

The trade-off between frequency and throughput is genuine: each standard injection consumes time, mobile phase, and column life. A risk-based framework sets SST frequency by the method's demonstrated intermediate precision during validation, the batch's criticality (release assays for finished peptides justify more frequent checks than early-development screening runs), and the column's known lifetime. Whatever the frequency, it must be defined in the SOP before the sequence starts; ad hoc SST injections inserted after a suspicious chromatogram are a data integrity concern.

## SST Failure: Investigation and Root Cause Analysis

When an SST criterion fails, the batch must not be reported. The investigation follows a structured diagnostic path, not a blind re-run that hopes for a better outcome:

| Symptom | Likely Cause | First Action | Second Action |
|---------|--------------|--------------|---------------|
| RSD of area fails | Autosampler needle seal leak, air bubble in sample loop, injector partial-loop error | Re-prime injector; inspect needle seal; purge sample loop | Check injection precision of an independent standard solution; if RSD improves, the original sample vial preparation is suspect |
| Tailing factor exceeds limit | Column contamination from previous samples, residual silanol exposure, mass overload | Regenerate column with strong solvent (80% ACN); verify pH of mobile phase | Reduce injection mass; if tailing corrects, adjust sample concentration; if not, replace column |
| Resolution fails | Column efficiency loss, wrong mobile phase composition, gradient malfunction | Re-prepare mobile phase; verify gradient proportioning valve function | Check column plate count; if N has dropped >20%, column is likely degraded |
| Plate count drops | Column aging, frit blockage, void at column head | Measure backpressure trend; replace guard column first | If N remains low, replace analytical column and re-qualify |
| RT drift beyond RSD | Column oven temperature instability, mobile phase evaporation, pump proportioning error | Verify column oven setpoint with thermometer; prepare fresh mobile phase | Check pump proportioning accuracy with step-gradient test |
| Capacity factor drops | Mobile phase organic content too high, column degradation | Verify gradient composition; check pump calibration | If k' shift is consistent across all peaks, correct mobile phase; if inconsistent, column chemistry has changed |

Document every investigation step in the batch record, including the corrective action taken and its result. The SST re-run after corrective action must pass all criteria before samples are processed. A laboratory that replaces its failed-SST column, re-runs SST without documenting the failure, and then runs samples has committed a data integrity violation — the failed column's chromatograms are part of the batch record whether or not they were "final."

### The Data Integrity Dimension

SST records are part of the analytical batch and are subject to the same data integrity rules as sample results under 21 CFR Part 11, EU Annex 11, and WHO guidance on good data and record management practices. In practice, this means:

1. **Automated integration must use the same parameters as the validated method.** Manual reintegration of SST injections — changing the baseline, integration threshold, or peak start/end — must be flagged by the CDS audit trail, justified in writing, and approved by a second analyst. A common data integrity red flag is an SST chromatogram whose integration differs from the method's SOP without a contemporaneous justification.
2. **Re-injection of standards after a failed SST must be documented as a deviation.** The original failed injections must remain in the data file, not be overwritten. The CDS should not permit retroactive deletion of injections from a sequence.
3. **Audit trails must record any editing of SST results after approval.** A system that allows "correcting" the RSD value from 1.3% to 0.9% after the batch is approved is a data integrity risk, not a convenience feature.
4. **SST pass/fail gating in the CDS** — where samples are held in the injection queue until SST passes — is good automated practice, but the gating logic must be validated and the audit trail must record the hold event and the analyst's release action.

## Automation, Data Systems, and SST Integrity

Modern chromatography data systems (CDS) such as Waters Empower, Agilent OpenLab, and Thermo Chromeleon compute SST parameters automatically during or immediately after the SST injections. These systems can gate the sequence — samples are held in the queue until the software confirms SST has passed — and can generate SST summary reports that auto-populate the batch record. This automation improves efficiency and reduces transcription errors, but it also introduces specific integrity considerations:

1. **The SST calculation method must match the pharmacopeial definition.** A CDS default for "resolution" might use the half-height formula (EP convention) while the method SOP specifies baseline widths (USP convention). The CDS configuration must be verified and documented as part of method transfer.
2. **Integration parameters for SST injections must be locked.** If the CDS allows different integration parameters for SST standards versus samples, the SST results are not comparable to the sample quantification.
3. **Manual peak identification in SST —** where the analyst overrides the CDS peak assignment — must be rare, justified, and auditable. A pattern of manual peak reassignments in SST data signals an unstable method or an operator compensating for instrument problems.
4. **SST results must be reviewed and approved by a second analyst** before the batch report is finalized. This second-person review is not just a regulatory checkbox; it is the last opportunity to catch a CDS configuration error, an integration mistake, or a failing parameter that the software's pass/fail logic misclassified.

## SST and the Link to Buyer-Supplier Trust

For a peptide buyer reviewing a COA, the presence of SST data — even in summary form — is a fast and reliable signal of laboratory maturity:

1. **SST values confirm system health.** A COA that reports "Injection precision RSD: 0.4% (limit ≤ 1.0%). Tailing factor: 1.12 (limit ≤ 1.5). Resolution (critical pair): 1.8 (limit ≥ 1.5)." tells you the system was performing well on measurement day.
2. **SST parameter selection reveals laboratory priorities.** A lab that reports only RSD, omitting resolution and tailing, may not be checking the critical impurity pair — and a co-eluting deletion peptide would go undetected.
3. **SST trend data across batches reveals method stability.** A supplier whose tailing factor trends from 1.05 to 1.38 across six months is watching its column age; a supplier whose SST values are identical across every batch may be copying-and-pasting rather than measuring.
4. **Requesting SST raw data is a reasonable audit ask.** Mature suppliers can produce the SST injection list, calculated values, pass/fail verdicts, and the audit trail on request. A supplier that cannot produce these artifacts for a COA under audit is operating below the standard of a quality-controlled laboratory.

A COA without any SST evidence is not necessarily wrong — but it provides the buyer with no evidence that the measurement day was valid. In an industry where purity numbers drive purchasing decisions, that evidential gap is significant.

## A Practical SST SOP Template for Peptide Methods

A concise SST SOP for a peptide purity method should specify the following elements, each referenced to the method's validation data:

1. **Standard solution preparation:** concentration (typically 0.5–1.0 mg/mL), solvent composition, storage conditions, and expiry time (typically 24–48 hours at 2–8 °C, or fresh daily). The standard should be prepared from the same reference material lot used during validation, or demonstrated equivalent.
2. **Injection sequence:** blank (diluent), five or six replicate standard injections, resolution mixture (critical impurity spiked at reporting-threshold concentration), samples, bracketing standard every 10–20 injections, final standard at sequence end.
3. **Acceptance criteria:** RSD of area ≤ 1.0%; retention time RSD ≤ 0.5%; tailing factor T ≤ 1.5; resolution Rs ≥ 1.5 for the critical pair; plate count N ≥ method minimum (from validation); capacity factor k' ≥ 2.0.
4. **Failure handling:** stop the sequence, investigate per the diagnostic table above, document the deviation and corrective action, re-establish SST with a fresh standard preparation and a new sequence, and do not run samples until all criteria pass on the re-run.
5. **Data review:** specify who reviews SST results (analyst plus second reviewer), what they verify (calculated values versus limits, integration consistency, audit trail integrity), and how the approval is recorded (electronic signature in CDS or wet signature on printed batch record).

Adopting a written SOP template removes ambiguity about what constitutes a passing system. It also makes the audit trail legible to both internal quality assurance and external customers — every piece of SST evidence traces to a defined, documented requirement.

## SST vs. Method Validation: Understanding the Distinction

SST and method validation are complementary activities that serve different purposes, operate on different timescales, and answer different questions. The table below summarizes the key differences:

| Aspect | Validation | System Suitability |
|--------|-----------|-------------------|
| When performed | Once per method (plus revalidation after changes) | Every batch / every analytical run |
| Scope | All eight validation characteristics (accuracy, precision, specificity, linearity, range, LOD, LOQ, robustness) | Day-of-analysis system checks (precision, tailing, resolution, plate count, capacity factor, retention time stability) |
| Question answered | "Can this method produce accurate, reliable results?" | "Is this instrument performing correctly today?" |
| Acceptance criteria origin | Established during method development and confirmed during validation | Derived from validation data and documented in the method SOP |
| Regulatory basis | ICH Q2(R2), USP <1225> | USP <621>, ICH Q2(R2) Section 3.1, Ph. Eur. 2.2.46 |

The SST limits must trace back to validation data through a documented rationale. For example, if validation demonstrated a repeatability RSD of 0.5%, the SST limit might be set at 1.0% to allow practical margin while remaining within the validated range. If validation's intermediate precision (day-to-day, analyst-to-analyst) was 1.2%, an SST RSD limit of 1.0% is aggressive but defensible if SST is run daily and the system is well maintained. The traceability chain — validation data → statistical analysis → SOP limit → SST check → batch release — is a fundamental element of analytical quality assurance.

## Key Takeaways

- SST verifies the instrument and column are fit for use before every batch — never skip it, and never treat it as a procedural formality.
- Core parameters: RSD of area ≤ 1.0%, tailing T ≤ 1.5, resolution Rs ≥ 1.5, plate count per method minimum, RT RSD ≤ 0.5%, k' ≥ 2.0.
- A resolution mixture containing a real critical impurity (deletion peptide or oxidized species) at reporting-threshold concentration is the most informative SST injection a peptide laboratory can run.
- SST failure stops the batch: investigate per a structured diagnostic table, correct the root cause, re-run SST to confirm the fix, and document every step in the batch record.
- SST limits come from validation data, not from arbitrary defaults — the traceability chain must be documented.
- SST data on a COA is a trust signal between supplier and buyer; its absence is an evidential gap that sophisticated procurement groups should probe.
- A COA that reports purity without any SST evidence leaves the measurement day unproven.

## FAQ

<div class="faq-item">
<h3>Q: What is system suitability testing?</h3>
<p class="faq-answer">A: System suitability testing (SST) is a set of pre-defined checks — injection precision, retention time repeatability, tailing factor, resolution, and plate count — run before each analytical batch to confirm the HPLC system performs within the validated operating envelope on that day. It verifies that the pump, injector, column, detector, and data system are fit for purpose before any sample result is generated.</p>
</div>

<div class="faq-item">
<h3>Q: Why is SST mandatory under USP &lt;621&gt;?</h3>
<p class="faq-answer">A: USP &lt;621&gt; requires SST because method validation alone cannot guarantee instrument performance on a future date. Instruments drift: columns age, lamps dim, mobile phases evaporate. SST bridges the time gap between validation (a one-time or periodic event) and daily measurement by re-verifying the parameters most sensitive to instrument condition on every sequence.</p>
</div>

<div class="faq-item">
<h3>Q: What are the standard SST parameters in peptide HPLC?</h3>
<p class="faq-answer">A: The standard SST panel includes: injection precision (RSD of peak area, typically ≤ 1.0%), retention time RSD (≤ 0.5%), tailing factor T (≤ 1.5), resolution Rs between the main peak and nearest impurity (≥ 1.5), plate count N (≥ method-specific minimum), and capacity factor k' (≥ 2.0). Additional parameters such as signal-to-noise ratio and detector linearity may be included per the method SOP.</p>
</div>

<div class="faq-item">
<h3>Q: What happens if an SST criterion fails?</h3>
<p class="faq-answer">A: The batch sequence must stop. Do not proceed to sample injections. Follow a structured investigation: identify the failing parameter, diagnose the likely cause (referencing the diagnostic table in the SOP), apply corrective action, document the deviation and corrective action in the batch record, re-prepare fresh standards, re-run SST, and only proceed to samples after all SST criteria pass on the re-run. The original failed SST injections must remain in the data file.</p>
</div>

<div class="faq-item">
<h3>Q: What is the difference between SST and method validation?</h3>
<p class="faq-answer">A: Method validation is performed once per method (or upon revalidation after changes) and covers all eight ICH characteristics: accuracy, precision, specificity, linearity, range, LOD, LOQ, and robustness. SST is performed every batch and checks only the subset of parameters — precision, tailing, resolution, plate count — that are sensitive to day-to-day instrument condition. Validation proves the method works; SST proves the instrument works today.</p>
</div>

<div class="faq-item">
<h3>Q: How many standard replicate injections are required for SST?</h3>
<p class="faq-answer">A: USP &lt;621&gt; specifies a minimum of five replicate injections of the reference standard for injection precision determination. Six replicates provide a more statistically robust RSD estimate and are preferred when method precision is borderline. Fewer than five replicates produce an RSD with insufficient degrees of freedom for reliable pass/fail decisions.</p>
</div>

<div class="faq-item">
<h3>Q: What is a resolution mixture in SST?</h3>
<p class="faq-answer">A: A resolution mixture is the reference standard spiked with a known critical impurity — typically a deletion peptide, oxidized species, or epimer — at a low concentration (0.5–2.0%) relative to the main peak. Running this mixture during SST simultaneously verifies the critical-pair resolution, the retention time stability of both species, and the detector's ability to detect a low-level impurity adjacent to a large main peak. It is the single most informative SST injection.</p>
</div>

<div class="faq-item">
<h3>Q: How often should bracketing standards be injected?</h3>
<p class="faq-answer">A: Best practice is a bracketing standard injection every 10–20 sample injections and at the end of the sequence. The bracketing standard's area RSD is evaluated across the full sequence — if it exceeds the method's limit, the sequence has experienced instrument drift and the results between the drifting standards may be unreliable. More frequent bracketing provides earlier drift detection; less frequent bracketing saves time and column life but increases the risk of unrecognized drift.</p>
</div>

<div class="faq-item">
<h3>Q: What does SST tell a peptide buyer about a COA?</h3>
<p class="faq-answer">A: SST data on a COA tells the buyer that the instrument was verified fit for purpose before the sample was run. It provides values for injection precision, tailing, and resolution that independently confirm the measurements were made under controlled conditions. A COA without SST evidence offers no proof that the instrument was performing correctly on measurement day — the purity number is an assertion without contemporaneous verification.</p>
</div>

<div class="faq-item">
<h3>Q: Can SST data be audited?</h3>
<p class="faq-answer">A: Yes. SST data — the injection sequence list with date/time stamps, calculated parameter values, pass/fail verdicts, and CDS audit trails — are part of the analytical batch record and subject to the same data integrity requirements as sample results under 21 CFR Part 11 and EU Annex 11. Mature suppliers can produce SST raw data on request. Suppliers that cannot produce these records for an audited COA are operating below the standard of a quality-controlled analytical laboratory.</p>
</div>

## References

1. USP General Chapter <621> Chromatography. United States Pharmacopeia–National Formulary, USP 46–NF 41. Rockville, MD: United States Pharmacopeial Convention; 2023.
2. ICH Q2(R2) Validation of Analytical Procedures. International Council for Harmonisation of Technical Requirements for Pharmaceuticals for Human Use; 2024.
3. European Pharmacopoeia 11th Edition, Chapter 2.2.46: Chromatographic Separation Techniques. Strasbourg: European Directorate for the Quality of Medicines & HealthCare; 2023.
4. Ermer, J.; Miller, J. H. McB. Method Validation in Pharmaceutical Analysis: A Guide to Best Practice. *J. Pharm. Biomed. Anal.* 2005, 38(4), 653–663. doi:10.1016/j.jpba.2005.02.016
5. Snyder, L. R.; Kirkland, J. J.; Dolan, J. W. *Introduction to Modern Liquid Chromatography*, 3rd ed. Hoboken, NJ: John Wiley & Sons; 2010. doi:10.1002/9780470508183
6. Dong, M. W. System Suitability Testing for HPLC Methods. *LCGC North America* 2019, 37(5), 324–332.
7. Dolan, J. W. Troubleshooting LC Autosamplers. *LCGC North America* 2013, 31(8), 618–624.
8. Neue, U. D. *HPLC Columns: Theory, Technology, and Practice*. New York: Wiley-VCH; 1997.
9. FDA Guidance for Industry: Analytical Procedures and Methods Validation for Drugs and Biologics. Silver Spring, MD: U.S. Food and Drug Administration; 2015.
10. WHO Technical Report Series No. 996, Annex 5: Guidance on Good Data and Record Management Practices. Geneva: World Health Organization; 2016.
11. Huber, L. Validation and Qualification in Analytical Laboratories, 2nd ed. New York: Informa Healthcare; 2007.
12. Ahuja, S.; Dong, M. W. *Handbook of Pharmaceutical Analysis by HPLC*. Amsterdam: Elsevier; 2005. doi:10.1016/S0149-6395(05)80041-8
13. Krull, I. S.; Swartz, M. E. Analytical Method Development and Validation for the Academic Researcher. *Anal. Chem.* 1999, 71(22), 795A–801A. doi:10.1021/ac990793v
14. Meyer, V. R. *Practical High-Performance Liquid Chromatography*, 5th ed. Chichester: Wiley; 2010. doi:10.1002/9780470682180
15. Ahuja, S.; Rasmussen, H. *HPLC Method Development for Pharmaceuticals*. Amsterdam: Elsevier; 2007. doi:10.1016/S0149-6395(07)80032-8
16. ICH Q14 Analytical Procedure Development. International Council for Harmonisation of Technical Requirements for Pharmaceuticals for Human Use; 2024.
17. USP General Chapter <1225> Validation of Compendial Procedures. United States Pharmacopeia–National Formulary, USP 46–NF 41. Rockville, MD: United States Pharmacopeial Convention; 2023.

Return to [How to Read a Peptide COA](../coa-guide/index.md) or read [Analytical Method Transfer](../coa-guide/10-analytical-method-transfer.md).
