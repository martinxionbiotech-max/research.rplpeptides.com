---
title: "Bioinformatics Visualization for Peptide Research: Sequence Logos, Heatmaps, Networks, and Automated Pipelines"
description: "Master bioinformatics visualization for peptides — sequence logos, phylogenetic trees, heatmaps, volcano plots, protein-protein interaction networks, and automated PyMOL scripting pipelines."
slug: bioinformatics-visualization-peptides
category: Interactive Figures
tags: [Bioinformatics, Sequence Logo, Phylogenetic Tree, Heatmap, Volcano Plot, Network Graph, PyMOL Scripting, Data Visualization]
author: RPL Peptides Research Team
published: 2026-08-07
---

# Bioinformatics Visualization for Peptide Research: Sequence Logos, Heatmaps, Networks, and Automated Pipelines

## Executive Summary

Bioinformatics visualization transforms high-dimensional peptide sequence and interaction data into interpretable graphical representations that reveal evolutionary conservation, expression patterns, structure-activity relationships, and molecular interaction networks. This article provides a comprehensive guide to six core bioinformatics visualization modalities for peptide research: sequence logos for conservation analysis, phylogenetic trees for evolutionary context, heatmaps for high-throughput data, volcano plots for differential analysis, network graphs for protein-peptide interactions, and automated PyMOL scripting pipelines for high-throughput structural visualization. Each section covers underlying methodology, software implementation, interpretation strategies, and publication-quality figure design. The article concludes with a practical framework for building an end-to-end bioinformatics visualization pipeline that takes raw sequence or omics data and produces journal-ready figures through reproducible, scripted workflows. For peptide researchers seeking rigorously characterized materials for computational validation studies, [RPL Peptides](https://rplpeptides.com) provides analytical-grade peptides, with downloadable characterization data available at [data.rplpeptides.com](https://data.rplpeptides.com).

## Background

The peptide bioinformatics landscape has been transformed by the convergence of three forces: the explosion of publicly available sequence data (UniProt now contains over 250 million sequences), the maturation of machine learning methods for sequence and structure prediction (AlphaFold, ESMFold, ProtGPT2), and the development of specialized visualization libraries that translate abstract computational outputs into biologically interpretable graphics. A peptide researcher in 2026 can, within a single afternoon, retrieve all known sequences of a peptide hormone family, align them, compute a sequence logo, build a phylogenetic tree, map conservation onto an AlphaFold-predicted structure, and overlay known functional residue annotations — a workflow that would have required months of computation and custom programming a decade ago.

Yet the accessibility of these tools creates a new challenge: generating figures is easy, but generating figures that communicate biological insight is not. Default software settings produce generic outputs that obscure as often as they reveal. A sequence logo with default color and scaling parameters may fail to distinguish between functionally critical conservation and stochastic sequence identity. A heatmap with the wrong color palette can create or erase apparent clusters. A network graph laid out by a force-directed algorithm without biological constraints may scatter functionally related nodes to opposite quadrants of the figure.

This article addresses both the "how" and the "why" of bioinformatics visualization for peptides. Each section provides the computational foundations, the practical commands, and — critically — the design principles that separate informative figures from default outputs. The final section on automated pipelines addresses the reproducibility crisis in computational peptide research: a figure that cannot be regenerated from scripted commands is not a scientific result; it is an anecdote.

## Sequence Logos: Visualizing Conservation and Information Content

### Theoretical Foundation

A sequence logo is a graphical representation of a multiple sequence alignment (MSA) in which each position is represented by a stack of letters whose heights are proportional to their frequency at that position, weighted by the information content of the position. The total height of the stack at position *i* is the information content *R_i*:

$$R_i = \log_2(20) - (H_i + e_n)$$

where $H_i = -\sum_{a} f_{a,i} \log_2(f_{a,i})$ is the Shannon entropy at position $i$, $f_{a,i}$ is the observed frequency of amino acid $a$ at position $i$, and $e_n$ is a small-sample correction term that accounts for the finite number of sequences in the alignment. The correction term is given by:

$$e_n = \frac{s - 1}{2\ln(2) \cdot n}$$

where $s$ is the number of distinct amino acid types (typically 20, but may be fewer for gapped positions) and $n$ is the number of sequences in the alignment.

The log₂(20) = 4.32 bits represents the maximum possible information content — a position that is perfectly conserved (one amino acid at 100% frequency) carries log₂(20) bits of information, while a position with all 20 amino acids at equal frequency carries zero bits. Within each stack, the height of an individual amino acid letter is proportional to its weighted frequency: $f_{a,i} \times R_i$.

This formulation, due to Schneider and Stephens (1990), has an elegant information-theoretic interpretation: the logo displays how much a sequence alignment tells us about which residues are expected at each position, measured in bits.

### Software and Implementation

The most widely used tools for sequence logo generation are:

- **WebLogo 3** (Crooks et al., 2004): The classic web-server implementation. Accepts aligned FASTA sequences and produces publication-quality logos with customizable color schemes, ranging from simple black-on-white to chemistry-based coloring (hydrophobic in black, polar in green, positively charged in blue, negatively charged in red, etc.).
- **ggseqlogo** (Wagih, 2017): An R package based on ggplot2 that provides programmatic control over every aspect of the logo. This is the recommended tool for automated pipelines and for generating multi-panel figures where the logo must be consistent with other ggplot2-based plots.
- **Logomaker** (Tareen & Kinney, 2020): A Python package that generates sequence logos as matplotlib figures. Particularly useful for integrating logos into Python-based bioinformatics workflows.
- **Skylign**: A web-based tool that can generate logos from HMM (hidden Markov model) profiles in addition to MSAs, providing a profile-based alternative to alignment-based logos.

A typical ggseqlogo command in R for peptide analysis:

```r
library(ggseqlogo)
library(ggplot2)

# Read aligned peptide sequences (FASTA format)
seqs <- read_fasta("peptide_msa.fasta")

# Generate logo with chemistry coloring
ggseqlogo(seqs, method = "bits", seq_type = 'aa',
          col_scheme = 'chemistry') +
  theme_minimal() +
  labs(title = "Sequence Conservation: GLP-1 Peptide Family",
       x = "Position", y = "Information Content (bits)") +
  theme(axis.text.x = element_text(size = 8),
        plot.title = element_text(hjust = 0.5, size = 12))
```

### Figure Design Principles for Sequence Logos

The default sequence logo is rarely publication-ready. The following design interventions elevate a raw logo to a scientific figure:

1. **Consistent color chemistry**: Use the RasMol amino acid color scheme or the Taylor scheme, both of which group chemically similar residues. This is not merely aesthetic — a reviewer should be able to identify the physicochemical character of conserved positions without consulting a color key.

2. **Annotate known functional residues**: Above the logo, add markers for residues with experimentally characterized functional roles. Arrowheads, asterisks, or small colored bars above specific positions immediately connect evolutionary conservation to functional importance.

3. **Include a secondary structure bar**: Below the logo, display the consensus secondary structure (α-helix as a coiled line or red bar, β-strand as an arrow, loop as a thin line). This reveals whether conserved positions cluster in specific secondary structure elements.

4. **Align with a representative sequence**: Below the secondary structure bar, show a single representative peptide sequence (the most common sequence, the human sequence, or the consensus) in a monospaced font, providing a concrete amino acid reference for each position.

5. **Number the positions**: Either the MSA position number or the residue number in a reference sequence should be displayed along the x-axis. For long peptides (>30 residues), stagger the position numbers to avoid crowding.

6. **Control the y-axis maximum**: Setting $y_{max}$ to $\log_2(20)$ (4.32 bits) provides a consistent reference across all logos in a publication. If the logo is normalized differently, state the normalization explicitly in the legend.

### Applications in Peptide Research

Sequence logos serve five principal purposes in peptide research:

- **Identifying conserved functional motifs**: The GLP-1 peptide family, for example, shows strong conservation at residues His7, Gly10, Phe12, Thr13, Asp15, and Leu26 — positions that are known to be involved in receptor binding or structural stabilization. A logo of 50+ GLP-1 family sequences makes this conservation pattern immediately visible.

- **Comparing orthologs across species**: Logos for a peptide hormone from mammals, fish, and reptiles reveal lineage-specific conservation patterns. Residues conserved across all vertebrates are likely essential for structure or function; residues conserved only within mammals may reflect mammalian-specific receptor interactions.

- **Synthetic library design guidance**: When designing a peptide library for lead optimization, a logo of active analogs reveals which positions tolerate substitution (low information content) and which do not (high information content), informing library diversity.

- **Evaluating alignment quality**: A logo with uniform information content near zero across all positions suggests a misalignment (randomly arranged sequences). Conversely, a logo with blocks of high information content separated by gaps suggests an alignment containing insertions that is still informative.

- **Validating structure predictions**: Comparing a logo with an AlphaFold-predicted structure reveals whether conserved positions map to the structural core (expected) or to surface loops (surprising, and worth investigating).

## Phylogenetic Trees for Peptide Families

### Tree Construction Methods

Phylogenetic trees for peptide sequences illustrate evolutionary relationships and enable functional inference through orthology and paralogy analysis. The construction workflow proceeds in four stages:

1. **Multiple sequence alignment**: Use MAFFT (Katoh & Standley, 2013) with the L-INS-i algorithm for peptide families (<100 sequences) or the FFT-NS-2 algorithm for larger families. The `--auto` flag selects the appropriate strategy automatically.

2. **Tree inference**: For peptide sequences, maximum-likelihood methods (IQ-TREE, RAxML, or PhyML) are preferred over distance methods (neighbor-joining) because amino acid substitution models (LG, WAG, JTT, or the model selected automatically by IQ-TREE's ModelFinder) better capture the evolutionary process than simple distance metrics. An IQ-TREE command for a typical peptide family:

```bash
iqtree -s peptide_alignment.fasta -m MFP -B 1000 -alrt 1000 -nt AUTO
```

The `-m MFP` flag invokes ModelFinder to select the optimal substitution model. `-B 1000` performs 1000 ultrafast bootstrap replicates. `-alrt 1000` performs the SH-aLRT branch test for an additional support metric.

3. **Bayesian alternatives**: For smaller datasets where model uncertainty is a concern, MrBayes provides a Bayesian framework that integrates over substitution model parameters. Bayesian posterior probabilities and maximum-likelihood bootstrap values are complementary and often reported together.

4. **Rooting**: Peptide trees should be rooted by an appropriate outgroup — typically a paralogous peptide from a distantly related family or, when available, a truly distant ortholog (e.g., a basal vertebrate sequence when studying mammal-specific peptide evolution).

### Tree Visualization with ggtree

ggtree (Yu et al., 2017) is the dominant tool for publication-quality phylogenetic tree visualization. It extends the ggplot2 framework to tree objects and supports layered annotation with heatmaps, bar charts, and sequence data.

A production-quality tree visualization in R:\n\n```r\nlibrary(ggtree)\nlibrary(ggplot2)\nlibrary(treeio)\n\n# Read IQ-TREE output\ntree <- read.iqtree("peptide_alignment.fasta.treefile")

# Base tree with bootstrap support
p <- ggtree(tree, layout = "rectangular", size = 0.4) +
  geom_tiplab(size = 2.5, offset = 0.02, fontface = "italic") +
  geom_nodepoint(aes(subset = UFboot >= 95), color = "black", size = 1.5) +
  geom_nodepoint(aes(subset = UFboot >= 70 & UFboot < 95),
                 color = "gray50", size = 1) +
  xlim(0, 1.5) +
  theme_tree2()

# Add activity heatmap to the right
p2 <- gheatmap(p, activity_data, offset = 0.05, width = 0.2,
               colnames_angle = 45, font.size = 2) +
  scale_fill_viridis_c(option = "plasma", name = "log(EC50)")

print(p2)
```

### Figure Design Principles for Peptide Phylogenetic Trees

1. **Support values**: Bootstrap support (≥70%) or posterior probabilities (≥0.95) should be displayed at internal nodes. Use filled circles (color-coded by support level) rather than raw numbers, which create visual clutter. The standard convention: black circle = strong support, gray = moderate, no circle = weak or not supported.

2. **Tip label formatting**: Species names should be in the standard binomial format (italicized for publication). For large trees (>50 sequences), tip labels may be abbreviated to the genus initial and species epithet, with a full table of sequence identifiers in supplementary information.

3. **Scale bar**: Every tree must include a scale bar showing substitutions per site. The scale bar should be placed at a position where it does not overlap with any tree branch or annotation.

4. **Layout choice**: Rectangular (cladogram) layouts are standard for publications. Circular layouts are space-efficient for large trees (>100 sequences) but make it harder to visually trace specific branches. For comparative figures (e.g., a peptide family tree alongside its receptor family tree), tanglegram layouts that connect corresponding tips with lines are increasingly popular.

5. **Contextual annotation layers**: The most informative peptide trees overlay multiple data layers: (a) an activity heatmap showing functional potency for each sequence against a panel of receptors; (b) a bar chart of peptide length or physicochemical properties; (c) symbols indicating whether the sequence has been experimentally characterized (filled) or is predicted (open); and (d) colored strips marking taxonomic groups or functional classes.

### Practical Applications

In peptide drug discovery, phylogenetic trees serve as target-selection tools. A tree of venom peptides from cone snails (conotoxins), annotated with ion-channel subtype selectivity data, reveals evolutionary lineages that are selectively active against specific human ion-channel subtypes — a phylogenetic shortcut to target identification. Similarly, a tree of antimicrobial peptide sequences from frogs, annotated with minimal inhibitory concentration (MIC) data against MRSA, can guide the selection of candidate sequences for synthesis and testing based on their proximity to high-activity orthologs.

## Heatmaps for High-Throughput Peptide Data

### Data Structure and Preprocessing

Heatmaps are the default visualization for two-dimensional matrices where rows represent peptides (or peptide features) and columns represent experimental conditions (or samples). In peptide research, common heatmap data types include:

- **Alanine scanning matrices**: rows = residue positions (1 to n), columns = receptor subtypes, values = Δlog(EC₅₀) relative to wild-type.
- **Expression matrices**: rows = peptide precursor genes, columns = tissue types or cell lines, values = normalized expression level (log₂ fold change or transcripts per million).
- **Binding affinity matrices**: rows = peptide variants, columns = target proteins, values = Kd (nM).
- **Physicochemical property fingerprints**: rows = peptide sequences, columns = calculated properties (hydrophobicity, net charge, isoelectric point, helical propensity, etc.), values = property values.

Before visualization, data should be preprocessed: missing values imputed (using k-nearest neighbors or column means for small datasets), values scaled (z-score normalization per row or column), and clustering performed if desired (hierarchical clustering with Euclidean distance and Ward's linkage for rows, correlation distance for columns).

### The pheatmap and ComplexHeatmap Ecosystems

In R, `pheatmap` provides a straightforward interface for standard heatmaps, while `ComplexHeatmap` (Gu et al., 2016) enables multi-layer annotated heatmaps with row and column annotations, multiple color scales, and custom legends. For peptide research, ComplexHeatmap is the recommended tool because peptide data almost always benefits from stratification by physicochemical property, functional class, or taxonomic origin.

A typical ComplexHeatmap for alanine scanning data:

```r
library(ComplexHeatmap)
library(circlize)

# Data matrix: rows = positions, columns = receptor subtypes
# Values = log2 fold change in EC50 relative to wild-type

# Color scale centered at zero
col_fun <- colorRamp2(c(-3, 0, 3), c("blue", "white", "red"))

# Row annotation: secondary structure
row_anno <- rowAnnotation(
  SecondaryStructure = anno_block(
    gp = gpar(fill = c("red", "yellow", "green")),
    labels = c("α-Helix", "Loop", "β-Strand"),
    labels_gp = gpar(col = "white", fontsize = 8)
  )
)

# Main heatmap
Heatmap(data_matrix,
        name = "log2(ΔEC50)",
        col = col_fun,
        cluster_rows = FALSE,
        cluster_columns = TRUE,
        row_split = structure_groups,
        column_title = "Receptor Subtype",
        row_title = "Residue Position",
        cell_fun = function(j, i, x, y, width, height, fill) {
          if(abs(data_matrix[i, j]) > 1.5)
            grid.text(sprintf("%.1f", data_matrix[i, j]), x, y,
                      gp = gpar(fontsize = 6))
        })
```

### Figure Design Principles for Peptide Heatmaps

1. **Color scale centered at zero for comparative data**: For alanine-scanning and differential expression data, the color scale must be symmetric around zero (or 1.0 for fold-change data), with zero mapped to a neutral color (white, light gray). Asymmetric color scales create the illusion of effects where none exist.

2. **Perceptually uniform color palettes**: The viridis palette family (viridis, magma, inferno, plasma) is perceptually uniform, colorblind-friendly, and prints well in grayscale. For diverging data, the RdBu (red-white-blue) palette from RColorBrewer is standard. Avoid the default rainbow palette — it is perceptually nonlinear and creates artifacts.

3. **Cell-level annotation for key values**: For matrices with clear "hits" (strongly positive or negative values), annotating individual cells with their numeric values improves interpretability. Use a threshold to avoid annotating every cell — only annotate values with |z-score| > 1.5 or |log₂FC| > 1.

4. **Row and column grouping with labeled blocks**: Splitting rows by secondary structure type, domain, or functional class provides immediate structural context. Block labels should be clearly visible and use a distinct color for each category.

5. **Include a data density sidebar**: A small histogram or density plot alongside the heatmap color scale shows the distribution of values, helping the reader calibrate visual interpretation ("are these values mostly near zero, or is there a broad spread?").

6. **Whitespace spacing for grouped heatmaps**: When displaying multiple heatmaps side by side (e.g., binding data for three different peptide families), insert a thin white gap (1–2 mm) between heatmap blocks to provide visual separation without wasting space.

## Volcano Plots for Differential Peptide Analysis

### Construction and Interpretation

A volcano plot displays the statistical significance (negative log₁₀ of the p-value, on the y-axis) against the magnitude of the effect (log₂ fold change, on the x-axis) for each peptide, gene, or feature in a comparison between two conditions. The plot's name derives from its characteristic shape: as the fold change increases, statistical significance rises, producing two "flanks" that resemble a volcanic eruption.

For peptide-level differential analysis (e.g., comparing the peptidome of treated vs. untreated cells, or comparing peptide abundances between disease and healthy tissue), the volcano plot is the primary visualization because it simultaneously communicates effect size and statistical confidence.

In R with ggplot2:

```r
library(ggplot2)
library(ggrepel)

ggplot(volcano_data, aes(x = log2FC, y = -log10(pvalue))) +
  geom_point(aes(color = significance), size = 0.8, alpha = 0.6) +
  scale_color_manual(values = c("Not Significant" = "gray70",
                                 "Significant" = "steelblue",
                                 "Upregulated" = "firebrick",
                                 "Downregulated" = "royalblue")) +
  geom_vline(xintercept = c(-1, 1), linetype = "dashed", color = "gray50") +
  geom_hline(yintercept = -log10(0.05), linetype = "dashed", color = "gray50") +
  geom_text_repel(data = subset(volcano_data, label == TRUE),
                  aes(label = peptide_id), size = 3, max.overlaps = 30) +
  labs(x = expression(log[2]~"(Fold Change)"),
       y = expression(-log[10]~"(p-value)"),
       title = "Differential Peptide Abundance: Treatment vs. Control") +
  theme_minimal(base_size = 11)
```

### Design Principles for Volcano Plots

1. **Threshold lines clearly shown**: Vertical dashed lines at the chosen fold-change threshold (typically |log₂FC| > 1, corresponding to a twofold change) and a horizontal dashed line at the chosen significance threshold (typically p < 0.05, or the Bonferroni-corrected threshold for multiple testing). The lines should be dashed (not dotted, which are harder to see) and rendered in a visible gray (not too faint).

2. **Four-class coloring**: Points should be colored into four categories: (a) significantly upregulated (log₂FC > threshold, p < significance), in red; (b) significantly downregulated (log₂FC < −threshold, p < significance), in blue; (c) non-significant but beyond the fold-change threshold, in light gray; and (d) below both thresholds, in very light gray. This coloring scheme is universally understood in the omics community.

3. **Label top hits**: The 5–15 most significant or most changed peptides should be labeled by their identifier (sequence or gene name). Use `ggrepel` to avoid label overlap. Do not label more than 20 points — the volcano plot should communicate the distribution, and excessive labeling obscures it.

4. **Symmetrical x-axis**: The x-axis range should be symmetric around zero (e.g., [-5, 5] for log₂FC) so that up- and down-regulation are visually balanced. An asymmetric axis misleads the reader about the relative distribution of positive and negative effects.

5. **Report the number of significant features**: In a corner of the plot, display text annotations: "n_up = 47, n_down = 23, p < 0.05, |log₂FC| > 1". This saves the reader from counting and provides immediate quantitative context.

### Enhanced Volcano Plots

For peptide-specific applications, enhanced volcano plots can encode additional dimensions:

- **Point size proportional to peptide abundance**: Larger points for more abundant peptides, which typically have more reliable statistical metrics.
- **Point shape indicating peptide length or charge class**: Circles for neutral peptides, triangles for positively charged, squares for negatively charged.
- **Marginal histograms**: Add density plots or histograms along the top (log₂FC distribution) and right (−log₁₀(p) distribution) axes using the `ggExtra` package's `ggMarginal` function.
- **Enrichment highlighting**: Color a subset of points belonging to a pathway or functional category of interest (e.g., "GPCR Ligands" in yellow) to highlight enrichment of that category among regulated peptides.

## Network Graphs for Peptide-Protein Interactions

### Network Construction

Network graphs represent peptides and their interacting partners (proteins, receptors, other peptides) as nodes, connected by edges representing experimentally determined or predicted interactions. The three most common network types in peptide bioinformatics are:

1. **Protein-peptide interaction (PepPI) networks**: Peptides as query nodes connected to their protein binding partners. Edge weights can represent binding affinity (Kd), interaction probability, or experimental confidence.

2. **Peptide similarity networks**: Peptides as nodes connected by edges weighted by sequence identity, structural similarity, or shared functional annotation. These networks reveal clusters of functionally related peptides.

3. **Signaling cascade networks**: Peptide hormones, their receptors, downstream effectors, and transcriptional targets as nodes in a directed graph. Edge direction indicates signal flow; edge weight can indicate response magnitude.

Interaction data sources include:

| Database | Content | Peptide Relevance |
|----------|---------|-------------------|
| STRING | Functional protein association networks | Includes peptide hormones and their receptor interactions |
| BioGRID | Curated protein-protein, genetic, and chemical interactions | High-quality peptide-receptor and peptide-modulator interactions |
| IntAct/IMEx | Molecular interaction database | Manually curated peptide-binding interactions with affinity data |
| PepBDB | Peptide-binding protein database | Peptide-protein complex structures with binding affinity |
| PDBbind | Binding affinity data for biomolecular complexes | Experimentally measured Kd/Ki values for peptide-protein complexes |
| DEPOD | Human dephosphorylation database | Peptide substrates for phosphatases |

### Visualization with Cytoscape

Cytoscape (Shannon et al., 2003) remains the standard for interactive network visualization, and the RCy3 package provides programmatic control from R. For Python users, NetworkX combined with its matplotlib-based drawing functions provides equivalent functionality.

A production-quality workflow for a peptide-protein interaction network:

1. Query STRING or BioGRID for interactions of a query peptide family.
2. Import into Cytoscape via a tab-delimited file (source node, target node, interaction type, confidence score).
3. Apply an edge-weighted spring-embedded layout (or a prefuse force-directed layout for larger networks) to position nodes based on connectivity.
4. Style nodes by molecular type (peptide hormones = large circles, receptors = squares, signaling proteins = triangles).
5. Color nodes by functional category (e.g., GPCR class, enzyme family).
6. Size nodes by degree centrality or betweenness centrality to highlight network hubs.
7. Export as SVG for final annotation.

### ggraph for Programmatic Network Figures

The ggraph R package (Pedersen, 2021) extends ggplot2 to network data, enabling fully programmatic, reproducible network figure generation:

```r
library(ggraph)
library(tidygraph)
library(igraph)

# Create graph from edge list
graph <- tbl_graph(nodes = node_data, edges = edge_data,
                   directed = FALSE)

ggraph(graph, layout = "stress") +
  geom_edge_link(aes(edge_width = confidence),
                 alpha = 0.3, color = "gray50") +
  geom_node_point(aes(size = degree, color = category),
                  alpha = 0.85) +
  geom_node_text(aes(label = name, filter = degree > 10),
                 size = 3, repel = TRUE) +
  scale_color_brewer(palette = "Set2") +
  scale_edge_width(range = c(0.1, 2)) +
  theme_graph() +
  labs(title = "GLP-1 Receptor Signaling Network")
```

### Design Principles for Peptide Interaction Networks

1. **Layout driven by biology, not algorithm defaults**. Force-directed layouts (Fruchterman-Reingold, Kamada-Kawai) distribute nodes evenly but may scatter functionally related nodes. Constrain receptor nodes to the center, peptide ligands to the periphery, and downstream effectors in between, using layout constraints or manual positioning.

2. **Node size proportional to connectivity**: Larger nodes for highly connected proteins (hubs) communicate network topology at a glance. Degree centrality, betweenness centrality, or the total number of interactions are all valid sizing metrics — choose the one most relevant to your biological question and state the metric in the legend.

3. **Edge transparency for dense networks**: For networks with >100 edges, set edge alpha to 0.15–0.30. This allows the reader to perceive edge density (darker regions have more edges) without each individual edge becoming a visual obstacle.

4. **Multi-edge bundling**: When multiple peptides interact with the same receptor (or vice versa), edge bundling merges overlapping edges into a thicker bundle, reducing visual clutter. The ggraph package supports edge bundling through the `geom_edge_bundle_path` geometry.

5. **Dual-layer visualization for structural context**: The most advanced network figures overlay the abstract graph with structural information: a peptide-receptor interaction edge is drawn as a line, and an inset shows the actual binding interface in a PyMOL ribbon rendering. This bridges the gap between systems-level and molecular-level understanding.

## Molecular Interaction Maps

Molecular interaction maps extend network visualization into the structural domain by projecting interaction data onto three-dimensional protein structures. For peptide research, the most common molecular interaction map is the receptor surface annotated with peptide-contact footprint: the receptor is rendered as a gray surface, and residues that contact the peptide (within 4–5 Å of any peptide atom in the complex structure) are highlighted in a distinct color. This visualization directly communicates the size, shape, and chemical character of the peptide-binding epitope.

The PyMOL script for generating an interaction footprint:

```python
# Load complex structure
fetch 6x18, async=0  # Example: peptide-GPCR complex

# Select peptide and receptor
select peptide, chain B
select receptor, chain A

# Find receptor residues within 5 Å of peptide
select contact, receptor within 5 of peptide

# Render receptor as gray surface, contact residues in orange
show surface, receptor
set surface_color, gray70, receptor
show surface, contact
set surface_color, orange, contact

# Show peptide as cartoon
show cartoon, peptide
set cartoon_color, magenta, peptide
color magenta, peptide

# Highlight key hydrogen bonds
distance hbonds, (peptide and name N+O), (receptor and name N+O), 3.5, mode=2
color yellow, hbonds

# Render and export
ray 2400, 2400
png interaction_footprint.png, dpi=300
```

## Automated PyMOL Scripting Pipeline

### Rationale for Scripted Visualization

Manual figure generation in PyMOL or ChimeraX is adequate for one-off figures but untenable for high-throughput analysis — a peptide library of 50 variants, each requiring a structural figure, cannot practically be visualized by hand. Scripting transforms visualization from a craft (one figure at a time) to a manufacturing process (hundreds of figures from a single command). Beyond throughput, scripting provides reproducibility: a scripted figure can be regenerated exactly when the underlying data changes, meeting the FAIR (Findable, Accessible, Interoperable, Reusable) data principles for computational research.

### Pipeline Architecture

A production-grade peptide visualization pipeline in PyMOL consists of:

1. **Input module**: Reads peptide sequences and activity data from a CSV or TSV file. Each row represents one peptide variant with its sequence, activity values (EC₅₀, Ki, etc.), and an identifier.

2. **Structure prediction module**: Calls an external folding tool (AlphaFold via ColabFold API, ESMFold, or a local Rosetta installation) to predict the three-dimensional structure of each peptide, or retrieves the structure from a template PDB via homology modeling.

3. **Property calculation module**: Computes electrostatic potential (via APBS), solvent-accessible surface area (via PyMOL's `get_area`), and hydrogen-bond satisfaction from the predicted structure.

4. **Rendering module**: Generates a standardized suite of figures for each peptide: (a) ribbon diagram with secondary structure coloring; (b) electrostatic surface map; (c) Ramachandran plot; (d) structure with activity data mapped onto residue positions via B-factor coloring.

5. **Export module**: Writes PNG files at 300 dpi and SVG vector files for each figure, organized into a per-peptide directory structure.

6. **Report generation module**: Compiles figures into a summary HTML or PDF report with activity tables.

### Implementation

A minimal but functional PyMOL scripting pipeline:

```python
#!/usr/bin/env python3
"""Automated peptide structure visualization pipeline."""

import os
import csv
import subprocess
from pathlib import Path

PEPTIDE_CSV = "peptide_library.csv"
OUTPUT_DIR = "output_figures"
PYMOL_EXEC = "pymol"

def generate_pymol_script(peptide_id, sequence, activity_data, output_path):
    """Generate a PyMOL script for one peptide."""
    script = f'''
# Auto-generated visualization script for {peptide_id}
# Structure must be pre-generated and named {peptide_id}.pdb

load {peptide_id}.pdb, obj
hide everything, all

# Panel 1: Ribbon diagram with secondary structure coloring
show cartoon, obj
set cartoon_fancy_helices, 1
set cartoon_cylindrical_helices, 1
color palecyan, obj and ss h
color pink, obj and ss s
color palegreen, obj and ss l+''

# Map activity data to B-factors
'''
    for residue, activity in activity_data.items():
        script += f'alter obj and resi {residue} and name CA, b={activity}\n'

    script += f'''
# Color by B-factor for activity visualization
spectrum b, blue_white_red, obj and name CA
show spheres, obj and name CA
set sphere_scale, 0.4

# Orient and render
orient obj
set ray_trace_mode, 3
set antialias, 2
set ray_shadow, 2
ray 2400, 2400

# Export
png {output_path}/{peptide_id}_ribbon.png, dpi=300

# Electrostatic surface (requires APBS pre-run)
# Load precomputed potential
load {peptide_id}_potential.dx, pot
show surface, obj
ramp_new e_pot, pot, [-5, 0, 5]
set surface_color, e_pot, obj
png {output_path}/{peptide_id}_electrostatics.png, dpi=300

# Ramachandran plot
hide surface, obj
ramachandran obj, dynamics=off
png {output_path}/{peptide_id}_rama.png, dpi=300

quit
'''
    return script


def main():
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

    with open(PEPTIDE_CSV, 'r') as f:\n        reader = csv.DictReader(f)\n        for row in reader:
            peptide_id = row['peptide_id']
            sequence = row['sequence']

            # Parse activity data from CSV columns (e.g., EC50_1, EC50_2, ...)
            activity_data = {}
            for key, value in row.items():
                if key.startswith('EC50_') and value:
                    residue_num = int(key.split('_')[1])
                    activity_data[residue_num] = float(value)

            # Generate PyMOL script
            script = generate_pymol_script(
                peptide_id, sequence, activity_data, OUTPUT_DIR)

            script_path = f"/tmp/pymol_script_{peptide_id}.pml"
            with open(script_path, 'w') as f_script:
                f_script.write(script)

            # Execute PyMOL
            subprocess.run(
                [PYMOL_EXEC, '-cq', script_path],
                check=True, timeout=300)

            print(f"Completed: {peptide_id}")

    print("Pipeline complete.")


if __name__ == '__main__':
    main()
```

### Pipeline Best Practices

1. **Version control for scripts and outputs**: Every script should carry a version number and a hash of the input data it processed. Figures should be tagged with generation metadata (date, script version, input data version) — either in the PNG metadata or in an accompanying JSON file.

2. **Consistent camera angles across variants**: When comparing 50 peptide variants, the camera orientation must be identical. Use PyMOL's `set_view` command with a pre-recorded view matrix rather than `orient`, which produces a variant-specific view.

3. **Parallelization at scale**: For libraries of more than 50 peptides, execute PyMOL instances in parallel using GNU Parallel or a Python `concurrent.futures` ProcessPoolExecutor. Each PyMOL instance requires approximately 1–2 GB RAM for a typical peptide.

4. **Incremental regeneration**: When one peptide's sequence or activity data changes, regenerate only that peptide's figures. A Makefile-based workflow with figure files as targets and input data as dependencies provides automatic incremental regeneration:

```makefile
OUTPUT_DIR = output_figures

all: $(shell cat peptide_ids.txt | sed 's/.*/$(OUTPUT_DIR)\/&_ribbon.png/')

$(OUTPUT_DIR)/%_ribbon.png: structures/%.pdb scripts/generate_figures.py
	pymol -cq scripts/generate_figures.py -- --peptide $*
```

5. **Quality control checkpoint**: After auto-generation, a QC script should check each figure for common rendering failures: images smaller than a minimum pixel threshold (indicating a render failure), blank images (all pixels the same color), and figures where the peptide is not visible (e.g., `orient` placed it behind the camera). Flagged figures should be logged for manual inspection.

## Research Evidence

The visualization methods described in this article are grounded in decades of research in bioinformatics, computational biology, and data visualization design.

| Study | Key Finding | Relevance to Peptide Bioinformatics Visualization |
|-------|------------|---------------------------------------------------|
| Schneider & Stephens (1990) | Introduced the information-theoretic formulation of sequence logos | Foundation of all modern sequence logo visualization; the Rᵢ = log₂(20) − Hᵢ formula used universally |
| Crooks et al. (2004) | WebLogo: a sequence logo generator | Established the web-based sequence logo standard with customizable chemistry-based coloring |
| Wagih (2017) | ggseqlogo: a versatile R package for drawing sequence logos | Brought sequence logos into the ggplot2 ecosystem, enabling programmatic figure generation |
| Tareen & Kinney (2020) | Logomaker: beautiful sequence logos in Python | Extended logo generation to Python, enabling integration with scikit-learn and PyTorch workflows |
| Katoh & Standley (2013) | MAFFT multiple sequence alignment software version 7 | The standard aligner for peptide MSA; L-INS-i algorithm optimized for short peptide sequences |
| Yu et al. (2017) | ggtree: an R package for visualization and annotation of phylogenetic trees | The dominant tool for publication-quality phylogenetic figure generation with multi-layer annotation |
| Gu et al. (2016) | ComplexHeatmap: a package for making complex heatmaps in R | Established the layered-heatmap paradigm with row/column annotations essential for peptide data |
| Shannon et al. (2003) | Cytoscape: a software environment for integrated models of biomolecular interaction networks | The standard platform for interactive protein-peptide interaction network visualization |
| Pedersen (2021) | ggraph: an implementation of grammar of graphics for graphs and networks | Extended ggplot2 to network visualization, bringing programmatic figure generation to interaction maps |
| Szklarczyk et al. (2021) | The STRING database in 2021: customizable protein–protein networks | The most comprehensive source of functional interaction data including peptide signaling networks |
| Jumper et al. (2021) | Highly accurate protein structure prediction with AlphaFold | Transformed peptide structure prediction; the source of coordinates for structure-based bioinformatics visualization |
| Cock et al. (2009) | Biopython: freely available Python tools for computational molecular biology and bioinformatics | The foundational Python library providing sequence parsing, alignment, and analysis tools for visualization pipelines |
| O'Donoghue et al. (2010) | Aquaria: simplifying discovery in the age of sequence data | Demonstrated the power of mapping sequence conservation onto 3D structures — a visualization paradigm now standard in peptide bioinformatics |
| Wilkinson et al. (2016) | The FAIR Guiding Principles for scientific data management and stewardship | Established the reproducibility requirements (Findable, Accessible, Interoperable, Reusable) that scripted visualization pipelines are designed to satisfy |
| Tufte (2001) | The Visual Display of Quantitative Information | The design principles — maximize data-ink ratio, eliminate chartjunk, use small multiples — that apply universally to bioinformatics figure design |

## Frequently Asked Questions

<div class="faq-container">

<div class="faq-item" markdown="1">
### What is the difference between information content and conservation in a sequence logo?

Information content (Rᵢ, measured in bits) is a position-level metric that quantifies how much a sequence alignment tells us about which residues are expected at that position, compared to a uniform background distribution. Conservation, by contrast, is often operationalized as the frequency of the most common amino acid at that position. A position where one residue appears at 90% frequency has high conservation but lower information content than a position where three chemically similar residues (e.g., Leu, Ile, Val) each appear at ~33% — the latter position tells us the chemical character is conserved (hydrophobic) but the specific identity varies. Sequence logos display information content, which captures both the degree of conservation and the number of functionally equivalent alternatives. This is why a logo is more informative than a simple consensus sequence: it reveals positions where multiple chemically distinct solutions are evolutionarily viable.
</div>

<div class="faq-item" markdown="1">
### Which amino acid substitution model should I use for peptide phylogenetic trees?

For most peptide families, use IQ-TREE's ModelFinder (`-m MFP`) to automatically select the best-fitting substitution model. However, general guidance based on empirical studies: the LG model (Le & Gascuel, 2008) is the default for general-purpose amino acid phylogenetics and outperforms older models (WAG, JTT) in most benchmarks. For peptide families with unusual amino acid compositions — such as antimicrobial peptides rich in Lys and Arg, or collagen peptides rich in Gly and Pro — specialized models (mtZOA for mitochondrial, FLU for influenza, HIVb for HIV) may fit better, but ModelFinder will identify these automatically. The critical principle is not the specific model but that it is selected based on data (AIC, BIC, or cross-validation) rather than assuming the default. Report the model used and its selection criterion in every tree figure legend.
</div>

<div class="faq-item" markdown="1">
### How do I choose between hierarchical clustering and k-means for my peptide heatmap?

The choice depends on the shape of your data and your biological question. Hierarchical clustering (HC) with Ward's linkage minimizes within-cluster variance and produces a dendrogram — a tree that visualizes the clustering hierarchy, which is informative when you want to understand relationships at multiple levels of granularity. k-means partitions data into k pre-specified clusters and is faster for large datasets (>1000 rows). For peptide data, HC is almost always preferred because: (a) peptide datasets are typically small enough (<500 peptides) that HC's O(n²) complexity is not problematic; (b) the dendrogram provides biological insight — are peptides from the same family clustering together? Are functional subfamilies recovered?; and (c) k-means requires specifying k in advance, which in exploratory peptide analysis is usually unknown. If you use k-means, report the gap statistic or silhouette score used to select k.
</div>

<div class="faq-item" markdown="1">
### What is the best way to label significant peptides in a volcano plot?

Use the `ggrepel` package's `geom_text_repel` with sensible parameters to avoid overlapping labels. Key settings: (a) `max.overlaps = 15` to limit the number of labels (it's better to label the 15 most important peptides clearly than to label 50 illegibly); (b) `box.padding = 0.5` to provide space around each label; (c) `segment.color = "gray50"` to draw thin connector lines from label to point; (d) `force = 2` to increase repulsion between labels. Pre-filter your data: only label peptides that satisfy both |log₂FC| > 2 and −log₁₀(p) > 5, or the top 10–20 peptides by a composite score (e.g., |log₂FC| × −log₁₀(p)). The labels should be peptide identifiers (gene symbols for endogenous peptides, sequence codes for synthetic variants), not accession numbers, which are uninformative to readers. For synthetic peptide libraries, label by the mutation (e.g., "A12K" for an Ala→Lys substitution at position 12).
</div>

<div class="faq-item" markdown="1">
### How can I annotate a phylogenetic tree with functional data?

The ggtree package in R provides the most flexible annotation framework. Using the `%<+%` operator to join external data frames to the tree object, you can add annotation layers including: (a) colored strips (heatmap rings in circular trees, horizontal bars in rectangular trees) indicating taxonomic group, functional class, or experimental status; (b) bar charts at tip positions showing quantitative data (peptide length, net charge, activity); (c) symbols at tips indicating properties (filled = experimentally validated activity, open = predicted); and (d) text labels with support values at internal nodes. The key design principle is to use annotation layers that complement the tree topology — a tree of GLP-1 family peptides benefits from a bar chart of GLP-1R activation potency at the tips, because the reader can immediately assess whether potency clusters on specific branches.
</div>

<div class="faq-item" markdown="1">
### What causes the "exploding volcano" effect in my volcano plot?

The "exploding volcano" occurs when one or a few peptides have extremely small p-values (e.g., p < 10⁻³⁰⁰) that push the y-axis maximum so high that most points are compressed into the bottom of the plot. This is common in proteomics and peptidomics experiments with large sample sizes and high-precision measurements. The fix is to cap the y-axis at a reasonable maximum, such as −log₁₀(p) = 10 (p = 10⁻¹⁰) or 15 (p = 10⁻¹⁵), and render points beyond this cap as triangles at the top edge of the plot with a note in the legend: "△ p < 10⁻¹⁰" (where the exponent matches your cap). This preserves the distribution of all points while still identifying the extreme outliers. Always state the cap in the figure legend.
</div>

<div class="faq-item" markdown="1">
### How do I choose between Cytoscape and ggraph for network visualization?

Cytoscape excels at interactive exploration — you can click on nodes, filter by attribute, search for specific peptides, and iteratively refine the layout. Use Cytoscape during the exploratory data analysis phase when you are discovering network structure. ggraph (in R) excels at programmatic, reproducible figure generation — every element of the plot is specified in code, the figure can be regenerated exactly from the script, and it integrates with the ggplot2 ecosystem for consistent styling across figure types. Use ggraph for publication figures. A productive workflow uses Cytoscape for exploration, exports the final layout coordinates, and replots in ggraph for the publication figure, preserving the interactively chosen layout while gaining reproducibility.
</div>

<div class="faq-item" markdown="1">
### What file formats should I use for bioinformatics figures in publications?

For vector graphics (preferred for figures composed of lines, text, and simple shapes — including phylogenetic trees, heatmaps, and volcano plots): export as SVG or PDF. SVG is editable in Inkscape and Illustrator; PDF embeds fonts and is the preferred format for most journals. Avoid EPS for complex figures with many data points, as it becomes impractically large. For raster graphics (preferred for 3D molecular structures, density maps, and anything with gradients or transparency): export as PNG at 300 dpi minimum, with dimensions matched to the target column width (85 mm single column, 170 mm double column). For supplementary figures that may be zoomed, export at 600 dpi. Never export publication figures as JPEG — compression artifacts degrade text and fine lines. For interactive web supplements, export as interactive HTML (plotly for R/Python figures, NGL Viewer for structural figures) that readers can rotate, zoom, and explore.
</div>

<div class="faq-item" markdown="1">
### How can I integrate AlphaFold structures into my visualization pipeline?

AlphaFold-predicted structures are PDB-format files that can be loaded into PyMOL or ChimeraX just like experimentally determined structures, but they require two additional considerations. First, AlphaFold provides per-residue confidence scores (pLDDT) in the B-factor column — use these to color the structure by confidence (blue for high confidence pLDDT > 90, yellow for medium 70–90, orange/red for low <70) so readers can assess which regions of the figure are reliable. Second, AlphaFold typically predicts a single conformation, which may not represent the peptide's dynamic ensemble in solution — consider running a short molecular dynamics simulation (10–50 ns) on the AlphaFold prediction and visualizing the trajectory ensemble as described in the structure visualization article. For automated pipelines, call AlphaFold via the ColabFold API (`colabfold_batch`) or the ESMFold API, both of which accept FASTA sequences and return PDB-format coordinates in under a minute for typical peptide lengths.
</div>

<div class="faq-item" markdown="1">
### What are the common mistakes in bioinformatics figure design and how do I avoid them?

The five most common mistakes: (1) **Default software color schemes** — WebLogo's default coloring, ggtree's default tip labels, and ComplexHeatmap's default color scale are not publication-quality. Always customize colors to your data and maintain consistency across all figures in a manuscript. (2) **Missing scale bars, legends, or axis labels** — a tree without a scale bar, a heatmap without a labeled color scale, or a volcano plot without threshold lines are incomplete figures. Every figure should be interpretable without reading the main text. (3) **Overplotting** — labeling too many points, displaying every edge in a dense network, or showing every residue in a sequence logo for a 200-residue alignment creates visual noise that obscures signal. Filter, aggregate, and display only what matters. (4) **Inconsistent units and normalization** — if one heatmap shows z-scores and another shows raw values, or if one tree uses substitutions/site and another uses raw distance, the reader cannot compare figures. Standardize across figures. (5) **Irreproducible figures** — a figure generated by clicking through a GUI, without a script that can regenerate it from the raw data, is not a scientific result. Script every figure in R, Python, or PyMOL command files, and commit the scripts alongside the raw data.
</div>

</div>

## References

1. Schneider, T. D., & Stephens, R. M. (1990). Sequence logos: a new way to display consensus sequences. *Nucleic Acids Research*, 18(20), 6097–6100. DOI: [10.1093/nar/18.20.6097](https://doi.org/10.1093/nar/18.20.6097)

2. Crooks, G. E., Hon, G., Chandonia, J. M., & Brenner, S. E. (2004). WebLogo: a sequence logo generator. *Genome Research*, 14(6), 1188–1190. DOI: [10.1101/gr.849004](https://doi.org/10.1101/gr.849004)

3. Wagih, O. (2017). ggseqlogo: a versatile R package for drawing sequence logos. *Bioinformatics*, 33(22), 3645–3647. DOI: [10.1093/bioinformatics/btx469](https://doi.org/10.1093/bioinformatics/btx469)

4. Tareen, A., & Kinney, J. B. (2020). Logomaker: beautiful sequence logos in Python. *Bioinformatics*, 36(7), 2272–2274. DOI: [10.1093/bioinformatics/btz921](https://doi.org/10.1093/bioinformatics/btz921)

5. Katoh, K., & Standley, D. M. (2013). MAFFT multiple sequence alignment software version 7: improvements in performance and usability. *Molecular Biology and Evolution*, 30(4), 772–780. DOI: [10.1093/molbev/mst010](https://doi.org/10.1093/molbev/mst010)

6. Yu, G., Smith, D. K., Zhu, H., Guan, Y., & Lam, T. T.-Y. (2017). ggtree: an R package for visualization and annotation of phylogenetic trees with their covariates and other associated data. *Methods in Ecology and Evolution*, 8(1), 28–36. DOI: [10.1111/2041-210X.12628](https://doi.org/10.1111/2041-210X.12628)

7. Gu, Z., Eils, R., & Schlesner, M. (2016). Complex heatmaps reveal patterns and correlations in multidimensional genomic data. *Bioinformatics*, 32(18), 2847–2849. DOI: [10.1093/bioinformatics/btw313](https://doi.org/10.1093/bioinformatics/btw313)

8. Shannon, P., Markiel, A., Ozier, O., Baliga, N. S., Wang, J. T., Ramage, D., Amin, N., Schwikowski, B., & Ideker, T. (2003). Cytoscape: a software environment for integrated models of biomolecular interaction networks. *Genome Research*, 13(11), 2498–2504. DOI: [10.1101/gr.1239303](https://doi.org/10.1101/gr.1239303)

9. Pedersen, T. L. (2021). ggraph: an implementation of grammar of graphics for graphs and networks. R package version 2.0.5. https://CRAN.R-project.org/package=ggraph

10. Szklarczyk, D., Gable, A. L., Nastou, K. C., Lyon, D., Kirsch, R., Pyysalo, S., Doncheva, N. T., Legeay, M., Fang, T., Bork, P., Jensen, L. J., & von Mering, C. (2021). The STRING database in 2021: customizable protein–protein networks, and functional characterization of user-uploaded gene/measurement sets. *Nucleic Acids Research*, 49(D1), D605–D612. DOI: [10.1093/nar/gkaa1074](https://doi.org/10.1093/nar/gkaa1074)

11. Jumper, J., Evans, R., Pritzel, A., Green, T., Figurnov, M., Ronneberger, O., Tunyasuvunakool, K., Bates, R., Žídek, A., Potapenko, A., Bridgland, A., Meyer, C., Kohl, S. A. A., Ballard, A. J., Cowie, A., Romera-Paredes, B., Nikolov, S., Jain, R., Adler, J., … Hassabis, D. (2021). Highly accurate protein structure prediction with AlphaFold. *Nature*, 596(7873), 583–589. DOI: [10.1038/s41586-021-03819-2](https://doi.org/10.1038/s41586-021-03819-2)

12. Cock, P. J. A., Antao, T., Chang, J. T., Chapman, B. A., Cox, C. J., Dalke, A., Friedberg, I., Hamelryck, T., Kauff, F., Wilczynski, B., & de Hoon, M. J. L. (2009). Biopython: freely available Python tools for computational molecular biology and bioinformatics. *Bioinformatics*, 25(11), 1422–1423. DOI: [10.1093/bioinformatics/btp163](https://doi.org/10.1093/bioinformatics/btp163)

13. O'Donoghue, S. I., Gavin, A.-C., Gehlenborg, N., Goodsell, D. S., Hériché, J.-K., Nielsen, C. B., North, C., Olson, A. J., Procter, J. B., Shattuck, D. W., Walter, T., & Wong, B. (2010). Visualizing biological data — now and in the future. *Nature Methods*, 7(3s), S2–S4. DOI: [10.1038/nmeth.f.301](https://doi.org/10.1038/nmeth.f.301)

14. Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., Appleton, G., Axton, M., Baak, A., Blomberg, N., Boiten, J. W., da Silva Santos, L. B., Bourne, P. E., Bouwman, J., Brookes, A. J., Clark, T., Crosas, M., Dillo, I., Dumon, O., Edmunds, S., Evelo, C. T., Finkers, R., … Mons, B. (2016). The FAIR Guiding Principles for scientific data management and stewardship. *Scientific Data*, 3, 160018. DOI: [10.1038/sdata.2016.18](https://doi.org/10.1038/sdata.2016.18)

15. Tufte, E. R. (2001). *The Visual Display of Quantitative Information* (2nd ed.). Graphics Press. ISBN: 978-1930824133.

---

*For research-grade peptides suitable for bioinformatics-driven discovery, computational modeling, and experimental validation studies, explore the catalog at [RPL Peptides](https://rplpeptides.com). Download supporting analytical characterization data from the [RPL Peptides Data Portal](https://data.rplpeptides.com).*

Return to [Interactive Figures](index.md).
