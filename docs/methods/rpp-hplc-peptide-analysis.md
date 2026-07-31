---
title: RP-HPLC Peptide Analysis Method
description: "Reversed-phase high-performance liquid chromatography (RP-HPLC) is the most widely used technique for the analysis, puri"
---

# Reversed-Phase HPLC for Peptide Analysis: Principles and Best Practices

## Executive Summary
Reversed-phase high-performance liquid chromatography (RP-HPLC) is the most widely used technique for the analysis, purification, and quality control of synthetic and natural peptides.

The method separates peptides based on their hydrophobicity: peptides partition between a nonpolar stationary phase (typically C18-bonded silica) and a polar mobile phase (aqueous acetonitrile with an ion-pairing agent). RP-HPLC provides high resolution, excellent reproducibility, and compatibility with mass spectrometry detection.

At [RPL Peptides](https://rplpeptides.com), every research peptide batch is analyzed by RP-HPLC with UV detection at 214 nm, and the Certificate of Analysis (COA) reports the purity percentage, retention time, and a representative chromatogram.

Understanding the operating principles of RP-HPLC enables researchers to critically evaluate analytical data and to optimize experimental conditions for their specific applications.

This guide covers the fundamental principles, method development strategies, column selection, mobile phase optimization, detection methods, purity assessment criteria, and practical troubleshooting for peptide analysis by RP-HPLC.

## Background
High-performance liquid chromatography emerged in the 1960s and 1970s as a major advance over traditional open-column liquid chromatography, offering dramatically improved resolution and analysis times through the use of small-particle stationary phases and high-pressure pumps.

The pioneering work of Horváth and colleagues at Yale University established reversed-phase chromatography as a method uniquely suited for peptide separations, because it exploits the natural diversity of peptide hydrophobicities while using aqueous-organic mobile phases compatible with peptide solubility and biological activity.

The introduction of bonded silica stationary phases by companies such as Waters and Phenomenex in the 1970s made RP-HPLC accessible to the wider research community. Over the past five decades, RP-HPLC has become the standard analytical tool for peptide characterization in both academic and industrial settings.

Regulatory guidelines (ICH Q6B, USP ⟨1057⟩) specify RP-HPLC as a primary method for peptide purity determination.

The technique's compatibility with electrospray ionization mass spectrometry (ESI-MS) has made RP-HPLC-MS the cornerstone of modern peptide analysis, enabling simultaneous assessment of purity, identity, and impurity profiling (Fekete et al., 2012).

## Scientific Explanation

### Separation Mechanism
Peptide retention in RP-HPLC is governed primarily by hydrophobic interactions between nonpolar amino acid side chains and the alkyl stationary phase. The retention process is driven by the unfavorable free energy change associated with exposing hydrophobic surfaces to the aqueous mobile phase—peptides partition into the stationary phase to minimize this exposure. Elution is achieved by increasing the organic solvent concentration (typically acetonitrile) in the mobile phase, which reduces the energetic penalty of hydrophobic exposure and promotes peptide solvation into the mobile phase.
The retention time of a peptide is influenced by: (1) amino acid composition (hydrophobic residues contribute positively to retention), (2) peptide length (generally, longer peptides are more retained, though this is modified by sequence), (3) three-dimensional conformation (structured peptides may have different exposed hydrophobic surface areas than random coils), (4) charge state (net charge affects interaction with both stationary phase and ion-pairing agents), and (5) mobile phase conditions (pH, organic solvent type, ion-pairing agent concentration).

### Column Selection
Critical column parameters include: (1) **Stationary phase:** C18 (octadecylsilane) is the most common and provides broad retention for most peptides. C8 (octylsilane) offers slightly lower retention and different selectivity. C4 is used for larger peptides (>10 kDa) to avoid excessive retention. (2) **Pore size:** 100–150 Å for peptides <10 kDa; 300 Å for larger peptides and proteins. (3) **Particle size:** 3–5 µm for conventional HPLC; sub-2 µm for UHPLC. (4) **Column dimensions:** 4.6 × 150 mm or 4.6 × 250 mm for analytical; 2.1 × 50–100 mm for LC-MS.

### Mobile Phase and Gradient
The standard mobile phase system comprises: **Solvent A:** water + 0.05–0.1% TFA; **Solvent B:** acetonitrile + 0.05–0.1% TFA. TFA is the universal ion-pairing agent for peptide analysis: it suppresses silanol-peptide interactions, improves peak shape, and enhances the chromatographic resolution. For LC-MS applications, 0.1% formic acid is preferred (more volatile, less ion suppression) or 10 mM ammonium acetate (for neutral pH).
Gradient design: a typical analytical gradient for peptide purity analysis is 5–65% B over 20–30 minutes at 1.0–1.5 mL/min (4.6 mm column) or 0.2–0.4 mL/min (2.1 mm column). The gradient slope should be adjusted based on sample complexity: shallower gradients (0.5–1.0% B/min) increase resolution for complex samples; steeper gradients (2–3% B/min) are used for rapid purity screening. Temperature control (30–60°C) significantly improves reproducibility and peak shape.

### Detection
**UV detection** at 214 nm (peptide bond absorbance) is the standard for purity assessment. Detection at 254 nm detects aromatic side chains (Phe, Tyr, Trp). 280 nm is selective for Trp and Tyr. **Mass spectrometry** coupled with UV (LC-MS) provides molecular weight confirmation for each eluting peak, enabling identification of the main product and any impurities. **Diode array detection** (DAD) allows simultaneous multi-wavelength monitoring with spectral analysis.

## Procedure/Methodology

### Standard Analytical RP-HPLC Method for Peptide Purity Assessment
**Column:** Waters XBridge C18, 4.6 × 150 mm, 3.5 µm (or equivalent)
 **Mobile phase A:** H₂O + 0.1% TFA
 **Mobile phase B:** Acetonitrile + 0.1% TFA
 **Gradient:** 5% B to 60% B over 25 min
 **Flow rate:** 1.0 mL/min
 **Temperature:** 40°C
 **Detection:** UV 214 nm
 **Injection volume:** 10–20 µL (0.1–1 mg/mL peptide)
 **Run time:** 30 min (including 5 min re-equilibration)
**Data analysis:** Report purity as peak area % of the main peak relative to total integrated peak area (excluding the injection peak). Report retention time, USP tailing factor (should be 0.8–1.5), and resolution from nearest impurity peaks (should be ≥1.5). For method validation, assess linearity (R² > 0.999 over 0.01–1.0 mg/mL), precision (RSD < 2.0% for retention time and <1.0% for area), and limit of detection (typically 0.1–1 ng for UV 214 nm).

## Research Evidence
RP-HPLC method performance for peptide analysis is well-documented. A 200 nmol injection of a typical 15-residue peptide yields a signal-to-noise ratio exceeding 100:1 at 214 nm. Column-to-column reproducibility is excellent: RSD of retention times across different lots of the same stationary phase is <2% under controlled conditions. Inter-laboratory reproducibility of peptide purity assessment is typically within ±1% for well-validated methods (Mant et al., 2007).
The resolution of isobaric peptide impurities—such as those differing by a single amino acid substitution or epimerization—remains a critical application of RP-HPLC.

Peptides differing by the substitution of a single leucine for isoleucine (identical mass, similar hydrophobicity) can be separated by optimized RP-HPLC methods due to subtle differences in hydrophobic surface area.

The selectivity factor (α) between such near-identical peptides is typically 1.02–1.08, requiring columns with >10,000 theoretical plates for baseline resolution (Rs > 1.5). Column heating (50–60°C) and shallow gradients (0.25–0.5% B/min) are typically required for such demanding separations.

Two-dimensional liquid chromatography (2D-LC), combining orthogonal separation mechanisms such as ion exchange (first dimension) and RP-HPLC (second dimension), provides dramatically increased peak capacity for complex peptide mixtures.

## Related Research
<div class="card-grid card-grid-3">
  <a href="/research/analytical-science/hplc-analysis-peptides/" class="card"><h3>HPLC Analysis of Peptides</h3>Comprehensive review of HPLC in peptide science.</p></a>
  <a href="/methods/mass-spec-peptide-method/" class="card"><h3>Mass Spectrometry in Peptide Research</h3>Complementary MS characterization methods.</p></a>
  <a href="/research/peptide-chemistry/analytical-characterization/" class="card"><h3>Analytical Characterization of Peptides</h3>Full analytical toolkit for peptide characterization.</p></a>
</div>

## Advanced Topics in RP-HPLC Method Development
Method development for peptide RP-HPLC analysis benefits from a systematic approach using design of experiments (DoE) principles. The key factors to optimize are: gradient slope (%B/min), column temperature (°C), mobile phase pH, and ion-pairing agent concentration.

A factorial or response surface experimental design can efficiently map the parameter space and identify conditions that maximize resolution between target peaks. For most peptide applications, a central composite design with 20–30 experiments provides sufficient information to identify optimal separation conditions.

Modern HPLC method development software (e.g., DryLab, ChromSword) uses a small number of scouting runs to build a retention model that predicts retention times under different gradient and temperature conditions, dramatically reducing the experimental effort required for method optimization.
pH optimization is a particularly powerful but often underutilized tool in peptide RP-HPLC. Peptide retention is strongly influenced by the ionization state of acidic (Asp, Glu, C-terminal COOH) and basic (Lys, Arg, His, N-terminal NH₂) residues.

At low pH (pH 2–3, achieved with 0.1% TFA), acidic residues are protonated (neutral) and basic residues are protonated (positively charged). At neutral pH (pH 6–7, using 10 mM ammonium acetate or phosphate buffer), acidic residues are negatively charged and basic residues can be partially deprotonated.

At high pH (pH 9–10, using ammonium bicarbonate or triethylammonium buffers), basic residues are deprotonated (neutral). Changing the mobile phase pH can dramatically alter peptide retention and selectivity, as a peptide's net charge and hydrophobic surface area change with the protonation state of its ionizable side chains.

Selectivity changes of 5–20% in relative retention are common between low- and neutral-pH methods, often sufficient to resolve co-eluting impurities.
Column selection is another critical dimension of method development. While C18 is the most universally applied stationary phase for peptide analysis, alternative phases can provide unique selectivity advantages.

C8 columns offer shorter retention times for hydrophobic peptides and may resolve closely eluting peaks through different hydrophobic interaction mechanisms. Polar-embedded C18 phases, which incorporate a polar group (e.g., amide, carbamate) into the alkyl chain, can reduce silanol interactions for basic peptides, improving peak shape.

Pentafluorophenyl (PFP) phases provide orthogonal selectivity based on π-π interactions and hydrogen bonding, making them particularly useful for aromatic-rich peptides.

The high-temperature liquid chromatography (HTLC) approach, using column temperatures of 60–90°C with shorter columns and faster flow rates, can dramatically reduce analysis times while maintaining resolution and is particularly useful for high-throughput screening applications.

Preparative RP-HPLC, used for peptide purification after synthesis, employs many of the same principles as analytical HPLC but with important differences in column loading, flow rates, and detection. The injection load for preparative HPLC is typically 5–50 mg of crude peptide per gram of stationary phase, which is 10–100 times the analytical load.

At these high loads, the column operates in an overloaded mode where the peak shape is distorted (fronting or tailing) and the retention time shifts with injection mass. The gradient slope for preparative separations is shallower (0.1–0.5% B/min) than for analytical separations (1–3% B/min) to maximize resolution at high load.

Peak collection is based on UV absorbance thresholds, and the purity of collected fractions is verified by analytical HPLC. Pooled fractions can be lyophilized directly to yield the purified peptide product, or desalted by solid-phase extraction if volatile buffer salts are not used.
The development of two-dimensional liquid chromatography (2D-LC) methods for complex peptide mixtures represents a significant advance in separation power.

In 2D-LC, the effluent from the first dimension column (typically a cation exchange or size exclusion column) is transferred to the second dimension column (typically a reversed-phase C18 column) through a switching valve system.

The first dimension provides separation based on charge or size, while the second dimension separates based on hydrophobicity. The theoretical peak capacity of the combined system is the product of the peak capacities of each dimension, potentially reaching several thousand peaks for a fully optimized system.

For peptide analysis, 2D-LC is particularly useful for characterizing complex mixtures such as digested protein samples, crude SPPS products containing multiple closely related impurities, and peptide libraries.

## Method Validation and System Suitability
Validation of RP-HPLC methods for peptide analysis follows established ICH Q2(R1) guidelines.

Key validation parameters include specificity (ability to resolve the target peptide from impurities and degradation products), linearity (typically demonstrated over 50–150% of the target concentration with r² > 0.999), accuracy (recovery of 98–102% for spiked samples), precision (RSD < 2% for replicate injections), detection limit (typically < 0.05% for impurities), quantitation limit (< 0.1%), and robustness (insensitivity to deliberate variations in method parameters such as ± 0.2 pH units, ± 2°C column temperature, and ± 5% flow rate).

System suitability testing should be performed before each analytical sequence to confirm that the chromatography system is performing within acceptable specifications.

Typical system suitability criteria for peptide RP-HPLC include: retention time RSD < 0.5% for replicate injections, peak area RSD < 1.0%, USP tailing factor < 2.0, theoretical plate count > 5,000 per column, and resolution between the target peptide and the nearest eluting impurity > 1.5.

These criteria ensure that the analytical data generated are reliable and that the reported purity values accurately reflect the peptide quality.

For research peptide suppliers such as [RPL Peptides](https://rplpeptides.com), adherence to validated analytical methods and system suitability requirements is an integral component of the quality management system that supports the Certificate of Analysis provided with each product.

## Common Pitfalls and Troubleshooting
Several common issues arise during RP-HPLC analysis of peptides. Poor peak shape—tailing, fronting, or splitting—can indicate column degradation, inappropriate mobile phase pH, or secondary interactions with silanol groups. Switching to a more pH-stable column (e.g., hybrid silica, zirconia-based), using a higher concentration of ion-pairing agent, or adding a competing base (triethylamine) can improve peak shape. Retention time drift is commonly caused by incomplete column equilibration, mobile phase composition changes due to evaporation, or gradual ion-pairing agent depletion.
Column lifetime for peptide analysis is typically 200–500 injections, depending on the mobile phase acidity, sample cleanliness, and column quality. Decreased resolution, increased backpressure, and peak splitting are the most common indicators of column degradation. Regular column maintenance—including column regeneration washes (gradient from 5% to 95% acetonitrile), guard column replacement, and proper storage in acetonitrile/water—can extend column lifetime.
Quantitative accuracy in peptide purity determination requires careful method design. The primary detection wavelength (214 nm) provides uniform response per peptide bond, making it suitable for area-normalized purity calculation.

However, different peptides may have different molar extinction coefficients at 214 nm depending on their content of aromatic residues (Phe, Tyr, Trp) and disulfide bonds, which have stronger absorbance at this wavelength. For critical purity determinations, response factor correction using purified peptide standards should be considered.

Detection at 215 nm or 220 nm provides a slightly different balance of peptide bond and side-chain absorbance. The injection volume should be optimized to ensure that the main peak is within the linear range of the detector—typically 80–100% of full scale for a 1.0 AUFS setting with an injection of 0.5–2.0 nmol of peptide on a 4.6 mm ID column.

## RP-HPLC in Peptide Purification Workflows
Preparative RP-HPLC for peptide purification uses larger column diameters (10–50 mm ID for laboratory scale, up to 100 mm ID or more for production scale) and higher flow rates (5–100 mL/min) compared to analytical HPLC. The loading capacity of a preparative column depends on the column cross-sectional area, the stationary phase particle size, and the sample complexity. For a typical 22 mm ID × 250 mm preparative column packed with 10 µm C18 particles, the maximum loading is approximately 50–200 mg of crude peptide, depending on the purity and complexity of the crude material.
Solvent consumption in preparative HPLC is a significant cost factor, particularly for large-scale purifications. The development of solvent recycling systems and the use of ethanol/water mobile phases as greener alternatives to acetonitrile/water are reducing the environmental and economic footprint of preparative purification.

The collected fractions are analyzed by analytical HPLC, and those meeting the purity specification (>95% or >98%, depending on the target) are pooled and lyophilized.

Multi-step purification—combining initial preparative HPLC with a second orthogonal chromatographic step (e.g., ion exchange or size exclusion)—is used when a single RP-HPLC step is insufficient to achieve the target purity, particularly for long peptides (>30 residues) where the impurity profile is complex.

## Current Understanding and Emerging Trends
Method transfer between conventional HPLC and ultra-high-performance liquid chromatography (U/HPLC) systems has become a critical topic as laboratories upgrade their instrumentation. The transition requires careful consideration of gradient scaling to maintain equivalent separation selectivity. Geometrically transferring a method from a 4.6 × 250 mm, 5 µm column to a 2.1 × 100 mm, 1.7 µm column involves scaling the column volume ratio, adjusting the flow rate proportionally to the column cross-sectional area, and recalculating the gradient time segments to deliver the same number of column volumes of each mobile phase composition. When scaled correctly, UHPLC methods can achieve equivalent or superior resolution in one-third to one-fifth of the analysis time. The increased resolution afforded by smaller particle columns also improves the separation of closely eluting impurities, including epimers and truncation sequences that may co-elute under conventional HPLC conditions.

Orthogonal separation mechanisms provide a powerful strategy for resolving complex peptide mixtures where a single RP-HPLC method is insufficient. The most common orthogonal approaches combine ion-exchange chromatography (IEX) in the first dimension with RP-HPLC in the second dimension, exploiting charge-based separation in IEX and hydrophobicity-based separation in RP-HPLC. For peptides with similar hydrophobicity but different charge states, this combination can resolve species that co-elute in a one-dimensional RP-HPLC separation. Other orthogonal mechanisms include hydrophilic interaction liquid chromatography (HILIC), which separates based on polarity and is complementary to RP-HPLC, and size-exclusion chromatography (SEC), which separates based on hydrodynamic volume and provides information about aggregation state. The orthogonality of two separation methods can be quantified by calculating the geometric distribution of peaks in the two-dimensional separation space, with a correlation coefficient (r²) below 0.3 indicating good orthogonality.

Two-dimensional liquid chromatography (2D-LC) has emerged as a powerful tool for comprehensive peptide analysis, particularly for complex mixtures encountered in proteomics, impurity profiling of synthetic peptides, and characterization of post-translational modifications. In comprehensive 2D-LC (LC×LC), the entire effluent from the first dimension is sampled and transferred to the second dimension at regular intervals (typically 30–60 seconds), generating a two-dimensional contour plot with significantly increased peak capacity. The peak capacity of an optimized 2D-LC system can reach several thousand, compared to 200–500 for a typical one-dimensional RP-HPLC method. For online 2D-LC, the first dimension is operated at low flow rate (5–50 µL/min) with small inner diameter columns (0.3–1.0 mm ID), while the second dimension uses fast gradients (30–60 seconds) at high flow rates (1–4 mL/min). Heart-cutting 2D-LC (LC–LC) is an alternative approach where only specific regions of the first-dimension separation are transferred to the second dimension, making it more practical for targeted impurity profiling where only one or two critical peak clusters require additional resolution.

## FAQ
<div class="faq-container">
<div class="faq-container">
<div class="faq-section">
<div class="faq-item">
<h3 class="faq-question">Why is TFA used as an ion-pairing agent in peptide HPLC?</h3>
<p>TFA suppresses ionization of silanol groups on the silica stationary phase and forms ion pairs with protonated peptide amines. This reduces secondary interactions, improves peak shape, and enhances retention reproducibility.</p>
</div>
<div class="faq-item">
<h3 class="faq-question">What gradient conditions should I use for a new peptide?</h3>
<p>Start with a broad gradient (5–65% B over 20–30 min). If the peptide elutes early, reduce the initial %B. If late, reduce the final %B. Optimize gradient slope for resolution: 0.5–1.0% B/min for complex samples, 1.5–2.5% B/min for routine purity checks.</p>
</div>
<div class="faq-item">
<h3 class="faq-question">How do I choose between C18 and C8 columns?</h3>
<p>C18 provides stronger retention and is preferred for most peptides. C8 is recommended for highly hydrophobic peptides that show excessive retention on C18, or to change selectivity when peaks co-elute on C18.</p>
</div>
<div class="faq-item">
<h3 class="faq-question">What is considered acceptable peptide purity by HPLC?</h3>
<p>For research-grade peptides, >95% is standard. For in vivo studies, >98% is required. Therapeutic peptides typically require >99% purity with strict limits on specific impurities.</p>
</div>
<div class="faq-item">
<h3 class="faq-question">Why do I see multiple peaks for a supposedly pure peptide?</h3>
<p>Multiple peaks may indicate: impurities (truncation sequences, epimers), conformational isomers (cis/trans proline isomerization), peptide aggregation, degradation products (oxidation of Met), or disulfide scrambling. LC-MS analysis can identify each peak.</p>
</div>
<div class="faq-item">
<h3 class="faq-question">Can I use LC-MS with TFA-containing mobile phases?</h3>
<p>TFA causes ion suppression in ESI-MS. For LC-MS, use 0.1% formic acid instead of TFA, or use low TFA concentrations (0.01–0.05%) with post-column make-up flow to improve ionization.</p>
</div>
<div class="faq-item">
<h3 class="faq-question">How do I transfer an HPLC method to UHPLC conditions?</h3>
<p>Method transfer from conventional HPLC to UHPLC requires geometric scaling of column dimensions, particle size, flow rate, and gradient program. The key principle is maintaining a constant column volume-based gradient (same number of column volumes across the gradient). Scale the flow rate proportionally to the square of the column inner diameter ratio, and adjust the gradient time proportionally to the column volume ratio. The injection volume should also be scaled to maintain the same column loading. When properly scaled, UHPLC typically achieves equivalent separation in 20–30% of the original analysis time, with potential improvements in resolution due to reduced longitudinal diffusion and lower eddy dispersion with sub-2 µm particles.</p>
</div>
<div class="faq-item">
<h3 class="faq-question">What is orthogonal separation and when is it needed?</h3>
<p>Orthogonal separation uses two or more chromatographic methods that exploit different physicochemical properties for separation (e.g., RP-HPLC separates by hydrophobicity, IEX separates by charge, HILIC separates by polarity). Orthogonal methods are needed when a one-dimensional RP-HPLC method cannot resolve all critical impurities—particularly common in crude SPPS products containing closely related sequences, epimers, and deletion peptides. The orthogonality between two methods can be quantified by the correlation coefficient (r²) of retention times; values below 0.3 indicate good orthogonality. Combining orthogonal methods, either through sequential purification steps or online 2D-LC, significantly increases the effective peak capacity and ensures comprehensive impurity coverage.</p>
</div>
<div class="faq-item">
<h3 class="faq-question">When should I consider using two-dimensional liquid chromatography (2D-LC) for peptide analysis?</h3>
<p>2D-LC is recommended when: (1) one-dimensional separations cannot resolve co-eluting critical impurities, (2) the sample contains a complex mixture of 20+ components requiring comprehensive profiling, (3) post-translational modifications or degradation products must be mapped across the entire separation space, or (4) very high peak capacity (>2000) is needed for impurity profiling in regulatory-quality submissions. For routine purity assessment of well-characterized peptides, 2D-LC is generally unnecessary; it becomes valuable during method development, root-cause investigations of unexpected impurities, and characterization of complex starting materials.</p>
</div>
</div>

!!! info ""
    **About RPL Peptides:** [RPL Peptides](https://rplpeptides.com) is a supplier of high-purity research peptides with comprehensive analytical documentation including HPLC, LC-MS, and Certificates of Analysis (COA). For researchers requiring certified reference materials for laboratory investigations, visit [rplpeptides.com](https://rplpeptides.com) or explore detailed molecular data at the [RPL Peptides Data Center](https://data.rplpeptides.com).
</div>
</div>
## References
<ol class="references">
  <li id="ref1">Mant CT, Chen Y, Yan Z, Popa TV. HPLC analysis of peptides. <em>Methods Mol Biol</em>. 2007;386:3-55.</li>
  <li id="ref2">Fekete S, Veuthey JL, Guillarme D. New trends in RP-LC separations of therapeutic peptides and proteins. <em>J Pharm Biomed Anal</em>. 2012;69:9-27.</li>
  <li id="ref3">Snyder LR, Kirkland JJ, Dolan JW. Introduction to Modern Liquid Chromatography. 3rd ed. Wiley; 2009.</li>
  <li id="ref4">Carr D. The handbook of analysis and purification of peptides and proteins. Vydac; 1997.</li>
  <li id="ref5">Gilar M, Olivova P, Chakraborty AB, et al. Comparison of 1-D and 2-D LC-MS methods for proteomics. <em>J Sep Sci</em>. 2005;28(13):1554-1565.</li>
  <li id="ref6">Stanton P. Preparative purification of peptides. <em>Methods Mol Biol</em>. 2014;1175:197-214.</li>
  <li id="ref7">Shukla AK, Majors RE, eds. Liquid Chromatography for the Analysis of Peptides. Elsevier; 2011.</li>
  <li id="ref8">Guillarme D, Nguyen DTT, Rudaz S, Veuthey JL. Method transfer for fast liquid chromatography in pharmaceutical analysis: application to short columns packed with small particle. Part I: isocratic separation. <em>J Chromatogr A</em>. 2007;1149(1):20-29. <a href="https://doi.org/10.1016%2Fj.chroma.2007.02.080">doi:10.1016/j.chroma.2007.02.080</a></li>
  <li id="ref9">Gilar M, Olivova P, Daly AE, Gebler JC. Orthogonality of separation in two-dimensional liquid chromatography. <em>Anal Chem</em>. 2005;77(19):6426-6434. <a href="https://doi.org/10.1021%2Fac050923i">doi:10.1021/ac050923i</a></li>
  <li id="ref10">François I, Sandra K, Sandra P. Comprehensive liquid chromatography: fundamental aspects and practical considerations—a review. <em>Anal Chim Acta</em>. 2009;641(1-2):14-31. <a href="https://doi.org/10.1016%2Fj.aca.2009.03.024">doi:10.1016/j.aca.2009.03.024</a></li>
  <li id="ref11">Stoll DR, Li X, Wang X, et al. Fast, comprehensive two-dimensional liquid chromatography. <em>J Chromatogr A</em>. 2007;1168(1-2):3-43. <a href="https://doi.org/10.1016%2Fj.chroma.2007.08.054">doi:10.1016/j.chroma.2007.08.054</a></li>
  <li id="ref12">Horváth K, Fairchild JN, Guiochon G. Detection in comprehensive two-dimensional liquid chromatography. <em>J Chromatogr A</em>. 2009;1216(9):1385-1395. <a href="https://doi.org/10.1016%2Fj.chroma.2008.12.093">doi:10.1016/j.chroma.2008.12.093</a></li>
  <li id="ref13">Vanhoenacker G, Sandra P. High temperature liquid chromatography (HTLC) of peptides and proteins. <em>J Sep Sci</em>. 2006;29(12):1822-1835. <a href="https://doi.org/10.1002%2Fjssc.200600123">doi:10.1002/jssc.200600123</a></li>
</ol>
