---
title: X-Ray Crystallography of Peptides — Methods and Applications
description: "Comprehensive guide to peptide X-ray crystallography: crystallization techniques, synchrotron data collection, phasing methods, refinement strategies, and PDB deposition."
---

# X-Ray Crystallography of Peptides — Methods and Applications

## Executive Summary

X-ray crystallography remains the gold standard for determining three-dimensional structures of peptides and proteins at atomic or near-atomic resolution. The technique has been responsible for approximately 85% of the more than 200,000 structures deposited in the Protein Data Bank, making it the single most productive method in structural biology. For peptides in particular, successful structure determination requires specialized approaches to crystallization, which can be more challenging than for larger proteins due to the intrinsic flexibility and limited contact surface area of short polypeptide chains. This article reviews the complete crystallographic workflow for peptides, from crystal growth through data collection at synchrotron sources, phasing, refinement, and deposition.

## Background

The birth of protein crystallography is inseparable from the development of X-ray diffraction itself. Following Max von Laue's discovery of X-ray diffraction by crystals in 1912 and the formulation of Bragg's law by William Henry Bragg and William Lawrence Bragg in 1913, the first protein crystal diffraction pattern — from pepsin — was recorded by John Desmond Bernal and Dorothy Crowfoot Hodgkin in 1934. The first protein structures solved at atomic resolution — myoglobin by John Kendrew (1958) and hemoglobin by Max Perutz (1960) — required decades of effort, including the development of the multiple isomorphous replacement (MIR) phasing method.

For peptides, crystallography began with the determination of small model peptides and dipeptides in the 1950s and 1960s. These early structures were instrumental in validating Pauling's predicted secondary structure geometries and in defining the conformational preferences of individual amino acids. The structures of glycyl-L-alanine, L-alanyl-L-alanine, and other dipeptides were among the first peptide crystals analyzed, providing foundational data for the Ramachandran plot and modern computational chemistry force fields.

The last two decades have seen dramatic technological advances that have transformed peptide crystallography. Synchrotron radiation sources now deliver X-ray beams of exceptional brilliance and tunability, enabling data collection from microcrystals (<10 μm) that were previously intractable. The development of cryocrystallography (flash-cooling crystals to 100 K) has virtually eliminated radiation damage as a limiting factor. Phasing methods have expanded from traditional MIR to include multiwavelength anomalous diffraction (MAD), single-wavelength anomalous diffraction (SAD), and molecular replacement (MR), the latter now dominant due to the availability of accurate search models from AlphaFold2 and related prediction algorithms.

## Crystallization of Peptides

### Fundamental Principles

Peptide crystallization is a phase transition from a supersaturated solution to an ordered solid state. The process involves two stages: nucleation (formation of critical nuclei) and growth (addition of molecules to nuclei). The phase diagram for crystallization maps concentration against a precipitating parameter (e.g., precipitant concentration, temperature, or pH), defining three regions: undersaturated (no crystal growth), metastable (growth without nucleation), and labile (spontaneous nucleation and growth). Successful crystallization requires reaching the nucleation zone transiently and then moving into the metastable zone for controlled growth.

### Hanging-Drop Vapor Diffusion

The hanging-drop method, introduced by David Davies and colleagues in the 1970s, remains the most widely used peptide crystallization technique. A small droplet (typically 1–5 μL) containing peptide solution mixed with an equal volume of reservoir solution is suspended from a siliconized glass coverslip sealed over a well containing 0.5–1.0 mL of reservoir solution. Water vapor diffuses from the drop (which initially has a lower precipitant concentration than the reservoir) to the reservoir, slowly increasing both peptide and precipitant concentrations in the drop until supersaturation is achieved.

Advantages of the hanging-drop method include:
- Slow, controlled equilibration through vapor diffusion.
- Visual monitoring through the transparent coverslip.
- Easy retrieval of crystals for mounting.
- Scalability with 24-well trays (VDX plates) for screening multiple conditions.

For peptides, common screening strategies employ sparse-matrix screens (e.g., Hampton Research Crystal Screen, JCSG+ Suite) or systematic grid screens varying PEG molecular weight, salt type, and buffer pH. Commercial screens specifically optimized for small molecules and peptides are available.

### Sitting-Drop Vapor Diffusion

The sitting-drop configuration positions the crystallization droplet in a concave well adjacent to the reservoir, rather than suspended above it. This arrangement is compatible with 96-well high-throughput crystallization platforms (e.g., sitting-drop Intelli-Plates or MRC 2-well plates) and robotic liquid handling systems capable of dispensing nanoliter volumes (100–500 nL). Sitting-drop screening dramatically reduces peptide consumption, a critical advantage when working with synthetic peptides that may be available in limited quantities.

The sitting-drop geometry also eliminates problems associated with drop detachment from coverslips and permits the use of optically clear tape or film sealing for automated imaging. Most large-scale crystallization facilities now employ sitting-drop robotics with automated imaging at regular intervals, coupled with machine learning-based crystal detection algorithms.

### Microbatch Under Oil

The microbatch method, developed by Naomi Chayen and colleagues, dispenses peptide and precipitant solutions directly under a layer of paraffin or silicone oil in a microtiter plate well. Unlike vapor diffusion, the oil layer prevents evaporation, producing a batch crystallization environment in which the peptide concentration is fixed at the time of setup. Supersaturation is achieved by mixing at higher starting concentrations than would be compatible with vapor diffusion.

The microbatch method offers several advantages for peptide crystallization:
- **Reduced convection**: The oil layer suppresses convective flow, favoring diffusion-limited growth and producing higher-quality crystals.
- **Kinetic control**: The absence of concentration changes during equilibration permits precise control over nucleation kinetics.
- **Screening at high concentrations**: Conditions that produce amorphous precipitation in vapor diffusion may yield crystals in microbatch due to different nucleation kinetics.
- **Compatibility with viscous additives**: Low-molecular-weight PEGs and oils can be incorporated directly.

### Specialized Techniques for Peptides

Peptides present unique crystallization challenges compared to globular proteins:

1. **Conformational flexibility**: Short peptides often sample multiple conformations in solution, preventing the homogeneous conformation required for crystallization. This can be addressed through the use of conformationally constrained peptide analogs (e.g., cyclic peptides, stapled peptides, or those incorporating α-aminoisobutyric acid or other Cα-tetrasubstituted residues) or by exploiting solvent conditions that favor a single predominant conformation.

2. **Limited contact surface area**: Peptides have a higher surface-to-volume ratio than proteins, providing fewer opportunities for crystal-packing contacts. Strategies to enhance crystallization include the addition of small-molecule ligands or metal ions that bridge symmetry-related molecules, the use of racemic crystallization (crystallization of a mixture of L- and D-peptide enantiomers), and fusion to crystallization chaperones.

3. **Racemic crystallography**: Introduced by the Kent laboratory, this approach exploits the fact that racemic mixtures of L- and D-peptides frequently crystallize in centrosymmetric space groups (e.g., P-1) that are inaccessible to homochiral peptides. The expanded repertoire of space groups increases the probability of successful crystallization, and centrosymmetric space groups simplify phasing.

4. **Seeding techniques**: Microseeding (introduction of crushed crystal fragments) or macroseeding (transfer of intact seed crystals) can rescue crystallization trials that exhibit excessive nucleation or fail to nucleate spontaneously. Streak-seeding, in which a whisker or fiber is drawn through a pre-equilibrated drop, is particularly effective for peptides.

## Synchrotron Data Collection

### Synchrotron Radiation Sources

Synchrotron radiation is produced when charged particles (electrons or positrons) traveling at relativistic speeds are accelerated by magnetic fields. Modern third-generation synchrotron sources — including the Advanced Photon Source (APS, USA), European Synchrotron Radiation Facility (ESRF, France), SPring-8 (Japan), Diamond Light Source (UK), and PETRA III (Germany) — provide X-ray beams with exceptional properties:

- **Brilliance**: Flux per unit source area per unit solid angle per unit bandwidth, typically 10¹⁶–10²⁰ photons/s/mm²/mrad²/0.1% bandwidth, several orders of magnitude greater than laboratory rotating-anode sources.
- **Tunability**: The ability to select any desired wavelength enables anomalous diffraction experiments (MAD/SAD) exploiting the absorption edges of selenium, sulfur, or incorporated heavy atoms.
- **Microfocus capability**: Beam sizes of 1–10 μm enable data collection from microcrystals that would produce negligible diffraction on a home source.
- **Low divergence**: The nearly parallel beam minimizes systematic errors in reflection positions.

For peptide crystallography, the tunability for sulfur-SAD phasing is particularly valuable, as the naturally occurring sulfur atoms in cysteine and methionine residues can serve as anomalous scatterers, eliminating the need for heavy-atom derivatization.

### Cryocrystallography

Modern macromolecular crystallography is predominantly performed at cryogenic temperatures (typically 100 K) to mitigate radiation damage. Peptide crystals are harvested from crystallization drops using cryoloops (nylon loops of 50–500 μm diameter), briefly transferred through a cryoprotectant solution (commonly 20–30% glycerol, ethylene glycol, or low-molecular-weight PEG), and flash-cooled in a liquid nitrogen gas stream or by direct plunging into liquid nitrogen.

Cryoprotection is critical for peptides, as their crystals often contain high solvent content (typically 30–70%) and are susceptible to ice formation during cooling. The cryoprotectant must be compatible with the crystallization conditions and must not dissolve or damage the crystals. Gradual transfer through increasing cryoprotectant concentrations may be necessary for sensitive peptide crystals.

### Data Collection Strategy

Optimal data collection for peptide crystals involves several interdependent decisions:

1. **Detector selection**: Hybrid photon-counting detectors (e.g., DECTRIS PILATUS, EIGER) offer zero readout noise, high dynamic range, and rapid frame rates, enabling fine-slicing strategies (0.1–0.2° oscillation per frame) that improve signal-to-noise ratios for weak reflections.

2. **Wavelength selection**: For native datasets without anomalous signal, wavelengths of 0.9–1.0 Å provide a good compromise between flux and absorption. For sulfur-SAD, longer wavelengths (1.5–2.0 Å) maximize the anomalous signal from sulfur (f" ≈ 0.5 e⁻ at 1.5 Å vs. 0.2 e⁻ at 1.0 Å), though absorption increases. Helium beam paths reduce air absorption at long wavelengths.

3. **Oscillation range**: The total rotation range should cover at least 180° (or 360° for anomalous data, to collect Friedel pairs with the same absorption path). For peptides in high-symmetry space groups, 90–120° may suffice.

4. **Dose management**: The deposited radiation dose must be controlled to avoid specific structural damage that precedes global degradation. For peptides, disulfide bonds, acidic residues (glutamate, aspartate), and methionine side chains are particularly radiosensitive.

5. **Data processing**: Modern pipelines (XDS, DIALS, HKL-3000, autoPROC) integrate automated indexing, integration, scaling, and merging. Key quality indicators include R-merge (or R-meas), I/σ(I), completeness, multiplicity, and CC₁/₂ (the correlation coefficient between random half-datasets, a sensitive indicator of resolution limits).

## Phasing Methods

### Molecular Replacement

Molecular replacement (MR) is the dominant phasing method when a sufficiently similar search model exists. The method, formulated by Michael Rossmann and David Blow in the 1960s, solves the crystallographic phase problem by placing a known structure (the search model) in the unit cell of the target crystal by rotation and translation operations.

For peptides, several scenarios arise:
- **Direct MR**: When the crystal contains the same peptide as a previously solved structure (e.g., from a related crystal form or a homolog).
- **Fragment-based MR**: Smaller fragments or individual residues can serve as search models. Programs such as ARCIMBOLDO use libraries of small ideal fragments (alpha-helices, polyalanine stretches) placed by maximum-likelihood MR and extended by density modification.
- **AlphaFold-assisted MR**: Predicted models from AlphaFold2 or RoseTTAFold, often of sufficient accuracy for MR, have dramatically expanded the scope of MR phasing. For peptide-protein complexes, an AlphaFold prediction of the binding partner can serve as a partial model, with the peptide located in difference density.
- **AMPLE**: This pipeline automatically generates search models by clustering and truncating distantly related structures.

The success of MR depends on the sequence identity and structural similarity between the search model and the target. A rule of thumb is that MR is straightforward above 40% sequence identity, feasible with modern likelihood-based methods (Phaser, MOLREP) at 25–40%, and challenging but sometimes successful below 25%. Phaser implements a maximum-likelihood framework that performs rotation and translation searches simultaneously when appropriate.

### Anomalous Diffraction Methods

**Single-wavelength Anomalous Diffraction (SAD)** has become the most widely used experimental phasing method. It exploits the anomalous scattering of specific atoms when the incident X-ray wavelength approaches their absorption edge. For peptides, the primary anomalous scatterers are:

- **Sulfur (cysteine, methionine)**: Sulfur-SAD is particularly attractive for peptides because it requires no chemical derivatization. However, the anomalous signal from sulfur is weak (f" ≈ 0.5 e⁻ at 1.8 Å), requiring highly redundant data (multiplicity > 50) and careful data processing to extract the signal.

- **Selenium (selenomethionine)**: For peptides that can be expressed recombinantly as fusion proteins, incorporation of selenomethionine provides a strong anomalous signal (f" ≈ 4 e⁻ at the Se K-edge, 0.9795 Å). While less common than for proteins, selenomethionine labeling of expressed peptide fusions followed by proteolytic release is feasible.

- **Halide ions (iodide, bromide)**: Soaking peptide crystals in solutions of KI or KBr can introduce anomalous scatterers at ordered solvent sites. Iodide (f" ≈ 7 e⁻ at Cu Kα) provides a strong signal on laboratory sources.

- **Heavy-atom derivatives**: Traditional derivatization with mercury, platinum, gold, or uranium compounds remains viable. The peptide's functional groups (cysteine thiols, histidine imidazoles, methionine thioethers) provide specific binding sites.

**Multi-wavelength Anomalous Diffraction (MAD)** collects data at multiple wavelengths around an absorption edge (typically peak, inflection, and remote) to maximize the dispersive and anomalous differences. While MAD produces higher-quality phases than SAD, it requires a tunable synchrotron beamline and greater radiation dose, making SAD the more practical choice for most peptide projects.

### Direct Methods

Direct methods, which derive phases from the statistical relationships among reflection intensities, are the standard approach for small-molecule crystallography (up to ~200 atoms in the asymmetric unit) but have historically been inapplicable to macromolecules due to the resolution requirement (typically 1.2 Å or better). However, for small peptides in favorable space groups diffracting to atomic resolution (<1.2 Å), direct methods implemented in programs such as SHELXD are viable.

Dual-space recycling algorithms (SHELXD, SHELXE), which alternate between real-space density modification and reciprocal-space phase refinement, have extended the size limit of direct methods to approximately 1,000 atoms. These methods are particularly effective for peptides because:
- Peptide crystals often diffract to higher resolution than protein crystals.
- The smaller asymmetric unit is within reach of direct methods.
- The combination of direct methods with density modification (the "Shake-and-Bake" approach) is robust.

## Structure Refinement

### Refinement Principles

Crystallographic refinement adjusts the atomic model to maximize agreement between calculated and observed structure factor amplitudes while satisfying prior chemical knowledge (bond lengths, bond angles, planarity, non-bonded contacts). The refinement target function typically combines a crystallographic residual (least-squares or maximum-likelihood) with geometric restraints:

E_total = w_X × E_X-ray + w_geom × E_geometry

For peptides refined at resolutions typical of macromolecular crystallography (1.0–2.5 Å), maximum-likelihood targets are preferred because they account for model errors and incompleteness. Programs such as REFMAC5, phenix.refine (from the PHENIX suite), and BUSTER are widely used.

### Refinement Strategies for Peptides

1. **Initial rigid-body refinement**: The entire peptide is refined as a rigid group (or as several groups corresponding to individual residues) to correct overall positioning. This is particularly important for MR solutions where the search model may be slightly displaced.

2. **Restrained refinement**: Individual atomic positions and isotropic B-factors are refined with stereochemical restraints. For high-resolution data, anisotropic B-factors (6 parameters per atom describing an ellipsoid of displacement) may be justified.

3. **Solvent modeling**: Ordered water molecules are identified from difference density (F_o − F_c) maps. The placement and validation of water molecules requires careful evaluation, particularly for peptides where solvent networks at crystal contacts may be functionally relevant.

4. **Alternative conformations**: Side chains (and occasionally the peptide backbone) may adopt multiple discrete conformations. Refinement packages can model alternative conformations with associated occupancies summing to 1.0.

5. **TLS refinement**: Translation/Libration/Screw refinement models rigid-body displacements of defined groups (individual residues, secondary structure elements, or the entire peptide), improving B-factor modeling at resolutions of approximately 1.5 Å and better.

### Validation

Refinement must be continuously cross-validated using R_free, which is calculated from a small subset of reflections (typically 5%) excluded from refinement. A gap between R_work and R_free exceeding ~7% indicates overfitting. Additional validation metrics include:
- **Ramachandran plot**: Percentage of residues in favored, allowed, and outlier regions.
- **Rotamer analysis**: Conformational preferences of side chains compared to a rotamer library.
- **Clashscore**: Number of unfavorable steric overlaps per 1,000 atoms.
- **MolProbity score**: A composite quality metric combining clashscore, Ramachandran outliers, and rotamer outliers.

For peptide structures, particular attention must be paid to the phi/psi angles of terminal residues, which are often less well defined due to flexibility and may adopt unusual conformations.

## PDB Deposition

### The wwPDB Deposition Pipeline

Structure deposition to the Protein Data Bank is managed by the worldwide Protein Data Bank (wwPDB) consortium, comprising the RCSB PDB (USA), PDBe (Europe), PDBj (Japan), and BMRB (NMR data). The deposition process involves:

1. **Data preparation**: Structure factor amplitudes (or intensities), final refined coordinates, and processing statistics must be collected. For peptide structures, the refinement program output logs provide the required statistics.

2. **Validation report**: The wwPDB validation pipeline generates a comprehensive report including geometric quality metrics, agreement between model and data, and comparisons with other structures. The report must be reviewed and any serious issues addressed.

3. **Metadata**: Detailed experimental metadata — crystallization conditions, data collection parameters, refinement protocol, and software versions — must be recorded.

4. **Ligand and modification descriptions**: Non-standard amino acids, chemical modifications (N-terminal acetylation, C-terminal amidation, phosphorylation, cyclization), and ligands require Chemical Component Dictionary entries. For novel peptide modifications, a chemical description including atom connectivity, bond orders, and ideal geometry must be provided.

5. **Release**: Structures can be held until publication (HPUB) or released immediately upon deposition. The PDB ID is assigned upon deposition and should be cited in the associated publication.

## Research Evidence

| Study | Peptide System | Resolution | Key Technique | Finding |
|-------|---------------|------------|---------------|---------|
| Karle & Karle (1963) | Leu-Pro-Gly cyclic peptide | 1.0 Å | Direct methods | First crystal structure of a tripeptide; validated predicted peptide bond geometry |
| Toniolo et al. (2001) | Aib-rich peptides (20 structures) | 0.9–1.2 Å | Direct methods + synchrotron | Comprehensive analysis of 3₁₀/α-helix preferences in Cα-tetrasubstituted peptides |
| Mandal et al. (2012) | Racemic heterochiral peptide | 1.0 Å | Racemic crystallization | Demonstrated that racemic crystallization expands accessible space groups |
| Usón et al. (2003) | Various (ARCIMBOLDO test set) | 1.0–2.0 Å | Fragment-based MR (ARCIMBOLDO) | Automated phasing using small ideal polyalanine fragments |
| Rose et al. (2015) | Natural and synthetic peptides | 2.0–2.8 Å | Sulfur-SAD at 1.8 Å | Demonstrated routine sulfur-SAD phasing for peptides with ≤4 sulfur atoms |
| Liebschner et al. (2019) | PHENIX test set | 1.5–3.5 Å | phenix.refine maximum-likelihood | Systematic comparison of refinement strategies and validation metrics |
| McCoy et al. (2007) | PDB-wide benchmark | Various | Phaser maximum-likelihood MR | Established automated MR pipeline now used in >80% of new PDB depositions |
| Sheldrick (2010) | Small peptides (SHELXD/E test) | 0.8–1.2 Å | Dual-space recycling (Shake-and-Bake) | Extended direct methods to ~1,000 atoms in the asymmetric unit |
| Karplus & Diederichs (2012) | Benchmark datasets | Various | CC₁/₂ analysis | Introduced CC₁/₂ as a robust resolution cutoff criterion, replacing I/σ(I) |
| Williams et al. (2018) | MolProbity validation set | Various | MolProbity analysis | Established the current wwPDB validation standards for geometry and clashscore |
| Kabsch (2010) | Benchmark datasets | Various | XDS data processing | Developed XDS, now one of the most widely used integration and scaling packages |
| Chayen & Saridakis (2008) | Various proteins and peptides | — | Microbatch review | Comprehensive review of crystallization under oil and its advantages |

## Current Understanding

X-ray crystallography of peptides has matured into a well-established pipeline capable of delivering atomic-resolution structures for a wide range of peptide systems. Several key principles are firmly established:

Crystallization remains the primary bottleneck. For peptides, the use of sparse-matrix screening at the nanoliter scale, combined with automated imaging, has dramatically improved the success rate. The recognition that peptide crystals often require substantially different conditions than protein crystals has led to the development of peptide-specific screening strategies and commercial screens.

Data collection at modern synchrotron beamlines is highly automated, with robotic sample changers, automated beam alignment, and real-time data analysis guiding the collection strategy. The practical lower limit for crystal size has decreased from ~50 μm a decade ago to ~1–5 μm with microfocus beamlines, though radiation damage imposes practical constraints.

Phasing by molecular replacement, facilitated by the availability of AlphaFold2-predicted models for virtually any protein or peptide sequence, has become the default method. Experimental phasing (SAD/MAD) is now reserved for cases where MR fails, though sulfur-SAD is increasingly used as a routine alternative when MR models are of insufficient quality.

The PDB now contains over 200,000 structures, of which a substantial fraction are peptide-containing (either as free peptides, peptide-protein complexes, or peptide ligands). This wealth of data has enabled systematic analyses of peptide conformational preferences, hydrogen bonding patterns, and crystal packing interactions, providing an empirical foundation for peptide design.

## Future Research Directions

- **Serial femtosecond crystallography (SFX)**: X-ray free-electron lasers (XFELs) such as the LCLS (USA), SACLA (Japan), and European XFEL (Germany) deliver femtosecond X-ray pulses of unprecedented brilliance, enabling data collection from nanocrystals and potentially from single particles, eliminating the need for large crystals entirely.

- **MicroED (microcrystal electron diffraction)**: The application of cryo-electron microscopy instrumentation to electron diffraction of peptide microcrystals, which are often too small for X-ray diffraction, is emerging as a powerful complementary technique with the advantage that electrons interact more strongly with matter, requiring smaller crystals.

- **Room-temperature data collection**: The growing recognition that cryogenic temperatures may introduce artifacts (altered side-chain conformations, suppressed dynamics) has renewed interest in room-temperature data collection using synchrotron and XFEL sources, enabled by advances in noise-free detectors and serial approaches.

- **Integrative pipelines**: Automated pipelines combining MR with AlphaFold2 predictions, density modification, and automated model building (e.g., ModelCraft, ARP/wARP, Buccaneer) promise to reduce the human effort in phasing and building to near-zero for well-behaved peptide crystals.

- **In situ diffraction**: Direct data collection from crystals in their crystallization drops eliminates the need for crystal harvesting and cryoprotection, reducing mechanical damage and enabling screening of fragile peptide crystals.

- **Dynamic crystallography**: Time-resolved crystallography at XFELs and synchrotrons, capable of capturing peptide conformational changes on femtosecond-to-millisecond timescales, will reveal the dynamic structural basis of peptide function and folding.

## Frequently Asked Questions

<div class="faq-container">

<div class="faq-item">
<h3 class="faq-question">Why is it harder to crystallize peptides than larger proteins?</h3>
<p>Peptides have a higher surface-to-volume ratio, providing fewer intermolecular contact points for crystal lattice formation. Their conformational flexibility means that multiple conformations coexist in solution, reducing the population of any single crystallizable species. Additionally, peptides lack the extensive hydrophobic cores that drive protein crystallization. Strategies to address these challenges include racemic crystallization, conformational constraint (cyclic or stapled peptides), and the use of small-molecule additives to promote lattice contacts.</p>
</div>

<div class="faq-item">
<h3 class="faq-question">What is the difference between hanging-drop and sitting-drop crystallization?</h3>
<p>Both are vapor diffusion methods. In hanging-drop, the crystallization drop is suspended from a coverslip over the reservoir; in sitting-drop, it rests in a well adjacent to the reservoir. Hanging-drop allows easy crystal retrieval, while sitting-drop is compatible with 96-well plates and robotic nanoliter dispensing systems. For peptides, initial screening is typically performed in sitting-drop format to conserve material, with optimization in hanging-drop format.</p>
</div>

<div class="faq-item">
<h3 class="faq-question">How does molecular replacement work?</h3>
<p>Molecular replacement places a known model structure (the "search model") in the unit cell of the target crystal by solving for the rotation (3 angles) and translation (3 coordinates) that maximize agreement between calculated and observed structure factor amplitudes. Modern implementations (Phaser, MOLREP) use maximum-likelihood statistics rather than traditional Patterson-based rotation and translation functions, providing greater sensitivity with weaker search models. For custom peptide structure determination services, visit <a href="https://rplpeptides.com">RPL Peptides</a>.</p>
</div>

<div class="faq-item">
<h3 class="faq-question">What resolution is considered "good" for a peptide crystal structure?</h3>
<p>For peptide structures, resolutions of 1.5 Å or better are common and considered high quality, permitting reliable placement of all atoms including solvent molecules. Resolutions of 1.0–1.2 Å approach atomic resolution, enabling refinement of anisotropic displacement parameters and, in favorable cases, visualization of hydrogen atoms in difference maps. Resolutions of 2.0–2.5 Å are adequate for determining backbone conformation and side-chain orientation but may leave some solvent and flexible regions poorly defined.</p>
</div>

<div class="faq-item">
<h3 class="faq-question">What is racemic crystallography and when is it useful?</h3>
<p>Racemic crystallography involves crystallizing a 1:1 mixture of L- and D-enantiomers of a peptide. Because the racemic mixture is centrosymmetric (each L-molecule has an equivalent D-molecule related by inversion), the crystals typically adopt centrosymmetric space groups such as P-1, which are inaccessible to homochiral peptides. This expands the repertoire of possible crystal forms and increases the probability of crystallization. Additionally, centrosymmetric space groups simplify phasing. The method was pioneered by the Kent laboratory and has been successfully applied to peptides up to ~50 residues.</p>
</div>

<div class="faq-item">
<h3 class="faq-question">How does sulfur-SAD phasing work?</h3>
<p>Sulfur-SAD exploits the anomalous scattering of sulfur atoms naturally present in cysteine and methionine residues. The anomalous signal (f") from sulfur is approximately 0.5 electrons at a wavelength of 1.8 Å, requiring highly redundant data (multiplicity >50) and precise measurement to extract the signal above noise. Modern hybrid photon-counting detectors and synchrotron beamlines with helium paths have made sulfur-SAD increasingly routine. The method eliminates the need for selenium incorporation or heavy-atom derivatization. Research-grade peptides optimized for structural studies are available from <a href="https://data.rplpeptides.com">RPL Peptides Data Center</a>.</p>
</div>

<div class="faq-item">
<h3 class="faq-question">What is the R-free and why is it important?</h3>
<p>R-free is a cross-validation metric calculated from a small subset of reflections (typically 5–10%) that are excluded from refinement. It provides an unbiased estimate of the agreement between the model and the data, whereas R-work (calculated from reflections used in refinement) can decrease artifactually due to overfitting. A gap between R-free and R-work exceeding 5–7% suggests overfitting. Modern refinement programs use R-free to guide the choice of weighting parameters between X-ray and geometric terms.</p>
</div>

<div class="faq-item">
<h3 class="faq-question">Can AlphaFold2 replace experimental crystallography for peptides?</h3>
<p>AlphaFold2 can predict peptide structures with remarkable accuracy when the peptide is part of a larger protein or forms a well-defined complex. However, for isolated short peptides, predictions are less reliable because the model has limited training data for conformational ensembles and may not capture the effects of specific solvent conditions, ligands, or crystal packing. Experimental structure determination remains essential for validating computational predictions and for applications requiring the highest accuracy, such as structure-based drug design.</p>
</div>

<div class="faq-item">
<h3 class="faq-question">What are the criteria for PDB deposition?</h3>
<p>The wwPDB requires: (1) atomic coordinates in PDB or mmCIF format; (2) structure factor amplitudes or intensities, processed and merged with associated statistics (completeness, R-merge, I/σ(I)); (3) experimental details including crystallization conditions, data collection parameters, and refinement protocol; (4) a satisfactory validation report with no major geometric or fit-to-data outliers. Structures must have been refined against experimental data; purely computational models (including AlphaFold2 predictions) are deposited separately to the ModelArchive.</p>
</div>

<div class="faq-item">
<h3 class="faq-question">How are peptide crystals cryoprotected?</h3>
<p>Cryoprotection involves transferring the peptide crystal through a solution containing 20–30% cryoprotectant (glycerol, ethylene glycol, low-molecular-weight PEG, MPD, or sucrose) before flash-cooling in liquid nitrogen or a nitrogen gas stream at 100 K. The cryoprotectant must be compatible with the crystallization conditions. For delicate peptide crystals, stepwise transfer through increasing cryoprotectant concentrations minimizes osmotic shock. Some crystallization conditions (high PEG, high salt) may be inherently cryoprotective.</p>
</div>

</div>

## References

<ol class="references">
<li id="ref1">Karle, I. L., & Karle, J. (1963). An application of a new phase determination procedure to the structure of cyclo(hexaglycyl)dimethyl ester. Acta Crystallographica, 16(10), 969–975. DOI: 10.1107/S0365110X63002653</li>
<li id="ref2">Toniolo, C., Crisma, M., Formaggio, F., & Peggion, C. (2001). Control of peptide conformation by the Thorpe-Ingold effect (Cα-tetrasubstitution). Peptide Science, 60(6), 396–419. DOI: 10.1002/1097-0282(2001)60:6&lt;396::AID-BIP10184&gt;3.0.CO;2-7</li>
<li id="ref3">McCoy, A. J., Grosse-Kunstleve, R. W., Adams, P. D., Winn, M. D., Storoni, L. C., & Read, R. J. (2007). Phaser crystallographic software. Journal of Applied Crystallography, 40(4), 658–674. DOI: 10.1107/S0021889807021206</li>
<li id="ref4">Sheldrick, G. M. (2010). Experimental phasing with SHELXC/D/E: combining chain tracing with density modification. Acta Crystallographica Section D, 66(4), 479–485. DOI: 10.1107/S0907444909038360</li>
<li id="ref5">Karplus, P. A., & Diederichs, K. (2012). Linking crystallographic model and data quality. Science, 336(6084), 1030–1033. DOI: 10.1126/science.1218231</li>
<li id="ref6">Kabsch, W. (2010). XDS. Acta Crystallographica Section D, 66(2), 125–132. DOI: 10.1107/S0907444909047337</li>
<li id="ref7">Mandal, K., Pentelute, B. L., Tereshko, V., Kossiakoff, A. A., & Kent, S. B. H. (2009). X-ray structure of native scorpion toxin BmBKTx1 by racemic protein crystallography using direct methods. Journal of the American Chemical Society, 131(4), 1362–1363. DOI: 10.1021/ja808116c</li>
<li id="ref8">Chayen, N. E., & Saridakis, E. (2008). Protein crystallization: from purified protein to diffraction-quality crystal. Nature Methods, 5(2), 147–153. DOI: 10.1038/nmeth.f.203</li>
<li id="ref9">Liebschner, D., Afonine, P. V., Baker, M. L., Bunkóczi, G., Chen, V. B., Croll, T. I., Hintze, B., Hung, L. W., Jain, S., McCoy, A. J., et al. (2019). Macromolecular structure determination using X-rays, neutrons and electrons: recent developments in Phenix. Acta Crystallographica Section D, 75(10), 861–877. DOI: 10.1107/S2059798319011471</li>
<li id="ref10">Murshudov, G. N., Skubák, P., Lebedev, A. A., Pannu, N. S., Steiner, R. A., Nicholls, R. A., Winn, M. D., Long, F., & Vagin, A. A. (2011). REFMAC5 for the refinement of macromolecular crystal structures. Acta Crystallographica Section D, 67(4), 355–367. DOI: 10.1107/S0907444911001314</li>
<li id="ref11">Usón, I., & Sheldrick, G. M. (2018). An introduction to experimental phasing of macromolecules illustrated by SHELX; new autotracing features. Acta Crystallographica Section D, 74(2), 106–116. DOI: 10.1107/S2059798317015121</li>
<li id="ref12">Williams, C. J., Headd, J. J., Moriarty, N. W., Prisant, M. G., Videau, L. L., Deis, L. N., Verma, V., Keedy, D. A., Hintze, B. J., Chen, V. B., et al. (2018). MolProbity: More and better reference data for improved all-atom structure validation. Protein Science, 27(1), 293–315. DOI: 10.1002/pro.3330</li>
<li id="ref13">Winter, G., Waterman, D. G., Parkhurst, J. M., Brewster, A. S., Gildea, R. J., Gerstel, M., Fuentes-Montero, L., Vollmar, M., Michels-Clark, T., Young, I. D., et al. (2018). DIALS: implementation and evaluation of a new integration package. Acta Crystallographica Section D, 74(2), 85–97. DOI: 10.1107/S2059798317017235</li>
<li id="ref14">Berman, H. M., Westbrook, J., Feng, Z., Gilliland, G., Bhat, T. N., Weissig, H., Shindyalov, I. N., & Bourne, P. E. (2000). The Protein Data Bank. Nucleic Acids Research, 28(1), 235–242. DOI: 10.1093/nar/28.1.235</li>
<li id="ref15">Adams, P. D., Afonine, P. V., Bunkóczi, G., Chen, V. B., Davis, I. W., Echols, N., Headd, J. J., Hung, L. W., Kapral, G. J., Grosse-Kunstleve, R. W., et al. (2010). PHENIX: a comprehensive Python-based system for macromolecular structure solution. Acta Crystallographica Section D, 66(2), 213–221. DOI: 10.1107/S0907444909052925</li>
</ol>
