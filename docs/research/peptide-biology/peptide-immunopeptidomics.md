---
title: Peptide Immunopeptidomics
description: "A comprehensive scientific overview of the immunopeptidome — the repertoire of peptides presented by MHC molecules — covering MHC peptide presentation, immunopeptidomics technologies, T-cell epitope discovery, and neoantigen prediction."
schema_type: TechArticle
slug: peptide-immunopeptidomics
---

# Peptide Immunopeptidomics


## Executive Summary

Immunopeptidomics is the comprehensive study of the repertoire of peptides presented by major histocompatibility complex (MHC) molecules on the cell surface. This peptide–MHC (pMHC) complex repertoire — known as the immunopeptidome — constitutes the molecular interface between intracellular protein metabolism and immune surveillance by T lymphocytes.

The immunopeptidome encompasses all peptides derived from the cellular proteome that are processed by the proteasome and other peptidases, transported into the endoplasmic reticulum, loaded onto MHC molecules, and trafficked to the cell surface. For MHC class I, these are typically 8–11 amino acid peptides representing the "snapshot" of intracellular protein content — including proteins from pathogens, mutated oncogenes, and self-proteins. For MHC class II, longer peptides (12–25 amino acids) derived primarily from exogenous proteins are displayed.

Mass spectrometry-based immunopeptidomics has become the central technology for characterizing the immunopeptidome, enabling unbiased identification of thousands of pMHC ligands from cell lines, tissues, and patient samples. The field has been transformed by advances in high-resolution mass spectrometry, sample preparation workflows, and bioinformatic tools for peptide identification.

The clinical impact of immunopeptidomics is most dramatically realized in cancer immunotherapy, where the identification of patient-specific tumor neoantigens — peptides derived from somatic mutations — enables personalized cancer vaccines, adoptive T‑cell therapies, and biomarker-driven immunotherapy selection.


## Background

The conceptual and experimental foundations of immunopeptidomics were laid in the 1980s and 1990s, following the elucidation of MHC restriction by Zinkernagel and Doherty (Nobel Prize 1996). In 1987, Bjorkman and colleagues solved the first X‑ray crystal structure of an MHC class I molecule (HLA-A2), revealing a peptide-binding groove occupied by electron-dense material — the bound peptide — though its sequence could not be determined at the time.

The direct identification of naturally processed MHC-bound peptides was achieved by Rammensee and colleagues in the early 1990s. Using acid elution of peptides from affinity-purified MHC molecules, followed by reversed-phase HPLC fractionation and Edman degradation, they determined the sequence of naturally presented peptides and established the "motif" concept — the observation that peptides binding to a given MHC allele share characteristic anchor residues at specific positions.

The transition to mass spectrometry-based immunopeptidomics occurred in the late 1990s and early 2000s. The Hunt laboratory demonstrated the first comprehensive LC-MS/MS identification of MHC class I ligands, including the detection of a melanoma-associated antigen (MART-1) peptide. The development of milder acid elution protocols, improved affinity chromatography matrices (e.g., pan-MHC class I antibody W6/32), and computational search algorithms enabled the identification of thousands of peptides per experiment.

The landmark publication of the complete human immunopeptidome by the Rammensee group in 2005 cataloged over 2,000 naturally processed MHC ligands from human cells, establishing the depth and complexity of the immunopeptidome. Today, state-of-the-art immunopeptidomics experiments routinely identify 10,000–30,000 unique peptides from a single cell line or tissue sample, with the complete human immunopeptidome estimated to contain over 100,000 distinct peptide species.

The field has experienced explosive growth since 2015, driven by (1) the revolution in cancer genomics enabling neoantigen prediction, (2) the advent of personalized cancer immunotherapy, (3) improvements in mass spectrometry sensitivity and speed, and (4) the development of dedicated bioinformatic tools for immunopeptidomics data analysis.


## Scientific Explanation

### MHC Peptide Presentation Pathway

**MHC Class I Pathway (Endogenous Antigens)**:

1. **Proteasomal degradation**: Cytosolic proteins are degraded by the proteasome, particularly the immunoproteasome (containing subunits β1i, β2i, β5i induced by IFN-γ), producing peptide fragments of 2–25 amino acids.
2. **TAP transport**: Peptides are translocated into the endoplasmic reticulum (ER) by the transporter associated with antigen processing (TAP1/TAP2 complex), preferentially selecting peptides of 8–16 residues with hydrophobic or basic C‑termini.
3. **ER processing**: Amino-terminal trimming by ER aminopeptidases (ERAP1 and ERAP2) generates the final 8–11 residue epitope length.
4. **MHC class I loading**: The peptide is loaded onto MHC class I heavy chain–β2-microglobulin heterodimers within the peptide loading complex (PLC), which includes tapasin, calreticulin, ERp57, and the chaperone BiP.
5. **Surface presentation**: Stable pMHC class I complexes traffic through the Golgi apparatus to the cell surface, where they are surveyed by CD8⁺ cytotoxic T lymphocytes.

**MHC Class II Pathway (Exogenous Antigens)**:

1. **Endocytosis**: Extracellular proteins are internalized by APCs through phagocytosis, macropinocytosis, or receptor-mediated endocytosis.
2. **Proteolytic processing**: Endocytosed proteins are degraded within endosomal/lysosomal compartments by cathepsins and other acidic proteases.
3. **MHC class II synthesis**: MHC class II αβ heterodimers are synthesized in the ER and associated with the invariant chain (Ii, CD74), which blocks the peptide-binding groove.
4. **Invariant chain processing**: The invariant chain is cleaved by cathepsins, leaving a small fragment (CLIP) in the peptide-binding groove.
5. **HLA-DM-mediated peptide exchange**: HLA-DM catalyzes the removal of CLIP and facilitates loading of antigenic peptides onto MHC class II.
6. **Surface presentation**: pMHC class II complexes are displayed on the APC surface for recognition by CD4⁺ helper T cells.

### Mass Spectrometry-Based Immunopeptidomics

The standard immunopeptidomics workflow consists of five steps:

1. **Sample preparation**: Cells (10⁷–10⁹) or tissues are lysed in mild detergent. MHC–peptide complexes are immunoaffinity purified using allele-specific antibodies (e.g., W6/32 for pan-MHC class I, L243 for pan-HLA-DR) coupled to Sepharose or agarose beads.

2. **Peptide elution**: Bound peptides are eluted from the MHC complex by acid treatment (typically 10% acetic acid or 0.1% TFA). Peptides are separated from the MHC heavy chain and β2-microglobulin by size-exclusion filtration (10 kDa cutoff) or solid-phase extraction.

3. **Peptide fractionation**: The complex peptide mixture can be pre-fractionated by strong cation exchange (SCX) chromatography, basic reversed-phase HPLC, or high-field asymmetric waveform ion mobility spectrometry (FAIMS) to reduce complexity and increase depth.

4. **LC-MS/MS analysis**: Peptides are separated by nanoflow reversed-phase HPLC and analyzed by high-resolution tandem mass spectrometry (Orbitrap or Q-TOF platforms). Data-dependent acquisition (DDA) or data-independent acquisition (DIA) modes are used. The most sensitive immunopeptidomics experiments now achieve detection limits of 1–10 attomoles of peptide.

5. **Peptide identification**: MS/MS spectra are searched against the human proteome database (or customized databases including mutations, splice variants, and pathogen sequences) using search engines such as Mascot, MaxQuant/Andromeda, PEAKS, MSFragger, or dedicated immunopeptidomics tools (e.g., PeptideProphet, Percolator, PEAKS DB). False discovery rate (FDR) is typically controlled at 1–2% using target–decoy approaches.

### Bioinformatic Prediction of MHC Binding and Presentation

The computational prediction of which peptides will be presented by MHC molecules is a critical component of modern immunopeptidomics and vaccine design. The field has evolved from simple binding motif identification to sophisticated machine learning approaches.

**NetMHCpan and NetMHCIIpan**: The most widely used tools for predicting MHC-peptide binding. These artificial neural network (ANN) models are trained on large datasets of experimentally measured binding affinities and naturally eluted ligands. NetMHCpan-4.1 introduced the "eluted ligand" prediction mode, which integrates both binding affinity and processing data for improved presentation prediction.

**MHCflurry**: An open-source ANN-based predictor for MHC class I binding that offers competitive performance with NetMHCpan and supports batch prediction and interactive use.

**MixMHCpred**: Developed by the Bassani-Sternberg group, this tool leverages large-scale immunopeptidomics data and considers peptide length, anchor residue preferences, and ligand-specific motifs for improved prediction accuracy.

**Deep Learning Approaches**: Recent models based on deep learning architectures (convolutional neural networks, transformers) have achieved state-of-the-art performance. NetMHCpan-4.1 using the ConvNet architecture and the EnsembleModel approach combining multiple predictors show improved prediction of actual presentation (as opposed to just binding).

### Neoantigen Discovery

Neoantigens — peptides derived from tumor-specific somatic mutations — are the most immunogenic targets for cancer immunotherapy because they are not subject to central tolerance. The discovery pipeline involves:

1. **Tumor sequencing**: Whole-exome or whole-genome sequencing of tumor and matched normal DNA identifies somatic mutations (non-synonymous single nucleotide variants, insertions/deletions, gene fusions).
2. **RNA sequencing**: Confirms mutant allele expression and provides HLA typing information.
3. **MHC binding prediction**: Mutant peptides spanning each mutation (typically 9–11 mers for class I, 15–18 mers for class II) are evaluated for predicted MHC binding affinity (IC₅₀ < 500 nM is a common threshold).
4. **Immunopeptidomics validation**: Mass spectrometry analysis of patient tumor samples or patient-derived cell lines can provide direct evidence of MHC presentation.
5. **T‑cell reactivity testing**: Candidate neoantigens are tested in T‑cell assays (ELISpot, multimer staining, intracellular cytokine staining) using patient peripheral blood or tumor-infiltrating lymphocytes (TILs).

The first studies demonstrating the feasibility of personalized neoantigen vaccination in melanoma patients (Ott et al., 2017) showed that 60–98% of predicted neoantigens were immunogenic, leading to durable clinical responses in a subset of patients. The success rate of neoantigen immunogenicity — defined as the fraction of predicted candidates that elicit detectable T‑cell responses — ranges from 10% to >50% depending on the prediction filters, the tumor type, and the patient's immune status.


## Research Evidence

<table>
<thead>
  <tr>
    <th>Technology/Method</th>
    <th>Application</th>
    <th>Throughput</th>
    <th>Key Metric</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>W6/32 immunoaffinity LC-MS/MS</td>
    <td>Pan-MHC class I immunopeptidome profiling</td>
    <td>5,000–30,000 peptides/experiment</td>
    <td>10⁷ cells yields ~10,000 unique peptides</td>
  </tr>
  <tr>
    <td>HLA-DR (L243) immunopeptidomics</td>
    <td>MHC class II ligand discovery</td>
    <td>2,000–15,000 peptides/experiment</td>
    <td>Lower yield than class I due to peptide length heterogeneity</td>
  </tr>
  <tr>
    <td>NetMHCpan-4.1</td>
    <td>MHC binding and presentation prediction</td>
    <td>Thousands of alleles, millions of peptides</td>
    <td>AUC >0.90 for most common HLA alleles</td>
  </tr>
  <tr>
    <td>MixMHCpred</td>
    <td>MHC class I ligand prediction</td>
    <td>Allele-specific prediction</td>
    <td>Ligand recovery rate >80% at 2% FDR</td>
  </tr>
  <tr>
    <td>T‑cell multimer staining</td>
    <td>Validation of pMHC-specific T cells</td>
    <td>Single-cell resolution</td>
    <td>Detection limit 0.001% of CD8⁺ T cells</td>
  </tr>
  <tr>
    <td>Neoantigen prediction pipeline</td>
    <td>Personalized cancer vaccine design</td>
    <td>50–200 candidate neoantigens/patient</td>
    <td>10–50% immunogenic in functional testing</td>
  </tr>
</tbody>
</table>

Key quantitative findings from the literature include:

- The human immunopeptidome is estimated to contain >100,000 distinct peptide species per cell type, with each MHC class I molecule displaying approximately 10⁴–10⁵ peptide copies per cell <em>Nature Reviews Immunology</em>, 16(5), 297–308.
- Approximately 90% of peptides identified by immunopeptidomics derive from the "dark matter" of the proteome — non-canonical protein products from alternative reading frames, intronic regions, and non-coding RNAs <em>Science Translational Medicine</em>, 12(564), eaax3324.
- In a study of 16 melanoma patients treated with personalized neoantigen vaccines, 60% of CD8⁺-restricted and 98% of CD4⁺-restricted neoantigens elicited immune responses <em>Nature</em>, 547(7662), 217–221.
- The concordance between predicted MHC binding and actual MHC presentation measured by mass spectrometry is 60–80% for high-affinity binders (IC₅₀ < 50 nM) but drops below 20% for moderate binders (IC₅₀ 100–500 nM) <em>Nature Biotechnology</em>, 35(10), 936–941.
- Mass spectrometry-based immunopeptidomics of tumor samples can identify 0.3–3 confirmed neo-epitopes per million somatic mutations, establishing the experimental bottleneck for neoantigen validation <em>Nature Communications</em>, 10(1), 3430.


## Current Understanding

Immunopeptidomics has moved from a descriptive science to a predictive and interventional tool. The field is now focused on translating immunopeptidomic insights into clinical applications.

**Non-Canonical Peptides**: A major finding of recent years is that a substantial fraction of the immunopeptidome — up to 50–90% depending on the study — derives from non-canonical translation events. These include peptides from alternative open reading frames, intronic regions, untranslated regions (UTRs), non-coding RNAs, and defective ribosomal products (DRiPs). These "cryptic" peptides can be immunogenic and, in cancer, may represent a new class of tumor-specific antigens.

**Clinical Immunopeptidomics**: The application of immunopeptidomics to patient tumor samples — typically from surgical resections or core needle biopsies — has become a key translational frontier. The challenge is the limited sample quantity; current protocols require 10⁷–10⁸ cells, which may not be available from small biopsies. Micro-immunopeptidomics methods (<10⁶ cells) are an active area of development.

**Tumor Antigen Discovery**: Immunopeptidomic profiling of patient tumors has been used to identify tumor-associated antigens (TAAs), cancer-testis antigens (e.g., MAGE, NY-ESO-1), and neoantigens. Combined with tumor sequencing, immunopeptidomics provides experimental validation that a mutation-derived peptide is actually presented on the tumor surface — the key criterion for immunotherapeutic relevance.

**Personalized Immunotherapy**: The convergence of immunopeptidomics, genomics, and T‑cell biology now enables personalized cancer immunotherapy. The clinical pipeline includes personalized neoantigen vaccines (mRNA, long peptide, or DC-based), neoantigen-directed T‑cell receptor (TCR) engineered T cells, and biomarker-driven patient selection for immune checkpoint inhibitors.

For researchers studying the immunopeptidome, the [RPL Peptides Data Center](https://data.rplpeptides.com) provides analytical data including mass spectra and HPLC purity for research-grade peptides. Additional tools for sequence analysis and peptide characterization can be accessed at the [RPL Peptides Research Tools](https://tool.rplpeptides.com) platform.


## Frequently Asked Questions

<div class="faq-container">
  <div class="faq-item">
<h3 class="faq-question">What is the immunopeptidome?</h3>
<p>The immunopeptidome is the complete repertoire of peptides bound to and presented by major histocompatibility complex (MHC) molecules on the cell surface. These peptides are derived from the cellular proteome through proteasomal processing, TAP transport, and MHC loading. The immunopeptidome serves as a molecular snapshot of the cell's protein content — including self-proteins, pathogen-derived proteins, and mutated proteins — that is surveyed by T lymphocytes for immune surveillance.</p>
</div>
  <div class="faq-item">
<h3 class="faq-question">How are peptides identified in immunopeptidomics experiments?</h3>
<p>Peptides are identified through a multi-step workflow: (1) MHC-peptide complexes are immunoaffinity purified from cell lysates using antibodies against MHC molecules; (2) bound peptides are eluted from the MHC complex using mild acid treatment; (3) the peptide mixture is separated from MHC proteins by size-exclusion filtration; (4) peptides are analyzed by nanoflow liquid chromatography-tandem mass spectrometry (LC-MS/MS); and (5) the resulting MS/MS spectra are searched against protein databases using search engines such as Mascot, MaxQuant, PEAKS, or MSFragger to assign peptide sequences.</p>
</div>
  <div class="faq-item">
<h3 class="faq-question">What is the difference between MHC class I and class II immunopeptidomes?</h3>
<p>MHC class I molecules present short peptides (8–11 amino acids) derived primarily from the degradation of intracellular proteins (endogenous antigens) to CD8⁺ cytotoxic T lymphocytes. MHC class II molecules present longer peptides (12–25 amino acids) derived from extracellular proteins (exogenous antigens) internalized by antigen-presenting cells, and are recognized by CD4⁺ helper T cells. MHC class I is expressed on virtually all nucleated cells, while MHC class II is restricted to professional antigen-presenting cells (dendritic cells, macrophages, B cells).</p>
</div>
  <div class="faq-item">
<h3 class="faq-question">What are neoantigens and why are they important in cancer immunotherapy?</h3>
<p>Neoantigens are peptides derived from tumor-specific somatic mutations that are presented on MHC molecules. They are "non-self" to the immune system and are not subject to central tolerance (the process that eliminates self-reactive T cells during thymic development). Neoantigens are therefore highly immunogenic and are excellent targets for cancer immunotherapy. Personalized neoantigen vaccines, adoptive T‑cell therapy targeting neoantigens, and neoantigen TCR-engineered T cells represent promising therapeutic strategies. Neoantigen load also correlates with response to immune checkpoint inhibitors.</p>
</div>
  <div class="faq-item">
<h3 class="faq-question">How does the proteasome contribute to the immunopeptidome?</h3>
<p>The proteasome — particularly the immunoproteasome (induced by IFN-γ) — is the primary protease responsible for generating MHC class I-presented peptides. The proteasome cleaves cytosolic proteins into peptide fragments through its three catalytic subunits (β1, β2, β5 in the standard proteasome; β1i, β2i, β5i in the immunoproteasome). The immunoproteasome has altered cleavage preferences that favor the production of peptides with hydrophobic or basic C‑termini — the preferred anchor residues for MHC class I binding. This makes the immunoproteasome more efficient at generating MHC-compatible peptides during infection or inflammation.</p>
</div>
  <div class="faq-item">
<h3 class="faq-question">What is the role of TAP in antigen presentation?</h3>
<p>The transporter associated with antigen processing (TAP) — composed of TAP1 and TAP2 subunits — is a heterodimeric ABC transporter located in the endoplasmic reticulum (ER) membrane. It translocates proteasome-generated peptides from the cytosol into the ER lumen, where they can be loaded onto MHC class I molecules. TAP preferentially transports peptides of 8–16 amino acids with hydrophobic or basic C‑termini. TAP deficiency — either through genetic mutation or viral inhibition (e.g., HSV ICP47, HCMV US6) — severely impairs MHC class I presentation and allows infected cells to evade CD8⁺ T‑cell recognition.</p>
</div>
  <div class="faq-item">
<h3 class="faq-question">How are bioinformatic tools used in immunopeptidomics?</h3>
<p>Bioinformatic tools are used at every stage of immunopeptidomics: (1) for MS/MS spectral identification (search engines like Mascot, MaxQuant, PEAKS, and MSFragger); (2) for MHC binding prediction (NetMHCpan, MHCflurry, MixMHCpred, which predict whether a peptide will bind to a given MHC allele); (3) for neoantigen prioritization (pipelines that integrate mutation calls, RNA expression, and MHC binding predictions); and (4) for data analysis (statistical validation of peptide identification through false discovery rate estimation, and motif analysis to identify allele-specific binding preferences).</p>
</div>
  <div class="faq-item">
<h3 class="faq-question">What challenges are associated with mass spectrometry-based immunopeptidomics?</h3>
<p>Key challenges include: (1) sample quantity — most protocols require 10⁷–10⁸ cells, limiting application to small clinical biopsies; (2) peptide dynamic range — the immunopeptidome spans >5 orders of magnitude in abundance, making low-abundance ligands difficult to detect; (3) peptide hydrophobicity — some pMHC ligands are too hydrophilic or too hydrophobic for standard LC-MS analysis; (4) false discovery rate control — the combination of non-tryptic peptides and large search databases increases the risk of false identifications; (5) MHC allele specificity — immunopeptidomics is most efficient for common HLA types, and rare alleles are poorly characterized; and (6) sample integrity — tissue handling and freezing can alter the immunopeptidome.</p>
</div>
  <div class="faq-item">
<h3 class="faq-question">How are peptide-MHC (pMHC) multimers used in T‑cell detection?</h3>
<p>pMHC multimers are fluorescently labeled complexes of MHC molecules loaded with a specific peptide, typically tetramerized using streptavidin–biotin chemistry. These reagents bind specifically to T‑cell receptors (TCRs) that recognize the displayed pMHC complex, enabling the identification, enumeration, and isolation of antigen-specific T cells by flow cytometry. pMHC multimers can detect T cells at frequencies as low as 0.001% of the CD8⁺ T‑cell population, providing a highly sensitive readout for immunogenicity testing of predicted epitopes and neoantigens.</p>
</div>
  <div class="faq-item">
<h3 class="faq-question">What are the clinical applications of immunopeptidomics?</h3>
<p>Clinical applications of immunopeptidomics include: (1) personalized cancer vaccine design — identifying patient-specific neoantigens for therapeutic vaccination; (2) adoptive T‑cell therapy — selecting neoantigen targets for TCR-engineered T cells; (3) immune checkpoint biomarker development — stratifying patients based on neoantigen burden and presentation; (4) infectious disease vaccine design — identifying protective epitopes from pathogens such as HIV, influenza, and SARS-CoV-2; (5) autoimmune disease research — characterizing self-peptides that trigger autoreactive T cells; and (6) graft-versus-host disease prediction — identifying minor histocompatibility antigens in transplantation.</p>
</div>
</div>


## References

<ol class="references">
  <li id="ref1">Bjorkman, P. J., Saper, M. A., Samraoui, B., Bennett, W. S., Strominger, J. L., & Wiley, D. C. (1987). Structure of the human class I histocompatibility antigen, HLA-A2. <em>Nature</em>, 329(6139), 506–512. <a href="https://doi.org/10.1038/329506a0">doi:10.1038/329506a0</a></li>
  <li id="ref2">Rammensee, H. G., Friede, T., & Stevanović, S. (1995). MHC ligands and peptide motifs: first listing. <em>Immunogenetics</em>, 41(4), 178–228. <a href="https://doi.org/10.1007/BF00172063">doi:10.1007/BF00172063</a></li>
  <li id="ref3">Hunt, D. F., Henderson, R. A., Shabanowitz, J., Sakaguchi, K., Michel, H., Sevilir, N., Cox, A. L., Appella, E., & Engelhard, V. H. (1992). Characterization of peptides bound to the class I MHC molecule HLA-A2.1 by mass spectrometry. <em>Science</em>, 255(5049), 1261–1263. <a href="https://doi.org/10.1126/science.1546328">doi:10.1126/science.1546328</a></li>
  <li id="ref4">Neefjes, J., Jongsma, M. L. M., Paul, P., & Bakke, O. (2011). Towards a systems understanding of MHC class I and MHC class II antigen presentation. <em>Nature Reviews Immunology</em>, 11(12), 823–836. <a href="https://doi.org/10.1038/nri3084">doi:10.1038/nri3084</a></li>
  <li id="ref5">Bassani-Sternberg, M., Pletscher-Frankild, S., Jensen, L. J., & Mann, M. (2015). Mass spectrometry of human leukocyte antigen class I peptidomes reveals strong effects of protein abundance and turnover on antigen presentation. <em>Molecular & Cellular Proteomics</em>, 14(3), 658–673. <a href="https://doi.org/10.1074/mcp.M114.042812">doi:10.1074/mcp.M114.042812</a></li>
  <li id="ref6">Pearson, H., Daouda, T., Granados, D. P., Durette, C., Bonneil, E., Courcelles, M., Rodenbrock, A., Laverdure, J. P., Côté, C., Mader, S., Lemieux, S., Thibault, P., & Perreault, C. (2016). MHC class I-associated peptides derive from selective regions of the human genome. <em>Journal of Clinical Investigation</em>, 126(12), 4690–4701. <a href="https://doi.org/10.1172/JCI88590">doi:10.1172/JCI88590</a></li>
  <li id="ref7">Jurtz, V., Paul, S., Andreatta, M., Marcatili, P., Peters, B., & Nielsen, M. (2017). NetMHCpan-4.1: Improved peptide-MHC class I interaction predictions integrating eluted ligand and peptide binding affinity data. <em>Nucleic Acids Research</em>, 45(W1), W24–W29. <a href="https://doi.org/10.1093/nar/gkw932">doi:10.1093/nar/gkw932</a></li>
  <li id="ref8">Gfeller, D., Guillaume, P., Michaux, J., Pak, H., Bassani-Sternberg, M., & Müller, M. (2018). The length distribution and multiple specificity of naturally presented HLA-I ligands. <em>The Journal of Immunology</em>, 201(12), 3705–3716. <a href="https://doi.org/10.4049/jimmunol.1800914">doi:10.4049/jimmunol.1800914</a></li>
  <li id="ref9">Yewdell, J. W., & Nicchitta, C. V. (2006). The DRiP hypothesis decennial: support, controversy, refinement and extension. <em>Trends in Immunology</em>, 27(8), 368–373. <a href="https://doi.org/10.1016/j.it.2006.06.008">doi:10.1016/j.it.2006.06.008</a></li>
  <li id="ref10">Schumacher, T. N., & Schreiber, R. D. (2015). Neoantigens in cancer immunotherapy. <em>Science</em>, 348(6230), 69–74. <a href="https://doi.org/10.1126/science.aaa4971">doi:10.1126/science.aaa4971</a></li>
  <li id="ref11">Racle, J., Guillaume, P., Schmidt, J., Michaux, J., Larabi, A., Lau, K., Caron, E., & Bassani-Sternberg, M. (2019). Machine learning predictions of MHC-I peptide binding and presentation. <em>Nature Biotechnology</em>, 37(5), 501–506. <a href="https://doi.org/10.1038/s41587-019-0076-5">doi:10.1038/s41587-019-0076-5</a></li>
  <li id="ref12">Yadav, M., Jhunjhunwala, S., Phung, Q. T., Lupardus, P., Tanguay, J., Bumbaca, S., Franci, C., Cheung, T. K., Fritsche, J., Weinschenk, T., Modrusan, Z., Mellman, I., Lill, J. R., & Delamarre, L. (2014). Predicting immunogenic tumour mutations by combining mass spectrometry and exome sequencing. <em>Nature</em>, 515(7528), 572–576. <a href="https://doi.org/10.1038/nature14001">doi:10.1038/nature14001</a></li>
  <li id="ref13">Laumont, C. M., Vincent, K., Hesnard, L., Audemard, É., Bonneil, É., Laverdure, J. P., Gendron, P., Courcelles, M., Hardy, M. P., Côté, C., Durette, C., St-Pierre, C., Benhammadi, M., Lanoix, J., Vobecky, S., Haddad, E., Lemieux, S., Thibault, P., & Perreault, C. (2018). Noncoding regions are the main source of targetable tumor-specific antigens. <em>Science Translational Medicine</em>, 10(470), eaau5516. <a href="https://doi.org/10.1126/scitranslmed.aau5516">doi:10.1126/scitranslmed.aau5516</a></li>
  <li id="ref14">Sarkizova, S., Klaeger, S., Le, P. M., Li, L. W., Oliveira, G., Keshishian, H., Hartigan, C. R., Zhang, W., Braun, D. A., Ligon, K. L., Bachireddy, P., Zaitsev, K., Clauser, K. R., Hacohen, N., Carr, S. A., & Keskin, D. B. (2020). A large peptidome dataset improves HLA class I epitope prediction across most of the human population. <em>Nature Biotechnology</em>, 38(2), 199–209. <a href="https://doi.org/10.1038/s41587-019-0322-9">doi:10.1038/s41587-019-0322-9</a></li>
</ol>
