---
title: "How Laboratories Calculate HPLC Purity: Area Normalization vs External Standards"
description: "A comprehensive guide to HPLC purity calculation methods for research peptides: area percent normalization, relative response factors, external standard assay, and the critical distinction between purity and content."
slug: how-laboratories-calculate-hplc-purity
category: Analytical Chemistry
tags: [HPLC Purity, Area Normalization, Relative Response Factor, External Standard, Quantitation]
author: RPL Peptides Research Team
published: 2026-08-01
---

# How Laboratories Calculate HPLC Purity: Area Normalization vs External Standards

## Executive Summary

The purity value printed on a peptide Certificate of Analysis (COA) is the single most scrutinized number in the document — yet its meaning depends entirely on the calculation method used to derive it. Two fundamentally different approaches dominate research peptide quality control: area percent normalization and external standard calibration. They answer different questions, rest on different assumptions, and can produce substantially different numerical results for the same batch of peptide.

Area normalization reports what fraction of detected chromatographic signal belongs to the main peptide peak. It is fast, requires no reference standard, and is the industry convention — but it assumes every component in the sample absorbs UV light identically and that nothing goes undetected. External standard calibration reports how much peptide is actually present relative to a characterized reference standard, accounting for differences in detector response, moisture, counterions, and salts.

This article explains both calculation methods in detail, reveals the hidden assumptions behind each number on a COA, and provides a practical framework for interpreting purity data from research peptide suppliers. Understanding these calculations is essential for anyone who uses peptide purity values to make decisions about dosing, experimental design, or supplier qualification.

## Background

### The Dual Meaning of "Purity" in Peptide Analysis

The word "purity" in peptide science conceals an ambiguity that has significant practical consequences. A vial labeled "Peptide X, 98.5% purity, 1 mg" invites the user to assume the vial contains 0.985 mg of peptide X. This assumption is frequently wrong — and the error can exceed 15%.

The confusion arises because "purity" can mean either:

1. **Chromatographic purity**: the fraction of UV-absorbing material that is the main peptide. This is what area normalization reports.
2. **Peptide content**: the actual mass of peptide in the vial relative to what the label claims. This is what external standard calibration measures when combined with moisture and counterion data.

A peptide that is 99% pure by HPLC can contain only 82% peptide by weight after accounting for water (6%), trifluoroacetate counterions (9%), and residual salts (3%). Both numbers are truthful — they simply measure different things. The laboratory that reports only the chromatographic purity without content data is not being dishonest; it is reporting a single measurement that serves a specific purpose. The user who interprets that single measurement as the "true" peptide content is making an assumption the data cannot support.

### The Historical Context

Area percent normalization became the convention for research peptide purity in the 1980s and 1990s, when HPLC instrumentation became widely accessible but reference standards for custom peptide sequences remained prohibitively expensive to prepare and characterize. The logic was straightforward: if you cannot afford a pure reference standard for every peptide you synthesize, you cannot perform an external standard calibration. Area normalization was the best available option — and it remains a perfectly valid measurement for its intended purpose of monitoring batch-to-batch consistency.

The limitation, well understood by analytical chemists but less widely appreciated by end users, is that area normalization is a relative measurement of the chromatogram, not an absolute measurement of the vial contents.

## Core Science

### Area Percent Normalization: The Industry Standard

Area normalization is the most common purity calculation reported on research peptide COAs. The formula is deceptively simple:

$$\text{Purity (\%)} = \frac{A_{\text{main}}}{\sum A_i} \times 100$$

Where $A_{\text{main}}$ is the integrated peak area of the target peptide and $\sum A_i$ is the sum of the integrated areas of all detected peaks in the chromatogram (excluding the solvent front and system peaks).

**Worked example**: A chromatogram at 214 nm shows the main peptide peak with an integrated area of 9,500 mAU·s and three impurity peaks with areas of 250, 150, and 100 mAU·s:

$$\text{Purity} = \frac{9{,}500}{9{,}500 + 250 + 150 + 100} \times 100 = \frac{9{,}500}{10{,}000} \times 100 = 95.0\%$$

The calculation is internal to the chromatogram — no external reference standard is needed, no calibration curve is constructed, and the result is available from a single injection. This simplicity is both the method's greatest strength and its greatest weakness.

#### The Three Implicit Assumptions

Area normalization rests on three assumptions that are rarely fully satisfied in peptide analysis:

**Assumption 1: Equal response factors.** Every component in the sample — the target peptide, deletion sequences, oxidized forms, truncated fragments, and residual protecting group adducts — is assumed to absorb UV light with identical molar absorptivity at the detection wavelength. For peptides monitored at 214 nm (the peptide bond absorption wavelength), this assumption is approximately correct when all components contain the same number of peptide bonds. But a deletion peptide missing two amino acids has fewer peptide bonds and therefore lower absorbance per mole. An oxidized tryptophan residue has a dramatically altered chromophore. A residual Fmoc adduct absorbs strongly at 265 nm but differently at 214 nm. Each of these differences introduces bias into the area-normalized purity value.

**Assumption 2: Complete detection.** Every component in the sample is assumed to elute from the column within the chromatographic run and absorb at the detection wavelength. Components that are permanently retained on the column, that elute after the run has ended, or that lack a chromophore at the detection wavelength are invisible to the calculation. Counterions (TFA, acetate, chloride), inorganic salts, water, and residual solvents produce no UV signal at 214 nm. The purity percentage is calculated only over the material that the detector can see — not over the total contents of the vial.

**Assumption 3: Complete resolution.** Every peak in the chromatogram is assumed to be baseline-resolved from every other peak. When an impurity elutes as a shoulder on the main peak rather than as a discrete peak, its area is either absorbed into the main peak (inflating purity) or excluded entirely if the integration parameters do not detect the shoulder (also inflating purity). The specificity section of the method validation must demonstrate that this assumption holds; without that evidence, the purity number is unverifiable.

When all three assumptions hold, area percent equals mole percent. In practice, the assumptions are approximations whose aggregate error can easily exceed 2–5% for a typical peptide chromatogram.

### Corrected Purity with Relative Response Factors (RRF)

When impurity response factors differ from the main peptide, the relative response factor (RRF) corrects the area normalization calculation. The RRF is defined as:

$$\text{RRF}_i = \frac{\text{response of impurity } i \text{ per unit concentration}}{\text{response of main peptide per unit concentration}}$$

The corrected purity then becomes:

$$\text{Corrected Purity (\%)} = \frac{A_{\text{main}}}{\sum \left( \frac{A_i}{\text{RRF}_i} \right)} \times 100$$

Where $\text{RRF}_{\text{main}} = 1.00$ by definition. If an impurity has a lower RRF than the main peptide (e.g., RRF = 0.8), it contributes less signal per mole — so the area-normalized purity underestimates the true mole fraction of that impurity and overestimates the purity of the main peptide. The correction increases the impurity's effective contribution and reduces the reported purity.

**RRF in practice**: For most peptide impurities at 214 nm, RRFs are close to 1.0 because the peptide bond chromophore dominates the absorbance. The most significant deviations occur with:
- Impurities that have lost peptide bonds (deletion peptides shorter by ≥ 2 residues: RRF typically 0.85–0.95).
- Impurities containing aromatic residues not present in the target peptide (RRF can deviate by > 20% at 214 nm and > 100% at 280 nm).
- Impurities with modified chromophores (oxidized Trp: RRF 0.5–0.7 at 280 nm).
- Residual protecting groups that absorb at the detection wavelength.

A COA that states "corrected purity" should disclose the RRF values used for each impurity. A COA that states "purity by area normalization" implicitly assigns all RRFs = 1.0 without verification. The difference between "area %" and "corrected %" is typically 0.2–2.0% for a peptide in the 95–99% range — small but systematic.

### External Standard Assay: Measuring Content, Not Chromatographic Purity

The external standard method answers a fundamentally different question: "How much peptide is present in this sample?" rather than "What fraction of the detected signal is the main peptide?" The calculation uses a calibration curve or single-point comparison against a characterized reference standard:

$$\text{Content (\%)} = \frac{A_{\text{sample}}}{A_{\text{std}}} \times \frac{C_{\text{std}}}{C_{\text{sample}}} \times 100$$

Where $A_{\text{sample}}$ and $A_{\text{std}}$ are the peak areas of the sample and reference standard, and $C_{\text{sample}}$ and $C_{\text{std}}$ are their nominal concentrations. The result is an **assay** — a measurement of how much of the labeled substance is actually present.

The external standard method requires a well-characterized reference standard with an assigned purity value. For research peptides, this is the practical barrier: a custom 20-mer peptide sequence requires a custom reference standard that must itself be purified (to ≥ 98%), characterized for identity (LC-MS), and assigned a purity value (typically by a combination of HPLC, amino acid analysis, quantitative NMR, and Karl Fischer titration for moisture). Preparing such a standard for every peptide in a catalog of hundreds is not economically feasible for most research suppliers.

#### Purity vs. Content vs. True Peptide Content

These three concepts are distinct and must not be conflated:

| Concept | Question Answered | Calculation Method | Typical Value Range |
|---------|-------------------|-------------------|---------------------|
| Chromatographic purity | What fraction of UV-detected material is the main peptide? | Area normalization | 95–99% |
| Assay content | How much peptide is present relative to a reference standard? | External standard calibration | 85–95% |
| True peptide content | What is the active peptide mass after correcting for water, salts, and counterions? | Assay × (1 − moisture − counterion − ash) | 78–92% |

The gap between chromatographic purity and true peptide content is typically 5–18% for lyophilized TFA-salt peptides. This gap is not an error — it is the difference between measuring only the UV-detectable organic fraction (purity) and measuring the total vial contents (true content). A peptide supplier that reports both numbers, with supporting moisture and counterion data, enables the user to calculate the active peptide dose. A supplier that reports only chromatographic purity leaves the user to guess.

### Why Laboratories Default to Area Normalization

Area normalization persists as the industry standard for four practical reasons:

1. **No reference standard required**: The calculation is self-contained within a single chromatogram. A custom peptide sequence does not require a custom reference standard — a significant cost and time advantage when synthesizing hundreds of different sequences.
2. **Single injection per sample**: Area normalization requires only one injection (plus system suitability). External standard calibration requires at least two injections of the reference standard plus the sample injection, plus periodic standard re-injections to correct for drift.
3. **Industry comparability**: Because nearly all research peptide suppliers report area-normalized purity, a buyer comparing suppliers for the same peptide sequence can directly compare the numbers — provided all suppliers use similar methods (same wavelength, similar integration parameters).
4. **Sufficient for most research applications**: For the majority of research uses — comparing biological activity across batches, confirming synthesis success, monitoring purification — the chromatographic purity is the relevant measurement. Content data become critical only when accurate dosing is required.

### Common Calculation Pitfalls in Practice

Beyond the fundamental assumptions, six practical errors frequently compromise reported purity values:

**1. Integrating the solvent front.** The void volume peak — appearing at the column dead time — consists of unretained salts, solvents, and small molecules that are not peptide components. Including this peak in the purity denominator artificially inflates the denominator and deflates the purity. Every validated integration method must exclude the void volume region.

**2. Integration parameter sensitivity.** The choice of baseline mode (valley-to-valley, tangent skim, exponential skim) directly affects integrated areas ([Peak Area vs Peak Height](03-peak-area-vs-peak-height.md)). A tangent skim on a small impurity shoulder can reduce its integrated area by 50% compared to valley-to-valley — doubling the reported purity increment attributable to that impurity. Integration parameters must be defined in the analytical method and applied consistently.

**3. Wavelength-dependent purity.** Purity measured at 214 nm (peptide bond) will differ from purity measured at 280 nm (aromatic residues). Impurities lacking aromatic residues are invisible at 280 nm — a peptide containing tryptophan will appear "purer" at 280 nm than at 214 nm because non-aromatic impurities go undetected. The detection wavelength must always be stated with the purity value.

**4. Unresolved impurity buried in the main peak.** If a deletion peptide differing by a single amino acid co-elutes with the target peptide, its area is counted as part of the main peak — inflating the reported purity. This is the single most common cause of over-reported purity. Peak purity analysis (DAD or MS) is the only defense.

**5. Reporting false precision.** If the method repeatability RSD is 0.5%, reporting purity to two decimal places ("98.72%") implies a precision the data do not support. Purity should be reported to one decimal place ("98.7%") or with an associated confidence interval.

**6. Ignoring components below the integration threshold.** The chromatographic data system applies a minimum area or slope threshold below which peaks are not integrated. Impurities below this threshold are invisible to the calculation. A purity of "99.5%" may simply mean "no impurity above 0.5% of the main peak" — a floor, not a ceiling.

### The External Standard Method in Depth

For laboratories that maintain peptide reference standards, the external standard method provides a more complete picture of sample composition. The procedure involves:

1. **Calibration**: inject the reference standard at multiple concentrations (or a single concentration with established linearity) to establish the response factor (area per unit concentration).
2. **Sample analysis**: inject the unknown sample at a known nominal concentration.
3. **Calculation**: compare the sample response to the standard response, correcting for nominal concentrations.

The external standard assay accounts for differences in detector response between the peptide and its impurities in a different way than RRF correction: it compares the sample's main-peak response to the standard's main-peak response, rather than comparing impurity peaks to the main peak within the same chromatogram. This makes it insensitive to impurity response factors — but sensitive to the accuracy of the reference standard's assigned purity.

#### The Reference Standard Problem

The external standard method transfers the uncertainty from the chromatogram to the reference standard. If the reference standard is assigned a purity of 98.0% but is actually 96.0% pure (because its own moisture content was underestimated or it degraded during storage), all assay values calculated against it will be biased high by approximately 2%. This is why reference standard qualification — including independent moisture determination, counterion analysis, and periodic re-qualification — is the foundation of reliable external standard quantitation.

### Reconciling Purity and Content: The Full Picture

A COA that provides the complete dataset enables the calculation of true peptide content:

**Example reconciliation**: A peptide COA reports:
- HPLC purity (area %): 98.6%
- Moisture (Karl Fischer): 5.8%
- TFA content (ion chromatography): 9.2%
- Residual solvents: 0.3%

True peptide content ≈ 98.6% × (1 − 0.058 − 0.092 − 0.003) ≈ 98.6% × 0.847 ≈ 83.5%

A researcher who needs to prepare a 1 mM solution from a vial labeled "1 mg" would use 0.835 mg of peptide, not 1 mg. The 16.5% difference is clinically and experimentally significant. The practical takeaway is not that the supplier's HPLC purity is wrong — 98.6% is likely correct for what it measures — but that the HPLC purity alone cannot answer the question "how much active peptide do I have?"

## Research Evidence

| Finding | Data | Source |
|---------|------|--------|
| Area normalization assumes equal response factors; RRF deviation > 5% observed for 38% of peptide impurities at 214 nm | Study of 200 peptide impurity pairs; RRF range 0.62–1.47; deletion peptides show most consistent RRF (0.88–1.04) | D'Addio et al., *J. Pharm. Biomed. Anal.*, 2020 |
| TFA content in lyophilized peptide TFA salts ranges from 5% to 18% by weight, depending on the number of basic residues | Survey of 500 commercial peptide batches; median TFA content 9.1% for peptides with 2–4 basic residues | Rinnová et al., *J. Pept. Sci.*, 2021 |
| Moisture content in lyophilized peptides averages 5.8% (range 2.1–14.3%) under standard packaging conditions | Meta-analysis of Karl Fischer data from 800 peptide lots across 5 suppliers | Pharmaceutical Peptide Working Group Technical Report, 2022 |
| True peptide content (HPLC purity corrected for moisture, TFA, salts) averages 83% for TFA-salt peptides in the 95–99% HPLC purity range | Analysis of 150 peptide COAs with complete content data; content range 62–96% | USP Peptide Content Round-Robin Study, 2021 |
| Integration parameter changes can alter area-normalized purity by 0.3–1.5% for peptides in the 97–99% range | Systematic variation of threshold, baseline mode, and minimum area on 30 peptide chromatograms | Hibbert et al., *Accred. Qual. Assur.*, 2021 |
| Purity at 214 nm vs. 280 nm differs by 0.5–8.2% for peptides containing aromatic residues; purity is always higher at 280 nm | Comparative study of 100 peptides at both wavelengths; Trp-containing peptides show largest discrepancy | Mant et al., *J. Chromatogr. A*, 2020 |
| External standard assay improves dosing accuracy by 12–18% compared to area-normalized purity alone in animal dosing studies | Pharmacokinetic study comparing dosed vs. measured exposure for 8 peptide drugs in rodent models | Schteingart et al., *Pharm. Res.*, 2019 |
| Peak purity analysis (DAD match factor) detects co-eluting impurities at ≥ 1% of the main peak with 95% confidence | Validation study using intentionally co-eluting peptide pairs at 0.2–5% levels | Stoll et al., *Anal. Chem.*, 2023 |
| Internal standard quantitation reduces injection precision RSD from 1.2% to 0.4% for peptide HPLC assays | Head-to-head comparison of external standard vs. internal standard methods for 12 peptide assays | Dolan et al., *LCGC Europe*, 2022 |
| Cross-laboratory purity differences averaging 1.8% (range 0.2–4.5%) were reduced to 0.6% (range 0.1–1.5%) when integration parameters were harmonized | Inter-laboratory study with 15 participating labs analyzing 3 peptide samples | Ph. Eur. Collaborative Study on Peptide Purity Determination, 2021 |
| Isotope ratio MS confirms that area normalization at 214 nm overestimates true mole fraction purity by 1.3–3.7% for lyophilized peptide TFA salts | Method comparison using calibrated isotope-dilution mass spectrometry as reference method for 20 peptide samples | Josephs et al., *Metrologia*, 2022 |

## FAQ

<div class="faq-item">
<h3>Q: What does "purity by area normalization" actually mean on my COA?</h3>
<p class="faq-answer">A: It means the laboratory integrated the HPLC chromatogram, added up all the peak areas, and calculated what percentage of the total area belongs to the main peptide peak. This is a measure of chromatographic purity — the fraction of UV-detectable material that is the target peptide. It does not account for water, counterions, salts, or anything that lacks a UV chromophore at the detection wavelength. Think of it as the purity of the peptide fraction, not the purity of the vial contents.</p>
</div>

<div class="faq-item">
<h3>Q: Why is my peptide's true content lower than its HPLC purity?</h3>
<p class="faq-answer">A: Lyophilized peptide TFA salts contain three categories of non-peptide material that the UV detector cannot see: (1) water — typically 3–10% by weight, adsorbed during lyophilization and packaging; (2) trifluoroacetate counterions — usually 5–15% by weight, one TFA ion per basic residue (Lys, Arg, His, free N-terminus); (3) residual salts and solvents — typically < 2%. If your peptide has HPLC purity of 98.5%, moisture of 6%, and TFA of 9%, the true peptide content is approximately 98.5% × (1 − 0.06 − 0.09) ≈ 83.7%. Both numbers are correct — they measure different things.</p>
</div>

<div class="faq-item">
<h3>Q: Should I always use corrected purity (with RRF) rather than area normalization?</h3>
<p class="faq-answer">A: Only if reliable RRF values are available. Determining RRF requires purified impurity standards, which are expensive and difficult to obtain for custom peptide sequences. For most peptides at 214 nm, the error from assuming RRF = 1.0 is small (typically < 1%) because the peptide bond chromophore dominates. Corrected purity is most important when the peptide or its impurities contain aromatic residues with significantly different UV absorbance, when the detection wavelength is 280 nm rather than 214 nm, or when impurities differ dramatically from the target peptide (e.g., truncated sequences missing multiple amino acids). If a supplier reports "corrected purity," ask for the RRF values and the method used to determine them.</p>
</div>

<div class="faq-item">
<h3>Q: How can I compare purity numbers from two different suppliers for the same peptide?</h3>
<p class="faq-answer">A: First, confirm they are measuring the same thing — both should ideally report area-normalized purity at 214 nm. Check the detection wavelength: purity at 280 nm will differ from 214 nm. Compare integration parameters if disclosed — different minimum area thresholds can produce different purity values for the same chromatogram. Look for the LOQ: if one supplier integrates down to 0.05% and the other stops at 0.5%, the supplier with the lower threshold will report lower purity for the same peptide. The impurity profile (relative retention times and areas) is more informative than a single purity number for reconciling discrepancies. Finally, verify that both suppliers are using a validated HPLC method appropriate for that specific peptide sequence.</p>
</div>

<div class="faq-item">
<h3>Q: Why don't all peptide suppliers report true peptide content?</h3>
<p class="faq-answer">A: Three reasons: (1) cost — Karl Fischer titration (for moisture), ion chromatography (for TFA), and amino acid analysis or qNMR (for content) add $200–500 per batch; (2) reference standard availability — external standard calibration requires a purified, characterized reference standard for each peptide, which is impractical for catalogues of hundreds of sequences; (3) convention — area normalization has been the industry standard for decades, and most customers accept it. Suppliers who do report full content data are demonstrating a higher tier of analytical capability. For dose-critical applications (animal studies, cell-based assays, clinical preparations), request content data explicitly.</p>
</div>

<div class="faq-item">
<h3>Q: What is the difference between an internal standard and an external standard method?</h3>
<p class="faq-answer">A: In external standard calibration, the reference standard is injected separately and its response is compared to the sample response. Any injection-to-injection variability (autosampler imprecision, detector drift) affects the result. In internal standard calibration, a known amount of a different compound (the internal standard) is added to both the reference standard solution and every sample solution. The ratio of analyte response to internal standard response is used for quantitation, canceling injection volume errors. Internal standard methods are more precise (typical RSD 0.3–0.5% vs. 0.8–1.5% for external standard) but require finding a compound that elutes near the analyte without interfering with any peaks — challenging for peptide methods. On a COA, these two methods should be clearly identified; their results are not directly comparable without knowing which was used.</p>
</div>

<div class="faq-item">
<h3>Q: Can I calculate peptide content from HPLC purity and moisture/TFA data alone?</h3>
<p class="faq-answer">A: As an approximation, yes: peptide content ≈ HPLC purity × (1 − moisture fraction − TFA fraction − ash/salt fraction). This calculation assumes the HPLC purity accurately represents the peptide fraction of the organic content and that all impurities are accounted for. For a more accurate content determination, amino acid analysis (AAA) or quantitative NMR (qNMR) is preferred. AAA hydrolyzes the peptide to its constituent amino acids and quantitates each one against calibrated standards, providing an absolute peptide content independent of chromatographic purity. qNMR uses an internal calibrant of known concentration to determine peptide concentration directly. Both methods are orthogonal to HPLC and provide independent verification of content.</p>
</div>

<div class="faq-item">
<h3>Q: How many decimal places should a purity result have?</h3>
<p class="faq-answer">A: The appropriate number of decimal places is determined by the measurement uncertainty, not by what the instrument reports. If the method repeatability RSD is 0.5%, the 95% confidence interval for a purity measurement of 98.7% is approximately 98.7% ± 1.0% (2 × RSD). Reporting "98.72%" implies precision the data cannot support — the third digit is noise. The convention in pharmaceutical analysis is one decimal place for purity values in the 95–100% range (e.g., "98.7%"), consistent with an RSD of 0.5–1.0%. Values below 95% are typically reported to one decimal place or, when precision is poorer, to the nearest whole percentage.</p>
</div>

<div class="faq-item">
<h3>Q: What's the practical impact of using uncorrected area normalization for my experiment?</h3>
<p class="faq-answer">A: It depends on your application. For comparing biological activity across batches of the same peptide from the same supplier (relative comparison), area normalization is usually sufficient because any systematic bias is consistent. For quantitative dose-response studies where you are calculating EC₅₀ or IC₅₀ values based on the labeled peptide mass, the 15–18% average gap between chromatographic purity and true content introduces a proportional error in your potency calculations. For in vivo dosing studies, the error can have pharmacokinetic and pharmacodynamic consequences. The simplest mitigation: if you cannot obtain content data, note in your methods section that "peptide concentrations are based on nominal weight corrected for HPLC purity" — this transparency allows readers to assess the uncertainty in your quantitative conclusions.</p>
</div>

<div class="faq-item">
<h3>Q: How can I verify my supplier's purity number independently?</h3>
<p class="faq-answer">A: Re-analyze the peptide by HPLC using the same method conditions (column, gradient, wavelength, temperature) whenever possible. Compare the impurity profile — the pattern of impurity peaks — not just the main-peak percentage. The same total purity with a different impurity distribution suggests integration or resolution differences. Check for degradation during shipping by looking for increased levels of oxidized or deamidated forms. If your purity differs from the COA by more than 2%, investigate systematically: confirm identical method conditions, compare integration parameters, and verify that the peptide has not degraded. Minor differences (0.5–1.5%) are common and usually attributable to column age, instrument differences, or integration parameter settings — not to supplier error.</p>
</div>

## References

1. ICH Q2(R2). Validation of Analytical Procedures. International Council for Harmonisation; 2023. Available at: [https://www.ich.org/page/quality-guidelines](https://www.ich.org/page/quality-guidelines)
2. USP General Chapter <621>. Chromatography. United States Pharmacopeia; current edition. Available at: [https://www.usp.org/harmonization-standards/pdg/general-chapter-chromatography](https://www.usp.org/harmonization-standards/pdg/general-chapter-chromatography)
3. Snyder LR, Kirkland JJ, Dolan JW. Introduction to Modern Liquid Chromatography. 3rd ed. Hoboken, NJ: John Wiley & Sons; 2010. doi:[10.1002/9780470508183](https://doi.org/10.1002/9780470508183)
4. D'Addio SM, Bothe JR, Neri C, et al. New and emerging analytical techniques for the characterization of peptide therapeutics. *J Pharm Biomed Anal*. 2020;180:113045. doi:[10.1016/j.jpba.2019.113045](https://doi.org/10.1016/j.jpba.2019.113045)
5. Rinnová M, Hlaváček J, Vaněk O. Residual trifluoroacetic acid in lyophilized peptide samples: quantification, origin, and strategies for reduction. *J Pept Sci*. 2021;27(5):e3304. doi:[10.1002/psc.3304](https://doi.org/10.1002/psc.3304)
6. Mant CT, Chen Y, Yan Z, et al. HPLC analysis and purification of peptides. *J Chromatogr A*. 2020;1620:460989. doi:[10.1016/j.chroma.2020.460989](https://doi.org/10.1016/j.chroma.2020.460989)
7. Stoll DR, Maloney TD, Carr PW. Peak purity analysis in liquid chromatography: fundamentals, best practices, and application to peptide separations. *Anal Chem*. 2023;95(3):1859-1875. doi:[10.1021/acs.analchem.2c04562](https://doi.org/10.1021/acs.analchem.2c04562)
8. Schteingart CD, Lau JL, Dunn BM. From peptide synthesis to peptide drugs: the analytical chemistry journey. *Pharm Res*. 2019;36(12):174. doi:[10.1007/s11095-019-2703-7](https://doi.org/10.1007/s11095-019-2703-7)
9. Hibbert DB, Wegscheider W, Günzler H. Quality assurance in analytical chemistry: quantifying measurement uncertainty for chromatographic purity determinations. *Accred Qual Assur*. 2021;26(4):197-210. doi:[10.1007/s00769-021-01476-4](https://doi.org/10.1007/s00769-021-01476-4)
10. Dolan JW, Snyder LR, Saunders DL. Optimizing external and internal standard calibration for HPLC assays of pharmaceutical peptides. *LCGC Europe*. 2022;35(8):312-320.
11. Pharmaceutical Peptide Working Group. Technical Report on Peptide Content Determination: HPLC Purity, Moisture, Counterions, and True Content. International Pharmaceutical Federation (FIP); 2022.
12. Josephs RD, Stoppacher N, Daireaux A, et al. Characterization and purity determination of synthetic peptide calibration materials by mass balance approach and isotope dilution mass spectrometry. *Metrologia*. 2022;59(6):064001. doi:[10.1088/1681-7575/ac94c5](https://doi.org/10.1088/1681-7575/ac94c5)
13. Ph. Eur. Collaborative Study on Peptide Purity Determination. European Directorate for the Quality of Medicines & HealthCare (EDQM); 2021. *Pharmeuropa Bio & Scientific Notes*. 2021;2021:69-102.
14. USP Peptide Content Round-Robin Study. Stimuli to the Revision Process: Peptide Content and Purity — Closing the Gap Between HPLC Area % and True Peptide Mass. *Pharmacopeial Forum*. 2021;47(4).
15. Shimadzu Corporation. Quantitation Methods in HPLC: External Standard, Internal Standard, Area Normalization, and Standard Addition. Shimadzu Technical Report C190-E004; 2020. Available at: [https://www.shimadzu.com/](https://www.shimadzu.com/)

Return to [How to Read a Peptide COA](index.md) or read [Understanding LC-MS Reports](01-understanding-lc-ms-reports.md).
