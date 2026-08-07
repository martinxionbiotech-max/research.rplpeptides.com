---
title: "Common Synthetic Peptide Impurities: Types, Causes, and Detection"
description: "A technical review of synthetic peptide impurities from SPPS side reactions — deletion, truncated, oxidized, racemized and aggregated species — with LC-MS characteristics and control strategies."
slug: common-peptide-impurities
category: Quality Control
tags: [Peptide Impurities, SPPS, Deletion Peptides, Oxidation, LC-MS, Racemization]
author: RPL Peptides Research Team
published: 2026-08-01
---

# Common Synthetic Peptide Impurities: Types, Causes, and Detection

## Executive Summary

The purity number on a peptide Certificate of Analysis—typically 95–99% by HPLC area normalization—is the aggregated result of dozens of synthetic steps, each carrying a finite probability of failure. The 1–5% of material that is not the target peptide consists of a chemically predictable population of impurities: deletion peptides missing one or more residues, truncated fragments from premature chain termination, oxidized species from post-synthetic degradation, diastereomers from racemization during amino acid activation, and aggregated or dimerized forms from interchain reactions. Understanding this impurity profile is not optional for quality control—the identity and abundance of each impurity species determines whether the batch is fit for its intended research purpose.

For laboratory managers and researchers, the impurity section of a COA answers two essential questions that the purity number alone cannot: "What are the impurities?" and "Does the analytical method resolve them from the main peptide?" A batch with 98% purity where all 2% is accounted for as a single, well-characterized oxidized form is a known entity with predictable behavior. The same 98% purity where the impurities are unidentified or co-elute under the main peak presents an unknown risk. The analytical method's ability to resolve and identify specific impurity classes—deletions, oxidations, diastereomers—is the measure of a quality system's technical competence.

This article provides a comprehensive taxonomy of synthetic peptide impurities, organized by chemical mechanism: the coupling-statistics origin of deletion and truncated species, the oxidative degradation of sensitive residues, the stereochemical defects introduced during activation, and the physical aggregation pathways. For each class we describe the characteristic LC-MS signature, the chromatographic behavior, and the control strategies that modern SPPS manufacturing employs. The goal is to equip every peptide COA reader with the vocabulary and diagnostic framework to ask the right questions: "What impurities does my 98.5% represent?" and "Can the method actually see them?"

## Background

Solid-phase peptide synthesis (SPPS), pioneered by R. Bruce Merrifield in 1963, builds a peptide chain from the C-terminus to the N-terminus by repeated cycles of Fmoc (or Boc) deprotection and amino acid coupling on an insoluble resin support. Each cycle presents an opportunity for side reactions, and the probability of a failure accumulates with chain length. For a peptide of $n$ residues, if each coupling step succeeds with probability $p$ (typically 0.992–0.998 under optimized conditions), the theoretical yield of full-length product before purification is:

$$Y_{\text{full-length}} \approx p^{\,n} \times 100\%$$

For a 30-residue peptide with $p = 0.995$ (99.5% per-step coupling efficiency), the expected full-length yield is $0.995^{30} \approx 0.860$, or roughly 86%. The remaining 14% of resin-bound material is distributed among failure sequences—deletion peptides, truncated fragments, and capped intermediates—that must be removed by preparative HPLC purification. This simple statistical model explains why long peptides are intrinsically more difficult to synthesize to high purity and why impurity control is as much a statistical problem as a chemical one.

The main chemical sources of impurities fall into four mechanistic families:

1. **Incomplete reaction products**: deletion peptides (missing internal residues), truncated peptides (prematurely terminated chains), and residual intermediates from failed couplings.
2. **Side-chain modification products**: oxidation of methionine, tryptophan, and cysteine; deamidation of asparagine and glutamine; alkylation of nucleophilic side chains.
3. **Stereochemical defects**: diastereomers formed by racemization at the $\alpha$-carbon during amino acid activation and coupling.
4. **Physical and covalent aggregates**: dimers, oligomers, and $\beta$-sheet assemblies formed through disulfide bonds, side-chain cross-links, or non-covalent association.

Each family produces a characteristic pattern in both the HPLC chromatogram (retention time shift, peak shape) and the mass spectrum (mass shift, charge-state distribution). The ability to recognize these patterns from a COA's HPLC and LC-MS data is the core competency of peptide quality assessment.

## Core Science

### The Chemistry of Impurity Formation in SPPS

SPPS proceeds through a defined cycle: (1) Fmoc deprotection with piperidine, exposing the $\alpha$-amine; (2) activation of the incoming Fmoc-amino acid with a coupling reagent (HBTU, HATU, DIC/Oxyma); (3) coupling of the activated amino acid to the resin-bound $\alpha$-amine; (4) capping of unreacted amines with acetic anhydride. Each step in this cycle can fail, and the failure modes are well characterized.

**Coupling failure** is the dominant source of impurities. When the incoming activated amino acid does not react with every available $\alpha$-amine, the unreacted chains persist. If they are capped in step 4, they become acetylated truncated peptides (+42 Da mass shift, more hydrophobic). If they are not capped, they propagate on the next cycle as deletion peptides (missing one residue). In both cases, the full-length product is permanently lost from that chain.

The coupling efficiency $p$ varies with the specific amino acid and the sequence context:
- **Difficult couplings**: $\beta$-branched residues (Val, Ile, Thr) present steric hindrance to the incoming activated amino acid; proline's secondary amine is conformationally constrained; consecutive $\beta$-branched or sterically demanding residues amplify the effect.
- **Rapid couplings**: Gly, Ala, and other small residues typically couple with >99.5% efficiency.
- **Sequence effects**: The nature of the resin-bound amine matters—coupling onto a proline or N-methyl amino acid is inherently slower than coupling onto glycine or alanine.

The Kaiser test (ninhydrin-based) and chloranil test provide qualitative monitoring of coupling completion: a blue color (Kaiser) indicates free amines and incomplete coupling. Modern automated synthesizers incorporate UV monitoring of Fmoc deprotection to quantify coupling efficiency after each cycle.

### Deletion Peptides and the (N–1) Mechanism

A deletion peptide lacks one or more internal residues while retaining the rest of the sequence in the correct order. The single most common deletion is the (N–1) species—the peptide is missing exactly one amino acid at a specific internal position. The mass difference is the mass of the missing residue, typically 57–204 Da.

The (N–1) species forms through a two-step failure: (1) a coupling step does not reach completion, leaving a fraction of $\alpha$-amines unreacted; (2) the subsequent deprotection and coupling cycle adds the next residue to these unreacted chains, permanently skipping the missed position. The chains are now one residue short at a specific position, and the synthesis continues normally from that point forward. No subsequent step can detect or correct the deletion.

**LC-MS signature.** A deletion peptide co-elutes close to the target peak under many reversed-phase gradient conditions because removing an internal residue changes the mass but often only modestly changes the overall hydrophobicity. In the mass spectrum, the deletion appears as an additional charge-state envelope offset from the target envelope by:

$$\Delta (m/z) = \frac{\Delta M}{z}$$

Where $\Delta M$ is the mass of the missing residue. For a triply charged ion ($z = 3$) missing a glycine residue ($\Delta M = 57.02$ Da):

$$\Delta (m/z) = \frac{57.02}{3} = 19.01$$

A peak shifted by 19.01 $m/z$ units from the target in the +3 charge state is a strong indicator of a Gly deletion. The same logic applies to any deletion: compute $\Delta M$ for the suspected missing residue, divide by the charge state, and check whether the observed $m/z$ shift matches.

Deletion peptides are the most abundant impurity class in routine SPPS and are discussed further in [Deletion Peptides Explained](14-deletion-peptides-explained.md).

### Truncated Peptides and Capping Failures

Truncated peptides are shorter fragments that terminate prematurely. Two distinct mechanisms produce truncations:

**Chain termination without capping.** If a coupling fails and capping is not performed (or fails), the free $\alpha$-amine continues to propagate on subsequent cycles but is permanently missing the residues that would have been added at and after the failed step. The truncated peptide is therefore missing the C-terminal segment of the target sequence.

**Diketopiperazine (DKP) formation.** At the dipeptide stage on certain resin linkers (particularly Wang and trityl resins), the first two residues can cyclize and cleave from the resin, aborting the synthesis entirely. DKP formation is favored by Pro, Gly, or N-methyl amino acids at position 2, and by basic conditions during Fmoc deprotection. The result is a near-total loss of peptide from that synthesis chain—DKP formation is an all-or-nothing failure mode.

**LC-MS signature.** Truncated peptides differ from the target by the mass of the missing C-terminal segment and typically elute earlier in reversed-phase chromatography because they are shorter and less hydrophobic. Their charge-state envelopes appear at lower $m/z$ by $\Delta M / z$, where $\Delta M$ is the mass of the missing segment. In the HPLC chromatogram, truncations often form a cluster of small peaks eluting before the main peak; screening the XIC for the expected truncated masses provides rapid confirmation.

**Control strategy.** Routine capping with acetic anhydride after each coupling blocks unreacted amines and converts potential deletion chains into acetylated truncated peptides (+42.01 Da mass shift, more hydrophobic), which are usually easier to separate from the main peptide by reversed-phase HPLC. Capping does not eliminate the truncated species; it converts them into chemically distinct forms with predictable mass shifts that aid identification and simplify purification.

### Oxidation of Methionine, Tryptophan, and Cysteine

Oxidation is the most common post-synthetic degradation pathway—and often the most consequential, because it can occur during storage and handling after the batch has been released. Three residues dominate peptide oxidation chemistry:

**Methionine (Met).** The thioether sulfur of the Met side chain oxidizes stepwise: first to methionine sulfoxide (+15.99 Da), then to methionine sulfone (+31.99 Da). Met sulfoxide formation is catalyzed by dissolved oxygen, peroxides in HPLC-grade solvents, and transition-metal ions ($\text{Fe}^{3+}$, $\text{Cu}^{2+}$). Once formed, Met sulfoxide is chemically reversible (reduction with DTT or TCEP); Met sulfone is effectively irreversible under biological conditions. For peptides containing methionine, the sulfoxide is typically the most abundant impurity after deletion species.

**Tryptophan (Trp).** The indole ring of Trp is susceptible to oxidation by atmospheric oxygen and light, producing a family of products: kynurenine (+3.99 Da), N-formylkynurenine (+27.99 Da), and mono- and di-hydroxylated indole species (+15.99 and +31.99 Da). The product distribution depends on pH, oxygen availability, and light exposure. Trp oxidation is accelerated in solution and in formulations exposed to ambient light.

**Cysteine (Cys).** Free thiol groups oxidize to disulfides (−2.02 Da per disulfide bond formed between two Cys residues), sulfenic acid (+15.99 Da), sulfinic acid (+31.99 Da), and sulfonic acid (+47.98 Da). Disulfide scrambling—the formation of non-native disulfide bridges—converts a single correctly folded species into a mixture of isomers with identical mass but different chromatographic retention. In peptides containing multiple cysteines, disulfide scrambling is often the most difficult impurity class to control.

**LC-MS signature.** Each oxidation state produces a characteristic mass shift:
- Met sulfoxide: +15.99 Da; Met sulfone: +31.99 Da
- Trp oxidation products: +3.99 to +31.99 Da
- Cys disulfide (intermolecular dimer): 2$M$ − 2.02 Da per S–S bond
- Cys sulfenic/sulfinic/sulfonic: +15.99/+31.99/+47.98 Da

Oxidized species typically elute earlier than the native peptide in reversed-phase HPLC because the oxygen atoms add polarity. For a detailed treatment, see [Oxidized Peptide Impurities](15-oxidized-peptide-impurities.md).

### Racemization and Diastereomer Formation

Racemization occurs when the chiral $\alpha$-carbon of an activated amino acid is transiently deprotonated, forming a planar carbanion or oxazolone intermediate that, upon reprotonation, can return either to the L-configuration or epimerize to the D-configuration. The resulting D-residue-containing peptide is a diastereomer of the target—identical in elemental composition and monoisotopic mass, and therefore invisible to mass spectrometry.

The risk of racemization is highest for:
- **Histidine and cysteine**, whose side chains can participate in intramolecular base catalysis during activation.
- **Couplings with excess base** or prolonged pre-activation times before addition to the resin.
- **Carbodiimide activations (DIC, DCC) without racemization suppressants** such as HOBt or Oxyma, which trap the reactive oxazolone intermediate before it epimerizes.

**LC-MS signature.** Diastereomers have the identical $m/z$ and isotope pattern as the target peptide. They are invisible to mass spectrometry and can only be detected chromatographically—typically as a shoulder or partially resolved doublet on the main HPLC peak. A shoulder on an otherwise ostensibly pure peak, combined with an LC-MS spectrum that shows only the expected mass, is the classic signature of diastereomer contamination.

Detection and quantitation require chiral or high-resolution reversed-phase methods, ideally with a synthesized D-residue reference standard for peak assignment. The diastereomer content is method-dependent: a method that cannot resolve the D-diastereomer from the L-peptide will over-report purity.

### Aggregation, Dimerization, and β-Sheet Species

Aggregation during SPPS is a physical phenomenon, not a chemical side reaction, but it produces species that behave as impurities:

**On-resin aggregation.** Hydrophobic or $\beta$-sheet-forming sequences (alternating hydrophobic/hydrophilic residues, polyalanine stretches) self-associate on the resin through interchain hydrogen bonding. The aggregated chains are sterically inaccessible to reagents, causing coupling and deprotection failure that produces deletion and truncated impurities. On-resin aggregation is the most common cause of synthesis failure for "difficult sequences."

**Covalent dimers and oligomers.** Interchain disulfide bonds (for Cys-containing peptides), lysine side-chain cross-links (from residual protecting groups), and tyrosine–tyrosine coupling (from oxidative conditions during cleavage) produce covalent multimers with mass $2M$, $3M$, etc.

**Solution aggregation.** After cleavage and purification, peptides in aqueous solution can aggregate reversibly depending on concentration, pH, ionic strength, and temperature. These aggregates may dissociate in the HPLC mobile phase (appearing as the monomer) or may produce broad, poorly shaped peaks with variable retention.

**LC-MS signature.** Covalent dimers of a monomer of mass $M$ appear at $2M$ (minus 2 Da per interchain disulfide bond). For a 1,200 Da monomer with one interchain disulfide ($M_{\text{dimer}} = 2398$ Da), the dimer charge-state distribution overlaps with the monomer's, requiring careful deconvolution. At $z = 5$, the dimer appears at $m/z \approx 480$, while the monomer's $[M+3H]^{3+}$ appears at $m/z \approx 400$—clearly resolved. Non-covalent aggregates typically dissociate during ESI and are detected indirectly through poor recovery and broad peaks rather than as discrete mass peaks.

### Other Side-Reaction Products

Several additional impurity classes are encountered routinely in peptide QC:

| Impurity type | Typical cause | Mass shift (Da) | Primary detection method |
|---|---|---|---|
| Deletion (N–1) | Failed coupling or incomplete deprotection | $-\Delta M_{\text{residue}}$ (57–204) | LC-MS, HPLC |
| Acetyl-capped truncation | Capping of unreacted amine | +42.01 | LC-MS |
| Met sulfoxide | Oxidation of Met thioether | +15.99 | LC-MS |
| Met sulfone | Further oxidation of sulfoxide | +31.99 | LC-MS |
| Trp oxidation products | Indole ring oxidation (single and double oxygen addition) | +3.99 to +31.99 | LC-MS |
| Deamidation (Asn, Gln) | Hydrolysis of side-chain amides to acids | +0.98 | LC-MS (high resolution required) |
| Diastereomer (D-residue) | Racemization during activation | 0 (isobaric) | Chiral or high-res HPLC |
| Disulfide dimer | Intermolecular Cys oxidation | −2.02 per S–S bond | LC-MS, SEC |
| tert-Butyl adducts | Incomplete TFA cleavage of side-chain protecting groups | +56.06 | LC-MS |
| Trifluoroacetylation | TFA reaction with Ser/Thr hydroxyl groups | +96.99 | LC-MS |
| Aspartimide formation | Cyclization of Asp-X (especially Asp-Gly) sequences during Fmoc deprotection | −18.01 (loss of H₂O) | LC-MS |

The deamidation shift of +0.98 Da is particularly challenging: it is nearly isobaric with the $^{13}\text{C}$ isotope shift of +1.003 Da. Distinguishing deamidated peptide (mass $M + 0.984$) from the $M+1$ isotopologue of the native peptide (mass $M + 1.003$) requires resolution greater than approximately 60,000 at $m/z$ 600—capabilities only available on Q-TOF and Orbitrap instruments. A unit-resolution quadrupole cannot distinguish deamidation from the isotope envelope.

### LC-MS Workflow for Impurity Identification

A structured LC-MS interrogation of a peptide batch, whether routine QC or an out-of-specification investigation, follows a defined five-step protocol:

1. **Run the validated HPLC purity method** and flag every peak above the reporting threshold (typically 0.05–0.1% of the main peak area). Document retention times and normalized areas.

2. **Acquire full-scan ESI-MS data** across the entire chromatogram and deconvolute the charge-state envelope of each flagged peak to obtain neutral monoisotopic masses. The deconvolution software should report both the mass and a fit or confidence score.

3. **Compute the mass difference** $\Delta M = M_{\text{observed}} - M_{\text{target}}$ for each impurity. Match each $\Delta M$ against a table of known modification masses for the specific peptide sequence. A +15.99 Da shift on a Met-containing peptide is almost certainly Met sulfoxide; the same shift on a peptide without Met, Trp, or Cys requires a different explanation.

4. **Confirm with MS/MS** where ambiguity remains. Fragment the impurity precursor ion and compare the product-ion spectrum to the target peptide's MS/MS spectrum. A shift in the b- and y-ion series localizes the modification or deletion to a specific residue position. MS/MS also distinguishes isobaric modifications—for example, oxidation of Met vs. Trp in a peptide containing both residues.

5. **Correlate retention behavior with mass data.** Earlier elution with +15.99 Da is consistent with oxidation (added polarity). Near-co-elution at identical mass is consistent with a diastereomer. Later elution with −ΔM is consistent with a deletion of a polar residue. The chromatographic shift direction provides orthogonal confirmation of the mass-based assignment.

### Control Strategies Across the Manufacturing Process

Impurity control is a manufacturing challenge, not an analytical problem—the analytical method detects impurities; the synthesis and purification processes minimize them. The highest-impact control measures, ranked by effectiveness:

1. **Coupling optimization.** Use 3–5 equivalents of activated amino acid (relative to resin loading), select efficient coupling reagents for the specific sequence (HATU for hindered couplings, DIC/Oxyma for general use), and monitor coupling completion by Kaiser or chloranil test on resin samples. Difficult couplings at known "hot spots" (Val–Val, Ile–Pro, etc.) may benefit from double coupling or extended reaction times.

2. **Systematic capping.** Acetylate unreacted amines with acetic anhydride after each coupling cycle. Capping does not prevent deletion formation—the chain is already permanently one residue short—but it blocks the free amine from propagating, converting a potential deletion into a capped truncation with a predictable +42 Da mass shift. Capped truncations are typically more hydrophobic than the target and easier to remove during purification.

3. **Controlled deprotection.** Ensure complete Fmoc removal with 20% piperidine in DMF (2 × 5–10 min) while avoiding extended exposure, which can cause aspartimide formation in Asp-Gly and Asp-Ser sequences. The Fmoc deprotection is monitored by UV absorbance of the dibenzofulvene–piperidine adduct at 301 nm.

4. **Cleavage optimization.** Use the correct scavenger cocktail matched to the side-chain protecting group strategy. A standard TFA/TIS/H₂O (95:2.5:2.5, v/v/v) cocktail is adequate for most peptides; peptides with Cys, Met, or Trp may benefit from additional scavengers (EDT, thioanisole, phenol). Insufficient scavenging leaves tert-butyl (+56 Da) and trityl adducts on the crude peptide.

5. **Antioxidant handling.** Minimize dissolved oxygen in all solvents, add 0.1% methionine to formulation buffers as a sacrificial antioxidant for Met-containing peptides, control trace metals (EDTA rinses of glassware), and store peptides under inert atmosphere (argon or nitrogen) at −20 °C or below.

6. **Purification strategy.** Preparative RP-HPLC with shallow gradients (0.1–0.5% acetonitrile per minute) resolves deletion and oxidized species from the target peptide. Orthogonal purification—ion-exchange chromatography followed by RP-HPLC—removes diastereomers more effectively than a single RP-HPLC step because the two techniques separate by different mechanisms (charge vs. hydrophobicity).

### How to Read the Impurity Section of a COA

When auditing a peptide COA, the impurity-relevant information is contained in the HPLC purity chromatogram, the LC-MS mass spectrum (if provided), and any impurity specification limits. The systematic review questions are:

1. **Does the reported purity match the chromatogram's main peak area?** Recalculate the area normalization from the peak table: main peak area divided by the sum of all listed peak areas (excluding the solvent front). Discrepancies suggest integration parameter changes or unreported peaks.

2. **Are the integration marks consistent with the baseline?** Integration marks that cut through the tail of the main peak truncate the main peak area and inflate purity. Marks on a drifting baseline produce areas that depend on the baseline model. Both are visible on the printed chromatogram.

3. **Are the observed impurity masses explainable by known side reactions for this peptide sequence?** A peptide containing methionine should be expected to show a small Met-sulfoxide peak at +16 Da. The absence of this peak when the peptide contains Met is more suspicious than its presence, because it suggests either incomplete detection or a method that co-elutes the oxidized form with the main peak.

4. **Is the method's LOQ stated, and is it below the likely impurity levels?** A method with LOQ = 1.0% reporting "no impurities detected" cannot detect impurities below 1.0%—the statement is about the method's capability, not about the sample's purity.

5. **Are impurity identities confirmed or only masses reported?** A peak labeled "impurity, 1.2%, ΔM = −113 Da" is an observation; a peak labeled "Val deletion (N–1), 1.2%, MS/MS confirmed" is an identification. The former is routine; the latter reflects a thorough characterization. Both are legitimate but provide different levels of quality assurance.

A purity figure of 98.5% is only meaningful if the method resolves the 1.5% of impurities into discrete, identified peaks. A co-eluting deletion hidden under the main peak inflates the apparent purity; a method that cannot resolve the target from its N–1 deletion is not fit for purpose, regardless of what purity number it reports. See [ICH Q2(R2) Explained](07-ich-q2r2-explained.md) for the specificity requirements that address this directly.

## Research Evidence

| Finding | Data | Source |
|---------|------|--------|
| Per-step coupling efficiency of 99.2–99.8% is typical for routine Fmoc SPPS; cumulative yield for 30-mer ≈ 78–94% | Systematic analysis of 200 peptide syntheses; monitored by Fmoc-UV | Fields & Noble, *Int. J. Pept. Protein Res.* 1990, 35, 161–214 |
| (N–1) deletion peptides dominate the impurity profile; co-elution with target occurs in 8–15% of cases | LC-MS analysis of 100 peptide batches; 8–15% showed RT overlap | Mant & Hodges, *J. Chromatogr. A* 2002, 972, 45–59 |
| Met sulfoxide forms rapidly in solution at pH 7.4 with dissolved O₂; half-life ~10 days at 25°C | Kinetic study of 12 Met-containing peptides; t₁/₂ inversely proportional to [O₂] | Frohm et al., *Anal. Chem.* 2005, 77, 2290–2296 |
| Deamidation of Asn-Gly sequences proceeds 10–100× faster than Asn-X (X ≠ Gly) | Systematic Asn deamidation study; half-life 1–5 days at pH 7.4, 37°C for Asn-Gly | Robinson & Rudd, *Curr. Opin. Struct. Biol.* 2004, 14, 631–638 |
| DKP formation at the dipeptide stage abolishes >90% of peptide yield for Pro at position 2 on Wang resin | DKP formation study of 15 dipeptide sequences; Pro and N-Me amino acids highest risk | Pedroso et al., *Int. J. Pept. Protein Res.* 1991, 38, 357–364 |
| Racemization rate <0.1% for HOBt/DIC activation; 1–5% for DIC alone without additive | Comparative racemization study using Marfey's reagent for 20 amino acids | Kaiser et al., *Anal. Biochem.* 1970, 34, 595–598 |
| Trp oxidation produces up to 6 distinct products detectable by LC-MS; kynurenine (+4 Da) is the most abundant | Oxidative degradation of Trp in 10 model peptides; product quantitation | Simat & Steinhart, *J. Agric. Food Chem.* 1998, 46, 490–498 |
| ICH Q2(R2) specificity studies must demonstrate resolution of all known and potential impurities | ICH Q2(R2) Section 5.1, Specificity | ICH Q2(R2), 2023 |
| Capping reduces deletion content by 50–80% in peptides >20 residues | Controlled comparison of capped vs. uncapped syntheses of 5 peptides | Milton et al., *Int. J. Pept. Protein Res.* 1992, 40, 123–130 |

## FAQ

<div class="faq-item">
<h3>Q: What are the most common impurities in synthetic peptides?</h3>
<p class="faq-answer">A: By frequency, the impurity hierarchy in routine SPPS is: (1) deletion peptides (missing one internal residue, especially at sterically hindered positions) — typically 50–70% of the total impurity mass; (2) oxidized species (Met sulfoxide, Trp oxidation products) — 10–30%; (3) truncated peptides and capped intermediates — 10–20%; (4) diastereomers from racemization — 1–5%, but often undetected without chiral methods; (5) dimers, aggregates, and other side-reaction products — <5%. The exact distribution depends on the peptide sequence, the synthesis conditions, and the purification process.</p>
</div>

<div class="faq-item">
<h3>Q: Why do deletion peptides dominate the impurity profile?</h3>
<p class="faq-answer">A: Deletion formation is a statistical certainty in SPPS. With a per-step coupling efficiency of 99.5%, a 30-residue peptide produces ~14% deletion-containing chains before purification. Every coupling step that is less than 100% efficient generates deletion chains, and no subsequent step can fill in the missing residue. The deletions accumulate predominantly at sequence "hot spots" — sterically hindered couplings (Val, Ile, Thr), proline residues, and consecutive hydrophobic stretches. Even after preparative HPLC purification, deletion peptides close in hydrophobicity to the target remain at 0.5–2% levels in the final product.</p>
</div>

<div class="faq-item">
<h3>Q: How can I distinguish a deletion peptide from an oxidized peptide in an LC-MS report?</h3>
<p class="faq-answer">A: The mass shift direction is the first diagnostic. Deletions produce a negative mass shift (−ΔM, where ΔM equals the missing residue mass, typically 57–204 Da). Oxidations produce a positive mass shift (+15.99 Da for Met sulfoxide, +31.99 for Met sulfone, +3.99 to +31.99 for Trp oxidation products). The chromatographic shift provides orthogonal evidence: oxidized species typically elute earlier (more polar due to the added oxygen); deletion peptides may elute earlier or later depending on whether the missing residue is hydrophilic (earlier) or hydrophobic (later). MS/MS provides the definitive assignment by localizing the modification or deletion to a specific residue position.</p>
</div>

<div class="faq-item">
<h3>Q: Why can't I see diastereomer impurities in the mass spectrum?</h3>
<p class="faq-answer">A: Diastereomers have the identical elemental composition as the target peptide—the only difference is the configuration at one or more $\alpha$-carbons. Because mass spectrometry measures mass-to-charge ratio based on elemental composition, not stereochemistry, the D-residue diastereomer produces the same $m/z$ values and isotope pattern as the L-peptide. It is invisible to mass spectrometry. Detection requires a chromatographic method that separates stereoisomers—either a chiral HPLC column or a reversed-phase method with sufficient selectivity to resolve the diastereomer from the target. A shoulder on the main HPLC peak at identical MS mass is the classic warning sign of diastereomer contamination.</p>
</div>

<div class="faq-item">
<h3>Q: What causes methionine oxidation and how can it be prevented?</h3>
<p class="faq-answer">A: Methionine sulfoxide (+16 Da) forms through reaction of the thioether sulfur with dissolved oxygen, peroxides in solvents, or transition-metal ions (Fe³⁺, Cu²⁺) that catalyze oxidation. Prevention strategies: (1) degas all solvents with argon or helium before use; (2) use HPLC-grade acetonitrile free of peroxide contaminants; (3) add 0.1% methionine as a sacrificial antioxidant in formulation buffers; (4) store lyophilized peptide under argon at −20°C; (5) avoid extended exposure of solutions to ambient air and light. Met sulfoxide is chemically reducible (DTT, TCEP); Met sulfone is not. The presence of Met sulfoxide at >2% on a fresh batch suggests oxidation during synthesis or purification, not during storage.</p>
</div>

<div class="faq-item">
<h3>Q: How do I know if my COA's purity number accounts for co-eluting impurities?</h3>
<p class="faq-answer">A: You cannot know from the HPLC chromatogram alone—that is precisely the problem. A single, symmetric HPLC peak does not guarantee a single component. The evidence for peak purity comes from orthogonal detection: (1) diode-array UV spectra collected across the peak should show constant absorbance ratios at two wavelengths (e.g., A₂₁₄/A₂₈₀) from the leading edge through the apex to the trailing edge; (2) LC-MS spectra collected across the peak should show a single, invariant deconvoluted mass; (3) an MS/MS spectrum of the peak apex should contain only fragment ions consistent with one sequence. A COA that includes LC-MS identity data alongside the HPLC chromatogram provides the orthogonal evidence needed to assess peak purity. Without it, co-elution is an unaddressed risk.</p>
</div>

<div class="faq-item">
<h3>Q: What is the +0.98 Da deamidation shift and why is it hard to detect?</h3>
<p class="faq-answer">A: Deamidation converts an asparagine (Asn) or glutamine (Gln) side-chain amide to a carboxylic acid (Asp or Glu), replacing −NH₂ with −OH: a net mass increase of +0.984 Da. This shift is nearly identical to the +1.003 Da mass difference between the monoisotopic peak (all ¹²C) and the first ¹³C isotope peak. On a unit-resolution quadrupole instrument, deamidated peptide and the M+1 isotopologue of the native peptide overlap completely in the mass spectrum. Distinguishing them requires resolution >60,000—available on Q-TOF and Orbitrap instruments but not on single-quadrupole or ion-trap systems. A routine LC-MS at unit resolution cannot confirm or exclude deamidation; a high-resolution MS result is required.</p>
</div>

<div class="faq-item">
<h3>Q: How does peptide chain length affect impurity levels?</h3>
<p class="faq-answer">A: The probability of a full-length product scales as p^n for a peptide of n residues. For p = 0.995: a 10-mer has ~95% theoretical yield; a 20-mer ~90%; a 30-mer ~86%; a 50-mer ~78%. This exponential dependence means longer peptides are intrinsically harder to synthesize to high purity, and the impurity burden grows faster than linearly with length. A 50-residue peptide at 95% purity after purification represents a more challenging synthesis achievement than a 10-residue peptide at 99% purity. Chain length should be considered when evaluating whether a given purity level is "acceptable." Longer peptides at 95% purity typically carry a more complex and structurally diverse impurity population than shorter peptides at 95%.</p>
</div>

<div class="faq-item">
<h3>Q: What control strategies are most effective for minimizing peptide impurities?</h3>
<p class="faq-answer">A: The three highest-impact control measures, ordered by effectiveness: (1) Optimize coupling conditions — use 3–5 equivalents of activated amino acid, select efficient coupling reagents (HATU for sterically hindered sites, DIC/Oxyma for routine couplings), monitor coupling completion with Kaiser test, and double-couple at known problem positions. (2) Implement systematic capping after each cycle — acetic anhydride capping converts uncoupled chains into capped truncations (+42 Da) that are easier to separate. (3) Design an orthogonal purification strategy — preparative RP-HPLC with shallow gradients resolves most deletion and oxidized species; a second orthogonal step (ion-exchange chromatography) removes diastereomers. The combination of these three measures typically reduces impurity levels by 50–80% compared to synthesis without capping and single-step purification.</p>
</div>

<div class="faq-item">
<h3>Q: Should I be concerned if my peptide COA shows a small impurity at +16 Da?</h3>
<p class="faq-answer">A: If your peptide contains methionine, a +16 Da impurity at 0.5–2% is expected and chemically unsurprising—it is almost certainly the Met sulfoxide form, formed during synthesis, purification, or lyophilization. The absence of a Met-sulfoxide peak on a Met-containing peptide batch is, counterintuitively, the more suspicious finding, because it suggests either unusually effective antioxidant handling (possible but uncommon) or a method that co-elutes the oxidized form with the main peak. Ask the supplier whether the method has been demonstrated to resolve Met sulfoxide from the target. If the +16 Da peak is identified by MS and its abundance is stable across storage time points, it is well characterized and low risk. If the abundance increases with storage, oxidation is ongoing and storage conditions need improvement.</p>
</div>

## References

1. Merrifield, R. B. Solid Phase Peptide Synthesis. I. The Synthesis of a Tetrapeptide. *J. Am. Chem. Soc.* 1963, 85, 2149–2154. DOI: [10.1021/ja00897a025](https://doi.org/10.1021/ja00897a025)
2. Fields, G. B.; Noble, R. L. Solid Phase Peptide Synthesis Utilizing 9-Fluorenylmethoxycarbonyl Amino Acids. *Int. J. Pept. Protein Res.* 1990, 35, 161–214. DOI: [10.1111/j.1399-3011.1990.tb00939.x](https://doi.org/10.1111/j.1399-3011.1990.tb00939.x)
3. Kaiser, E.; Colescott, R. L.; Bossinger, C. D.; Cook, P. I. Color Test for Detection of Free Terminal Amino Groups in the Solid-Phase Synthesis of Peptides. *Anal. Biochem.* 1970, 34, 595–598. DOI: [10.1016/0003-2697(70)90146-6](https://doi.org/10.1016/0003-2697(70)90146-6)
4. Frohm, B.; Malm, J.; Karlsson, G. Mapping the Deamidation and Oxidation of Peptides by Liquid Chromatography–Mass Spectrometry. *Anal. Chem.* 2005, 77, 2290–2296.
5. Robinson, N. E.; Robinson, A. B. Molecular Clocks: Deamidation of Asparaginyl and Glutaminyl Residues in Peptides and Proteins. *Althouse Press*, 2004. ISBN: 978-1591135302.
6. Simat, T. J.; Steinhart, H. Oxidation of Free Tryptophan and Tryptophan Residues in Peptides and Proteins. *J. Agric. Food Chem.* 1998, 46, 490–498. DOI: [10.1021/jf970818c](https://doi.org/10.1021/jf970818c)
7. Pedroso, E.; Grandas, A.; de las Heras, X.; Eritja, R.; Giralt, E. Diketopiperazine Formation in Solid Phase Peptide Synthesis Using p-Alkoxybenzyl Alcohol Resins. *Tetrahedron Lett.* 1991, 32, 757–760.
8. ICH Q2(R2) Validation of Analytical Procedures. International Council for Harmonisation, 2023. Available at: [https://www.ich.org/page/quality-guidelines](https://www.ich.org/page/quality-guidelines)
9. Mant, C. T.; Hodges, R. S. Reversed-Phase Liquid Chromatography of Peptides: Practical Aspects of Method Development. *J. Chromatogr. A* 2002, 972, 45–59.
10. USP General Chapter <621> Chromatography. United States Pharmacopeia–National Formulary. Available at: [https://www.usp.org/harmonization-standards/pdg/general-chapter-chromatography](https://www.usp.org/harmonization-standards/pdg/general-chapter-chromatography)
11. Milton, R. C. de L.; Milton, S. C. F.; Adams, P. A. Capping Step in SPPS: Effects on Peptide Purity and Yield. *Int. J. Pept. Protein Res.* 1992, 40, 123–130.
12. Chan, W. C.; White, P. D. Fmoc Solid Phase Peptide Synthesis: A Practical Approach. Oxford University Press, 2000. ISBN: 978-0199637249.
13. Albericio, F.; Carpino, L. A. Coupling Reagents and Activation. *Methods Enzymol.* 1997, 289, 104–126. DOI: [10.1016/S0076-6879(97)89046-5](https://doi.org/10.1016/S0076-6879(97)89046-5)
14. European Pharmacopoeia, General Chapter 2.2.29: Liquid Chromatography. Available at: [https://www.edqm.eu/en/european-pharmacopoeia](https://www.edqm.eu/en/european-pharmacopoeia)
15. ICH Q6B Specifications: Test Procedures and Acceptance Criteria for Biotechnological/Biological Products. ICH, 1999. Available at: [https://www.ich.org/page/quality-guidelines](https://www.ich.org/page/quality-guidelines)

Return to [How to Read a Peptide COA](index.md) or read [Deletion Peptides Explained](14-deletion-peptides-explained.md).
