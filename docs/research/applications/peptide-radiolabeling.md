---
title: Peptide Radiolabeling
description: "A comprehensive scientific overview of peptide radiolabeling strategies for PET and SPECT imaging, including ¹⁸F, ⁶⁸Ga, ⁹⁹ᵐTc, and ¹⁷⁷Lu labeling, chelator chemistry, and theranostic applications."
schema_type: TechArticle
slug: peptide-radiolabeling
---

# Peptide Radiolabeling


## Executive Summary

Peptide radiolabeling is the chemical strategy of attaching radioactive isotopes to peptide vectors for molecular imaging and targeted radionuclide therapy. Peptides offer ideal properties as imaging vectors: rapid target binding, fast clearance from non-target tissues, favorable pharmacokinetics, and modular chemistry for radionuclide attachment.

The field encompasses two major application domains: (1) diagnostic imaging using positron emission tomography (PET) or single-photon emission computed tomography (SPECT) with radionuclides including ¹⁸F (t½ = 109.7 min), ⁶⁸Ga (t½ = 67.7 min), and ⁹⁹ᵐTc (t½ = 6.01 h), and (2) targeted radionuclide therapy using β⁻-emitters such as ¹⁷⁷Lu (t½ = 6.65 d) and ⁹⁰Y (t½ = 2.67 d). The combination of matched diagnostic and therapeutic radionuclide pairs — the "theranostic" approach — enables patient selection, dosimetry, and therapy monitoring using the same peptide vector.

The development of bifunctional chelators (BFCs) that stably coordinate radiometals while conjugating to the peptide has been central to the field. Key chelator systems include DOTA (1,4,7,10-tetraazacyclododecane-1,4,7,10-tetraacetic acid), NOTA (1,4,7-triazacyclononane-1,4,7-triacetic acid), and HYNIC (hydrazinonicotinamide). Clinically approved radiolabeled peptide drugs include ⁶⁸Ga-DOTATATE and ¹⁷⁷Lu-DOTATATE for neuroendocrine tumors, which have transformed the management of somatostatin receptor-positive malignancies.


## Background

The concept of using radiolabeled peptides for medical imaging emerged from two converging lines of research. First, the discovery and characterization of peptide hormone receptors — particularly somatostatin receptors (SSTRs) — that are overexpressed on tumor cells provided a molecular target. Second, advances in peptide synthesis and chelation chemistry made it feasible to attach imaging radionuclides while preserving receptor binding affinity.

The pioneering work of Krenning and Lamberts in the late 1980s demonstrated that ¹²³I-labeled somatostatin analogs could visualize neuroendocrine tumors by scintigraphy. This proof-of-concept led to the development of ¹¹¹In-DTPA-octreotide (OctreoScan), which became the gold standard for SSTR imaging for two decades.

The replacement of ¹¹¹In (γ-emitter, SPECT) with ⁶⁸Ga (β⁺-emitter, PET) represented a major advance. Maecke and colleagues developed ⁶⁸Ga-DOTATOC in the early 2000s, exploiting the convenient generator-based production of ⁶⁸Ga from a ⁶⁸Ge/⁶⁸Ga generator. PET imaging with ⁶⁸Ga-labeled peptides offered superior spatial resolution (2–3 mm vs. 8–10 mm for SPECT) and quantification capability.

The theranostic paradigm was solidified by the introduction of ¹⁷⁷Lu-DOTATATE. The same peptide-chelator conjugate used for diagnostic imaging with ⁶⁸Ga could be labeled with ¹⁷⁷Lu for peptide receptor radionuclide therapy (PRRT). The landmark NETTER-1 trial (2017) demonstrated that ¹⁷⁷Lu-DOTATATE significantly improved progression-free survival in patients with midgut neuroendocrine tumors, leading to regulatory approval.

Today, radiolabeled peptide development has expanded far beyond somatostatin analogs to include ligands targeting integrins (RGD peptides for αvβ3), gastrin-releasing peptide receptor (GRPR) for prostate cancer, cholecystokinin-2 receptor (CCK2R), GLP-1 receptor for insulinoma imaging, and many others.


## Scientific Explanation

### Radionuclide Selection

The choice of radionuclide depends on the intended application (imaging vs. therapy), the required radiation characteristics, and the pharmacokinetics of the peptide vector.

**Diagnostic Radionuclides for PET:**

- **¹⁸F**: Cyclotron-produced, t½ = 109.7 min. Ideal imaging properties (97% β⁺ branching, low positron energy of 633 keV, short range in tissue). Requires covalent attachment — typically via prosthetic groups such as N-succinimidyl-4-[¹⁸F]fluorobenzoate ([¹⁸F]SFB) or 4-[¹⁸F]fluorobenzaldehyde — limiting radiochemical yields.
- **⁶⁸Ga**: Generator-produced (⁶⁸Ge/⁶⁸Ga generator), t½ = 67.7 min. Convenient production without cyclotron. Chelator-based coordination chemistry facilitates kit-type labeling. Moderate positron energy (1.9 MeV) gives slightly lower resolution than ¹⁸F.
- **⁶⁴Cu**: Cyclotron-produced, t½ = 12.7 h. Allows imaging at later time points. Multiple oxidation states require careful chelator design.

**Diagnostic Radionuclides for SPECT:**

- **⁹⁹ᵐTc**: Generator-produced (⁹⁹Mo/⁹⁹ᵐTc generator), t½ = 6.01 h. Ideal for clinical logistics. Versatile coordination chemistry with multiple oxidation states. The 140 keV γ-ray is optimal for gamma camera imaging.
- **¹¹¹In**: Cyclotron-produced, t½ = 2.81 d. Slower clearance from background. Historically important for OctreoScan.
- **¹²³I**: Cyclotron-produced, t½ = 13.2 h. Direct labeling via electrophilic iodination.

**Therapeutic Radionuclides:**

- **¹⁷⁷Lu**: Reactor-produced, t½ = 6.65 d. β⁻ emission (Eβ₋ₐᵥ = 134 keV, range ~0.2 mm) suitable for small tumors. Also emits γ‑rays (113 keV, 208 keV) enabling post-therapy imaging and dosimetry.
- **⁹⁰Y**: Reactor-produced, t½ = 2.67 d. Higher β⁻ energy (Eβ₋ₐᵥ = 933 keV, range ~2.5 mm) more suitable for larger tumors. No γ‑emission for imaging; a surrogate diagnostic pair (e.g., ⁸⁶Y or ¹¹¹In) is needed.
- **²¹³Bi** and **²¹¹At**: α‑emitters with high linear energy transfer (LET, ~100 keV/μm) and short range (<100 μm), promising for disseminated or single-cell disease. Despite higher potency, α‑emitters present production and handling challenges.

### Chelator Chemistry

For radiometals, stable coordination within a bifunctional chelator (BFC) is essential to prevent transchelation and release of free metal, which could accumulate in bone marrow or other non-target tissues.

**DOTA (1,4,7,10-tetraazacyclododecane-1,4,7,10-tetraacetic acid)**: The most widely used macrocyclic chelator. Forms stable complexes with ⁶⁸Ga, ¹⁷⁷Lu, ⁹⁰Y, ⁶⁴Cu, and ¹¹¹In. DOTA conjugation typically requires coupling to the peptide's N‑terminus or lysine side chain. Labeling requires elevated temperatures (80–95 °C) and acidic pH (3.5–5.5), which may limit use with heat-sensitive peptides.

**NOTA (1,4,7-triazacyclononane-1,4,7-triacetic acid)**: Smaller macrocycle that forms more kinetically inert complexes with ⁶⁸Ga and ⁶⁴Cu. Allows room-temperature labeling with ⁶⁸Ga, simplifying kit-formulation. NODAGA (NOTA with a glutaric acid side chain) is a popular derivative.

**TETA (1,4,8,11-tetraazacyclotetradecane-1,4,8,11-tetraacetic acid)**: Optimized for ⁶⁴Cu, though DOTA and NOTA derivatives also perform well.

**HYNIC (hydrazinonicotinamide)**: Used for ⁹⁹ᵐTc labeling. Requires co-ligands (e.g., tricine, EDDA, nicotinic acid) to complete the coordination sphere. Produces mixtures of isomers, complicating quality control.

**HEDP and Other Phosphonates**: For labeling with ⁹⁹ᵐTc or ¹⁸⁸Re for bone-targeting agents.

### Labeling Strategies

**Direct Labeling**: For radiohalogens (¹⁸F, ¹²³I, ¹²⁴I). ¹⁸F is typically introduced via prosthetic groups — pre-labeled building blocks conjugated to the peptide after a second coupling step — because direct fluorination conditions are too harsh for peptides.

**Chelator-Based Labeling (Radiometals)**: The peptide-chelator conjugate is synthesized first (fully characterized and purified), then incubated with the radiometal under optimized pH, temperature, and buffer conditions. After labeling, the product is purified (typically by C18 solid-phase extraction) and formulated for injection.

**Kit Formulations**: Pre-manufactured vials containing the peptide-chelator conjugate (e.g., ⁶⁸Ga-DOTATATE kit) allow simple one-step radiolabeling with generator eluate. This kit approach has been crucial for the clinical adoption of ⁶⁸Ga-based imaging.

### Pharmacological Considerations

The introduction of a chelator and radionuclide to a peptide can significantly alter its pharmacokinetics. Key factors include:

- **Hydrophilicity**: Chelators increase overall hydrophilicity, shifting clearance from hepatobiliary to renal.
- **Charge**: The net charge of the metal-chelate complex affects tissue retention and renal reabsorption.
- **Size**: The combined peptide-chelator-radiometal mass affects filtration and tissue penetration.
- **Stability**: Radiometal dissociation in vivo leads to free metal accumulation in bone and liver.
- **Receptor binding**: Chelator conjugation can reduce receptor affinity; careful optimization (spacer length, conjugation site) is required.


## Research Evidence

<table>
<thead>
  <tr>
    <th>Radiotracer</th>
    <th>Target</th>
    <th>Application</th>
    <th>Clinical Status</th>
    <th>Key Finding</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>⁶⁸Ga-DOTATATE</td>
    <td>SSTR2</td>
    <td>Neuroendocrine tumor PET</td>
    <td>FDA approved (2016)</td>
    <td>96% sensitivity, 86% specificity for NET detection</td>
  </tr>
  <tr>
    <td>¹⁷⁷Lu-DOTATATE</td>
    <td>SSTR2</td>
    <td>PRRT therapy</td>
    <td>FDA approved (2018)</td>
    <td>79% reduction in PD risk vs. high-dose octreotide (NETTER-1)</td>
  </tr>
  <tr>
    <td>⁶⁸Ga-PSMA-11</td>
    <td>PSMA</td>
    <td>Prostate cancer PET</td>
    <td>FDA approved (2020)</td>
    <td>92% sensitivity for prostate cancer lymph node metastases</td>
  </tr>
  <tr>
    <td>⁶⁸Ga-NODAGA-RGD</td>
    <td>αvβ3 integrin</td>
    <td>Angiogenesis imaging</td>
    <td>Phase II</td>
    <td>Correlated with microvessel density in glioblastoma</td>
  </tr>
  <tr>
    <td>¹⁸F-FPPRGD2</td>
    <td>αvβ3 integrin</td>
    <td>PET angiogenesis imaging</td>
    <td>Phase I/II</td>
    <td>SUV correlated with VEGF expression in breast cancer</td>
  </tr>
  <tr>
    <td>⁹⁹ᵐTc-HYNIC-TOC</td>
    <td>SSTR2</td>
    <td>SPECT NET imaging</td>
    <td>Clinical use (EU)</td>
    <td>Comparable sensitivity to ¹¹¹In-OctreoScan</td>
  </tr>
  <tr>
    <td>⁶⁸Ga-Exendin-4</td>
    <td>GLP-1R</td>
    <td>Insulinoma PET</td>
    <td>Phase II</td>
    <td>95% sensitivity for benign insulinoma detection</td>
  </tr>
  <tr>
    <td>¹⁷⁷Lu-PSMA-617</td>
    <td>PSMA</td>
    <td>Prostate cancer therapy</td>
    <td>FDA approved (2022)</td>
    <td>38% reduction in death vs. standard care (VISION trial)</td>
  </tr>
</tbody>
</table>

Key quantitative findings from the literature include:

- ⁶⁸Ga-DOTATATE PET/CT identified additional tumor lesions in 38% of neuroendocrine tumor patients compared to conventional imaging <em>Journal of Nuclear Medicine</em>, 55(10), 1598–1604.
- The theranostic pairing of ⁶⁸Ga-DOTATATE (diagnostic) and ¹⁷⁷Lu-DOTATATE (therapy) achieved a 29.8% objective response rate in NET patients, with median PFS of 28.4 months <em>Journal of Clinical Oncology</em>, 35(18), 2004–2012.
- ¹⁷⁷Lu-DOTATATE treatment improved quality of life in neuroendocrine tumor patients, with a median PFS of 8.4 months longer than the control group <em>New England Journal of Medicine</em>, 376(2), 125–135.
- DOTA labeling with ⁶⁸Ga achieves >98% radiochemical purity with specific activities exceeding 100 GBq/μmol under optimized conditions <em>Bioconjugate Chemistry</em>, 23(10), 2113–2122.
- NOTA-conjugated peptides can be labeled with ⁶⁸Ga at room temperature in 5–10 minutes with >95% radiochemical yield, compared to 30–45 minutes at 95 °C for DOTA <em>Journal of Nuclear Medicine</em>, 49(7), 1164–1170.


## Current Understanding

Peptide radiolabeling has matured from a specialized radiochemical technique to a clinically established modality. The field is now focused on extending the theranostic paradigm to new targets and optimizing the chemical, pharmacokinetic, and dosimetric properties of radiopeptide agents.

**Target Expansion**: Beyond SSTR2 and PSMA, radiopeptides are being developed for fibroblast activation protein (FAP), chemokine receptor CXCR4, neurotensin receptor (NTSR1), melanocortin-1 receptor (MC1R), and integrin αvβ6. FAP-targeting peptides are particularly exciting given the near-universal expression of FAP in the tumor stroma of epithelial cancers.

**Pretargeting Strategies**: To overcome the pharmacokinetic mismatch between rapid-targeting peptides (minutes to hours) and long-circulating antibodies, pretargeting approaches use bioorthogonal click chemistry (e.g., tetrazine-trans-cyclooctene). A non-radioactive antibody-bioorthogonal tag is administered first, allowing time for tumor accumulation and blood clearance, followed by a rapidly clearing radiolabeled peptide that "clicks" to the pre-targeted antibody at the tumor site.

**Alpha Therapy**: The transition from β⁻-emitters (¹⁷⁷Lu, ⁹⁰Y) to α-emitters (²¹³Bi, ²¹¹At, ²²⁵Ac) is a major frontier. α‑particles deposit substantially more energy per unit track length (LET ~100 keV/μm vs. 0.2 keV/μm for β⁻), causing complex, difficult-to-repair DNA double-strand breaks. Clinical trials with ²²⁵Ac-PSMA-617 have shown promise in patients who failed ¹⁷⁷Lu-PSMA therapy.

**Regulatory and Manufacturing Advances**: Kit-based ⁶⁸Ga labeling and automated synthesis modules for ¹⁸F-fluorination are making peptide radiolabeling more accessible. The adoption of good manufacturing practice (GMP) standards for radiopharmaceutical production ensures consistent quality for clinical use.

For researchers developing radiolabeled peptide probes, the [RPL Peptides Data Center](https://data.rplpeptides.com) provides analytical data for candidate peptide vectors. Additional tools for peptide characterization can be accessed at the [RPL Peptides Research Tools](https://tool.rplpeptides.com) platform.


## Frequently Asked Questions

<div class="faq-container">
  <div class="faq-item">
<h3 class="faq-question">What is the difference between PET and SPECT radionuclides?</h3>
<p>PET (positron emission tomography) radionuclides emit positrons (β⁺) that annihilate with electrons, producing two 511 keV γ‑rays emitted 180° apart. PET provides higher spatial resolution (2–3 mm), better sensitivity, and quantitative imaging capability. SPECT (single-photon emission computed tomography) radionuclides emit single γ‑rays at various energies, requiring collimation and resulting in lower resolution (8–10 mm). Common PET radionuclides for peptides include ⁶⁸Ga and ¹⁸F; common SPECT radionuclides include ⁹⁹ᵐTc and ¹¹¹In.</p>
</div>
  <div class="faq-item">
<h3 class="faq-question">What is a bifunctional chelator (BFC)?</h3>
<p>A bifunctional chelator (BFC) is a molecule that contains both a metal-chelating domain — typically a macrocycle (DOTA, NOTA) or acyclic chelator (DTPA, HYNIC) — and a functional group for conjugation to the peptide (e.g., a carboxylic acid or NHS-ester activated for amide bond formation). The BFC serves as a molecular bridge, stably coordinating the radiometal while remaining covalently attached to the targeting peptide, preventing dissociation of the radioactive metal in vivo.</p>
</div>
  <div class="faq-item">
<h3 class="faq-question">Why is ⁶⁸Ga so popular for peptide PET imaging?</h3>
<p>⁶⁸Ga is popular for several reasons: (1) it is produced from a ⁶⁸Ge/⁶⁸Ga generator, avoiding the need for an on-site cyclotron; (2) it has a convenient half-life (67.7 min) matching peptide pharmacokinetics; (3) it coordinates stably with DOTA- and NOTA-based chelators; (4) kit-based labeling formulations enable simple, rapid preparation; and (5) PET imaging with ⁶⁸Ga provides high spatial resolution and quantification capability suitable for lesion detection and therapy response monitoring.</p>
</div>
  <div class="faq-item">
<h3 class="faq-question">What is the theranostic approach in peptide radiolabeling?</h3>
<p>Theranostics combines diagnostic imaging and therapy using the same or closely related targeting vectors labeled with matched radionuclides. For example, a somatostatin peptide analog is labeled with ⁶⁸Ga for PET imaging to identify patients with SSTR2-positive neuroendocrine tumors, and the same peptide is then labeled with ¹⁷⁷Lu for targeted radionuclide therapy. This "see and treat" approach enables patient selection (only those with sufficient target expression receive therapy), individualized dosimetry, and therapy monitoring using post-therapy imaging.</p>
</div>
  <div class="faq-item">
<h3 class="faq-question">What is the role of a chelator in preventing toxicity?</h3>
<p>The chelator is critical for preventing radiotoxicity. If the radiometal dissociates from the chelator (transchelation), the free metal ion can be taken up by non-target tissues — particularly the bone marrow for ⁹⁰Y and ¹⁷⁷Lu, or the kidneys — causing radiation damage. A stable chelator complex prevents this by sequestering the radiometal with high thermodynamic stability and kinetic inertness. Macrocyclic chelators like DOTA form more inert complexes than acyclic chelators, which is why they are preferred for therapeutic radiometals.</p>
</div>
  <div class="faq-item">
<h3 class="faq-question">How does ¹⁷⁷Lu differ from ⁹⁰Y for peptide receptor radionuclide therapy?</h3>
<p>¹⁷⁷Lu and ⁹⁰Y are both β⁻-emitters for therapy but differ in several key aspects. ¹⁷⁷Lu has a longer half-life (6.65 d vs. 2.67 d), lower β⁻ energy (Eβ₋ₐᵥ = 134 keV vs. 933 keV), and shorter tissue range (~0.2 mm vs. ~2.5 mm). ¹⁷⁷Lu also emits γ‑rays that allow post-therapy imaging. The shorter range of ¹⁷⁷Lu is better suited for small tumors (<1 cm), while ⁹⁰Y is more effective for larger tumors. ¹⁷⁷Lu-DOTA complexes are more stable than ⁹⁰Y-DOTA, giving ¹⁷⁷Lu a lower bone marrow toxicity profile.</p>
</div>
  <div class="faq-item">
<h3 class="faq-question">What is PSMA and what radiopeptides target it?</h3>
<p>Prostate-specific membrane antigen (PSMA) is a transmembrane protein highly overexpressed on prostate cancer cells (100–1,000 fold higher than on normal prostate tissue). PSMA-targeting radiopeptides such as ⁶⁸Ga-PSMA-11, ¹⁸F-DCFPyL, and ¹⁷⁷Lu-PSMA-617 are glutamate-urea-lysine based inhibitors of PSMA's enzymatic activity. These tracers have become the standard of care for prostate cancer imaging (⁶⁸Ga-PSMA-11, FDA approved 2020) and are increasingly used for therapy (¹⁷⁷Lu-PSMA-617, FDA approved 2022 based on the VISION trial).</p>
</div>
  <div class="faq-item">
<h3 class="faq-question">What are the challenges of using ¹⁸F for peptide labeling?</h3>
<p>¹⁸F labeling of peptides is challenging because (1) ¹⁸F requires covalent bond formation, typically through nucleophilic substitution, which requires harsh conditions (high temperature, organic solvents) incompatible with many peptides; (2) the short half-life (109.7 min) limits time for multi-step synthesis; (3) prosthetic groups (e.g., [¹⁸F]SFB, [¹⁸F]FBEM) must be synthesized first, then conjugated to the peptide — a multi-step process that reduces overall radiochemical yield (typically 5–30%); and (4) the final product requires HPLC purification, which is time-consuming for clinical production.</p>
</div>
  <div class="faq-item">
<h3 class="faq-question">What are the approved radiolabeled peptide drugs?</h3>
<p>FDA-approved radiolabeled peptide drugs include: (1) ⁶⁸Ga-DOTATATE (Netspot™, 2016) for SSTR PET imaging of neuroendocrine tumors; (2) ¹⁷⁷Lu-DOTATATE (Lutathera®, 2018) for PRRT of SSTR-positive gastroenteropancreatic neuroendocrine tumors; (3) ⁶⁸Ga-PSMA-11 (Illuccix®, 2021) for PSMA PET imaging in prostate cancer; (4) ¹⁸F-DCFPyL (Pylarify®, 2021) for PSMA PET imaging; and (5) ¹⁷⁷Lu-PSMA-617 (Pluvicto®, 2022) for PSMA-positive metastatic castration-resistant prostate cancer.</p>
</div>
  <div class="faq-item">
<h3 class="faq-question">What is alpha therapy in the context of peptide radiolabeling?</h3>
<p>Alpha therapy uses peptide vectors labeled with α-emitting radionuclides such as ²¹³Bi, ²¹¹At, or ²²⁵Ac. α‑particles have high linear energy transfer (LET, ~100 keV/μm) and short tissue range (<100 μm, or 2–3 cell diameters). This combination delivers a highly concentrated radiation dose to target cells while sparing surrounding healthy tissue. α‑emitters are particularly effective for disseminated or micro-metastatic disease where single cancer cells are the target. Clinical evidence suggests ²²⁵Ac-PSMA can be effective in patients who have progressed after ¹⁷⁷Lu-PSMA therapy.</p>
</div>
</div>


## References

<ol class="references">
  <li id="ref1">Maecke, H. R., & Reubi, J. C. (2011). Somatostatin receptors as targets for nuclear medicine imaging and radionuclide treatment. <em>Journal of Nuclear Medicine</em>, 52(6), 841–844. <a href="https://doi.org/10.2967/jnumed.110.084236">doi:10.2967/jnumed.110.084236</a></li>
  <li id="ref2">Strosberg, J., El-Haddad, G., Wolin, E., Hendifar, A., Yao, J., Chasen, B., Mittra, E., Kunz, P. L., Kulke, M. H., Jacene, H., Bushnell, D., O'Dorisio, T. M., Baum, R. P., Kulkarni, H. R., Caplin, M., Lebtahi, R., Hobday, T., Delpassand, E., Van Cutsem, E., … Krenning, E. (2017). Phase 3 trial of ¹⁷⁷Lu-DOTATATE for midgut neuroendocrine tumors. <em>New England Journal of Medicine</em>, 376(2), 125–135. <a href="https://doi.org/10.1056/NEJMoa1607427">doi:10.1056/NEJMoa1607427</a></li>
  <li id="ref3">Hofman, M. S., Lawrentschuk, N., Francis, R. J., Tang, C., Vela, I., Thomas, P., Rutherford, N., Martin, J. M., Frydenberg, M., Shakher, R., Wong, L. M., Taubman, K., Ting Lee, S., Hsiao, E., Roach, P., Nottage, M., Kirkwood, I., Chiam, K., & Murphy, D. G. (2020). Prostate-specific membrane antigen PET-CT in patients with high-risk prostate cancer before curative-intent surgery or radiotherapy (proPSMA): a prospective, randomised, multicentre study. <em>The Lancet</em>, 395(10231), 1208–1216. <a href="https://doi.org/10.1016/S0140-6736%2820%2930314-7">doi:10.1016/S0140-6736(20)30314-7</a></li>
  <li id="ref4">Sartor, O., de Bono, J., Chi, K. N., Fizazi, K., Herrmann, K., Rahbar, K., Tagawa, S. T., Nordquist, L. T., Vaishampayan, N., El-Haddad, G., Park, C. H., Beer, T. M., Armour, A., Pérez-Contreras, W. J., DeSilvio, M., Kpamegan, E., Gericke, G., Messmann, R. A., Morris, M. J., & Krause, B. J. (2021). Lutetium-177-PSMA-617 for metastatic castration-resistant prostate cancer. <em>New England Journal of Medicine</em>, 385(12), 1091–1103. <a href="https://doi.org/10.1056/NEJMoa2107322">doi:10.1056/NEJMoa2107322</a></li>
  <li id="ref5">Price, E. W., & Orvig, C. (2014). Matching chelators to radiometals for radiopharmaceuticals. <em>Chemical Society Reviews</em>, 43(1), 260–290. <a href="https://doi.org/10.1039/C3CS60304K">doi:10.1039/C3CS60304K</a></li>
  <li id="ref6">Tolmachev, V., & Orlova, A. (2020). Affibody molecules as targeting agents for imaging and therapy. <em>Cancers</em>, 12(12), 3758. <a href="https://doi.org/10.3390/cancers12123758">doi:10.3390/cancers12123758</a></li>
  <li id="ref7">Rosenkranz, A. A., Slastnikova, T. A., Savchenko, E. A., & Sobolev, A. S. (2018). Peptide-based strategies for molecular imaging and therapy of cancer. <em>International Journal of Molecular Sciences</em>, 19(7), 1984. <a href="https://doi.org/10.3390/ijms19071984">doi:10.3390/ijms19071984</a></li>
  <li id="ref8">Müller, C., & Schibli, R. (2011). Prospects in the development of radiolabeled peptides for cancer imaging and therapy. <em>Journal of Labelled Compounds and Radiopharmaceuticals</em>, 54(7), 377–385. <a href="https://doi.org/10.1002/jlcr.1879">doi:10.1002/jlcr.1879</a></li>
  <li id="ref9">Graham, M. M., & Menda, Y. (2019). Peptide-based radiopharmaceuticals for cancer diagnosis and therapy. <em>Seminars in Nuclear Medicine</em>, 49(2), 125–136. <a href="https://doi.org/10.1053/j.semnuclmed.2018.11.006">doi:10.1053/j.semnuclmed.2018.11.006</a></li>
  <li id="ref10">Kratochwil, C., Bruchertseifer, F., Giesel, F. L., Weis, M., Verburg, F. A., Mottaghy, F., Kopka, K., Apostolidis, C., Haberkorn, U., & Morgenstern, A. (2016). ²²⁵Ac-PSMA-617 for PSMA-targeted α-radiation therapy of metastatic castration-resistant prostate cancer. <em>Journal of Nuclear Medicine</em>, 57(12), 1941–1944. <a href="https://doi.org/10.2967/jnumed.116.178673">doi:10.2967/jnumed.116.178673</a></li>
  <li id="ref11">Fani, M., & Maecke, H. R. (2012). Multifunctional peptide-based radiopharmaceuticals for imaging and therapy. <em>European Journal of Nuclear Medicine and Molecular Imaging</em>, 39(Suppl 1), S11–S30. <a href="https://doi.org/10.1007/s00259-011-1997-2">doi:10.1007/s00259-011-1997-2</a></li>
  <li id="ref12">Ambrosini, V., Fani, M., Fanti, S., Forrer, F., & Maecke, H. R. (2011). Radiopeptide imaging and therapy in Europe. <em>Journal of Nuclear Medicine</em>, 52(Suppl 2), 42S–55S. <a href="https://doi.org/10.2967/jnumed.110.085753">doi:10.2967/jnumed.110.085753</a></li>
  <li id="ref13">Velikyan, I. (2015). Prospective of ⁶⁸Ga-radiopharmaceutical development. <em>Theranostics</em>, 4(1), 47–80. <a href="https://doi.org/10.7150/thno.7447">doi:10.7150/thno.7447</a></li>
  <li id="ref14">Bode, S., Löser, R., & Pietzsch, J. (2020). Recent advances in peptide-based PET imaging. <em>Molecules</em>, 25(22), 5320. <a href="https://doi.org/10.3390/molecules25225320">doi:10.3390/molecules25225320</a></li>
</ol>
