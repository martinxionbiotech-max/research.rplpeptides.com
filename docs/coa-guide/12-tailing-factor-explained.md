---
title: "Tailing Factor Explained: Calculation, Causes, and Mitigation"
description: "Peak tailing in peptide HPLC: tailing factor T calculation, asymmetry causes (silanol interactions, overload, secondary retention), and mitigation strategies."
slug: tailing-factor-explained
category: Chromatography
tags: [Tailing Factor, Peak Shape, HPLC, Column Chemistry, System Suitability]
author: RPL Peptides Research Team
published: 2026-08-01
---

# Tailing Factor Explained: Calculation, Causes, and Mitigation

## Executive Summary

Peak tailing is the most visible sign of chromatographic ill-health in peptide HPLC. A tailing peak — one that rises sharply on its leading edge and falls gradually on its trailing edge — reduces resolution, compromises integration accuracy, and, most dangerously, can mask a small impurity eluting on the tail of the main peptide. The tailing factor T, defined by USP <621> and measured at 5% of peak height, quantifies this asymmetry: T = 1.0 is a perfectly symmetrical Gaussian peak, and T ≤ 1.5 is the standard acceptance criterion for quantitative analysis. When T exceeds 1.5, the reliability of the purity number on a peptide COA is compromised.

For peptide chemists and QC analysts, tailing is not merely an aesthetic defect. Peptide sequences rich in basic residues — lysine, arginine, histidine — are inherently prone to tailing because protonated amines interact electrostatically with residual acidic silanol groups on the silica stationary phase. This secondary ion-exchange retention mechanism slows the rear portion of the analyte band relative to the front, producing the characteristic asymmetric peak shape. The problem is well known, well studied, and, crucially, well mitigated: low pH mobile phases containing TFA, modern end-capped type-B silica columns, and elevated column temperatures together reduce tailing to acceptable levels for the vast majority of research peptides.

For the COA reader, the tailing factor is a diagnostic indicator. A COA that reports T = 1.08 for the main peak tells you the separation was clean and the integration was reliable. A COA that reports no tailing factor at all — or that reports T = 1.9 without investigation — tells you the laboratory either does not measure peak shape or does not act on the results. In peptide purity analysis, where impurities often elute within 0.5 minutes of the main peak, an unmeasured tail is an uncontrolled risk.

## Background

### Definition and Formula

The USP tailing factor T is defined at 5% of the peak height from the baseline — a point chosen because it is the region where tailing is most pronounced and most diagnostically informative:

$$T = \frac{W_{0.05}}{2f}$$

Where:

- W₀.₀₅ is the total peak width measured at 5% of peak height above the baseline.
- f is the distance from the leading edge of the peak (at 5% height) to the perpendicular dropped from the peak apex to the baseline.

For a perfectly symmetrical Gaussian peak, the leading half-width (f) equals the trailing half-width, so W₀.₀₅ = 2f and T = 1.0. When the peak tails, f is narrower than the trailing half-width, W₀.₀₅ > 2f, and T > 1.0. When the peak fronts, f is wider than the trailing half-width and T < 1.0.

The tailing factor is sometimes confused with the asymmetry factor As, which is measured at 10% of peak height and uses a different calculation convention:

$$A_s = \frac{b}{a}$$

Where a is the distance from the leading edge to the apex and b is the distance from the apex to the trailing edge, both at 10% height. As = 1.0 is symmetrical. For moderate tailing, T and As are related by the approximate relationship T ≈ 1.1 × As. The USP convention uses T at 5% height; the European Pharmacopoeia (Ph. Eur.) convention uses As at 10% height. Most peptide HPLC data systems can calculate both; the COA should note which is reported.

### Worked Example

A peak measured on a printed chromatogram has W₀.₀₅ = 1.20 cm and f = 0.55 cm:

$$T = \frac{1.20}{2 \times 0.55} = \frac{1.20}{1.10} = 1.09$$

A tailing factor of 1.09 indicates a nearly symmetrical peak with negligible tailing — the peak shape is effectively Gaussian and integration accuracy is not compromised by asymmetry.

A second example: the same measurement yields W₀.₀₅ = 1.40 cm and f = 0.40 cm:

$$T = \frac{1.40}{2 \times 0.40} = \frac{1.40}{0.80} = 1.75$$

T = 1.75 exceeds the standard acceptance criterion of 1.5. The integration of this peak is unreliable, resolution to the next-eluting peak is degraded, and the underlying cause — column chemistry, pH, overload, or contamination — must be investigated before the batch can be reported.

## Core Science

### Causes of Peak Tailing in Peptide HPLC

Peptide tailing has a limited set of root causes, each with a distinct diagnostic signature. Understanding the mechanism directs the mitigation to the correct variable.

| Cause | Mechanism | Diagnostic Signature |
|-------|-----------|---------------------|
| Silanol interactions | Protonated basic residues (Lys, Arg, His) bind electrostatically to ionized residual silanols (Si–O⁻) on the silica surface | Tailing worsens at pH 4–7; improves at pH 2–3; worse on older, non-end-capped columns |
| Column overload | The injected mass exceeds the linear capacity of the stationary phase; the adsorption isotherm becomes nonlinear | Tailing appears or worsens with increasing injection mass; disappears on 5× dilution |
| Secondary retention (mixed mode) | Simultaneous hydrophobic and ion-exchange retention creates two populations of analyte with different retention rates | pH- and buffer-dependent tailing; responds to ion-pairing agent concentration or buffer ionic strength |
| Injection solvent mismatch | Sample dissolved in a solvent with higher eluotropic strength than the starting mobile phase | Fronting with some tailing; affects early-eluting peaks more than late-eluting peaks |
| Column contamination | Strongly retained peptides, lipids, or particulates accumulate at the column head or on the stationary phase | Progressive tailing over multiple injections; improves temporarily after regeneration wash |
| Void volume / dead volume | Loose fittings, poorly cut tubing, or a void at the column head create unswept volume | Tail on all peaks, especially early-eluting ones; injection-marker peak (uracil) also shows tailing |
| Detector flow-cell effects | Oversized detector flow cell or poor cell geometry causes band broadening after separation | Affects early peaks more than late peaks; independent of column chemistry |

### Why Peptides Are Particularly Prone to Tailing

Peptides are among the most tailing-prone analytes in reversed-phase HPLC. The reason is structural: peptides carry multiple basic residues. At the standard working pH of 2–3, these residues are fully protonated (Lys ε-NH₃⁺, Arg guanidinium⁺, His imidazolium⁺), and the peptide carries a net positive charge that depends on the balance of basic versus acidic residues.

Residual silanols on the silica surface are weakly acidic (pKa of isolated silanols ≈ 3.5–5 in the presence of acetonitrile). At pH 3–4, a significant fraction of silanols is ionized (Si–O⁻), creating cation-exchange sites. The protonated peptide amines interact electrostatically with these sites in addition to the hydrophobic reversed-phase interaction. This mixed-mode retention — RP + IEC — slows the transfer of some peptide molecules relative to others, broadening the peak tail.

This is why several best practices in peptide HPLC are specifically anti-tailing measures:

- **Low-pH mobile phases (pH 2–3) protonate silanols** (Si–OH, neutral) and suppress the ion-exchange mechanism.
- **TFA ion-pairs with basic residues**, masking the positive charge and reducing electrostatic attraction to residual silanols. See [Reverse Phase HPLC for Peptides](../coa-guide/11-reverse-phase-hplc-for-peptides.md).
- **Modern type-B silica** has far fewer residual metals (aluminum, iron) in the silica matrix, and its silanols are less acidic and less abundant than type-A silicas used before the 1990s.
- **End-capping** — a secondary reaction that caps residual silanols with a small silane (typically trimethylsilane) — further reduces silanol exposure. Well-end-capped C18 columns show tailing factors of 1.0–1.2 for most peptides.

### Effect of Tailing on Purity Calculations

Tailing affects integration — and therefore the reported purity — in three ways, each introducing a different bias direction and magnitude.

1. **Truncated integration of the main peak.** Integration software defines the peak end when the signal drops below a threshold or when the second derivative of the signal passes through zero. On a tailing peak, the slowly descending tail region may fall below the integration threshold before the peak has fully returned to baseline, cutting off a fraction of the peak's true area. The main peak area is underestimated, and the reported purity is correspondingly underestimated. The error is typically small (0.1–0.3%) for moderate tailing (T < 1.5) but grows rapidly for T > 2.0.

2. **Incorrect baseline placement between overlapping peaks.** When a small impurity elutes on the tail of the main peak, the integration software must decide where the main peak ends and the impurity begins. On a tailing main peak, the valley between the two peaks may never reach the true baseline. Valley-to-valley integration splits the area at the lowest point, potentially assigning part of the impurity's area to the main peak (purity overstated) or part of the main peak's tail to the impurity (impurity level overstated). See [Peak Area vs Peak Height](../coa-guide/03-peak-area-vs-peak-height.md) for a detailed discussion of integration modes.

3. **Hidden impurities.** The most dangerous consequence of tailing: a small impurity that elutes into the tail region of the main peak may not be detected by the integration software at all, because the slope of the main peak's trailing edge masks the impurity's rise. The impurity is present, it absorbs at the detection wavelength, but it contributes to the main peak's area rather than appearing as a separate integrated peak. The reported purity is inflated, and neither the COA nor the chromatogram provides evidence of the hidden impurity. This is the mechanism by which tailing T > 1.5 becomes a direct threat to the purity claim. See [Resolution in Chromatography](../coa-guide/13-resolution-in-chromatography.md) for the quantitative relationship between tailing and hidden impurities.

### Peak Fronting (Anti-Tailing)

Fronting — the peak leans to the left, with a gradual rise and a sharp descent — is the opposite shape distortion. While less common than tailing in peptide HPLC, fronting has its own diagnostic value:

- **Column overload:** when the injected mass exceeds the stationary phase's linear capacity, the adsorption isotherm is concave at high concentration, producing a fronting peak. Dilute the sample by a factor of five and re-inject; if the peak shape becomes symmetrical, overload is confirmed.
- **Injection solvent too strong:** if the peptide is dissolved in a solvent with higher eluotropic strength than the starting mobile phase composition (e.g., 50% acetonitrile in a gradient starting at 5% acetonitrile), the plug of strong solvent poorly focuses the sample at the column head, producing a distorted, often fronting, peak shape. Match the sample solvent to the starting mobile phase composition — or use a weaker solvent — to eliminate this problem.

### Tailing, Resolution, and the Hidden Impurity Problem

The practical danger of tailing is not aesthetic — it is that tailing hides impurities. When the main peak tails, the tail region overlaps the elution window of the next peak. The quantitative relationship between tailing and resolution is direct: a peak with T = 2.0 has an effective width approximately 1.5× that of a symmetrical peak, and resolution to an adjacent peak falls in rough proportion.

Consider a method where the main peptide and its nearest-eluting impurity are separated by Rs = 1.5 (baseline) on a new column with T = 1.1. Six months later, the same column shows T = 1.8 for the main peak. The resolution has dropped to approximately Rs = 0.9–1.1 — peaks that were baseline-separated now overlap significantly. The impurity is still present at the same concentration, but the integration software may no longer recognize it as a separate peak. The reported purity has risen, not because the batch is purer, but because the column degraded.

This scenario — silent resolution loss driven by tailing increase that precedes plate-count decline — is the earliest warning of column aging and the most compelling reason to monitor the tailing factor trend in SST records, not just its pass/fail snapshot. See [System Suitability Testing](../coa-guide/09-system-suitability-testing.md) for the SST monitoring framework.

### Measuring Tailing Under Realistic Conditions

The tailing factor is a straightforward calculation that becomes unreliable under non-ideal conditions:

1. **Baseline drift:** the 5% height measurement assumes a stable, flat baseline under the peak. A drifting baseline — from gradient slope with mismatched TFA concentrations, TFA absorbance drift, or temperature effects — biases the measured f and W₀.₀₅. Subtract a blank injection's baseline trace or correct the baseline before measuring.
2. **Co-eluting impurities:** a shoulder or closely eluting impurity on the trailing edge of the main peak distorts the tail and inflates T even when the main peak itself is inherently symmetrical. T measured on a partially resolved peak is a measure of overlap, not of peak shape. Measure T on the reference standard injection — clean matrix, single component — for a true assessment of column performance.
3. **Noise at 5% height:** at 5% of a moderate-sized peak, detector noise can make the width measurement uncertain. Smoothing (Savitzky-Golay, boxcar) may be necessary, but over-smoothing artificially narrows the peak and produces a falsely low T. Most CDS software applies moderate smoothing by default; the parameters should be documented and consistent.

## Research Evidence

| Finding | Data | Source |
|---------|------|--------|
| USP tailing factor T ≤ 1.5 is the standard acceptance criterion for quantitative HPLC | USP <621> defines T at 5% peak height and sets T ≤ 1.5 for most assay applications | USP General Chapter <621>, Chromatography (2023) |
| Peptide tailing is primarily caused by silanol interactions with basic residues; low pH and TFA mitigate it | Systematic study of 12 model peptides on C18 columns with pH 2–7; tailing minimized at pH 2–3 with 0.1% TFA | Mant, C. T.; Hodges, R. S. *J. Chromatogr. A* 2002, 972, 61–75 |
| Type-B silica and end-capping reduce peptide tailing by 40–60% compared to type-A silica | Head-to-head comparison of tailing for 20 peptides on type-A vs. type-B C18 columns | Neue, U. D. *HPLC Columns*, Wiley-VCH, 1997 |
| TFA concentration of 0.05–0.1% is optimal; higher concentrations do not further reduce tailing | Tailing factor vs. TFA concentration 0.01–0.5% for 6 basic peptides; plateau at 0.05% | Shibue, M.; Mant, C. T.; Hodges, R. S. *J. Chromatogr. A* 2005, 1080, 58–67 |
| Column temperature of 40–60 °C reduces peptide tailing by 20–30% relative to 25 °C | Tailing factor as function of temperature (20–80 °C) for 10 peptides on C18 with TFA | Chen, Y.; Mant, C. T.; Hodges, R. S. *J. Chromatogr. A* 2003, 1010, 45–61 |
| Tailing T > 1.5 can mask impurities contributing 1–2% of total area under the tail | Simulation study of peak overlap as function of tailing factor and concentration ratio | Dolan, J. W. *LCGC North America* 2003, 21(11), 1076–1082 |
| Column overload tailing is detectable above approximately 10 µg for a 4.6 mm C18 column; 1–5 µg typically linear | Mass load study for peptides on 4.6 mm and 2.1 mm columns; linear range limits | Snyder, L. R.; Kirkland, J. J.; Dolan, J. W. *Introduction to Modern Liquid Chromatography*, 3rd ed., 2010 |
| HFBA reduces tailing for highly basic peptides (≥3 Arg/Lys) more effectively than TFA | Tailing comparison: TFA (0.1%) vs. HFBA (0.02%) for poly-Arg peptides; T reduced by 0.3–0.5 units with HFBA | Mant, C. T.; Hodges, R. S. *J. Chromatogr. A* 2002, 972, 61–75 |
| Tailing factor trend (ΔT > 0.2 over column life) is the earliest indicator of column aging, preceding plate count drop | Column lifetime study tracking T, N, and backpressure for 500 peptide injections | Dolan, J. W. *LCGC North America* 2002, 20(5), 438–444 |
| Epimerization and Pro cis/trans isomerization produce doublet peaks, not tailing — a different diagnostic | Case studies distinguishing tailing from conformational peak splitting in peptide HPLC | Gesquière, J. C.; et al. *J. Chromatogr.* 1989, 480, 295–310 |

## Mitigation Strategies

The appropriate tailing mitigation depends on the diagnosed cause. The table below maps the symptom to the corrective action:

| Strategy | When to Apply | Mechanism |
|----------|--------------|-----------|
| Lower pH to 2 (0.1% TFA) | Tailing attributed to silanol interactions; standard for all peptide methods | Protonates residual silanols, suppressing ion-exchange retention |
| Add ion-pairing agent (TFA 0.1%, HFBA 0.02%) | Basic peptides; tailing that persists at pH 2 | Masks positive charge on Lys/Arg, reducing electrostatic silanol interaction |
| Reduce mass load | Tailing that disappears on 5× dilution; overload pattern | Restores linear adsorption isotherm |
| Change to modern end-capped C18 column | Tailing on older column; type-A silica; un-end-capped phase | Fewer, less acidic silanols; chemical end-capping blocks residual sites |
| Increase column temperature to 40–60 °C | General peptide tailing; improves both peak shape and efficiency | Accelerates silanol exchange kinetics; increases diffusion rates |
| Add amine modifier (triethylamine 0.1%) | Very basic peptides; strong silanol tailing | Competes with peptide for silanol sites; masks silanol interaction |
| Regenerate or replace column | Progressive tailing; failure to recover after regeneration | Removes adsorbed contaminants; replaces degraded bonded phase |
| Match injection solvent to starting mobile phase | Fronting plus tailing; solvent mismatch signature | Eliminates solvent-strength gradient at column head during sample focusing |

### Tailing and Column Lifecycle Management

Tailing is the earliest, most sensitive indicator of column aging — more responsive than plate count or backpressure changes. A well-maintained C18 column at pH 2 with TFA will show a slow, monotonic increase in T for the same reference standard across its working life. The SST trend record reveals this increase weeks or months before the column fails a plate-count criterion.

Practical column lifecycle practices that integrate tailing monitoring:

1. **Record T for the reference standard in a column log at every use.** A column whose T rises from 1.05 to 1.38 over 400 injections is aging predictably; a column whose T jumps from 1.10 to 1.85 between two sequences has experienced a specific event (contaminated sample, mobile phase error, pressure shock).
2. **Set a column retirement criterion based on T.** For example: retire the column when T exceeds 1.6 for the reference standard, or when the plate count has dropped 20% from the column's baseline, whichever occurs first. This criterion should be in the column management SOP.
3. **Track the effect of regeneration washes on T.** A column whose T returns to near-baseline after a regeneration wash is contaminated, not degraded — contamination is reversible. A column whose T is unchanged after regeneration is degraded — replacement is the only remedy.
4. **Keep the column history with the batch records.** When auditing a COA, a tailing factor of 1.40 may be acceptable on a column at 80% of its rated lifetime; the same value on a brand-new column signals a method or system problem. Without the column history, the T value lacks context.

## Key Takeaways

- The tailing factor T = W₀.₀₅ / 2f (5% height); T ≤ 1.5 is the standard USP acceptance criterion; T = 1.0 is perfect symmetry.
- Peptide tailing is overwhelmingly caused by electrostatic interactions between protonated basic residues and residual silanols — mitigated by low pH (TFA), end-capped columns, and elevated temperature.
- Column overload and injection-solvent mismatch also cause tailing; dilute the sample to check.
- Tailing distorts purity in both directions: truncated integration understates the main peak, and hidden impurities on the tail inflate the reported purity.
- The tailing trend (ΔT over column life) is a more informative diagnostic than the pass/fail snapshot at any single time point.
- A COA's chromatogram showing T > 1.5 for the main peak is a reliability red flag for the purity result.

## FAQ

<div class="faq-item">
<h3>Q: What is the tailing factor and how is it calculated?</h3>
<p class="faq-answer">A: The USP tailing factor T is a measure of peak symmetry, calculated as T = W₀.₀₅ / 2f, where W₀.₀₅ is the peak width at 5% of peak height and f is the distance from the leading edge to the apex at that height. T = 1.0 is a perfectly symmetrical Gaussian peak; T > 1.0 indicates tailing (the rear of the peak is broader than the front); T < 1.0 indicates fronting.</p>
</div>

<div class="faq-item">
<h3>Q: What is the acceptable tailing factor for peptide HPLC?</h3>
<p class="faq-answer">A: USP <621> specifies T ≤ 1.5 as the general acceptance criterion for quantitative analysis. For peptide purity methods, laboratories commonly aim for T ≤ 1.3 during method development, with T ≤ 1.5 as the SST limit. A tailing factor above 1.5 compromises integration accuracy and risks masking small impurities eluting on the main peak's tail.</p>
</div>

<div class="faq-item">
<h3>Q: Why do peptides tail more than small-molecule drugs?</h3>
<p class="faq-answer">A: Peptides carry multiple basic residues (Lys, Arg, His) that are protonated at the standard working pH of 2–3. These protonated amines interact electrostatically with residual ionized silanols (Si–O⁻) on the silica stationary phase, creating a secondary ion-exchange retention mechanism that slows the rear portion of the analyte band. Small-molecule drugs typically have fewer charged groups and are less prone to this mixed-mode tailing.</p>
</div>

<div class="faq-item">
<h3>Q: What is the difference between tailing factor (T) and asymmetry factor (As)?</h3>
<p class="faq-answer">A: The tailing factor T is measured at 5% of peak height using the USP convention: T = W₀.₀₅ / 2f. The asymmetry factor As is measured at 10% of peak height: As = b/a, where a is the front half-width and b is the rear half-width. For moderate tailing, T ≈ 1.1 × As. USP <621> uses T; the European Pharmacopoeia uses As. Most modern CDS software can report both, and the COA should state which is used.</p>
</div>

<div class="faq-item">
<h3>Q: How does tailing affect the reported purity?</h3>
<p class="faq-answer">A: Tailing affects purity in three ways: (1) truncated integration may cut off part of the main peak's tail, underestimating peak area and purity; (2) a tailing main peak complicates valley-to-valley integration with an adjacent impurity, potentially misallocating area; (3) a small impurity eluting on the tail of a badly tailing main peak (T > 1.5) may not be detected at all, inflating the reported purity. The hidden-impurity problem is the most serious consequence of tailing.</p>
</div>

<div class="faq-item">
<h3>Q: How can I reduce tailing in my peptide HPLC method?</h3>
<p class="faq-answer">A: The standard anti-tailing measures, ordered from most to least effective, are: (1) use 0.1% TFA at pH ~2 to protonate silanols; (2) use a modern end-capped C18 column with type-B silica; (3) operate at 40–60 °C column temperature; (4) reduce the injected mass (typically below 10 µg for a 4.6 mm column); (5) for very basic peptides, try HFBA (0.01–0.02%) or triethylamine phosphate as the ion-pairing agent; (6) regenerate or replace the column if tailing has progressively worsened over multiple sequences.</p>
</div>

<div class="faq-item">
<h3>Q: What causes peak fronting instead of tailing?</h3>
<p class="faq-answer">A: Fronting (the peak leans left, with a gradual rise and sharp descent) is usually caused by column overload — the injected mass exceeds the stationary phase's linear capacity — or by injecting the sample in a solvent that is stronger (higher organic content) than the starting mobile phase. Diluting the sample and re-injecting, or matching the sample solvent to the mobile phase starting composition, resolves fronting in most cases.</p>
</div>

<div class="faq-item">
<h3>Q: Can peak tailing hide impurities?</h3>
<p class="faq-answer">A: Yes, and this is the most dangerous consequence of tailing. When the main peak tails significantly (T > 1.5), a small impurity eluting on the trailing edge may fall below the integration software's detection threshold because the slope of the main peak's tail masks the impurity's signal. The impurity contributes to the main peak's integrated area, inflating the reported purity. The only defense is to maintain T ≤ 1.5 through proper method development and column maintenance.</p>
</div>

<div class="faq-item">
<h3>Q: Is tailing always caused by column chemistry?</h3>
<p class="faq-answer">A: No. While silanol interactions are the most common cause of peptide tailing, other causes include: column overload (too much mass injected), injection solvent mismatch (sample in a stronger solvent than the starting mobile phase), column contamination (adsorbed peptides or lipids), void volume in the system (loose fittings or a void at the column head), and detector flow-cell effects (oversized cell causing extra-column band broadening). Each cause produces a different diagnostic pattern and requires a different corrective action.</p>
</div>

<div class="faq-item">
<h3>Q: How should I monitor tailing as a column ages?</h3>
<p class="faq-answer">A: Record T for the reference standard at every use in a column log. Set a retirement criterion — for example, retire when T exceeds 1.6 or plate count drops 20% from baseline, whichever occurs first. A gradual increase in T (e.g., from 1.05 to 1.40 over 400 injections) is normal aging; a sudden jump signals a specific event. Track the response to regeneration washes: a return to baseline T after wash indicates contamination; no improvement indicates bonded-phase degradation and signals replacement.</p>
</div>

## References

1. USP General Chapter <621> Chromatography. United States Pharmacopeia–National Formulary, USP 46–NF 41. Rockville, MD: United States Pharmacopeial Convention; 2023.
2. Mant, C. T.; Hodges, R. S. Reversed-Phase Liquid Chromatography of Peptides: Practical Aspects of Column Selection and Mobile Phase Optimization. *J. Chromatogr. A* 2002, 972(1), 61–75. doi:10.1016/S0021-9673(02)01074-2
3. Neue, U. D. *HPLC Columns: Theory, Technology, and Practice*. New York: Wiley-VCH; 1997.
4. Shibue, M.; Mant, C. T.; Hodges, R. S. Effect of Anionic Ion-Pairing Agent Concentration on Peptide Retention in Reversed-Phase Chromatography. *J. Chromatogr. A* 2005, 1080(1), 58–67. doi:10.1016/j.chroma.2005.02.063
5. Chen, Y.; Mant, C. T.; Hodges, R. S. Temperature Selectivity Effects in Reversed-Phase Liquid Chromatography of Peptides. *J. Chromatogr. A* 2003, 1010(1), 45–61. doi:10.1016/S0021-9673(03)01032-X
6. Dolan, J. W. Peak Tailing and Resolution. *LCGC North America* 2003, 21(11), 1076–1082.
7. Snyder, L. R.; Kirkland, J. J.; Dolan, J. W. *Introduction to Modern Liquid Chromatography*, 3rd ed. Hoboken, NJ: John Wiley & Sons; 2010. doi:10.1002/9780470508183
8. Dolan, J. W. Column Care and Use. *LCGC North America* 2002, 20(5), 438–444.
9. Gesquière, J. C.; Diesis, E.; Cung, M. T.; Tartar, A. Slow Isomerization of Some Proline-Containing Peptides. *J. Chromatogr.* 1989, 480, 295–310.
10. European Pharmacopoeia 11th Edition, Chapter 2.2.46: Chromatographic Separation Techniques. Strasbourg: European Directorate for the Quality of Medicines & HealthCare; 2023.
11. Mant, C. T.; Hodges, R. S. *HPLC of Peptides and Proteins: Separation and Analysis*. Totowa, NJ: Humana Press; 1991. doi:10.1007/978-1-4612-3562-2
12. Dolan, J. W. Troubleshooting LC Column Problems. *LCGC North America* 2010, 28(10), 858–866.
13. Kirkland, J. J.; van Straten, M. A.; Claessens, H. A. High pH Mobile Phase Effects on Silica-Based Reversed-Phase Columns. *J. Chromatogr. A* 1995, 691(1–2), 3–19. doi:10.1016/0021-9673(94)00831-S
14. Nawrocki, J. The Silanol Group and Its Role in Liquid Chromatography. *J. Chromatogr. A* 1997, 779(1–2), 29–71. doi:10.1016/S0021-9673(97)00410-0
15. Gritti, F.; Guiochon, G. Mass Transfer Kinetics, Band Broadening and Column Efficiency. *J. Chromatogr. A* 2012, 1221, 2–40. doi:10.1016/j.chroma.2011.04.058
16. Bidlingmeyer, B. A. *Practical HPLC Methodology and Applications*. New York: John Wiley & Sons; 1992.

Return to [How to Read a Peptide COA](../coa-guide/index.md) or read [Resolution in Chromatography](../coa-guide/13-resolution-in-chromatography.md).
