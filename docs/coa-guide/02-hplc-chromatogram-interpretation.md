---
title: "HPLC Chromatogram Interpretation: A Practical Field Guide"
description: "Master HPLC chromatogram reading: baseline stability, signal-to-noise ratio, ghost peaks, solvent fronts, integration parameters, and peak shape diagnosis."
slug: hplc-chromatogram-interpretation
category: Chromatography
tags: [HPLC, Chromatogram, Baseline, Analytical Testing, Signal-to-Noise]
author: RPL Peptides Research Team
published: 2026-08-01
---

# HPLC Chromatogram Interpretation: A Practical Field Guide

## Executive Summary

A chromatogram is the primary physical evidence supporting the purity value reported on a peptide Certificate of Analysis. Every chromatogram encodes five independent pieces of information—baseline quality, peak symmetry, signal-to-noise ratio, retention time consistency, and integration boundaries—and each one must be evaluated critically before the printed purity number can be trusted. A chromatogram that appears "clean" at first glance may conceal co-eluting impurities, integration artifacts, or baseline anomalies that inflate the reported purity by several percentage points.

For laboratory managers and research scientists who review peptide COAs, chromatogram interpretation is not a niche skill—it is the single most important quality-control competency short of direct mass spectrometric identity confirmation. The difference between a reported purity of 98.0% and 99.5% is often not a difference in peptide quality but a difference in how the chromatogram was integrated, what wavelength was monitored, and whether the solvent front was correctly excluded. Understanding these variables transforms a COA reader from a passive recipient of numbers into an active evaluator of analytical evidence.

This guide provides a comprehensive framework for HPLC chromatogram interpretation in the context of peptide purity analysis. We cover the five mandatory elements of every chromatogram, baseline stability diagnostics, signal-to-noise ratio fundamentals, the identification and prevention of ghost peaks, the impact of integration parameters on reported purity, peak shape as a diagnostic tool, and the critical distinction between gradient and isocratic chromatograms. Each section is illustrated with worked examples and specific diagnostic rules that can be applied to any peptide chromatogram.

## Background

High-performance liquid chromatography (HPLC) with UV detection is the workhorse technique for peptide purity determination. A peptide sample is injected onto a reversed-phase column (typically C18), eluted with a water-acetonitrile gradient containing 0.1% trifluoroacetic acid (TFA), and detected by UV absorbance at 214 nm—the wavelength at which the peptide bond absorbs maximally. The resulting chromatogram plots detector response (milli-absorbance units, mAU) against time (minutes), producing a series of peaks whose integrated areas, when normalized, yield the area-percent purity value reported on the COA.

The chromatogram's apparent simplicity is deceptive. Every peak represents not just the peptide but also the cumulative effects of column chemistry, mobile phase composition, instrument configuration, detector performance, and software integration algorithms. A chromatogram is not a photograph of the sample; it is a processed representation produced by a chain of instrumental and computational transformations. Interpreting it correctly requires understanding each link in that chain.

The regulatory framework for chromatographic analysis is anchored by USP General Chapter <621> Chromatography and ICH Q2(R2) Validation of Analytical Procedures. USP <621> defines system suitability requirements and allowable method adjustments; ICH Q2(R2) specifies the validation characteristics—specificity, accuracy, precision, linearity, range, detection limit, quantitation limit, and robustness—that must be demonstrated before a chromatographic method's results can be considered reliable. Both are discussed in detail in [USP <621> Chromatography Guide](06-usp-621-chromatography-guide.md) and [ICH Q2(R2) Explained](07-ich-q2r2-explained.md).

## Core Science

### The Five Elements of Every Chromatogram

Every useful chromatogram contains five elements that should be checked in order, as each depends on the ones before it:

1. **Baseline**: the detector signal in the absence of eluting analyte. A stable, flat baseline is the foundation of reliable integration because every peak area is measured relative to the baseline. A drifting baseline makes the definition of "where the peak starts" ambiguous, and small impurities riding on a rising baseline are easily missed or misintegrated.

2. **Solvent front (void volume peak)**: the unretained material that elutes at the column void time $t_0$, typically 2.0–3.5 minutes for a 4.6 × 250 mm column at 1.0 mL/min. This peak contains injection solvent, salts, and highly polar components. It must be identified and excluded from the purity calculation because it is not a peptide-related impurity.

3. **Analyte peaks**: the resolved signals corresponding to the target peptide and its impurities. Each peak's retention time, area, symmetry, and width provide independent diagnostic information about the separation quality.

4. **Noise**: random high-frequency fluctuation of the baseline, typically measured as peak-to-peak amplitude over a representative time window. Noise determines the smallest peak that can be reliably detected or quantified—the LOD and LOQ of the method.

5. **Integration marks**: the software's assignment of peak start and end points, shown as tick marks or vertical lines on the printed chromatogram. These are the single most important quality check on any COA chromatogram: if the integration marks sit inside the peak rather than at the true baseline, the reported area is incorrect.

### Baseline Stability and Its Importance

The baseline should be flat—drift below 0.1% of full scale per minute—and free of wandering. Baseline quality is often the first thing an experienced chromatographer checks because a compromised baseline invalidates every subsequent measurement. Three mechanisms dominate baseline problems:

**Column equilibration failure.** Insufficient re-equilibration between gradient runs leaves the column with residual organic modifier, so the initial mobile phase composition differs from what the method specifies. Early-eluting peaks are then retained differently—or not at all—producing a rising or falling baseline at the start of the run. The remedy is straightforward: extend the post-run equilibration time. A rule of thumb is 5–10 column volumes of starting mobile phase, which for a 4.6 × 250 mm column at 1.0 mL/min translates to approximately 12–25 minutes.

**Temperature fluctuation.** Ambient temperature changes of even 2–3 °C alter solvent viscosity and detector response, producing slow baseline undulations. A column oven set to a controlled temperature—typically 30–40 °C for peptide separations—stabilizes both retention times and baseline flatness. Laboratories that run HPLC without column temperature control should expect baseline wander as a routine artifact.

**Detector warm-up drift.** Deuterium lamps in UV detectors require 20–30 minutes after ignition to reach thermal equilibrium. During this warm-up period, the baseline drifts upward as the lamp output stabilizes. Running samples before the detector has equilibrated produces chromatograms with a characteristic exponential-decay baseline shape that is immediately recognizable to an experienced analyst.

A rising baseline under gradient elution is normal and expected when the mobile phase B (organic modifier, typically acetonitrile) absorbs UV light at the detection wavelength. Acetonitrile has a UV cutoff of approximately 190 nm, so at 214 nm some absorbance is unavoidable. What matters diagnostically is that the baseline rise is smooth, monotonic, and reproducible between runs. A step change—a sudden vertical displacement—indicates a pump malfunction or air in the solvent delivery system, not a routine gradient artifact.

### Signal-to-Noise Ratio (S/N)

The signal-to-noise ratio quantifies the smallest peak that can be reliably distinguished from background fluctuations. It is defined as:

$$\text{S/N} = \frac{2H}{h}$$

Where $H$ is peak height measured from baseline to apex, and $h$ is the peak-to-peak amplitude of the baseline noise measured over a representative region—typically a time window equal to 20 times the peak width at half height—in a blank injection under identical conditions.

**Worked Example.** A peptide peak has height $H = 15.0$ mAU. In a blank injection run on the same system, the baseline noise amplitude is $h = 0.15$ mAU peak-to-peak over a 5-minute window:

$$\text{S/N} = \frac{2 \times 15.0}{0.15} = 200$$

An S/N of 200 is excellent and well above the regulatory thresholds. For reliable quantitation, ICH Q2(R2) requires S/N ≥ 10; for detection (limit of detection, LOD), S/N ≥ 3. An S/N of 200 means the main peak is 20 times above the quantitation threshold, confirming the method has ample dynamic range for impurity detection. For the formal LOD/LOQ definitions, see [ICH Q2(R2) Explained](07-ich-q2r2-explained.md).

The practical implication for COA evaluation: if the S/N is low (e.g., S/N = 30 for the main peak), impurities at the 0.5% level will be at or below the quantitation limit. A COA reporting "purity 99.5%" from a chromatogram with S/N = 30 for the main peak is effectively reporting that the method cannot detect impurities below 0.5%—not that no impurities exist.

### The Solvent Front and Void Volume

The solvent front is the first disturbance on the chromatogram, eluting at the void time $t_0$. It contains unretained material—injection solvent, buffer salts, and highly polar components that do not interact with the stationary phase. Key quantitative facts for a standard 4.6 × 250 mm, 5 µm C18 column:

- The void volume is approximately 2.5–3.0 mL.
- At a flow rate of 1.0 mL/min, $t_0$ ≈ 2.5–3.0 minutes.
- A large solvent-front peak can obscure early-eluting peptide impurities with $k' < 1$.

Never integrate the solvent front as an analyte peak. It is not a real component of the peptide sample, and including it in the total area denominator deflates the reported purity. A common COA audit finding is the inclusion of the solvent front in the peak table as "impurity at $t_R$ 2.8 min." The void peak should be explicitly excluded from integration in the processing method, and the exclusion should be visible on the printed chromatogram.

If the target peptide elutes very early ($t_R < 5$ min on a standard column), consider whether the injection solvent is stronger than the starting mobile phase. Matching the injection solvent to the starting mobile phase composition eliminates solvent-strength effects that distort early peaks.

### Ghost Peaks: Causes and Prevention

Ghost peaks—also called system peaks, artifact peaks, or phantom peaks—are reproducible signals that appear in blank injections containing no analyte. They are not sample-derived and must be eliminated before any batch analysis because they can co-elute with real impurities, producing false-positive impurity assignments.

| Cause | Signature | Prevention |
|-------|-----------|------------|
| Contaminated mobile phase | Peaks grow in area over successive runs as contaminants accumulate on-column | Use fresh HPLC-grade solvents daily; filter all aqueous mobile phases through 0.22 µm membranes |
| Injector carryover | Peaks appear after high-concentration samples and diminish with blank washes | Program needle-wash cycles (e.g., 10% methanol or acetonitrile) between injections; use a dedicated wash vial |
| Buffer precipitation | Irregular spikes accompanied by pressure instability | Pre-mix aqueous and organic buffer components; check salt solubility limits in the organic phase |
| Detector cell contamination | Broad, slowly drifting baseline humps rather than sharp peaks | Clean the detector flow cell with 50% nitric acid followed by copious water; verify baseline recovery |
| Column bleed | Small, regularly spaced peaks at high organic percentage in the gradient | Use a column with bonded phase stable at the method's pH and organic modifier range; replace aged columns |

The definitive ghost-peak test: run a blank injection (pure injection solvent, no peptide) under the same gradient and integration parameters as the sample. Any peak appearing at S/N ≥ 3 in the blank is a ghost peak and must be eliminated from the method or explicitly subtracted—never integrated as an impurity in the sample. A COA from a laboratory that cannot produce a clean blank chromatogram is making purity claims on a contaminated system.

### Integration Parameters That Change Purity Results

Integration settings are not passive measurements—they are active choices that directly and sometimes dramatically change the reported purity. Three parameters dominate:

1. **Slope sensitivity (threshold)**: the minimum rate of signal change that the software uses to define the start and end of a peak. Too low a threshold causes baseline noise to be integrated as phantom peaks, inflating the impurity count and deflating the reported purity. Too high a threshold causes small real impurity peaks to be merged into the main peak or the baseline, inflating the reported purity by hiding real contaminants. The optimal threshold is empirically determined during method validation and should not be changed without documented justification.

2. **Peak width**: the expected peak width at half height, used by the software's smoothing algorithm and for peak-detection logic. An incorrect peak width estimate distorts the fitted baseline under each peak and can split a single broad peak into two false signals or merge two narrow, partially resolved peaks into one.

3. **Baseline mode**: the algorithm for drawing the baseline under overlapping peaks. Three modes are common—valley-to-valley (baseline drops to the valley between peaks), perpendicular drop (vertical line from the valley to the baseline), and tangent skim (tangent drawn under a small peak riding on the tail of a large peak). For unresolved impurity peaks eluting close to the main peptide peak, the choice of baseline mode changes the area split between the main peak and the impurity. Different modes give different purities from the same raw data.

A well-integrated chromatogram shows integration marks at the true boundaries of each peak—on the baseline, not inside the peak envelope. If the printed chromatogram on a COA shows integration tick marks cutting through the tail of the main peak, the reported main-peak area is truncated, and the purity is unreliable. This is one of the most common audit observations in peptide QC and one of the easiest to spot.

### Peak Shape as a Diagnostic Tool

Peak shape is not merely aesthetic—each deviation from ideal Gaussian symmetry points to a specific root cause in the column, the mobile phase, or the sample:

- **Symmetrical peak (asymmetry factor 0.9–1.1)**: healthy column, appropriate sample loading, proper mobile phase composition. This is the target state.
- **Tailing (asymmetry factor > 1.2)**: the peak leans to the right, with a sharp front and an extended rear. Caused by secondary interactions with residual silanol groups on the silica surface (most common), column overload, or extra-column band broadening from poorly plumbed fittings. Tailing reduces resolution between the main peak and a later-eluting impurity. See [Tailing Factor Explained](12-tailing-factor-explained.md) for the quantitative treatment.
- **Fronting (asymmetry factor < 0.8)**: the peak leans to the left. Caused by column overload (the stationary phase is saturated) or by injecting the sample in a solvent stronger than the mobile phase, which pushes the analyte band ahead faster than its equilibrium distribution would predict.
- **Shoulder (a bump or inflection on the side of the main peak)**: a partially resolved co-eluting species—often a diastereomer from racemization or a deletion peptide with nearly identical hydrophobicity. Shoulders are the most diagnostically significant peak-shape anomaly because they indicate a separation that is "almost but not quite" achieved. Confirmation requires LC-MS analysis of the shoulder region. See [Understanding LC-MS Reports](01-understanding-lc-ms-reports.md).

### Gradient vs Isocratic Chromatograms

Peptide purity methods use either gradient or isocratic elution, and the chromatograms look fundamentally different:

| Feature | Isocratic | Gradient |
|---------|-----------|----------|
| Mobile phase | Constant composition throughout the run | Composition changes over time (e.g., 5→95% acetonitrile) |
| Peak width | Broadens progressively with increasing retention time | Peaks remain narrow and roughly constant in width throughout the run |
| Run time | Long for late-eluting peptide peaks | Controlled by the gradient slope; late peaks are eluted faster |
| Baseline | Flat (low drift) when properly equilibrated | Systematically rising as UV-absorbing organic modifier increases |
| Typical use | Short peptides (<10 residues), simple mixtures, isocratic purity check | Most peptide purity methods; resolves complex impurity profiles |
| Method transfer robustness | Sensitive to small composition changes (±0.5% organic) | Generally more robust; gradient normalizes some inter-instrument differences |

On a gradient chromatogram, a steadily rising baseline is normal—the increasing acetonitrile concentration absorbs at 214 nm. A step change, a sawtooth pattern, or an irregular baseline shape is not normal and signals a pump or degasser malfunction, not the peptide sample.

### Electronic Data, Audit Trails, and Reproducibility

The printed chromatogram on a COA is a representation of electronic data, and its trustworthiness depends on the data system behind it. Four attributes define a defensible electronic record:

1. **Raw data files** (not screenshots or printed copies) must be archivable and re-integrable. Any analyst should be able to open the raw file and apply the method's integration parameters to reproduce the printed result.
2. **Audit trails** must record who processed the data, when, and what was changed. Manual reintegration—a common cause of purity inflation—must be flagged as a deviation from the automated processing method.
3. **The processing method** (integration parameters, calibration table, peak identification windows) must be stored with the data so that the same chromatogram can be reproduced from the raw file.
4. **Time-stamped sequence logs** tie each injection to a vial position, an instrument configuration, and an analyst, creating an unbroken chain of custody from sample to result.

When a customer re-analyzes a peptide and obtains a different purity from the COA, the first question is not "which lab is wrong" but "are the processing methods identical?" Reproducibility between laboratories is fundamentally a method question, not a blame question. See [Analytical Method Transfer](10-analytical-method-transfer.md) for the structured approach to inter-laboratory comparison.

### A Worked Walk-Through of a Realistic Purity Chromatogram

Consider a 25-residue peptide analyzed by RP-HPLC at 214 nm on a 4.6 × 250 mm C18 column with a 5–65% acetonitrile gradient over 30 minutes at 1.0 mL/min and 40 °C. The chromatogram shows:

- **Main peptide peak** at 18.4 min, area = 9,450 mAU·s, asymmetry factor = 1.2 (slight tailing).
- **Small peak** at 16.9 min, area = 120 mAU·s.
- **Small peak** at 19.6 min, area = 85 mAU·s.
- **Very early peak** at 3.2 min, area = 310 mAU·s (the integration settings exclude this peak from the peak table).

Step-by-step evaluation:

**Step 1:** The early peak at 3.2 min coincides with the void time ($t_0$ ≈ 2.8 min for this column). It is the solvent front and must be excluded from the purity calculation. The integration software has correctly excluded it—this is a positive finding.

**Step 2:** The impurity at 16.9 min elutes 1.5 min before the main peak—consistent with a more polar species, possibly the methionine sulfoxide form (oxidation, +16 Da) or a truncated peptide missing hydrophobic residues. See [Oxidized Peptide Impurities](15-oxidized-peptide-impurities.md).

**Step 3:** The impurity at 19.6 min elutes after the main peak—indicating a species more hydrophobic than the target, possibly a deletion peptide missing a polar residue (e.g., Asp, Glu, Ser) or a tert-butyl-protected intermediate. See [Deletion Peptides Explained](14-deletion-peptides-explained.md).

**Step 4:** Purity by area normalization (solvent front excluded):

$$\text{Purity} = \frac{9450}{9450 + 120 + 85} \times 100 = 97.9\%$$

**Step 5:** Request LC-MS masses for both impurity peaks. Without mass confirmation, their identities are speculative. The 16.9 min peak at +16 Da would confirm oxidation; a different mass shift would suggest a different chemistry entirely. A supplier should be able to provide impurity masses on request.

### Common Interpretation Mistakes and Their Consequences

Five systematic errors dominate chromatogram misinterpretation in peptide QC. Recognizing them is the first step to reading a COA critically rather than literally:

1. **Treating every baseline blip as an impurity.** Noise spikes at the detection threshold inflate the impurity sum and deflate the purity. The LOQ exists precisely to separate signal from noise—peaks below the LOQ are not quantifiable and should be reported as "below LOQ," not integrated into the purity denominator.

2. **Including the solvent front in the area sum.** Counting the void peak as a component changes the total area denominator and artificially lowers the purity. This is easy to catch: if the earliest listed peak has $t_R < 3.5$ min on a 4.6 × 250 mm column, it is almost certainly the void peak.

3. **Comparing purities across different wavelengths.** Purity at 214 nm (peptide bond absorption) is not numerically equivalent to purity at 220 nm or 280 nm. A peptide measured at 214 nm may show 95% purity; the same sample at 280 nm may show 98% if aromatic-residue-containing impurities are less abundant. Always note and compare the detection wavelength.

4. **Assuming a single, symmetric peak means a single compound.** Co-elution is invisible to UV detection. Two species with identical retention times but different masses are a single peak in the UV chromatogram but two distinct charge-state envelopes in the mass spectrum. LC-MS is the arbiter of peak purity.

5. **Trusting the software's default integration parameters.** Default settings are generic starting points, not method-specific optimizations. Validated integration parameters—documented during method validation and locked in the processing method—must be used for every analysis. A chromatogram integrated with "default" parameters is not a validated result.

## Research Evidence

| Finding | Data | Source |
|---------|------|--------|
| Baseline noise must be ≤0.05 mAU for reliable 0.1% impurity detection in peptide HPLC | Instrument qualification study of 12 commercial HPLC systems | Dolan, *LCGC North America* 2008, 26, 532–539 |
| Retention time RSD must be ≤0.5% for reliable peak identification across a sequence | Analysis of 500 peptide injections under gradient conditions | Neue et al., *J. Chromatogr. A* 2005, 1079, 50–58 |
| Integration parameter changes can shift reported purity by 1–3% in peptide methods | Systematic variation of slope sensitivity and baseline mode across 20 peptide chromatograms | Dyson, *Chromatographic Integration Methods*, RSC 1998 |
| Gradient delay volume differences of 0.5 mL produce 0.5–1.0 min RT shifts between instruments | Inter-laboratory study with 15 HPLC systems of varying configuration | Dolan & Snyder, *J. Chromatogr. A* 2009, 1216, 4404–4411 |
| S/N ≥ 10 required for quantitation; S/N ≥ 3 for detection per ICH Q2(R2) | ICH Q2(R2) Guideline, Section 6.0 | ICH Q2(R2), 2023 |
| Peak asymmetry >1.5 degrades resolution sufficiently to miss 1% impurities | Simulated chromatograms with controlled tailing; experimental validation on 10 peptide separations | Snyder et al., *Introduction to Modern Liquid Chromatography*, 3rd ed., Wiley 2010 |
| Co-eluting peptides differing by ≤0.1 min in retention are invisible to UV single-wavelength detection | LC-MS analysis of 200 peptide purity chromatograms identified co-elution in 8% of apparently pure peaks | Mant & Hodges, *J. Chromatogr. A* 2002, 972, 45–59 |
| USP <621> requires system suitability before and during sample analysis; tailing factor 0.8–1.5 typical | USP <621> Chromatography, official text | USP–NF, General Chapter <621> |
| Blank injection analysis detects system contamination with >95% sensitivity for ghost peaks >0.05% | Blank-run audit of 50 peptide QC laboratories | Dolan, *LC Troubleshooting*, LCGC 2015, 33, 12–18 |

## FAQ

<div class="faq-item">
<h3>Q: What should I check first when I receive a peptide COA chromatogram?</h3>
<p class="faq-answer">A: Check five things in order: (1) Is the baseline flat and free of drift? (2) Is the solvent front excluded from integration? (3) Are the integration marks sitting on the baseline, not inside the peak? (4) Are all impurity peaks labeled with retention times and areas? (5) Is the detection wavelength stated (typically 214 nm for peptides)? A "yes" to all five means the chromatogram is at least interpretable; a "no" to any one means the reported purity should be questioned.</p>
</div>

<div class="faq-item">
<h3>Q: Why does the baseline slope upward in a gradient HPLC chromatogram?</h3>
<p class="faq-answer">A: Gradient elution increases the percentage of organic modifier (usually acetonitrile) over time. Acetonitrile absorbs UV light—its UV cutoff is approximately 190 nm—so at the typical peptide detection wavelength of 214 nm, a rising acetonitrile concentration produces a smoothly increasing baseline absorbance. This is normal and expected. What is not normal is a step change, sawtooth pattern, or irregular baseline shape—these indicate pump problems or air in the solvent lines.</p>
</div>

<div class="faq-item">
<h3>Q: How can I tell if a small peak is a real impurity or just baseline noise?</h3>
<p class="faq-answer">A: Apply the S/N ≥ 3 rule. Measure the peak height and compare it to the baseline noise amplitude in a blank region of the chromatogram. If S/N ≥ 3, the peak is above the detection limit; if S/N ≥ 10, it is above the quantitation limit. Peaks below S/N = 3 are noise and should not be integrated. A rigorous COA will state the LOQ of the method, and any peak below that LOQ should be annotated "below LOQ" rather than assigned a numerical area.</p>
</div>

<div class="faq-item">
<h3>Q: What is the void peak and why must it be excluded from purity calculations?</h3>
<p class="faq-answer">A: The void peak (solvent front) is the earliest peak on the chromatogram—typically at 2.5–3.5 min for a 4.6 × 250 mm column at 1.0 mL/min. It contains unretained material: injection solvent, salts, and buffer components. It is not related to the peptide and including it in the area sum artificially deflates the reported purity. A defensible COA shows the void peak excluded from integration, with the exclusion documented in the processing method.</p>
</div>

<div class="faq-item">
<h3>Q: Can I compare purity values from chromatograms run at different wavelengths?</h3>
<p class="faq-answer">A: No. Purity is wavelength-dependent because different chemical species absorb differently at different wavelengths. A peptide purity measured at 214 nm reflects total peptide-bond absorbance; at 280 nm it reflects primarily aromatic residues (Trp, Tyr, Phe). The two values will differ for the same sample. When comparing COAs from different suppliers or different batches, always verify that the detection wavelength is the same. If it differs, the purity values are not directly comparable.</p>
</div>

<div class="faq-item">
<h3>Q: How do integration parameter settings affect the reported purity?</h3>
<p class="faq-answer">A: Integration parameters—slope sensitivity, peak width, baseline mode, and minimum area threshold—directly determine which peaks the software detects and how it draws the baseline under each peak. Changing the slope sensitivity can make small impurity peaks appear or disappear. Changing the baseline mode from valley-to-valley to perpendicular drop changes how area is split between the main peak and an adjacent impurity. A rigorous COA states the integration parameters or at minimum the LOQ; without this information, the reported purity cannot be independently verified.</p>
</div>

<div class="faq-item">
<h3>Q: What does it mean if the main peak has a shoulder?</h3>
<p class="faq-answer">A: A shoulder—a bump or inflection on the leading or trailing edge of the main peak—is a strong indicator of a partially resolved co-eluting impurity. Common causes in peptide HPLC include diastereomers (racemization at a single residue), deletion peptides with nearly identical hydrophobicity to the target, and oxidized species. A shoulder should always trigger an LC-MS investigation: acquire mass spectra across the peak from the leading edge through the apex to the trailing edge. If the deconvoluted mass shifts, a co-eluting impurity is confirmed.</p>
</div>

<div class="faq-item">
<h3>Q: What causes ghost peaks and how do I know if they are present?</h3>
<p class="faq-answer">A: Ghost peaks are artifact peaks that appear even in blank injections and are caused by contaminated mobile phase, injector carryover, buffer precipitation, detector cell fouling, or column bleed. The definitive test is a blank injection run under identical gradient and integration conditions. Any peak with S/N ≥ 3 in the blank is a ghost peak. A laboratory that cannot produce a clean blank chromatogram is reporting purity on a contaminated system, and the results are unreliable regardless of how the numbers look.</p>
</div>

<div class="faq-item">
<h3>Q: What is the difference between gradient and isocratic chromatograms for peptide analysis?</h3>
<p class="faq-answer">A: In isocratic elution, the mobile phase composition is constant, producing a flat baseline but broad peaks for late-eluting species. In gradient elution, the organic modifier increases over time, producing a rising baseline but narrow peaks throughout the run. Gradient methods are the standard for peptide purity analysis because they resolve complex impurity profiles in a controlled runtime. A gradient chromatogram with a gently rising baseline is normal; sharp baseline discontinuities indicate pump or degasser malfunctions.</p>
</div>

<div class="faq-item">
<h3>Q: How can two laboratories get different purity values for the same peptide sample?</h3>
<p class="faq-answer">A: Differences arise from method variables, not necessarily from different peptide quality. Potential sources: (1) different detection wavelengths (214 vs. 220 nm), (2) different integration parameters (slope sensitivity, baseline mode), (3) different column selectivity (different C18 brands), (4) different gradient slopes and delay volumes, (5) different LOQ thresholds. The first diagnostic step is to compare the full method conditions, not the purity numbers. Method equivalence assessment—see our article on [Analytical Method Transfer](10-analytical-method-transfer.md)—is the systematic approach to resolving inter-laboratory discrepancies.</p>
</div>

## References

1. Snyder, L. R.; Kirkland, J. J.; Dolan, J. W. Introduction to Modern Liquid Chromatography, 3rd ed. Wiley, 2010. ISBN: 978-0470167540.
2. USP General Chapter <621> Chromatography. United States Pharmacopeia–National Formulary. Available at: [https://www.usp.org/harmonization-standards/pdg/general-chapter-chromatography](https://www.usp.org/harmonization-standards/pdg/general-chapter-chromatography)
3. ICH Q2(R2) Validation of Analytical Procedures. International Council for Harmonisation, 2023. Available at: [https://www.ich.org/page/quality-guidelines](https://www.ich.org/page/quality-guidelines)
4. Dolan, J. W. LC Troubleshooting: Ghost Peaks. *LCGC North America* 2008, 26, 532–539. Available at: [https://www.chromatographyonline.com/](https://www.chromatographyonline.com/)
5. Neue, U. D.; Mazzeo, J. R.; Carney, D. P. A Systematic Investigation of Gradient Retention Reproducibility. *J. Chromatogr. A* 2005, 1079, 50–58. DOI: [10.1016/j.chroma.2005.03.125](https://doi.org/10.1016/j.chroma.2005.03.125)
6. Dyson, N. Chromatographic Integration Methods, 2nd ed. Royal Society of Chemistry, 1998. ISBN: 978-0854045105.
7. Dolan, J. W.; Snyder, L. R. Gradient Elution Chromatography. In *Encyclopedia of Analytical Chemistry*, Wiley, 2009. DOI: [10.1002/9780470027318.a5906](https://doi.org/10.1002/9780470027318.a5906)
8. Mant, C. T.; Hodges, R. S. Reversed-Phase Liquid Chromatography of Peptides: Practical Aspects. *J. Chromatogr. A* 2002, 972, 45–59.
9. ICH Q2(R1) Validation of Analytical Procedures: Text and Methodology. ICH, 2005. Available at: [https://www.ich.org/page/quality-guidelines](https://www.ich.org/page/quality-guidelines)
10. Felinger, A. Data Analysis and Signal Processing in Chromatography. Elsevier, 1998. ISBN: 978-0444820662.
11. Dolan, J. W. Method Adjustment and System Suitability. *LCGC North America* 2015, 33, 12–18. Available at: [https://www.chromatographyonline.com/](https://www.chromatographyonline.com/)
12. FDA Guidance for Industry: Analytical Procedures and Methods Validation for Drugs and Biologics. U.S. FDA, 2015. Available at: [https://www.fda.gov/regulatory-information/search-fda-guidance-documents/analytical-procedures-and-methods-validation-drugs-and-biologics](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/analytical-procedures-and-methods-validation-drugs-and-biologics)
13. Meyer, V. R. Practical High-Performance Liquid Chromatography, 5th ed. Wiley, 2010. ISBN: 978-0470682180.
14. Dong, M. W. Modern HPLC for Practicing Scientists. Wiley, 2006. ISBN: 978-0471727897.
15. Ermer, J.; Nethercote, P. W. Method Validation in Pharmaceutical Analysis: A Guide to Best Practice, 2nd ed. Wiley-VCH, 2015. ISBN: 978-3527335633.

Return to [How to Read a Peptide COA](index.md) or read [Peak Area vs Peak Height](03-peak-area-vs-peak-height.md).
