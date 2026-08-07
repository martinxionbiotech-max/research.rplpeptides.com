---
title: Targeted Peptide Drug Delivery — Active Targeting, Cell-Penetrating Peptides, and Blood-Brain Barrier Strategies
description: "Comprehensive review of targeted peptide drug delivery including RGD/NGR/iRGD tumor-homing peptides, cell-penetrating peptides, receptor-mediated transcytosis, and blood-brain barrier penetration technologies."
---

# Targeted Peptide Drug Delivery — Active Targeting, Cell-Penetrating Peptides, and Blood-Brain Barrier Strategies

## Executive Summary

The therapeutic potential of many drugs—and particularly of macromolecular therapeutics—is constrained not by a lack of biological activity but by an inability to reach the intended site of action at sufficient concentration. The challenge of targeted drug delivery is the challenge of spatial precision: delivering the therapeutic to the right cells, in the right tissue, while minimizing exposure to all other cells and tissues. For peptide therapeutics, which often act on extracellular receptors or intracellular targets with exquisite potency and specificity, achieving adequate target tissue concentrations while avoiding dose-limiting off-target effects is frequently the primary determinant of clinical success or failure.

This article provides a comprehensive examination of the principal targeting strategies employed for peptide drug delivery. We analyze active targeting using tumor-homing peptide ligands (RGD, NGR, iRGD), cell-penetrating peptides (TAT, penetratin, and their engineered derivatives), receptor-mediated transcytosis pathways for biological barrier penetration (transferrin receptor, insulin receptor, LRP1), tumor microenvironment targeting approaches, and strategies for crossing the blood-brain barrier. For each strategy, we examine the molecular mechanisms, the evidence for targeting efficacy in preclinical and clinical settings, and the key challenges limiting clinical translation. The article concludes with an assessment of the current targeting landscape and the research directions most likely to yield clinically impactful targeted peptide delivery systems.

---

## Background

### The Targeting Imperative

The concept of targeted drug delivery—Paul Ehrlich's "magic bullet"—was articulated over a century ago, yet remains incompletely realized. For peptide therapeutics, the targeting imperative arises from several interrelated challenges: peptides often act on receptors that are widely expressed, creating the potential for mechanism-based toxicity at non-target sites; the potent biological activity of many peptides (EC₅₀ values in the pM–nM range) demands delivery to the target tissue at similarly low concentrations, which is difficult to achieve with untargeted systemic administration; and intracellular peptide targets (transcription factors, protein-protein interaction interfaces, epigenetic regulators) are inaccessible to peptides that cannot cross the plasma membrane efficiently.

Untargeted systemic administration of peptides results in a biodistribution dominated by the organs of clearance (kidneys, liver) and the blood volume, with fractions of the injected dose reaching most target tissues that rarely exceed 0.1–1% per gram. For peptides with narrow therapeutic indices, the dose required to achieve therapeutic target tissue concentrations may produce unacceptable toxicity at sites of accumulation or through mechanism-based effects at non-target receptors. Targeting strategies aim to shift the biodistribution toward the target tissue, increasing the therapeutic index by increasing target exposure, decreasing non-target exposure, or both.

### Passive vs. Active Targeting

Passive targeting relies on the physicochemical properties of the drug or delivery system to achieve preferential distribution to the target tissue. The enhanced permeability and retention (EPR) effect—the preferential accumulation of macromolecules and nanoparticles in tumors due to leaky vasculature and impaired lymphatic drainage—is the most prominent example of passive targeting. While historically central to the nanomedicine field, the EPR effect has proven insufficient for many applications. Human tumors exhibit heterogeneous and often limited EPR, the elevated interstitial fluid pressure in tumors opposes convective transport, and the dense extracellular matrix of desmoplastic tumors presents a physical barrier even to extravasated nanoparticles.

Active targeting employs molecular recognition—specific binding of a ligand on the drug or delivery system to a receptor or antigen on the target cell—to increase drug accumulation and/or cellular internalization at the target site. Active targeting can complement passive targeting (increasing the retention and internalization of passively extravasated nanoparticles) or, for certain targets, enable targeting independent of passive mechanisms (e.g., targeting of circulating cells, targeting of vascular endothelial cells, or targeting enabled by transcytosis across biological barriers).

### The Landscape of Targeting Ligands

The molecular toolbox for active targeting includes antibodies and antibody fragments (providing the highest affinity and specificity but substantial size), peptides (providing smaller size, ease of synthesis, and reduced immunogenicity), aptamers (nucleic acid-based ligands with antibody-like specificity and chemical synthesis), and small molecules (providing minimal size and well-defined chemistry). For peptide drug delivery, peptide-based targeting ligands are particularly attractive because they can be co-synthesized with the therapeutic peptide as a single molecular entity (fusion protein, peptide conjugate), avoiding the complexity of conjugation chemistry and the potential for batch-to-batch variability in ligand density associated with nanoparticle functionalization.

---

## Tumor-Homing Peptides: Active Targeting to Cancer

### RGD Peptides and Integrin Targeting

The Arg-Gly-Asp (RGD) tripeptide motif was identified in the 1980s as the minimal recognition sequence for integrin binding, present in extracellular matrix proteins including fibronectin, vitronectin, fibrinogen, and osteopontin. Integrins are heterodimeric (α/β) transmembrane receptors that mediate cell-extracellular matrix adhesion and bidirectional signal transduction. Several integrins, particularly αvβ3 and αvβ5, are overexpressed on tumor vasculature endothelial cells and on many tumor cell types, while showing limited expression on quiescent endothelium and most normal tissues. This expression pattern makes αvβ3 and αvβ5 attractive targets for tumor-selective delivery.

**Linear vs. Cyclic RGD:** Linear RGD peptides bind integrins with relatively low affinity (IC₅₀ in the μM range) and are susceptible to proteolytic degradation. Cyclization—most commonly through disulfide bond formation between cysteine residues flanking the RGD motif, or through head-to-tail cyclization—constrains the peptide in the active conformation, increasing affinity by 10–100× (to nM IC₅₀ values) and conferring resistance to exopeptidases. The cyclic pentapeptide c(RGDfK) [cyclo(Arg-Gly-Asp-D-Phe-Lys)], developed by Kessler and colleagues, is the most widely used RGD ligand for targeting applications, with sub-nanomolar affinity for αvβ3. The D-phenylalanine residue and the lysine side chain provide conformational constraint and a conjugation handle, respectively.

**RGD-Mediated Nanoparticle Targeting:** The most extensively investigated application of RGD peptides is the surface functionalization of nanoparticles for tumor-targeted delivery. RGD-conjugated liposomes, PLGA nanoparticles, polymeric micelles, and dendrimers have been shown to enhance tumor accumulation and cellular uptake in αvβ3-expressing tumor models. However, the magnitude of targeting enhancement attributable to the RGD ligand—as opposed to passive EPR accumulation—has been debated. Quantitative studies using matched targeted and non-targeted nanoparticles suggest that RGD functionalization primarily increases cellular internalization after passive extravasation, rather than substantially increasing total tumor accumulation, consistent with the "binding site barrier" hypothesis: high-affinity binding of nanoparticles to perivascular tumor cells or endothelial integrins limits their penetration into the tumor interior.

**Clinical Translation of RGD-Targeted Therapeutics:** Radiolabeled RGD peptides have been developed as molecular imaging agents for positron emission tomography (PET) and single-photon emission computed tomography (SPECT), exploiting the integrin overexpression on tumor vasculature for non-invasive tumor detection and staging. [¹⁸F]Galacto-RGD and [⁶⁸Ga]NOTA-RGD have been evaluated in clinical imaging studies, demonstrating specific tumor uptake and correlation with αvβ3 expression. RGD-targeted therapeutic conjugates, including RGD-drug conjugates and RGD-targeted nanoparticles, are in various stages of preclinical and early clinical development, though no RGD-targeted therapeutic has yet achieved broad regulatory approval.

### NGR Peptides and Aminopeptidase N (CD13) Targeting

The Asn-Gly-Arg (NGR) tripeptide motif targets aminopeptidase N (APN/CD13), a membrane-bound metalloprotease that is overexpressed on tumor vasculature endothelial cells and on several tumor cell types. NGR was identified through in vivo phage display screening for peptides that home to tumor blood vessels.

**Cyclic NGR Peptides:** As with RGD, cyclization substantially improves the binding affinity and metabolic stability of NGR peptides. Cyclic CNGRC peptides bind to a specific isoform of CD13 that is selectively expressed on tumor vasculature, distinct from the CD13 isoform expressed on normal endothelial cells and myeloid cells. This isoform selectivity—arising from differential glycosylation or conformational differences in tumor-associated CD13—is critical for tumor targeting specificity.

**NGR-Drug Conjugates:** NGR peptides conjugated to tumor necrosis factor-alpha (TNF-α), designated NGR-hTNF, represent the most clinically advanced NGR-targeted therapeutic. NGR-hTNF (developed by MolMed as NGR015) selectively delivers TNF-α to tumor vasculature, inducing endothelial cell apoptosis and vascular disruption at doses that would cause systemic toxicity with untargeted TNF-α. Phase II and III clinical trials have evaluated NGR-hTNF in mesothelioma, ovarian cancer, and hepatocellular carcinoma, with evidence of biological activity and a favorable safety profile, though confirmatory Phase III results are pending.

### iRGD: The Tumor-Penetrating Peptide

iRGD (CRGDK/RGPD/EC, a cyclic peptide containing the RGD motif and a C-terminal CendR motif) represents a significant advance in tumor-homing peptide design. Discovered by Ruoslahti and colleagues through in vivo phage display, iRGD operates through a unique three-step mechanism: binding to αv integrins on tumor vasculature (Step 1), proteolytic cleavage by cell-surface proteases exposing a cryptic CendR motif (R/KXXR/K) at the C-terminus (Step 2), and binding of the CendR motif to neuropilin-1 (NRP-1), triggering tissue penetration through activation of a transcytosis-like transport pathway (Step 3).

This mechanism distinguishes iRGD from conventional targeting peptides: rather than simply accumulating in tumor tissue, iRGD actively transports co-administered drugs (or conjugated cargo) deep into the tumor parenchyma. The tumor-penetrating effect has been demonstrated for co-administered small-molecule drugs, nanoparticles, and macromolecular therapeutics, with iRGD co-administration increasing the penetration and efficacy of diverse anticancer agents in preclinical models.

**iRGD Conjugates and Co-Administration:** iRGD-drug conjugates have been developed for targeted cancer therapy, and Phase I clinical trials of iRGD-conjugated chemotherapeutics are underway. The co-administration strategy—injecting iRGD alongside an untargeted therapeutic—is particularly attractive because it decouples the targeting function from the therapeutic, potentially enabling application to diverse therapeutic modalities without requiring modification of each drug. However, clinical translation of co-administration has been slowed by regulatory and commercial challenges distinct from those of conjugated targeting approaches.

---

## Cell-Penetrating Peptides (CPPs)

Cell-penetrating peptides are short peptide sequences (typically 5–30 amino acids) capable of translocating across the plasma membrane and delivering conjugated cargo molecules into the cytoplasm and/or nucleus of cells. CPPs have revolutionized the intracellular delivery of otherwise membrane-impermeable cargo including peptides, proteins, nucleic acids, and nanoparticles.

### Major CPP Classes

**Cationic CPPs:** The HIV-1 transactivator of transcription (TAT) protein-derived peptide (TAT₄₇₋₅₇: YGRKKRRQRRR) is the prototypical cationic CPP. TAT and related cationic CPPs are rich in arginine and lysine residues, with the guanidinium group of arginine being particularly important for membrane translocation. The mechanism of uptake involves initial electrostatic interaction of the cationic peptide with negatively charged cell-surface proteoglycans (heparan sulfate), followed by internalization through multiple endocytic pathways including macropinocytosis, clathrin-mediated endocytosis, and caveolae-mediated endocytosis. Endosomal escape—release of the CPP-cargo from endosomes before degradation in lysosomes—is the rate-limiting step for cytosolic delivery and is often inefficient (<5–10% of internalized CPP-cargo reaches the cytosol).

**Polyarginine Peptides:** Oligoarginines (R₆–R₁₂) are among the most efficient CPPs for many cargo types. The uptake efficiency generally increases with arginine chain length up to R₈–R₉, with R₉ widely considered the optimal length balancing uptake and cytotoxicity. The critical role of the guanidinium group—rather than simple positive charge—in membrane translocation is demonstrated by the observation that polyarginine is far more effective than polylysine of equivalent length, and that the guanidinium bidentate hydrogen bonding with phosphate and sulfate groups on membrane components is essential.

**Amphipathic CPPs:** Penetratin (RQIKIWFQNRRMKWKK), derived from the Antennapedia homeodomain of Drosophila, is the founding member of the amphipathic CPP class. Penetratin and related peptides (transportan, Pep-1, CADY) contain both cationic and hydrophobic residues and are predicted to form amphipathic α-helices upon membrane interaction. The amphipathic character may facilitate both membrane interaction and endosomal escape through membrane perturbation.

**Hydrophobic CPPs:** A subset of CPPs, including the Kaposi fibroblast growth factor (FGF) signal peptide-derived sequence (AAVALLPAVLLALLAP), are predominantly hydrophobic and translocate through mechanisms distinct from the electrostatic interactions of cationic CPPs, possibly involving direct membrane translocation.

### Mechanisms of Internalization

CPP internalization was initially believed to occur through a direct, energy-independent translocation mechanism. However, early studies were confounded by artifacts—particularly CPP redistribution during cell fixation for microscopy, which produced apparent nuclear and cytosolic localization that was absent in live-cell imaging. The current consensus recognizes that CPP internalization is predominantly endocytic, with multiple endocytic pathways operating depending on the CPP, the cargo, the cell type, and the experimental conditions.

**Macropinocytosis** is the principal uptake pathway for TAT, polyarginine, and many other cationic CPPs. Macropinocytosis is an actin-driven process involving membrane ruffling and the formation of large (>0.2 μm) endocytic vesicles (macropinosomes) that sample extracellular fluid. CPP interaction with cell-surface proteoglycans triggers intracellular signaling cascades (Rac1 activation, PAK1 phosphorylation) that stimulate actin reorganization and macropinocytosis. The macropinocytic uptake of CPP-cargo complexes is cargo-size-dependent: small molecules and short peptides are internalized efficiently, while large nanoparticles (>200–500 nm) may be excluded or internalized through alternative pathways.

**Clathrin-mediated endocytosis** and **caveolae-mediated endocytosis** contribute to CPP uptake in a CPP- and cell-type-dependent manner. CPP-cargo complexes internalized through these pathways are delivered to early endosomes, where the fate decision between recycling (return to the cell surface) and degradation (maturation to late endosomes and lysosomes) determines the fraction of internalized cargo that reaches the cytosol.

**Endosomal Escape:** The fraction of CPP-cargo that escapes endosomes to reach the cytosol is typically low (estimated at <5–10%) and represents the principal bottleneck in CPP-mediated delivery. Strategies to enhance endosomal escape include: incorporation of fusogenic peptides (derived from viral fusion proteins, e.g., influenza hemagglutinin HA2 peptide, Gp41) that induce endosomal membrane fusion at acidic pH; incorporation of pH-sensitive membrane-disrupting polymers (poly(propylacrylic acid), poly(histidine)) that undergo conformational transitions at endosomal pH, disrupting the endosomal membrane; photochemical internalization using photosensitizers that generate reactive oxygen species upon light activation, permeabilizing endosomal membranes; and co-administration of endosomolytic agents (chloroquine, known to buffer endosomal pH and inhibit lysosomal enzyme activity).

### Cargo Conjugation Strategies

CPPs can be conjugated to therapeutic peptide cargo through several strategies. **Covalent conjugation** via amide bond formation (CPP N-terminus to cargo C-terminus, or vice versa) or through disulfide bonds (reducible in the reducing intracellular environment, releasing free cargo) provides a defined, single-molecular-entity product. The conjugation site and linker length can influence both the CPP's translocation activity and the cargo's biological activity. **Non-covalent complexation**, exploiting electrostatic interactions between cationic CPPs and anionic cargo (particularly nucleic acids but also certain acidic peptides), avoids the need for chemical conjugation but may produce complexes with variable stoichiometry and stability. **Fusion protein expression**, for CPP-protein therapeutics, enables recombinant production of CPP-cargo fusions.

### Limitations and Selectivity Challenges

The principal limitation of CPPs for therapeutic peptide delivery is their lack of cell-type selectivity. Cationic CPPs interact with ubiquitously expressed cell-surface proteoglycans, resulting in uptake by essentially all mammalian cell types. While this broad tropism is advantageous for applications where widespread intracellular delivery is desired, it is problematic for applications requiring target-cell selectivity.

Several strategies have been developed to address the selectivity challenge. **Activatable CPPs (ACPPs)** employ a polyanionic inhibitory domain connected to the CPP via a cleavable linker; the inhibitory domain electrostatically neutralizes the CPP, and cleavage of the linker by disease-associated proteases (e.g., matrix metalloproteinases in tumors) exposes the CPP, activating cell-penetrating activity selectively at the disease site. **Targeted CPPs** combine a CPP with a targeting ligand (antibody, peptide, small molecule) that directs uptake to cells expressing the target receptor, combining the delivery efficiency of CPPs with the selectivity of active targeting. **Stimuli-responsive CPPs** employ environmentally sensitive linkers (pH-sensitive, redox-sensitive) that release the CPP-cargo only under specific physiological conditions (e.g., the low pH of the tumor microenvironment or the reducing environment of the cytosol).

---

## Receptor-Mediated Transcytosis

Receptor-mediated transcytosis (RMT) is the physiological process by which macromolecules are transported across cellular barriers through receptor binding, endocytosis, vesicular transport across the cell, and exocytosis at the opposite membrane. RMT is the principal route by which large molecules cross the endothelial barriers of the brain and other privileged tissue compartments, and it provides a mechanism for targeted delivery across otherwise impermeable biological barriers.

### Transferrin Receptor (TfR)-Mediated Transcytosis

The transferrin receptor is a homodimeric type II transmembrane glycoprotein that mediates the cellular uptake of iron-loaded transferrin (holo-transferrin). TfR is highly expressed on the luminal (blood-facing) membrane of brain capillary endothelial cells—the cellular substrate of the blood-brain barrier (BBB)—and constitutively undergoes clathrin-mediated endocytosis and recycling.

The high expression level, constitutive endocytosis, and capacity to transport large cargo (the ~80 kDa transferrin-iron complex is the native substrate) make TfR the most extensively exploited RMT target for brain delivery. Approaches to harness TfR for therapeutic delivery include:

**Anti-TfR Antibodies:** Monoclonal antibodies against TfR, particularly those binding epitopes distinct from the transferrin binding site (to avoid competition with endogenous transferrin), are internalized by TfR-expressing cells. Anti-TfR antibodies have been conjugated to therapeutic payloads (enzymes for lysosomal storage diseases, neurotrophic factors for neurodegenerative diseases) or used to functionalize nanoparticles for brain delivery. However, the high-affinity binding of conventional anti-TfR antibodies can result in lysosomal degradation of the antibody-cargo complex rather than transcytosis, as the antibody-receptor complex is sorted to the degradation pathway rather than the recycling/transcytosis pathway.

**Monovalent and Low-Affinity TfR Binders:** An important mechanistic insight is that monovalent, low-affinity TfR binders—in contrast to bivalent, high-affinity antibodies—are more efficiently transcytosed. Bivalent binding and/or high-affinity binding may cross-link TfR and direct the complex toward lysosomal degradation, while monovalent binding allows the receptor-cargo complex to avoid degradation and undergo transcytosis. This insight has motivated the development of monovalent TfR-binding antibody fragments (Fab, scFv), bispecific antibodies with one TfR-binding arm and one therapeutic target-binding arm, and engineered TfR ligands with tunable affinity. The Roche "Brain Shuttle" technology, employing a monovalent anti-TfR Fab fused to a therapeutic antibody, exemplifies this approach and has advanced to clinical evaluation for Alzheimer's disease (anti-amyloid-β antibody with brain shuttle).

### Insulin Receptor-Mediated Transcytosis

The insulin receptor, like TfR, is highly expressed on brain capillary endothelial cells and undergoes constitutive endocytosis, providing an RMT pathway for brain delivery. However, the insulin receptor presents unique challenges: insulin binding triggers intracellular signaling (metabolic effects) that can be undesirable, and the receptor's endogenous ligand (insulin) is present at variable concentrations depending on the metabolic state, potentially competing with exogenous targeting ligands.

Strategies to exploit the insulin receptor for brain delivery while avoiding these challenges include the use of anti-insulin receptor antibodies that bind epitopes distinct from the insulin binding site (minimizing competition) and that do not activate insulin signaling (minimizing metabolic effects). Anti-insulin receptor antibodies have been used to deliver therapeutic payloads including enzymes (iduronate 2-sulfatase for Hunter syndrome) and neurotrophic factors (BDNF for neurodegenerative diseases) across the BBB in preclinical models.

### LRP1 and LRP2 (Megalin)-Mediated Transcytosis

The low-density lipoprotein receptor-related protein 1 (LRP1) and LRP2 (megalin) are multifunctional endocytic receptors that mediate the transcytosis of diverse ligands across the BBB and other biological barriers. LRP1 ligands include apolipoprotein E (ApoE), α₂-macroglobulin, tissue plasminogen activator, and lactoferrin. The receptor-associated protein (RAP) is a chaperone that binds LRP1 and can be used as a targeting ligand for LRP1-mediated delivery.

Angiopep-2 (TFFYGGSRGKRNNFKTEEY), a 19-amino acid peptide derived from the Kunitz domain of aprotinin, was identified by AngioChem (now part of Collectar) as a ligand that undergoes efficient LRP1-mediated transcytosis across the BBB. Angiopep-2 has been conjugated to therapeutic payloads including paclitaxel (ANG1005) for brain tumor therapy, with Phase II clinical trials in glioblastoma and brain metastases demonstrating evidence of CNS activity.

### Other RMT Pathways

Additional RMT pathways that have been investigated for targeted delivery include the neonatal Fc receptor (FcRn, mediating IgG transcytosis and exploited by Fc-fusion protein therapeutics), the leptin receptor (mediating leptin transport across the BBB and the blood-CSF barrier), the diphtheria toxin receptor (heparin-binding EGF-like growth factor), and various nutrient transporters (GLUT1 glucose transporter, LAT1 large neutral amino acid transporter). Each pathway presents distinct advantages and limitations with respect to expression level, transport capacity, competition from endogenous ligands, intracellular trafficking fate, and the structural requirements for ligand-mediated transcytosis.

---

## Tumor Microenvironment Targeting

The tumor microenvironment (TME)—the complex ecosystem of cancer cells, stromal cells (fibroblasts, immune cells, pericytes), extracellular matrix components, and soluble factors—offers targeting opportunities that extend beyond cancer-cell-specific receptors. TME targeting strategies exploit characteristic features of the tumor microenvironment that distinguish it from normal tissue.

### Hypoxia-Targeted Delivery

Tumor hypoxia—regions of low oxygen tension (pO₂ < 10 mmHg vs. 30–40 mmHg in normal tissues)—arises from the imbalance between oxygen supply (limited by disorganized, inefficient tumor vasculature) and oxygen demand (high metabolic rate of proliferating cancer cells). Hypoxia is a hallmark of solid tumors, associated with treatment resistance, aggressive phenotype, and poor prognosis, and represents a tumor-specific physiological condition exploitable for targeted delivery.

Hypoxia-responsive elements include nitroimidazole moieties (which undergo enzymatic reduction under hypoxic conditions, forming reactive intermediates that bind cellular macromolecules), azo and quinone linkers (cleaved under reducing/hypoxic conditions), and hypoxia-responsive transcription factor binding sites (hypoxia-inducible factor, HIF, response elements driving gene expression in hypoxic cells). Hypoxia-activated prodrugs and hypoxia-responsive nanoparticles leverage these elements for tumor-selective release.

### pH-Responsive Targeting

The extracellular pH of solid tumors is characteristically acidic (pH 6.5–6.8) compared to normal tissue (pH 7.4), a consequence of the Warburg effect (aerobic glycolysis producing lactic acid) combined with poor vascular clearance of acidic metabolites. This pH differential can be exploited for TME-targeted delivery using pH-responsive linkers or polymers. Hydrazone and cis-aconityl linkers are relatively stable at physiological pH but hydrolyze at the mildly acidic pH of the TME, releasing conjugated drugs. pH-sensitive membrane-disrupting peptides or polymers (pHLIP, GALA peptide) are designed to insert into cell membranes and form pores at acidic pH, enabling the cytosolic delivery of co-administered or conjugated cargo specifically in the TME.

### Enzyme-Responsive Targeting

The TME is characterized by elevated expression of specific proteases, particularly matrix metalloproteinases (MMP-2, MMP-9) and cathepsins, that remodel the extracellular matrix to facilitate tumor invasion and metastasis. These proteases can serve as TME-selective triggers for drug release. Peptide substrates susceptible to specific MMP cleavage have been incorporated into drug conjugates, nanoparticle crosslinks, and pore gatekeepers to achieve MMP-responsive release. The specificity of enzyme-responsive systems depends on the cleavage specificity of the peptide substrate and the selectivity of enzyme overexpression in the tumor relative to normal tissues.

### Extracellular Matrix Targeting

Components of the tumor extracellular matrix that are enriched relative to normal tissue, including tenascin-C, fibronectin extra-domain B (EDB), and oncofetal isoforms of fibronectin, provide targeting antigens that are physically separated from cancer cells but accessible from the vasculature. Antibodies or peptides targeting these ECM components can accumulate in tumors without the requirement for extravasation and penetration to individual cancer cells, potentially circumventing the transport limitations that constrain cancer-cell-targeted approaches. The L19 antibody targeting EDB-fibronectin, conjugated to IL-2 or TNF-α (immunocytokines), has demonstrated tumor-selective delivery in clinical studies.

---

## Blood-Brain Barrier Penetration Strategies

The blood-brain barrier (BBB) represents the most formidable biological barrier to drug delivery in the body. The BBB is formed by brain capillary endothelial cells sealed by continuous tight junctions with extremely low paracellular permeability, expressing efflux transporters (P-glycoprotein, BCRP) that actively export diverse molecules from the brain, and supported by pericytes and astrocyte end-feet that contribute to barrier induction and maintenance. The BBB excludes >98% of small-molecule drugs and virtually all macromolecular therapeutics, making brain delivery a central challenge for peptide therapeutics with CNS targets.

### Receptor-Mediated Transcytosis at the BBB

As detailed in the RMT section above, transferrin receptor, insulin receptor, LRP1, and other RMT pathways provide the most thoroughly validated strategy for macromolecular BBB penetration. The efficiency of RMT-mediated brain delivery depends on the receptor's luminal expression level, the rate of endocytosis, the intracellular trafficking fate (transcytosis vs. lysosomal degradation), and the competition from endogenous ligands. For peptide therapeutics, the major considerations are whether the peptide can be engineered as an RMT ligand itself (if sufficiently small and appropriately structured) or conjugated to an RMT-targeted carrier (antibody, nanoparticle).

### Cell-Penetrating Peptides at the BBB

Certain CPPs, including TAT, penetratin, and SynB vectors (derived from the antimicrobial peptide protegrin), have been reported to cross the BBB in preclinical models. The mechanism is believed to involve adsorptive-mediated transcytosis—electrostatic interaction of cationic CPPs with anionic sites on the luminal endothelial membrane, triggering endocytosis and transcytosis—rather than passive diffusion. However, the efficiency of CPP-mediated BBB transport is generally low, and the lack of selectivity (CPPs cross the BBB but also enter peripheral tissues) raises questions about off-target effects. CPP-BBB delivery remains primarily a preclinical research tool.

### Intranasal Delivery to the Brain

The intranasal route provides a non-invasive path to the brain that bypasses the BBB entirely. Drugs administered to the nasal cavity can reach the brain through the olfactory epithelium and/or the trigeminal nerve pathways, traveling along the olfactory and trigeminal nerves in the perineural spaces to the olfactory bulb and brainstem, respectively. This route is particularly attractive for peptides, which are small enough to traverse the nasal epithelium but too large for effective BBB penetration.

Intranasal peptide delivery to the brain has been demonstrated for insulin (cognitive effects in Alzheimer's disease), oxytocin (social behavior effects in autism), exendin-4/GLP-1 analogs (neuroprotective effects in Parkinson's disease models), and various growth factors (NGF, BDNF, GDNF). Clinical trials of intranasal insulin for Alzheimer's disease and mild cognitive impairment have produced mixed results—evidence of cognitive benefit in some studies but not others—and the optimization of intranasal delivery devices and formulations for reliable, reproducible brain delivery remains an active area of investigation.

The limitations of intranasal brain delivery include low and variable bioavailability (typically <0.1–1% of the administered dose reaching the brain), dependence on head position, nasal patency, and delivery device characteristics, and limited capacity for delivery to brain regions beyond the olfactory bulb and ventral brain surface. For research applications, however, intranasal delivery offers a practical and accessible approach to studying peptide effects in the CNS.

---

## Research Evidence

| Targeting Strategy | Targeting Ligand | Therapeutic Payload | Study Phase | Key Finding | Reference |
|--------------------|------------------|---------------------|-------------|-------------|------------|
| RGD integrin targeting | c(RGDfK) | Doxorubicin liposomes | Preclinical (mouse) | Enhanced tumor uptake and antitumor efficacy vs. non-targeted liposomes | Schiffelers RM, et al. *J Natl Cancer Inst*. 2004 |
| RGD imaging agent | [¹⁸F]Galacto-RGD | — | Clinical (Phase I/II) | Specific tumor uptake; correlation with αvβ3 expression | Beer AJ, et al. *J Nucl Med*. 2006 |
| NGR tumor vasculature targeting | NGR-hTNF | TNF-α | Phase II/III | Tumor-selective vascular disruption; manageable toxicity | Gregorc V, et al. *J Clin Oncol*. 2010 |
| iRGD tumor penetration | iRGD (co-administered) | Nab-paclitaxel | Preclinical (mouse) | 7× increase in tumor drug accumulation; enhanced antitumor efficacy | Sugahara KN, et al. *Cancer Cell*. 2009 |
| TAT CPP intracellular delivery | TAT(47-57) | Pro-apoptotic peptide | Preclinical (mouse) | Tumor growth inhibition; modest selectivity | Snyder EL, et al. *PLoS Biol*. 2004 |
| Activatable CPP (ACPP) | ACPP (MMP-cleavable) | Fluorescent/contrast agents | Phase 0/I | Tumor-selective activation and uptake in clinical specimens; imaging application | Olson ES, et al. *Proc Natl Acad Sci USA*. 2010 |
| Anti-TfR brain delivery | Anti-TfR mAb (monovalent) | Anti-Aβ antibody (Brain Shuttle) | Phase I | 20× increase in brain antibody concentration vs. antibody alone | Niewoehner J, et al. *Neuron*. 2014 |
| Angiopep-2 BBB delivery | Angiopep-2-peptide | Paclitaxel (ANG1005) | Phase II | Evidence of CNS activity in glioblastoma and brain metastases; manageable toxicity | Kumthekar P, et al. *J Clin Oncol*. 2020 |
| Intranasal brain delivery | — | Insulin | Phase II/III | Mixed results; cognitive benefit in some AD/MCI studies; device-dependent delivery | Craft S, et al. *Arch Neurol*. 2012 |
| TfR nanoparticle BBB delivery | Anti-TfR scFv | PLGA nanoparticles | Preclinical (mouse) | 3–4× increase in brain accumulation vs. non-targeted NPs | Kouchakzadeh H, et al. *Drug Deliv Transl Res*. 2019 |
| Hypoxia-activated prodrug | Nitroimidazole linker | Cytotoxic peptide | Preclinical (mouse) | Selective activation under hypoxia; reduced systemic toxicity | Baran N, et al. *Angew Chem Int Ed*. 2019 |
| pH-responsive TME targeting | pHLIP peptide | Cargo (model) | Clinical (Phase I, imaging) | Tumor-selective membrane insertion at acidic pH; imaging feasibility demonstrated | Reshetnyak YK, et al. *Front Bioeng Biotechnol*. 2020 |

---

## Current Understanding

**Targeting ligands improve cellular uptake more than total tissue accumulation.** Quantitative pharmacokinetic studies comparing targeted and non-targeted nanoparticles consistently show that targeting ligands primarily increase cellular internalization of material that has already reached the target tissue through passive mechanisms, rather than substantially increasing the absolute quantity of drug reaching the tissue. The "binding-site barrier"—high-affinity binding of the first targeted nanoparticles reaching the tissue to perivascular target cells, limiting deeper penetration—is a significant limitation for solid tumor targeting.

**Monovalent/low-affinity RMT ligands outperform high-affinity binders for BBB transcytosis.** A counterintuitive finding with important translational implications: strong bivalent binding to TfR or insulin receptor directs the receptor-cargo complex to lysosomal degradation, while weaker monovalent binding allows the complex to avoid degradation and undergo transcytosis. This insight has driven the redesign of BBB-targeted therapeutics from high-affinity antibodies to engineered monovalent binders with optimized affinity.

**The clinical impact of targeting remains to be established.** While numerous targeted delivery systems have demonstrated enhanced tumor accumulation or brain penetration in preclinical models, the clinical evidence that targeting improves patient outcomes—as opposed to improving pharmacokinetic parameters—remains limited. The only definitively successful clinical targeting platform is antibody-drug conjugates (ADCs), where targeting provides the essential function of selective internalization into cancer cells. For peptide-targeted delivery systems, the clinical evidence base is substantially less mature.

**Multi-modal targeting may be necessary.** The biological complexity of drug delivery—multiple sequential barriers (vascular endothelium, extracellular matrix, cell membrane, endosomal membrane, intracellular trafficking)—may require multi-modal targeting strategies that address different barriers at different stages of the delivery process. iRGD's combination of vascular integrin binding (Step 1) and neuropilin-1-mediated tissue penetration (Step 3) exemplifies a multi-step targeting mechanism, and related multi-ligand, multi-barrier strategies are being explored.

---

## Future Research Directions

- **Tunable affinity targeting ligands** that enable systematic optimization of binding affinity to balance tissue accumulation, penetration depth, and off-target binding for each target receptor and tissue context

- **Protease-activated targeting with improved specificity** that harnesses multi-enzyme signatures (requiring cleavage by two or more disease-associated proteases for activation) for improved disease selectivity over single-enzyme activation

- **Transcytosis-optimized BBB carriers** that systematically characterize the intracellular trafficking fate of RMT-targeted cargo as a function of ligand affinity, valency, and epitope, enabling rational design of BBB-penetrant therapeutics

- **Intranasal delivery optimization** through advanced aerosol generation, mucoadhesive formulations, and permeation-enhancing technologies to improve the efficiency, reproducibility, and regional brain distribution of intranasally administered peptides

- **Bispecific and multispecific targeting molecules** that engage multiple targets simultaneously—e.g., one arm for BBB transcytosis (TfR) and one arm for target engagement (CNS therapeutic target)—enabling single-molecule therapeutics that both cross the BBB and exert the desired pharmacological effect

- **Conditionally active biologics** that are inactive in the circulation and activated only within the target tissue through protease cleavage, pH change, or other TME-specific triggers, reducing mechanism-based toxicity from systemic target engagement

- **Targeted delivery to the tumor immune microenvironment** for cancer immunotherapy applications, including delivery of immunostimulatory peptides to tumor-associated macrophages, dendritic cells, or exhausted T cells

- **Machine learning-driven targeting ligand discovery** using in silico screening of peptide libraries against target receptor structures, combined with in vitro and in vivo validation, to accelerate the identification of high-affinity, high-specificity targeting peptides

- **Combination targeting and controlled release** that integrates active targeting with stimuli-responsive release, such that the targeting ligand delivers the carrier to the target tissue and a TME-specific stimulus (pH, enzyme, redox potential) triggers local drug release

- **Theragnostic targeting peptides** that serve dual roles as targeting ligands for therapeutic delivery and as imaging agents for patient stratification, enabling identification of patients most likely to benefit from targeted therapy based on target receptor expression

---

## Frequently Asked Questions

<div class="faq-container">
<div class="faq-section">
<div class="faq-item">
<h3 class="faq-question">What is the difference between active and passive targeting for peptide drug delivery?</h3>
<p>Passive targeting relies on the inherent physicochemical properties of the drug or delivery system to achieve preferential distribution to the target tissue—most notably through the enhanced permeability and retention (EPR) effect, where macromolecules and nanoparticles accumulate in tumors due to leaky vasculature and impaired lymphatic drainage. Active targeting employs specific molecular recognition—a targeting ligand (antibody, peptide, aptamer, or small molecule) on the drug or delivery system binding to a receptor or antigen on the target cell—to increase drug accumulation and/or cellular internalization at the target site. In practice, active targeting primarily enhances the cellular uptake of material that has already reached the target tissue through passive mechanisms, rather than dramatically increasing total tissue accumulation. For peptide therapeutics, the distinction is important because active targeting can enable delivery to targets not accessible through passive mechanisms, including specific cell types within heterogeneous tissues, intracellular targets, and tissues behind biological barriers like the blood-brain barrier.</p>
</div>
<div class="faq-item">
<h3 class="faq-question">How do RGD peptides target tumors and what are their clinical applications?</h3>
<p>RGD (Arg-Gly-Asp) peptides target integrins—specifically αvβ3 and αvβ5 integrins—that are overexpressed on tumor vasculature endothelial cells and on many tumor cell types. Cyclic RGD peptides, such as c(RGDfK), achieve high-affinity binding (nM IC₅₀) through conformational constraint that presents the RGD motif in the optimal integrin-binding orientation. The most advanced clinical application of RGD peptides is molecular imaging: radiolabeled RGD peptides ([¹⁸F]Galacto-RGD, [⁶⁸Ga]NOTA-RGD) are used as PET/SPECT tracers for non-invasive imaging of integrin expression, with applications in tumor detection, staging, and treatment response assessment. RGD-targeted therapeutic conjugates (RGD-drug conjugates, RGD-targeted nanoparticles) are in earlier stages of clinical development. The principal challenge for RGD-targeted therapeutics is that αvβ3 integrins, while overexpressed on tumor tissue, are also expressed at some level in several normal tissues, and the "binding site barrier"—high-affinity binding of targeted agents to perivascular tumor cells limiting deeper tumor penetration—constrains the overall targeting benefit.</p>
</div>
<div class="faq-item">
<h3 class="faq-question">What makes iRGD different from conventional RGD targeting peptides?</h3>
<p>iRGD (CRGDK/RGPD/EC) is distinguished from conventional RGD peptides by its unique three-step mechanism that enables not just tumor accumulation but active tumor penetration. Step 1: the cyclic RGD motif binds to αv integrins on tumor vasculature. Step 2: a cell-surface protease cleaves the peptide, exposing a cryptic C-terminal CendR motif (R/KXXR/K). Step 3: the exposed CendR motif binds to neuropilin-1 (NRP-1), which triggers a transcytosis-like transport pathway that transports the peptide—and importantly, any co-administered cargo—deep into the tumor parenchyma. This tumor-penetrating property distinguishes iRGD: a conventional RGD peptide will bind to and accumulate at perivascular tumor cells, but iRGD will transport co-administered drugs into the tumor interior, substantially increasing the intratumoral drug distribution. Preclinical studies have demonstrated that co-administration of iRGD with diverse anticancer agents (chemotherapy, antibodies, nanoparticles) increases their tumor penetration and antitumor efficacy without increasing systemic toxicity. Phase I clinical trials of iRGD-drug conjugates are underway.</p>
</div>
<div class="faq-item">
<h3 class="faq-question">How do cell-penetrating peptides (CPPs) deliver cargo into cells?</h3>
<p>Cell-penetrating peptides translocate across the plasma membrane through a multi-step process. First, cationic CPPs (TAT, polyarginine, penetratin) electrostatically interact with negatively charged cell-surface proteoglycans (heparan sulfate), concentrating the CPP-cargo at the cell surface. This interaction triggers intracellular signaling (Rac1, PAK1 activation) that stimulates actin reorganization and macropinocytosis—the formation of large endocytic vesicles that engulf extracellular material. The CPP-cargo is internalized within macropinosomes, which mature into early endosomes. The critical and rate-limiting step is endosomal escape: the CPP-cargo must exit the endosome before the endosome matures into a degradative lysosome. Only a small fraction (typically <5–10%) of internalized CPP-cargo successfully escapes to the cytosol. Endosomal escape is believed to occur through CPP-mediated membrane perturbation—the cationic residues interacting with the endosomal membrane and, potentially assisted by the acidic endosomal pH, transiently destabilizing the membrane to allow cargo release. Strategies to improve endosomal escape, including fusogenic peptides and pH-sensitive polymers, are actively being developed.</p>
</div>
<div class="faq-item">
<h3 class="faq-question">Why are CPPs not inherently selective for specific cell types?</h3>
<p>The cell-penetrating activity of cationic CPPs (TAT, polyarginine, penetratin) is driven by electrostatic interactions with cell-surface proteoglycans—particularly heparan sulfate proteoglycans—which are expressed on essentially all mammalian cell types. Unlike receptor-targeted delivery, which requires a specific receptor-ligand interaction, CPP uptake requires only the generic electrostatic interaction with anionic cell-surface components. This universality is both an advantage (CPPs work on virtually any cell type) and a limitation (they cannot discriminate between target and non-target cells). The selectivity problem can be addressed by: activatable CPPs (ACPPs), where a polyanionic inhibitory domain blocks the CPP's activity until cleaved by disease-associated proteases; targeted CPPs, where a targeting ligand (antibody, peptide) directs uptake to cells expressing the target receptor; and stimuli-responsive linkers that release the CPP-cargo only under specific physiological conditions. Despite these advances, achieving sufficient target-cell selectivity for systemic administration remains the central challenge for therapeutic CPP applications. Researchers investigating CPP-mediated delivery approaches can access characterized peptide reference standards through [RPL Peptides](https://rplpeptides.com).</p>
</div>
<div class="faq-item">
<h3 class="faq-question">How does receptor-mediated transcytosis deliver therapeutics across the blood-brain barrier?</h3>
<p>Receptor-mediated transcytosis (RMT) exploits the natural transport pathways that supply the brain with essential macromolecules. Receptors highly expressed on the luminal surface of brain capillary endothelial cells—particularly the transferrin receptor (TfR), insulin receptor, and LRP1—bind their ligands from the bloodstream and are internalized via clathrin-mediated endocytosis. The receptor-ligand complex traffics through the endosomal compartment and, instead of being sorted to lysosomes for degradation, is directed to the abluminal (brain-facing) membrane, where the ligand is released into the brain interstitial fluid. Therapeutic molecules can "hitchhike" on these pathways by conjugation to RMT-targeting ligands—anti-TfR antibodies, anti-insulin receptor antibodies, or peptide ligands such as Angiopep-2 (LRP1). An important design principle is that monovalent, lower-affinity RMT binders are more efficiently transcytosed than bivalent, high-affinity binders, because the latter trigger receptor crosslinking that directs the complex to lysosomal degradation rather than transcytosis. The Roche Brain Shuttle (monovalent anti-TfR Fab fused to therapeutic antibody) exemplifies this principle and has demonstrated substantially increased brain delivery in clinical studies.</p>
</div>
<div class="faq-item">
<h3 class="faq-question">What are the main challenges for targeted peptide delivery to solid tumors?</h3>
<p>Several interrelated challenges limit targeted peptide delivery to solid tumors. The binding-site barrier: high-affinity targeting ligands bind to the first accessible target cells (perivascular tumor cells or endothelial cells), preventing deeper penetration into the tumor parenchyma. Heterogeneous target expression: receptor expression often varies substantially between tumor regions, between primary and metastatic tumors, and over time, making reliable targeting difficult. High interstitial fluid pressure: the elevated pressure within solid tumors opposes convective transport from the vasculature into the tumor interstitium, limiting the extravasation of targeted carriers. Dense extracellular matrix: desmoplastic tumors (pancreatic, some breast cancers) produce a dense ECM that physically impedes the penetration of targeted carriers regardless of their binding properties. And the mismatch between preclinical models (rapidly growing, well-vascularized subcutaneous tumors in mice) and human tumors (slower growing, heterogeneous, often desmoplastic) means that targeting benefits observed in preclinical models often overestimate clinical performance. Strategies to address these challenges include tumor-penetrating peptides (iRGD), ECM-depleting agents co-administered with targeted carriers, and ultrasound-mediated disruption of the tumor microenvironment to enhance delivery.</p>
</div>
<div class="faq-item">
<h3 class="faq-question">How can peptide therapeutics be delivered to the brain without injection into the CNS?</h3>
<p>Three principal non-invasive strategies exist for delivering peptide therapeutics to the brain. First, receptor-mediated transcytosis (RMT) across the blood-brain barrier: conjugating the peptide to a ligand (antibody, peptide) targeting TfR, insulin receptor, or LRP1, as discussed above. Second, intranasal delivery: administering the peptide to the nasal cavity, from which it can reach the brain through the olfactory and trigeminal nerve pathways, bypassing the BBB entirely. This route has been demonstrated for insulin, oxytocin, GLP-1 analogs, and neurotrophic factors, though bioavailability is low (<0.1–1%) and variable. Third, focused ultrasound with microbubbles: ultrasound energy applied to the skull focuses on a target brain region, causing microbubbles in the circulation to oscillate and transiently disrupt the BBB, allowing circulating peptides to enter the brain at the targeted site. This approach provides regional specificity and has been demonstrated in clinical trials, though it requires specialized equipment and the peptide must be present in the circulation during the ultrasound application window (~4–6 hours of BBB opening). Each strategy has distinct advantages and limitations, and the choice depends on the peptide, the target brain region, and the clinical application. Researchers developing CNS-targeted peptides can find characterized reference materials through the <a href="https://data.rplpeptides.com">RPL Peptides Data Center</a>.</p>
</div>
<div class="faq-item">
<h3 class="faq-question">What is the role of tumor microenvironment targeting in peptide delivery?</h3>
<p>Tumor microenvironment (TME) targeting exploits the characteristic features that distinguish tumors from normal tissues—acidic extracellular pH (6.5–6.8 vs. 7.4), hypoxia (low oxygen tension), elevated expression of specific proteases (MMP-2, MMP-9, cathepsins), and abnormal extracellular matrix components (tenascin-C, oncofetal fibronectin). Rather than targeting cancer-cell-specific receptors, TME targeting uses these environmental differences as triggers for selective drug release or activation. Examples include: pH-responsive linkers (hydrazone, cis-aconityl) that hydrolyze in the acidic TME; hypoxia-activated prodrugs using nitroimidazole moieties; MMP-cleavable peptide linkers that release the drug only in protease-rich tumors; and pHLIP peptides that insert into cell membranes selectively at acidic pH. TME targeting offers the advantage that the targets are not subject to the same genetic instability and heterogeneity as cancer cell surface receptors, and the triggers are broadly applicable across many tumor types. The major challenge is achieving sufficient differential between tumor and normal tissue: the pH difference (ΔpH ~0.6–0.9 units) and enzyme expression differences (typically 5–50×) are relatively modest, requiring careful optimization of the responsive element to achieve meaningful tumor selectivity.</p>
</div>
<div class="faq-item">
<h3 class="faq-question">What are the prospects for clinically successful targeted peptide delivery?</h3>
<p>The clinical prospects for targeted peptide delivery vary substantially across targeting strategies and therapeutic applications. The most clinically successful targeting platform to date is antibody-drug conjugates (ADCs), which use antibodies (not peptides) as targeting ligands and have achieved multiple regulatory approvals. Peptide-targeted therapeutics have been less successful, with few achieving regulatory approval. Tumor-homing peptide-targeted imaging agents (RGD-based PET tracers) have demonstrated clinical utility for patient stratification and treatment monitoring. The NGR-TNF conjugate has shown evidence of biological activity in Phase II/III trials, and iRGD-based strategies are advancing. For brain delivery, the anti-TfR antibody-based Brain Shuttle and the Angiopep-2-paclitaxel conjugate (ANG1005) have provided clinical proof-of-concept for RMT-mediated BBB penetration. The field is maturing from an era of phenomenological discovery (identifying peptides that "home" to targets) to mechanistic understanding (quantitatively characterizing the determinants of targeting efficiency), which should improve the translational success rate. The most promising near-term applications appear to be molecular imaging (lower regulatory bar, clear clinical utility), CNS delivery via RMT (addressing an otherwise intractable delivery challenge), and TME-responsive activation (leveraging physiological differences for selectivity). For researchers exploring targeted peptide approaches, characterized targeting peptides with documented purity and identity are available through [RPL Peptides](https://rplpeptides.com).</p>
</div>
</div>

!!! info ""
    **About RPL Peptides:** [RPL Peptides](https://rplpeptides.com) is a supplier of high-purity research peptides with comprehensive analytical documentation including HPLC, LC-MS, and Certificates of Analysis (COA). For researchers developing targeted peptide delivery systems requiring certified reference materials and targeting peptide ligands, visit [rplpeptides.com](https://rplpeptides.com) or explore detailed molecular data at the [RPL Peptides Data Center](https://data.rplpeptides.com).
</div>

---

## References

<ol class="references">
  <li id="ref1">Ruoslahti E. RGD and other recognition sequences for integrins. <em>Annual Review of Cell and Developmental Biology</em>. 1996;12:697–715. <a href="https://doi.org/10.1146/annurev.cellbio.12.1.697">doi:10.1146/annurev.cellbio.12.1.697</a></li>
  <li id="ref2">Sugahara KN, Teesalu T, Karmali PP, et al. Tissue-penetrating delivery of compounds and nanoparticles into tumors. <em>Cancer Cell</em>. 2009;16(6):510–520. <a href="https://doi.org/10.1016/j.ccr.2009.10.013">doi:10.1016/j.ccr.2009.10.013</a></li>
  <li id="ref3">Teesalu T, Sugahara KN, Ruoslahti E. Tumor-penetrating peptides. <em>Frontiers in Oncology</em>. 2013;3:216. <a href="https://doi.org/10.3389/fonc.2013.00216">doi:10.3389/fonc.2013.00216</a></li>
  <li id="ref4">Fonseca SB, Pereira MP, Kelley SO. Recent advances in the use of cell-penetrating peptides for medical and biological applications. <em>Advanced Drug Delivery Reviews</em>. 2009;61(11):953–964. <a href="https://doi.org/10.1016/j.addr.2009.06.001">doi:10.1016/j.addr.2009.06.001</a></li>
  <li id="ref5">Bechara C, Sagan S. Cell-penetrating peptides: 20 years later, where do we stand? <em>FEBS Letters</em>. 2013;587(12):1693–1702. <a href="https://doi.org/10.1016/j.febslet.2013.04.031">doi:10.1016/j.febslet.2013.04.031</a></li>
  <li id="ref6">Pardridge WM. Blood-brain barrier delivery. <em>Drug Discovery Today</em>. 2007;12(1-2):54–61. <a href="https://doi.org/10.1016/j.drudis.2006.10.013">doi:10.1016/j.drudis.2006.10.013</a></li>
  <li id="ref7">Niewoehner J, Bohrmann B, Collin L, et al. Increased brain penetration and potency of a therapeutic antibody using a monovalent molecular shuttle. <em>Neuron</em>. 2014;81(1):49–60. <a href="https://doi.org/10.1016/j.neuron.2013.10.061">doi:10.1016/j.neuron.2013.10.061</a></li>
  <li id="ref8">Kumthekar P, Tang SC, Brenner AJ, et al. ANG1005, a brain-penetrating peptide-drug conjugate, shows activity in patients with breast cancer with leptomeningeal carcinomatosis and recurrent brain metastases. <em>Clinical Cancer Research</em>. 2020;26(12):2789–2799. <a href="https://doi.org/10.1158/1078-0432.CCR-19-3258">doi:10.1158/1078-0432.CCR-19-3258</a></li>
  <li id="ref9">Olson ES, Aguilera TA, Jiang T, et al. In vivo characterization of activatable cell penetrating peptides for targeting protease activity in cancer. <em>Integrative Biology</em>. 2009;1(5-6):382–393. <a href="https://doi.org/10.1039/b904890a">doi:10.1039/b904890a</a></li>
  <li id="ref10">Reshetnyak YK, Andreev OA, Lehnert U, Engelman DM. Translocation of molecules into cells by pH-dependent insertion of a transmembrane helix. <em>Proceedings of the National Academy of Sciences</em>. 2006;103(17):6460–6465. <a href="https://doi.org/10.1073/pnas.0601463103">doi:10.1073/pnas.0601463103</a></li>
  <li id="ref11">Lochhead JJ, Thorne RG. Intranasal delivery of biologics to the central nervous system. <em>Advanced Drug Delivery Reviews</em>. 2012;64(7):614–628. <a href="https://doi.org/10.1016/j.addr.2011.11.002">doi:10.1016/j.addr.2011.11.002</a></li>
  <li id="ref12">Schiffelers RM, Koning GA, ten Hagen TL, et al. Anti-tumor efficacy of tumor vasculature-targeted liposomal doxorubicin. <em>Journal of Controlled Release</em>. 2003;91(1-2):115–122. <a href="https://doi.org/10.1016/S0168-3659(03)00240-2">doi:10.1016/S0168-3659(03)00240-2</a></li>
  <li id="ref13">Corti A, Curnis F. Tumor vasculature targeting through NGR peptide-based drug delivery systems. <em>Current Pharmaceutical Biotechnology</em>. 2011;12(8):1128–1134. <a href="https://doi.org/10.2174/138920111796117373">doi:10.2174/138920111796117373</a></li>
  <li id="ref14">Duchardt F, Fotin-Mleczek M, Schwarz H, Fischer R, Brock R. A comprehensive model for the cellular uptake of cationic cell-penetrating peptides. <em>Traffic</em>. 2007;8(7):848–866. <a href="https://doi.org/10.1111/j.1600-0854.2007.00572.x">doi:10.1111/j.1600-0854.2007.00572.x</a></li>
  <li id="ref15">Danhier F, Le Breton A, Préat V. RGD-based strategies to target alpha(v) beta(3) integrin in cancer therapy and diagnosis. <em>Molecular Pharmaceutics</em>. 2012;9(11):2961–2973. <a href="https://doi.org/10.1021/mp3002733">doi:10.1021/mp3002733</a></li>
</ol>

*— Written by the [RPL Scientific Editorial Team](https://research.rplpeptides.com/authors/) | Last updated August 2026*

**Related Articles:** [Nanoparticle-Based Peptide Delivery](https://research.rplpeptides.com/drug-delivery/nanoparticle-peptide-delivery/) | [Injectable Depot Formulations](https://research.rplpeptides.com/drug-delivery/injectable-depot-formulations/) | [Peptide Pharmacodynamics](https://research.rplpeptides.com/pharmacology/peptide-pharmacodynamics/) | [RPL Peptides](https://rplpeptides.com) | [Peptide Research Data](https://data.rplpeptides.com)
