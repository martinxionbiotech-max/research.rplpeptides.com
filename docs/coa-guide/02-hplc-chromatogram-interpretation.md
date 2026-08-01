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

A chromatogram is a graphical plot of detector response versus time. Interpreting a chromatogram requires evaluating peak symmetry, baseline noise, and signal resolution. For research peptides, the chromatogram printed on a Certificate of Analysis (COA) is the primary evidence of purity — learning to read it critically is an essential quality-control skill.

## The Five Elements of Every Chromatogram

Every useful chromatogram contains five elements you should check in order:

1. **Baseline**: the detector signal when no analyte elutes. A stable, flat baseline is the foundation of reliable integration.
2. **Solvent front (void volume peak)**: the unretained component eluting at the column void time $t_0$; it marks the start of the run.
3. **Analyte peaks**: resolved signals corresponding to the peptide and its impurities.
4. **Noise**: random high-frequency fluctuation of the baseline.
5. **Integration marks**: the software's assignment of peak start/end points, shown as tick marks or vertical lines on the printed chromatogram.

## Baseline Stability and Its Importance

The baseline should be flat (drift below 0.1% of full scale per minute) and free of wandering. Baseline drift has three common causes:

- **Column equilibration failure**: insufficient re-equilibration between gradient runs leaves residual mobile phase composition changes.
- **Temperature fluctuation**: ambient temperature changes alter detector response; a column oven set to $40\,^\circ\text{C}$ stabilizes retention and baseline.
- **Detector warm-up**: UV detectors need 20–30 minutes to reach thermal equilibrium after lamp ignition.

A rising baseline under gradient elution is normal when the mobile phase B (organic modifier) absorbs UV light. What matters is that the drift is smooth and reproducible between runs.

## Signal-to-Noise Ratio (S/N)

The signal-to-noise ratio quantifies the smallest peak that can be reliably distinguished from background noise. It is defined as:

$$\text{S/N} = \frac{2H}{h}$$

Where $H$ is peak height measured from baseline, and $h$ is peak-to-peak noise of the baseline in a blank run (measured over a representative region, typically 20 times the peak width at half height).

### Worked Example

A peptide peak has a height $H = 15.0$ mAU. In a blank injection, the baseline noise spans $h = 0.15$ mAU peak-to-peak:

$$\text{S/N} = \frac{2 \times 15.0}{0.15} = 200$$

An S/N of 200 is excellent — well above the S/N $\ge$ 10 required for quantitation and S/N $\ge$ 3 required for detection (see [ICH Q2(R2) Explained](07-ich-q2r2-explained.md) for the LOD/LOQ definitions).

## The Solvent Front and Void Volume

The solvent front is the first disturbance on the chromatogram, eluting at the void time $t_0$. It contains unretained material: injection solvent, salts, and highly polar components. Key points:

- The void volume of a $4.6 \times 250$ mm column is approximately 2.5–3.0 mL; at 1.0 mL/min, $t_0 \approx 2.5$–3.0 min.
- A large solvent-front peak can mask early-eluting impurities. If the peptide elutes very early, consider a weaker injection solvent (match the injection solvent to the starting mobile phase).
- Never integrate the solvent front as an analyte peak; it is not a real component.

## Ghost Peaks: Causes and Prevention

Ghost peaks (also called system peaks or artifact peaks) are reproducible peaks that appear even in blank injections. Common causes:

| Cause | Signature | Prevention |
|-------|-----------|------------|
| Contaminated mobile phase | Peaks grow with time | Use fresh HPLC-grade solvents; filter mobile phase |
| Injector carryover | Peaks appear after high-concentration samples | Add needle-wash cycles (e.g., 10% methanol or acetonitrile) |
| Buffer precipitation | Irregular spikes, pressure instability | Pre-mix buffers; check salt solubility in organic phase |
| Detector cell contamination | Broad, drifting baseline humps | Clean cell with 50% nitric acid, then water |
| Column bleed | Small peaks at high organic % | Use a column compatible with the mobile phase pH |

If a ghost peak co-elutes with the peptide, the reported purity is unreliable. The standard test: run a blank injection under the same gradient and compare.

## Integration Parameters That Change Purity Results

Software integration settings dramatically affect reported peak areas. The three most consequential parameters:

1. **Slope sensitivity (threshold)**: the minimum rate of signal change that defines a peak start/end. Too low → noise is integrated as peaks; too high → real peaks are merged or truncated.
2. **Peak width**: the expected width at half height; wrong values distort the smoothing and baseline-fit algorithm.
3. **Baseline mode**: valley-to-valley vs. drop-line vs. tangent skim. For unresolved impurity peaks, the choice of baseline mode changes the area split.

A well-integrated chromatogram shows integration marks at the true peak boundaries — at the baseline, not inside the peak. If the printed chromatogram on a COA shows integration marks inside peak tails, the reported purity may be inflated.

## Peak Shape as a Diagnostic Tool

Peak shape reveals column and method health:

- **Symmetrical peak**: healthy column, proper loading.
- **Tailing** (peak leans right): secondary interactions with silanol groups, or column overload. See [Tailing Factor Explained](12-tailing-factor-explained.md).
- **Fronting** (peak leans left): column overload or injection solvent stronger than the mobile phase.
- **Shoulder** (bump on the side of the main peak): a co-eluting impurity or a diastereomer; check with LC-MS. See [Understanding LC-MS Reports](01-understanding-lc-ms-reports.md).

## Common Interpretation Mistakes

1. **Reading purity from peak height**: Height varies with conditions; area is the accepted metric. See [Peak Area vs Peak Height](03-peak-area-vs-peak-height.md).
2. **Ignoring the baseline noise level**: A noisy baseline means small impurity peaks may be invisible; request the LOD/LOQ of the method.
3. **Accepting a single wavelength**: Purity at 214 nm (peptide bond) differs from purity at 280 nm (aromatic residues). Check which wavelength the COA used.
4. **Not checking for peak purity**: A "clean" single peak can hide a co-eluting impurity; UV spectrum comparison or MS detection is required to prove peak purity.

## Gradient vs Isocratic Chromatograms

Peptide purity methods use either gradient or isocratic elution, and the chromatogram looks different in each case:

| Feature | Isocratic | Gradient |
|---------|-----------|----------|
| Mobile phase | Constant composition | Composition changes over time |
| Peak width | Broadens with retention | Narrow throughout the run |
| Run time | Long for late peaks | Controlled by gradient length |
| Baseline | Flat (low drift) | Rising baseline with %B increase |
| Typical use | Short peptides, simple mixtures | Most peptide purity methods |

On a gradient chromatogram, a steadily rising baseline is normal — UV-absorbing mobile phase components increase as %B rises. What is *not* normal is a step change in the baseline, which usually signals a pump malfunction or air in the line.

## A Worked Walk-Through of a Realistic Purity Chromatogram

Consider a 25-residue peptide analyzed by RP-HPLC at 214 nm. The report shows: main peak at 18.4 min (area 9,450 mAU·s), a small peak at 16.9 min (area 120), a peak at 19.6 min (area 85), and a pre-peak at 3.2 min that the integration settings exclude.

Step 1: the pre-peak at 3.2 min coincides with the void volume — it is the solvent front and must be excluded. Step 2: the 16.9 min peak elutes 1.5 min before the main peak — consistent with a more polar species, possibly the methionine sulfoxide form ([Oxidized Peptide Impurities](15-oxidized-peptide-impurities.md)). Step 3: the 19.6 min peak elutes after the main peak — a more hydrophobic species, possibly a deletion peptide missing a polar residue ([Deletion Peptides Explained](14-deletion-peptides-explained.md)). Step 4: purity by area normalization is $9450 / (9450 + 120 + 85) = 97.9\%$. Step 5: ask for the LC-MS masses of those two peaks to confirm identities before accepting the numbers.

## Electronic Data, Audit Trails, and Reproducible Chromatograms

The chromatogram on a COA is a representation of electronic data, and its trustworthiness depends on the data system behind it: (1) raw data files (not screenshots) should be archivable and re-integrable; (2) audit trails should record who processed the data, when, and what was changed — manual reintegration must be flagged; (3) the processing method (integration parameters) should be stored with the data so the same chromatogram can be reproduced; (4) time-stamped sequence logs tie each peak to an injection. When a buyer re-analyzes a peptide and obtains a different purity than the COA, the first question is not "which lab is wrong" but "are the processing methods identical?". Reproducibility between laboratories is a method question, not a blame question ([Analytical Method Transfer](10-analytical-method-transfer.md)).

## Common Interpretation Mistakes and Their Consequences

Five mistakes dominate chromatogram misinterpretation in peptide QC. (1) **Treating every baseline blip as an impurity** — noise spikes at the detection threshold inflate the impurity sum and deflate purity; the LOQ exists precisely to separate signal from noise. (2) **Ignoring the void peak** — counting the solvent front as a component changes the denominator and the purity. (3) **Comparing purities across different wavelengths** — 214 nm and 220 nm numbers are not interchangeable. (4) **Assuming a single peak means one compound** — co-elution is invisible to UV alone; LC-MS is the arbiter. (5) **Trusting the software's default integration** — defaults are generic, not method-specific; validated integration parameters must be stored and used. Each mistake moves the purity number in a predictable direction, and recognizing them is the first step to reading a COA critically rather than literally.

## Key Takeaways

- Always check baseline flatness, solvent front position, and integration marks before trusting a purity number.
- S/N $\ge$ 10 is required for quantitation; S/N $\ge$ 3 for detection.
- Ghost peaks in blank runs invalidate the method; investigate carryover and mobile phase contamination.
- Integration parameters (slope threshold, peak width, baseline mode) directly change the reported purity — they must be documented.
- Peak shape is a diagnostic: tailing, fronting, and shoulders each point to specific root causes.
- Purity is wavelength-dependent; always record and report the detection wavelength.

## References

1. [Snyder, L. R.; Kirkland, J. J.; Dolan, J. W. Introduction to Modern Liquid Chromatography, 3rd ed. Wiley 2010](https://www.wiley.com/en-us/Introduction+to+Modern+Liquid+Chromatography%2C+3rd+Edition-p-9780470167540)
2. [USP General Chapter <621> Chromatography](https://www.usp.org/harmonization-standards/pdg/general-chapter-chromatography)
3. [ICH Q2(R2) Validation of Analytical Procedures (International Council for Harmonisation)](https://www.ich.org/page/quality-guidelines)
4. [Dolan, J. W. LC Troubleshooting: Ghost Peaks. LCGC North America](https://www.chromatographyonline.com/)

Return to [How to Read a Peptide COA](index.md) or read [Peak Area vs Peak Height](03-peak-area-vs-peak-height.md).
