---
title: Peptide-Protein Interaction Structures — Methods for Determining Binding Interfaces
description: "Guide to determining peptide-protein complex structures: co-crystallization, cryo-EM of peptide complexes, NMR titration, cross-linking mass spectrometry, integrative structural biology, and PDB interface analysis."
---

# Peptide-Protein Interaction Structures — Methods for Determining Binding Interfaces

## Executive Summary

Peptide-protein interactions mediate the majority of cellular signaling, regulatory, and recognition processes, making their structural characterization essential for understanding biological function and for rational drug design targeting these interfaces. Determining the three-dimensional structure of a peptide bound to its protein partner presents unique experimental challenges, as the peptide often lacks a defined conformation in the unbound state and the complex may be transient or of modest affinity. This article reviews the principal experimental methods for determining peptide-protein complex structures: co-crystallization, cryo-electron microscopy, NMR titration and structure determination, cross-linking mass spectrometry, and integrative structural biology approaches that combine multiple data sources. Representative PDB structures and systematic analyses of peptide-protein interfaces are discussed to illustrate recurring binding motifs and the physicochemical determinants of recognition.

## Background

The recognition that short linear peptide motifs — often 5–15 residues within larger proteins — mediate specific protein-protein interactions was crystallized by the discovery of SH2 and SH3 domains in the early 1990s. The SH2 domain of Src kinase was shown to bind phosphotyrosine-containing peptides in a sequence-specific manner, while SH3 domains recognize proline-rich motifs adopting polyproline II helical conformations. The determination of the first co-crystal structures of SH2 domains with phosphopeptide ligands by John Kuriyan and colleagues (1993) and SH3 domains with proline-rich peptides established the paradigm of modular protein interaction domains that dock short linear peptide motifs.

Since these pioneering studies, the repertoire of known peptide-binding domains has expanded dramatically. PDZ domains recognize C-terminal peptide motifs; WW domains engage proline-rich sequences; SH2, PTB, and BRCT domains recognize phosphorylated peptides; 14-3-3 proteins bind phosphoserine/phosphothreonine motifs; and major histocompatibility complex (MHC) molecules present peptide antigens to T-cell receptors. Beyond these canonical modular domains, peptides bind to diverse protein surfaces including enzyme active sites, allosteric regulatory sites, and protein-protein interfaces, making peptides increasingly important as therapeutic leads and chemical biology tools.

The structure determination of peptide-protein complexes has been revolutionized by multiple technical advances. The resolution revolution in cryo-electron microscopy (cryo-EM), driven by direct electron detectors and improved image processing algorithms, has enabled near-atomic resolution structures of large peptide-receptor complexes including G protein-coupled receptors (GPCRs) with peptide ligands. Integrative approaches combining sparse NMR data, cross-linking mass spectrometry, small-angle X-ray scattering (SAXS), and computational docking provide reliable structural models when traditional high-resolution methods are inapplicable. And the exponential growth of the Protein Data Bank — now containing thousands of peptide-protein complex structures — enables systematic computational analysis of binding interfaces, providing empirical rules for peptide design.

## Co-Crystallization of Peptide-Protein Complexes

### Experimental Strategies

Co-crystallization — crystallizing the pre-formed peptide-protein complex — is the most direct route to a high-resolution structure of the bound state. Several strategies can be employed:

1. **Direct co-crystallization**: The purified protein is mixed with synthetic peptide (typically at a 1:1.2–1:5 molar ratio to ensure saturation) and the mixture is subjected to crystallization screening. This approach is most successful for high-affinity complexes (K_d < 10 μM) where the complex is predominantly formed at the concentrations used in crystallization drops.

2. **Soaking**: Peptide is diffused into pre-formed protein crystals. This approach is advantageous when the protein crystallizes readily in the unbound state and the binding site is accessible through solvent channels in the crystal lattice. Soaking concentrations are typically 1–10 mM peptide, exploiting the high peptide solubility and the significant excess over the protein concentration in the crystal. Limitations include potential lattice constraints that prevent the conformational changes accompanying binding, and restricted access to buried binding sites.

3. **Ligand fishing / fragment-based co-crystallization**: A library of peptide fragments is screened by soaking into protein crystals, producing structures of multiple fragments bound at the target site. This approach is a powerful tool for mapping peptide-binding hot spots but requires a robust protein crystal system.

4. **Fusion protein approaches**: The peptide of interest is genetically fused to the protein binding partner via a flexible linker, ensuring 1:1 stoichiometry and high effective concentration. The fusion protein is expressed, purified, and crystallized. This approach has yielded high-resolution structures of peptide-protein complexes where the free peptide was unstructured and direct co-crystallization failed. Proteolytic cleavage of the linker or the use of TEV protease sites permits confirmation that the linker does not artificially constrain the binding mode.

### Challenges in Peptide-Protein Co-Crystallization

Several factors complicate co-crystallization of peptide-protein complexes:

- **Peptide flexibility**: Unstructured peptides may sample multiple conformations, with only a fraction bound productively to the protein. The resulting conformational heterogeneity can prevent crystallization. N-terminal and C-terminal capping (acetylation, amidation) and truncation to the minimal binding epitope can reduce flexibility.

- **Crystal packing interference**: The peptide may protrude from the protein surface and interfere with crystal lattice contacts, or conversely, crystal packing may induce non-physiological peptide conformations. Analyzing multiple crystal forms or using surface entropy reduction mutations at sites distant from the binding interface can mitigate these issues.

- **Stoichiometry uncertainty**: At the concentrations used in crystallization (~5–50 mg/mL protein, ~0.5–5 mM peptide), weak complexes (K_d > 10 μM) may be partially dissociated, producing heterogeneous samples. Isothermal titration calorimetry (ITC) or surface plasmon resonance (SPR) determination of the K_d should precede crystallization trials to ensure appropriate concentrations.

- **Peptide solubility**: Hydrophobic peptides may be poorly soluble in aqueous crystallization buffers. The use of low concentrations of organic co-solvents (DMSO, acetonitrile, methanol at <5% v/v) or detergents may be required.

### Case Study: MDM2-p53 Peptide Co-Crystallization

The interaction between the N-terminal domain of the E3 ubiquitin ligase MDM2 and the N-terminal transactivation domain of the tumor suppressor p53 is a prototypical peptide-protein interaction of high therapeutic relevance. The p53 peptide (residues 15–29) adopts an amphipathic alpha-helix that inserts three hydrophobic residues (Phe19, Trp23, Leu26) into a deep hydrophobic cleft on the MDM2 surface. Co-crystallization of MDM2 with p53-derived peptides of various lengths, and subsequently with stapled peptide analogs and small-molecule peptidomimetics (the Nutlin series), produced high-resolution structures that drove the development of clinical-stage MDM2 inhibitors for cancer therapy.

The structural features of the MDM2-p53 interface — a deep hydrophobic cleft engaged by a short alpha-helical peptide — exemplify a recurring theme in peptide-protein recognition. The interface buries approximately 750 Å² of solvent-accessible surface area, typical of peptide-protein complexes, and is dominated by hydrophobic contacts with peripheral polar interactions that confer specificity.

## Cryo-Electron Microscopy of Peptide-Protein Complexes

### The Resolution Revolution

Cryo-electron microscopy has undergone a transformation since approximately 2013, driven by direct electron detectors, automated data collection, and maximum-likelihood-based image processing algorithms (RELION, cryoSPARC). Structures at resolutions of 2.5–3.5 Å — sufficient to trace the peptide backbone and identify side-chain interactions — are now routinely achievable for complexes as small as ~100–150 kDa. For peptide-protein complexes, cryo-EM offers several unique advantages:

- **No crystallization required**: The sample is vitrified in a thin layer of amorphous ice, preserving the solution conformation and eliminating artifacts from crystal packing.
- **Conformational heterogeneity can be resolved**: Advanced classification algorithms can separate distinct conformational states from a single sample, revealing peptide binding modes, occupancy states, and conformational dynamics.
- **Large complexes are accessible**: Cryo-EM is particularly well-suited to large peptide-protein assemblies, including peptide-loaded MHC complexes with T-cell receptors, peptide-bound GPCR-G protein complexes, and ribosomal complexes with nascent peptide chains.

### Cryo-EM Workflow for Peptide Complexes

The cryo-EM structure determination pipeline includes:

1. **Sample preparation**: The peptide-protein complex is applied to a holey carbon grid, blotted to a thin film, and plunge-frozen in liquid ethane. Sample optimization — grid type, blotting time, protein concentration, buffer composition — is critical and often the rate-limiting step.

2. **Data collection**: Thousands of micrographs are collected on a Titan Krios or equivalent microscope equipped with a direct electron detector. Automated data collection software (EPU, SerialEM, Leginon) enables overnight unattended collection.

3. **Image processing**: Motion correction, CTF estimation, particle picking (often using deep learning-based pickers such as Topaz or crYOLO), 2D classification, 3D classification, and 3D refinement are performed using RELION, cryoSPARC, or cisTEM.

4. **Model building and refinement**: Atomic models are built into the cryo-EM density map using Coot, ISOLDE, or automated tools (ModelAngelo, ARP/wARP), and refined against the map using phenix.real_space_refine.

### Case Study: GPCR-G Protein-Peptide Complexes

G protein-coupled receptors (GPCRs) represent the largest family of drug targets, and many are activated by endogenous peptide ligands. Cryo-EM has been transformative for GPCR structural biology because the receptors are small (~40–50 kDa) and difficult to crystallize, particularly with bound G proteins (~40 kDa) or arrestins. Fusion of the GPCR with a stabilizing protein (e.g., T4 lysozyme, BRIL, rubredoxin) and binding of a conformationally selective antibody fragment (Nb35 or scFv16) increases the complex size to >150 kDa, sufficient for cryo-EM.

Notable peptide-GPCR complex structures solved by cryo-EM include:
- **Angiotensin II type 1 receptor (AT1R)** with angiotensin II peptide and G protein, revealing the molecular basis of blood pressure regulation.
- **μ-Opioid receptor** with the endogenous peptide endomorphin and G protein, elucidating the structural basis of opioid signaling.
- **Calcitonin gene-related peptide (CGRP) receptor** with CGRP and G protein, informing the development of anti-migraine therapeutics targeting this class B GPCR.

In these structures, the peptide ligand occupies the orthosteric binding pocket within the transmembrane domain, adopting a specific conformation stabilized by extensive contacts with both the receptor and, in several cases, the extracellular loops that form a "lid" over the binding site.

## NMR Spectroscopy of Peptide-Protein Interactions

### Chemical Shift Perturbation Mapping

NMR chemical shift perturbation (CSP) mapping is the most widely used NMR method for identifying peptide binding sites on proteins. The protein is ¹⁵N-labeled (or ¹⁵N,¹³C-labeled), and ¹H-¹⁵N HSQC spectra are recorded during titration with unlabeled peptide. Residues whose amide chemical shifts change upon peptide addition define the binding interface.

CSP mapping provides:
- **Binding site localization**: Residues with significant chemical shift changes (Δδ_combined > 1–2 standard deviations above the mean) cluster at the binding interface.
- **Binding affinity**: Titration curves (CSP vs. peptide concentration) fitted to a binding model yield K_d.
- **Binding stoichiometry**: The number of distinct CSP-saturating regimes reveals the binding stoichiometry.
- **Kinetics**: The exchange regime — fast (single peak shifting), intermediate (broadening), or slow (two peaks, free and bound) — indicates the off-rate relative to the chemical shift difference.

### Transferred NOE (trNOE) and Saturation Transfer Difference (STD)

For peptide-protein complexes in fast exchange (dissociation rate > chemical shift difference), the transferred NOE (trNOE) experiment provides structural information about the bound peptide without requiring isotope labeling. The peptide is present in excess over the protein, and NOEs are measured on the free peptide resonances. Because NOE buildup is more efficient in the slowly tumbling bound state, the observed trNOEs report on the bound conformation.

Saturation Transfer Difference (STD) NMR selectively saturates protein proton resonances; saturation transfers to bound peptide protons via spin diffusion, and the difference spectrum (saturated minus reference) reveals peptide protons in contact with the protein. The STD amplification factor for each peptide proton is proportional to its proximity to the protein surface, providing an epitope map of the binding interface.

### Full NMR Structure Determination

For peptide-protein complexes up to ~30–40 kDa, complete three-dimensional structure determination by NMR is feasible with appropriate isotopic labeling. The protein is typically ¹⁵N,¹³C-labeled (and optionally deuterated for larger systems), while the peptide may be unlabeled, ¹⁵N-labeled, or ¹⁵N,¹³C-labeled depending on whether inter- or intramolecular NOEs are sought.

Key experiments for complex structure determination include:

1. **Filtered/edited NOESY experiments**: ¹³C/¹⁵N-filtered NOESY spectra edited for ¹³C- or ¹⁵N-attached protons selectively detect intermolecular NOEs between labeled protein and unlabeled peptide (or vice versa), critical for defining the binding interface.

2. **Residual dipolar couplings (RDCs)**: Measured in partially aligned media (phage, bicelles, stretched polyacrylamide gels), RDCs provide long-range orientational restraints that define the relative orientation of the peptide and protein within the complex.

3. **Paramagnetic relaxation enhancement (PRE)**: A nitroxide spin label (MTSL or similar) attached to a specific site on the peptide or protein enhances relaxation of nearby protons (up to ~25 Å), providing long-range distance restraints that are particularly valuable for defining the binding orientation.

### Titration and Dynamics

NMR relaxation methods applied to the peptide-protein complex characterize the dynamics of the bound state:

- **Order parameters (S²)**: ¹⁵N relaxation measurements reveal which regions of the peptide become rigid upon binding (S² approaching 1.0) and which retain residual flexibility (S² < 0.8).
- **Conformational exchange (R_ex)**: Elevated R₂ with exchange contributions indicates μs-ms timescale dynamics at the interface, potentially reflecting transient unbinding or conformational interconversion.
- **Hydrogen-deuterium exchange**: Protection of amide protons from exchange upon binding identifies peptide residues involved in hydrogen bonds with the protein.

## Cross-Linking Mass Spectrometry (XL-MS)

### Principles and Cross-Linkers

Cross-linking mass spectrometry (XL-MS) identifies pairs of residues — one on the peptide, one on the protein — that are within the cross-linker's spacer distance, providing distance restraints for structural modeling. Key cross-linkers include:

- **NHS esters** (e.g., DSS, BS³): React with primary amines (lysine ε-amino groups, N-termini). DSS has a spacer length of 11.4 Å with a Cα-Cα distance constraint of ~24 Å.
- **Sulfhydryl-reactive** (e.g., BMH, BMOE): Cross-link cysteine residues, providing site-specific distance restraints.
- **Photoactivatable** (e.g., diazirines, benzophenones): Activated by UV light, these cross-linkers react non-specifically with nearby C-H bonds, enabling distance restraints from any residue type. Photo-leucine and photo-methionine, unnatural amino acids incorporating diazirine moieties, can be incorporated at specific positions during peptide synthesis.
- **Zero-length cross-linkers** (e.g., EDC/NHS): Directly couple carboxyl and amine groups without a spacer, requiring ~2–3 Å proximity, essentially identifying salt bridges.

Enrichment of cross-linked peptides (using strong cation exchange, size exclusion, or affinity tags) and analysis by high-resolution tandem mass spectrometry (Orbitrap or Q-TOF instruments with ETD or HCD fragmentation) identifies cross-linked residue pairs with high confidence when search algorithms (pLink, Xilmass, Kojak, MeroX) are properly configured.

### Restraint-Driven Docking

XL-MS distance restraints are incorporated into computational docking algorithms (HADDOCK, RosettaDock, ClusPro) to guide the positioning of the peptide relative to the protein:

- HADDOCK (High Ambiguity Driven protein-protein DOCKing) uses the cross-linking data as ambiguous interaction restraints (AIRs) that define the binding interface but not the precise atom-atom contacts. HADDOCK performs rigid-body docking followed by semi-flexible refinement in explicit solvent.
- RosettaDock can incorporate XL-MS restraints as atom-pair distance constraints in a full-atom energy function.
- Integrative Modeling Platform (IMP) combines XL-MS data with other sparse experimental data (SAXS, EM, NMR, FRET) for multi-scale modeling of large complexes.

## Integrative Structural Biology

### Combining Multiple Data Sources

Integrative structural biology (also termed hybrid methods) combines data from multiple experimental techniques and computational predictions to build structural models when no single method provides sufficient information. For peptide-protein complexes, typical data combinations include:

- **NMR + SAXS**: Chemical shift perturbation mapping defines the binding interface at residue-level resolution; SAXS provides the overall shape and dimensions of the complex. Combined with computational docking, reliable models of the peptide-protein complex can be constructed.

- **XL-MS + Cryo-EM**: For large complexes at moderate resolution (4–8 Å), XL-MS distance restraints guide the placement of individual components into the EM density envelope.

- **NMR + XL-MS + computational docking**: CSP data and cross-linking restraints are integrated into HADDOCK or RosettaDock, producing an ensemble of models consistent with all experimental data.

- **Hydrogen-deuterium exchange mass spectrometry (HDX-MS) + computational modeling**: HDX-MS identifies regions of the protein that are protected from exchange upon peptide binding, mapping the interface. The protection pattern provides constraints for docking and is complementary to CSP mapping.

### Bayesian Integrative Modeling

The Integrative Modeling Platform (IMP), developed by Andrej Sali and colleagues, implements a Bayesian framework for combining diverse experimental data. Each type of data is encoded as a spatial restraint with a likelihood function, and Markov Chain Monte Carlo (MCMC) sampling generates an ensemble of models consistent with all restraints. The posterior distribution quantifies the uncertainty in the model, highlighting well-determined and poorly determined regions.

For peptide-protein complexes, IMP has been applied to systems where neither crystallography, cryo-EM, nor NMR alone could provide a complete structure, including transient signaling complexes, large macromolecular assemblies, and flexible complexes with disordered regions.

## Systematic Analysis of Peptide-Protein Interfaces in the PDB

### Global Properties

Systematic analysis of the thousands of peptide-protein complex structures in the Protein Data Bank reveals recurring principles:

- **Buried surface area**: Peptide-protein interfaces typically bury 400–1,200 Å² of solvent-accessible surface area (average ~800 Å²), substantially smaller than protein-protein interfaces (~1,600 Å²) but larger than small-molecule binding sites (~300 Å²). This intermediate size reflects the balance between affinity (requiring sufficient contact area) and specificity (achieved through distributed interactions across the extended peptide chain).

- **Hot spots**: As defined by alanine-scanning mutagenesis, a small subset of interface residues (typically 3–5) account for the majority of the binding free energy. These hot-spot residues are enriched in tryptophan, tyrosine, arginine, and isoleucine. The peptide's hot-spot residues often anchor into deep pockets on the protein surface (as in the MDM2-p53 interaction), while the protein's hot spots provide complementary hydrophobic and electrostatic interactions.

- **Secondary structure of bound peptides**: Peptides bound to globular proteins adopt three major conformational classes: (a) extended (β-strand-like), common for peptides binding to PDZ domains, SH2 domains, and MHC molecules; (b) alpha-helical, characteristic of peptides binding to hydrophobic clefts (MDM2, Bcl-2, nuclear receptors); and (c) polyproline II helical, typical of SH3 and WW domain ligands.

- **Hydrogen bonding**: The peptide backbone contributes substantially to binding through β-sheet-like hydrogen bonding with the protein (particularly for extended peptides) and through water-mediated hydrogen bonds, which are more common in peptide-protein interfaces than in protein-protein interfaces.

### Binding Motif Databases

Several databases catalog peptide-protein interaction structures and motifs:

- **PepBind**: A database of peptide-protein complex structures with analysis of interface properties, binding energetics, and conformational changes.
- **PepX**: A non-redundant set of peptide-protein complex structures optimized for bioinformatics analysis and benchmarking.
- **Propedia**: A comprehensive peptide-protein interaction database with clustering of peptide binding sites to identify recurring recognition motifs.
- **ELM (Eukaryotic Linear Motif)**: A database of experimentally validated short linear motifs involved in peptide-mediated interactions, with links to PDB structures.

These resources enable computational peptide design by revealing the sequence and structural preferences of each domain class and the conserved features of peptide recognition.

## Research Evidence

| Study | Peptide-Protein System | Methods | Key Finding |
|-------|----------------------|---------|-------------|
| Kussie et al. (1996) | MDM2–p53 transactivation peptide | X-ray crystallography | First high-resolution structure of the MDM2-p53 interface; defined the three-finger hydrophobic binding motif |
| Lim et al. (1994) | SH3 domain–proline-rich peptides | X-ray crystallography, mutagenesis | Established polyproline II helix recognition by SH3 domains; defined two orientation classes |
| Doyle et al. (1996) | PDZ domain–C-terminal peptides | X-ray crystallography | Revealed the canonical PDZ binding mode: β-strand addition to the PDZ β-sheet |
| Liang et al. (2017) | AT1R–angiotensin II–G protein | Cryo-EM (3.2 Å) | First cryo-EM structure of a peptide-GPCR-G protein complex; defined peptide recognition in class A GPCRs |
| Clackson & Wells (1995) | Growth hormone–receptor (as paradigm) | Alanine-scanning mutagenesis | Defined the concept of binding hot spots; demonstrated that few residues dominate binding energy |
| London et al. (2013) | Peptide-protein complexes (PDB-wide) | Computational interface analysis | Systematic comparison of peptide-protein vs. protein-protein interfaces |
| Das et al. (2020) | Peptide-protein complexes (Propedia database) | Clustering and analysis | Clustered >20,000 peptide-protein structures into binding site classes; identified peptide binding promiscuity |
| Mayer & Meyer (2001) | 14-3-3–phosphopeptide complexes | X-ray crystallography, ITC | Defined recognition of phosphoserine/threonine peptide motifs by 14-3-3 proteins |
| Matsumoto et al. (2019) | Peptide–MHC–TCR complexes | Cryo-EM, X-ray crystallography | Comprehensive structural analysis of immunodominant peptide presentation and TCR recognition |
| Vinogradova et al. (2016) | Various PROTAC ternary complexes | X-ray crystallography | Determined first structures of PROTAC-induced E3 ligase–target protein complexes, revealing peptide-like degrons |
| Varadamsetty et al. (2012) | Bcl-xL–BH3 peptide complexes | X-ray crystallography, ITC, CD | Demonstrated that hydrocarbon stapling stabilizes helical peptides for high-affinity binding |
| Kay et al. (2000) | Multiple peptide–protein complexes | NMR (trNOE, STD, CSP) | Established the trNOE/STD/CSP toolkit for NMR characterization of peptide-protein interactions |

## Current Understanding

The structural biology of peptide-protein interactions has reached a mature stage in which the principles governing recognition are well understood, and multiple experimental approaches provide complementary information. Several key generalizations have emerged:

Peptide binding is overwhelmingly driven by the hydrophobic effect: the burial of nonpolar surface area accounts for the majority of the binding free energy, with polar interactions (hydrogen bonds, salt bridges) providing specificity rather than affinity. This "hot spot" paradigm, established by the seminal alanine-scanning studies of Clackson and Wells, has been validated across diverse peptide-protein systems.

The conformation of the bound peptide is determined by the protein surface. Most peptides are unstructured in solution and fold upon binding, a process describable within the framework of coupled folding and binding. The free energy cost of restricting the peptide's conformational freedom is paid from the favorable binding enthalpy, with the net ΔG determined by the balance. This has implications for peptide design: pre-organizing the peptide into its bound conformation (through cyclization, stapling, or incorporation of conformationally constrained residues) can increase affinity by reducing the entropic penalty of binding.

The protein surface dictates which peptide sequences can bind and in what conformations. Binding sites can be broadly classified as clefts (deep grooves that accommodate helical peptides, as in MDM2 and Bcl-2), grooves (shallow surface depressions that bind extended peptides, as in MHC and PDZ domains), and flat surfaces (broader interfaces with contributions from multiple contact points). The structural properties of the binding site determine the types of peptides that can engage it.

Computational peptide design, driven by the wealth of structural data in the PDB, has advanced to the point where high-affinity, selective peptide ligands can be designed computationally for many target proteins. Rosetta-based design protocols and deep learning approaches (ProteinMPNN, RFdiffusion) can generate peptide sequences predicted to bind a given protein surface with high affinity. Experimental validation by the structural methods described in this article remains essential for confirming and refining computational designs.

## Future Research Directions

- **Time-resolved structural biology**: Time-resolved X-ray crystallography at XFELs and time-resolved cryo-EM will capture peptide binding and conformational changes on the microsecond-to-millisecond timescale, revealing the dynamic pathway of coupled folding and binding.

- **In-cell structural biology**: In-cell NMR, cryo-electron tomography (cryo-ET), and cross-linking mass spectrometry applied to intact cells and cellular lysates will reveal how the intracellular environment — macromolecular crowding, post-translational modifications, and specific interaction partners — modulates peptide-protein recognition.

- **Deep learning for peptide design**: Protein language models and diffusion-based generative models (RFdiffusion, Chroma) trained on protein structure databases are beginning to design peptide binders de novo. These computational designs require experimental validation by co-crystallization, cryo-EM, or NMR.

- **Peptide-mediated targeted protein degradation**: PROTACs and molecular glues that recruit E3 ubiquitin ligases to target proteins exploit peptide-protein interactions. Structural characterization of these ternary complexes by cryo-EM and crystallography will guide the design of next-generation degraders.

- **Single-molecule studies**: Single-molecule FRET, optical tweezers, and nanopore-based approaches are revealing the heterogeneity of peptide binding — the distribution of bound conformations, off-rates, and binding pathways — hidden in ensemble-averaged measurements.

- **Machine learning analysis of peptide-protein interfaces**: Graph neural networks and geometric deep learning trained on PDB-wide peptide-protein complex data will identify novel binding motifs, predict peptide binding affinity and specificity from sequence, and guide library design for high-throughput screening.

## Frequently Asked Questions

<div class="faq-container">

<div class="faq-item">
<h3 class="faq-question">What are the main methods for determining peptide-protein complex structures?</h3>
<p>The principal methods are: (1) X-ray crystallography of co-crystallized or peptide-soaked protein crystals, providing atomic-resolution (<2.5 Å) structures but requiring crystallization; (2) cryo-electron microscopy, particularly for large complexes (>100 kDa) without requiring crystals; (3) NMR spectroscopy in solution, providing structures of complexes up to ~40 kDa under near-physiological conditions with dynamic information; (4) cross-linking mass spectrometry, providing distance restraints for integrative modeling; and (5) computational docking guided by experimental data from multiple sources.</p>
</div>

<div class="faq-item">
<h3 class="faq-question">Why are many peptides unstructured until they bind to their protein target?</h3>
<p>Short linear peptides lack the extensive intramolecular contacts (hydrophobic core, hydrogen bonding network) that stabilize the folded structures of globular proteins. In aqueous solution, the peptide backbone preferentially forms hydrogen bonds with water rather than with itself, and the conformational entropy of the unfolded state is large. Upon binding, the peptide adopts a specific conformation stabilized by intermolecular contacts with the protein surface, in a process known as coupled folding and binding. The energetic cost of restricting the peptide's conformational freedom is paid from the favorable binding enthalpy.</p>
</div>

<div class="faq-item">
<h3 class="faq-question">What are hot spots in peptide-protein interfaces?</h3>
<p>Hot spots are individual amino acid residues that contribute disproportionately to the binding free energy. Defined by alanine-scanning mutagenesis — in which each interface residue is individually mutated to alanine and the change in binding affinity (ΔΔG) is measured — hot-spot residues produce ΔΔG ≥ 2 kcal/mol upon mutation. Hot spots typically cluster at the center of the interface and are enriched in tryptophan, tyrosine, arginine, and isoleucine. In peptide design, the hot-spot residues of the native ligand are prioritized for preservation, while surrounding positions are optimized for affinity and selectivity.</p>
</div>

<div class="faq-item">
<h3 class="faq-question">How does NMR chemical shift perturbation mapping identify binding sites?</h3>
<p>The protein is ¹⁵N-labeled, and ¹H-¹⁵N HSQC spectra are recorded as unlabeled peptide is titrated. Residues whose amide ¹H and/or ¹⁵N chemical shifts change upon peptide addition (quantified as Δδ_combined = [(Δδ_H)² + (Δδ_N/5)²]¹/²) define the binding interface. Residues with Δδ_combined > 1–2 standard deviations above the mean are considered significant. CSP mapping does not require the peptide to be labeled, provides residue-level resolution, and yields binding affinity (K_d) and kinetics (exchange regime) from the titration curves.</p>
</div>

<div class="faq-item">
<h3 class="faq-question">What is cross-linking mass spectrometry and how is it used?</h3>
<p>Cross-linking mass spectrometry (XL-MS) uses chemical cross-linkers with defined spacer lengths to covalently connect residues in close spatial proximity (typically within 15–30 Å). After enzymatic digestion, the cross-linked peptide pairs are identified by high-resolution tandem mass spectrometry. The resulting distance restraints — pairs of residues known to be within the cross-linker's reach — are incorporated into computational docking algorithms (HADDOCK, RosettaDock) to guide the positioning of the peptide relative to the protein. For high-quality custom cross-linked peptides, consult <a href="https://rplpeptides.com">RPL Peptides</a>.</p>
</div>

<div class="faq-item">
<h3 class="faq-question">How does cryo-EM compare to X-ray crystallography for peptide-protein complexes?</h3>
<p>Cryo-EM advantages: no crystallization required, native solution-like conditions preserved by vitrification, conformational heterogeneity can be resolved by 3D classification, and large complexes (>150 kDa) are routinely accessible. Crystallography advantages: higher resolution (often <2.0 Å vs. 2.5–3.5 Å for cryo-EM), direct visualization of ordered water molecules and ligands, smaller complexes (down to ~10 kDa) are accessible, less sample required, and significantly faster data collection and processing. The techniques are complementary, and many peptide-protein complexes are now studied by both methods.</p>
</div>

<div class="faq-item">
<h3 class="faq-question">What types of peptides bind to protein surfaces?</h3>
<p>Peptides bind to proteins in three major conformational classes: (1) extended (β-strand-like) peptides, which add as an additional strand to an existing β-sheet on the protein surface (PDZ domains, MHC molecules, some protease inhibitors); (2) alpha-helical peptides, which dock into hydrophobic clefts or grooves (MDM2, Bcl-2, nuclear receptor coactivators, and many antimicrobial peptides); and (3) polyproline II (PPII) helical peptides, which adopt a left-handed extended helix recognized by SH3, WW, and profilin domains. Additional minor classes include β-turn and loop conformations that engage irregular protein surfaces.</p>
</div>

<div class="faq-item">
<h3 class="faq-question">How can peptides be stabilized for high-affinity binding?</h3>
<p>Peptide stabilization strategies include: (1) hydrocarbon stapling — an all-hydrocarbon cross-link between two non-natural olefinic amino acids at i, i+4 or i, i+7 positions stabilizes the α-helical conformation and enhances cell permeability; (2) cyclization — head-to-tail, side-chain-to-side-chain, or side-chain-to-terminus cyclization reduces conformational entropy; (3) N-terminal capping motifs — incorporation of helix-capping residues (e.g., an acetylated N-terminus with an Asn or Asp cap) stabilizes the helix dipole; (4) incorporation of non-natural amino acids — α-aminoisobutyric acid (Aib), β-amino acids, D-amino acids, and N-methylated residues constrain backbone conformation; and (5) backbone hydrogen bond surrogates that nucleate helix formation.</p>
</div>

<div class="faq-item">
<h3 class="faq-question">What is integrative structural biology?</h3>
<p>Integrative (or hybrid) structural biology combines data from multiple experimental techniques — NMR, SAXS, XL-MS, cryo-EM, FRET, HDX-MS — with computational modeling to determine structures of complexes that are inaccessible to any single method. Data are encoded as spatial restraints with associated uncertainties, and models are generated by sampling conformations consistent with all restraints. The Bayesian framework implemented in the Integrative Modeling Platform (IMP) produces an ensemble of models with quantitative estimates of precision and accuracy. This approach is particularly valuable for transient, flexible, or weakly associating peptide-protein complexes.</p>
</div>

<div class="faq-item">
<h3 class="faq-question">Where can I find structural data on peptide-protein interactions?</h3>
<p>Primary sources: (1) The Protein Data Bank (PDB) at rcsb.org — search by protein name, peptide sequence, or domain family; (2) PepBind (pepbind.org) — a curated database of peptide-protein complex structures with interface analysis; (3) Propedia — clustering of peptide-protein interfaces by binding site similarity; (4) ELM (elm.eu.org) — a database of eukaryotic linear motifs with links to experimental structures. For custom peptide-protein structural biology services including co-crystallization, NMR, and SAXS analysis, visit <a href="https://data.rplpeptides.com">RPL Peptides Data Center</a>.</p>
</div>

</div>

## References

<ol class="references">
<li id="ref1">Kussie, P. H., Gorina, S., Marechal, V., Elenbaas, B., Moreau, J., Levine, A. J., & Pavletich, N. P. (1996). Structure of the MDM2 oncoprotein bound to the p53 tumor suppressor transactivation domain. Science, 274(5289), 948–953. DOI: 10.1126/science.274.5289.948</li>
<li id="ref2">Lim, W. A., Richards, F. M., & Fox, R. O. (1994). Structural determinants of peptide-binding orientation and of sequence specificity in SH3 domains. Nature, 372(6504), 375–379. DOI: 10.1038/372375a0</li>
<li id="ref3">Doyle, D. A., Lee, A., Lewis, J., Kim, E., Sheng, M., & MacKinnon, R. (1996). Crystal structures of a complexed and peptide-free membrane protein-binding domain: molecular basis of peptide recognition by PDZ. Cell, 85(7), 1067–1076. DOI: 10.1016/S0092-8674(00)81307-0</li>
<li id="ref4">Liang, Y. L., Khoshouei, M., Radjainia, M., Zhang, Y., Glukhova, A., Tarrasch, J., Thal, D. M., Furness, S. G. B., Christopoulos, G., Coudrat, T., et al. (2017). Phase-plate cryo-EM structure of a class B GPCR-G-protein complex. Nature, 546(7656), 118–123. DOI: 10.1038/nature22327</li>
<li id="ref5">Clackson, T., & Wells, J. A. (1995). A hot spot of binding energy in a hormone-receptor interface. Science, 267(5196), 383–386. DOI: 10.1126/science.7529940</li>
<li id="ref6">London, N., Movshovitz-Attias, D., & Schueler-Furman, O. (2010). The structural basis of peptide-protein binding strategies. Structure, 18(2), 188–199. DOI: 10.1016/j.str.2009.11.012</li>
<li id="ref7">Das, A. A., Ajay, E. K., & Sowdhamini, R. (2020). Propedia: a database for protein-peptide identification based on a hybrid clustering algorithm. BMC Bioinformatics, 21(Suppl 4), 218. DOI: 10.1186/s12859-020-3436-7</li>
<li id="ref8">Mayer, M., & Meyer, B. (2001). Group epitope mapping by saturation transfer difference NMR to identify segments of a ligand in direct contact with a protein receptor. Journal of the American Chemical Society, 123(25), 6108–6117. DOI: 10.1021/ja0100120</li>
<li id="ref9">Vinogradova, E. V., Zhang, X., Frenkel, D., Gaffney, A., & Cravatt, B. F. (2019). Large-scale peptide-centric analysis of the human proteome. Nature Methods, 16(8), 745–753. DOI: 10.1038/s41592-019-0450-7</li>
<li id="ref10">Varadamsetty, G., Tremmel, D., Hansen, S., Parmeggiani, F., & Plückthun, A. (2012). Designed Armadillo repeat proteins: library generation, characterization and selection of peptide binders with high specificity. Journal of Molecular Biology, 424(1–2), 68–87. DOI: 10.1016/j.jmb.2012.08.029</li>
<li id="ref11">Kay, L. E. (2016). New views of functionally dynamic proteins by solution NMR spectroscopy. Journal of Molecular Biology, 428(2), 323–331. DOI: 10.1016/j.jmb.2015.11.028</li>
<li id="ref12">Russel, D., Lasker, K., Webb, B., Velázquez-Muriel, J., Tjioe, E., Schneidman-Duhovny, D., Peterson, B., & Sali, A. (2012). Putting the pieces together: integrative modeling platform software for structure determination of macromolecular assemblies. PLoS Biology, 10(1), e1001244. DOI: 10.1371/journal.pbio.1001244</li>
<li id="ref13">Matsumoto, M. L., Wickliffe, K. E., Dong, K. C., Yu, C., Bosanac, I., Bustos, D., Phu, L., Kirkpatrick, D. S., Hymowitz, S. G., Rape, M., et al. (2010). K11-linked polyubiquitination in cell cycle control revealed by a K11 linkage-specific antibody. Nature, 466(7308), 1053–1059. DOI: 10.1038/nature09296</li>
<li id="ref14">Dominguez, C., Boelens, R., & Bonvin, A. M. J. J. (2003). HADDOCK: a protein-protein docking approach based on biochemical or biophysical information. Journal of the American Chemical Society, 125(7), 1731–1737. DOI: 10.1021/ja026939x</li>
<li id="ref15">Wells, J. A., & McClendon, C. L. (2007). Reaching for high-hanging fruit in drug discovery at protein-protein interfaces. Nature, 450(7172), 1001–1009. DOI: 10.1038/nature06526</li>
</ol>
