---
title: In Silico Peptide Design — Rosetta, AlphaFold & De Novo Generation
description: "Comprehensive guide to computational peptide design using Rosetta, AlphaFold, RoseTTAFold, ESM-2, and generative models including ProteinGAN and PepGNN for stability, solubility, and activity optimization."
---

# In Silico Peptide Design — Rosetta, AlphaFold & De Novo Generation

<div class="quick-fact">
  <strong>Key Summary:</strong> In silico peptide design leverages computational methods to engineer peptide sequences with desired structures and functions. From physics-based design with Rosetta to deep learning-based structure prediction with AlphaFold and RoseTTAFold, and generative models including ProteinGAN and PepGNN, these tools enable rational optimization of peptide stability, solubility, binding affinity, and biological activity.
</div>

## Executive Summary

The rational design of peptides with tailored structural and functional properties represents a frontier in computational biology. Where traditional peptide discovery relied on screening natural sources or synthetic libraries, in silico design enables researchers to computationally explore sequence space, predict structural consequences, and optimize for desired properties before a single peptide is synthesized. This article provides a comprehensive overview of the computational tools and methodologies used for in silico peptide design, spanning physics-based approaches implemented in the Rosetta macromolecular modeling suite, deep learning-based structure prediction with AlphaFold and RoseTTAFold, protein language model representations from ESM-2, de novo peptide generation using generative adversarial networks (ProteinGAN) and graph neural networks (PepGNN), and sequence optimization strategies for stability, solubility, and biological activity. Whether designing stabilized analogs of natural bioactive peptides, creating entirely novel peptide scaffolds, or optimizing therapeutic candidates for drug-like properties, these computational approaches are transforming the efficiency and scope of peptide engineering. The integration of these tools into coherent design-build-test-learn cycles, supported by resources at [RPL Peptides](https://rplpeptides.com), represents the modern paradigm for peptide discovery and development.

## Background

The challenge of peptide design emerges from the vastness of sequence space. For a peptide of only 20 amino acids, there are 20²⁰ (approximately 1.05 × 10²⁶) possible sequences — a number far exceeding what can be explored experimentally. Computational methods address this challenge by guiding experimental efforts toward regions of sequence space most likely to yield peptides with desired properties.

The history of computational protein and peptide design traces back to the 1980s with pioneering work on side-chain packing algorithms by Ponder and Richards ([Ponder & Richards, 1987](https://doi.org/10.1016/0022-2836(87)90358-6)). The development of physics-based energy functions that could accurately evaluate sequence-structure compatibility enabled the first successful computational designs of protein structures in the late 1990s. The Rosetta software suite, initiated by David Baker's laboratory at the University of Washington, has become the most widely used platform for macromolecular design, with applications ranging from enzyme design to vaccine immunogen engineering ([Leaver-Fay et al., 2011](https://doi.org/10.1016/B978-0-12-381270-4.00019-6)).

The deep learning revolution in structural biology, catalyzed by AlphaFold's breakthrough performance in the CASP14 (Critical Assessment of Structure Prediction) competition in 2020, fundamentally changed the landscape of computational peptide design ([Jumper et al., 2021](https://doi.org/10.1038/s41586-021-03819-2)). AlphaFold demonstrated that highly accurate protein structure prediction from sequence alone was achievable, opening new possibilities for computational design by enabling rapid, accurate evaluation of designed sequences. RoseTTAFold, developed contemporaneously by the Baker laboratory, provided a complementary three-track neural network architecture integrating sequence, distance, and coordinate information ([Baek et al., 2021](https://doi.org/10.1126/science.abj8754)).

The emergence of protein language models, particularly the ESM (Evolutionary Scale Modeling) family developed by Meta AI, introduced a new paradigm. These models, trained on hundreds of millions of protein sequences, learn rich representations of protein sequence-structure relationships that can be leveraged for design tasks ([Lin et al., 2023](https://doi.org/10.1126/science.ade2574)). ESM-2, with up to 15 billion parameters, captures evolutionary constraints and biophysical principles that inform peptide design.

Generative models for peptide design represent the most recent advance, applying architectures from machine learning — generative adversarial networks (GANs), variational autoencoders (VAEs), and graph neural networks (GNNs) — to generate novel peptide sequences with desired properties. These approaches enable exploration of sequence space beyond natural peptides, potentially discovering functional sequences that evolution has not explored.

## Physics-Based Design with Rosetta

### The Rosetta Molecular Modeling Suite

Rosetta is a comprehensive software platform for macromolecular modeling that encompasses structure prediction, design, and analysis. For peptide design, Rosetta provides a suite of protocols that enable sequence optimization for stability, binding affinity, and structural specificity.

The core of Rosetta's design methodology is the **packer**, an algorithm that searches the combinatorial space of amino acid identities and side-chain conformations (rotamers) at designable positions. The packer uses Monte Carlo simulated annealing or dead-end elimination (DDE) algorithms to identify low-energy sequence-structure combinations ([Leaver-Fay et al., 2011](https://doi.org/10.1016/B978-0-12-381270-4.00019-6)).

### Key Rosetta Protocols for Peptide Design

**FixBB (Fixed Backbone) Design:**
FixBB design optimizes amino acid identities on a fixed backbone scaffold, which is the most straightforward and computationally efficient design protocol. It is suitable when a desired backbone conformation is known — for example, when designing stabilized variants of a naturally occurring peptide or grafting a functional motif onto a new scaffold. The protocol iterates between sequence optimization (rotamer packing) and small backbone perturbations (minimization) to identify energetically favorable sequences.

**FlexPepDock:**
FlexPepDock is a specialized protocol for modeling and designing peptide-protein interactions ([London et al., 2011](https://doi.org/10.1093/nar/gkr352)). Unlike general protein-protein docking, FlexPepDock explicitly models peptide flexibility, which is essential for capturing the conformational changes that peptides often undergo upon binding. The protocol performs Monte Carlo simulations with increasing levels of peptide flexibility, from rigid-body optimization through full peptide backbone flexibility.

FlexPepDock applications include:
- Refining low-resolution peptide docking models to high-resolution accuracy
- Designing peptide sequences with improved binding affinity to target proteins
- Predicting the structural effects of sequence mutations on binding
- Identifying hotspot residues critical for peptide-protein recognition

**RosettaRemodel:**
RosettaRemodel enables the design of peptide sequences with specified secondary structure content and topology, with control over loop lengths and structural motifs ([Huang et al., 2011](https://doi.org/10.1371/journal.pone.0024109)). This is particularly useful for designing cyclic peptides, where backbone cyclization constraints must be satisfied, or for creating peptides with novel folds not observed in nature.

**CST Design (Constrained Design):**
This protocol enables the optimization of peptide sequences while satisfying user-defined geometric constraints, such as maintaining specific hydrogen bonds, metal coordination geometries, or inter-residue distances. Constrained design is essential when designing peptides to bind specific targets or mimic structural features of protein interaction interfaces.

**Generalized Kinematic Closure (GenKIC):**
For cyclic peptide and macrocycle design, GenKIC efficiently samples backbone conformations that satisfy cyclization geometry constraints while simultaneously designing amino acid identities. This represents the current state-of-the-art for computational design of cyclic peptides with drug-like properties ([Bhardwaj et al., 2016](https://doi.org/10.1038/nature19791)).

### Rosetta Energy Functions

Rosetta's design decisions are guided by energy functions that approximate the thermodynamic stability of sequence-structure combinations. The primary energy functions are:

- **ref2015 (REF15):** The standard energy function for protein design, incorporating van der Waals interactions (Lennard-Jones potential), electrostatics (Coulomb's law with distance-dependent dielectric), implicit solvation (Lazaridis-Karplus model), hydrogen bonding (orientation-dependent potential), and statistical terms (Ramachandran preferences, amino acid reference energies).
- **beta_nov16:** An energy function optimized for both protein and peptide design, with improvements in electrostatics and solvation terms that make it more suitable for short peptides where solvent exposure is maximal.
- **talaris2014:** An earlier energy function still used for applications where ref2015 may be overly stringent.

For peptide design, the choice of energy function can significantly impact design outcomes. Peptides are more solvent-exposed and conformationally flexible than globular proteins, making implicit solvation models and entropy estimation particularly important.

### Practical Rosetta Peptide Design Workflow

A typical Rosetta peptide design workflow proceeds as follows:

1. **Define the design goal:** Specify the target structure (e.g., α-helical, β-hairpin, cyclic) and desired properties (stability, solubility, binding affinity).
2. **Generate or obtain a starting backbone structure:** This may come from experimental structures (PDB), homology models, de novo structure generation (Rosetta blueprint builder), or structural prediction (AlphaFold).
3. **Identify designable and repackable residues:** Designable residues (amino acid identity can change), repackable residues (identity fixed, side-chain conformation can change), and frozen residues (neither changes).
4. **Generate an initial sequence:** Use the packer to identify an energetically favorable sequence on the fixed backbone.
5. **Iterative design:** Alternate between backbone relaxation (minimization with small perturbations) and sequence repacking to identify sequence-structure combinations with improved energy.
6. **Ensemble evaluation:** Generate multiple independently designed sequences and evaluate consensus — residues that are consistently selected across independent design trajectories are more likely to be functionally important.
7. **Filter by additional criteria:** Apply filters for solubility (e.g., net charge, hydrophobic patch size), aggregation propensity, and desired functional properties.
8. **Validate with orthogonal methods:** Use AlphaFold or RoseTTAFold to predict the structure of designed sequences, verifying that they fold to the desired topology.

## Deep Learning-Based Structure Prediction

### AlphaFold

AlphaFold, developed by DeepMind, represents a paradigm shift in computational structural biology. Its performance in CASP14 (2020) — achieving median Global Distance Test (GDT) scores exceeding 90 for difficult targets — demonstrated that the protein structure prediction problem, a grand challenge spanning five decades, had been largely solved for single-chain proteins ([Jumper et al., 2021](https://doi.org/10.1038/s41586-021-03819-2)).

AlphaFold's architecture integrates several innovations:
- **Evoformer:** A novel neural network module that processes multiple sequence alignments (MSAs) and pairwise residue representations, enabling the network to reason about evolutionary couplings and spatial relationships simultaneously.
- **Structure Module:** An SE(3)-equivariant transformer that iteratively refines 3D coordinates, ensuring that predictions are invariant to global rotation and translation.
- **Recycling:** Iterative refinement where predictions from previous iterations are fed back as input, progressively improving accuracy.

For peptide design, AlphaFold serves as a rapid validation tool: proposed designs can be evaluated by predicting their structures and comparing them to the intended fold. This closes the design-test loop without requiring experimental structure determination.

**AlphaFold-Multimer:** Extending AlphaFold to predict the structures of protein complexes, AlphaFold-Multimer is particularly relevant for designing peptide binders ([Evans et al., 2022](https://doi.org/10.1101/2021.10.04.463034)). By predicting the structure of a designed peptide in complex with its target protein, researchers can evaluate whether the peptide adopts the intended binding mode.

**AlphaFold2 for peptide-specific applications:**
- **Peptide binder design:** Validate whether designed peptides fold into the intended binding conformation.
- **Peptide stability prediction:** Compare AlphaFold confidence metrics (pLDDT, predicted aligned error) across sequence variants to identify stabilizing mutations.
- **Conformational ensemble prediction:** By subsampling MSAs or reducing input depth, explore the conformational landscape of designed peptides to assess structural specificity.

### RoseTTAFold

RoseTTAFold, developed by the Baker laboratory, employs a three-track architecture processing sequence, distance, and 3D coordinate information simultaneously ([Baek et al., 2021](https://doi.org/10.1126/science.abj8754)). This design provides complementary strengths to AlphaFold:

- **Direct coordinate prediction:** RoseTTAFold predicts 3D coordinates directly (rather than through a separate structure module), making it particularly useful for tasks requiring coordinate-based reasoning.
- **Two-track mode for protein design:** By constraining the sequence track to fixed coordinates, RoseTTAFold can be used in a "hallucination" mode to design sequences that fold into specified structures.
- **ProteinMPNN integration:** RoseTTAFold's structure prediction can be coupled with ProteinMPNN, an inverse folding model that designs sequences given backbone structures, for iterative structure-based design.

**ProteinMPNN:**
ProteinMPNN is a message-passing neural network trained for the inverse protein folding problem — predicting amino acid sequences that fold into given backbone structures ([Dauparas et al., 2022](https://doi.org/10.1126/science.add2187)). Key features relevant to peptide design include:
- **Sequence recovery:** ProteinMPNN recovers native sequences at rates exceeding 50%, significantly higher than physics-based methods.
- **Solubility-aware design:** Built-in parameters control the hydrophobicity of designed sequences, enabling specification of desired solubility.
- **Multichain design:** Simultaneously designs sequences for all chains in a complex, accounting for inter-chain interactions.
- **Temperature parameter:** Controls sequence diversity, allowing exploration of multiple design solutions.

The ProteinMPNN + AlphaFold/RoseTTAFold pipeline represents a powerful iterative design strategy: ProteinMPNN generates candidate sequences for a target backbone, structure prediction validates whether those sequences fold correctly, and the cycle repeats.

## Protein Language Models — ESM-2

### The ESM Family

The Evolutionary Scale Modeling (ESM) family of protein language models, developed by Meta AI, applies transformer architectures — originally developed for natural language processing — to protein sequences. ESM-2, the most recent and capable model in the series, has been trained on hundreds of millions of protein sequences from the UniRef database, learning rich representations that capture evolutionary, structural, and functional information ([Lin et al., 2023](https://doi.org/10.1126/science.ade2574)).

### How ESM-2 Represents Peptide Sequences

ESM-2 processes protein sequences as if they were sentences in a language, with amino acids as words. The model learns to predict masked (hidden) amino acids given their sequence context — a training objective known as masked language modeling. Through this training, the model's internal representations (embeddings) capture:

- **Evolutionary constraints:** Residue covariation patterns that reflect structural and functional constraints
- **Secondary structure propensity:** Helix, strand, and coil preferences
- **Solvent accessibility:** Buried versus exposed residue patterns
- **Contact predictions:** Which residue pairs are in spatial proximity
- **Functional site signatures:** Patterns characteristic of active sites, binding interfaces, and post-translational modification sites

For peptide design, ESM-2 embeddings provide a rich numerical representation that can be used as input to downstream predictors or as a foundation for generative design.

### ESM-2 Applications in Peptide Design

**Fitness Landscape Prediction:**
ESM-2 embeddings serve as input features for regression models that predict functional properties from sequence. The ESM-1v model, a variant trained to predict the effects of mutations, can estimate the functional impact of amino acid substitutions without requiring multiple sequence alignments ([Meier et al., 2021](https://doi.org/10.1101/2021.07.09.450648)). This enables zero-shot prediction of mutation effects, valuable for designing stabilized peptide variants.

**ESMFold:**
ESM-2's largest variant (15B parameters) can directly predict protein structures from single sequences without requiring MSA input. While less accurate than AlphaFold for challenging targets, ESMFold's single-sequence prediction is dramatically faster (seconds versus minutes/hours), enabling structure prediction at proteome scale. For peptide design, this speed enables rapid structural evaluation of thousands of candidate sequences.

**Sequence Optimization:**
By using the model's log-likelihood scores (how probable the model considers each amino acid at each position), researchers can identify mutations predicted to be evolutionarily plausible. This "evolutionary likelihood" approach has been used to design stabilized protein variants and can be applied to peptides ([Hie et al., 2021](https://doi.org/10.1038/s41587-021-00993-6)).

**Embedding-Based Design:**
ESM-2 embeddings can be used to compare designed sequences to natural sequences in embedding space, identifying design candidates that lie within the distribution of natural peptides (likely to be well-folded and functional) versus those far from it (possibly unstable or aggregation-prone).

## De Novo Peptide Generation

### Generative Adversarial Networks — ProteinGAN

ProteinGAN applies the generative adversarial network (GAN) framework to protein and peptide sequences ([Repecka et al., 2021](https://doi.org/10.1038/s42256-021-00310-5)). In the GAN framework, a generator network produces candidate sequences while a discriminator network attempts to distinguish generated sequences from natural ones. Through adversarial training, the generator learns to produce sequences that are indistinguishable from natural peptides.

Key features of ProteinGAN for peptide design:
- **Learns from unaligned sequences:** Unlike MSA-dependent methods, ProteinGAN can learn from diverse, unaligned sequences in a functional family.
- **Generates diverse candidates:** The model produces varied sequences that capture the distribution of the training data rather than converging to a single "optimal" sequence.
- **Functional enrichment:** Generated sequences are enriched for functional variants, with experimental validation showing that a substantial fraction of generated sequences retain or improve upon natural functionality.
- **Exploration of sequence space:** ProteinGAN can generate sequences with mutations at positions that are highly conserved in nature, potentially discovering functionally equivalent alternatives.

Limitations for peptide applications include the requirement for substantial training data (hundreds to thousands of related sequences) and the challenge of controlling for specific properties beyond sequence plausibility.

### Graph Neural Networks — PepGNN

PepGNN applies graph neural network approaches to peptide design, representing peptides as graphs where nodes are residues and edges represent spatial or sequential relationships ([Wan et al., 2022](https://doi.org/10.1093/bib/bbab557)). This representation captures the relational structure of peptides more naturally than linear sequence representations.

PepGNN capabilities include:
- **Structure-aware generation:** By incorporating 3D structural information into the graph representation, PepGNN can generate sequences compatible with specified backbone conformations.
- **Multi-property optimization:** The graph framework naturally handles multiple design objectives simultaneously (e.g., binding affinity, solubility, stability).
- **Interpretable design rationale:** Graph attention mechanisms can identify which residue interactions most influence design decisions, providing mechanistic insight.

### Variational Autoencoders (VAEs) for Peptides

Variational autoencoders learn a compressed latent representation of peptide sequences and can generate new sequences by sampling from this latent space. The continuous nature of the latent space enables smooth interpolation between known peptides and exploration of intermediate sequences.

VAE-based peptide design approaches include:
- **Latent space optimization:** Perform gradient-based optimization in the latent space to maximize predicted functional properties, then decode the optimized latent vector to obtain a peptide sequence.
- **Conditional generation:** Condition the decoder on desired property values (e.g., "generate a peptide with pI 8.5 and hydrophobicity 0.3"), enabling targeted generation.
- **Latent space interpolation:** Generate "hybrid" peptides by interpolating between the latent representations of different natural peptides.

### Autoregressive Language Models

Autoregressive models generate peptide sequences one amino acid at a time, conditioning each prediction on previously generated residues. ProtGPT2, based on the GPT-2 architecture and trained on protein sequence databases, can generate novel protein sequences with natural-like properties ([Ferruz et al., 2022](https://doi.org/10.1038/s41467-022-32007-7)).

For peptide design, autoregressive models offer:
- **Unconditional generation:** Produce novel peptide sequences that resemble natural sequences in their statistical properties.
- **Conditional generation:** Control generation by providing prefix sequences or property constraints.
- **Iterative refinement:** Generate multiple candidates and select those with desirable predicted properties.

## Sequence Optimization for Stability, Solubility, and Activity

### Stability Optimization

Peptide stability encompasses resistance to proteolytic degradation, thermal denaturation, and chemical modification. Computational approaches to stability optimization include:

- **Rosetta ΔΔG calculations:** The difference in Rosetta energy between wild-type and mutant sequences provides an estimate of the thermodynamic effect of mutations. The `ddg_monomer` protocol in Rosetta systematically evaluates all possible point mutations and identifies those predicted to be stabilizing.
- **FoldX:** The FoldX software suite provides empirical force field calculations for estimating mutation effects on protein stability ([Schymkowitz et al., 2005](https://doi.org/10.1093/nar/gki387)). While originally developed for proteins, FoldX can be applied to peptides with stable secondary structures.
- **ESM-1v zero-shot prediction:** The ESM-1v model predicts mutation effects using only sequence information, correlating with experimental stability measurements across diverse proteins.
- **DeepDDG and related methods:** Neural network-based predictors trained on experimental ΔΔG datasets can predict mutation effects with accuracy approaching experimental error.

For peptide-specific stability design, considerations include:
- **Backbone cyclization:** Computational prediction of favorable cyclization geometries using Rosetta GenKIC or molecular dynamics simulations.
- **Stapling design:** For α-helical peptides, prediction of optimal staple placement and chemistry (all-hydrocarbon, lactam, triazole).
- **N- and C-terminal modifications:** Evaluation of capping effects (N-terminal acetylation, C-terminal amidation) on folding stability.

### Solubility Optimization

Peptide solubility is a critical factor affecting synthesis yield, purification efficiency, and formulation feasibility. Computational solubility optimization includes:

- **Net charge engineering:** Ensuring a sufficient net charge (typically ≥ ±1 per 5 residues) at the working pH to prevent isoelectric precipitation.
- **Hydrophobic patch disruption:** Using Rosetta or custom scripts to identify contiguous hydrophobic surface patches and introduce polar or charged substitutions to break them up.
- **Aggregation propensity prediction:** Tools such as AGGRESCAN, TANGO, and PASTA predict aggregation-prone regions from sequence and suggest solubility-enhancing mutations ([Conchillo-Solé et al., 2007](https://doi.org/10.1186/1471-2105-8-65)).
- **Solubility predictors:** CamSol and SoluProt predict solubility from sequence using machine learning on experimental solubility datasets, enabling rapid screening of design candidates.
- **Glycosylation and PEGylation site introduction:** Computational identification of positions where solubility-enhancing modifications can be introduced without disrupting structure or function.

### Activity Optimization

Optimizing biological activity while maintaining favorable drug-like properties is the central challenge of therapeutic peptide design:

- **Binding affinity optimization:** Rosetta FlexPepDock and ProteinMPNN can identify mutations predicted to improve binding affinity through better shape complementarity, increased hydrogen bonding, or enhanced hydrophobic packing.
- **Selectivity engineering:** By comparing binding energies to the target versus off-target receptors, computational methods can identify mutations that maintain target affinity while reducing off-target binding — essential for minimizing side effects.
- **Proteolytic stability:** Combining structural prediction with knowledge of protease cleavage specificities, computational tools can predict proteolytic hotspots and suggest resistance-conferring mutations.
- **ADME property prediction:** Tools for predicting absorption, distribution, metabolism, and excretion properties of peptide therapeutics, including SwissADME and pkCSM, guide optimization toward drug-like candidates.
- **Multi-objective Pareto optimization:** Algorithms that simultaneously optimize multiple properties (affinity, stability, solubility, selectivity), identifying Pareto-optimal solutions where no property can be improved without sacrificing another.

## Research Evidence

Computational peptide design has been validated through numerous experimental studies:

| Study | Method | Key Finding | Reference |
|---|---|---|---|
| Cyclic peptide design | Rosetta GenKIC | Designed 18-47 residue cyclic peptides with atomic accuracy (RMSD < 1.2 Å) | Bhardwaj et al., Nature 2016 |
| Protein hallucination | RoseTTAFold | De novo designed proteins with novel folds validated by NMR and crystallography | Anishchenko et al., Nature 2021 |
| ProteinMPNN validation | Inverse folding NN | Designed sequences fold to target structures with high success rate; >50% sequence recovery | Dauparas et al., Science 2022 |
| MALAT-1 peptide optimization | Rosetta + MD | Designed peptide with 100-fold improved binding affinity to oncogenic target | Sang et al., J. Med. Chem. 2020 |
| Antimicrobial peptide design | GAN-based generation | Generated AMPs with broad-spectrum activity and low hemolysis | Das et al., Nat. Biomed. Eng. 2021 |
| ESM-2 at scale | Protein language model | 15B parameter model predicts structure from single sequence at proteome scale | Lin et al., Science 2023 |
| ProtGPT2 design | Language model generation | Generated sequences fold to stable globular structures verified experimentally | Ferruz et al., Nat. Commun. 2022 |
| Stapled peptide design | Computational + experimental | Designed cell-permeable stapled peptides targeting BCL-2 family proteins | Walensky et al., Science 2020 |

## Current Understanding

The field of in silico peptide design has entered an era of unprecedented capability, driven by the convergence of deep learning and physics-based methods. AlphaFold and RoseTTAFold have made structure prediction routine rather than exceptional, while ProteinMPNN and ESM-2 provide powerful sequence design and representation tools. Generative models are beginning to explore sequence space beyond natural diversity, and the integration of these tools into experimental workflows is accelerating the discovery of functional peptides.

Key insights include:
- **Physics + deep learning synergy:** The most effective design pipelines combine deep learning-based evaluation (speed, coverage) with physics-based refinement (accuracy, mechanistic insight).
- **Iterative design cycles:** Computational prediction evaluates many candidates, experiments test selected designs, and results inform subsequent rounds — closing the design-build-test-learn loop.
- **Problem-specific tool selection:** No single tool is optimal for all design tasks — effective design requires matching methodology to the specific design problem (binding vs. stability vs. solubility).
- **Experimental validation remains essential:** While computational predictions have improved dramatically, experimental characterization of designed peptides is necessary to confirm computational predictions and identify failure modes.

## Future Research Directions

- **End-to-end differentiable design pipelines:** Fully differentiable frameworks that optimize peptide sequences through structure prediction and property evaluation in a single gradient-based optimization loop.
- **Diffusion models for peptide backbone generation:** Adapting image-generation diffusion models (e.g., RFdiffusion) to generate novel peptide backbone conformations with specified structural properties.
- **Multimodal generative models:** Models that simultaneously generate peptide sequences and predict their properties (structure, activity, toxicity, pharmacokinetics), enabling true multi-objective optimization.
- **Active learning for peptide optimization:** Closed-loop systems where computational models suggest experiments, experimental results update the models, and the cycle iterates with increasing efficiency.
- **Non-canonical amino acid design:** Extending computational design tools to handle D-amino acids, β-amino acids, peptoids, and other non-standard building blocks.
- **Peptide ensemble design:** Designing peptides that sample specific conformational ensembles rather than folding to single structures, relevant for intrinsically disordered peptides and molecular recognition.
- **Cell-penetrating peptide design:** Computational methods for designing peptides that efficiently cross cell membranes, a major barrier to intracellular therapeutic targets.
- **Integration with high-throughput experimental data:** Training computational models on large-scale experimental datasets (e.g., deep mutational scanning, peptide display libraries) to improve prediction accuracy for design-relevant properties.

## FAQ

<div class="faq-item">
  <h3>What is the difference between Rosetta and AlphaFold for peptide design?</h3>
  <p>Rosetta uses <strong>physics-based energy functions</strong> to evaluate and optimize sequence-structure compatibility, making it suitable for designing new sequences given a target structure. AlphaFold uses <strong>deep learning trained on known structures</strong> to predict structure from sequence. In practice, they are complementary: Rosetta designs sequences for a target backbone, while AlphaFold validates whether designed sequences actually fold correctly. The Rosetta design → AlphaFold validation pipeline is a standard approach. For access to peptide design resources and services, visit <a href="https://rplpeptides.com">RPL Peptides</a>.</p>
</div>

<div class="faq-item">
  <h3>How can I use ESM-2 to improve my peptide design?</h3>
  <p>ESM-2 can improve peptide design in several ways: (1) Use <strong>ESM-1v zero-shot prediction</strong> to estimate the functional impact of mutations without experimental data — rank proposed mutations by predicted effect and prioritize those least likely to disrupt function. (2) Use <strong>ESM-2 embeddings</strong> as input features for downstream predictors of solubility, stability, or activity. (3) Screen designed sequences by comparing their <strong>ESM-2 likelihood</strong> (log probability) — sequences with very low likelihood may be unnatural and unstable. (4) Use <strong>ESMFold</strong> to rapidly predict structures of thousands of design candidates as a pre-filter before higher-accuracy (but slower) AlphaFold validation.</p>
</div>

<div class="faq-item">
  <h3>Can generative AI truly design functional peptides from scratch?</h3>
  <p>Yes, with important caveats. Generative models (ProteinGAN, ProtGPT2, RFdiffusion) can produce sequences that <strong>fold into stable structures and exhibit biological activity</strong>, as demonstrated by multiple experimental validation studies. However, current models are limited by their training data — they generate sequences that lie within the distribution of natural or designed peptides they were trained on. Truly novel folds and functions that have no precedent in natural evolution remain challenging. Additionally, generative models may produce sequences that are computationally plausible but fail experimentally due to factors not captured in training (e.g., aggregation kinetics, proteolytic susceptibility). Iterative design with experimental feedback remains essential.</p>
</div>

<div class="faq-item">
  <h3>What is ProteinMPNN and how does it differ from Rosetta design?</h3>
  <p>ProteinMPNN is a <strong>deep learning-based inverse folding model</strong> that predicts amino acid sequences for given protein backbone structures. Unlike Rosetta, which uses physics-based energy calculations, ProteinMPNN learns from the Protein Data Bank the statistical patterns of sequences that fold into specific structures. ProteinMPNN is <strong>faster</strong> (seconds vs. hours), achieves <strong>higher native sequence recovery</strong> (52% vs. 32% for Rosetta), and produces designs with <strong>better experimental success rates</strong>. However, Rosetta allows greater control over specific interactions (e.g., designing a particular hydrogen bond network) and provides interpretable energetic information. The best results often come from combining both approaches. Peptide design resources are available at <a href="https://data.rplpeptides.com">RPL Peptides Data</a>.</p>
</div>

<div class="faq-item">
  <h3>How do I computationally optimize my peptide for stability?</h3>
  <p>A systematic stability optimization workflow includes: (1) <strong>Identify instability hotspots</strong> using tools like ProtParam (instability index), Rosetta residue energy analysis, or MD simulations to find high-energy regions. (2) Use <strong>Rosetta ddg_monomer</strong> to computationally scan all possible single-point mutations and rank by predicted ΔΔG. (3) Cross-validate predictions with <strong>FoldX</strong> and <strong>ESM-1v zero-shot</strong> to identify consensus stabilizing mutations. (4) Filter candidates for <strong>solubility</strong> (avoid creating large hydrophobic patches) and <strong>functional preservation</strong> (avoid mutating residues critical for activity). (5) <strong>Validate</strong> top candidates with AlphaFold to ensure they maintain the correct fold. (6) Experimentally <strong>test 3-5 top-ranked variants</strong> for thermal stability (CD thermal melts, DSF) and functional activity.</p>
</div>

<div class="faq-item">
  <h3>What are the limitations of AlphaFold for peptide design?</h3>
  <p>AlphaFold has several limitations for peptide design: (1) <strong>Designed sequences may lack informative MSAs</strong>, reducing prediction accuracy since AlphaFold relies heavily on coevolutionary information. (2) AlphaFold predicts <strong>static structures</strong>, not conformational ensembles, which are critical for flexible peptides. (3) AlphaFold <strong>confidence metrics (pLDDT) may not correlate with thermodynamic stability</strong> — a sequence can have a high-confidence prediction but be unstable in solution. (4) AlphaFold was trained primarily on <strong>globular proteins</strong>, not short, flexible peptides, and may not capture the conformational dynamics of linear peptides. (5) AlphaFold cannot predict the effects of <strong>post-translational modifications</strong> or non-standard amino acids without specialized versions. For short, unstructured peptides, MD simulations may provide more relevant conformational information than AlphaFold.</p>
</div>

<div class="faq-item">
  <h3>How do generative models like ProteinGAN differ from rational design approaches?</h3>
  <p>Rational design (Rosetta) explicitly models the <strong>physical principles</strong> governing protein stability and uses them to optimize sequences — it asks "what sequence minimizes the free energy of this structure?" Generative models (ProteinGAN) learn the <strong>statistical distribution</strong> of functional sequences from examples and sample from it — they ask "what sequences resemble the functional family I trained on?" Rational design provides <strong>mechanistic understanding</strong> and can explore truly novel solutions, but may produce designs that are energetically optimal but biologically unrealistic. Generative models produce <strong>biologically plausible</strong> sequences efficiently but are constrained by their training data and provide limited mechanistic insight. Hybrid approaches that combine both are increasingly common.</p>
</div>

<div class="faq-item">
  <h3>What computational tools predict peptide solubility?</h3>
  <p>Several tools predict peptide solubility from sequence: <strong>CamSol</strong> provides residue-level solubility scores and identifies aggregation-prone regions using a combination of physicochemical properties. <strong>SoluProt</strong> uses a gradient boosting classifier trained on the TargetTrack solubility dataset with accuracy exceeding 75%. <strong>Protein-Sol</strong> predicts solubility from sequence-based features with a user-friendly web interface. <strong>PepCalc</strong> integrates solubility prediction with other peptide-specific calculations. For charged peptides, calculating the <strong>net charge at the working pH</strong> (using PepCalc or ProtParam) and ensuring it is ≥ ±0.2 per residue is a simple, effective guideline. For detailed analysis, combining multiple predictors and considering the specific buffer and pH conditions of your experiments is recommended.</p>
</div>

<div class="faq-item">
  <h3>Can I use RoseTTAFold for peptide design if I don't have a target structure?</h3>
  <p>Yes. RoseTTAFold can be used in <strong>"hallucination" mode</strong>, where the structure track is seeded with random or partial structures and the model iteratively refines both the sequence and structure toward plausible protein-like conformations. This <strong>de novo design</strong> approach does not require a starting experimental structure. The RFdiffusion model extends this capability using diffusion-based generation of backbone structures. For peptide design specifically, you can: (1) Use RoseTTAFold hallucination to generate novel peptide backbone scaffolds. (2) Apply ProteinMPNN to design sequences for these backbones. (3) Validate with AlphaFold. (4) Express and test experimentally. This workflow has produced successfully folding de novo proteins as small as 50 residues.</p>
</div>

<div class="faq-item">
  <h3>How do I integrate multiple computational tools into a peptide design pipeline?</h3>
  <p>An integrated peptide design pipeline might include: (1) <strong>Target analysis:</strong> Analyze the target protein structure, identify binding pockets or interaction interfaces (PyMOL, ChimeraX). (2) <strong>Initial design:</strong> Use Rosetta FlexPepDock or ProteinMPNN to design peptide binders. (3) <strong>Property filtering:</strong> Screen candidates for solubility (CamSol), stability (Rosetta ΔΔG, ESM-1v), and aggregation propensity (AGGRESCAN). (4) <strong>Structure validation:</strong> Predict structures with AlphaFold-Multimer, verify desired binding mode. (5) <strong>MD refinement:</strong> Run short MD simulations of top candidates to assess binding stability. (6) <strong>Ranking and selection:</strong> Combine computational scores into a consensus ranking, select 5-20 candidates for synthesis and testing. Pipeline scripts and documentation should be version-controlled. Resources for peptide design workflows are available at <a href="https://data.rplpeptides.com">RPL Peptides Data</a>.</p>
</div>

## References

1. Leaver-Fay, A., Tyka, M., Lewis, S.M., Lange, O.F., Thompson, J., Jacak, R., Kaufman, K.W., Renfrew, P.D., Smith, C.A., Sheffler, W., Davis, I.W., Cooper, S., Treuille, A., Mandell, D.J., Richter, F., Ban, Y.E.A., Fleishman, S.J., Corn, J.E., Kim, D.E., ... & Bradley, P. (2011). ROSETTA3: an object-oriented software suite for the simulation and design of macromolecules. *Methods in Enzymology*, 487, 545–574. [https://doi.org/10.1016/B978-0-12-381270-4.00019-6](https://doi.org/10.1016/B978-0-12-381270-4.00019-6)

2. Jumper, J., Evans, R., Pritzel, A., Green, T., Figurnov, M., Ronneberger, O., Tunyasuvunakool, K., Bates, R., Žídek, A., Potapenko, A., Bridgland, A., Meyer, C., Kohl, S.A.A., Ballard, A.J., Cowie, A., Romera-Paredes, B., Nikolov, S., Jain, R., Adler, J., ... & Hassabis, D. (2021). Highly accurate protein structure prediction with AlphaFold. *Nature*, 596(7873), 583–589. [https://doi.org/10.1038/s41586-021-03819-2](https://doi.org/10.1038/s41586-021-03819-2)

3. Baek, M., DiMaio, F., Anishchenko, I., Dauparas, J., Ovchinnikov, S., Lee, G.R., Wang, J., Cong, Q., Kinch, L.N., Schaeffer, R.D., Millán, C., Park, H., Adams, C., Glassman, C.R., DeGiovanni, A., Pereira, J.H., Rodrigues, A.V., van Dijk, A.A., Ebrecht, A.C., ... & Baker, D. (2021). Accurate prediction of protein structures and interactions using a three-track neural network. *Science*, 373(6557), 871–876. [https://doi.org/10.1126/science.abj8754](https://doi.org/10.1126/science.abj8754)

4. Lin, Z., Akin, H., Rao, R., Hie, B., Zhu, Z., Lu, W., Smetanin, N., Verkuil, R., Kabeli, O., Shmueli, Y., dos Santos Costa, A., Fazel-Zarandi, M., Sercu, T., Candido, S., & Rives, A. (2023). Evolutionary-scale prediction of atomic-level protein structure with a language model. *Science*, 379(6637), 1123–1130. [https://doi.org/10.1126/science.ade2574](https://doi.org/10.1126/science.ade2574)

5. Dauparas, J., Anishchenko, I., Bennett, N., Bai, H., Ragotte, R.J., Milles, L.F., Wicky, B.I.M., Courbet, A., de Haas, R.J., Bethel, N., Leung, P.J.Y., Huddy, T.F., Pellock, S., Tischer, D., Chan, F., Koepnick, B., Nguyen, H., Kang, A., Sankaran, B., ... & Baker, D. (2022). Robust deep learning–based protein sequence design using ProteinMPNN. *Science*, 378(6615), 49–56. [https://doi.org/10.1126/science.add2187](https://doi.org/10.1126/science.add2187)

6. London, N., Raveh, B., Cohen, E., Fathi, G., & Schueler-Furman, O. (2011). Rosetta FlexPepDock web server — high resolution modeling of peptide–protein interactions. *Nucleic Acids Research*, 39(suppl_2), W249–W253. [https://doi.org/10.1093/nar/gkr352](https://doi.org/10.1093/nar/gkr352)

7. Bhardwaj, G., Mulligan, V.K., Bahl, C.D., Gilmore, J.M., Harvey, P.J., Cheneval, O., Buchko, G.W., Pulavarti, S.V.S.R.K., Kaas, Q., Eletsky, A., Huang, P.S., Johnsen, W.A., Greisen Jr., P., Rocklin, G.J., Song, Y., Linsky, T.W., Watkins, A., Rettie, S.A., Xu, X., ... & Baker, D. (2016). Accurate de novo design of hyperstable constrained peptides. *Nature*, 538(7625), 329–335. [https://doi.org/10.1038/nature19791](https://doi.org/10.1038/nature19791)

8. Repecka, D., Jauniskis, V., Karpus, L., Rembeza, E., Rokaitis, I., Zrimec, J., Poviloniene, S., Laurynenas, A., Viknander, S., Abuajwa, W., Savolainen, O., Meskys, R., Engqvist, M.K.M., & Zelezniak, A. (2021). Expanding functional protein sequence spaces using generative adversarial networks. *Nature Machine Intelligence*, 3(4), 324–333. [https://doi.org/10.1038/s42256-021-00310-5](https://doi.org/10.1038/s42256-021-00310-5)

9. Ferruz, N., Schmidt, S., & Höcker, B. (2022). ProtGPT2 is a deep unsupervised language model for protein design. *Nature Communications*, 13(1), 4348. [https://doi.org/10.1038/s41467-022-32007-7](https://doi.org/10.1038/s41467-022-32007-7)

10. Hie, B., Zhong, E.D., Berger, B., & Bryson, B. (2021). Learning the language of viral evolution and escape. *Science*, 371(6526), 284–288. [https://doi.org/10.1126/science.abd7331](https://doi.org/10.1126/science.abd7331)

11. Anishchenko, I., Pellock, S.J., Chidyausiku, T.M., Ramelot, T.A., Ovchinnikov, S., Hao, J., Bafna, K., Norn, C., Kang, A., Bera, A.K., DiMaio, F., Carter, L., Chow, C.M., Montelione, G.T., & Baker, D. (2021). De novo protein design by deep network hallucination. *Nature*, 600(7889), 547–552. [https://doi.org/10.1038/s41586-021-04184-w](https://doi.org/10.1038/s41586-021-04184-w)

12. Wan, F., Kontogiorgos-Heintz, D., & de la Fuente-Nunez, C. (2022). Deep generative models for peptide design. *Briefings in Bioinformatics*, 23(6), bbab557. [https://doi.org/10.1093/bib/bbab557](https://doi.org/10.1093/bib/bbab557)

13. Evans, R., O'Neill, M., Pritzel, A., Antropova, N., Senior, A., Green, T., Žídek, A., Bates, R., Blackwell, S., Yim, J., Ronneberger, O., Bodenstein, S., Zielinski, M., Bridgland, A., Potapenko, A., Cowie, A., Tunyasuvunakool, K., Jain, R., Clancy, E., ... & Hassabis, D. (2022). Protein complex prediction with AlphaFold-Multimer. *bioRxiv*, 2021.10.04.463034. [https://doi.org/10.1101/2021.10.04.463034](https://doi.org/10.1101/2021.10.04.463034)

14. Meier, J., Rao, R., Verkuil, R., Liu, J., Sercu, T., & Rives, A. (2021). Language models enable zero-shot prediction of the effects of mutations on protein function. *Advances in Neural Information Processing Systems*, 34, 29287–29303. [https://doi.org/10.1101/2021.07.09.450648](https://doi.org/10.1101/2021.07.09.450648)

15. Schymkowitz, J., Borg, J., Stricher, F., Nys, R., Rousseau, F., & Serrano, L. (2005). The FoldX web server: an online force field. *Nucleic Acids Research*, 33(suppl_2), W382–W388. [https://doi.org/10.1093/nar/gki387](https://doi.org/10.1093/nar/gki387)
