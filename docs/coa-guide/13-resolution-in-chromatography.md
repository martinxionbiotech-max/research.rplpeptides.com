---
title: "Resolution in Chromatography: Formula, Peak Overlap, and Optimization"
description: "Chromatographic resolution Rs explained: the resolution equation, USP and EP calculation methods, peak overlap, and strategies to improve separation."
slug: resolution-in-chromatography
category: Chromatography
tags: [Resolution, Chromatography, HPLC, Peak Separation, Efficiency]
author: RPL Peptides Research Team
published: 2026-08-01
---

# Resolution in Chromatography: Formula, Peak Overlap, and Optimization

## Executive Summary

Resolution Rs — the degree of separation between two adjacent chromatographic peaks — is the single most important quality metric for a peptide purity method. Without demonstrated resolution between the main peptide and its critical impurities, the reported purity is an assumption, not a measurement: the chromatogram shows a single peak, but that peak may contain two, three, or more co-eluting species. In the research peptide industry, where deletion peptides differ from the parent by a single missing amino acid and oxidized forms differ by a single oxygen atom, the margin between a resolved impurity and a hidden one is often less than 0.5 minutes of retention time on a 30-minute gradient — and the Rs value quantifies whether that margin is sufficient.

For laboratory managers and QC directors, the practical significance of resolution is that it functions as the gatekeeper of every purity number. A method that was validated with Rs ≥ 1.5 against the known impurity set (deletion, oxidation, epimerization, dimerization) has demonstrated specificity — the ability to measure the main peptide in the presence of those impurities without interference. A method that was never tested for its critical-pair resolution has not demonstrated specificity, regardless of what other validation parameters (precision, linearity, accuracy) may have been checked. The chain of evidence is: known impurity set → identified critical pair → validated Rs ≥ 1.5 → SST check per batch → trustworthy purity. Each link must be present; a break at any point compromises the purity claim.

For the peptide buyer, resolution is the most important number on a COA after the purity itself. A COA that reports "Resolution (main peak / N-1 deletion): 1.8" tells you the method can see the most likely co-eluting impurity. A COA that reports "Resolution: 2.5" without identifying the peak pair may be reporting the separation between the main peak and a distant, well-resolved impurity — a number designed to look good rather than to provide assurance. Asking "which two peaks are you measuring Rs between?" is one of the most informative questions a buyer can ask about a COA method.

## Background

### The Resolution Equation

Resolution is defined as the distance between two peak maxima divided by the average of their baseline widths. For the USP convention using tangent baseline widths:

$$R_s = \frac{2(t_{R2} - t_{R1})}{W_1 + W_2}$$

Where tR₁ and tR₂ are the retention times of the earlier- and later-eluting peaks, and W₁ and W₂ are their baseline widths measured by the tangent method — the intersections of the tangent lines drawn at the inflection points with the baseline.

### Worked Example

Two peptide peaks elute at tR₁ = 12.0 minutes and tR₂ = 12.6 minutes, with baseline widths W₁ = W₂ = 0.4 minutes:

$$R_s = \frac{2(12.6 - 12.0)}{0.4 + 0.4} = \frac{1.2}{0.8} = 1.5$$

Rs = 1.5 is the widely cited threshold for "baseline separation" — the valley between the peaks returns to the baseline, and the area of each peak can be integrated reliably without cross-contamination.

### Peak Overlap as a Function of Resolution

Resolution is a continuous variable, and the degree of peak overlap transitions smoothly from complete co-elution to complete separation:

| Rs | Percent Overlap | Quantitative Interpretation |
|:--:|:--------------:|-----------------------------|
| 0.5 | ~16% | Peaks barely distinguishable as a shoulder; quantitative integration impossible; purity number meaningless |
| 0.8 | ~5% | Partial separation visible but valley >50% of peak height; quantitation unreliable |
| 1.0 | ~2.3% | Peaks resolved but significant overlap; 2–4% mutual area contamination; not acceptable for purity assays |
| 1.25 | ~0.6% | Approaching acceptable; minor overlap at the 1% level |
| 1.5 | ~0.1% | Baseline separation; overlap <0.1% of peak area; standard quantitation criterion |
| 2.0 | Negligible | Excellent separation; appropriate for trace-level impurity quantitation (≤0.1%) |
| 2.5 | Undetectable | Overlap is below the integration noise threshold |

The values in this table are calculated for equal-height Gaussian peaks. When the peaks are of unequal height — the common situation in purity assays, where the impurity is 100–1000× smaller than the main peak — the overlap asymmetry changes the quantitative interpretation. A small impurity riding on the tail of a large main peak experiences proportionally more overlap than the table suggests. This is why many regulatory methods specify Rs ≥ 2.0 for the critical pair when low-level impurities (≤0.5%) are quantitated: the safety margin compensates for the peak-height asymmetry.

### USP vs. EP Resolution Calculation

Two pharmacopeial conventions exist, and they produce numerically different Rs values from the same chromatogram:

| Convention | Formula | Width Measurement | Comment |
|------------|---------|-------------------|---------|
| USP <621> | Rs = 2(tR₂ − tR₁) / (W₁ + W₂) | Baseline widths (tangent method) | Standard in US and most of Asia; more sensitive to peak shape |
| EP/BP 2.2.46 | Rs = 1.18(tR₂ − tR₁) / (W₁,₀.₅ + W₂,₀.₅) | Widths at half-height | Standard in Europe; easier to measure on noisy baselines |

The factor 1.18 in the EP formula accounts for the relationship between half-height width (W₀.₅) and baseline width (W₁) for a true Gaussian peak: W₁ ≈ 1.699 × W₀.₅, and inserting this into the USP formula yields the EP conversion. For perfectly Gaussian peaks, both formulas give the same Rs. For tailing peaks — the norm in peptide HPLC — the USP value is typically lower (more conservative) than the EP value because tailing increases the baseline width more than the half-height width.

When reading a COA, always check which convention is used. A COA quoting Rs = 1.5 by the EP convention may correspond to Rs ≈ 1.2–1.4 by the USP convention — a meaningful difference if the acceptance criterion is set per USP. The CDS software's resolution calculation method must be verified and documented in the method SOP.

## Core Science

### The Fundamental Resolution Equation

Resolution is not a single property but the product of three independent factors, each of which can be manipulated independently during method development:

$$R_s = \frac{\sqrt{N}}{4} \cdot \frac{\alpha - 1}{\alpha} \cdot \frac{k'_2}{1 + k'_2}$$

This equation — sometimes called the Purnell equation in its isocratic form — partitions resolution into:

- **Efficiency term:** √N / 4, where N is the plate count. Doubling N (e.g., by switching from a 150 mm to a 250 mm column, or from 5 μm to 3 μm particles) increases Rs by a factor of √2 ≈ 1.41 (a 41% improvement).
- **Selectivity term:** (α − 1) / α, where α = k'₂ / k'₁ is the selectivity factor. This term is the most powerful optimization lever: a small improvement in α produces a disproportionately large increase in Rs. For example, increasing α from 1.05 to 1.10 (a 5% increase in relative retention) can increase Rs by approximately 50–100%, depending on the absolute value.
- **Retention term:** k'₂ / (1 + k'₂), where k'₂ is the capacity factor of the later-eluting peak. This term approaches 1 as k' becomes large and drops sharply as k' falls below approximately 2. For gradient elution, the effective capacity factor k* replaces k', and the retention term behaves analogously.

The fundamental equation teaches the method developer where to invest effort. Efficiency improvements (longer column, smaller particles) are expensive in time and backpressure and yield only √N returns. Selectivity improvements — changing the organic modifier, adjusting pH, switching ion-pairing agents — are often cheaper, faster, and produce larger Rs gains. The practical rule: optimize selectivity first, then adjust efficiency and retention to fine-tune.

### Why Resolution Fails in Peptide Purity Methods

Resolution failure in peptide HPLC has a finite set of causes, most of which are specific to the chemistry of peptide impurities:

1. **Co-eluting deletion peptides:** an N-1 deletion analog differs from the parent by a single amino acid — a mass difference of 57–186 Da but, depending on which residue is missing, a hydrophobicity difference that may be too small for the gradient to resolve. Hydrophobic-residue deletions (Leu, Phe, Trp) usually produce adequate ΔtR; hydrophilic-residue deletions (Gly, Ser) often produce co-elution. See [Deletion Peptides Explained](../coa-guide/14-deletion-peptides-explained.md).
2. **Oxidized forms:** methionine sulfoxide is more polar than methionine and elutes earlier on RP-HPLC, but the ΔtR may be only 0.3–0.5 minutes under a typical gradient. If the main peak width at baseline is 0.4 minutes, a 0.4-minute ΔtR gives Rs ≈ 1.0 — resolved but not baseline-separated. See [Oxidized Peptide Impurities](../coa-guide/15-oxidized-peptide-impurities.md).
3. **Diastereomers from epimerization:** racemized residues produce species with identical mass and near-identical hydrophobicity — the hardest separation in peptide chromatography. Resolution below 1.0 is common, and some epimers may never be separable on C18 with any mobile phase combination.
4. **Column aging:** plate count drops, peaks broaden, and Rs falls below 1.5 even though the retention times and selectivity are unchanged. This is a column maintenance problem detected by SST, not a method problem.
5. **Gradient slope not optimized:** a gradient that is too steep compresses the elution window, reducing ΔtR between peaks. The slope may have been adequate for the validation batch but insufficient for a batch with a different impurity distribution.

### Optimization Strategies: How to Improve Resolution

The table below organizes resolution optimization strategies by which term in the fundamental equation they target:

| Lever | Specific Action | Effect on Rs | Mechanism |
|-------|----------------|:-----------:|-----------|
| Selectivity (α) | Change organic modifier (ACN → MeOH → THF mixtures) | Largest | Changes relative partitioning of peptide and impurity |
| Selectivity (α) | Adjust pH (2.0 → 2.5 → 3.0) | Large | Changes ionization state of specific residues |
| Selectivity (α) | Change ion-pairing agent (TFA → HFBA → PFPA) | Large | Alters relative hydrophobicity of charged species |
| Selectivity (α) | Change column chemistry (C18 → C8 → C4 → phenyl) | Large | Different stationary phase selectivity |
| Efficiency (N) | Longer column (150 → 250 mm) | ∝ √N | More theoretical plates |
| Efficiency (N) | Smaller particles (5 → 3 → sub-2 μm) | ∝ √N | Higher plate count per unit length |
| Efficiency (N) | Higher temperature (40 → 60 °C) | Moderate | Increases diffusion; reduces mass-transfer broadening |
| Efficiency (N) | Lower flow rate (1.0 → 0.5 mL/min) | Small–moderate | Closer to van Deemter optimum velocity |
| Retention (k') | Weaker starting mobile phase (10% → 5% B) | Moderate | Elution starts later; peaks spend more time in column |
| Retention (k') | Shallower gradient slope (2% → 0.5% B/min) | Moderate–large | Spreads peaks further apart in time |

For a resolution-critical pair — the main peak versus the most difficult impurity — the most productive approach is a targeted method development experiment. Screen organic modifiers (acetonitrile, methanol, 50:50 ACN–MeOH, 5% THF) at two pH values (2.0 with TFA, 3.0 with formate) on the critical pair. The modifier–pH combination that maximizes ΔtR is the starting point for gradient optimization. This experiment requires 6–12 injections and typically identifies a selectivity improvement within a morning's work.

### Resolution in Two Dimensions: Peak Purity Assessment and the Co-Elution Blind Spot

Resolution is only meaningful between *known* peak pairs — peaks the method developer has identified and tested. Two compounds that co-elute perfectly (Rs = 0) produce a single chromatographic peak, and the chromatogram cannot reveal them. This is the fundamental blind spot of one-dimensional chromatography, and it is the reason that a "single peak by HPLC" claim proves nothing about whether that peak contains one species or several.

Several tools address this blind spot, each with limitations:

- **Diode-array detection (DAD) peak purity:** the UV spectrum is recorded across the eluting peak. If the spectrum changes across the peak (spectral inhomogeneity), a co-eluting species with a different chromophore is likely present. However, two peptides often have very similar UV spectra — both are backbone-heavy at 214 nm — and spectral similarity does not guarantee chemical homogeneity. DAD purity is a useful flag but a weak proof.
- **LC-MS extracted ion monitoring:** the mass spectrometer records signal at the mass-to-charge ratios of the expected peptide and its potential impurities (deletion, oxidation, adducts). Extracted ion chromatograms at different m/z values reveal whether a single UV peak contains species of different masses. This is the definitive co-elution check and should be part of any peptide purity method's specificity validation. See [Understanding LC-MS Reports](../coa-guide/01-understanding-lc-ms-reports.md).
- **Orthogonal separations:** capillary electrophoresis (CE) separates by charge-to-size ratio, orthogonal to RP-HPLC's hydrophobicity-based separation. A species that co-elutes by HPLC may resolve by CE, and vice versa. Combining HPLC with CE or another orthogonal technique provides the most complete evidence of chromatographic purity.

### Baseline Separation vs. Practically Acceptable Separation

Rs = 1.5 is "baseline separation" for equal-height Gaussian peaks, but the real criterion for a purity method is practical: can the impurity be integrated accurately in the presence of the main peak? When the impurity is much smaller than the main peak (the common case: 99% main peak and 0.5% impurity), valley-to-valley integration at Rs = 1.5 can still bias the small peak's area downward by 10–20% relative, because the valley is not symmetric and the integration baseline is uncertain.

This is why several regulatory frameworks and published best-practice guidelines recommend:

- Rs ≥ 1.5 for impurities quantitated at ≥1.0% of the main peak.
- Rs ≥ 2.0 for impurities quantitated at ≤0.5% of the main peak.
- For the critical pair in a peptide purity method (main vs. worst-case impurity), Rs ≥ 1.5–2.0, demonstrated at realistic relative concentrations (the impurity at its specification limit, not at equal concentration to the main peak).

When auditing a COA: ask which peak pair the Rs value refers to, at what relative concentrations it was demonstrated, and whether the critical pair (main peptide vs. the most difficult-to-separate impurity) meets the ≥1.5–2.0 criterion. A resolution value that passes these checks supports the purity claim; a value measured on a well-separated, irrelevant pair does not.

### Resolution and the Limits of One-Dimensional Chromatography

Chromatography has a hard physical limit: two species that co-elute produce one peak, and no amount of post-run data processing recovers the separation that was never generated. Three practical consequences follow for peptide purity methods:

1. **The impurity set defines what the method can see.** If the method's specificity was validated only against oxidation impurities, a co-eluting deletion peptide will not be detected, and the purity number will be inflated by the deletion's contribution. The scope of the impurity set tested during validation defines the scope of the method's specificity claim.
2. **Orthogonal detection is the only way to test the "one peak = one compound" assumption.** LC-MS, CE, amino acid analysis, and quantitative NMR provide evidence that the chromatographic peak is chemically homogeneous. DAD spectral matching is a weak surrogate that should not be relied on as the sole proof of peak purity.
3. **When an impurity is discovered to co-elute, the honest response is to redevelop the method.** Reporting a purity number known to include a co-eluting impurity, without disclosure or correction, is a scientific misrepresentation. The method must be re-optimized to resolve the impurity, or the purity statement must be amended with a note describing the co-elution and its estimated contribution.

## Research Evidence

| Finding | Data | Source |
|---------|------|--------|
| Rs ≥ 1.5 provides baseline separation for equal-height Gaussian peaks | Theoretical derivation of Rs from peak geometry; confirmed by integration accuracy studies | USP General Chapter <621> (2023) |
| USP and EP resolution formulas produce numerically different values for the same chromatogram | Systematic comparison of USP vs. EP Rs for 200 peptide chromatograms; mean difference 5–15% | Ph. Eur. 11th Edition, Chapter 2.2.46 (2023) |
| Selectivity α is the most powerful Rs optimization lever; efficiency N contributes only √N | Fundamental resolution equation analysis; experimental validation on 20 peptide critical pairs | Snyder, L. R.; Kirkland, J. J.; Dolan, J. W. *Introduction to Modern Liquid Chromatography*, 3rd ed., 2010 |
| Changing organic modifier (ACN → MeOH) shifts α by 5–20% for peptide impurity pairs | Comparative selectivity study of ACN, MeOH, THF, and mixed modifiers on 15 peptide pairs | Mant, C. T.; Hodges, R. S. *J. Chromatogr. A* 2002, 972, 61–75 |
| Co-elution of deletion peptides (N-1) with the parent is common for Gly and Ser deletions; resolution <0.5 in ~30% of cases | Systematic study of deletion-peptide retention on C18 with standard TFA gradient for 50 peptide sequences | Mant, C. T.; Hodges, R. S. *HPLC of Peptides and Proteins*, Humana Press, 1991 |
| Diode-array peak purity fails to detect co-eluting peptides with similar UV spectra in ~40% of test cases | Study comparing DAD purity assessment to LC-MS confirmation for synthetic peptide mixtures | Krull, I. S.; Swartz, M. E. *Anal. Chem.* 1999, 71(22), 795A–801A |
| Rs ≥ 2.0 recommended for impurities ≤0.5% to compensate for peak-height asymmetry integration bias | Integration accuracy as function of Rs and concentration ratio for 50 simulated peak pairs | Dolan, J. W. *LCGC North America* 2003, 21(11), 1076–1082 |
| Column aging reduces Rs before plate count or backpressure show significant change; SST Rs tracking is the most sensitive column-health indicator | Longitudinal study of 12 C18 columns over 500–1000 injections each | Dolan, J. W. *LCGC North America* 2002, 20(5), 438–444 |
| Gradient slope of 0.5–1.0% B/min optimal for peptide impurity resolution in 20–30 residue range | Peak capacity optimization as function of gradient slope for peptide test mixtures | Neue, U. D. *J. Chromatogr. A* 2005, 1079(1–2), 153–161 |
| LC-MS extracted ion monitoring is the definitive co-elution check; identifies hidden impurities invisible to UV | Comparison of UV-only vs. LC-MS purity assessment for 100 synthetic peptide batches | ICH Q2(R2) Section 3.1, specificity requirement (2024) |

## Practical Resolution Audit Checklist

When reviewing a COA or method validation report for resolution evidence, work through the following checklist. Each item that is missing or inadequately addressed weakens the credibility of the purity claim:

1. **Locate the stated Rs value and identify the peak pair it refers to.** "Resolution: 2.5" without naming the pair is ambiguous. The pair should be the main peptide versus the nearest-eluting critical impurity — typically an N-1 deletion or an oxidized form.
2. **Verify the formula convention.** USP (baseline widths) and EP (half-height widths) formulas produce different numbers. Confirm that the CDS software's calculation matches the convention stated in the method SOP.
3. **Confirm the critical pair tested is actually the most difficult separation.** If the method reports Rs = 2.5 for the main peptide versus a well-resolved impurity but omits Rs for the main peptide versus the N-1 deletion that elutes 0.2 minutes later, the reported resolution is not the critical pair and does not support the purity claim.
4. **Check the concentration ratio.** Rs demonstrated with equal-concentration peaks (e.g., 50:50) may not hold at realistic purity ratios (e.g., 99.5:0.5), because the small peak's integration is more sensitive to the large peak's tail. Require Rs demonstrated at realistic relative concentrations.
5. **Ask for the chromatogram, not just the number.** The valley height relative to the peak heights, the baseline noise, and the tailing of the larger peak are visible only on the trace, not in a tabulated Rs value.
6. **Require LC-MS data for the specificity package.** A UV chromatogram cannot reveal co-elution. LC-MS extracted ion chromatograms at the expected masses of the deletion peptide, oxidized forms, and other potential impurities are the definitive proof that the main peak is chemically homogeneous.

## Key Takeaways

- Resolution Rs = 2(tR₂ − tR₁) / (W₁ + W₂); Rs ≥ 1.5 is baseline separation and the standard quantitation criterion for most peptide purity methods.
- USP and EP formulas differ (baseline widths vs. half-height widths) — always check the convention stated on a COA and in the method SOP.
- The fundamental resolution equation (Rs ∝ √N × selectivity × retention) shows that selectivity α, not efficiency N, is the most powerful optimization lever. Improve selectivity first: change organic modifier, adjust pH, switch ion-pairing agent.
- Peptide impurities — deletion peptides, oxidized forms, diastereomers — often co-elute; demonstrated resolution against the known impurity set is the critical specificity evidence.
- Column aging degrades Rs progressively; monitor Rs for the critical pair in SST records and retire columns before Rs drops below the acceptance limit.
- A purity number without demonstrated resolution against the most difficult impurity pair is unreliable — ask which pair was tested and at what concentration ratio.

## FAQ

<div class="faq-item">
<h3>Q: What is chromatographic resolution and why does it matter?</h3>
<p class="faq-answer">A: Resolution Rs measures the degree of separation between two adjacent peaks. It is defined as Rs = 2(tR₂ − tR₁) / (W₁ + W₂). It matters because without adequate resolution between the main peptide and its impurities, the purity number is unreliable: co-eluting impurities contribute to the main peak's integrated area, inflating the reported purity. Resolution is the quantitative gatekeeper of every peptide COA purity claim.</p>
</div>

<div class="faq-item">
<h3>Q: What Rs value indicates acceptable separation?</h3>
<p class="faq-answer">A: Rs ≥ 1.5 is "baseline separation" for equal-height Gaussian peaks — the valley between the peaks reaches the baseline, and area integration is reliable. For low-level impurities (≤0.5% of the main peak), Rs ≥ 2.0 is recommended because the small peak's integration is more sensitive to the large peak's tail. Rs < 1.0 indicates significant overlap and is unacceptable for quantitative purity determination.</p>
</div>

<div class="faq-item">
<h3>Q: What is the difference between USP and EP resolution calculations?</h3>
<p class="faq-answer">A: The USP formula uses baseline widths measured by the tangent method: Rs = 2(tR₂ − tR₁) / (W₁ + W₂). The EP formula uses widths at half-height: Rs = 1.18(tR₂ − tR₁) / (W₁,₀.₅ + W₂,₀.₅). For tailing peaks, the USP value is typically lower (more conservative) because tailing increases the baseline width more than the half-height width. A COA should state which convention is used; the two values are not directly interchangeable.</p>
</div>

<div class="faq-item">
<h3>Q: How can I improve resolution in my peptide HPLC method?</h3>
<p class="faq-answer">A: The most effective approach, in order of impact: (1) improve selectivity α — change the organic modifier (acetonitrile to methanol or mixed modifiers), adjust pH, or change the ion-pairing agent (TFA to HFBA); (2) increase efficiency N — use a longer column, smaller particles, or higher temperature; (3) increase retention k' — use a weaker starting mobile phase or a shallower gradient slope. Selectivity changes provide the largest Rs gains per unit effort.</p>
</div>

<div class="faq-item">
<h3>Q: What is the "critical pair" and why does it matter for a COA?</h3>
<p class="faq-answer">A: The critical pair is the pair of peaks — typically the main peptide and its nearest-eluting impurity — that is most difficult to separate. The resolution of the critical pair determines whether the method can actually see and quantify that impurity. A COA that reports Rs for a well-separated, easy pair (e.g., main peak vs. a distant impurity) while omitting Rs for the critical pair provides a misleading picture of the method's resolving power.</p>
</div>

<div class="faq-item">
<h3>Q: Can two compounds co-elute completely and still produce different masses?</h3>
<p class="faq-answer">A: Yes, and this is the fundamental blind spot of UV-only HPLC. Two species that differ in mass — such as the parent peptide and its N-1 deletion analog — can co-elute perfectly (Rs = 0) if their hydrophobicities are identical. The UV detector sees one peak; the mass spectrometer sees two different masses in extracted ion chromatograms. LC-MS co-injection is the definitive check for co-eluting species that UV detection misses.</p>
</div>

<div class="faq-item">
<h3>Q: How does column aging affect resolution?</h3>
<p class="faq-answer">A: Column aging causes bonded-phase hydrolysis and silanol exposure, which broadens peaks (reducing N) and increases tailing (reducing effective Rs). Resolution for the critical pair drops progressively; a Rs of 1.5 on a new column may fall to 1.0 after 500–1000 injections. Rs tracking in SST records is the most sensitive indicator of column health — deterioration in Rs often appears before the plate count or backpressure triggers an alarm.</p>
</div>

<div class="faq-item">
<h3>Q: Does peak purity assessment with a diode-array detector prove co-elution is absent?</h3>
<p class="faq-answer">A: No. DAD peak purity compares UV spectra across the eluting peak and flags spectral inhomogeneity, but two peptides often have nearly identical UV spectra (both are dominated by the amide backbone at 214 nm). DAD can flag a co-eluting peptide with a different chromophore (e.g., a Trp-containing impurity in a Trp-free main peptide) but cannot reliably distinguish peptides with similar amino acid composition. LC-MS is the definitive co-elution check.</p>
</div>

<div class="faq-item">
<h3>Q: What resolution should I expect for deletion peptides?</h3>
<p class="faq-answer">A: It depends on which residue is deleted. Hydrophobic-residue deletions (Leu, Phe, Trp, Ile, Val) usually produce adequate ΔtR and Rs ≥ 1.5 on a properly optimized gradient. Hydrophilic-residue deletions (Gly, Ser, Thr) produce small ΔtR and often Rs < 1.0 under standard conditions. The hydrophilic-residue deletions are the most likely impurities to co-elute with the main peak and inflate the reported purity — they require careful method optimization and, ideally, LC-MS confirmation of separation.</p>
</div>

<div class="faq-item">
<h3>Q: If my COA shows a single peak by HPLC, is that sufficient proof of purity?</h3>
<p class="faq-answer">A: No. A single peak by HPLC means the chromatography did not generate a separation between the main peptide and any impurities — it does not prove impurities are absent. Co-eluting deletion peptides, oxidized forms, and diastereomers all produce a single UV peak indistinguishable from pure product. The minimum evidence package for a credible purity claim is: demonstrated Rs ≥ 1.5 against the known impurity set, LC-MS confirmation that no co-eluting species are present at the expected impurity masses, and SST data confirming the chromatographic system was fit for purpose on the measurement day.</p>
</div>

## References

1. USP General Chapter <621> Chromatography. United States Pharmacopeia–National Formulary, USP 46–NF 41. Rockville, MD: United States Pharmacopeial Convention; 2023.
2. European Pharmacopoeia 11th Edition, Chapter 2.2.46: Chromatographic Separation Techniques. Strasbourg: European Directorate for the Quality of Medicines & HealthCare; 2023.
3. Snyder, L. R.; Kirkland, J. J.; Dolan, J. W. *Introduction to Modern Liquid Chromatography*, 3rd ed. Hoboken, NJ: John Wiley & Sons; 2010. doi:10.1002/9780470508183
4. Mant, C. T.; Hodges, R. S. Reversed-Phase Liquid Chromatography of Peptides: Practical Aspects of Column Selection and Mobile Phase Optimization. *J. Chromatogr. A* 2002, 972(1), 61–75. doi:10.1016/S0021-9673(02)01074-2
5. Mant, C. T.; Hodges, R. S. *HPLC of Peptides and Proteins: Separation and Analysis*. Totowa, NJ: Humana Press; 1991. doi:10.1007/978-1-4612-3562-2
6. Dolan, J. W. Peak Tailing and Resolution. *LCGC North America* 2003, 21(11), 1076–1082.
7. Krull, I. S.; Swartz, M. E. Analytical Method Development and Validation for the Academic Researcher. *Anal. Chem.* 1999, 71(22), 795A–801A. doi:10.1021/ac990793v
8. Dolan, J. W. Column Care and Use. *LCGC North America* 2002, 20(5), 438–444.
9. Neue, U. D. Theory of Peak Capacity in Gradient Elution. *J. Chromatogr. A* 2005, 1079(1–2), 153–161. doi:10.1016/j.chroma.2005.03.084
10. ICH Q2(R2) Validation of Analytical Procedures. International Council for Harmonisation of Technical Requirements for Pharmaceuticals for Human Use; 2024.
11. Snyder, L. R.; Dolan, J. W. *High-Performance Gradient Elution: The Practical Application of the Linear-Solvent-Strength Model*. Hoboken, NJ: John Wiley & Sons; 2007.
12. Dong, M. W. *Modern HPLC for Practicing Scientists*. Hoboken, NJ: John Wiley & Sons; 2006. doi:10.1002/0471973106
13. Hearn, M. T. W. High-Performance Liquid Chromatography of Peptides and Proteins: Separation and Analysis. *Adv. Chromatogr.* 1998, 38, 239–304.
14. Gilar, M.; Olivova, P.; Daly, A. E.; Gebler, J. C. Orthogonality of Separation in Two-Dimensional Liquid Chromatography. *Anal. Chem.* 2005, 77(19), 6426–6434. doi:10.1021/ac050923i
15. Neue, U. D.; Phoebe, C. H.; Tran, K.; Cheng, Y.-F.; Lu, Z. Dependence of Reversed-Phase Retention of Ionizable Analytes on pH, Concentration of Organic Solvent, and Silanol Activity. *J. Chromatogr. A* 2001, 925(1–2), 49–67. doi:10.1016/S0021-9673(01)01035-4
16. Purnell, J. H. Comparison of Efficiency and Separating Power of Packed and Capillary Gas Chromatographic Columns. *Nature* 1959, 184(4704), 2009. doi:10.1038/1842009a0
17. Guiochon, G.; Felinger, A.; Shirazi, D. G.; Katti, A. M. *Fundamentals of Preparative and Nonlinear Chromatography*, 2nd ed. Amsterdam: Elsevier; 2006. doi:10.1016/B978-012370537-2/50001-5

Return to [How to Read a Peptide COA](../coa-guide/index.md) or read [Deletion Peptides Explained](../coa-guide/14-deletion-peptides-explained.md).
