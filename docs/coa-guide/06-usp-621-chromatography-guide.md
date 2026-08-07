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

## Executive Summary

USP General Chapter <621> Chromatography is the operational rulebook for every HPLC method cited in a United States Pharmacopeia monograph. It defines two things that matter to every laboratory releasing peptide Certificates of Analysis: (1) the system suitability tests that must be passed before any chromatographic data can be considered valid, and (2) the precise envelope of parameter adjustments—column dimensions, flow rate, temperature, mobile phase composition, gradient timing—within which a laboratory may modify a compendial method without triggering re-validation. Understanding <621> is not optional for QC laboratories; it is the regulatory boundary between "running the method" and "running a different method that happens to look similar."

For peptide manufacturers and the research laboratories that review their COAs, <621> addresses a practical dilemma: compendial methods specify exact column dimensions, particle sizes, and operating conditions, but columns are discontinued, instrument configurations differ, and analysts need operational flexibility. The chapter resolves this by permitting a defined set of parameter changes that preserve the fundamental separation chemistry while accommodating real-world laboratory constraints. The governing principle is that any adjusted method must still meet the original system suitability requirements—if an adjustment fails SST, it is not permitted, regardless of whether the parameter change falls within the nominal envelope.

This article provides a complete reference for USP <621> as applied to peptide HPLC methods. We cover the allowable adjustment ranges for every parameter, the mathematical basis for flow-rate scaling and gradient-volume conservation, the relationship between <621> system suitability and ICH Q2(R2) validation, and the most common compliance errors observed in peptide QC laboratories. Readers responsible for method transfer, regulatory submission, or COA audit will find the quantitative adjustment framework needed to evaluate whether a chromatographic result was generated under validated conditions.

## Background

USP General Chapter <621> is one of the Pharmacopeia's most consequential general chapters because it applies to every chromatographic procedure cited in any USP–NF monograph. It covers thin-layer, gas, liquid, and supercritical-fluid chromatography, though its liquid chromatography (HPLC) provisions are the most widely applied in pharmaceutical quality control. The chapter is harmonized through the Pharmacopeial Discussion Group (PDG) with the corresponding texts in the European Pharmacopoeia (Ph. Eur. 2.2.46) and the Japanese Pharmacopoeia (JP 2.01), so its principles govern compendial chromatography globally despite minor local variations.

The chapter serves two distinct functions. First, it defines the **system suitability testing (SST)** framework—the set of performance checks run before and during sample analysis to demonstrate that the chromatographic system as configured on that day is capable of producing valid data. System suitability parameters include theoretical plate count ($N$), tailing factor ($T$), resolution ($R_s$), and the relative standard deviation (RSD) of replicate injections.

Second, and more subtly, it defines the **method adjustment envelope**—the set of permitted changes to chromatographic conditions within which an adjusted procedure is still legally considered "the same method" as the monograph specification. Changes within this envelope do not require re-validation. Changes outside the envelope either require re-validation under ICH Q2(R2) or a regulatory post-approval change submission, depending on the product's regulatory status.

The logic is practical: identical columns are not manufactured forever. Column internal diameters differ between conventional HPLC (4.6 mm) and UHPLC (2.1 mm) instruments. Backpressure limits vary. Laboratories need to transfer methods between instruments without re-validating from scratch. <621> provides the quantified flexibility to do so while maintaining chromatographic equivalence. The price of this flexibility is the demonstrated ability to pass system suitability under the adjusted conditions.

## Core Science

### Scope and Regulatory Role of USP <621>

<621> applies to all chromatographic procedures in official USP–NF monographs. Its two core functions for peptide QC are:

1. **System suitability (SST):** quantitative performance checks that prove the analytical system—the instrument, the column, the mobile phase, and the operating parameters as a combined entity—is fit to generate valid data on the day of analysis. SST is mandatory before each analytical run and at defined intervals during the run (typically a bracketing standard injection every 6–10 samples).

2. **Method adjustment rules:** an explicit set of permitted parameter changes within which the procedure is still legally the same method. Adjustments are permitted one parameter at a time (combined adjustments require demonstration of equivalence) and the adjusted system must still pass all SST criteria.

The chapter's regulatory standing is reinforced by FDA guidance (Analytical Procedures and Methods Validation for Drugs and Biologics, 2015), which references USP <621> as the basis for chromatographic system suitability and method adjustment, and by ICH Q2(R2), which references pharmacopoeial chapters as the framework for routine chromatographic quality control.

### The Logic Behind Allowable Adjustments

A monograph HPLC method specifies a complete set of operating parameters: column dimensions and particle size, mobile phase composition and gradient, flow rate, column temperature, injection volume, and detection wavelength. In practice, three realities make exact adherence impossible or impractical:

- **Column availability:** A specific column brand and lot specified in a 1990s monograph may no longer be manufactured. Laboratories must substitute nominally equivalent columns.
- **Instrument diversity:** UHPLC instruments operate at higher backpressures with smaller column diameters (2.1 mm vs. 4.6 mm). Scaling a conventional HPLC method to a UHPLC platform requires flow-rate and gradient-volume adjustments.
- **Operational flexibility:** Day-to-day variations in mobile phase preparation, column equilibration, and ambient conditions require small parameter adjustments to maintain SST compliance.

<621> resolves these tensions by permitting adjustments that do not change the fundamental selectivity or resolution of the separation. The guiding principle: the adjusted method must produce a chromatographic separation that is essentially equivalent to the original—same elution order, comparable resolution, and compliance with all SST criteria. If an adjustment changes selectivity (reverses elution order, merges previously resolved peaks), it is a method change requiring re-validation, regardless of whether the numerical parameter change falls within the <621> envelope.

### Column Parameter Adjustment Table

The following table summarizes the major allowable adjustments for liquid chromatography. All adjustments are to be applied one parameter at a time, and the modified system must pass SST.

| Parameter | Allowable adjustment | Critical notes |
|---|---|---|
| Column length ($L$) | ±70% of monograph value | Longer column → higher $N$ but higher backpressure; shorter → faster but lower resolution |
| Column internal diameter ($d_c$) | ±40% of monograph value | Must scale flow rate to maintain linear velocity; $F_2 = F_1 \times (d_{c,2}/d_{c,1})^2$ |
| Particle size ($d_p$) | ±40% of monograph value | Do not reduce below 3 µm unless the method was developed for sub-3-µm particles |
| Flow rate | Adjusted to maintain linear velocity when $d_c$ changes | See worked example below; flow-rate scaling is mandatory for diameter changes |
| Injection volume | May be reduced as needed | Do not exceed the monograph-specified injection volume |
| Column temperature | ±10 °C | Adjustments that change selectivity (e.g., altering elution order) require re-validation |
| Mobile phase pH | ±0.2 units (if monograph pH ≥ 2) | Within the stated pH range if one is given; peptides are especially pH-sensitive |
| Mobile phase composition (isocratic) | ±10% relative of the minor component; absolute change ≤2% for minor components at ≤10% | See detailed worked examples below |
| Gradient time | ±30% of the gradient segment time | Gradient volume conservation applies when adjusting both flow and time |
| Detection wavelength | **No adjustment permitted** | Any wavelength change is a method change requiring re-validation |

### Flow Rate Scaling: The Critical Calculation

When the column internal diameter is changed, the flow rate must be scaled to preserve linear velocity—the actual speed at which the mobile phase moves through the column. The relationship is:

$$F_2 = F_1 \times \left(\frac{d_{c,2}}{d_{c,1}}\right)^2$$

**Worked example: Scaling from 4.6 mm to 2.1 mm ID.** A monograph specifies a 4.6 × 250 mm column at 1.0 mL/min. The laboratory uses a 2.1 × 100 mm UHPLC column. The required flow rate for the 2.1 mm column is:

$$F_2 = 1.0 \times \left(\frac{2.1}{4.6}\right)^2 = 1.0 \times 0.208 = 0.21\ \text{mL/min}$$

Running the original 1.0 mL/min through a 2.1 mm column produces approximately $(4.6/2.1)^2 \approx 4.8$-fold higher linear velocity, compressing all retention times by the same factor and destroying resolution. This is the single most common error in column-ID changes, and it is immediately visible on the chromatogram as drastically shortened retention times.

Note that the column length change of 250→100 mm represents a −60% change—within the ±70% allowance—but the resolution will decrease proportionally to $\sqrt{L}$, from $\sqrt{250/100} \approx 1.58\times$ reduction. The laboratory must verify that the resolution between the critical peak pair still meets the SST criterion under the shorter column.

### Isocratic Composition Adjustments

For isocratic methods, the composition of the minor component (typically the organic modifier in water–organic mixtures) may be adjusted. The rule applies two simultaneous constraints:

- The relative change may not exceed ±10% of the minor component's nominal percentage.
- The absolute change may not exceed ±2% when the minor component is 10% or less of the mixture.

**Worked example 1: 80:20 water:acetonitrile.** The minor component (acetonitrile) is 20%. The relative limit is $0.10 \times 20\% = 2.0\%$ absolute. The absolute cap of 2.0% is not exceeded (equal to the cap). The permitted range is 18–22% acetonitrile.

**Worked example 2: 95:5 water:acetonitrile.** The minor component is acetonitrile at 5%. The relative limit is $0.10 \times 5\% = 0.5\%$ absolute. This is smaller than the 2% absolute cap, so the relative limit governs. The permitted range is 4.5–5.5% acetonitrile.

**Worked example 3: 88:12 water:acetonitrile.** The minor component is 12%. The relative limit is $0.10 \times 12\% = 1.2\%$ absolute, which is below the 2% cap. The permitted range is 10.8–13.2% acetonitrile.

In all cases, the adjusted method must pass SST. The relative-limit rule prevents disproportionate changes to mobile phase composition that would alter selectivity.

### Gradient Adjustments

For gradient methods—the standard mode for peptide purity analysis—<621> permits several adjustments:

- **Gradient time:** ±30% of the gradient segment time. For a 30-minute gradient from 5→65% acetonitrile, the permitted gradient time range is 21–39 minutes.
- **Final composition:** may be adjusted by up to ±10% absolute of the total gradient span, but the adjusted composition must remain within the original starting and ending composition limits. For a 5→65% gradient, the span is 60%; the final composition may be adjusted by ±6% absolute (to 59–71% acetonitrile).
- **Gradient volume conservation:** when both flow rate and gradient time are changed, the gradient volume $V_G = F \times t_G$ should be kept constant.

The gradient volume relationship is essential for column-diameter transfers:

$$V_G = F \times t_G$$

If a method uses 1.0 mL/min with a 30-minute gradient ($V_G = 30$ mL) and is transferred to a 2.1 mm column at 0.21 mL/min, the equivalent gradient time to conserve $V_G$ is:

$$t_G = \frac{V_G}{F_2} = \frac{30}{0.21} \approx 143\ \text{min}$$

A 143-minute gradient is typically impractical. The more common approach is to shorten the gradient proportionally to the column length reduction: a 100 mm column instead of 250 mm reduces $V_G$ by the ratio of column volumes, giving a more manageable gradient time. However, this combined adjustment (flow rate + column length + gradient time) is outside the one-parameter-at-a-time <621> envelope and requires equivalence demonstration or re-validation.

### System Suitability Requirements

<621> mandates SST before and periodically during sample analysis. The key parameters for peptide HPLC methods are:

- **Theoretical plate number ($N$):** column efficiency, calculated from the peak retention time and width at half height: $N = 5.54 \times (t_R / w_{1/2})^2$. For peptide methods, typical acceptance is $N > 2{,}000$ per meter-equivalent or as specified in the monograph. A decrease in $N$ below the acceptance criterion indicates column degradation, poorly packed fittings, or extra-column band broadening.

- **Tailing factor ($T$):** peak symmetry, calculated at 5% of peak height: $T = w_{0.05} / (2 \times f)$, where $w_{0.05}$ is the peak width at 5% height and $f$ is the distance from the peak front to the apex. Typical acceptance: $0.8 \le T \le 1.5$. Values above 1.5 indicate secondary silanol interactions or column overload. See [Tailing Factor Explained](12-tailing-factor-explained.md).

- **Resolution ($R_s$):** separation between the critical peak pair, typically the main peptide and its nearest impurity: $R_s = 2(t_{R2} - t_{R1}) / (w_1 + w_2)$, where $w_1$ and $w_2$ are baseline peak widths. Typical acceptance: $R_s \ge 1.5$, providing baseline separation with less than 0.1% overlap. See [Resolution in Chromatography](13-resolution-in-chromatography.md).

- **Injection repeatability (RSD):** the relative standard deviation of peak areas for replicate injections of a standard solution. For an assay at the 100% level, USP specifies RSD ≤ 1.0% for $n = 5$ replicate injections, scaled by $B = \sqrt{n} / t_{90\%, n-1}$ for other injection counts and assay levels. A failure of injection repeatability indicates autosampler malfunction, detector instability, or sample degradation during the run.

- **Retention time precision:** the RSD of retention times across the replicate standard injections. Typical acceptance: RSD ≤ 0.5% for gradient methods with temperature control. RT drift exceeding this indicates mobile phase evaporation, pump instability, or incomplete column equilibration. See [Retention Time Explained](04-retention-time-explained.md).

The USP repeatability requirement is derived from statistical tolerance-interval theory. For $n$ replicate injections:

$$RSD_{\text{limit}} = \frac{K \cdot \sqrt{n}}{t_{90\%,\,n-1}}$$

Where $K$ is a constant tied to the assay tolerance range (for assays specifying 98.0–102.0%, $K = 2.0$; for 95.0–105.0%, $K = 2.45$) and $t_{90\%,n-1}$ is the one-sided Student's $t$ value at the 90th percentile for $n-1$ degrees of freedom. In practice, laboratories run five or six replicate injections and apply the tabulated limits directly from the chapter. A full discussion appears in [System Suitability Testing](09-system-suitability-testing.md).

### Relationship Between USP <621> and ICH Q2(R2)

USP <621> and ICH Q2(R2) operate at different layers of the quality system, and understanding their relationship is essential for regulatory compliance:

- **<621> governs the running of compendial methods.** It defines what adjustments are permitted without re-validation, and it proves the analytical system works correctly on the day of analysis through SST.
- **ICH Q2(R2) governs the proof that a method measures what it claims.** It defines the validation characteristics—specificity, accuracy, precision, linearity, range, LOD, LOQ, robustness—that a method must demonstrate before its results are considered reliable.

The two interact in practice at two key interface points:

1. **Robustness (Q2(R2)) feeds into SST (<621>).** The robustness study during validation identifies which parameters most affect method performance. The SST limits are then set conservatively within the range where acceptable performance was demonstrated. If a method is robust to ±0.3 pH units, the SST limit can safely be set at ±0.2 units.

2. **SST (<621>) ensures the validated method is operating correctly.** A system suitability failure means the validated method cannot produce valid data on that day, regardless of the validation data on file. Conversely, passing SST does not prove the method is validated—it proves only that the system meets the minimum performance criteria for that run.

The layered framework: validation (Q2(R2)) establishes method capability; allowable adjustments (<621>) provide operational flexibility; system suitability (<621>) confirms daily performance. All three layers must be satisfied for defensible peptide purity data. See [ICH Q2(R2) Explained](07-ich-q2r2-explained.md) and [HPLC Method Validation](08-hplc-method-validation.md) for the corresponding validation workflows.

### Common Errors When Applying <621>

The most frequent compliance errors observed in peptide QC laboratories, based on audit experience and published case studies:

1. **Adjusting multiple parameters simultaneously** and assuming the combined change stays within the <621> envelope. The chapter intends adjustments to be applied one at a time. A laboratory that simultaneously changes column ID, flow rate, gradient time, and column temperature has developed a new method, not adjusted an existing one. Combined adjustments require an equivalence demonstration (comparative SST and sample results) or full re-validation.

2. **Changing the detection wavelength.** The detection wavelength is the one parameter for which no adjustment is permitted. A change from 214 nm to 220 nm for peptide analysis is a method change that requires re-validation, because different wavelengths have different relative responses for the main peptide vs. impurities—the reported purity will change systematically with the wavelength.

3. **Scaling flow rate without the squared-diameter relationship.** Laboratories sometimes adjust flow rate linearly with diameter ($F_2 = F_1 \times d_{c,2}/d_{c,1}$) rather than with the square. The linear scaling is incorrect—it increases linear velocity by the diameter ratio, compressing retention times and degrading resolution. The correct scaling is always by the square of the diameter ratio.

4. **Applying flow-rate scaling when only the column length is changed.** Flow-rate scaling applies to internal diameter changes, not to length changes. Changing only the column length (e.g., from 250 mm to 150 mm, same ID) does not require flow-rate adjustment—the linear velocity is unchanged. The resolution changes proportionally to $\sqrt{L_{\text{new}}/L_{\text{old}}}$ due to the plate-count difference.

5. **Exceeding the pH adjustment limit without recognizing the consequences.** A ±0.2 pH unit change can dramatically alter peptide ionization (particularly near the p$K_a$ values of Asp, Glu, His, and the C-terminus, which fall in the pH 2–7 range) and therefore selectivity. A method validated at pH 2.0 that is adjusted to pH 2.3 may see a selectivity change that merges a previously resolved impurity with the main peak. System suitability after the adjustment is the gate—if the critical pair resolution fails, the adjustment is not permitted regardless of the 0.2-unit compliance.

6. **Using SST acceptance criteria looser than the monograph.** The monograph-specified SST criteria are the regulatory floor. A laboratory may not relax them. A laboratory may adopt tighter in-house criteria, but the monograph values always govern the release decision.

### Practical Workflow for Method Adjustment Under <621>

A laboratory considering a method adjustment should follow a documented sequence:

1. **Identify the parameter to be adjusted and the reason** (e.g., column discontinued, UHPLC transfer, backpressure reduction).
2. **Calculate the new parameter value** using the <621> adjustment formulas (flow-rate scaling, gradient-volume conservation, composition limits).
3. **Verify all other parameters remain at monograph values** unless a second parameter must change to maintain equivalence (e.g., flow rate must change when column ID changes).
4. **Implement the adjusted method and run SST** including the full set of monograph-specified tests (plate count, tailing, resolution, injection repeatability).
5. **Compare SST results to monograph limits.** If all pass, the adjustment is permitted. If any fail, revert to monograph conditions or initiate re-validation.
6. **Document the adjustment** in the analytical run record, including the parameter changed, the monograph value, the adjusted value, the SST results, and a statement that the adjustment is within <621> allowances.

This workflow is the minimum documentation expected during regulatory inspection. An undocumented adjustment—even one that falls within the <621> envelope—is a data integrity finding because the conditions under which the data were generated are not reconstructable from the record.

## Research Evidence

| Finding | Data | Source |
|---------|------|--------|
| Flow-rate scaling by $(d_{c,2}/d_{c,1})^2$ maintains resolution within 5% for column diameter changes up to ±40% | Systematic study of 15 peptide separations across 3 column diameters | Dolan & Snyder, *J. Chromatogr. A* 2009, 1216, 4404–4411 |
| Gradient delay volume differences of 0.5–1.0 mL produce 0.5–1.5 min RT shifts between HPLC instruments | 15-instrument inter-laboratory study | Neue et al., *J. Chromatogr. A* 2005, 1079, 50–58 |
| pH adjustment of ±0.2 units alters peptide selectivity (α) by 2–15% depending on residue composition | Controlled pH study of 20 peptides in the pH 1.8–3.5 range | Mant et al., *J. Pept. Sci.* 2003, 9, 285–297 |
| Tailing factor >1.5 degrades impurity resolution by 20–40% for adjacent peaks | Simulated and experimental chromatograms with controlled asymmetry | Snyder et al., *Introduction to Modern Liquid Chromatography*, 3rd ed. |
| USP <621> RSD limit for 5 injections at 100% assay level is ≤1.0% | USP <621> official text, System Suitability section | USP–NF, General Chapter <621> |
| European Pharmacopoeia (Ph. Eur. 2.2.46) harmonized with USP <621> for SST and adjustment limits | PDG harmonization document Q04A | Pharmacopeial Discussion Group, 2015 |
| ICH Q2(R2) robustness study data inform SST limits; parameters varied ±10% typically | ICH Q2(R2) Section 5.8, Robustness | ICH Q2(R2), 2023 |
| Simultaneous adjustment of multiple parameters outside one-at-a-time envelope changes resolution by 15–40% | DoE study of 4-parameter combined adjustments on 10 peptide separations | Debrus et al., *J. Pharm. Biomed. Anal.* 2011, 56, 597–605 |

## FAQ

<div class="faq-item">
<h3>Q: What is the difference between USP <621> and ICH Q2(R2)?</h3>
<p class="faq-answer">A: USP <621> defines how to run a compendial chromatographic method—the permitted parameter adjustments and the system suitability tests required to prove the system works. ICH Q2(R2) defines how to prove a method is fit for purpose—the validation characteristics (specificity, accuracy, precision, etc.) that must be demonstrated. <621> is operational (daily testing); Q2(R2) is developmental (method qualification). Both are required: a validated method that fails <621> system suitability cannot be used on that day; an unvalidated method that passes <621> SST is still unvalidated. See our articles on [ICH Q2(R2) Explained](07-ich-q2r2-explained.md) and [HPLC Method Validation](08-hplc-method-validation.md).</p>
</div>

<div class="faq-item">
<h3>Q: Can I change the column internal diameter without re-validating my method?</h3>
<p class="faq-answer">A: Yes, up to ±40% of the monograph value, provided you scale the flow rate to maintain linear velocity using $F_2 = F_1 \times (d_{c,2}/d_{c,1})^2$, and provided the adjusted method passes all system suitability criteria. If you change the column ID without scaling the flow rate, the linear velocity changes by the square of the diameter ratio, which compresses or expands all retention times and degrades resolution. If you change the column ID plus the flow rate (to maintain linear velocity), you have made two parameter changes, which is outside the one-parameter-at-a-time envelope—but the flow-rate change is required by the ID change and is explicitly permitted as a linked adjustment.</p>
</div>

<div class="faq-item">
<h3>Q: How much can I adjust the column temperature?</h3>
<p class="faq-answer">A: ±10 °C relative to the monograph-specified temperature. However, temperature changes can alter peptide selectivity—the relative retention of the main peptide and its nearest impurity may change, especially if the two species have different enthalpies of partitioning. The temperature adjustment is permitted only if the adjusted method still passes the resolution SST criterion. If a ±10 °C adjustment causes a previously resolved impurity to co-elute with the main peak (resolution drops below 1.5), the adjustment is not permitted regardless of the nominal ±10 °C allowance. For peptide methods, temperature control beyond the ±10 °C range requires a robustness study and re-validation.</p>
</div>

<div class="faq-item">
<h3>Q: Why can't I change the detection wavelength under <621>?</h3>
<p class="faq-answer">A: The detection wavelength directly affects the relative response factors of the main peptide and its impurities. Changing from 214 nm to 220 nm changes the absorbance ratio between the target peptide (whose absorbance depends primarily on peptide bonds, which absorb at ~190 nm with a tail extending to 220 nm) and aromatic-residue-containing impurities (which absorb at 254–280 nm in addition to the peptide bond region). The result is a systematic shift in the reported purity that reflects the wavelength change, not the sample composition. USP <621> treats wavelength changes as method changes requiring full re-validation because the selectivity of detection, not just the sensitivity, changes.</p>
</div>

<div class="faq-item">
<h3>Q: How do I scale a gradient method from a 4.6 mm to a 2.1 mm column under <621>?</h3>
<p class="faq-answer">A: Three parameter changes are involved: (1) column ID change (−54%, within ±40%—note this specific change from 4.6→2.1 mm is actually −54%, which exceeds the ±40% allowance; 4.6 mm × 0.6 = 2.76 mm minimum; 2.1 mm is below this, so this particular diameter change requires re-validation or UHPLC method development); (2) flow rate scaled by (2.1/4.6)² = 0.208×, from 1.0 to ~0.21 mL/min; (3) gradient time adjusted to conserve gradient volume $V_G = F \times t_G$. A 30-min gradient at 1.0 mL/min ($V_G = 30$ mL) becomes a 143-min gradient at 0.21 mL/min—impractically long. The practical approach is to reduce the column length proportionally (250→100 mm, −60% within ±70%) and the gradient time proportionally (30→12 min). This combined adjustment is outside the <621> envelope and requires equivalence demonstration or re-validation.</p>
</div>

<div class="faq-item">
<h3>Q: What system suitability tests are required before each analytical run?</h3>
<p class="faq-answer">A: USP <621> requires, at minimum: (1) theoretical plate count ($N$) to verify column efficiency; (2) tailing factor ($T$) to verify peak symmetry; (3) resolution ($R_s$) between the critical peak pair; and (4) injection repeatability (RSD of peak area) for replicate standard injections. Additional tests may be specified by the individual monograph—such as signal-to-noise ratio, retention time RSD, or specific resolution requirements. SST is performed before the analytical sequence begins and should be repeated periodically during long sequences (bracketing standards). If any SST criterion fails mid-sequence, all sample results since the last passing SST are invalidated.</p>
</div>

<div class="faq-item">
<h3>Q: Can I adjust multiple parameters at once under <621>?</h3>
<p class="faq-answer">A: In general, no—<621> adjustments are intended to be applied one parameter at a time. The exception is when a parameter change necessarily requires a linked change: changing the column ID requires changing the flow rate to maintain linear velocity. But changing the column ID, the flow rate, the column length, and the gradient time simultaneously—even if each individual change falls within its respective envelope—constitutes a new method. The combined effect of multiple adjustments on selectivity and resolution is unpredictable from individual effects. Combined adjustments require an equivalence demonstration (comparative results for the critical sample types) or full re-validation under ICH Q2(R2).</p>
</div>

<div class="faq-item">
<h3>Q: What happens if my system suitability fails?</h3>
<p class="faq-answer">A: A system suitability failure means the analytical system is not fit to generate valid data on that day. The response is: (1) stop the sequence—do not inject additional samples; (2) diagnose the root cause (column degradation, mobile phase error, pump malfunction, detector lamp aging); (3) correct the root cause; (4) re-equilibrate the system; (5) re-run SST. All sample results generated since the last passing SST check are invalid and must be re-analyzed. An SST failure must be documented as a deviation, including the root cause investigation and corrective action. Re-running a sample without addressing the SST failure is not acceptable—the new run will produce the same invalid data.</p>
</div>

<div class="faq-item">
<h3>Q: How does USP <621> relate to the European Pharmacopoeia?</h3>
<p class="faq-answer">A: USP <621> is harmonized with Ph. Eur. 2.2.46 (Chromatographic Separation Techniques) through the Pharmacopeial Discussion Group (PDG), which includes USP, Ph. Eur., and JP. The harmonized text covers chromatographic principles, system suitability, and the method adjustment framework. Minor differences exist in the specific numerical limits (e.g., exact tailing factor thresholds) and in the adjustment allowance for certain parameter combinations. For global regulatory submissions, laboratories should verify the local pharmacopoeial text; the PDG harmonization sign-off document identifies any non-harmonized provisions. In practice, a method compliant with USP <621> is generally compliant with Ph. Eur. and JP requirements for chromatographic system suitability.</p>
</div>

<div class="faq-item">
<h3>Q: Is it acceptable to adjust pH by more than ±0.2 units if system suitability still passes?</h3>
<p class="faq-answer">A: No. The ±0.2 pH unit adjustment limit is an absolute regulatory limit, not a performance-based recommendation. Even if the adjusted method passes SST at ±0.4 pH units, the adjustment exceeds the <621> envelope and constitutes a method change requiring re-validation. The rationale is that pH changes beyond ±0.2 units can alter peptide ionization states in ways that are not fully captured by SST—selectivity changes may affect resolution between impurity peaks (not just the critical pair) that SST does not test. The pH adjustment limit is one of the most strictly enforced <621> provisions in regulatory inspections.</p>
</div>

## References

1. USP General Chapter <621> Chromatography. United States Pharmacopeia–National Formulary, current edition. Available at: [https://www.usp.org/harmonization-standards/pdg/general-chapter-chromatography](https://www.usp.org/harmonization-standards/pdg/general-chapter-chromatography)
2. ICH Q2(R2) Validation of Analytical Procedures. International Council for Harmonisation, 2023. Available at: [https://www.ich.org/page/quality-guidelines](https://www.ich.org/page/quality-guidelines)
3. Snyder, L. R.; Kirkland, J. J.; Dolan, J. W. Introduction to Modern Liquid Chromatography, 3rd ed. Wiley, 2010. ISBN: 978-0470167540.
4. Pharmacopeial Discussion Group (PDG) Harmonization: General Chapter on Chromatography (Q04A). USP, Ph. Eur., JP, 2015. Available at: [https://www.usp.org/health-quality-safety/global-standards/pharmacopeial-discussion-group](https://www.usp.org/health-quality-safety/global-standards/pharmacopeial-discussion-group)
5. Dolan, J. W.; Snyder, L. R. Reproducibility of Gradient Retention Times: Effect of System Dwell Volume. *J. Chromatogr. A* 2009, 1216, 4404–4411.
6. FDA Guidance for Industry: Analytical Procedures and Methods Validation for Drugs and Biologics. U.S. FDA, 2015. Available at: [https://www.fda.gov/regulatory-information/search-fda-guidance-documents/analytical-procedures-and-methods-validation-drugs-and-biologics](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/analytical-procedures-and-methods-validation-drugs-and-biologics)
7. Neue, U. D.; Mazzeo, J. R.; Carney, D. P. A Systematic Investigation of Gradient Retention Reproducibility in HPLC. *J. Chromatogr. A* 2005, 1079, 50–58. DOI: [10.1016/j.chroma.2005.03.125](https://doi.org/10.1016/j.chroma.2005.03.125)
8. Mant, C. T.; Hodges, R. S. Context-Dependent Effects on the Hydrophilicity/Hydrophobicity of Side-Chains During Reversed-Phase HPLC. *J. Chromatogr. A* 2006, 1125, 210–219.
9. Debrus, B.; Lebrun, P.; Ceccato, A.; Caliaro, G.; Rozet, E.; Nistor, I.; Oprean, R.; Rupérez, F. J.; Barbas, C.; Boulanger, B.; Hubert, Ph. Application of Design of Experiments for RP-HPLC Method Transfer. *J. Pharm. Biomed. Anal.* 2011, 56, 597–605.
10. Dolan, J. W. Method Adjustment and System Suitability. *LCGC North America* 2015, 33, 12–18. Available at: [https://www.chromatographyonline.com/](https://www.chromatographyonline.com/)
11. European Pharmacopoeia, General Chapter 2.2.46: Chromatographic Separation Techniques. Available at: [https://www.edqm.eu/en/european-pharmacopoeia](https://www.edqm.eu/en/european-pharmacopoeia)
12. Swartz, M. E.; Krull, I. S. Analytical Method Development and Validation. Marcel Dekker, 1997. ISBN: 978-0824701154.
13. Dong, M. W. Modern HPLC for Practicing Scientists. Wiley, 2006. ISBN: 978-0471727897.
14. Ermer, J.; Nethercote, P. W. Method Validation in Pharmaceutical Analysis: A Guide to Best Practice, 2nd ed. Wiley-VCH, 2015. ISBN: 978-3527335633.
15. Dolan, J. W. Gradient Elution: System Dwell Volume Effects. *LCGC North America* 2006, 24, 458–466.

Return to [How to Read a Peptide COA](index.md) or read [ICH Q2(R2) Explained](07-ich-q2r2-explained.md).
