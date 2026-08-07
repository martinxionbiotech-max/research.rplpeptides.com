---
title: Peptide Database Resources — UniProt, PDB, PeptideAtlas & Specialized Repositories
description: "Comprehensive survey of peptide databases: UniProt, NCBI Protein, PDB, PeptideAtlas, CAMP, DBAASP, APD3, SATPdb, PepBank, DRAMP, CancerPPD. Covers data formats (FASTA, PDB, mmCIF), API access, and integration workflows."
---

# Peptide Database Resources — UniProt, PDB, PeptideAtlas & Specialized Repositories

<div class="quick-fact">
  <strong>Key Summary:</strong> The modern peptide researcher has access to an extensive ecosystem of databases spanning general protein sequences (UniProt, NCBI Protein), three-dimensional structures (PDB), and specialized peptide repositories (PeptideAtlas, CAMP, DBAASP, APD3, DRAMP, SATPdb, PepBank, CancerPPD). This article provides a comprehensive survey of these resources, their data formats, programmatic API access methods, and strategies for integrating multi-source data into coherent research workflows.
</div>

## Executive Summary

The exponential growth of biological data has transformed peptide research from a data-poor to a data-rich discipline. Today's peptide scientist must navigate dozens of specialized databases, each offering unique perspectives on peptide sequences, structures, functions, and experimental properties. This article provides a comprehensive roadmap to the peptide database landscape. We begin with foundational general-purpose resources — UniProt, NCBI Protein, and the Protein Data Bank (PDB) — that provide broad coverage of peptide and protein sequences and structures. We then survey specialized peptide databases organized by functional category: antimicrobial peptides (APD3, CAMP, DRAMP, DBAASP), therapeutic peptides (SATPdb, CancerPPD, THPdb), bioactive peptides (PepBank, BIOPEP-UWM, EROP-Moscow), and mass spectrometry-based peptide repositories (PeptideAtlas, PRIDE, MassIVE). For each database, we discuss scope, curation philosophy, unique features, and practical access methods. We cover essential data formats — FASTA for sequence data, PDB and mmCIF for structural data, and SDF/SMILES for chemical representations — including best practices for parsing and validation. The article addresses programmatic access through REST APIs, bulk downloads, and database-specific query languages, enabling researchers to integrate peptide data into computational pipelines. Finally, we present strategies for multi-database integration workflows that combine complementary information from disparate sources, supported by resources at [RPL Peptides Data](https://data.rplpeptides.com).

## Background

The history of biological databases is intertwined with the history of molecular biology itself. Margaret Dayhoff's *Atlas of Protein Sequence and Structure*, first published in 1965, was arguably the first biological database, painstakingly compiled before the era of computer-based sequence repositories. The establishment of GenBank in 1982 and the Protein Data Bank in 1971 laid the foundation for the modern database ecosystem, which now encompasses hundreds of specialized repositories.

The exponential growth of sequence data — driven by successive revolutions in DNA sequencing technology, from Sanger sequencing through next-generation sequencing to long-read platforms — has transformed database scale. The European Nucleotide Archive (ENA), for instance, contained approximately 50 petabytes of data by 2023, while UniProt has grown from roughly 2 million entries in 2008 to over 250 million in 2024.

For peptide researchers, this data abundance creates both opportunity and challenge. The opportunity lies in the unprecedented ability to contextualize peptide sequences within evolutionary relationships, structural frameworks, and functional annotations. The challenge lies in navigating a fragmented landscape where data is distributed across dozens of databases with varying curation standards, update frequencies, and access protocols.

The development of specialized peptide databases has been driven by the recognition that general-purpose sequence databases are often poorly suited for peptide research. Many biologically active peptides are short (5-50 residues), post-translationally modified, or derived from precursor proteins through proteolytic processing — characteristics that are poorly captured by databases designed around full-length proteins. The emergence of databases such as the Antimicrobial Peptide Database (APD) in 2004 represented a paradigm shift toward community-curated, functionally focused repositories ([Wang & Wang, 2004](https://doi.org/10.1093/nar/gkh148)).

The FAIR data principles — Findable, Accessible, Interoperable, and Reusable — articulated in 2016, provide a framework for evaluating database quality ([Wilkinson et al., 2016](https://doi.org/10.1038/sdata.2016.18)). The best peptide databases adhere to these principles through persistent identifiers (DOIs, accession numbers), standardized data formats, documented APIs, and clear licensing terms.

## General Protein Sequence Databases

### UniProt (Universal Protein Resource)

UniProt is the most comprehensive and widely used protein sequence database, produced by the UniProt Consortium — a collaboration between the European Bioinformatics Institute (EMBL-EBI), the SIB Swiss Institute of Bioinformatics, and the Protein Information Resource (PIR) ([UniProt Consortium, 2023](https://doi.org/10.1093/nar/gkac1052)).

**UniProtKB components:**

**Swiss-Prot (reviewed):**
- Manually annotated, non-redundant entries with information extracted from literature and curator-evaluated computational analyses.
- Each entry reviewed by expert curators, ensuring high-quality functional annotation, post-translational modification documentation, and variant information.
- Contains approximately 570,000 entries (as of 2024), representing the gold standard for protein annotation quality.
- For peptide researchers, Swiss-Prot provides curated information on peptide hormones, toxins, antimicrobial peptides, and other bioactive peptides with high-confidence annotations.

**TrEMBL (unreviewed):**
- Automatically annotated entries derived from translation of coding sequences in EMBL-Bank/GenBank/DDBJ.
- Contains over 250 million entries with computationally predicted annotations.
- Coverage vastly exceeds Swiss-Prot, capturing the full diversity of sequenced organisms, but with lower annotation quality.
- Useful for exploring peptide sequence diversity across the tree of life, with the caveat that annotations are predictions rather than experimentally confirmed observations.

**UniRef (Reference Clusters):**
- Clustered sets of sequences from UniProtKB at 100% (UniRef100), 90% (UniRef90), and 50% (UniRef50) sequence identity.
- Reduces redundancy for large-scale analyses — UniRef50 provides a representative sequence set suitable for database searching and clustering.
- Essential for peptide researchers performing large-scale sequence similarity searches, as searching against UniRef90 (rather than the full UniProtKB) dramatically reduces computational requirements while maintaining biological diversity.

**UniParc (Archive):**
- Comprehensive, non-redundant database of all protein sequences from major public databases, tracking sequence history.
- Valuable for peptide researchers studying sequence evolution or accessing sequences that have been removed from current databases.

**Access methods:**
- Web interface: [https://www.uniprot.org](https://www.uniprot.org) with advanced query syntax and customizable result views.
- REST API: Programmatic access through [https://rest.uniprot.org](https://rest.uniprot.org), supporting sequence retrieval, identifier mapping, and annotation queries.
- FTP downloads: Complete database in FASTA, XML, and text formats, updated at least every 8 weeks.
- SPARQL endpoint: Semantic web queries through UniProt's RDF representation.

**Querying for peptides in UniProt:**
Effective peptide-specific queries include:
- `length:[5 TO 50]` — restrict to short sequences
- `annotation:(type:"signal peptide")` — identify peptide precursors
- `keyword:"Antimicrobial [KW-0929]"` — retrieve annotated antimicrobial peptides
- `cc_alternative_products` — find peptides derived from precursor processing
- Combined queries: `length:[5 TO 50] AND keyword:"Secreted [KW-0964]"` to find short secreted peptides

### NCBI Protein Database

The NCBI Protein database is a collection of sequences from several sources, including translations from GenBank coding regions, RefSeq, Swiss-Prot, PIR, PRF, and PDB.

**Key features:**
- **Entrez search system:** Powerful Boolean query language enabling complex search strategies across NCBI's integrated databases.
- **RefSeq subset:** Curated, non-redundant sequence set providing a stable reference for annotation, with distinct accession prefixes (NP_ for proteins, XP_ for predicted proteins).
- **Identical Protein Groups:** Clustering of identical sequences from different sources, reducing redundancy.
- **LinkOut:** Links to external resources including specialized databases, publications, and structural data.

**Peptide-specific considerations:**
The NCBI Protein database is less curated for peptide-specific annotations than UniProt/Swiss-Prot, but its integration with genomic data through the Entrez system makes it valuable for peptide genomics — tracing peptide-coding genes to genomic loci, regulatory elements, and evolutionary synteny.

### Other General Sequence Repositories

- **RefSeq:** NCBI's curated reference sequence database providing a comprehensive, integrated, non-redundant set of sequences.
- **Ensembl:** Genome-centric resource providing genomic context for peptide-coding genes, including splice variants and regulatory annotations.
- **InterPro:** Integrates protein family, domain, and functional site classification from multiple member databases, providing comprehensive functional annotation.

## Structural Databases

### Protein Data Bank (PDB)

The Protein Data Bank, established in 1971, is the single worldwide repository for experimentally determined three-dimensional structures of biological macromolecules ([wwPDB Consortium, 2019](https://doi.org/10.1093/nar/gky1004)). For peptide researchers, the PDB provides atomic-resolution structural data essential for understanding peptide conformation, molecular recognition, and structure-based design.

**PDB content relevant to peptides:**
- **Peptide-protein complexes:** Thousands of structures of peptides bound to receptors, enzymes, antibodies, and MHC molecules, providing direct visualization of binding modes.
- **Free peptide structures:** Though less common (due to conformational flexibility), structures of free peptides (particularly cyclic and disulfide-stabilized peptides) are available.
- **Peptide drugs and inhibitors:** Structural characterization of peptide therapeutics bound to their targets.
- **NMR and cryo-EM structures:** Techniques that can capture peptide conformational ensembles not accessible through crystallography.

**Access methods:**
- Web search: [https://www.rcsb.org](https://www.rcsb.org) with advanced search including sequence similarity, ligand identity, and structural features.
- REST API: Programmatic access to search, data retrieval, and sequence-structure mapping.
- Bulk download: Complete PDB archive available through rsync and HTTP.
- PDBe-KB: Aggregated structural annotations and functional predictions for all PDB entries.

### PDB Data Format: PDB and mmCIF

**PDB format:**
The legacy PDB file format is a fixed-column text format where each line begins with a record type identifier (e.g., ATOM, HETATM, SEQRES). While human-readable, the format has significant limitations: 4-character chain identifiers, 5-digit residue numbers, and a maximum of 99,999 atoms — constraints that modern large structures frequently violate.

**mmCIF (macromolecular Crystallographic Information File):**
The mmCIF format is the current PDB standard, using a flexible key-value pair structure organized into categories. mmCIF addresses all PDB format limitations and supports rich metadata including experimental details, structure factors, and extensive annotation. Since 2014, the wwPDB has mandated mmCIF as the primary archive format, and the legacy PDB format is generated as a derived format.

For programmatic work with structural data, using mmCIF-aware parsers (BioPython's MMCIFParser, PyMOL, or specialized mmCIF libraries) is recommended over legacy PDB parsers.

### Structural Data Resources

- **PDBe:** European PDB resource with enhanced analysis tools, domain assignments, and assembly information.
- **PDBj:** Japanese PDB resource with specialized NMR data tools.
- **SCOP2 and CATH:** Hierarchical structural classification databases useful for identifying structural relationships among peptides and their targets.
- **AlphaFold Protein Structure Database:** Predicted structures for over 200 million UniProt sequences, jointly developed by DeepMind and EMBL-EBI. While predictions rather than experimental structures, the AlphaFold DB dramatically expands structural coverage for peptide families.

## Specialized Peptide Databases

### Antimicrobial Peptide Databases

**APD3 (Antimicrobial Peptide Database):**
The APD, maintained at the University of Nebraska Medical Center, is the foundational antimicrobial peptide database, established in 2004 ([Wang et al., 2016](https://doi.org/10.1093/nar/gkv1278)). APD3 contains over 3,200 experimentally validated AMPs from all biological kingdoms.

- **Unique features:** Calculates physicochemical parameters (net charge, hydrophobicity, Boman index) for each entry, includes structural information (NMR and X-ray structures) where available, and provides statistical analysis of AMP sequence features.
- **Curation:** Each entry is manually curated with experimental validation required for inclusion.
- **Access:** Web-based search, browsing by source organism, activity, structure, or physicochemical properties.
- **Limitations:** Relatively small size compared to aggregate databases; limited to natural AMPs.

**CAMP_R3 (Collection of Anti-Microbial Peptides):**
CAMP_R3 integrates data from multiple AMP databases and literature, containing over 8,000 sequences ([Waghu et al., 2016](https://doi.org/10.1093/nar/gkv1153)).

- **Unique features:** Integrates multiple ML-based AMP prediction tools, providing both experimental and predicted AMPs with confidence scores.
- **Sequence signatures:** Identifies conserved patterns characteristic of AMP families.
- **Access:** Web interface with sequence search, BLAST integration, and batch download.

**DRAMP 3.0 (Data Repository of Antimicrobial Peptides):**
DRAMP provides the most comprehensive collection of antimicrobial peptides, with over 22,000 entries spanning natural AMPs, synthetic AMPs, patented sequences, and clinical candidates ([Shi et al., 2022](https://doi.org/10.1093/nar/gkab1027)).

- **Unique features:** Distinguishes between general AMPs, patented sequences, and peptides in clinical trials. Includes antimicrobial activity data (MIC values) where available.
- **Annotations:** Structure, activity, target species, hemolytic activity, and physicochemical properties.
- **Access:** Web interface with advanced search, sequence alignment, and batch download. Most comprehensive for translational AMP research.

**DBAASP v3 (Database of Antimicrobial Activity and Structure of Peptides):**
DBAASP focuses on quantitative antimicrobial activity data, providing MIC values against specific microbial strains ([Pirtskhalava et al., 2021](https://doi.org/10.1093/nar/gkaa991)).

- **Unique features:** Specialized for structure-activity relationship analysis with standardized MIC data. Includes hemolytic activity data for therapeutic index calculation.
- **Physicochemical analysis:** Detailed analysis of charge, hydrophobicity, amphipathicity, and structural features correlated with activity.
- **Access:** Web interface with powerful filtering by activity, structure, and physicochemical properties.

### Therapeutic Peptide Databases

**SATPdb (Structurally Annotated Therapeutic Peptides Database):**
SATPdb catalogs therapeutic peptides with detailed structural annotations ([Singh et al., 2016](https://doi.org/10.1093/nar/gkv1274)).

- **Scope:** Peptide therapeutics across categories including anticancer, antimicrobial, antiviral, antidiabetic, and cardiovascular peptides.
- **Structural features:** Secondary structure content, disulfide bonding patterns, post-translational modifications, and structural models.
- **Clinical status:** Classification by preclinical, clinical trial phase, and approved status.

**CancerPPD (Cancer Peptide and Protein Database):**
CancerPPD is a specialized database for anticancer peptides and proteins, containing experimentally validated entries with detailed activity data ([Tyagi et al., 2015](https://doi.org/10.1093/nar/gku1198)).

- **Unique features:** Cell line-specific activity data (IC₅₀ values), mechanism of action annotations, origin (natural/synthetic/chimeric), and target information.
- **Natural and synthetic:** Includes both naturally occurring anticancer peptides and designed/optimized variants.
- **Access:** Web interface with search by sequence, structure, activity, or origin.

**THPdb (FDA Approved Therapeutic Peptides and Proteins Database):**
THPdb provides comprehensive information on FDA-approved peptide and protein therapeutics ([Usmani et al., 2017](https://doi.org/10.1371/journal.pone.0181748)).

- **Scope:** All FDA-approved therapeutic peptides and proteins with detailed pharmaceutical information.
- **Clinical data:** Indications, administration routes, pharmacokinetics, pharmacodynamics, and adverse effects where available.
- **Access:** Web interface with browsing by therapeutic category, target, or administration route.

### Mass Spectrometry Peptide Repositories

**PeptideAtlas:**
PeptideAtlas is a comprehensive repository of mass spectrometry-based proteomics data, providing peptide identifications with statistical validation ([Desiere et al., 2006](https://doi.org/10.1093/nar/gkj040)).

- **Scope:** Peptide identifications from thousands of LC-MS/MS experiments across multiple organisms and sample types.
- **Statistical validation:** PeptideProphet probability scores provide confidence estimates for each identification.
- **Genome mapping:** Peptides mapped to genomic coordinates, enabling proteogenomic analysis.
- **Access:** Web interface, FTP downloads, and API access to processed peptide data.

**PRIDE (PRoteomics IDEntifications Database):**
PRIDE is the world's largest mass spectrometry-based proteomics data repository, hosted at EMBL-EBI ([Perez-Riverol et al., 2022](https://doi.org/10.1093/nar/gkab1038)).

- **Scope:** Raw mass spectrometry data, processed peptide and protein identifications, and quantification results.
- **ProteomeXchange:** PRIDE is a founding member of the ProteomeXchange consortium, enabling cross-repository data discovery.
- **Access:** Web interface, REST API, and programmatic access through PRIDE Inspector tools.

**MassIVE (Mass Spectrometry Interactive Virtual Environment):**
MassIVE is a community-oriented mass spectrometry data repository with reanalysis capabilities.

- **Unique features:** Supports data reanalysis through integrated workflows, enabling researchers to re-process raw data with updated search algorithms.
- **Community datasets:** Large-scale community proteomics projects such as the Clinical Proteomic Tumor Analysis Consortium (CPTAC).

### Bioactive Peptide Databases

**PepBank:**
PepBank is a database of bioactive peptides with emphasis on peptide-receptor interactions and functional annotations ([Shtatland et al., 2007](https://doi.org/10.1093/nar/gkl1048)).

- **Scope:** Experimentally validated bioactive peptides with known receptors or molecular targets.
- **Features:** Sequence, source, target, biological activity, and literature references.

**BIOPEP-UWM:**
BIOPEP is a database of bioactive peptide sequences within food proteins, maintained at the University of Warmia and Mazury ([Minkiewicz et al., 2019](https://doi.org/10.3390/ijms20235748)).

- **Scope:** Peptides with demonstrated bioactivity (antihypertensive, antioxidant, opioid, immunomodulatory, etc.) identified in food protein sequences.
- **Unique features:** Tools for simulating enzymatic digestion of proteins to predict release of bioactive peptides.
- **Applications:** Nutraceutical and functional food research.

**EROP-Moscow:**
The Endogenous Regulatory OligoPeptides database catalogs oligopeptides with regulatory functions in living organisms ([Zamyatnin, 2009](https://doi.org/10.1093/nar/gkn786)).

- **Scope:** Endogenous peptides (2-50 residues) with demonstrated regulatory activity.
- **Features:** Sequence, structure, tissue distribution, receptor interactions, and biological functions.

## Data Formats for Peptide Bioinformatics

### FASTA Format

FASTA is the universal format for representing peptide and protein sequences:

```
>sp|P01308|INS_HUMAN Insulin OS=Homo sapiens
MALWMRLLPLLALLALWGPDPAAAFVNQHLCGSHLVEALYLVCGERGFFYTPKTRREAEDLQ
VGQVELGGGPGAGSLQPLALEGSLQKRGIVEQCCTSICSLYQLENYCN
```

- **Header line:** Begins with `>`, conventionally containing accession, identifier, description, and organism.
- **Sequence lines:** One-letter amino acid codes, typically wrapped at 60-80 characters.
- **Multiple sequences:** Multiple FASTA records can be concatenated in a single file.

**Best practices:**
- Use standard IUPAC one-letter amino acid codes.
- Avoid ambiguous characters (B, Z, X) unless genuinely representing ambiguous positions.
- Include source organism in the header for traceability.
- Validate sequences programmatically — tools like `seqkit` can identify format issues.

### PDB Format

For structural data, the legacy PDB format remains widely used for small structures:

```
ATOM      1  N   ALA A   1       1.142   2.454   0.000  1.00  0.00           N
ATOM      2  CA  ALA A   1       2.631   2.425   0.000  1.00  0.00           C
...
```

**Limitations for peptides:**
- Fixed-column format with limited field widths
- Cannot represent large structures with >99,999 atoms
- Chain IDs limited to single characters

### mmCIF Format

mmCIF uses a flexible key-value structure:

```
_atom_site.group_PDB
_atom_site.id
_atom_site.type_symbol
_atom_site.label_atom_id
...
ATOM   1    N  N   . ALA A 1  ? 1.142  2.454  0.000  1.00  0.000  ? ...
```

mmCIF is the recommended format for all new structural bioinformatics work.

### SMILES and Chemical Formats

For modified peptides and peptidomimetics:
- **SMILES:** Linear string representation of chemical structure (e.g., `CC(C(=O)O)N` for alanine).
- **HELM (Hierarchical Editing Language for Macromolecules):** Notation system for complex biomolecules including peptides with non-natural modifications.
- **SDF/MOL:** File formats for chemical structures with 2D/3D coordinates.

## API Access and Programmatic Integration

### REST APIs

Most major peptide databases provide REST (Representational State Transfer) APIs for programmatic access:

**UniProt REST API:**
- Endpoint: `https://rest.uniprot.org/uniprotkb/`
- Capabilities: Search, retrieve entries in multiple formats, map identifiers between databases, and batch operations.
- Example: Retrieve peptide entries by keyword:
  ```
  GET /uniprotkb/search?query=(keyword:antimicrobial)+AND+(length:[5+TO+50])&format=json
  ```

**NCBI E-utilities:**
- Endpoint: `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/`
- Capabilities: Search across all NCBI databases, retrieve records, and link between databases.
- Rate limiting: 3 requests/second without API key, 10 requests/second with API key.
- Example: Search for AMPs in Protein database:
  ```
  esearch.fcgi?db=protein&term=antimicrobial+peptide[title]+AND+5:50[SLEN]
  ```

**RCSB PDB REST API:**
- Endpoint: `https://data.rcsb.org/rest/v1/`
- Capabilities: Search by sequence, structure, ligand, experimental method, resolution, and structural features.
- GraphQL interface for complex queries returning only requested fields.

**PDBe REST API:**
- Endpoint: `https://www.ebi.ac.uk/pdbe/api/`
- Capabilities: Detailed structural annotations, domain assignments, binding site analysis.

### Bulk Downloads

For large-scale peptide bioinformatics, bulk downloads are often more practical than API access:

| Database | Download Format | Update Frequency | Size |
|---|---|---|---|
| UniProtKB | FASTA, XML, TXT | Every 8 weeks | ~100 GB (compressed) |
| NCBI Protein | FASTA | Weekly | ~500 GB |
| PDB Archive | mmCIF | Weekly | ~2 TB (with structure factors) |
| PeptideAtlas | Custom TSV | Per-build | ~1 GB per organism |
| DRAMP 3.0 | FASTA, CSV | Periodic | ~50 MB |
| DBAASP | CSV | Periodic | ~30 MB |

**Best practices for bulk data processing:**
- Use tools designed for bioinformatics data: `seqkit` for FASTA manipulation, BioPython for sequence parsing, PyMOL/ProDy for structural analysis.
- Process data incrementally — complete UniProtKB in FASTA format is ~100 GB and parsing the entire file into memory is impractical.
- Maintain local database mirrors using rsync for regularly updated resources (PDB, UniProt).
- Version-track downloaded data — database content changes over time, and reproducibility requires knowing which version was used.

### Workflow Integration

Integrating multiple peptide databases into analysis workflows requires:

**Identifier mapping:**
Peptide identifiers differ across databases. UniProt provides the `idmapping` service for converting between:
- UniProtKB AC/ID ↔ Gene names, RefSeq, Ensembl, PDB, Pfam, InterPro, GO and dozens more.

**Data harmonization:**
Different databases use different annotation schemas. Strategies for harmonization:
- Map to common controlled vocabularies (Gene Ontology, ChEBI, PSI-MOD for modifications).
- Use database cross-references (each UniProt entry lists cross-references to >180 databases).
- Implement data validation checks — flag inconsistencies between databases for manual review.

**Pipeline design:**
A typical multi-database peptide analysis pipeline:
1. **Retrieve candidate sequences** from UniProt/Swiss-Prot using keyword, taxonomy, and length filters.
2. **Cross-reference with specialized databases** (CAMP, DBAASP, SATPdb) for functional annotations.
3. **Retrieve structural data** from PDB or AlphaFold DB for candidates with available structures.
4. **Enrich with experimental data** from PeptideAtlas or PRIDE for proteomic evidence.
5. **Integrate physicochemical predictions** using computational tools or pre-computed database values.
6. **Prioritize candidates** based on consensus annotations, structural features, and predicted properties.

## Research Evidence

The utility and reliability of peptide databases are documented in extensive literature:

| Database | Validation Study | Key Finding |
|---|---|---|
| APD3 | Wang et al., NAR 2016 | 3,200+ experimentally validated AMPs; predicts AMP features correlating with activity |
| CAMP_R3 | Waghu et al., NAR 2016 | ML classifiers achieve >93% accuracy; sequence signatures identify novel AMPs |
| DRAMP 3.0 | Shi et al., NAR 2022 | 22,000+ entries unified from 17 sources; clinical trial data integration |
| DBAASP v3 | Pirtskhalava et al., NAR 2021 | Standardized MIC data enables quantitative SAR; therapeutic index calculation |
| UniProt | UniProt Consortium, NAR 2023 | 250M+ sequences; manual curation achieves >99% annotation accuracy for Swiss-Prot |
| PeptideAtlas | Desiere et al., NAR 2006 | Statistical validation reduces false discovery to <1%; multi-organism coverage |
| PRIDE | Perez-Riverol et al., NAR 2022 | Largest proteomics repository; ProteomeXchange enables cross-repository discovery |
| CancerPPD | Tyagi et al., NAR 2015 | 3,400+ anticancer peptides with cell line activity data |
| PDB | wwPDB Consortium, NAR 2019 | 180,000+ structures; comprehensive peptide-protein complex coverage |

## Current Understanding

The peptide database ecosystem is characterized by several themes:

- **Complementarity, not redundancy:** While there is overlap between databases, each serves distinct needs — structural (PDB), sequence (UniProt), functional (APD3/DRAMP), or quantitative (DBAASP). Effective researchers leverage this complementarity through multi-database integration.
- **The curation gap:** A fundamental divide exists between highly curated resources (Swiss-Prot, APD3) and automated resources (TrEMBL, predicted entries in CAMP). For hypothesis generation, automated resources provide breadth; for hypothesis testing, curated resources provide confidence.
- **FAIR compliance varies:** Major databases (UniProt, PDB, PRIDE) are exemplars of FAIR principles. Smaller specialized databases vary in their adherence to persistent identifiers, documented APIs, and standardized formats.
- **Machine learning integration:** Modern databases increasingly incorporate ML-based predictions alongside experimental data, blurring the line between data repositories and analysis platforms.
- **The clinical translation gap:** Despite rich academic peptide databases, systematic integration with clinical trial data, pharmacokinetic data, and regulatory information remains limited — THPdb is a notable exception.

## Future Research Directions

- **Unified peptide meta-database:** A single access point that integrates data from all major peptide databases through standardized APIs and ontologies, eliminating redundant searching across multiple platforms.
- **Real-time database updating:** Continuous integration pipelines that incorporate new literature and sequence data within days rather than months.
- **Bidirectional experimental-database feedback:** Platforms where experimental results feed directly into databases, reducing the current years-long lag between discovery and database inclusion.
- **Peptide knowledge graphs:** Graph-based representations capturing relationships between peptide sequences, structures, activities, targets, pathways, and diseases, enabling network-based analysis and discovery.
- **AI-augmented curation:** Machine learning models that assist human curators by prioritizing literature for review, flagging potential annotation errors, and suggesting annotations based on computational predictions.
- **Natural language interfaces:** Query interfaces that accept natural language questions ("show me antimicrobial peptides longer than 10 residues from frog skin with MIC < 10 µM against E. coli") rather than requiring formal query languages.
- **Standards for peptide-specific data:** Community-developed minimum information standards for peptide activity data (MIAPE), synthesis protocols, and characterization, analogous to MIAME for microarrays.
- **Integrated peptide virtual screening platforms:** Databases that not only store peptide data but provide on-demand computational analysis — docking, property prediction, toxicity screening — through integrated cloud computing resources.

## FAQ

<div class="faq-item">
  <h3>Which database should I use as a starting point for peptide sequence data?</h3>
  <p>Start with <strong>UniProtKB/Swiss-Prot</strong> for the highest quality curated annotations. Query using keywords, taxonomy, and length filters to identify peptides of interest. Expand your search to <strong>UniProtKB/TrEMBL</strong> for broader coverage, recognizing that TrEMBL annotations are computationally predicted and less reliable. For known peptide families, consult the relevant specialized database: <strong>APD3 or DRAMP</strong> for antimicrobial peptides, <strong>DBAASP</strong> for quantitative activity data, <strong>SATPdb</strong> for therapeutic peptides, and <strong>PeptideAtlas</strong> for mass spectrometry evidence. Document which database versions were accessed for reproducibility. Integrated resources are available at <a href="https://rplpeptides.com">RPL Peptides</a>.</p>
</div>

<div class="faq-item">
  <h3>What is the difference between Swiss-Prot and TrEMBL, and when should I use each?</h3>
  <p><strong>Swiss-Prot</strong> entries are manually curated by expert annotators who review experimental literature to confirm protein existence, function, post-translational modifications, and variants. Swiss-Prot has <strong>very high accuracy</strong> (~570,000 entries) but limited coverage. Use Swiss-Prot for: hypothesis testing, mechanism studies, and applications where annotation errors would be costly. <strong>TrEMBL</strong> entries are computationally translated from nucleotide sequences and automatically annotated. TrEMBL has <strong>vast coverage</strong> (>250 million entries) but lower annotation quality, with potential errors in gene prediction and functional assignment. Use TrEMBL for: exploring sequence diversity across organisms, identifying novel peptide families, and large-scale computational screens where individual errors average out statistically.</p>
</div>

<div class="faq-item">
  <h3>How do I programmatically access peptide databases for large-scale analysis?</h3>
  <p>For <strong>high-throughput programmatic access</strong>: (1) Download <strong>bulk data files</strong> (FASTA format from UniProt FTP, mmCIF from PDB via rsync) and process locally — this is the most efficient approach for analyzing thousands to millions of peptides. (2) Use <strong>REST APIs</strong> for targeted queries (UniProt REST API, NCBI E-utilities, RCSB PDB REST API) when you need a specific subset of data. (3) Implement <strong>rate-limiting awareness</strong> — NCBI E-utilities limit to 3 requests/second without an API key; UniProt recommends caching results. (4) Use <strong>BioPython</strong> for parsing downloaded data — `SeqIO.parse()` handles FASTA, `MMCIFParser` handles mmCIF, and `Entrez` module interfaces with NCBI E-utilities. (5) <strong>Version-track your data</strong> — always record database release dates and download URLs for reproducibility. API access documentation is available at <a href="https://data.rplpeptides.com">RPL Peptides Data</a>.</p>
</div>

<div class="faq-item">
  <h3>Which antimicrobial peptide database is the most comprehensive?</h3>
  <p><strong>DRAMP 3.0</strong> (Data Repository of Antimicrobial Peptides) is the most comprehensive, with over 22,000 entries drawn from 17 distinct sources including APD3, CAMP, literature, and patent databases. It uniquely categorizes entries as natural, synthetic, patented, or clinical candidates. <strong>DBAASP v3</strong> provides the most detailed quantitative activity data (MIC values against specific strains). <strong>APD3</strong> maintains the highest curation standards with experimental validation required for all entries. For most purposes, querying DRAMP for broad coverage and cross-referencing against DBAASP for quantitative activity data provides the most complete picture. No single database captures all known AMPs — systematic literature mining still reveals peptides not present in any database.</p>
</div>

<div class="faq-item">
  <h3>How can I find structural information for my peptide of interest?</h3>
  <p>Start by searching the <strong>PDB</strong> (rcsb.org) using your peptide's sequence. The RCSB PDB offers sequence similarity search (BLAST against PDB sequences) and text search by peptide name. If no experimental structure exists: (1) Check the <strong>AlphaFold Protein Structure Database</strong> (alphafold.ebi.ac.uk) for predicted structures — coverage includes most UniProt sequences. (2) Use <strong>ESMFold</strong> or <strong>AlphaFold2</strong> to predict the structure locally. (3) Search for structures of close homologs in PDB — a structure of a related peptide may inform your peptide's conformation. (4) For peptide-protein complexes, search with the protein receptor's PDB ID and filter for peptide ligands. (5) NMR ensembles in the PDB may capture peptide conformational flexibility more accurately than single crystal structures. Note that short, flexible peptides may not have stable structures in isolation — their bound conformations are more relevant for functional analysis.</p>
</div>

<div class="faq-item">
  <h3>What data formats should I use for storing and exchanging peptide data?</h3>
  <p><strong>For sequences:</strong> <strong>FASTA format</strong> is the universal standard. Ensure headers contain unique identifiers and source information. <strong>For structures:</strong> Use <strong>mmCIF</strong> (PDBx/mmCIF) as the modern standard — it avoids the fixed-column limitations of legacy PDB format and supports comprehensive metadata. <strong>For modified peptides:</strong> Use <strong>HELM notation</strong> (Hierarchical Editing Language for Macromolecules) which represents complex peptides including non-natural amino acids, cyclizations, and conjugates. <strong>For chemical information:</strong> <strong>SMILES</strong> for simple representations, <strong>SDF</strong> for structures with coordinates. <strong>For tabular data:</strong> <strong>CSV or TSV</strong> with documented column headers — avoid Excel formats for computational workflows. <strong>For metadata:</strong> Use <strong>JSON</strong> for structured metadata that doesn't fit tabular formats. When depositing data, follow community standards (MIAPE for proteomics, PDB deposition guidelines for structures).</p>
</div>

<div class="faq-item">
  <h3>How do I handle peptides with post-translational modifications in database searches?</h3>
  <p>Post-translational modifications (PTMs) complicate database searching because: (1) Many databases store only the unmodified sequence, and (2) standard BLAST cannot match modified residues to their unmodified counterparts. Strategies: (1) <strong>UniProtKB</strong> annotates PTMs in the "PTM/Processing" section — search by unmodified sequence and review PTM annotations. (2) <strong>PhosphoSitePlus</strong> is the most comprehensive PTM-specific database for phosphorylation, acetylation, ubiquitination, and other modifications. (3) <strong>dbPTM</strong> integrates PTM data from multiple sources with structural mapping. (4) For <strong>database searching with mass spectrometry data</strong>, specify variable modifications in your search engine (MaxQuant, Mascot, MSFragger) — this allows matching spectra to modified peptide forms. (5) For <strong>sequence-similarity searching</strong> of modified peptides, search using the unmodified sequence and manually examine PTM annotations of hits. Modified peptide resources are available at <a href="https://data.rplpeptides.com">RPL Peptides Data</a>.</p>
</div>

<div class="faq-item">
  <h3>How do I integrate data from multiple peptide databases into a unified analysis?</h3>
  <p>A multi-database integration workflow: (1) <strong>Define your integration schema</strong> — identify which fields you need from each database (e.g., sequence from UniProt, MIC from DBAASP, structure from PDB). (2) <strong>Retrieve data</strong> programmatically using APIs or bulk downloads for each source. (3) <strong>Map identifiers</strong> using UniProt's ID mapping service to convert between database-specific accessions. (4) <strong>Merge by sequence identity</strong> — peptides with identical sequences are the same entity, even if database accessions differ. At 100% identity, merge confidently; at ≥90%, require manual review for near-identical isoforms. (5) <strong>Handle conflicting annotations</strong> — when databases disagree (e.g., one lists a peptide as AMP, another doesn't), flag conflicts and prefer curated sources. (6) <strong>Store in a structured format</strong> — SQLite or Pandas DataFrame for tabular data, or a custom JSON schema for nested data. (7) <strong>Version-control your integration code</strong> — database schemas change, and reproducible analyses require reproducible data processing.</p>
</div>

<div class="faq-item">
  <h3>What are the limitations of peptide databases I should be aware of?</h3>
  <p>Key limitations include: (1) <strong>Publication bias:</strong> Negative results (peptides tested and found inactive) are rarely published and almost never entered into databases, skewing datasets toward positive examples. (2) <strong>Taxonomic bias:</strong> AMP databases are heavily biased toward amphibian, insect, and mammalian sources, with underrepresentation of microbial, plant, and marine peptides. (3) <strong>Assay heterogeneity:</strong> "Antimicrobial" is defined by different assays with different conditions (inoculum size, media, incubation time), making cross-study comparisons problematic. (4) <strong>Annotation lag:</strong> Peptides discovered in the literature typically take 1-3 years to appear in curated databases. (5) <strong>Sequence errors:</strong> Errors in deposited sequences (from sequencing errors, translation errors, or database entry errors) propagate through analyses — cross-reference multiple sources. (6) <strong>Missing metadata:</strong> Many entries lack information on synthesis method, purity, formulation, or assay conditions that affect experimental reproducibility. (7) <strong>Database-specific formats:</strong> Lack of standardization makes data integration time-consuming. Awareness of these limitations is essential for interpreting database-derived results appropriately.</p>
</div>

<div class="faq-item">
  <h3>How can I contribute my peptide data to public databases?</h3>
  <p>Contributing data strengthens the entire research community: (1) <strong>For sequences:</strong> Submit to GenBank/ENA/DDBJ (International Nucleotide Sequence Database Collaboration) — peptide sequences are typically submitted as part of nucleotide or protein sequence records. (2) <strong>For structures:</strong> Deposit in the PDB — structural data must be deposited upon publication for most journals. (3) <strong>For proteomics data:</strong> Submit raw and processed mass spectrometry data to PRIDE or MassIVE (through ProteomeXchange) — this is required by many journals and funding agencies. (4) <strong>For AMP data:</strong> Contact APD3 or DRAMP curators with your published data for inclusion. (5) <strong>For functional data:</strong> DBAASP accepts submissions with quantitative activity data. (6) <strong>General guidance:</strong> Follow community data standards, include comprehensive metadata (synthesis protocols, purification methods, assay conditions), use persistent sample identifiers, and publish under open licenses (CC0 or CC-BY) to maximize reusability. The <a href="https://rplpeptides.com">RPL Peptides</a> platform also provides resources for peptide data management and sharing.</p>
</div>

## References

1. UniProt Consortium. (2023). UniProt: the Universal Protein Knowledgebase in 2023. *Nucleic Acids Research*, 51(D1), D523–D531. [https://doi.org/10.1093/nar/gkac1052](https://doi.org/10.1093/nar/gkac1052)

2. wwPDB Consortium. (2019). Protein Data Bank: the single global archive for 3D macromolecular structure data. *Nucleic Acids Research*, 47(D1), D520–D528. [https://doi.org/10.1093/nar/gky1004](https://doi.org/10.1093/nar/gky1004)

3. Wang, G., Li, X., & Wang, Z. (2016). APD3: the antimicrobial peptide database as a tool for research and education. *Nucleic Acids Research*, 44(D1), D1087–D1093. [https://doi.org/10.1093/nar/gkv1278](https://doi.org/10.1093/nar/gkv1278)

4. Waghu, F.H., Barai, R.S., Gurung, P., & Idicula-Thomas, S. (2016). CAMPR3: a database on sequences, structures and signatures of antimicrobial peptides. *Nucleic Acids Research*, 44(D1), D1094–D1097. [https://doi.org/10.1093/nar/gkv1153](https://doi.org/10.1093/nar/gkv1153)

5. Shi, G., Kang, X., Dong, F., Liu, Y., Zhu, N., Hu, Y., Xu, H., Lao, X., & Zheng, H. (2022). DRAMP 3.0: an enhanced comprehensive data repository of antimicrobial peptides. *Nucleic Acids Research*, 50(D1), D488–D496. [https://doi.org/10.1093/nar/gkab1027](https://doi.org/10.1093/nar/gkab1027)

6. Pirtskhalava, M., Amstrong, A.A., Grigolava, M., Chubinidze, M., Alimbarashvili, E., Vishnepolsky, B., Gabrielian, A., Rosenthal, A., Hurt, D.E., & Tartakovsky, M. (2021). DBAASP v3: database of antimicrobial/cytotoxic activity and structure of peptides as a resource for development of new therapeutics. *Nucleic Acids Research*, 49(D1), D288–D297. [https://doi.org/10.1093/nar/gkaa991](https://doi.org/10.1093/nar/gkaa991)

7. Singh, S., Chaudhary, K., Dhanda, S.K., Bhalla, S., Usmani, S.S., Gautam, A., Tuknait, A., Agrawal, P., Mathur, D., & Raghava, G.P.S. (2016). SATPdb: a database of structurally annotated therapeutic peptides. *Nucleic Acids Research*, 44(D1), D1119–D1126. [https://doi.org/10.1093/nar/gkv1274](https://doi.org/10.1093/nar/gkv1274)

8. Tyagi, A., Tuknait, A., Anand, P., Gupta, S., Sharma, M., Mathur, D., Joshi, A., Singh, S., Gautam, A., & Raghava, G.P.S. (2015). CancerPPD: a database of anticancer peptides and proteins. *Nucleic Acids Research*, 43(D1), D837–D843. [https://doi.org/10.1093/nar/gku1198](https://doi.org/10.1093/nar/gku1198)

9. Desiere, F., Deutsch, E.W., King, N.L., Nesvizhskii, A.I., Mallick, P., Eng, J., Chen, S., Eddes, J., Loevenich, S.N., & Aebersold, R. (2006). The PeptideAtlas project. *Nucleic Acids Research*, 34(suppl_1), D655–D658. [https://doi.org/10.1093/nar/gkj040](https://doi.org/10.1093/nar/gkj040)

10. Perez-Riverol, Y., Bai, J., Bandla, C., García-Seisdedos, D., Hewapathirana, S., Kamatchinathan, S., Kundu, D.J., Prakash, A., Frericks-Zipper, A., Eisenacher, M., Walzer, M., Wang, S., Brazma, A., & Vizcaíno, J.A. (2022). The PRIDE database resources in 2022: a hub for mass spectrometry-based proteomics evidences. *Nucleic Acids Research*, 50(D1), D543–D552. [https://doi.org/10.1093/nar/gkab1038](https://doi.org/10.1093/nar/gkab1038)

11. Shtatland, T., Guettler, D., Kossodo, M., Pivovarov, M., & Weissleder, R. (2007). PepBank — a database of peptides based on sequence text mining and public peptide data sources. *BMC Bioinformatics*, 8, 280. [https://doi.org/10.1186/1471-2105-8-280](https://doi.org/10.1186/1471-2105-8-280)

12. Usmani, S.S., Bedi, G., Samuel, J.S., Singh, S., Kalra, S., Kumar, P., Ahuja, A.A., Sharma, M., Gautam, A., & Raghava, G.P.S. (2017). THPdb: database of FDA-approved peptide and protein therapeutics. *PLoS ONE*, 12(7), e0181748. [https://doi.org/10.1371/journal.pone.0181748](https://doi.org/10.1371/journal.pone.0181748)

13. Wilkinson, M.D., Dumontier, M., Aalbersberg, I.J., Appleton, G., Axton, M., Baak, A., Blomberg, N., Boiten, J.W., da Silva Santos, L.B., Bourne, P.E., Bouwman, J., Brookes, A.J., Clark, T., Crosas, M., Dillo, I., Dumon, O., Edmunds, S., Evelo, C.T., Finkers, R., ... & Mons, B. (2016). The FAIR Guiding Principles for scientific data management and stewardship. *Scientific Data*, 3, 160018. [https://doi.org/10.1038/sdata.2016.18](https://doi.org/10.1038/sdata.2016.18)

14. Minkiewicz, P., Iwaniak, A., & Darewicz, M. (2019). BIOPEP-UWM database of bioactive peptides: current opportunities. *International Journal of Molecular Sciences*, 20(23), 5978. [https://doi.org/10.3390/ijms20235978](https://doi.org/10.3390/ijms20235978)

15. Zamyatnin, A.A. (2009). Fragmentomics of proteins and natural oligopeptides. *Biochemistry (Moscow)*, 73(13), 1457–1471. [https://doi.org/10.1134/S000629790813003X](https://doi.org/10.1134/S000629790813003X)
