---
title: "Peak Area vs Peak Height in HPLC Purity Calculations"
description: "Why chromatographic peak area integration is mathematically required for peptide purity calculations instead of peak height: theory, band broadening, and integration practice."
slug: peak-area-vs-peak-height
category: Analytical Chemistry
tags: [Peak Area, Peak Height, HPLC Purity, Integration, Band Broadening]
author: RPL Peptides Research Team
published: 2026-08-01
---

# Peak Area vs Peak Height in HPLC Purity Calculations

## Executive Summary

The choice between peak area and peak height for HPLC purity calculations is not a matter of convenience or software preference—it is a requirement rooted in the physics of chromatographic band broadening and the chemistry of the Beer-Lambert law. Peak area is proportional to the mass of analyte injected, independent of how the chromatographic band broadens as it travels through the column. Peak height, by contrast, depends on the width of the band at its apex, which changes systematically with column age, flow rate, temperature, and sample loading. Using height instead of area for peptide purity calculations introduces systematic bias that can shift the reported purity by 1–3 percentage points—enough to move a batch across a specification threshold.

For laboratory managers and researchers evaluating peptide Certificates of Analysis, understanding the area-versus-height distinction is one of the most operationally consequential pieces of chromatographic knowledge. A COA that reports "purity 98.5%" derived from peak heights is not reporting purity on the same measurement basis as one that reports "purity 98.5%" from peak areas, and the two numbers are not comparable. The defensible standard in pharmaceutical analysis, codified in USP <621> and implied in ICH Q2(R2) through its accuracy and linearity requirements, is area-based quantitation.

This article explains the physical chemistry basis for area-based purity, quantifies the sources and magnitude of height-based bias, provides worked examples of the discrepancy, discusses integration parameter selection in practice, and examines the narrow circumstances in which peak height remains a useful metric. Readers will emerge with the ability to audit any peptide COA for measurement-basis integrity and to recognize when height-based numbers have been substituted for area-based ones.

## Background

Chromatographic quantitation has used peak area since the earliest days of electronic integration. The underlying principle was established by the pioneers of modern liquid chromatography—Snyder, Kirkland, and Dolan—and is now codified in pharmacopoeial chapters and regulatory guidelines worldwide. The fundamental reasoning is deceptively simple but its implications are profound: as a solute band travels through a chromatographic column, it broadens due to diffusion and mass-transfer kinetics, reducing its concentration at any single point in time. The peak height at the detector records this reduced concentration, but the integrated area captures the total mass that passed through the detector cell, which is conserved.

In peptide analysis, the consequence is particularly acute because peptide separations in reversed-phase HPLC often involve gradient elution, where peak widths vary systematically across the chromatogram. Early-eluting impurities appear as narrow, tall peaks; late-eluting impurities appear as broad, short peaks. A height-based purity calculation would over-weight the early-eluting narrow peaks and under-weight the late-eluting broad peaks, producing a purity number that does not reflect the true mass distribution. Area-based normalization corrects for this differential band broadening automatically.

The regulatory framework reinforces this physics: ICH Q2(R2) requires linearity to be demonstrated using peak area versus concentration, not peak height, precisely because area alone maintains the proportional relationship across the validated range. USP <621> specifies system suitability acceptance criteria—injection repeatability as RSD of peak area—on the same basis. A method that reports purity from peak heights is operating outside both compendial expectations and the physical constraints of the measurement.

## Core Science

### The Mathematical Basis: Why Area Is Proportional to Mass

The proportionality between peak area and injected mass follows from the Beer-Lambert law of UV absorbance and the conservation of mass in a constant-flow system. The Beer-Lambert law states:

$$A = \varepsilon \cdot c \cdot l$$

Where $A$ is absorbance (dimensionless), $\varepsilon$ is the molar absorptivity (L·mol⁻¹·cm⁻¹), $c$ is the concentration in the detector cell (mol/L), and $l$ is the optical path length (cm). As the analyte band flows through the detector cell at a constant volumetric flow rate $F$ (mL/min), the instantaneous absorbance $A(t)$ varies with the local concentration $c(t)$.

The integrated area under the chromatographic peak is:

$$A_{\text{area}} = \int_{t_1}^{t_2} A(t) \, dt = \int_{t_1}^{t_2} \varepsilon \cdot c(t) \cdot l \, dt$$

Because the total mass $m$ of analyte is the integral of concentration over the eluted volume, and volume is flow rate times time ($V = F \cdot t$):

$$m = \int_{V_1}^{V_2} c(V) \, dV = F \int_{t_1}^{t_2} c(t) \, dt$$

Substituting:

$$m = \frac{F}{\varepsilon \cdot l} \cdot A_{\text{area}}$$

The proportionality constant $F/(\varepsilon \cdot l)$ is the same for all peaks measured under identical conditions—same flow rate, same wavelength (constant $\varepsilon$ for a given analyte), same path length—provided the detector response is linear. This is the mathematical proof that peak area, not peak height, is proportional to injected mass.

### Why Peak Height Fails as a Purity Metric

Peak height $H_{\text{max}}$ is the maximum absorbance recorded at the peak apex. It depends on the width of the chromatographic band at the detector—specifically, on the variance $\sigma^2$ of the band's Gaussian concentration profile. The total band variance is the sum of independent contributions:

$$\sigma^2_{\text{total}} = \sigma^2_{\text{injection}} + \sigma^2_{\text{column}} + \sigma^2_{\text{tubing}} + \sigma^2_{\text{detector}} + \sigma^2_{\text{data rate}}$$

Where $\sigma^2_{\text{column}}$ is the dominant term and is inversely proportional to the column's plate count $N$:

$$\sigma^2_{\text{column}} \propto \frac{L}{N}$$

For a Gaussian peak, the peak height at a given injected mass $m$ is:

$$H_{\text{max}} = \frac{m}{\sigma \sqrt{2\pi}} \times \text{(detector constant)}$$

As the column ages, $N$ decreases, $\sigma$ increases, and $H_{\text{max}}$ decreases—even though the same mass of analyte elutes. The practical consequences are summarized in the table below:

| Condition | Peak Area | Peak Height | Reason |
|-----------|:---------:|:-----------:|--------|
| Column aging (plate loss) | Constant | Decreases | Band broadens; area conserved |
| Flow rate increase | Constant | Increases | Narrower peaks; area conserved |
| Column overload (mass increase) | Proportional | Sub-proportional | Peak flattens; plateaus at detector saturation |
| Tailing (silanol interaction) | Constant | Decreases | Mass shifted to tail; apex depressed |
| Temperature increase (±5 °C) | Constant | Slightly increases | Faster diffusion narrows bands |
| Gradient slope change | Constant | Changes | Peak width changes; mass conserved |

The key message: area is robust to all these perturbations; height is not. An area-based purity calculation reports the true mass fraction of the main component regardless of band shape, column history, or day-to-day variations in operating conditions.

### Tailing and Its Differential Effect

Tailing peaks present the starkest case for area over height. In a tailing peak, the asymmetry arises from secondary interactions—most commonly between protonated basic residues (Lys, Arg, His) and residual ionized silanol groups on the silica surface—that retard a fraction of the analyte molecules. The peak shape is no longer Gaussian: the apex is shifted earlier and depressed, and the tail redistributes analyte mass to later times.

For a tailing peak with asymmetry factor $A_s = 2.0$, the peak height at a given injected mass is approximately 70% of what it would be for a perfectly symmetric peak of the same area. A height-based purity calculation therefore under-reports the main peptide's contribution by ~30% and over-reports the relative abundance of narrower, earlier-eluting impurities. The error scales non-linearly with $A_s$: at $A_s = 1.5$, the height depression is ~15%; at $A_s = 3.0$, it exceeds 40%.

For the quantitative treatment of tailing factor and its measurement, see [Tailing Factor Explained](12-tailing-factor-explained.md). The practical rule for COA review: if the printed chromatogram shows visible tailing on the main peak and the purity is reported without specifying whether area or height was used, the value is of unknown reliability. If height was used, the purity is systematically underestimated.

### Area Percent Normalization: Assumptions and Limitations

The standard purity calculation on peptide COAs is area percent normalization:

$$\text{Purity (\%)} = \frac{A_{\text{main}}}{\sum A_i} \times 100$$

Where $A_{\text{main}}$ is the integrated area of the main peptide peak and $\sum A_i$ is the sum of all integrated peak areas in the chromatogram (excluding the solvent front). This simple formula carries three assumptions that are rarely stated but must be understood:

1. **Equal response factors.** All components—target peptide and all impurities—have the same molar absorptivity at the detection wavelength. This assumption fails when impurities have different chromophores (e.g., aromatic-residue-rich impurities vs. aliphatic main peptide) or when the main peak saturates the detector while impurities are in the linear range.
2. **Complete detection.** Nothing elutes in the solvent front, nothing is retained beyond the gradient end, and nothing lacks UV absorbance at the detection wavelength (e.g., non-peptide contaminants, residual salts, trifluoroacetate counterions).
3. **All components are resolved.** Co-eluting species share a single peak and a single area; their combined contribution is assigned to the main peak, inflating the reported purity by the fraction of the co-eluting impurity.

The first assumption—equal response factors—is the dominant source of systematic bias in peptide purity measurements. For a rigorous approach that accounts for relative response factors (RRFs), see [How Laboratories Calculate HPLC Purity](16-how-laboratories-calculate-hplc-purity.md).

### Worked Example: Area vs Height Purity Discrepancy

Consider a chromatogram showing a main peptide peak and one impurity:

| Peak | Area (mAU·s) | Height (mAU) | Width at Half Height (min) |
|------|:------------:|:------------:|:--------------------------:|
| Main peptide | 9,500 | 380 | 0.42 |
| Impurity | 500 | 25 | 0.34 |

**Area-based purity:**

$$\text{Purity} = \frac{9500}{9500 + 500} \times 100 = 95.0\%$$

**Height-based purity:**

$$\text{Purity} = \frac{380}{380 + 25} \times 100 = 93.8\%$$

The 1.2% discrepancy arises because the impurity peak is relatively narrow (0.34 min at half height vs. 0.42 min for the main peak), making it taller relative to its area than the main peak is. The area-based value (95.0%) is the correct mass fraction; the height-based value (93.8%) systematically underestimates the purity. This 1.2% difference is not trivial—it can determine whether a batch passes or fails a 95% specification.

The discrepancy can be much larger when multiple impurities of differing widths are present. A late-eluting, broad impurity with area 500 mAU·s may have a peak height of only 8 mAU, producing a height-based impurity contribution that is severely under-weighted relative to the main peak. In such cases area-versus-height differences of 3–5% are observed.

### Detector Linearity and the Dynamic Range

Area-based quantitation is only valid within the detector's linear dynamic range—the concentration interval over which absorbance is proportional to concentration per the Beer-Lambert law. At high concentrations, deviations from linearity occur due to:

- **Detector saturation**: the photomultiplier or photodiode reaches its maximum output.
- **Stray light**: a small fraction of light bypasses the sample, producing a non-zero baseline that compresses absorbance at high values.
- **Refractive index gradients**: at high concentrations, the sample solvent and the mobile phase have different refractive indices, producing apparent absorbance changes unrelated to the analyte.

The practical consequence: if the main peptide peak absorbance exceeds approximately 1.5 AU (absorbance units), the detector may be operating outside its linear range. The main peak area understates the true amount of peptide, and the normalized purity is inflated—a classic "purity 99.8% by area" from a saturated detector is an artifact.

Practical rules: (1) verify the detector's linear range during method validation by plotting absorbance vs. concentration for standards covering the expected range; (2) keep the main peak below approximately 1.5 AU; (3) if the main peak is off-scale (flat-topped), the chromatogram is not quantifiable regardless of what the integration software reports. See [HPLC Method Validation](08-hplc-method-validation.md) for the experimental protocol.

### Integration Parameters and Area Accuracy

Peak area is only as accurate as the software's boundary detection. The same physical peak integrated with different parameters yields different areas. The four most influential parameters are:

| Parameter | Effect on Purity |
|-----------|------------------|
| Slope sensitivity / threshold | Too low: noise integrated as fake impurity peaks → purity deflated. Too high: real impurities merged into baseline or main peak → purity inflated |
| Baseline mode (valley-to-valley vs. drop vs. tangent skim) | Changes how area is split between the main peak and a partially resolved impurity; different modes give different purity values |
| Peak width / expected width | Incorrect estimate distorts the smoothing algorithm and fitted baseline under each peak |
| Minimum area / height threshold | Removes small peaks from the integration entirely; a 0.1% threshold means impurities below 0.1% are invisible by definition |

A well-integrated chromatogram displays integration marks at the true peak boundaries—at the baseline, not inside the peak tail. A common audit finding is integration marks placed inside the tail of the main peak, which truncates the main-peak area, assigns the remaining tail to the baseline (or to a phantom "impurity" peak), and changes the reported purity. The integration marks should be consistent with the visual boundaries of each peak; if they are not, the integration is suspect.

A rigorous report states the integration parameters or, at minimum, the minimum area threshold expressed as a percentage of the main peak. If a COA claims "no impurities detected," the immediate question is: "at what LOQ?" Without that value, the statement "no impurities" is equivalent to "no impurities above an unknown threshold."

### Selecting Integration Parameters in Practice

Integration settings are operational choices, not inherent properties of the data, and they change the reported purity. The established workflow for setting defensible parameters during method validation is:

1. Run the reference standard at the target concentration and visually identify the expected impurity peaks.
2. Set the slope sensitivity to detect the smallest impurity of interest (typically 0.05–0.1% of the main peak area).
3. Run a blank injection to confirm the slope sensitivity does not integrate noise.
4. Set the peak width to match the narrowest peak in the chromatogram.
5. Choose a baseline mode appropriate to the peak spacing: valley-to-valley for baseline-resolved peaks, tangent skim for small shoulders on the main peak tail.
6. Lock all parameters in the processing method and use them for every subsequent analysis.

Parameters should not be "optimized" per batch—a practice that cherry-picks integration settings to achieve a desired purity number. The parameters validated during method development constitute the method, and changing them constitutes a method change that must be documented and re-validated.

### When Peak Height Is Still Useful

Peak height retains legitimate, narrow uses despite its unsuitability for purity quantitation:

1. **Signal-to-noise (S/N) calculations.** S/N is defined by the ICH guidelines using peak heights, not areas. LOD and LOQ are height-based by definition.
2. **Early-eluting peaks on a steeply rising baseline.** When a peak rides on a gradient slope, height is less sensitive to baseline placement than area.
3. **Very narrow peaks with poorly defined baselines.** When peak width is comparable to the data-sampling interval, baseline-to-baseline integration is unreliable, and height may be more reproducible.
4. **Trace impurity screening.** When the question is presence/absence below the quantitation limit (detection only), height from extracted ion chromatograms (LC-MS) is an appropriate screening metric.
5. **Partially resolved peak pairs.** When resolution is poor ($R_s < 1.0$), the height of the main peak is less affected by the overlapping peak than the integrated area is.

In every one of these cases, height-based numbers must be explicitly labeled as such because they are not comparable to area-based purity values. A COA that uses height for screening but reports the purity from area—clearly distinguishing the two uses—is employing height appropriately. A COA that reports a single "purity" number derived from heights is using height inappropriately.

### Area Ratios and Normalized Purity: Subtle Choices, Big Effects

Area normalization appears straightforward—divide the main peak area by the sum of all peak areas—but two operational choices, often undocumented, change the result:

1. **Which peaks are included.** The solvent front must be excluded (see [HPLC Chromatogram Interpretation](02-hplc-chromatogram-interpretation.md)). Peaks below the minimum area threshold are dropped. The choice of that threshold—0.05%, 0.1%, 0.2%—directly changes the denominator and the number of reported impurities. A method with a 0.2% threshold reports fewer impurities and a numerically higher purity than the same method with a 0.05% threshold on the same sample, even though the chemistry is identical.

2. **How the baseline is drawn between adjacent peaks.** Valley-to-valley integration assigns the lowest point between two peaks to the baseline and splits the area at the valleys. Perpendicular drop draws a vertical line from the valley point to the true baseline. For two partially resolved peaks, valley-to-valley integration assigns less area to the main peak than perpendicular drop—the main peak "gives up" the area between the valley and the baseline—and the reported purity is correspondingly lower.

The difference between two laboratories reporting 98.0% and 98.6% for the same batch is often entirely explained by integration settings rather than chemistry. When comparing COAs across laboratories, the diagnostic question is: "What are the integration parameters, and what is the minimum area threshold?" A supplier that discloses both demonstrates analytical maturity; one that cannot is operating without documented integration control.

## Research Evidence

| Finding | Data | Source |
|---------|------|--------|
| Peak area is linearly proportional to injected mass (r ≥ 0.999) across 3 orders of magnitude for peptide analytes | Validation study of 15 synthetic peptides at 1 µg–1 mg loading; area R² = 0.9996, height R² = 0.987 | Snyder et al., *J. Chromatogr. A* 1994, 662, 71–82 |
| Column aging reduces peak height by 15–30% while area remains within 2% | Accelerated aging study of C18 columns; 500 gradient cycles monitored | Neue et al., *J. Sep. Sci.* 2003, 26, 275–283 |
| Height-based purity differs from area-based purity by 1–5% absolute for tailing peptides | Quantitation of 50 peptide chromatograms; mean difference 2.3% | Dolan, *LCGC North America* 2001, 19, 522–528 |
| Detector linearity is typically 0–2.0 AU; above 1.5 AU area response compresses | UV detector linearity study of 10 commercial HPLC detectors | Johns & Macka, *J. Chromatogr. A* 2008, 1186, 75–84 |
| Integration baseline mode changes purity by 0.5–2% for partially resolved impurity pairs | Simulation study of 100 peak pairs at varying resolution (Rs 0.8–1.5) | Dyson, *Chromatographic Integration Methods*, RSC 1998 |
| ICH Q2(R2) specifies S/N ≥ 10 for LOQ using peak height, not area | ICH Q2(R2) Section 6.2, Limit of Quantitation | ICH Q2(R2), 2023 |
| USP <621> requires injection repeatability as RSD of peak area | USP <621> System Suitability section | USP–NF, General Chapter <621> |
| Relative response factors for peptide impurities range from 0.6 to 1.8 relative to the main peptide at 214 nm | Measured RRF for 20 synthetic peptide impurity standards | Mant et al., *J. Chromatogr. A* 2003, 1008, 69–82 |

## FAQ

<div class="faq-item">
<h3>Q: Why can't I use peak height for peptide purity calculations?</h3>
<p class="faq-answer">A: Peak height depends on how broad the chromatographic band is, which changes with column age, temperature, flow rate, and sample loading. Peak area is conserved regardless of band width because it is proportional to total injected mass through the Beer-Lambert law. Using peak height for purity introduces systematic bias—typically 1–3% for routine peptide analyses—that shifts with column condition and operating parameters. The pharmacopoeial standard (USP <621>, ICH Q2(R2)) requires area-based quantitation.</p>
</div>

<div class="faq-item">
<h3>Q: How much can height-based purity differ from area-based purity?</h3>
<p class="faq-answer">A: For a typical peptide chromatogram with 1–3 impurity peaks of varying widths, height-based purity is typically 1–3% lower than area-based purity. The discrepancy is larger when the impurity peaks are narrow relative to the main peak (over-weighting the impurities) or when the main peak tails (depressing the main peak's height). In extreme cases—a broad, late-eluting impurity with a $k'$ of 15–20 versus a sharp main peak—differences of 5% or more have been documented.</p>
</div>

<div class="faq-item">
<h3>Q: Does column aging affect area-based purity?</h3>
<p class="faq-answer">A: Column aging does not directly affect area-based purity because area is conserved as bands broaden. However, aging can affect purity indirectly: as plate count decreases, resolution between the main peak and a nearby impurity degrades, potentially merging two peaks into one. In that case area-based purity increases not because the peptide is purer but because the method can no longer resolve the impurity. This is a specificity failure, not an area measurement failure, and it is caught by system suitability testing—see [System Suitability Testing](09-system-suitability-testing.md).</p>
</div>

<div class="faq-item">
<h3>Q: What is area percent normalization and what assumptions does it make?</h3>
<p class="faq-answer">A: Area percent normalization calculates purity as (main peak area) ÷ (sum of all peak areas) × 100. It assumes: (1) all components have equal UV absorptivity at the detection wavelength (equal response factors), (2) all components are detected (nothing absorbs outside the monitored wavelength, nothing elutes in the void volume or after the gradient), and (3) all components are chromatographically resolved. These assumptions are reasonable for homologous peptide impurities (deletions, truncations) but break down for chemically dissimilar species. The method should be validated for specificity per [ICH Q2(R2) Explained](07-ich-q2r2-explained.md).</p>
</div>

<div class="faq-item">
<h3>Q: How do integration parameters affect the area measurement?</h3>
<p class="faq-answer">A: Integration parameters are not passive—they actively determine which peaks are detected and how their areas are calculated. Slope sensitivity controls whether small peaks are detected or merged into the baseline. Baseline mode (valley-to-valley, perpendicular drop, tangent skim) controls how overlapping peaks share area. Minimum area threshold excludes peaks below a chosen size. Changing any of these parameters changes the reported purity. Validated integration parameters must be locked in the processing method and used for every analysis; changing them per batch is not acceptable practice.</p>
</div>

<div class="faq-item">
<h3>Q: When is peak height actually appropriate to use?</h3>
<p class="faq-answer">A: Peak height is appropriate for signal-to-noise calculations (S/N, LOD, LOQ), for early-eluting peaks on a steeply rising gradient baseline, for very narrow peaks where baseline definition is unreliable, for trace impurity screening below the quantitation limit, and for partially resolved peak pairs where height is less affected by overlap than area. In all these cases, height-based numbers must be explicitly labeled as such because they are not comparable to area-based purity values. Height is never appropriate for reporting quantitative purity on a COA.</p>
</div>

<div class="faq-item">
<h3>Q: What happens if the main peptide peak saturates the detector?</h3>
<p class="faq-answer">A: When the detector absorbance exceeds its linear range (typically >1.5–2.0 AU), the area response compresses—the recorded area is smaller than the true value. Because the main peak saturates while small impurity peaks remain in the linear range, normalized purity is inflated. An off-scale (flat-topped) main peak means the chromatogram is not quantifiable, regardless of what the integration software reports. The solution is to dilute the sample and re-run the analysis, or to use a shorter-path-length detector cell.</p>
</div>

<div class="faq-item">
<h3>Q: Why do two labs get different purity values for the same peptide batch?</h3>
<p class="faq-answer">A: Beyond differences in column selectivity and gradient conditions, integration parameter settings are the most common source of inter-laboratory discrepancy. Different slope sensitivities detect different sets of impurity peaks. Different baseline modes split the main peak and an adjacent impurity differently. Different minimum area thresholds include or exclude different small peaks. The cumulative effect of these parameter differences is typically 0.5–2% absolute purity. The diagnostic step is to compare integration parameters, not just purity numbers—see our article on [Analytical Method Transfer](10-analytical-method-transfer.md).</p>
</div>

<div class="faq-item">
<h3>Q: Can I assess purity using peak height from an LC-MS extracted ion chromatogram?</h3>
<p class="faq-answer">A: No. LC-MS XIC peak heights are proportional to ion intensity, which depends on the compound's ionization efficiency in ESI—a property that varies widely between different peptides. Two co-eluting species with different ionization efficiencies will have different ion-intensity ratios than their true concentration ratios. LC-MS provides semi-quantitative information at best for relative abundance. HPLC-UV peak area is the quantitative method because UV absorbance at 214 nm depends on the number of peptide bonds, which correlates more closely with molar amount than ionization efficiency does with concentration.</p>
</div>

<div class="faq-item">
<h3>Q: How can I verify that the reported purity is based on area and not height?</h3>
<p class="faq-answer">A: The COA chromatogram should explicitly state the quantity used for purity calculation—ideally "area percent" or "area normalization." If the chromatogram shows integration start and end marks (tick marks) on each peak, that is strong evidence that area integration was used, because height-based methods do not require boundary marks. Additionally, the method description should reference ICH Q2(R2) validation, which specifies linearity of area vs. concentration. If the COA provides only a chromatogram figure with no integration parameters and no statement of area vs. height, the basis of the purity calculation is undocumented and should be queried.</p>
</div>

## References

1. Snyder, L. R.; Kirkland, J. J.; Dolan, J. W. Introduction to Modern Liquid Chromatography, 3rd ed. Wiley, 2010. ISBN: 978-0470167540.
2. USP General Chapter <621> Chromatography. United States Pharmacopeia–National Formulary. Available at: [https://www.usp.org/harmonization-standards/pdg/general-chapter-chromatography](https://www.usp.org/harmonization-standards/pdg/general-chapter-chromatography)
3. ICH Q2(R2) Validation of Analytical Procedures. International Council for Harmonisation, 2023. Available at: [https://www.ich.org/page/quality-guidelines](https://www.ich.org/page/quality-guidelines)
4. Dolan, J. W. Peak Area vs. Peak Height. *LCGC North America* 2001, 19, 522–528.
5. Dyson, N. Chromatographic Integration Methods, 2nd ed. Royal Society of Chemistry, 1998. ISBN: 978-0854045105.
6. Neue, U. D.; Alden, B. A.; Walter, T. H. Column Aging and Its Effect on Chromatographic Performance. *J. Sep. Sci.* 2003, 26, 275–283.
7. Mant, C. T.; Hodges, R. S. Design of Peptide Standards for Reversed-Phase HPLC Method Validation. *J. Chromatogr. A* 2003, 1008, 69–82.
8. Johns, C.; Macka, M.; Haddad, P. R. Measurement of Detector Linearity in HPLC. *J. Chromatogr. A* 2008, 1186, 75–84.
9. ICH Q2(R1) Validation of Analytical Procedures: Text and Methodology. ICH, 2005. Available at: [https://www.ich.org/page/quality-guidelines](https://www.ich.org/page/quality-guidelines)
10. Shabir, G. A. Validation of High-Performance Liquid Chromatography Methods for Pharmaceutical Analysis: Understanding the Differences and Similarities Between Validation Requirements of the US FDA, the USP, and the ICH. *J. Chromatogr. A* 2003, 987, 57–66. DOI: [10.1016/S0021-9673(02)01536-4](https://doi.org/10.1016/S0021-9673(02)01536-4)
11. FDA Guidance for Industry: Analytical Procedures and Methods Validation for Drugs and Biologics. U.S. FDA, 2015. Available at: [https://www.fda.gov/regulatory-information/search-fda-guidance-documents/analytical-procedures-and-methods-validation-drugs-and-biologics](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/analytical-procedures-and-methods-validation-drugs-and-biologics)
12. Felinger, A. Data Analysis and Signal Processing in Chromatography. Elsevier, 1998. ISBN: 978-0444820662.
13. Swartz, M. E.; Krull, I. S. Analytical Method Development and Validation. Marcel Dekker, 1997. ISBN: 978-0824701154.
14. Ermer, J.; Miller, J. H. McB. Method Validation in Pharmaceutical Analysis: A Guide to Best Practice. Wiley-VCH, 2005. ISBN: 978-3527312559.
15. Dong, M. W. Modern HPLC for Practicing Scientists. Wiley, 2006. ISBN: 978-0471727897.

Return to [How to Read a Peptide COA](index.md) or read [Retention Time Explained](04-retention-time-explained.md).
