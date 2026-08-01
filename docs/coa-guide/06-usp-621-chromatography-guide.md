---
title: "USP <621> Chromatography Guide: Allowable Method Adjustments"
description: "How USP <621> governs HPLC method adjustments — column dimensions, particle size, flow rate, gradient and temperature tolerances — plus system suitability and the link to ICH validation."
slug: usp-621-chromatography-guide
category: Regulatory Compliance
tags: [USP 621, Pharmacopeia, Chromatography, Method Adjustment, System Suitability, HPLC]
author: RPL Peptides Research Team
published: 2026-08-01
---

# USP <621> Chromatography Guide: Allowable Method Adjustments

USP General Chapter <621> Chromatography defines the official chromatographic procedures used in United States Pharmacopeia monographs, including system suitability requirements and the conditions under which a laboratory may adjust an HPLC method without re-validating it. For peptide quality control laboratories, <621> provides the operational boundary between "running the method as written" and "running a different method that happens to look similar." This article explains the allowable adjustment ranges, the system suitability framework, and how <621> relates to the validation expectations of ICH Q2(R2).

## Scope and Regulatory Role of USP <621>

<621> is a general chapter that applies to all chromatographic procedures cited in USP–NF monographs, covering thin-layer, gas, liquid, and supercritical-fluid chromatography. Its two most important functions for a quality control laboratory are:

1. **System suitability (SST):** a set of performance checks run with the actual analytical system before and during sample analysis to prove the system is capable of producing valid data.
2. **Method adjustment rules:** a defined envelope of permitted changes to chromatographic parameters within which the procedure is still considered the same method, and therefore does not require re-validation.

The chapter is harmonized with the corresponding texts in the European Pharmacopoeia and the Japanese Pharmacopoeia through the Pharmacopeial Discussion Group (PDG), so its principles apply globally even where the local compendium differs in detail.

## The Logic Behind Allowable Adjustments

A monograph method specifies a column, mobile phase, gradient, flow rate, temperature, and detection wavelength. In practice, identical columns are no longer manufactured forever, instrument backpressure limits vary, and analysts need flexibility. <621> permits adjustments that do not change the fundamental separation chemistry — that is, adjustments that keep the selectivity, resolution, and retention behavior essentially equivalent to the original method.

The governing principle is that the adjusted method must still meet the system suitability requirements of the original method. If an adjustment fails system suitability, the change is not permitted under <621> and the laboratory must revert to the monograph conditions or re-develop and re-validate the method.

## Column Parameter Adjustment Table

The following table summarizes the major allowable adjustments for liquid chromatography under <621>. All adjustments are to be made one parameter at a time unless the chapter explicitly permits combined changes, and the modified system must still pass system suitability.

| Parameter | Allowable adjustment | Notes |
|---|---|---|
| Column length ($L$) | $\pm 70\%$ of monograph length | Longer or shorter column; check pressure and resolution |
| Column internal diameter ($d_c$) | $\pm 40\%$ of monograph value | Must keep linear velocity constant by adjusting flow |
| Particle size ($d_p$) | $\pm 40\%$ of monograph value | Do not reduce below 3 µm unless specified by the method |
| Flow rate | Adjusted to keep linear velocity constant: $F_2 = F_1 \times (d_{c,2}/d_{c,1})^2$ | See worked example below |
| Injection volume | May be reduced as needed | Do not exceed the monograph volume |
| Column temperature | $\pm 10\,^\circ\text{C}$ | Adjustments that change selectivity require re-validation |
| Mobile phase pH | $\pm 0.2$ units (if monograph pH $\geq 2$) | Within a stated pH range if one is given |
| Mobile phase composition (isocratic) | $\pm 10\%$ relative of the minor component; not more than $\pm 2\%$ absolute of the minor component for a minor component at 10% or less | Example below |
| Gradient time | $\pm 30\%$ of the gradient segment time | See gradient table |
| Detection wavelength | No adjustment permitted | Change requires a new validation |

The flow-rate adjustment deserves emphasis: when the column internal diameter is changed, the flow rate must be scaled so the linear velocity is preserved. For a change from a 4.6 mm to a 2.1 mm ID column, the new flow rate is:

$$
F_2 = F_1 \times \left(\frac{d_{c,2}}{d_{c,1}}\right)^2 = 1.0 \times \left(\frac{2.1}{4.6}\right)^2 = 1.0 \times 0.208 \approx 0.21\ \text{mL/min}
$$

Running the original 1.0 mL/min flow through a 2.1 mm column would produce roughly five times the linear velocity, compressing retention times and degrading resolution.

## Isocratic Composition Adjustments

For isocratic methods, the composition of the minor component (for example, the organic modifier in a water/organic mixture) may be adjusted by up to $\pm 10\%$ relative, but the absolute change in the percentage of the minor component must not exceed $\pm 2\%$ when the minor component is 10% or less of the mixture.

**Worked example.** Suppose a monograph mobile phase is 80:20 (v/v) water:acetonitrile. The minor component is acetonitrile at 20%. The relative adjustment limit is $0.10 \times 20\% = 2\%$ (absolute), and the absolute cap of 2% is not exceeded. The permitted range is therefore 18–22% acetonitrile. If instead the monograph mobile phase is 95:5 water:acetonitrile, the relative limit is $0.10 \times 5\% = 0.5\%$ (absolute), which is smaller than the 2% absolute cap; the permitted range is 4.5–5.5% acetonitrile. In both cases the adjusted method must still pass system suitability.

## Gradient Adjustments

For gradient methods, the chapter permits:

- The gradient time (the duration of a gradient segment) to be adjusted by $\pm 30\%$.
- The final composition of a segment to be adjusted by up to $\pm 10\%$ absolute of the total gradient span, but the adjusted composition must remain within the span defined by the original starting and ending compositions.
- The gradient volume, defined as the product of flow rate and gradient time, to be kept constant when both flow rate and gradient time are changed.

The gradient volume relationship is useful when transferring a gradient between column diameters:

$$
V_G = F \times t_G
$$

where $V_G$ is the gradient volume, $F$ the flow rate, and $t_G$ the gradient time. If a method uses 1.0 mL/min with a 30-minute gradient ($V_G = 30$ mL) and is transferred to a 2.1 mm column at 0.21 mL/min, the equivalent gradient time is:

$$
t_G = \frac{V_G}{F} = \frac{30}{0.21} \approx 143\ \text{min}
$$

Such a large time scaling is usually impractical; most laboratories instead re-optimize the gradient and demonstrate equivalence, which is a change outside the <621> envelope and therefore requires re-validation.

## System Suitability Requirements

<621> mandates that the analytical system be evaluated with system suitability tests before and during analysis. The key parameters are:

- **Theoretical plate number ($N$)** — column efficiency; for peptide methods a typical acceptance is $N > 2000$ per meter-equivalent or as specified in the monograph.
- **Tailing factor ($T$)** — peak symmetry; typical acceptance $0.8 \le T \le 1.5$ (see [Tailing Factor Explained](12-tailing-factor-explained.md)).
- **Resolution ($R_s$)** — separation between critical peak pairs; $R_s \ge 1.5$ between the target and its nearest impurity is common (see [Resolution in Chromatography](13-resolution-in-chromatography.md)).
- **Relative standard deviation (RSD) of replicate injections** — for a target peak, USP historically specifies $RSD \le 1.0\%$ for five injections when the assay requirement is 100% (approximately), scaled by $\sqrt{n}$ rules for other injection counts.
- **Retention time precision** — repeatability of retention times across injections.

The USP repeatability requirement scales with the number of replicate injections. For $n$ injections the permitted RSD is roughly:

$$
RSD_{\text{limit}} = \frac{K \cdot \sqrt{n}}{t_{90\%,\,n-1}}
$$

where $K$ is a constant tied to the assay tolerance and $t_{90\%,n-1}$ is the Student's $t$ value. In practice, laboratories run five or six replicate injections and apply the tabulated limits from the chapter. A full discussion of these parameters and their acceptance criteria appears in [System Suitability Testing](09-system-suitability-testing.md).

## Relationship Between USP <621> and ICH Q2(R2)

USP <621> and ICH Q2(R2) operate at different layers of the quality system:

- **<621> governs the running of compendial methods** — it defines what counts as "the same method" (adjustments) and proves the system works on the day of analysis (SST).
- **ICH Q2(R2) governs the proof that a method measures what it claims** — specificity, accuracy, precision, linearity, range, LOD, LOQ, and robustness (see [ICH Q2(R2) Explained](07-ich-q2r2-explained.md)).

The two interact in practice: a method that has been re-validated under Q2(R2) after a change outside the <621> envelope must demonstrate system suitability under the new conditions; conversely, a system suitability failure under <621> means the validated method cannot be used for its intended purpose regardless of the validation data on file. Together they form the regulatory backbone of [HPLC Method Validation](08-hplc-method-validation.md) and of the [analytical method transfer](10-analytical-method-transfer.md) between laboratories.

## Common Errors When Applying <621>

The most frequent mistakes observed in peptide QC laboratories include:

- **Adjusting multiple parameters simultaneously** and assuming the combined change is still within the envelope — <621> adjustments are intended to be applied one parameter at a time; combined changes require equivalence demonstration or re-validation.
- **Changing the detection wavelength** — not permitted; wavelength changes are validation changes.
- **Scaling flow rate when changing column length only** — flow rate scaling applies to internal diameter changes; length changes alter the number of theoretical plates and the backpressure but not the linear velocity at constant flow.
- **Ignoring the pH adjustment limit** — a $\pm 0.2$ pH change can dramatically alter peptide ionization and selectivity; exceeding the limit without re-validation is a common audit finding.
- **Using SST acceptance criteria that are looser than the monograph** — the monograph criteria are the floor; a laboratory may not relax them.

## Key Takeaways

- USP <621> permits defined adjustments to column length ($\pm 70\%$), internal diameter ($\pm 40\%$), particle size ($\pm 40\%$), flow rate (linear-velocity scaling), temperature ($\pm 10\,^\circ\text{C}$), and gradient time ($\pm 30\%$) without re-validation, provided system suitability still passes.
- Flow rate must be scaled with the square of the diameter ratio ($F_2 = F_1 (d_{c,2}/d_{c,1})^2$); ignoring this destroys resolution when changing column IDs.
- Isocratic composition adjustments are limited to $\pm 10\%$ relative of the minor component, capped at $\pm 2\%$ absolute when the minor component is at or below 10%.
- Detection wavelength changes are never permitted as <621> adjustments, and combined parameter changes fall outside the adjustment envelope.
- System suitability (plates, tailing, resolution, injection RSD) is the gate: an adjusted method that fails SST must revert to monograph conditions or be re-validated.
- <621> defines "same method" operationally, while ICH Q2(R2) proves method performance — both are required for defensible peptide purity data.

## References

1. [USP General Chapter <621> Chromatography (USP–NF)](https://www.usp.org/harmonization-standards/pdg/general-chapter-chromatography)
2. [ICH Q2(R2) Validation of Analytical Procedures (International Council for Harmonisation)](https://www.ich.org/page/quality-guidelines)
3. [Pharmacopeial Discussion Group — PDG Harmonization Topics](https://www.usp.org/health-quality-safety/global-standards/pharmacopeial-discussion-group)
4. [Snyder, L. R.; Kirkland, J. J.; Dolan, J. W. Introduction to Modern Liquid Chromatography, 3rd ed. (Wiley)](https://pubmed.ncbi.nlm.nih.gov/)
5. [FDA Guidance for Industry: Analytical Procedures and Methods Validation for Drugs and Biologics](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/analytical-procedures-and-methods-validation-drugs-and-biologics)
6. [Dolan, J. W. Method Adjustment and System Suitability — LCGC](https://www.chromatographyonline.com/)

Return to [How to Read a Peptide COA](index.md) or read [ICH Q2(R2) Explained](07-ich-q2r2-explained.md).
