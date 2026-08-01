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

Chromatographic purity calculations use integrated peak area rather than peak height because peak height varies with column degradation, band broadening, and operating conditions — while peak area remains proportional to the mass of analyte injected, independent of peak shape.

## The Mathematical Basis: Why Area Is Proportional to Mass

In UV detection, the Beer-Lambert law states that absorbance is proportional to concentration:

$$A = \varepsilon \cdot c \cdot l$$

Where $A$ is absorbance, $\varepsilon$ is molar absorptivity, $c$ is concentration, and $l$ is path length. As the analyte band travels through the detector cell, the detector records absorbance over time. The integrated area is:

$$A_{\text{area}} = \int_{t_1}^{t_2} I(t) \, dt$$

Because the amount of analyte equals the concentration integrated over the eluted volume, and flow rate is constant, the peak area is directly proportional to the injected mass:

$$m = \frac{F}{\varepsilon \cdot l} \cdot \int_{t_1}^{t_2} I(t) \, dt$$

Where $F$ is the volumetric flow rate. The proportionality constant is the same for all peaks measured under identical conditions — provided the analyte obeys Beer-Lambert linearity in the detector range.

## Why Peak Height Fails as a Purity Metric

Peak height is the maximum detector response of the peak. It depends on how concentrated the band is at its apex, which is governed by band broadening:

$$\sigma^2_{\text{total}} = \sigma^2_{\text{injection}} + \sigma^2_{\text{column}} + \sigma^2_{\text{tubing}} + \sigma^2_{\text{detector}}$$

As the column ages, plate count $N$ decreases, peaks broaden, and the height of a fixed mass of analyte decreases — even though the area stays constant. Consequences:

| Condition | Peak Area | Peak Height |
|-----------|:---------:|:-----------:|
| Column aging (efficiency loss) | Constant | Decreases |
| Flow rate increase | Constant (area conserved) | Increases (narrower peaks) |
| Overload (mass increase) | Proportional | Sub-proportional (plateau) |
| Tailing (silanol interaction) | Constant | Decreases |
| Temperature increase | Constant | Slightly increases |

Area-based purity is therefore robust: it reports the true mass fraction regardless of band shape.

## Tailing and Its Differential Effect

For a tailing peak, the apex is depressed and the tail redistributes the mass. Peak height underestimates the analyte mass, while area integration captures the full distribution. See [Tailing Factor Explained](12-tailing-factor-explained.md) for the quantitative treatment. The practical rule: if a COA's chromatogram shows visible tailing, height-based numbers are unreliable, and area-based purity is the defensible metric.

## Integration Parameters and Area Accuracy

Area integration is only as good as the software's peak boundary detection. The critical parameters:

1. **Peak start/end thresholds (slope sensitivity)**: define where integration begins and ends on the baseline. Too aggressive a threshold truncates real peak area.
2. **Baseline mode**: valley-to-valley draws the baseline between adjacent peak valleys; tangent skim draws a tangent line under a shoulder peak. Different modes give different areas for the same chromatogram.
3. **Peak width estimate**: used for smoothing; an incorrect value distorts the fitted baseline under the peak.

Always verify that the integration marks on the printed chromatogram sit on the baseline, not inside the peak. A common audit finding is integration marks placed inside a tail, inflating the main peak area and deflating impurity areas.

## Area Percent Normalization

The standard purity calculation on peptide COAs is area normalization:

$$\text{Purity (\%)} = \frac{A_{\text{main}}}{\sum A_i} \times 100$$

Where $A_{\text{main}}$ is the area of the main peptide peak and $\sum A_i$ is the sum of all integrated peak areas in the chromatogram. This method assumes:

- All components have equal (or known) response factors.
- All components are detected at the chosen wavelength.
- Nothing elutes in the solvent front or is retained beyond the run.

These assumptions fail for impurities with very different chromophores or for non-UV-absorbing species. For a more rigorous approach, see [How Laboratories Calculate HPLC Purity](16-how-laboratories-calculate-hplc-purity.md) on relative response factor (RRF) correction.

## Worked Example: Area vs Height Purity

A chromatogram shows the main peptide peak and one impurity:

| Peak | Area (mAU·s) | Height (mAU) |
|------|:------------:|:------------:|
| Main peptide | 9,500 | 380 |
| Impurity | 500 | 25 |

Area-based purity: $9500 / (9500 + 500) = 95.0\%$

Height-based purity: $380 / (380 + 25) = 93.8\%$

The 1.2% discrepancy arises because the impurity peak is broader relative to its height (typical of a later-eluting, more retained component). The area-based value (95.0%) is the correct mass fraction.

## When Peak Height Is Still Useful

Peak height remains useful for:

- **Signal-to-noise calculations** (S/N uses heights; see [HPLC Chromatogram Interpretation](02-hplc-chromatogram-interpretation.md)).
- **Detection limit determinations** (LOD/LOQ are height-based).
- **Very early method development**, where integration has not yet been optimized.

It is never appropriate for reporting quantitative purity.

## Detector Linearity and the Dynamic Range

Area-based quantitation is only valid within the detector's linear dynamic range. The absorbance-concentration relationship follows the Beer–Lambert law:

$$A = \varepsilon \cdot c \cdot l$$

Where $A$ is absorbance, $\varepsilon$ the molar absorptivity, $c$ the concentration, and $l$ the path length. At high concentrations, the relationship bends — detector saturation, stray light, or refractive index effects compress the response, and the main peak area understates the true amount. This inflates purity when impurities are compared against a saturated main peak.

Practical rules: (1) keep the main peak absorbance below about 1.5 AU (many detectors are linear to 2.0 AU but verify empirically); (2) if the main peak is off-scale, the chromatogram is not quantifiable regardless of what integration software reports; (3) validate the linear range during method development ([HPLC Method Validation](08-hplc-method-validation.md)).

## Selecting Integration Parameters in Practice

Integration settings are choices, not facts, and they change the reported purity. The parameters that matter most:

| Parameter | Effect on Purity |
|-----------|------------------|
| Slope sensitivity / threshold | Too low: splits noise into fake peaks; too high: merges real impurities |
| Baseline mode (valley-to-valley vs drop) | Changes how adjacent peaks share area |
| Peak width / expected width | Sets smoothing and peak detection window |
| Minimum area / height | Removes small peaks from the sum — can hide impurities |
| Retention time window | Defines what counts as the "main peak" |

A rigorous report states the integration parameters or at least the minimum area threshold. If a COA says "no impurities detected," ask what minimum area threshold was applied — a threshold of 0.1% means impurities below that level are invisible by definition ([How Laboratories Calculate HPLC Purity](16-how-laboratories-calculate-hplc-purity.md)).

## Area Ratios and Normalized Purity: A Deeper Look

Area normalization reports the main peak as a fraction of all detected peaks, but two subtle choices change the number: (1) **which peaks are included** — the solvent front must be excluded, and peaks below the minimum area threshold are dropped; (2) **how the baseline is drawn** — valley-to-valley integration between the main peak and a small impurity assigns less area to the main peak than a perpendicular drop. The difference between two laboratories reporting 98.0% and 98.6% for the same sample is often entirely explained by integration settings, not chemistry. When comparing COAs, ask for the method's minimum area threshold and baseline mode; a supplier that discloses both demonstrates measurement maturity.

## When Peak Height Is Still Useful: A Balanced View

Although area is the standard for quantitation, peak height retains niche uses: (1) **early-eluting peaks on a rising baseline** — height is less sensitive to baseline drift than area; (2) **very narrow peaks** where baseline-to-baseline width is hard to define; (3) **trace impurity screening** where the question is presence/absence rather than exact amount; (4) **methods with poor resolution** where the height of the main peak is less affected by a partially resolved neighbor than its area. In all these cases, height-based numbers must be labeled as such, because they are not comparable to area-based purity. The rule for reading COAs remains: check which quantity the reported percentage is derived from — a "purity" computed from heights will differ from one computed from areas for the same chromatogram.

## Key Takeaways

- Peak area is proportional to injected mass (Beer-Lambert); peak height is not robust to band broadening.
- Column aging, temperature, flow rate, and tailing all distort height but not area.
- Area percent normalization assumes equal response factors and complete detection — know the assumptions.
- Integration parameters (threshold, baseline mode) directly change reported purity; verify integration marks on the printed chromatogram.
- A single worked example can expose 1–2% discrepancies between area- and height-based numbers.
- Use height only for S/N and detection limits, never for purity.

## References

1. [Snyder, L. R.; Kirkland, J. J.; Dolan, J. W. Introduction to Modern Liquid Chromatography, 3rd ed. Wiley 2010](https://www.wiley.com/en-us/Introduction+to+Modern+Liquid+Chromatography%2C+3rd+Edition-p-9780470167540)
2. [USP General Chapter <621> Chromatography](https://www.usp.org/harmonization-standards/pdg/general-chapter-chromatography)
3. [ICH Q2(R2) Validation of Analytical Procedures (International Council for Harmonisation)](https://www.ich.org/page/quality-guidelines)
4. [Dolan, J. W. Manual Integration Errors. LCGC North America](https://www.chromatographyonline.com/)

Return to [How to Read a Peptide COA](index.md) or read [Retention Time Explained](04-retention-time-explained.md).
