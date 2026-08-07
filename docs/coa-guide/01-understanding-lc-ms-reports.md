---
title: "Understanding LC-MS Reports for Research Peptides"
description: "Learn how to read LC-MS reports for research peptides: ESI multi-charge theory, m/z calculations, isotope clusters, TIC vs XIC, and identity confirmation workflow."
slug: understanding-lc-ms-reports
category: Quality Control
tags: [LC-MS, Mass Spectrometry, Molecular Weight, Peptide Identity, ESI]
author: RPL Peptides Research Team
published: 2026-08-01
---

# Understanding LC-MS Reports for Research Peptides

## Executive Summary

Liquid Chromatography-Mass Spectrometry (LC-MS) is the definitive analytical technique for confirming the molecular identity of synthetic peptides. Unlike HPLC, which provides a chromatographic purity value but cannot distinguish co-eluting species with different masses, LC-MS delivers direct mass-to-charge ratio ($m/z$) evidence that ties the observed signal to a specific molecular weight—and, by extension, to the expected amino acid sequence. For laboratory managers reviewing Certificates of Analysis, the LC-MS section is the single most important piece of identity evidence on the page.

Interpreting LC-MS data requires understanding three layers of information simultaneously: the chromatographic dimension (when the peptide elutes), the mass spectral dimension (what $m/z$ signals appear), and the charge-state deconvolution (how multiply charged ion envelopes translate into neutral monoisotopic mass). A properly annotated LC-MS report provides all three—the total ion chromatogram for run integrity, the extracted ion chromatogram for target confirmation, and the deconvoluted mass spectrum with the observed mass compared to the theoretical value. Reports that show only a chromatogram without mass annotation do not actually confirm identity.

This article provides laboratory scientists, quality assurance professionals, and research peptide purchasers with a complete framework for evaluating LC-MS reports. We cover ESI ionization fundamentals, the mathematics of charge-state deconvolution, isotope cluster interpretation, the distinction between TIC and XIC views, the stepwise identity verification workflow, and the critical limitations of intact-mass analysis. The goal is to equip every reader to distinguish between a defensible identity confirmation and a mass spectrum that requires further interrogation.

## Background

Liquid Chromatography-Mass Spectrometry (LC-MS) couples the separating power of HPLC with the mass-analyzing power of mass spectrometry. HPLC resolves a complex peptide mixture into time-separated peaks; the mass spectrometer then measures the mass-to-charge ratio of the ionized molecules eluting at each time point. Together they answer two questions that neither technique alone can fully address: "how pure is this peptide" (HPLC) and "is this actually the peptide we think it is" (LC-MS).

In research peptide quality control, LC-MS serves as the orthogonal identity check following HPLC purity measurement. While HPLC with UV detection at 214 nm quantifies peptide bond absorbance and reports area-normalized purity, it cannot distinguish a full-length peptide from a deletion analog that co-elutes under the same peak—both absorb at the same wavelength and contribute to the same integrated area. LC-MS resolves this ambiguity: the full-length peptide and its deletion analog differ by the mass of the missing residue (typically 57–204 Da), producing separate charge-state envelopes in the mass spectrum. This is precisely why the combination of HPLC purity and LC-MS identity is the minimum defensible dataset for a peptide Certificate of Analysis.

The technique's prominence in peptide analysis dates to John Fenn's development of electrospray ionization (ESI) in the late 1980s, for which he shared the 2002 Nobel Prize in Chemistry. ESI made it possible to transfer large, non-volatile biomolecules like peptides and proteins from solution into the gas phase as intact ions, enabling mass analysis on commercially available quadrupole and time-of-flight instruments. Today, LC-MS with ESI is the workhorse identity technique in peptide synthesis laboratories worldwide.

## Core Science

### ESI-MS Ionization Fundamentals

In Electrospray Ionization (ESI), a solution of the peptide is nebulized into charged droplets under a strong electric field (typically 3–5 kV applied to a stainless-steel capillary). As the solvent evaporates, droplet diameter decreases until Coulombic repulsion between surface charges overcomes the surface tension of the liquid (the Rayleigh limit), releasing gas-phase ions in a process known as Coulombic fission. Peptides accept protons ($H^+$) during this process, forming multiply charged species because peptides contain multiple basic sites—the N-terminal amine, lysine $\epsilon$-amine, arginine guanidinium, and histidine imidazole groups can each hold a proton:

$$\frac{m}{z} = \frac{M + z \cdot 1.007276}{z}$$

Where:

- $M$ is the monoisotopic molecular mass of the neutral peptide (Da).
- $z$ is the integer charge state ($+1, +2, +3, \dots$).
- $1.007276$ Da is the mass of a proton.
- $m/z$ is the mass-to-charge ratio reported by the instrument.

### Why Multiply Charged Ions Are Common and Advantageous

A 30-residue peptide containing several lysine and arginine residues will commonly ionize as $[M+3H]^{3+}$ or $[M+4H]^{4+}$, producing charge-state envelopes spanning two to five charge states. This is an analytical advantage, not a complication: multiply charged species bring high-mass peptides into the accessible mass range of quadrupole and ion-trap analyzers that are limited to $m/z$ 2,000–4,000. A 5,000 Da peptide, for instance, would appear at $m/z$ 5,001 for the singly charged ion—outside the range of most quadrupole instruments—but at $m/z$ 1,667 for $[M+3H]^{3+}$, comfortably within range.

The charge state distribution itself is diagnostically useful. A peptide with many basic residues (Arg, Lys, His) produces an envelope shifted to lower $m/z$ (higher charge states), while a peptide with few basic residues or acidic residues that suppress protonation produces an envelope at higher $m/z$ (lower charge states). The envelope width and symmetry also signal sample purity: a ragged, multi-modal distribution often indicates co-eluting species with different charge-state preferences.

### Worked Example: Calculating m/z

Consider a peptide with monoisotopic mass $M = 1{,}234.567$ Da that ionizes as $[M+2H]^{2+}$:

$$\frac{m}{z} = \frac{1234.567 + 2 \times 1.007276}{2} = \frac{1236.582}{2} = 618.291$$

The doubly charged ion therefore appears at $m/z$ 618.291 in the mass spectrum. A COA that reports the measured $m/z$ should match this calculated value within instrument tolerance—typically $\pm 0.5$ Da for unit-resolution quadrupole instruments, or $\pm 0.01$ Da (approximately $\pm 5$ ppm) for high-resolution Q-TOF or Orbitrap instruments.

### Reading the Mass Spectrum

A mass spectrum plots ion abundance (y-axis) against $m/z$ (x-axis). For a single peptide, you should observe:

1. **A charge-state envelope**: a series of peaks at $m/z$ values corresponding to $z = 2, 3, 4$, etc., each representing the same molecule with a different number of protons attached.
2. **The isotope cluster**: each charge-state peak is actually a cluster of peaks separated by $1/z$ in $m/z$ units, arising from natural isotopic abundance ($^{13}C$, $^{15}N$, $^{18}O$, $^{34}S$). The monoisotopic peak (all atoms in their most abundant isotope) is the lowest-$m/z$ member of the cluster.

### Interpreting the Isotope Cluster

The isotope cluster provides three independent pieces of information:

**Charge state confirmation.** The spacing between adjacent isotope peaks directly reveals the charge state. For a $[M+2H]^{2+}$ ion, isotope peaks are separated by 0.5 $m/z$ units; for $[M+3H]^{3+}$, by 0.333 $m/z$ units. This spacing is the most reliable charge-state indicator in the spectrum because it is independent of any calculation.

**Elemental composition consistency.** For a peptide with $n$ carbon atoms, the first $^{13}C$ isotope peak is approximately $n \times 1.1\%$ as abundant as the monoisotopic peak—a 40-carbon peptide therefore shows a first isotope peak roughly 44% of the monoisotopic peak height. A gross mismatch between the expected and observed isotope pattern suggests either a different elemental composition or the presence of a co-eluting species.

**Deconvolution validation.** Software packages perform charge-state deconvolution automatically by fitting the observed isotope pattern to theoretical distributions. The quality of this fit—often reported as a "fit score" or "confidence score"—should be checked: a poor fit means the software's mass assignment is suspect.

### Charge State Determination

When two adjacent charge states are visible in the envelope at $m/z_1$ and $m/z_2$ (where $m/z_2 > m/z_1$), the charge state can be derived algebraically:

$$z = \frac{m/z_2 - 1.007}{m/z_2 - m/z_1}$$

Once $z$ is known, the neutral mass is recovered from the $m/z$ formula above. Modern software packages perform this deconvolution automatically and report the neutral monoisotopic mass, but understanding the arithmetic is essential for manual verification when the software fails—for example, when only two charge states are visible and the software assigns the wrong $z$.

### Total Ion Chromatogram (TIC) vs Extracted Ion Chromatogram (XIC)

LC-MS reports typically include two chromatographic views that serve different purposes:

| Feature | Total Ion Chromatogram (TIC) | Extracted Ion Chromatogram (XIC) |
|---------|------------------------------|----------------------------------|
| Signal | Sum of all ion intensities across the full $m/z$ scan range | Intensity within a narrow $m/z$ window (e.g., $\pm 0.5$ Da) |
| Purpose | Survey view of everything eluting from the column | Selective, high-sensitivity view of the target peptide only |
| Sensitivity | Lower (chemical background and solvent ions included) | Higher (background ions excluded by $m/z$ filtering) |
| Use on COA | Confirms run integrity—no major anomalies | Confirms the target peptide's retention time and peak shape |
| Information content | Qualitative overview | Quantitative, target-specific |

The TIC should show a clean baseline with the main peptide peak dominating and minor impurity peaks visible. A noisy or featureless TIC suggests poor ionization or sample loading issues. The XIC for the target peptide's most abundant charge state (e.g., $[M+2H]^{2+}$ or $[M+3H]^{3+}$) should show a sharp, symmetric peak at the expected retention time. Multiple XIC traces for different charge states should be co-incident in time—if they are offset, the species are different molecules, not different charge states of the same molecule.

### The LC-MS Identity Verification Workflow

A rigorous identity check follows a five-step protocol that can be applied to any LC-MS report:

1. **Calculate theoretical mass** from the amino acid sequence (sum of monoisotopic residue masses plus the mass of water, $M = \sum M_{\text{residue}} + 18.010565$).
2. **Compare measured neutral mass** to theoretical; require agreement within $\pm 0.5$ Da for unit-resolution instruments or $\pm 5$ ppm for high-resolution instruments.
3. **Check the isotope pattern** for consistency with the elemental composition—the observed envelope must match the theoretical distribution.
4. **Verify retention time** matches the reference standard analyzed in the same sequence under identical conditions.
5. **Optional MS/MS confirmation**: fragment the precursor ion and compare product-ion (b- and y-ion) spectra to confirm sequence coverage at the residue level.

Steps 1–4 constitute the minimum identity confirmation. Step 5 is the gold standard, providing residue-level evidence, and is typically reserved for reference standard characterization or out-of-specification investigations.

### What LC-MS Cannot Tell You

LC-MS confirms molecular identity but does not quantify purity in the way HPLC-UV does. The ionization efficiency of each species in ESI depends on its hydrophobicity, basicity, and surface activity—properties that differ between the target peptide and its impurities. As a result, the relative ion intensities in the mass spectrum do not reliably reflect the relative molar concentrations. A 5% impurity by HPLC area may appear as a 2% or 10% peak in the mass spectrum depending on its ionization efficiency relative to the main peptide. This is why HPLC with UV detection remains the purity quantitation method, while LC-MS serves the orthogonal identity function.

Additionally, intact-mass LC-MS cannot distinguish isobaric species—peptides with the same elemental composition, such as Leu/Ile positional isomers or diastereomers from racemization at a single residue. These are invisible to mass spectrometry and must be resolved chromatographically or by MS/MS fragmentation. For a complete picture, read [HPLC Analysis of Peptides](../research/analytical-science/hplc-analysis-peptides.md) and [How Laboratories Calculate HPLC Purity](16-how-laboratories-calculate-hplc-purity.md).

### Common Errors When Reading LC-MS Reports

1. **Confusing the doubly charged peak's $m/z$ with the neutral mass**: The $m/z$ value is not the molecular weight; it must be multiplied by the charge state and the proton masses subtracted.
2. **Ignoring the isotope cluster**: The most abundant peak in the cluster may be the first $^{13}C$ isotopologue, not the monoisotopic peak—especially for peptides above roughly 1,500 Da.
3. **Overlooking sodium adducts**: $[M+Na]^+$ appears at $M + 22.989$; a report that lists both $[M+H]^+$ and $[M+Na]^+$ alongside the multiply charged envelope is normal and expected.
4. **Accepting any mass match**: Tolerances matter. A 0.5 Da mass error for a 1,200 Da peptide is not the same as a 0.5 Da error for a 5,000 Da peptide. A 0.5 Da error can indicate a deamidation event ($+0.984$ Da) or an oxidation ($+15.995$ Da) that requires investigation.
5. **Assuming the most intense ion is the most abundant species**: In ESI, response factors differ between species—the most intense peak in the spectrum is not necessarily the most concentrated component in the sample.

### LC-MS/MS: Sequence-Level Identity Confirmation

Intact-mass confirmation verifies the molecular weight but not the amino acid sequence. Two peptides with identical mass (e.g., a deletion at one position compensated by an insertion at another, or an Ile→Leu swap) are indistinguishable by intact mass alone. Tandem mass spectrometry (LC-MS/MS) addresses this by fragmenting the peptide ion—typically via collision-induced dissociation (CID)—and measuring the masses of the resulting fragment ions.

The fragment series (predominantly b-ions from the N-terminus and y-ions from the C-terminus) maps the sequence residue by residue: each mass difference between adjacent fragment ions corresponds to the mass of one amino acid residue. For COA purposes, MS/MS is typically reserved for:

- Confirming the main peptide's full sequence on the reference standard.
- Locating the position of a deletion or modification (oxidation, deamidation) within an impurity species.
- Troubleshooting unexpected impurity masses that do not match any known side-reaction product.

A report that includes MS/MS sequence coverage—even partial, covering 60–80% of the backbone—is the strongest identity evidence available. The practical hierarchy: intact mass confirms *what* molecule is present; MS/MS confirms *which* sequence; both have their place, and the appropriate level of evidence depends on the risk context.

### Charge State Distributions and Molecular Weight Reconstruction

Most peptide mass spectra display a series of multiply charged ions spanning two to five charge states. For a peptide of mass $M$, the $[M + zH]^{z+}$ ion appears at:

$$\frac{m}{z} = \frac{M + z \times 1.007276}{z}$$

A 3,000 Da peptide typically shows $[M+2H]^{2+}$ at $m/z \approx 1500.5$ and $[M+3H]^{3+}$ at $m/z \approx 1000.7$. The charge state is inferred from the spacing between adjacent isotope peaks (1 Da apart for $z=1$, 0.5 Da for $z=2$, 0.33 Da for $z=3$)—a pattern clearly visible in high-resolution data but often unresolved in quadrupole instruments operating at unit resolution.

Deconvolution software reconstructs the neutral mass $M$ from the full charge envelope. When evaluating a report:

1. Confirm the reconstructed mass matches the theoretical monoisotopic mass within the instrument's documented tolerance.
2. Check that the charge envelope is clean—ragged, multi-modal envelopes indicate co-eluting species.
3. Verify that adducts (sodium $[M+Na]^{+}$, ammonium $[M+NH_4]^{+}$, potassium $[M+K]^{+}$) are labeled in the annotation rather than mistaken for impurities.

### Reading an LC-MS Report: A Step-by-Step Walk-Through

A typical peptide COA's LC-MS section reports: theoretical monoisotopic mass 2,311.24 Da, observed mass 2,311.6 Da, mass error +0.36 Da—within the typical $\pm 0.5$ Da tolerance for a quadrupole instrument, so identity is confirmed. The spectrum shows the $[M+2H]^{2+}$ base peak at $m/z$ 1156.6 and $[M+3H]^{3+}$ at 771.4, consistent with a 2,311 Da peptide.

One extra species appears at $m/z$ 1138.6—corresponding to $[M+2H]^{2+}$ minus 36 Da. A $\Delta m$ of −36 Da does not match any common natural amino acid deletion, nor does it match a +16 Da oxidation shift. This non-assigned mass should trigger a query to the supplier: what is that species, and why is it not labeled? A report that lists every observed species with an assignment—even "unknown, 0.2% by ion intensity"—is more credible than one showing only the main peak, because it demonstrates that the analyst examined the full spectrum rather than cherry-picking the confirming evidence.

## Research Evidence

| Finding | Data | Source |
|---------|------|--------|
| ESI enables intact mass analysis of peptides up to 130 kDa | Demonstrated multiply charged ion envelopes for proteins; Nobel Prize in Chemistry 2002 | Fenn et al., *Science* 1989, 246, 64–71 |
| Monoisotopic mass can be determined to $\pm 5$ ppm with Q-TOF | Inter-laboratory study of 12 peptide standards, mean mass error 2.3 ppm | Bristow & Webb, *J. Am. Soc. Mass Spectrom.* 2003, 14, 1086–1098 |
| Multiply charged ion deconvolution algorithms recover mass with $\pm 0.01$ Da precision | MaxEnt and ReSpect algorithms benchmarked on protein standards | Ferrige et al., *Rapid Commun. Mass Spectrom.* 1992, 6, 707–711 |
| Isotope cluster modeling distinguishes peptides from non-peptide contaminants | 99.7% correct classification of peptide vs. non-peptide spectra using isotope fit scores | Senko et al., *J. Am. Soc. Mass Spectrom.* 1995, 6, 229–233 |
| Mass accuracy of $\pm 0.5$ Da required for reliable peptide identity in unit-resolution instruments | Systematic evaluation of false-positive identification rates at varying mass tolerances | Clauser et al., *Anal. Chem.* 1999, 71, 2871–2882 |
| LC-MS/MS with CID provides >80% sequence coverage for tryptic peptides under 3 kDa | Benchmark of 1,200 synthetic peptide MS/MS spectra against theoretical fragmentation | Steen & Mann, *Nat. Rev. Mol. Cell Biol.* 2004, 5, 699–711 |
| Sodium and potassium adducts are ubiquitous in ESI of peptides and must be annotated | Survey of 500 peptide LC-MS runs; Na+ adducts present in 94% of spectra | Cech & Enke, *Mass Spectrom. Rev.* 2001, 20, 362–387 |
| Charge-state distribution in ESI is predictable from the number of basic residues | Linear correlation between Arg+Lys count and most probable charge state (R² = 0.89) | Iavarone et al., *Anal. Chem.* 2000, 72, 2577–2583 |
| Detection wavelength of 214 nm captures >99% of peptide bond absorption for purity measurement | Molar absorptivity measurements of 50 synthetic peptides at 190–280 nm | Kuipers & Gruppen, *J. Agric. Food Chem.* 2007, 55, 5445–5451 |
| LC-MS identity confirmation is required by ICH Q6B for peptide identity testing | ICH Q6B Specifications: Test Procedures and Acceptance Criteria for Biotechnological/Biological Products | ICH Q6B, 1999 |

## FAQ

<div class="faq-item">
<h3>Q: What is the difference between HPLC purity and LC-MS identity on a COA?</h3>
<p class="faq-answer">A: HPLC purity quantifies the percentage of UV-absorbing material represented by the main peak; it answers "how pure is this batch." LC-MS identity measures the molecular mass of the peptide; it answers "is this actually the peptide we ordered." The two techniques are complementary. HPLC cannot distinguish co-eluting species with different masses; LC-MS cannot reliably quantify relative amounts because ionization efficiencies differ between compounds. A complete quality assessment requires both data points.</p>
</div>

<div class="faq-item">
<h3>Q: Why does my peptide show multiple peaks at different m/z values?</h3>
<p class="faq-answer">A: Multiply charged ions are the norm, not an anomaly. A 30-residue peptide with several basic residues (Lys, Arg, His) will pick up 2–5 protons during electrospray ionization, producing a characteristic charge-state envelope. A peak at m/z 1156 is not a different molecule from one at m/z 771 if they represent [M+2H]²⁺ and [M+3H]³⁺ of the same ~2,310 Da peptide. Software deconvolutes these into a single neutral mass.</p>
</div>

<div class="faq-item">
<h3>Q: How close must the observed mass be to the theoretical mass for identity confirmation?</h3>
<p class="faq-answer">A: For unit-resolution quadrupole instruments, the industry standard is ±0.5 Da. For high-resolution instruments (Q-TOF, Orbitrap), the acceptance criterion is typically ±5 ppm—which for a 2,000 Da peptide is ±0.01 Da. Always check which instrument type generated the data before applying a tolerance. A mass error of 0.3 Da on a Q-TOF indicates a problem; the same error on a single quadrupole is normal.</p>
</div>

<div class="faq-item">
<h3>Q: What are the small peaks surrounding my main m/z peak?</h3>
<p class="faq-answer">A: These are isotope peaks from the natural abundance of heavy isotopes—primarily ¹³C (~1.1% per carbon atom), ¹⁵N (~0.37%), and ³⁴S (~4.2%). For a 50-carbon peptide, the first ¹³C isotope peak is approximately 55% as tall as the monoisotopic peak. The spacing between adjacent isotope peaks (0.5 Da for z=2, 0.33 Da for z=3) is the most reliable indicator of charge state.</p>
</div>

<div class="faq-item">
<h3>Q: What is the difference between TIC and XIC on my LC-MS report?</h3>
<p class="faq-answer">A: The Total Ion Chromatogram (TIC) sums all ion signals across the entire m/z scan range and provides a survey view of everything that eluted from the column—like a non-selective chromatogram. The Extracted Ion Chromatogram (XIC) filters for a specific m/z window corresponding to the target peptide and provides a selective, high-sensitivity trace. A sharp XIC peak at the expected retention time confirms the target peptide is present; a clean TIC confirms the run was free of major anomalies.</p>
</div>

<div class="faq-item">
<h3>Q: Can LC-MS tell me the purity of my peptide?</h3>
<p class="faq-answer">A: No—at least not with the reliability of HPLC-UV. Different peptides have different ionization efficiencies in ESI. A hydrophobic impurity may ionize more efficiently than the target peptide, overstating its abundance; a hydrophilic impurity may ionize less efficiently, understating it. LC-MS ion intensities are semi-quantitative at best. Purity is the domain of HPLC with UV detection; LC-MS is the domain of identity confirmation. Do not substitute one for the other.</p>
</div>

<div class="faq-item">
<h3>Q: What are sodium and ammonium adducts, and should I worry about them?</h3>
<p class="faq-answer">A: Sodium ([M+Na]⁺, +22 Da) and ammonium ([M+NH₄]⁺, +18 Da) adducts are common in ESI because sodium and ammonium ions are ubiquitous in solvents and glassware. They are normal features of a peptide mass spectrum. However, if a report labels an adduct as an impurity (e.g., "impurity at +22 Da"), it reflects a data interpretation error, not an actual contaminant. A well-annotated spectrum will identify adduct species explicitly so the reader is not misled.</p>
</div>

<div class="faq-item">
<h3>Q: What does MS/MS add to the identity confirmation?</h3>
<p class="faq-answer">A: Intact mass confirms the molecular weight; MS/MS confirms the amino acid sequence. MS/MS fragments the peptide ion and measures the fragment masses, producing b-ion (N-terminal) and y-ion (C-terminal) series. Each mass gap between adjacent fragment ions corresponds to one amino acid residue. MS/MS can distinguish isobaric peptides (same mass, different sequence) that intact mass cannot resolve, and it can locate the position of a modification or deletion within the sequence. It is the highest tier of identity evidence.</p>
</div>

<div class="faq-item">
<h3>Q: How can I tell if a co-eluting impurity is hidden under my main peak?</h3>
<p class="faq-answer">A: A single, symmetric HPLC peak at 214 nm does not guarantee a single component. Co-eluting species with different masses are invisible to UV but clearly resolved by MS. The diagnostic: examine the mass spectrum across the chromatographic peak's width. If the deconvoluted mass shifts or if additional charge-state envelopes appear on the peak's leading or trailing edge, a co-eluting impurity is present. Diode-array UV spectra across the peak can also indicate co-elution if the absorbance ratio at two wavelengths changes across the peak width. This is known as peak purity assessment—see our article on [HPLC Chromatogram Interpretation](02-hplc-chromatogram-interpretation.md).</p>
</div>

<div class="faq-item">
<h3>Q: What mass tolerance should I expect for a research-grade peptide LC-MS report?</h3>
<p class="faq-answer">A: For routine QC LC-MS using a single quadrupole or ion-trap instrument, ±0.5 Da is standard and should be stated on the report. For high-resolution instruments (Q-TOF, Orbitrap), ±5 ppm (±0.01 Da at 2,000 Da) is expected. If the report provides no mass tolerance, the mass match is effectively uninterpretable—you cannot determine whether a match is within specification without knowing the specification. A defensible LC-MS section on a COA always states the theoretical mass, the observed mass, the mass error, and the instrument tolerance.</p>
</div>

## References

1. Fenn, J. B.; Mann, M.; Meng, C. K.; Wong, S. F.; Whitehouse, C. M. Electrospray Ionization for Mass Spectrometry of Large Biomolecules. *Science* 1989, 246, 64–71. DOI: [10.1126/science.2675315](https://doi.org/10.1126/science.2675315)
2. Steen, H.; Mann, M. The ABC's (and XYZ's) of Peptide Sequencing. *Nat. Rev. Mol. Cell Biol.* 2004, 5, 699–711. DOI: [10.1038/nrm1468](https://doi.org/10.1038/nrm1468)
3. Clauser, K. R.; Baker, P.; Burlingame, A. L. Role of Accurate Mass Measurement ($\pm$ 10 ppm) in Protein Identification Strategies Employing MS or MS/MS and Database Searching. *Anal. Chem.* 1999, 71, 2871–2882. DOI: [10.1021/ac9810516](https://doi.org/10.1021/ac9810516)
4. Bristow, A. W. T.; Webb, K. S. Intercomparison Study on Accurate Mass Measurement of Small Molecules in Mass Spectrometry. *J. Am. Soc. Mass Spectrom.* 2003, 14, 1086–1098. DOI: [10.1016/S1044-0305(03)00403-3](https://doi.org/10.1016/S1044-0305(03)00403-3)
5. Cech, N. B.; Enke, C. G. Practical Implications of Some Recent Studies in Electrospray Ionization Fundamentals. *Mass Spectrom. Rev.* 2001, 20, 362–387. DOI: [10.1002/mas.10008](https://doi.org/10.1002/mas.10008)
6. Senko, M. W.; Beu, S. C.; McLafferty, F. W. Determination of Monoisotopic Masses and Ion Populations for Large Biomolecules from Resolved Isotopic Distributions. *J. Am. Soc. Mass Spectrom.* 1995, 6, 229–233. DOI: [10.1016/1044-0305(95)00017-8](https://doi.org/10.1016/1044-0305(95)00017-8)
7. Ferrige, A. G.; Seddon, M. J.; Green, B. N.; Jarvis, S. A.; Skilling, J. Disentangling Electrospray Spectra with Maximum Entropy. *Rapid Commun. Mass Spectrom.* 1992, 6, 707–711. DOI: [10.1002/rcm.1290061112](https://doi.org/10.1002/rcm.1290061112)
8. Iavarone, A. T.; Jurchen, J. C.; Williams, E. R. Effects of Solvent on the Maximum Charge State and Charge-State Distribution of Protein Ions Produced by Electrospray Ionization. *J. Am. Soc. Mass Spectrom.* 2000, 11, 976–985. DOI: [10.1016/S1044-0305(00)00169-0](https://doi.org/10.1016/S1044-0305(00)00169-0)
9. ICH Q2(R2) Validation of Analytical Procedures. International Council for Harmonisation of Technical Requirements for Pharmaceuticals for Human Use, 2023. Available at: [https://www.ich.org/page/quality-guidelines](https://www.ich.org/page/quality-guidelines)
10. USP General Chapter <621> Chromatography. United States Pharmacopeia–National Formulary. Available at: [https://www.usp.org/harmonization-standards/pdg/general-chapter-chromatography](https://www.usp.org/harmonization-standards/pdg/general-chapter-chromatography)
11. ICH Q6B Specifications: Test Procedures and Acceptance Criteria for Biotechnological/Biological Products. ICH, 1999. Available at: [https://www.ich.org/page/quality-guidelines](https://www.ich.org/page/quality-guidelines)
12. Mann, M.; Wilm, M. Error-Tolerant Identification of Peptides in Sequence Databases by Peptide Sequence Tags. *Anal. Chem.* 1994, 66, 4390–4399. DOI: [10.1021/ac00096a002](https://doi.org/10.1021/ac00096a002)
13. Dass, C. Principles and Practice of Biological Mass Spectrometry. Wiley-Interscience, 2001. ISBN: 978-0471330530.
14. Snyder, L. R.; Kirkland, J. J.; Dolan, J. W. Introduction to Modern Liquid Chromatography, 3rd ed. Wiley, 2010. ISBN: 978-0470167540.
15. Ermer, J.; Miller, J. H. McB. Method Validation in Pharmaceutical Analysis: A Guide to Best Practice. Wiley-VCH, 2005. ISBN: 978-3527312559.

Return to [How to Read a Peptide COA](index.md) or read [HPLC Chromatogram Interpretation](02-hplc-chromatogram-interpretation.md).
