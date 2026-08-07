---
title: Peptide Secondary Structure — Alpha-Helices, Beta-Sheets, Turns, and Coils
description: "Comprehensive guide to peptide secondary structure: alpha-helices, beta-sheets, beta-turns, random coils, Ramachandran plots, phi/psi angles, prediction methods, and circular dichroism analysis."
---

# Peptide Secondary Structure — Alpha-Helices, Beta-Sheets, Turns, and Coils

## Executive Summary

Peptide secondary structure represents the local spatial arrangement of the polypeptide backbone, stabilized primarily by backbone hydrogen bonds and governed by the torsion angles phi (φ) and psi (ψ). The four canonical types — alpha-helices, beta-sheets, beta-turns, and random coils — form the fundamental building blocks that dictate higher-order protein folding, stability, and function. Understanding secondary structure is essential for peptide design, stability engineering, and the interpretation of experimental data from circular dichroism (CD), nuclear magnetic resonance (NMR), and X-ray crystallography. Advances in computational prediction methods, from early statistical approaches such as Chou-Fasman to modern deep learning algorithms including PSIPRED and AlphaFold, have dramatically improved our ability to predict secondary structure from sequence alone.

## Background

The concept of regular, repeating structural elements in proteins emerged during the mid-20th century, catalyzed by the pioneering crystallographic work of Linus Pauling, Robert Corey, and Herman Branson. In 1951, Pauling and Corey published a series of landmark papers that predicted the existence of two hydrogen-bonded helical structures — the alpha-helix and the gamma-helix — as well as the beta-pleated sheet, based solely on model building and the principles of chemical bonding. The subsequent determination of the first protein crystal structures by John Kendrew (myoglobin, 1958) and Max Perutz (hemoglobin, 1960) confirmed the presence of these predicted elements, establishing secondary structure as a cornerstone concept in structural biology.

The development of the Ramachandran plot by G.N. Ramachandran and colleagues in 1963 provided a rigorous geometric framework for understanding which backbone conformations are sterically allowed, based on the torsional degrees of freedom around the N-Cα (phi, φ) and Cα-C (psi, ψ) bonds. This plot remains one of the most widely used validation tools in protein structure determination, appearing in virtually every structure refinement and validation pipeline.

The 1970s and 1980s witnessed the development of the first computational methods for secondary structure prediction from amino acid sequence. Peter Chou and Gerald Fasman published a statistical propensity-based method in 1974, assigning each amino acid a numerical preference for alpha-helical, beta-sheet, or turn conformations. The Garnier-Osguthorpe-Robson (GOR) method, introduced in 1978, expanded upon this with information theory-based approaches that considered the influence of neighboring residues. These early methods achieved prediction accuracies of approximately 50–60%, constrained by the limited protein structure databases available at the time.

## The Structural Foundation: Phi/Psi Angles and the Ramachandran Plot

### Conformational Degrees of Freedom

The peptide backbone possesses two rotatable bonds per residue (excluding the peptide bond itself, which is planar and rigid due to its partial double-bond character). The phi (φ) angle describes rotation about the N-Cα bond, while the psi (ψ) angle describes rotation about the Cα-C' bond. These two angles, along with the trans or cis configuration of the peptide bond (ω angle), define the conformation of each residue.

In standard Ramachandran nomenclature, φ and ψ are defined as 0° when the N-H and C=O groups are eclipsed. Allowed conformations occupy discrete regions of the Ramachandran plot, corresponding to distinct secondary structure types:

- **Alpha-helical region**: φ ≈ −60°, ψ ≈ −45° (right-handed α-helix); also a less populated left-handed α-helix region centered at φ ≈ +60°, ψ ≈ +45°, observed occasionally for glycine and specific non-canonical motifs.
- **Beta-sheet region**: φ ≈ −120° to −135°, ψ ≈ +120° to +135° (antiparallel β-sheets occupy the upper-left quadrant, parallel β-sheets slightly shifted).
- **Polyproline II (PPII) helix**: φ ≈ −75°, ψ ≈ +150°, a left-handed extended helix common in collagen and unstructured peptides.
- **Left-handed alpha-helix (αL)**: φ ≈ +60°, ψ ≈ +45°, rarely observed except for glycine residues in tight turns.

Glycine, lacking a side chain, has far greater conformational freedom than any other residue and can occupy regions of the Ramachandran plot that are sterically forbidden for amino acids with Cβ atoms. Proline, conversely, is severely restricted by its cyclic side chain, which locks φ near −60° and limits psi flexibility.

### Stereochemical Constraints

The primary determinants of allowed Ramachandran regions are steric clashes between backbone and side-chain atoms. The "hard-sphere" model used by Ramachandran treated atoms as impenetrable spheres with van der Waals radii; conformations producing interatomic distances below the sum of these radii were considered disallowed. Modern Ramachandran plots, derived from high-resolution protein structures in the Protein Data Bank (PDB), show refined allowed regions that account for minor steric accommodations and the effects of local environment.

Pre-proline residues (those immediately N-terminal to proline) exhibit a distinct Ramachandran distribution due to steric interactions between the preceding residue's side chain and the proline ring. Similarly, residues preceding glycine show widened allowed regions. These context-dependent effects are incorporated into modern structure validation tools such as MolProbity.

## Alpha-Helices

### Geometric Parameters

The alpha-helix is the most abundant regular secondary structure element, accounting for approximately 30–35% of residues in globular proteins. It is a right-handed helix with 3.6 residues per turn, a pitch of 5.4 Å (translational rise per turn), and a rise per residue of 1.5 Å. The hydrogen bonding pattern is characterized by i → i+4 interactions, in which the carbonyl oxygen of residue i forms a hydrogen bond with the amide hydrogen of residue i+4. This creates a 13-atom ring (the 3.6₁₃ helix in standard nomenclature).

Key geometric features include:
- **Helix axis**: The central axis about which the helix spirals.
- **Helix dipole**: The alignment of peptide bond dipoles along the helix axis produces a net macrodipole with the positive pole at the N-terminus and the negative pole at the C-terminus. This dipole has a magnitude of approximately 0.5–0.7 Debye per residue, creating a significant electrostatic effect over the length of the helix.
- **Side-chain orientation**: Side chains project outward and slightly toward the N-terminus, creating an arrangement that facilitates tertiary interactions and can be visualized through helical wheel projections.

### Helix Stability Factors

Alpha-helix stability is governed by a complex interplay of factors:

1. **Amino acid propensities**: Alanine, leucine, methionine, and glutamate are strong helix formers; glycine and proline are helix breakers. The Chou-Fasman parameters quantify these propensities on a scale where values above 1.0 indicate helix-favoring residues.

2. **N-capping and C-capping motifs**: The first four N-terminal residues and last four C-terminal residues often adopt distinct conformations to satisfy unsatisfied backbone hydrogen bond donors and acceptors. The N-cap residue (immediately preceding the helix) frequently participates in a hydrogen bond between its side chain and the backbone amide of the N3 residue. Common N-cap residues include serine, threonine, and asparagine. C-cap residues, particularly glycine, facilitate termination of the helix through favorable phi/psi angles.

3. **Helix dipole compensation**: Negatively charged residues (glutamate, aspartate) are frequently observed near the N-terminus, while positively charged residues (lysine, arginine) cluster at the C-terminus, compensating for the unfavorable dipole.

4. **Side-chain interactions**: Intrahelical salt bridges between residues at positions i and i+3 or i+4 (e.g., glutamate-lysine pairs) can contribute substantially to stability. Hydrophobic interactions between side chains on the same helical face also stabilize the folded conformation.

### Helical Wheel Analysis

The helical wheel is a two-dimensional projection of the alpha-helix viewed down the helix axis. Residues are plotted at 100° intervals (360°/3.6 residues per turn = 100° per residue), revealing the spatial arrangement of side chains around the helix. Helical wheels are invaluable tools for visualizing amphipathic character — the segregation of hydrophobic and hydrophilic residues onto opposite faces of the helix, a hallmark of membrane-active peptides and many protein-protein interaction motifs.

For a canonical amphipathic helix, hydrophobic residues (leucine, isoleucine, valine, phenylalanine) cluster on one face while polar and charged residues (lysine, arginine, glutamate, serine) occupy the opposite face. This arrangement permits simultaneous interaction with hydrophobic lipid environments and aqueous solvent, and is central to the mechanism of many antimicrobial peptides.

## Beta-Sheets

### Parallel and Antiparallel Arrangements

Beta-sheets consist of extended polypeptide strands (β-strands) aligned laterally and stabilized by interstrand backbone hydrogen bonds. Each strand typically contains 3–10 residues in an extended conformation with phi/psi values in the beta region of the Ramachandran plot. Two distinct sheet geometries exist:

- **Antiparallel β-sheets**: Adjacent strands run in opposite N→C directions. Hydrogen bonds are nearly linear (N-H···O angle ≈ 160°), with pairs of hydrogen bonds formed between each pair of residues across the sheet. The optimal phi/psi angles are approximately φ = −139°, ψ = +135°.

- **Parallel β-sheets**: Adjacent strands run in the same N→C direction. Hydrogen bonds are more angled (and marginally less stable) than in antiparallel sheets, with phi/psi values shifted to approximately φ = −119°, ψ = +113°.

Mixed sheets incorporating both parallel and antiparallel elements are common in protein structures, and the subtle differences in hydrogen bond geometry have implications for sheet stability and dynamics.

### Sheet Topology and Twisting

A characteristic feature of virtually all beta-sheets is a right-handed twist when viewed along the strand direction. This twist arises from the intrinsic chirality of L-amino acids: the preferred non-planar conformation of the peptide unit minimizes steric strain and leads to the observed right-handed twist of approximately 0–30° per residue. The cumulative twist over several strands produces the familiar beta-barrel, beta-propeller, and beta-helix architectures seen in soluble and membrane proteins.

The connections between beta-strands follow characteristic topological patterns:
- **Hairpins**: Adjacent antiparallel strands connected by a short turn (often a β-turn).
- **Greek key motifs**: Four adjacent antiparallel strands arranged in a pattern resembling classical Greek decorative motifs.
- **Beta-meanders**: Sequential strands connected by longer loops.
- **Jelly-roll (beta-sandwich)**: Two antiparallel sheets packed face-to-face, common in viral capsid proteins and carbohydrate-binding domains.

### Beta-Hairpins in Peptide Design

Beta-hairpins are minimal beta-sheet models consisting of two antiparallel strands connected by a turn sequence. They have been extensively studied as model systems for understanding beta-sheet folding, stability, and design. The stability of a beta-hairpin depends on:
- Turn sequence compatibility (type I' and type II' turns are particularly favorable).
- Cross-strand side-chain interactions (hydrophobic clustering and interstrand hydrogen bonds).
- Strand length and terminal capping effects.

Designed beta-hairpin peptides have applications as scaffolds for epitope presentation, as antimicrobial agents, and as minimal models for studying protein folding mechanisms.

## Beta-Turns

Beta-turns are the most common type of tight reverse turn, reversing the polypeptide chain direction over four consecutive residues (positions i, i+1, i+2, i+3). They are stabilized by a hydrogen bond between the carbonyl oxygen of residue i and the amide hydrogen of residue i+3, forming a 10-atom ring (a type of β-turn or 3₁₀ turn). Beta-turns account for approximately 25–30% of residues in globular proteins and are often found at the protein surface, where they facilitate chain reversal between secondary structure elements.

### Classification of Beta-Turns

Venkatachalam (1968) first classified beta-turns based on the phi/psi angles of the central residues (i+1, i+2). The major types are:

| Turn Type | φ(i+1) | ψ(i+1) | φ(i+2) | ψ(i+2) | Preferred i+1 | Preferred i+2 |
|-----------|--------|--------|--------|--------|---------------|---------------|
| Type I    | −60°   | −30°   | −90°   | 0°     | Any           | Any           |
| Type II   | −60°   | +120°  | +80°   | 0°     | Any           | Gly           |
| Type I'   | +60°   | +30°   | +90°   | 0°     | Gly           | Any           |
| Type II'  | +60°   | −120°  | −80°   | 0°     | Gly           | Gly           |
| Type VIII | −60°   | −30°   | −120°  | +120°  | Any           | Any           |
| Type VI   | −60°   | +120°  | cis-Pro | —     | Any           | Pro           |

Type I and Type II turns are the most abundant, with Type II turns requiring glycine at position i+2 due to the positive phi angle. Prime variants (I', II') are the mirror images and are less common. Type VI turns involve a cis-proline peptide bond at position i+2→i+3.

### Gamma-Turns and Other Reverse Turns

Gamma-turns are three-residue reverse turns stabilized by an i → i+2 hydrogen bond (7-atom ring). They are less common than beta-turns but play important roles in specific structural contexts. Alpha-turns involve five residues with an i → i+4 hydrogen bond, effectively a single turn of an alpha-helix. Omega-loops are longer, non-repetitive loop structures of 6–16 residues that lack regular internal hydrogen bonding but maintain compact conformations.

## Secondary Structure Prediction

### Historical Methods: Chou-Fasman and GOR

The Chou-Fasman method (1974) was the first widely adopted secondary structure prediction algorithm. It calculates conformational parameters P(α), P(β), and P(t) for each amino acid based on their frequency in each secondary structure type in a database of known structures. A segment of sequence is predicted to form a helix when four out of six consecutive residues have P(α) > 1.03 and the average P(α) exceeds P(β). Nucleation and propagation are modeled as distinct processes, with helix nucleation requiring a cluster of strong helix-formers and extension proceeding bidirectionally until terminated by helix breakers or competitive beta-sheet prediction.

The GOR method (Garnier, Osguthorpe, and Robson, 1978) introduced information theory to secondary structure prediction. Rather than calculating simple residue propensities, GOR evaluates the conformational influence of each residue on its neighbors using conditional probability matrices derived from a window of typically 17 residues (positions −8 to +8). Successive versions (GOR I through GOR V) incorporated larger databases and more sophisticated statistical treatments, with GOR V achieving approximately 73% three-state accuracy.

### Modern Methods: PSIPRED and Deep Learning

PSIPRED (Jones, 1999) marked a paradigm shift by employing a two-stage neural network architecture. The first stage uses sequence profiles generated by PSI-BLAST (Position-Specific Iterated BLAST) as input, capturing evolutionary information in the form of position-specific scoring matrices (PSSMs). The second stage filters and refines the raw predictions, achieving a Q3 accuracy (percentage of residues correctly predicted as helix, sheet, or coil) of approximately 77–80%, a substantial improvement over single-sequence methods.

Contemporary deep learning approaches have pushed prediction accuracy still further:
- **SPOT-1D**: Uses deep convolutional and recurrent neural networks trained on a combination of sequence profiles, predicted backbone angles, and solvent accessibility, achieving Q3 accuracies exceeding 85%.
- **AlphaFold2**: While primarily designed for full three-dimensional structure prediction, AlphaFold2 implicitly learns secondary structure as a feature of the folding process and produces highly accurate secondary structure assignments.
- **NetSurfP-3.0**: Combines sequence-based predictions with information from homologous structures for state-of-the-art accuracy.

The improvement from ~55% (Chou-Fasman) to >85% (modern deep learning) over 50 years reflects both the exponential growth of the PDB and revolutionary advances in machine learning methodology.

## Circular Dichroism and Secondary Structure

### Principles of Far-UV CD

Circular dichroism spectroscopy in the far-ultraviolet region (typically 190–260 nm) is the most widely used experimental technique for rapid assessment of peptide secondary structure. The method measures the differential absorption of left- and right-circularly polarized light by peptide bond chromophores. The peptide bond n→π* transition (centered near 220 nm) and π→π* transition (near 190 nm) exhibit characteristic CD signatures that depend on the backbone conformation:

- **Alpha-helix**: Strong negative bands at 222 nm (n→π*) and 208 nm (π→π*), with a strong positive band near 192 nm. The ratio of the 222 nm and 208 nm bands (R₁ = [θ]₂₂₂/[θ]₂₀₈) provides information about helix length and distortion.
- **Beta-sheet**: A negative band near 215–218 nm (n→π*) and a positive band near 195 nm. The precise position and intensity vary with sheet twist and strand orientation.
- **Beta-turn**: CD signatures are type-dependent but typically include a negative band near 220–225 nm.
- **Random coil (disordered)**: A strong negative band near 195–200 nm and a weak positive or negative band near 220 nm. Polyproline II helices, common in disordered peptides, show a negative band near 200 nm and a weaker positive band near 220 nm.

### Quantitative Analysis: Deconvolution Algorithms

Several algorithms have been developed to estimate the fractional secondary structure content from far-UV CD spectra:

1. **CONTIN**: Uses a ridge regression approach with a reference set of proteins of known structure. Suitable for proteins with known crystal structures in the reference set.

2. **CDSSTR**: Employs a variable selection method that identifies the subset of reference proteins that best represents the spectrum of the unknown. It is particularly robust when the reference set is large and diverse.

3. **SELCON3**: Uses the self-consistent method with singular value decomposition. Requires a reference set of CD spectra and known structures; each protein in the reference set is analyzed using the remaining proteins as a basis set.

4. **BeStSel**: A web-based server optimized for beta-sheet-rich proteins, providing detailed analysis of parallel/antiparallel sheet content and sheet twist.

Accuracy depends critically on wavelength range (190–260 nm is optimal), spectral quality, and the appropriateness of the reference set. For short peptides (<20 residues), specialized algorithms and reference sets are required, as the conformational properties of short peptides differ substantially from globular proteins.

## Research Evidence

| Study | System | Method | Key Finding |
|-------|--------|--------|-------------|
| Pauling & Corey (1951) | Model peptides | X-ray diffraction of models | Predicted α-helix and β-sheet geometries; established the role of backbone hydrogen bonds |
| Ramachandran et al. (1963) | Model dipeptides | Hard-sphere calculations | Defined sterically allowed φ/ψ regions; established the Ramachandran plot |
| Chou & Fasman (1974) | 15 proteins (2,473 residues) | Statistical propensity analysis | First practical secondary structure prediction; P(α), P(β), P(t) scales |
| Garnier et al. (1978) | 25 proteins | Information theory (GOR I) | Incorporated residue windows; 55% Q3 accuracy |
| Jones (1999) | PDB Select (non-redundant) | PSIPRED neural network + PSI-BLAST | 77–80% Q3 accuracy; established PSSM-based prediction |
| Micsonai et al. (2018) | 73 reference proteins | BeStSel CD deconvolution | Improved beta-sheet content estimation including parallel/antiparallel discrimination |
| Singh et al. (2021) | CASP14 targets | Deep learning (NetSurfP-3.0) | >87% Q3 accuracy; integration of evolutionary and structural features |
| Jumper et al. (2021) | CASP14/CASP15 targets | AlphaFold2 deep learning | Atomic-accuracy structure prediction with implicit secondary structure |
| Toniolo et al. (2002) | α-aminoisobutyric acid peptides | CD, X-ray, NMR | Demonstrated induced CD for 3₁₀ and α-helices; established diagnostic CD signatures |
| Woody (1995) | Theoretical | Exciton theory of CD | Developed theoretical framework for interpreting peptide CD in terms of secondary structure |
| Chellgren & Creamer (2004) | Alanine-based peptides | CD thermal denaturation | Quantified residue-specific helix propensities for all 20 amino acids |
| Hutchinson & Thornton (1994) | PDB analysis (>300 proteins) | Structural bioinformatics | Comprehensive classification of β-turns and hairpins in protein structures |

## Current Understanding

The field of peptide secondary structure has matured into a sophisticated discipline that bridges fundamental physical chemistry, computational biology, and applied peptide engineering. Several key principles are well established:

The Ramachandran plot, while originally derived from steric considerations, has been validated and refined by five decades of high-resolution crystal structures. Modern statistical analyses of the PDB have shown that the allowed regions are populated non-uniformly, with residue-specific propensities reflecting the energetic preferences of different amino acids for particular backbone conformations.

The concept of secondary structure propensity — the intrinsic tendency of an amino acid to adopt a particular conformation — has been refined through experimental measurements using host-guest peptide systems, protein mutagenesis studies, and statistical analyses of the PDB. Alanine has the strongest helix propensity, glycine the weakest, but these propensities are context-dependent and can be modulated by solvent conditions (e.g., trifluoroethanol stabilizes helices; urea destabilizes them), pH, temperature, and ionic strength.

Computational prediction of secondary structure has achieved high accuracy (>85% three-state Q3), approaching the theoretical limit imposed by ambiguous assignment at boundaries between secondary structure elements. However, accurate prediction remains challenging for: (1) very short peptides (<10 residues), where end effects dominate; (2) sequences that sample multiple conformations in equilibrium; (3) non-canonical secondary structures such as 3₁₀ helices, polyproline II helices, and various turn types; and (4) peptides in membrane-mimetic or non-aqueous environments.

The interplay between secondary structure and higher-order folding remains an active area of investigation. While secondary structure elements are often treated as independent building blocks, their formation is cooperative and coupled to tertiary packing. The hierarchical model of folding — in which secondary structure forms first and subsequently assembles into tertiary structure — is an oversimplification; many proteins exhibit concerted folding in which secondary and tertiary structure develop simultaneously.

## Future Research Directions

- **Membrane-mimetic environments**: Development of CD reference sets and secondary structure prediction algorithms specifically trained on peptides in micellar, bicellar, and liposomal environments would dramatically improve the design and characterization of membrane-active peptides for antimicrobial and cell-penetrating applications.

- **Non-canonical amino acids**: As the chemical diversity of peptide therapeutics expands through incorporation of D-amino acids, beta-amino acids, peptoids, and other non-standard building blocks, new Ramachandran-type analyses and secondary structure assignment tools are required.

- **Real-time conformational dynamics**: Time-resolved CD, infrared spectroscopy, and NMR relaxation methods applied to peptides on microsecond-to-millisecond timescales will reveal the kinetic pathways of secondary structure formation and interconversion.

- **Integrative prediction frameworks**: Combining sequence-based secondary structure prediction with molecular dynamics simulations, NMR chemical shift prediction, and CD spectral prediction would provide a unified platform for peptide structural characterization.

- **Designed secondary structure elements**: Rational design of peptides with precisely specified secondary structure content, stability, and dynamics holds promise for creating novel biomaterials, sensors, and therapeutic agents.

- **Crowded and complex environments**: Studies of secondary structure in the crowded intracellular milieu (using in-cell NMR and in-cell CD) will bridge the gap between in vitro biophysics and in vivo function.

## Frequently Asked Questions

<div class="faq-container">

<div class="faq-item">
<h3 class="faq-question">What is the difference between alpha-helix and 3<sub>10</sub>-helix?</h3>
<p>The alpha-helix (3.6<sub>13</sub>) has 3.6 residues per turn with i→i+4 hydrogen bonding, while the 3<sub>10</sub>-helix has 3.0 residues per turn with i→i+3 hydrogen bonding, producing a tighter, narrower helix with a 10-atom hydrogen-bonded ring. The 3<sub>10</sub>-helix is less stable in isolation but occurs frequently at the termini of alpha-helices and in short peptides rich in α-aminoisobutyric acid (Aib) or other Cα-tetrasubstituted residues.</p>
</div>

<div class="faq-item">
<h3 class="faq-question">How does proline affect secondary structure?</h3>
<p>Proline is both a helix breaker and a helix initiator, depending on context. Its cyclic side chain restricts φ to approximately −60°, eliminating the backbone amide proton required for i→i+4 hydrogen bonding, which terminates alpha-helices. However, proline is highly favored at the N-cap+1 position and is essential for Type VI β-turns. In polyproline II helices, proline is the defining residue.</p>
</div>

<div class="faq-item">
<h3 class="faq-question">What information does a Ramachandran plot provide?</h3>
<p>A Ramachandran plot maps the phi (φ) and psi (ψ) backbone torsion angles of each residue, revealing allowed and disallowed conformations based on steric constraints. It is used to validate protein structures (residues in disallowed regions indicate errors), assign secondary structure type (alpha-helical, beta-sheet, or left-handed helical regions), and identify unusual conformations that may be functionally important.</p>
</div>

<div class="faq-item">
<h3 class="faq-question">How does circular dichroism work for secondary structure determination?</h3>
<p>Circular dichroism measures the differential absorption of left- and right-circularly polarized light by peptide bond chromophores in the far-UV region (190–260 nm). Different secondary structures produce characteristic CD spectra: alpha-helices show double minima at 208 and 222 nm, beta-sheets show a single minimum near 215 nm, and random coils show a minimum near 200 nm. Deconvolution algorithms estimate the fractional content of each secondary structure type.</p>
</div>

<div class="faq-item">
<h3 class="faq-question">What is the accuracy of modern secondary structure prediction?</h3>
<p>Modern deep learning methods such as NetSurfP-3.0 and SPOT-1D achieve Q3 (three-state: helix/sheet/coil) accuracies exceeding 85%, while segment overlap (SOV) scores, which better capture boundary accuracy, exceed 80%. This represents a dramatic improvement from ~55% for Chou-Fasman and ~65% for early neural networks. For research-grade custom peptides, structural biology services including CD and NMR are available through <a href="https://rplpeptides.com">RPL Peptides</a>.</p>
</div>

<div class="faq-item">
<h3 class="faq-question">Can secondary structure be predicted for short synthetic peptides?</h3>
<p>Secondary structure prediction for peptides shorter than 15 residues is less reliable than for proteins because end effects dominate, and many short peptides sample multiple conformations in equilibrium. However, solvent conditions (TFE for helix induction) and sequence design (incorporation of helix-stabilizing or turn-inducing residues) can produce predominantly single-conformation populations. For custom peptide synthesis and structural characterization, visit <a href="https://data.rplpeptides.com">RPL Peptides Data Center</a>.</p>
</div>

<div class="faq-item">
<h3 class="faq-question">What is an amphipathic helix and why is it important?</h3>
<p>An amphipathic helix has hydrophobic and hydrophilic residues segregated onto opposite faces, creating a dual-character surface. This arrangement is crucial for membrane-interacting peptides (antimicrobial peptides, cell-penetrating peptides), where the hydrophobic face inserts into the lipid bilayer while the hydrophilic face interacts with aqueous solvent or lipid head groups. Helical wheel projections are used to visualize amphipathic character.</p>
</div>

<div class="faq-item">
<h3 class="faq-question">How does solvent environment affect peptide secondary structure?</h3>
<p>Solvent polarity, hydrogen bonding capacity, and dielectric constant profoundly influence secondary structure. 2,2,2-trifluoroethanol (TFE) induces alpha-helical conformations by strengthening intrachain hydrogen bonds relative to peptide-solvent interactions. Membrane-mimetic solvents (SDS micelles, DPC micelles, lipid bicelles) can induce or stabilize amphipathic helices. Urea and guanidinium chloride destabilize all secondary structure types by competing for hydrogen bonds.</p>
</div>

<div class="faq-item">
<h3 class="faq-question">What are the limitations of the Chou-Fasman method?</h3>
<p>The Chou-Fasman method achieves only ~50–55% accuracy, limited by: (1) a small training database (15 proteins, 2,473 residues); (2) independent treatment of each residue, ignoring the influence of neighboring residues beyond a simple nucleation-propagation heuristic; (3) inability to account for long-range interactions and tertiary context; and (4) overlapping propensities for secondary structure types that produce ambiguous predictions at boundaries. Despite these limitations, the method remains pedagogically valuable for introducing the principles of structure prediction.</p>
</div>

<div class="faq-item">
<h3 class="faq-question">How are beta-turns classified?</h3>
<p>Beta-turns are classified primarily by the phi and psi angles of residues i+1 and i+2. The most common types are Type I (φ(i+1)≈−60°, ψ(i+1)≈−30°, φ(i+2)≈−90°, ψ(i+2)≈0°) and Type II (similar except ψ(i+1)≈+120°, φ(i+2)≈+80°). Type II requires glycine at position i+2 due to the positive phi angle. Prime types (I', II') are mirror images, and specialized types (VI, VIII) involve cis-proline or extended conformations. The classification is essential for the design of beta-hairpin peptides and protein engineering.</p>
</div>

</div>

## References

<ol class="references">
<li id="ref1">Pauling, L., Corey, R. B., & Branson, H. R. (1951). The structure of proteins: two hydrogen-bonded helical configurations of the polypeptide chain. Proceedings of the National Academy of Sciences, 37(4), 205–211. DOI: 10.1073/pnas.37.4.205</li>
<li id="ref2">Ramachandran, G. N., Ramakrishnan, C., & Sasisekharan, V. (1963). Stereochemistry of polypeptide chain configurations. Journal of Molecular Biology, 7(1), 95–99. DOI: 10.1016/S0022-2836(63)80023-6</li>
<li id="ref3">Chou, P. Y., & Fasman, G. D. (1974). Prediction of protein conformation. Biochemistry, 13(2), 222–245. DOI: 10.1021/bi00699a002</li>
<li id="ref4">Garnier, J., Osguthorpe, D. J., & Robson, B. (1978). Analysis of the accuracy and implications of simple methods for predicting the secondary structure of globular proteins. Journal of Molecular Biology, 120(1), 97–120. DOI: 10.1016/0022-2836(78)90297-8</li>
<li id="ref5">Jones, D. T. (1999). Protein secondary structure prediction based on position-specific scoring matrices. Journal of Molecular Biology, 292(2), 195–202. DOI: 10.1006/jmbi.1999.3091</li>
<li id="ref6">Micsonai, A., Wien, F., Bulyáki, É., Kun, J., Moussong, É., Lee, Y. H., Goto, Y., Réfrégiers, M., & Kardos, J. (2018). BeStSel: a web server for accurate protein secondary structure prediction and fold recognition from the circular dichroism spectra. Nucleic Acids Research, 46(W1), W315–W322. DOI: 10.1093/nar/gky497</li>
<li id="ref7">Woody, R. W. (1995). Circular dichroism. Methods in Enzymology, 246, 34–71. DOI: 10.1016/0076-6879(95)46006-3</li>
<li id="ref8">Hutchinson, E. G., & Thornton, J. M. (1994). A revised set of potentials for β-turn formation in proteins. Protein Science, 3(12), 2207–2216. DOI: 10.1002/pro.5560031206</li>
<li id="ref9">Chellgren, B. W., & Creamer, T. P. (2004). Short sequences of non-proline residues can adopt the polyproline II helical conformation. Biochemistry, 43(19), 5864–5869. DOI: 10.1021/bi0499228</li>
<li id="ref10">Jumper, J., Evans, R., Pritzel, A., Green, T., Figurnov, M., Ronneberger, O., Tunyasuvunakool, K., Bates, R., Žídek, A., Potapenko, A., et al. (2021). Highly accurate protein structure prediction with AlphaFold. Nature, 596(7873), 583–589. DOI: 10.1038/s41586-021-03819-2</li>
<li id="ref11">Høie, M. H., Kiehl, E. N., Petersen, B., Nielsen, M., Winther, O., Nielsen, H., Hallgren, J., & Marcatili, P. (2022). NetSurfP-3.0: accurate and fast prediction of protein structural features by deep learning. Nucleic Acids Research, 50(W1), W510–W515. DOI: 10.1093/nar/gkac439</li>
<li id="ref12">Toniolo, C., Crisma, M., Formaggio, F., & Peggion, C. (2001). Control of peptide conformation by the Thorpe-Ingold effect (Cα-tetrasubstitution). Peptide Science, 60(6), 396–419. DOI: 10.1002/1097-0282(2001)60:6&lt;396::AID-BIP10184&gt;3.0.CO;2-7</li>
<li id="ref13">Venkatachalam, C. M. (1968). Stereochemical criteria for polypeptides and proteins. V. Conformation of a system of three linked peptide units. Biopolymers, 6(10), 1425–1436. DOI: 10.1002/bip.1968.360061006</li>
<li id="ref14">Singh, J., Hanson, J., Paliwal, K., & Zhou, Y. (2021). SPOT-1D: Improved protein secondary structure prediction using dilated convolutional networks. Bioinformatics, 37(2), 187–194. DOI: 10.1093/bioinformatics/btaa847</li>
<li id="ref15">Greenfield, N. J. (2006). Using circular dichroism spectra to estimate protein secondary structure. Nature Protocols, 1(6), 2876–2890. DOI: 10.1038/nprot.2006.202</li>
</ol>
