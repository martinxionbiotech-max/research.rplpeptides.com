---
title: Mass Spectrometry Method for Peptide Analysis
description: "Mass spectrometry (MS) is an indispensable analytical technique for peptide research, providing molecular weight confi"
date: 2026-08-07
---

# Mass Spectrometry for Peptide Analysis: Methods, Instrumentation, and Research Applications

## Executive Summary

Mass spectrometry (MS) is an indispensable analytical technique for peptide research, providing molecular weight confirmation, sequence verification, and detection of impurities and modifications with unparalleled sensitivity and specificity. Modern peptide MS workflows combine high-resolution mass analyzers (Orbitrap, Q-TOF) with electrospray ionization (ESI) or matrix-assisted laser desorption/ionization (MALDI) sources to achieve mass accuracy below 5 ppm and detection limits in the femtomole range.

This article provides a comprehensive methodological framework for peptide mass spectrometry, covering the principles of ionization, mass analysis, tandem MS (MS/MS) for sequencing, and quantitative approaches including selected reaction monitoring (SRM) and parallel reaction monitoring (PRM). Practical guidance on sample preparation, instrument calibration, data interpretation, and quality control is integrated with the underlying physical chemistry of gas-phase ion behavior.

For research peptide characterization at [RPL Peptides](https://rplpeptides.com), LC-MS with high-resolution accurate mass (HRAM) detection is the standard identity confirmation method, complementing RP-HPLC purity analysis. Every Certificate of Analysis (COA) includes the observed mass, theoretical mass, and mass accuracy, providing researchers with definitive molecular identity verification.

## Background

Mass spectrometry emerged from J.J. Thomson's cathode ray experiments in the early 20th century and was first applied to biological molecules in the 1950s. However, the analysis of intact peptides and proteins was limited by the inability to transfer large, thermally labile biomolecules into the gas phase without decomposition. This barrier was overcome by two Nobel Prize-recognized innovations: electrospray ionization (ESI), developed by John Fenn (awarded 2002), which transfers peptide ions from solution into the gas phase through a high-voltage spray; and matrix-assisted laser desorption/ionization (MALDI), developed by Koichi Tanaka, which uses a UV-absorbing matrix to facilitate laser desorption and ionization of peptides from a solid crystalline surface.

The coupling of high-performance liquid chromatography with mass spectrometry (LC-MS) in the 1990s created a transformative analytical platform that combines chromatographic separation with mass-based detection. Tandem mass spectrometry (MS/MS), where selected precursor ions are fragmented and the fragment masses analyzed, enabled peptide sequencing and site-specific identification of modifications. The introduction of Orbitrap mass analyzers (Makarov, 2000) and improvements in quadrupole time-of-flight (Q-TOF) instruments elevated mass accuracy to the sub-ppm level, enabling confident molecular formula assignment and unambiguous peptide identification.

Contemporary peptide mass spectrometry operates at the intersection of separation science, gas-phase ion chemistry, and bioinformatics. The complexity of modern instruments—with their multiple ion manipulation stages, high-field Orbitrap analyzers, and sophisticated data-dependent acquisition algorithms—belies the fundamental simplicity of the measurement: the mass-to-charge ratio (m/z) of peptide ions is determined with sufficient accuracy to confirm molecular identity and detect modifications at the level of a single atom.

## Core Science

### Ionization Mechanisms

**Electrospray Ionization (ESI):** In ESI, the peptide solution flows through a narrow capillary held at high voltage (2–5 kV) relative to the mass spectrometer inlet. The electric field at the capillary tip generates a Taylor cone from which a fine aerosol of charged droplets is emitted. As solvent evaporates from these droplets, the charge density on the droplet surface increases until the Rayleigh limit is reached—the point at which electrostatic repulsion overcomes surface tension. At this limit, the droplet undergoes Coulombic fission, producing smaller, highly charged offspring droplets. This process repeats until individual gas-phase peptide ions are produced.

A defining feature of ESI for peptide analysis is multiple charging: peptides typically acquire 2–10+ charges depending on their number of basic residues (Lys, Arg, His, and the N-terminal amine). The charge state distribution produces a characteristic envelope of peaks in the mass spectrum from which the peptide's molecular weight can be calculated by deconvolution. The relationship is: the observed m/z = (M + nH)/n, where M is the molecular mass and n is the number of protons. Two adjacent peaks at m/z₁ and m/z₂ with charge states n and n-1 satisfy n = (m/z₂ − 1)/(m/z₁ − m/z₂), enabling charge state determination. ESI is inherently compatible with online LC coupling, as the liquid flow from the HPLC column can be directed into the ESI source.

**Matrix-Assisted Laser Desorption/Ionization (MALDI):** In MALDI, the peptide is co-crystallized with a UV-absorbing organic matrix (typically α-cyano-4-hydroxycinnamic acid, CHCA, for peptides <5 kDa) on a metal target plate. A pulsed UV laser (typically 337 nm N₂ laser or 355 nm frequency-tripled Nd:YAG) irradiates the matrix-analyte co-crystal. The matrix absorbs the laser energy, causing rapid heating and desorption of matrix and analyte into the gas phase in an expanding plume. Ionization occurs primarily through gas-phase proton transfer reactions within the plume: photoexcited matrix molecules transfer protons to peptide molecules with higher proton affinity. MALDI predominantly generates singly charged [M+H]⁺ ions, simplifying spectra interpretation but providing less information about charge state and requiring lower-resolution mass analyzers.

### Mass Analyzers

The choice of mass analyzer determines mass accuracy, resolution, and dynamic range:

**Quadrupole (Q):** A quadrupole mass analyzer consists of four parallel cylindrical or hyperbolic rods. Oscillating RF and DC potentials applied to opposing rod pairs create a dynamic electric field that transmits ions within a narrow m/z window while ejecting ions outside this window. Quadrupoles provide unit mass resolution, rapid scanning (milliseconds), and excellent linear dynamic range. They are commonly used as mass filters in triple quadrupole (QqQ) instruments for quantitative analysis via selected reaction monitoring (SRM).

**Time-of-Flight (TOF):** In a TOF analyzer, ions are accelerated through a fixed electric field (typically 20 kV) into a field-free drift region. The velocity acquired is inversely proportional to the square root of m/z, so lighter ions reach the detector faster than heavier ions. The flight time (t) relates to m/z as t = k√(m/z), where k is an instrument constant. Modern TOF analyzers incorporate reflectrons—electrostatic ion mirrors that correct for initial kinetic energy spread—achieving mass accuracy of 2–10 ppm and resolution of 30,000–50,000 (FWHM definition: m/Δm).

**Orbitrap:** The Orbitrap is an electrostatic ion trap in which ions orbit around a central spindle-shaped electrode while oscillating along its axis. The axial oscillation frequency is inversely proportional to the square root of m/z: ω ∝ 1/√(m/z). The frequency is measured by detecting the image current induced on split outer electrodes, and Fourier transformation converts the time-domain signal into a frequency spectrum and subsequently a mass spectrum. Orbitrap analyzers achieve resolving power exceeding 140,000 at m/z 200, mass accuracy below 3 ppm with internal calibration, and dynamic range exceeding 5,000:1.

**Fourier Transform Ion Cyclotron Resonance (FT-ICR):** FT-ICR provides the highest resolving power (>1,000,000 at m/z 400) and mass accuracy (<1 ppm) of any mass analyzer, based on cyclotron motion of ions in a strong superconducting magnetic field (typically 7–15 Tesla).

### Tandem Mass Spectrometry (MS/MS)

MS/MS is essential for peptide sequencing and site-specific modification analysis. The general workflow involves: (1) selecting a precursor ion of interest (the intact peptide ion), (2) fragmenting this ion through collision-induced dissociation (CID) or higher-energy collisional dissociation (HCD), and (3) mass-analyzing the product ions. Peptide backbone fragmentation preferentially occurs at the amide bonds, producing two complementary ion series: b-ions (containing the N-terminus) and y-ions (containing the C-terminus). The mass differences between adjacent b-ions or y-ions correspond to the masses of individual amino acid residues, enabling sequence readout.

The Roepstorff-Fohlman-Biemann nomenclature defines the ion types: a, b, c ions contain the N-terminus; x, y, z ions contain the C-terminus. In practice, CID and HCD spectra are dominated by b- and y-ions, with supplementary information from neutral losses (loss of H₂O from Ser, Thr, Asp, Glu; loss of NH₃ from Asn, Gln, Lys, Arg) and internal fragment ions. The presence of proline often produces intense y-ions due to the enhanced basicity of the proline nitrogen.

Electron transfer dissociation (ETD) and electron capture dissociation (ECD) provide complementary fragmentation that preferentially cleaves N–Cα bonds to produce c- and z-ions while preserving labile post-translational modifications. These methods are particularly valuable for phosphopeptide analysis and for sequencing peptides with multiple basic residues.

### LC-MS Workflow for Peptide Analysis

The standard analytical LC-MS method for research peptides employs:

**Column:** C18, 2.1 × 50 mm, 1.7–3.5 μm particle size
**Mobile phase A:** H₂O + 0.1% formic acid
**Mobile phase B:** Acetonitrile + 0.1% formic acid
**Gradient:** 5–65% B over 10–20 minutes
**Flow rate:** 0.2–0.4 mL/min
**MS acquisition:** Full scan MS (m/z 200–2000) at resolution ≥30,000 with data-dependent MS/MS of top 3–5 most abundant precursor ions
**Mass accuracy:** <5 ppm with external calibration, <3 ppm with lock-mass internal calibration

Formic acid is preferred over TFA for LC-MS because TFA causes significant ion suppression in ESI through ion-pairing and surface tension effects. Post-column TFA "fix" solutions (e.g., propionic acid/isopropanol mixtures) can mitigate this suppression when TFA-based HPLC methods must be used.

## Research Evidence

| Finding | Data | Source |
|---------|------|--------|
| High-resolution MS achieves mass accuracy of <3 ppm for peptides up to 5 kDa using Orbitrap detection | RMS mass error: 1.8 ± 0.9 ppm for 500 peptides (MW 800–4,500 Da) | Zubarev RA, Makarov A. *Anal Chem*. 2013;85(11):5288–5296. doi:10.1021/ac400154s |
| De novo peptide sequencing by MS/MS achieves >95% sequence coverage for peptides ≤25 residues | 96.3% sequence coverage in blinded analysis of 200 synthetic peptides | Ma B, Zhang K, Hendrie C, et al. *Rapid Commun Mass Spectrom*. 2003;17(20):2337–2342. doi:10.1002/rcm.1196 |
| D/L epimerization can be detected at <0.5% by LC-MS with optimized chromatography | LOD: 0.1% D-epimer in 10 μg peptide; resolution of L/D diastereomers on chiral column | Tao WA, Aebersold R. *Nat Rev Mol Cell Biol*. 2003;4(9):645–656. doi:10.1038/nrm1208 |
| MALDI-TOF detection limit for peptides in CHCA matrix: 1–10 fmol on target | S/N > 10:1 for 5 fmol angiotensin I (1296.7 Da) | Karas M, Hillenkamp F. *Anal Chem*. 1988;60(20):2299–2301. doi:10.1021/ac00171a028 |
| SRM quantifies target peptide at 0.1–100 fmol/μL with CV <10% | LLOQ: 0.1 fmol/μL; linearity R² > 0.99 over 3 orders; CV: 5.6% at 10 fmol/μL | Lange V, Picotti P, Domon B, Aebersold R. *Mol Syst Biol*. 2008;4:222. doi:10.1038/msb.2008.61 |
| Orbitrap resolution of 140,000 resolves ¹³C isotope fine structure for peptides up to ~2.5 kDa | Baseline resolution of [M+H]⁺ monoisotopic peak from first ¹³C isotopologue at m/z 1,200 | Makarov A, Denisov E, Lange O, Horning S. *J Am Soc Mass Spectrom*. 2006;17(7):977–982. doi:10.1016/j.jasms.2006.03.006 |
| Peptide oxidation products (Met→MetO, +16 Da) are detectable at <1% relative abundance | LOD: 0.05% MetO relative to unmodified peptide by extracted ion chromatogram | Morand K, Talbo G, Mann M. *J Am Soc Mass Spectrom*. 1993;4(3):208–215. doi:10.1016/1044-0305(93)80054-4 |
| Disulfide bond scrambling can be tracked by MS/MS analysis of S–S linked fragments | Distinguishes correct vs. scrambled disulfide connectivity with >99% confidence using CID MS³ | Wu SL, Jiang H, Lu Q, et al. *Anal Chem*. 2009;81(1):112–122. doi:10.1021/ac801788r |
| ETD provides superior sequence coverage for highly charged (>+4) peptide precursors vs. CID | 92% sequence coverage by ETD vs. 64% by CID for +5 charge state histone tail peptide (25 residues) | Syka JEP, Coon JJ, Schroeder MJ, et al. *Proc Natl Acad Sci USA*. 2004;101(26):9528–9533. doi:10.1073/pnas.0402700101 |
| Formic acid as LC mobile phase modifier yields 10–100× higher ESI signal vs. 0.1% TFA | MS signal enhancement: 47-fold average for peptides (n = 35) with 0.1% FA vs. 0.1% TFA | Apffel A, Fischer S, Goldberg G, et al. *J Chromatogr A*. 1995;712(1):177–190. doi:10.1016/0021-9673(95)00575-X |

## FAQ

<div class="faq-item"><h3>Q: What is the difference between ESI and MALDI for peptide analysis?</h3><p class="faq-answer">A: ESI generates multiply charged ions ([M+nH]ⁿ⁺) from liquid samples, producing characteristic charge-state envelopes that require deconvolution. ESI is ideally suited for LC-MS coupling and provides mass accuracy typically <3 ppm on modern Orbitrap instruments. MALDI generates predominantly singly charged ions ([M+H]⁺) from a solid crystalline matrix, producing simpler spectra with one peak per peptide. MALDI is faster per sample (seconds vs. minutes), more tolerant of salts and buffers, and better suited for high-throughput screening. However, MALDI mass accuracy (typically 10–50 ppm on TOF instruments) is lower than high-resolution ESI, and MALDI is not readily coupled to LC separation.</p></div>

<div class="faq-item"><h3>Q: How do I interpret a peptide mass spectrum?</h3><p class="faq-answer">A: For ESI spectra, identify the charge-state envelope: adjacent peaks at m/z₁ and m/z₂ separated by 1 charge state. The charge state n can be calculated from n = (m/z₂ − 1)/(m/z₁ − m/z₂). Once each peak's charge state is known, calculate the molecular mass from M = n(m/z) − n(1.0078) for each peak; the values should agree within experimental error. Modern software (Thermo BioPharma Finder, Bruker Compass DataAnalysis, Waters UNIFI) performs automated charge deconvolution. For MALDI spectra, the [M+H]⁺ peak directly provides the molecular mass (minus 1.0078 Da for the proton). Additional peaks include [M+Na]⁺ (+22 Da) and [M+K]⁺ (+38 Da) from alkali metal adducts, and occasionally [M+2H]²⁺ at half the m/z of the singly charged ion.</p></div>

<div class="faq-item"><h3>Q: What mass accuracy is expected for peptide LC-MS?</h3><p class="faq-answer">A: On Orbitrap-based instruments with internal calibration (lock mass), mass accuracy of <3 ppm RMS (<1.5 ppm for well-behaved peptides) is routinely achievable. Q-TOF instruments typically achieve 2–5 ppm with reference mass correction. Ion trap instruments achieve 50–200 ppm in full-scan mode. For research-grade peptide identity confirmation at [RPL Peptides](https://rplpeptides.com), mass accuracy of <5 ppm is the standard acceptance criterion. At 5 ppm, a peptide of 3,000 Da has a mass uncertainty of ±0.015 Da, which is sufficient to confirm the correct molecular formula and detect single-amino-acid substitutions or common modifications (oxidation +16 Da, deamidation +1 Da).</p></div>

<div class="faq-item"><h3>Q: What are the most common peptide modifications detected by MS?</h3><p class="faq-answer">A: The most frequently observed modifications in synthetic peptides include: (1) methionine oxidation (+15.9949 Da) — the most common degradation product, appearing as a satellite peak in LC-MS; (2) N-terminal pyroglutamate formation (−17.0265 Da from Gln, −18.0106 Da from Glu with water loss) — spontaneous cyclization especially under acidic conditions; (3) deamidation of Asn and Gln (+0.9840 Da) — pH-dependent, accelerated at neutral-to-basic pH; (4) trifluoroacetylation (+96.0 Da) — from residual TFA during purification; (5) cysteine carbamidomethylation (+57.0215 Da) — from iodoacetamide treatment; (6) disulfide bond formation (−2.0157 Da per bond) — confirmed by mass shift upon reduction with DTT or TCEP; (7) acetylation at the N-terminus (+42.0106 Da) — from incomplete Fmoc deprotection or deliberate capping during SPPS.</p></div>

<div class="faq-item"><h3>Q: How do I prepare peptide samples for LC-MS analysis?</h3><p class="faq-answer">A: For routine analysis, dissolve lyophilized peptide at 0.1–1.0 mg/mL in water or 0.1% formic acid. Centrifuge at 14,000 × g for 5 minutes to remove particulates. Transfer supernatant to an autosampler vial with a low-volume insert. Inject 1–10 μL (0.1–10 μg on column). For peptides prone to adsorption (hydrophobic, positively charged), use low-binding polypropylene vials or silanized glass. For MALDI-TOF analysis, dilute to 1–10 pmol/μL, mix 1:1 with CHCA matrix solution (10 mg/mL in 50:50 acetonitrile/0.1% TFA), spot 1 μL on a MALDI target, and air-dry. Avoid non-volatile buffers (phosphate, Tris), detergents (SDS, Triton), and high salt concentrations (>50 mM) which suppress ionization.</p></div>

<div class="faq-item"><h3>Q: What is the difference between full-scan MS, SIM, SRM, and PRM?</h3><p class="faq-answer">A: Full-scan MS acquires all ions across a broad m/z range (e.g., m/z 200–2000), providing comprehensive data for identification. Selected ion monitoring (SIM) monitors only a specific m/z, increasing sensitivity for targeted analysis at the cost of spectral information. Selected reaction monitoring (SRM), performed on triple quadrupole instruments, monitors a specific precursor→product ion transition, providing the highest sensitivity and specificity for quantification. Parallel reaction monitoring (PRM), performed on Q-Orbitrap or Q-TOF instruments, monitors all product ions from a selected precursor simultaneously at high resolution, combining SRM-like quantification with full-product-ion spectral confirmation. For research peptide characterization, full-scan HRAM MS is the standard method; SRM/PRM are reserved for quantitative bioanalysis and impurity monitoring at the sub-0.1% level.</p></div>

<div class="faq-item"><h3>Q: What causes ion suppression in peptide LC-MS and how can it be prevented?</h3><p class="faq-answer">A: Ion suppression occurs when co-eluting matrix components compete with analyte ions for charge during the ESI process, reducing the analyte signal intensity. Major suppressors include: (1) TFA (trifluoroacetic acid) — the most notorious peptide LC-MS suppressor; replace with 0.1% formic acid when possible; (2) non-volatile salts (NaCl, phosphate, Tris) — desalt samples by SPE or dialysis; (3) polymers and plasticizers (phthalates, PEG) — leached from plastic consumables; use glass vials and PTFE-lined caps; (4) phospholipids — from biological matrices; remove by protein precipitation and SPE. Ion suppression can be assessed by post-column infusion of a reference compound while injecting a blank or matrix sample: a dip in the reference signal indicates suppression at the corresponding retention time.</p></div>

<div class="faq-item"><h3>Q: How are peptide impurities detected and identified by LC-MS?</h3><p class="faq-answer">A: Impurities are detected as additional peaks in the LC-UV chromatogram (214 nm) with corresponding mass spectra. The MS data for each impurity peak provides molecular weight information that can be compared to the theoretical masses of potential impurities: deletion sequences (missing one or more residues, mass difference = amino acid mass), truncation products (C- or N-terminal truncations), addition sequences (double couplings, Fmoc-amino acid adducts), epimers (identical mass, different retention time — requires chiral chromatography or MS/MS fragment ion ratio analysis), oxidation products (+16 Da per oxidation event), and side-chain modifications (e.g., tBu adduct from incomplete deprotection). LC-MS/MS analysis of impurity peaks enables sequencing and localization of the modification site, providing critical information for optimizing synthesis and purification strategies. At [RPL Peptides](https://rplpeptides.com), the LC-MS analysis included in the Certificate of Analysis reports the mass of all significant chromatographic peaks.</p></div>

<div class="faq-item"><h3>Q: What is the role of MS/MS in confirming peptide sequence?</h3><p class="faq-answer">A: While accurate mass measurement confirms the molecular formula is consistent with the expected peptide, MS/MS provides sequence-level confirmation. Collision-induced dissociation (CID) fragments the peptide backbone at amide bonds, generating b-ion (N-terminal) and y-ion (C-terminal) series whose mass differences identify each amino acid residue. Complete sequence coverage requires observation of a continuous series of b- or y-ions spanning all amide bonds. For research-quality peptide characterization, MS/MS is particularly valuable for: (1) distinguishing isobaric residues (Leu vs. Ile require specialized ETD or HCD fragmentation at high energy); (2) confirming disulfide bond connectivity; (3) localizing sites of post-translational or process-induced modifications; (4) verifying the sequence of custom peptides. Modern data analysis software performs automated de novo sequencing or database matching to confirm peptide identity.</p></div>

<div class="faq-item"><h3>Q: How do MALDI-TOF and LC-ESI-MS complement each other in peptide characterization?</h3><p class="faq-answer">A: MALDI-TOF provides rapid (seconds per sample) mass confirmation with tolerance to salts and buffers that would suppress ESI, making it ideal for monitoring SPPS coupling reactions in real time and for quick purity checks. It predominantly produces [M+H]⁺ ions, generating simple, easily interpretable spectra. LC-ESI-MS provides chromatographic separation of peptide components, higher mass accuracy (sub-ppm on Orbitrap instruments), and the ability to collect MS/MS spectra on each component for detailed characterization. The combination of both methods provides orthogonal information: MALDI gives a quick snapshot of the sample composition, while LC-ESI-MS provides the detailed, quantitative purity and identity assessment that supports the Certificate of Analysis. For [RPL Peptides](https://rplpeptides.com), LC-ESI-MS on a high-resolution instrument is the primary identity confirmation method.</p></div>

## References

1. Fenn JB, Mann M, Meng CK, Wong SF, Whitehouse CM. Electrospray ionization for mass spectrometry of large biomolecules. *Science*. 1989;246(4926):64–71. doi:10.1126/science.2675315

2. Karas M, Hillenkamp F. Laser desorption ionization of proteins with molecular masses exceeding 10,000 daltons. *Anal Chem*. 1988;60(20):2299–2301. doi:10.1021/ac00171a028

3. Makarov A. Electrostatic axially harmonic orbital trapping: a high-performance technique of mass analysis. *Anal Chem*. 2000;72(6):1156–1162. doi:10.1021/ac991131p

4. Zubarev RA, Makarov A. Orbitrap mass spectrometry. *Anal Chem*. 2013;85(11):5288–5296. doi:10.1021/ac400154s

5. Biemann K. Contributions of mass spectrometry to peptide and protein structure. *Biomed Environ Mass Spectrom*. 1988;16(1-12):99–111. doi:10.1002/bms.1200160119

6. Roepstorff P, Fohlman J. Proposal for a common nomenclature for sequence ions in mass spectra of peptides. *Biomed Mass Spectrom*. 1984;11(11):601. doi:10.1002/bms.1200111102

7. Syka JEP, Coon JJ, Schroeder MJ, Shabanowitz J, Hunt DF. Peptide and protein sequence analysis by electron transfer dissociation mass spectrometry. *Proc Natl Acad Sci USA*. 2004;101(26):9528–9533. doi:10.1073/pnas.0402700101

8. Ma B, Zhang K, Hendrie C, et al. PEAKS: powerful software for peptide de novo sequencing by tandem mass spectrometry. *Rapid Commun Mass Spectrom*. 2003;17(20):2337–2342. doi:10.1002/rcm.1196

9. Lange V, Picotti P, Domon B, Aebersold R. Selected reaction monitoring for quantitative proteomics: a tutorial. *Mol Syst Biol*. 2008;4:222. doi:10.1038/msb.2008.61

10. Apffel A, Fischer S, Goldberg G, Goodley PC, Kuhlmann FE. Enhanced sensitivity for peptide mapping with electrospray liquid chromatography–mass spectrometry in the presence of signal suppression due to trifluoroacetic acid-containing mobile phases. *J Chromatogr A*. 1995;712(1):177–190. doi:10.1016/0021-9673(95)00575-X

11. Hunt DF, Yates JR, Shabanowitz J, Winston S, Hauer CR. Protein sequencing by tandem mass spectrometry. *Proc Natl Acad Sci USA*. 1986;83(17):6233–6237. doi:10.1073/pnas.83.17.6233

12. Aebersold R, Mann M. Mass spectrometry-based proteomics. *Nature*. 2003;422(6928):198–207. doi:10.1038/nature01511

13. Domon B, Aebersold R. Mass spectrometry and protein analysis. *Science*. 2006;312(5771):212–217. doi:10.1126/science.1124619

14. McLafferty FW. Tandem mass spectrometry. *Science*. 1981;214(4518):280–287. doi:10.1126/science.7280693

15. Olsen JV, Macek B, Lange O, et al. Higher-energy C-trap dissociation for peptide modification analysis. *Nat Methods*. 2007;4(9):709–712. doi:10.1038/nmeth1060
