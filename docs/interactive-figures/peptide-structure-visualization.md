---
title: "Peptide Structure Visualization: From Atomic Coordinates to Publication-Ready Figures"
description: "Master peptide 3D structure visualization using PyMOL and ChimeraX — ribbon diagrams, Ramachandran plots, electrostatic surface maps, molecular dynamics snapshots, and SAR analysis."
slug: peptide-structure-visualization
category: Interactive Figures
tags: [Structural Biology, PyMOL, ChimeraX, Ramachandran Plot, Molecular Dynamics, SAR]
author: RPL Peptides Research Team
published: 2026-08-07
---

# Peptide Structure Visualization: From Atomic Coordinates to Publication-Ready Figures

## Executive Summary

Visualizing peptide structures in three dimensions transforms abstract sequence data into interpretable molecular forms. This article provides a comprehensive guide to the tools, techniques, and design principles that produce publication-quality structural figures. We cover ribbon diagrams, surface representations, electrostatic potential mapping, Ramachandran plot generation, molecular dynamics trajectory visualization, and the critical transition from raw rendering to structure-activity relationship (SAR) communication. Whether you are a graduate student preparing your first structural biology figure or a seasoned researcher refining your visualization workflow in PyMOL or ChimeraX, the protocols and principles described here will elevate the clarity and impact of your peptide structure figures. For high-quality analytical-grade peptides suitable for structural studies, [RPL Peptides](https://rplpeptides.com) provides rigorously characterized material, with supporting analytical data available at the [RPL Peptides Data Portal](https://data.rplpeptides.com).

## Background

Structural biology entered the visual age when John Kendrew's 1958 ribbon diagram of myoglobin demonstrated that the three-dimensional fold of a protein could be communicated through simplified graphical representation. In the decades since, peptide and protein structure visualization has evolved from hand-drawn illustrations on transparent sheets to real-time interactive rendering on consumer hardware. Modern tools such as PyMOL (Schrödinger), UCSF ChimeraX, and VMD (University of Illinois) now offer crystallographic-quality rendering with physically based lighting, ambient occlusion, and real-time ray tracing.

For peptide researchers, structure visualization serves four distinct purposes. **First**, it validates experimental data — does the solved or modeled structure make chemical sense? **Second**, it communicates findings — a well-designed figure conveys conformational details, binding interfaces, and electrostatic features more effectively than a table of coordinates. **Third**, it generates hypotheses — visual inspection of a binding pocket often reveals unoccupied sub-pockets or unrealized hydrogen-bonding opportunities. **Fourth**, it supports SAR reasoning — mapping activity data onto a three-dimensional scaffold reveals stereoelectronic determinants of potency that sequence analysis alone would miss.

The peptide visualization pipeline typically proceeds through five stages: (1) coordinate acquisition from the Protein Data Bank (PDB), AlphaFold, or molecular dynamics simulations; (2) initial rendering with default representations and color schemes; (3) iterative refinement of display settings to highlight the features of interest; (4) annotation with labels, distance measurements, and schematic overlays; and (5) export at publication resolution (typically 300–600 dpi at the target column width).

## Core Visualization Techniques

### Ribbon Diagrams and Secondary Structure Representations

The ribbon diagram remains the most widely used representation of peptide and protein structure. Introduced by Jane Richardson in 1981, the ribbon traces the polypeptide backbone as a smooth spline through Cα positions, with secondary structure elements encoded as distinct glyphs: α-helices as coiled ribbons or cylinders, β-strands as flat arrows pointing toward the C-terminus, and loops as thin tubes or coils.

In PyMOL, the fundamental commands are deceptively simple but the parameter space is vast:

```python
# Basic ribbon representation
show cartoon, all
color palecyan, all

# Helix and sheet differentiation
set cartoon_cylindrical_helices, 1
set cartoon_rectangular_sheets, 1
set cartoon_fancy_helices, 1
```

The `cartoon_fancy_helices` setting introduces the iconic helical ribbon with its characteristic curvature that follows the helical path. Setting `cartoon_cylindrical_helices` to 0 produces a thin ribbon for helices, which is preferred in certain journals for consistency. For ChimeraX users, the equivalent commands use the `cartoon` style with similar parameter control:

```
cartoon style protein modeh default arrows false
cartoon style protein xsection oval width 1.6 thickness 0.6
```

**Color schemes** are a design decision with scientific consequences. The most common approaches include:

- **Secondary structure coloring**: α-helices in red, β-strands in yellow, loops in green. Universally understood but visually limited for distinguishing domains.
- **Chain coloring**: Each chain in a distinct color. Essential for multi-chain complexes (e.g., GLP-1 bound to its receptor).
- **B-factor (temperature factor) coloring**: Blue (low B-factor, well-ordered) through white to red (high B-factor, flexible). Provides immediate insight into structural confidence and conformational flexibility.
- **Residue-type coloring**: Hydrophobic in gray, polar in green, positively charged in blue, negatively charged in red. Reveals surface properties at a glance.
- **Conservation coloring**: Variable positions in cyan, conserved positions in magenta. Essential for functional site identification in peptide families.

For peptide-receptor complexes, a productive strategy is: receptor in pale gray ribbon, peptide ligand in a bold color (orange or magenta), with key interacting residues shown as sticks in atom-type coloring (carbon in the same bold color, oxygen red, nitrogen blue).

### Surface Representations

Surface representations communicate molecular shape, binding-pocket geometry, and the spatial distribution of chemical properties. Three surface types are standard:

**Solvent-accessible surface (SAS)**: Generated by rolling a spherical probe (typically 1.4 Å radius, simulating a water molecule) over the van der Waals surface. This is the surface that a solvent molecule or small ligand "sees." In PyMOL: `show surface, all; set transparency, 0.3`.

**Solvent-excluded surface (SES)**: Also called the Connolly surface or molecular surface. Generated by the same probe-rolling procedure but defines the surface at the probe's inward-facing contact points rather than its center. The SES reveals narrow clefts and pockets that the SAS smooths over.

**Van der Waals surface**: The union of spheres at each atom's van der Waals radius. Rarely used in isolation because the crevices between atoms produce a spiky, uninformative appearance, but useful as a validation layer.

**Practical surface strategy for peptide visualization**: Render the receptor as a gray semi-transparent surface and the peptide ligand as a cartoon or stick representation nested within the surface cleft. Add hydrogen-bond donors and acceptors as colored patches (blue for positive, red for negative) using PyMOL's `APBS` (Adaptive Poisson-Boltzmann Solver) plugin or ChimeraX's built-in Coulombic surface coloring.

### Electrostatic Surface Potentials

Electrostatic potential maps color the molecular surface by the local electrostatic potential experienced by a point positive charge. The standard color scale ranges from deep red (−5 kT/e or less, strongly negative) through white (neutral, 0 kT/e) to deep blue (+5 kT/e or more, strongly positive).

The computational pipeline requires solving the Poisson-Boltzmann equation, which describes the electrostatic potential in a dielectric continuum:

$$ \nabla \cdot [\epsilon(\mathbf{r}) \nabla \phi(\mathbf{r})] - \bar{\kappa}^2(\mathbf{r}) \sinh[\phi(\mathbf{r})] = -4\pi \rho^f(\mathbf{r}) $$

where $\epsilon(\mathbf{r})$ is the position-dependent dielectric constant, $\phi(\mathbf{r})$ is the electrostatic potential, $\bar{\kappa}^2$ is the modified Debye-Hückel screening parameter, and $\rho^f(\mathbf{r})$ is the fixed charge density from the atomic partial charges.

For most peptide researchers, the APBS plugin within PyMOL abstracts the computational complexity. The workflow is:

1. Prepare the structure: add hydrogens (`h_add` in PyMOL), assign protonation states at the pH of interest (typically 7.4 for physiological relevance).
2. Assign partial charges and radii using a force field: AMBER ff14SB or CHARMM36 for peptides, PARSE for implicit-solvent calculations.
3. Run APBS with default dielectric constants (protein interior ε = 2, solvent ε = 78.5), ionic strength 0.150 M (physiological), and a grid spacing of ~0.5 Å.
4. Map the resulting potential onto the molecular surface using a color spectrum.

In ChimeraX, the process is streamlined: `coulombic sel protein palette -10 red 0 white 10 blue`. The built-in Coulombic Surface Coloring tool uses the same Poisson-Boltzmann framework but integrates grid generation, solving, and mapping into a single command.

**Interpreting electrostatic maps for peptides**: A peptide hormone's receptor-binding face typically displays a complementary electrostatic pattern to its receptor. For example, the GLP-1 peptide presents a negatively charged patch (Asp and Glu residues) that interacts with a positively charged region on the GLP-1 receptor extracellular domain. Electrostatic mismatch in a peptide analog (e.g., replacing Asp9 with a neutral residue) is immediately visible on the electrostatic surface and correlates with reduced binding affinity.

### Ramachandran Plots

The Ramachandran plot is the foundational validation tool for peptide and protein structure quality. It maps each residue's backbone dihedral angles — φ (phi, C–N–Cα–C) and ψ (psi, N–Cα–C–N) — onto a two-dimensional scatter plot. Steric constraints between main-chain atoms restrict allowed φ/ψ combinations to specific regions.

**Allowed and disallowed regions**: For L-amino acids (excluding glycine and proline), the allowed regions cluster in three zones: (1) the right-handed α-helical region (φ ≈ −60°, ψ ≈ −45°), (2) the β-sheet region (φ ≈ −120°, ψ ≈ +120°), and (3) the left-handed α-helical region (φ ≈ +60°, ψ ≈ +40°), which is sparsely populated. Glycine, lacking a Cβ atom, samples a broader range; proline, with its cyclic pyrrolidine ring, restricts φ to approximately −65° ± 15°.

**Generating Ramachandran plots in PyMOL** uses the `ramachandran` command:

```python
# Generate Ramachandran plot for selection
fetch 1dpp, async=0  # Example peptide structure
ramachandran sele, dynamics=off
```

The `dynamics=off` flag generates a static plot suitable for figure export. Use `png rama_plot.png, dpi=300` to export at publication resolution. For ChimeraX:

```
open 1dpp
ramaplot #1
```

**Publication-quality plot design** requires attention to several details: (1) color residues by type (Gly in triangles, Pro in squares, pre-Pro in diamonds, general in circles); (2) overlay the favored (98%), allowed (99.8%), and outlier contours from the Richardson lab's Top8000 dataset; (3) label outlier residues with their sequence position and chain; and (4) include a legend showing the percentage of residues in each region. A well-constructed Ramachandran plot for a high-resolution peptide structure should show >98% of residues in favored regions and 0% outliers.

**Glycine and pre-proline considerations**: Glycine residues populate both the L-α and D-α regions of the Ramachandran plot because the absence of a Cβ side chain eliminates the steric clash that restricts other residues. Pre-proline residues (the residue immediately N-terminal to proline) exhibit a characteristic shift in their allowed φ/ψ distribution due to the steric influence of the proline δ carbon on the preceding residue's backbone. ChimeraX accounts for this automatically when rendering conformer-dependent contours.

### Molecular Dynamics Snapshot Visualization

Molecular dynamics (MD) simulations generate trajectories — time-ordered sequences of atomic coordinates that capture the peptide's conformational dynamics. Visualizing MD trajectories requires techniques beyond static structure rendering.

**Trajectory loading and frame management**: PyMOL loads trajectories through the `load_traj` command, which requires a topology file (e.g., the starting PDB) and a trajectory file (e.g., DCD, XTC, or NETCDF format from AMBER, GROMACS, or NAMD):

```python
load peptide_start.pdb, obj
load_traj peptide_traj.dcd, obj
```

Once loaded, the trajectory appears as a multi-state object, with each frame accessible via the state index. The `intra_fit` command superimposes all frames onto a reference (typically the first frame or an energy-minimized average structure) to remove global translation and rotation:

```python
intra_fit obj and name CA
```

**Visualizing conformational ensembles**: The simplest approach renders multiple frames as a semi-transparent overlay. Select 10–20 equally spaced frames from the trajectory, show them as thin cartoons at low transparency (e.g., 0.2), and color by frame index (blue → white → red) to indicate temporal progression. This creates a "cloud cartoon" that reveals flexible regions as broad, fuzzy areas and rigid regions as sharp, overlapping lines.

Command for ensemble overlay in PyMOL:

```python
set all_states, on
show cartoon, all
set cartoon_transparency, 0.7
```

**RMSD and RMSF as quantitative visualization**: Root-mean-square deviation (RMSD) and root-mean-square fluctuation (RMSF) quantify global and per-residue conformational variability, respectively. These are typically plotted as line graphs (RMSD vs. time) or bar charts (RMSF vs. residue number), but they can be directly mapped onto the 3D structure using B-factor coloring — a technique that transforms abstract numerical data into an intuitive structural visualization.

Algorithm for B-factor coloring by RMSF:

1. Calculate per-residue RMSF from the MD trajectory using GROMACS `gmx rmsf` or CPPTRAJ.
2. Write the RMSF values into the B-factor column of the average structure PDB file.
3. Open in PyMOL and color by B-factor: `spectrum b, blue_white_red, all`.

Flexible loops and termini will appear red, while rigid secondary structure elements remain blue. This visual directly answers the question: "Which parts of my peptide are dynamic?"

**Free energy landscape visualization**: For peptides that sample multiple conformational states, a free energy landscape provides a thermodynamics-grounded view of the conformational ensemble. The landscape is a two-dimensional surface plotted against two collective variables (typically the first two principal components from PCA, or two key distance/angle coordinates). Each bin represents a microstate; the free energy (ΔG = −kT ln P, where P is the probability of occupying that bin) is color-coded from deep blue (energy minimum, most populated) through green and yellow to red (energy barrier, sparsely populated).

GROMACS users generate the landscape with:

```bash
gmx covar -s md.tpr -f md.xtc -o eigenvec.xvg -v eigenval.xvg
gmx anaeig -s md.tpr -f md.xtc -v eigenvec.xvg -2d pc12.xvg -first 1 -last 2
gmx sham -f pc12.xvg -ls g_sham.xpm -notime
```

The resulting XPM image can be opened in PyMOL as a texture or plotted independently using matplotlib with `pcolormesh` for publication-quality rendering.

## Structure-Activity Relationships (SAR) Visualization

SAR visualization overlays biological activity data onto the three-dimensional peptide structure, revealing which structural features drive potency, selectivity, and metabolic stability. The goal is to communicate "if you change this atom, this is what happens to activity" in a single figure.

### Residue Scanning Heatmaps

Alanine scanning — systematic replacement of each residue with alanine — is the most common SAR method for peptide ligands. The resulting activity data is visualized by mapping the log-transformed potency change onto the structure:

```python
# In PyMOL, set B-factors to Δlog(EC₅₀) scanning data
alter sele and resi 1, b=0.3
alter sele and resi 2, b=-0.1
# ... for all residues
spectrum b, blue_white_red, sele and name CA
show spheres, sele and name CA
set sphere_scale, 0.5
```

Blue spheres indicate positions where alanine substitution improved activity (negative Δlog(EC₅₀)); red spheres indicate positions critical for activity (positive Δlog(EC₅₀)). The size of each sphere can be scaled by the absolute magnitude of the effect. This technique transforms a table of scanning data into an immediately interpretable 3D figure.

### Pharmacophore Mapping

A pharmacophore is the ensemble of steric and electronic features necessary for optimal supramolecular interactions with a biological target. Pharmacophore visualization abstracts the peptide structure into a set of feature points: hydrogen-bond donors (green), hydrogen-bond acceptors (red), hydrophobic centroids (yellow), positively ionizable groups (blue), and negatively ionizable groups (orange), together with their relative spatial arrangement.

In practice, pharmacophore models are generated by tools such as Schrödinger Phase, MOE, or LigandScout, then exported as feature coordinates. These can be rendered in PyMOL as spheres or as custom CGO (Compiled Graphics Objects) shapes. The key figure types are:

- **Feature-point overlay on the peptide structure**: semi-transparent peptide cartoon with opaque pharmacophore features shown as colored spheres. Demonstrates which parts of the peptide participate in target recognition.
- **Pharmacophore in the binding pocket**: receptor surface with the pharmacophore features nested inside, showing complementarity between ligand features and receptor environment.
- **Shape-based pharmacophore**: a molecular shape representation (Connolly surface or Gaussian volume) colored by pharmacophoric feature type, which communicates steric constraints for analog design.

### Figure Design Principles for SAR Communication

The difference between a confusing SAR figure and a clear one often comes down to adherence to several design principles:

1. **One figure, one message**: A figure showing alanine-scanning results should not simultaneously try to communicate hydrogen-bond networks, electrostatic potential, and conformational dynamics. Split complex stories across multiple panels.

2. **Consistent color language**: If red means "loss of activity" in one panel, it must not mean "gain of activity" in another panel of the same figure. Define a color key and enforce it across all panels.

3. **Labeling what matters**: Residue labels should be placed only on positions with significant SAR effects. Labeling every residue adds visual noise and obscures the signal.

4. **Multiple views of the same object**: A key interaction interface is rarely visible from a single viewing angle. Two orthogonal views (rotated 90° apart) with synchronized color schemes allow the reader to build a three-dimensional mental model.

5. **Reference the data source**: Every SAR figure should include, in its legend or as a supplementary table, the raw activity data from which the visualization was derived. The figure communicates the pattern; the table provides the evidence.

## Research Evidence

The techniques described in this article draw on a substantial body of peer-reviewed research in structural biology visualization, molecular graphics, and computational chemistry.

| Study | Key Finding | Relevance to Peptide Visualization |
|-------|------------|-------------------------------------|
| Richardson (1981) | Introduced the ribbon diagram formalism | Foundation of all secondary structure visualization; the visual grammar that every ribbon representation inherits |
| Humphrey et al. (1996) | VMD: Visual Molecular Dynamics | Established trajectory visualization with multi-frame rendering and interactive analysis |
| DeLano (2002) | PyMOL as an open-source molecular visualization system | The most widely used structural visualization tool in the peptide and protein community |
| Pettersen et al. (2004) | UCSF Chimera — a visualization system for exploratory research | Introduced the extensible plugin architecture adopted by ChimeraX and inspired modern interactive analysis |
| Baker et al. (2001) | Electrostatics of nanosystems: application to microtubules and the ribosome | APBS: the standard Poisson-Boltzmann solver underlying most electrostatic surface visualization |
| Chen et al. (2010) | MolProbity: all-atom structure validation for macromolecular crystallography | Defined the Ramachandran validation criteria (favored, allowed, outlier) used in contemporary plots |
| Pettersen et al. (2021) | UCSF ChimeraX: structure visualization for researchers, educators, and developers | Modern successor to Chimera with GPU-accelerated rendering, ambient occlusion, and real-time ray tracing |
| Goddard et al. (2018) | UCSF ChimeraX: meeting modern challenges in visualization and analysis | Detailed the ChimeraX rendering pipeline and interactive analysis capabilities for MD trajectories |
| Lovell et al. (2003) | Structure validation by Cα geometry: φ, ψ and Cβ deviation | Defined the updated Ramachandran plot boundaries including pre-proline and glycine-specific contours |
| Schrödinger LLC (2021) | PyMOL 2.5: enhanced rendering, APBS integration, and trajectory analysis | Benchmark of the modern PyMOL feature set for peptide structure and dynamics visualization |
| Grant et al. (2006) | Bio3d: an R package for the comparative analysis of protein structures | Principal component analysis of MD trajectories and free energy landscape construction methodology |
| Ramachandran et al. (1963) | Stereochemistry of polypeptide chain configurations | Original description of the φ/ψ dihedral angle space and allowed conformations of peptide backbones |
| Berman et al. (2000) | The Protein Data Bank | The universal repository of macromolecular structures; the starting point for essentially all peptide structure visualization |
| Jurrus et al. (2018) | Improvements to the APBS biomolecular solvation software suite | Modernized APBS with GPU acceleration and improved numerical solvers for more accurate electrostatic surfaces |
| Daura et al. (1999) | Peptide folding: when simulation meets experiment | Established cluster analysis of MD trajectories and the free energy landscape approach for peptide conformational sampling |

## Frequently Asked Questions

<div class="faq-container">

<div class="faq-item" markdown="1">
### What is the difference between PyMOL and ChimeraX for peptide visualization?

PyMOL and ChimeraX serve overlapping but distinct niches. PyMOL excels at publication-quality static images and has an extremely efficient command-line interface that rewards scripting. ChimeraX offers superior real-time rendering (GPU-accelerated ambient occlusion, shadows, and silhouette edges), better built-in analysis tools (Ramachandran plots, Coulombic surface coloring, MD trajectory playback), and an integrated Python 3 environment. For a typical peptide structure figure, both tools can produce journal-quality output. The choice often depends on whether your workflow emphasizes scripting (favoring PyMOL) or interactive exploration and built-in analysis (favoring ChimeraX). Many structural biology groups use both — ChimeraX for exploration and analysis, PyMOL for final figure rendering.
</div>

<div class="faq-item" markdown="1">
### How do I choose the right color scheme for my peptide structure figure?

The color scheme should serve the scientific message. For showing secondary structure, use the classic Richardson palette (α-helix red, β-strand yellow, loop green). For highlighting a peptide ligand against its receptor, use gray for the receptor and a bold color (orange or magenta) for the peptide. For displaying conformational flexibility, use a B-factor blue-white-red spectrum. For multiple chains in a complex, use distinct colors per chain that can be distinguished when printed in grayscale (vary lightness, not just hue). Avoid rainbow color maps for quantitative data — they introduce perceptual artifacts. Tools like ColorBrewer and the viridis/magma/inferno palettes provide perceptually uniform alternatives.
</div>

<div class="faq-item" markdown="1">
### What resolution should I use when exporting figures from PyMOL?

For journal publication, export at 300 dpi minimum, scaled to the target column width. A single-column figure in most journals is 85–90 mm (3.35–3.54 inches), so at 300 dpi you need at least 1000 × 1000 pixels. For a full-page figure (170–180 mm), target 2000+ pixels on the long axis. In PyMOL, use `ray 2400, 2400` followed by `png figure.png, dpi=300`. The ray-tracing step (`ray`) renders the image at the specified resolution before the `png` command writes it. For ChimeraX, use `save image.png width 2400 height 2400 supersample 3 transparentBackground false`.
</div>

<div class="faq-item" markdown="1">
### How do I show hydrogen bonds in my peptide structure visualization?

In PyMOL, hydrogen bonds are detected and displayed using the `show sticks` representation combined with `distance` measurements. Use `hide everything, all; show cartoon, all; show sticks, resi 1-30` (adjust residue range) to show the peptide backbone and side chains. Then use `distance hbonds, (donor), (acceptor), 3.5, mode=2` to draw dashed lines between hydrogen-bond donors and acceptors within 3.5 Å. The `mode=2` flag draws dashed cylinders rather than simple lines, which produces a three-dimensional appearance. For ChimeraX, the `hbonds` command with `distSlop 0.4` and `angleSlop 20` provides equivalent functionality with the added option to color H-bonds by geometry quality.
</div>

<div class="faq-item" markdown="1">
### What is a Ramachandran plot and what does it tell me about peptide structure quality?

A Ramachandran plot displays the backbone dihedral angles φ (phi) and ψ (psi) for every residue in a peptide or protein structure. Because steric clashes between main-chain atoms restrict which φ/ψ combinations are physically possible, residues from well-refined structures cluster in specific "allowed" regions. Plotting a structure's residues on these contours reveals outliers — residues with improbable backbone geometry — that indicate errors in the structure determination or unusual conformational strain. A high-quality peptide structure should have >98% of residues in the favored regions and 0% in the outlier regions. Glycine (flexible) and proline (constrained) populate distinct regions, so separate contours are used for these residue types. The plot is named after G.N. Ramachandran, who first mapped the sterically allowed backbone conformations in 1963.
</div>

<div class="faq-item" markdown="1">
### How can I visualize molecular dynamics simulation results for a peptide?

The standard workflow loads the trajectory into a visualization program and applies three analytical views. First, calculate RMSD over time and plot it to confirm that the simulation has equilibrated. Second, compute per-residue RMSF and map the values onto the 3D structure using B-factor coloring — red regions are flexible, blue regions are rigid. Third, overlay 10–20 equally spaced trajectory frames as semi-transparent cartoons to produce a dynamic ensemble view that reveals the range of sampled conformations. For peptides with multiple conformational states, construct a free energy landscape by projecting the trajectory onto two key collective variables (often the first two principal components) and plotting ΔG = −kT ln(P) using a blue (minimum) to red (barrier) color scale. ChimeraX's built-in trajectory playback (`coordset`) and PyMOL's multi-state rendering both support these workflows.
</div>

<div class="faq-item" markdown="1">
### What are the key differences between solvent-accessible surface, solvent-excluded surface, and van der Waals surface?

The van der Waals surface is the union of atomic spheres — spiky, showing interstitial crevices between atoms. The solvent-accessible surface (SAS; also called the Lee-Richards surface) is traced by the center of a spherical probe (typically 1.4 Å radius, simulating water) as it rolls over the van der Waals surface. It smooths over small crevices but can miss narrow pockets. The solvent-excluded surface (SES; also called the molecular surface or Connolly surface) is traced by the inward-facing contact points of the probe sphere. It preserves narrow clefts and pockets that the SAS smooths over, making it the preferred representation for binding-site analysis. In PyMOL, `show surface` generates the SES by default. In ChimeraX, `surface` also generates the SES; use `surface style solvent` for the SAS variant.
</div>

<div class="faq-item" markdown="1">
### How do I prepare a peptide-receptor complex figure for publication?

Start with the receptor rendered as a pale, semi-transparent surface (gray or very light blue at 40–60% transparency) to define the binding pocket. Show the peptide as a cartoon with a bold, opaque color — orange, magenta, or deep teal work well against gray. Display key interacting side chains from both peptide and receptor as sticks with atom-type coloring (carbon matches the parent molecule's color, oxygen red, nitrogen blue, sulfur yellow). Add hydrogen bonds as yellow dashed lines using the PyMOL `distance` command or ChimeraX `hbonds`. Consider including two orthogonal views (related by a 90° rotation about the vertical axis) to give the reader a three-dimensional understanding of the interface. Include distance labels for 2–3 key interactions. Use a clean white or very light gray background. Export at a minimum of 300 dpi for the target column width.
</div>

<div class="faq-item" markdown="1">
### Can I use free/open-source tools instead of PyMOL (which requires a license)?

Yes. UCSF ChimeraX is free for academic use and provides most capabilities described in this article, including ribbon diagrams, surface rendering, electrostatic potential mapping, Ramachandran plots, and MD trajectory playback. VMD (Visual Molecular Dynamics) from the University of Illinois is also free and open-source, with particular strength in trajectory visualization and analysis — it was designed specifically for MD simulation data. For web-based visualization without software installation, NGL Viewer and Mol* (the successor to LiteMol and the PDB's standard viewer) provide interactive 3D rendering in the browser. NGL Viewer can load PDB files, display cartoons and surfaces, and color by residue property, B-factor, or conservation. For command-line rendering in automated pipelines, PyMOL's open-source variant and the VMD command-line mode (`vmd -dispdev text`) can generate publication-quality figures programmatically without a GUI.
</div>

<div class="faq-item" markdown="1">
### How do I calculate and display electrostatic potential on a peptide surface?

The standard pipeline uses the Adaptive Poisson-Boltzmann Solver (APBS) to compute the electrostatic potential, then maps the results onto the molecular surface. In PyMOL: (1) prepare the structure with `h_add` to add hydrogens; (2) launch the APBS plugin from the Plugin menu; (3) select the AMBER or CHARMM force field for radius and charge assignment; (4) set the dielectric constants (ε_protein = 2, ε_solvent = 78.5) and ionic strength (0.150 M for physiological conditions); (5) run the calculation; (6) the potential is automatically loaded and mapped onto the surface with the standard red-white-blue color scale. In ChimeraX, use `coulombic sel protein palette -10 red 0 white 10 blue` for a streamlined single-command workflow. For comparing peptide analogs, render each electrostatic surface using identical parameters (grid spacing, dielectric constants, color scale) so that differences reflect real changes in charge distribution rather than differences in visualization settings.
</div>

</div>

## References

1. Richardson, J. S. (1981). The anatomy and taxonomy of protein structure. *Advances in Protein Chemistry*, 34, 167–339. DOI: [10.1016/S0065-3233(08)60520-3](https://doi.org/10.1016/S0065-3233(08)60520-3)

2. Humphrey, W., Dalke, A., & Schulten, K. (1996). VMD: Visual molecular dynamics. *Journal of Molecular Graphics*, 14(1), 33–38. DOI: [10.1016/0263-7855(96)00018-5](https://doi.org/10.1016/0263-7855(96)00018-5)

3. DeLano, W. L. (2002). PyMOL: An open-source molecular graphics tool. *CCP4 Newsletter on Protein Crystallography*, 40, 82–92.

4. Pettersen, E. F., Goddard, T. D., Huang, C. C., Couch, G. S., Greenblatt, D. M., Meng, E. C., & Ferrin, T. E. (2004). UCSF Chimera — a visualization system for exploratory research and analysis. *Journal of Computational Chemistry*, 25(13), 1605–1612. DOI: [10.1002/jcc.20084](https://doi.org/10.1002/jcc.20084)

5. Baker, N. A., Sept, D., Joseph, S., Holst, M. J., & McCammon, J. A. (2001). Electrostatics of nanosystems: application to microtubules and the ribosome. *Proceedings of the National Academy of Sciences*, 98(18), 10037–10041. DOI: [10.1073/pnas.181342398](https://doi.org/10.1073/pnas.181342398)

6. Chen, V. B., Arendall, W. B., Headd, J. J., Keedy, D. A., Immormino, R. M., Kapral, G. J., Murray, L. W., Richardson, J. S., & Richardson, D. C. (2010). MolProbity: all-atom structure validation for macromolecular crystallography. *Acta Crystallographica Section D*, 66(1), 12–21. DOI: [10.1107/S0907444909042073](https://doi.org/10.1107/S0907444909042073)

7. Pettersen, E. F., Goddard, T. D., Huang, C. C., Meng, E. C., Couch, G. S., Croll, T. I., Morris, J. H., & Ferrin, T. E. (2021). UCSF ChimeraX: structure visualization for researchers, educators, and developers. *Protein Science*, 30(1), 70–82. DOI: [10.1002/pro.3943](https://doi.org/10.1002/pro.3943)

8. Goddard, T. D., Huang, C. C., Meng, E. C., Pettersen, E. F., Couch, G. S., Morris, J. H., & Ferrin, T. E. (2018). UCSF ChimeraX: meeting modern challenges in visualization and analysis. *Protein Science*, 27(1), 14–25. DOI: [10.1002/pro.3235](https://doi.org/10.1002/pro.3235)

9. Lovell, S. C., Davis, I. W., Arendall, W. B., de Bakker, P. I. W., Word, J. M., Prisant, M. G., Richardson, J. S., & Richardson, D. C. (2003). Structure validation by Cα geometry: φ, ψ and Cβ deviation. *Proteins: Structure, Function, and Bioinformatics*, 50(3), 437–450. DOI: [10.1002/prot.10286](https://doi.org/10.1002/prot.10286)

10. Schrödinger, LLC. (2021). The PyMOL Molecular Graphics System, Version 2.5. https://pymol.org

11. Grant, B. J., Rodrigues, A. P. C., ElSawy, K. M., McCammon, J. A., & Caves, L. S. D. (2006). Bio3d: an R package for the comparative analysis of protein structures. *Bioinformatics*, 22(21), 2695–2696. DOI: [10.1093/bioinformatics/btl461](https://doi.org/10.1093/bioinformatics/btl461)

12. Ramachandran, G. N., Ramakrishnan, C., & Sasisekharan, V. (1963). Stereochemistry of polypeptide chain configurations. *Journal of Molecular Biology*, 7(1), 95–99. DOI: [10.1016/S0022-2836(63)80023-6](https://doi.org/10.1016/S0022-2836(63)80023-6)

13. Berman, H. M., Westbrook, J., Feng, Z., Gilliland, G., Bhat, T. N., Weissig, H., Shindyalov, I. N., & Bourne, P. E. (2000). The Protein Data Bank. *Nucleic Acids Research*, 28(1), 235–242. DOI: [10.1093/nar/28.1.235](https://doi.org/10.1093/nar/28.1.235)

14. Jurrus, E., Engel, D., Star, K., Monson, K., Brandi, J., Felberg, L. E., Brookes, D. H., Wilson, L., Chen, J., Liles, K., Chun, M., Li, P., Gohara, D. W., Dolinsky, T., Konecny, R., Koes, D. R., Nielsen, J. E., Head-Gordon, T., Geng, W., … Baker, N. A. (2018). Improvements to the APBS biomolecular solvation software suite. *Protein Science*, 27(1), 112–128. DOI: [10.1002/pro.3280](https://doi.org/10.1002/pro.3280)

15. Daura, X., van Gunsteren, W. F., & Mark, A. E. (1999). Folding–unfolding thermodynamics of a β-heptapeptide from equilibrium simulations. *Proteins: Structure, Function, and Bioinformatics*, 34(3), 269–280. DOI: [10.1002/(SICI)1097-0134(19990215)34:3<269::AID-PROT1>3.0.CO;2-3](https://doi.org/10.1002/(SICI)1097-0134(19990215)34:3%3C269::AID-PROT1%3E3.0.CO;2-3)

---

*For high-purity research peptides suitable for X-ray crystallography, NMR spectroscopy, and computational modeling studies, explore the [RPL Peptides product catalog](https://rplpeptides.com). Access supporting analytical data including LC-MS, HPLC, and structural characterization at the [RPL Peptides Data Portal](https://data.rplpeptides.com).*

Return to [Interactive Figures](index.md).
