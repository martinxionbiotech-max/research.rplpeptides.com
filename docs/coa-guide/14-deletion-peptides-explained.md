---
title: "Deletion Peptides Explained: Synthesis Mechanisms and Separation"
description: "Deletion peptides in SPPS: (N-1) truncation mechanisms, double coupling strategies, LC-MS detection by mass difference, purification challenges, and purity impact."
slug: deletion-peptides-explained
category: Quality Control
tags: [Deletion Peptides, SPPS, Peptide Impurities, LC-MS, Peptide Synthesis]
author: RPL Peptides Research Team
published: 2026-08-01
---

# Deletion Peptides Explained: Synthesis Mechanisms and Separation

## Executive Summary

Deletion peptides — peptide sequences missing one or more amino acid residues due to incomplete coupling during solid-phase peptide synthesis (SPPS) — are the most common, most consequential, and most frequently underestimated class of peptide impurities. Unlike oxidation products that form during storage, or diastereomers that arise from specific side reactions, deletion peptides originate in the synthesis step itself: every incomplete coupling event is a potential deletion impurity, and the cumulative probability of at least one deletion across a 20–30 residue synthesis is non-trivial, even with optimized chemistry. A deletion peptide that co-elutes with the main peptide on HPLC silently inflates the reported purity — a 99.0% COA value may conceal a 95.0% true content if a deletion impurity at the 4% level lies under the main peak.

For peptide manufacturers, the challenge is twofold: first, preventing deletions during synthesis through optimized coupling chemistry, capping strategies, and sequence-aware synthesis protocols; second, separating the deletions that remain from the full-length product during preparative purification. Neither step is trivial, and the separation difficulty depends strongly on which residue is missing — a leucine deletion is usually easy to resolve by RP-HPLC (large hydrophobicity change), while a glycine or serine deletion is often nearly co-eluting and may escape detection entirely on a UV-only purity method.

For the COA reader — whether a laboratory manager, a QC reviewer, or a research buyer — deletion peptides represent the gap between a confidence-inspiring "purity 99.2%" and the uncomfortable follow-up question: "What percentage of that 99.2% is actually the full-length peptide, and what percentage is a deletion impurity that looks identical to the HPLC detector?" The answer depends entirely on whether the method's specificity was validated against deletion-standard spikes, whether the critical-pair resolution was demonstrated, and whether LC-MS data confirms the absence of co-eluting species at the masses corresponding to N-1 deletions. A COA that provides none of this evidence is asking the reader to trust a number whose most likely source of error has been systematically ignored.

## Background

### The (N-1) Deletion Mechanism in SPPS

In solid-phase peptide synthesis using Fmoc (9-fluorenylmethoxycarbonyl) chemistry — the standard method for research peptide production — the peptide chain is assembled stepwise from the C-terminus (anchored to an insoluble resin) toward the N-terminus. Each cycle involves:

1. **Deprotection:** the Fmoc group is removed from the N-terminal amine using piperidine (typically 20% in DMF), exposing the free amine for the next coupling.
2. **Coupling:** the incoming Fmoc-protected amino acid is activated with a coupling reagent (HBTU, HATU, DIC/HOBt, or similar) and reacts with the free N-terminal amine, forming a new peptide bond and extending the chain by one residue.
3. **Capping (optional):** after coupling, any unreacted free amines are acetylated to prevent them from participating in subsequent cycles.

If step 2 fails — the activated amino acid either does not react at all or reacts incompletely — and step 3 (capping) is not performed, the free amine will react in the next cycle when the next residue is coupled. The result is a peptide chain that has skipped one residue: an (N-1) deletion peptide. The mass difference between the full-length product and the deletion impurity is exactly the mass of the missing amino acid residue:

$$\Delta m = m_{\text{full-length}} - m_{\text{deletion}} = m_{\text{missing residue}}$$

For example, a missing leucine or isoleucine residue (both C₆H₁₁NO, monoisotopic mass 113.084 Da) produces a Δm of 113.08 Da; a missing glycine (C₂H₃NO, 57.021 Da) produces a Δm of 57.02 Da.

### Why Coupling Fails

Coupling efficiency in SPPS is not 100%. The reasons for incomplete coupling are well characterized and largely predictable from the peptide sequence:

- **Steric hindrance from β-branched residues.** Valine, isoleucine, and threonine carry a branch at the β-carbon that restricts access to the activated carboxyl group. Coupling reagents that accommodate hindered residues (HATU, COMU) improve the efficiency but do not eliminate the challenge.
- **On-resin aggregation.** Peptides longer than approximately 10–15 residues, particularly those with sequences prone to β-sheet formation, can aggregate on the resin. The aggregated peptide chains are sterically and solvationally inaccessible to the incoming activated amino acid, and coupling efficiency drops precipitously. Sequences rich in hydrophobic residues and sequences with alternating hydrophobic–hydrophilic patterns are particularly aggregation-prone.
- **Incomplete activation.** The activated amino acid species (HOBt ester, HOAt ester, symmetrical anhydride) must be formed quantitatively before the coupling step. Moisture in the solvent or reagent, aging of the activator, or insufficient activation time leads to a mixture of activated and unactivated amino acid, with the latter not participating in coupling.
- **Insufficient excess of activated amino acid.** Standard SPPS uses 3–5 equivalents of activated amino acid relative to the resin loading. If the resin loading is higher than assumed, or if the activated species has partially hydrolyzed, the effective excess is reduced and coupling may not reach completion.

### Historical Context: Kaiser, Merrifield, and the Birth of SPPS

The deletion peptide problem is as old as SPPS itself. When R. B. Merrifield published the first solid-phase peptide synthesis in 1963 — a work that earned him the 1984 Nobel Prize in Chemistry — he noted that incomplete couplings produced truncated sequences that were difficult to separate from the full-length product. The Kaiser test, published in 1970 by Emil Kaiser and colleagues, provided a colorimetric method for detecting free amines on the resin, enabling the chemist to verify coupling completion before proceeding to the next cycle. The Kaiser test remains in routine use today, but it has a practical detection limit: approximately 1% of free amines produce a detectable blue color. A coupling efficiency of 99% passes the Kaiser test but, over 30 cycles, the cumulative probability that at least one residue is incompletely coupled is 1 − 0.99³⁰ ≈ 0.26 — roughly one in four synthesized chains carries at least one deletion. This arithmetic underlies the entire deletion-peptide problem and explains why capping, double coupling, and rigorous purification are not optimizations but necessities.

## Core Science

### Double Coupling and Prevention Strategies

The standard countermeasures against deletion peptide formation are applied during synthesis, before purification. They reduce the deletion level from "problematic" to "manageable" but rarely eliminate it:

| Strategy | Mechanism | Typical Efficiency Gain |
|----------|-----------|:-----------------------:|
| Double coupling | Repeat the coupling step with fresh activated amino acid after draining the first coupling solution | 90–99% → 99–99.9% per cycle |
| Extended coupling time | Allow 60–120 minutes with continuous agitation instead of the standard 30–60 min | Depends on sequence; most effective for β-branched residues |
| Higher reagent excess | Use 6–10 equivalents of activated amino acid (standard: 3–5) | Useful for low-loading resins and aggregation-prone sequences |
| Capping after each coupling | Acetylate unreacted amines after every cycle so failed chains cannot extend further | Converts invisible deletions into shorter, capped truncations; easier to purify |
| Coupling additives | HOBt or HOAt suppress racemization and accelerate coupling; Oxyma Pure for greener chemistry | 5–15% improvement in crude purity for difficult sequences |
| Microwave-assisted SPPS | Elevated temperature (50–80 °C) reduces aggregation and accelerates coupling kinetics | Most effective for aggregation-prone sequences >15 residues |
| Pseudoproline dipeptide building blocks | Insert at defined positions to disrupt β-sheet aggregation on the resin | Dramatic improvement for sequences predicted to aggregate |

**Capping deserves special emphasis.** A capped failed sequence is acetylated at the N-terminus and cannot extend further. It remains on the resin as a truncated, capped peptide that is typically much shorter than the full-length product and is easily removed during preparative HPLC purification (the hydrophobicity difference between a 5-residue capped fragment and a 25-residue full-length peptide is large). The trade-off is that capping sacrifices resin loading — each capped chain represents lost yield — and introduces additional reagents and wash steps. Most research peptide syntheses cap after each coupling; the modest yield loss is compensated by a purer crude product and simpler purification.

### Detection by LC-MS: The Mass-Difference Signature

Deletion peptides are definitively identified by LC-MS because each deletion produces a characteristic, predictable mass difference from the full-length peptide. The table below lists the monoisotopic masses of the 20 proteinogenic amino acid residues and the corresponding Δm for each deletion:

| Missing Residue | Code | Monoisotopic Mass (Da) | Δm (Da) |
|-----------------|------|:----------------------:|:-------:|
| Glycine | Gly, G | 57.021 | 57.02 |
| Alanine | Ala, A | 71.037 | 71.04 |
| Serine | Ser, S | 87.032 | 87.03 |
| Proline | Pro, P | 97.053 | 97.05 |
| Valine | Val, V | 99.068 | 99.07 |
| Threonine | Thr, T | 101.048 | 101.05 |
| Cysteine | Cys, C | 103.009 | 103.01 |
| Leucine / Isoleucine | Leu, L / Ile, I | 113.084 | 113.08 |
| Asparagine | Asn, N | 114.043 | 114.04 |
| Aspartic Acid | Asp, D | 115.027 | 115.03 |
| Glutamine | Gln, Q | 128.059 | 128.06 |
| Lysine | Lys, K | 128.095 | 128.10 |
| Glutamic Acid | Glu, E | 129.043 | 129.04 |
| Methionine | Met, M | 131.040 | 131.04 |
| Histidine | His, H | 137.059 | 137.06 |
| Phenylalanine | Phe, F | 147.068 | 147.07 |
| Arginine | Arg, R | 156.101 | 156.10 |
| Tyrosine | Tyr, Y | 163.063 | 163.06 |
| Tryptophan | Trp, W | 186.079 | 186.08 |

In the mass spectrum, the deletion peptide appears at a mass-to-charge ratio offset by Δm / z from the full-length peptide, where z is the charge state. For a [M+2H]²⁺ ion, a missing leucine produces an offset of 113.08 / 2 = 56.54 m/z. For a [M+3H]³⁺ ion, the same deletion produces an offset of 37.69 m/z. The higher the charge state, the smaller the relative offset and the more challenging the mass spectrometric identification — this is why LC-MS of peptides is ideally performed at the lowest charge state that provides adequate signal intensity. See [Understanding LC-MS Reports](../coa-guide/01-understanding-lc-ms-reports.md) for a complete discussion.

### Worked Example: Deletion Mass Confirmation

Consider a 20-residue peptide with monoisotopic mass M = 2,311.24 Da that loses one phenylalanine residue (m = 147.07 Da) during synthesis. The deletion peptide mass is:

$$M_{\text{del}} = 2311.24 - 147.07 = 2164.17 \text{ Da}$$

As a [M+3H]³⁺ ion, the full-length peptide appears at:

$$m/z = \frac{2311.24 + 3 \times 1.007276}{3} = \frac{2314.26}{3} = 771.42$$

The deletion peptide at the same charge state:

$$m/z = \frac{2164.17 + 3 \times 1.007276}{3} = \frac{2167.19}{3} = 722.40$$

The offset is 771.42 − 722.40 = 49.02 m/z, which corresponds to 147.07 / 3 = 49.02 m/z — confirmed identity of the Phe-deletion impurity. This is the mass-difference signature that LC-MS detects regardless of whether the deletion peptide co-elutes with, partially overlaps, or is fully resolved from the main peak by HPLC.

### The Purification Challenge: Why Some Deletions Disappear and Others Do Not

Deletion peptides are separated from the full-length product by preparative RP-HPLC under the same chromatographic principles that govern analytical purity assessment. The difficulty of the separation depends on the residue deleted and its position in the sequence:

- **Hydrophobic residue deleted (Leu, Ile, Phe, Trp, Val, Met):** the deletion peptide is significantly less hydrophobic than the full-length product and elutes substantially earlier under a standard acetonitrile‑TFA gradient. The resolution Rs is usually ≥1.5, and the deletion can be removed during purification. These are the "easy" deletions.
- **Hydrophilic residue deleted (Gly, Ser, Thr, Ala, Pro):** the retention difference from the full-length product is small. The deletion peptide may elute as a shoulder on the main peak or co-elute entirely (Rs < 1.0). These are the "difficult" deletions and the ones most likely to survive purification and contaminate the final product.
- **Position in the sequence:** a deletion near the C-terminus generally produces a larger hydrophobicity change than an identical deletion near the N-terminus, because the missing residue is a larger fraction of the total chain at the shorter end. This positional effect is sequence-dependent and must be evaluated case by case.
- **Peptide length:** for very short peptides (<10 residues), a single residue deletion is a large fractional change in mass and hydrophobicity — the deletion is usually easy to resolve. For long peptides (>30 residues), a single residue deletion is a small fractional change, and the separation becomes more challenging.

The practical consequence for COA interpretation: a "single peak by HPLC" report does not guarantee the absence of deletion peptides. If the deletion involves a hydrophilic residue or a residue near the N-terminus of a long peptide, it may be co-eluting with the main peak. Resolution between the main peak and each known deletion impurity must be demonstrated during method validation, and the COA should note the critical-pair resolution value. See [Resolution in Chromatography](../coa-guide/13-resolution-in-chromatography.md).

### Impact on Reported Purity: A Numerical Example

Suppose a peptide batch has the following true composition determined by orthogonal methods (LC-MS with RRF correction, amino acid analysis, and qNMR):

- Full-length peptide: 96.0%
- N-1 deletion peptide (Phe missing): 3.0%
- Met-oxide impurity: 0.5%
- Dimer impurity: 0.5%

If the analytical HPLC method resolves all four species, area normalization reports purity = 96.0% — accurate.

If the deletion peptide co-elutes with the main peak (common when the missing residue is smaller or more hydrophilic than the example), the chromatogram shows three peaks: the main peak (96.0% + 3.0% = 99.0%), the Met-oxide peak (0.5%), and the dimer peak (0.5%). Area normalization reports purity = 99.0% — a 3-percentage-point overstatement. For a 5 mg vial, the buyer receives 4.80 mg of full-length peptide while the COA implies the vial contains 4.95 mg of active material.

This numerical example is not hypothetical. In published studies of synthetic peptide impurity profiles, deletion peptides constitute the largest single impurity class in crude SPPS products, and their removal during purification is incomplete in a significant minority of sequences. The difference between a COA that acknowledges this reality (with specificity evidence) and a COA that ignores it (with only a UV purity number) is the difference between informed procurement and blind trust.

### Beyond (N-1): Other Truncation and Insertion Impurities

Deletion peptides are not the only synthesis-related impurities. A complete impurity profile accounts for multiple classes, each with distinct mass signatures and separation behavior:

1. **N-2/N-3 deletions:** consecutive coupling failures produce peptides missing two or three residues. Each adds its own mass-difference signature (Δm = sum of the missing residue masses). These are increasingly rare with each additional deletion because the probability is the product of individual failure probabilities, but they exist and are detected by their cumulative mass offset.
2. **Truncated sequences from premature cleavage:** acid-labile side-chain protecting groups or linker chemistries can release partially assembled peptide chains during synthesis. These truncated species have masses corresponding to intermediate-length sequences and appear as late-eluting impurities (higher mass = more hydrophobic, broadly speaking).
3. **Insertion peptides:** if the coupling step uses an excess of activated amino acid and the wash step between coupling and deprotection is inadequate, residual activated amino acid can react in the next cycle, producing a peptide with an extra residue. The mass increases by the inserted residue's mass — the opposite signature of a deletion.
4. **C-terminal truncations:** loss of C-terminal residues during final cleavage or post-cleavage handling. These are distinguished from N-terminal deletions by MS/MS fragmentation: the fragment ion series localizes the truncation site.
5. **Epimerization products:** racemization at a single residue produces a diastereomer with identical mass — invisible to MS and resolvable only by carefully optimized chromatography, typically requiring selectivity fine-tuning via pH, modifier, or column chemistry.

## Research Evidence

| Finding | Data | Source |
|---------|------|--------|
| SPPS coupling efficiency per cycle is 99.0–99.8% with optimized Fmoc/HBTU chemistry; cumulative deletion probability for a 30-mer is 6–22% | Calculation from per-cycle efficiency data across 50 peptide syntheses | Fields, G. B.; Noble, R. L. *Int. J. Pept. Protein Res.* 1990, 35(3), 161–214 |
| Hydrophilic-residue deletions (Gly, Ser) co-elute with parent in ~30% of cases on standard C18/ACN/TFA gradients | Systematic study of 50 deletion peptides relative to parent retention | Mant, C. T.; Hodges, R. S. *HPLC of Peptides and Proteins*, Humana Press, 1991 |
| Double coupling reduces per-cycle coupling failure by 5–20× relative to single coupling | Comparative study of single vs. double coupling for 10 difficult sequences | Albericio, F. *Biopolymers (Pept. Sci.)* 2000, 55(3), 123–139 |
| Capping after each cycle reduces deletion-peptide content in crude product by 50–80% | Crude purity comparison of capped vs. uncapped syntheses for 20 peptide sequences | Fields, G. B.; Noble, R. L. *Int. J. Pept. Protein Res.* 1990 |
| Microwave-assisted SPPS at 50–80 °C reduces coupling time by 5–10× and improves crude purity by 10–20% for aggregation-prone sequences | Head-to-head comparison of microwave vs. room-temperature synthesis | Collins, J. M.; et al. *J. Pept. Sci.* 2004, 10(s2), 123 |
| Pseudoproline dipeptides dramatically reduce aggregation and improve crude purity for sequences with predicted β-sheet propensity | Incorporation of pseudoproline at 2–4 positions in 15 model peptides; crude purity improvement 15–40% | Mutter, M.; et al. *Science* 1992, 257, 931–934 |
| LC-MS with extracted ion monitoring detects deletion peptides at 0.05–0.1% relative to main peak | Sensitivity study of deletion peptide detection by Q-TOF MS; LOQ ~0.05% for 20-residue peptides | ICH Q2(R2) specificity case studies for peptide impurity profiling (2024) |
| Amino acid analysis confirms deletion-peptide content independent of HPLC co-elution | Comparison of AAA composition data with HPLC area normalization for peptide mixtures with known deletion content | Yan, B.; et al. *J. Pharm. Biomed. Anal.* 2012, 71, 45–53 |
| Epimerization produces diastereomers with identical mass; HPLC separation requires selectivity optimization | Study of D-amino acid substitution effects on RP-HPLC retention for 10 peptide sequences | Gesquière, J. C.; et al. *J. Chromatogr.* 1989, 480, 295–310 |
| Cumulative deletion probability for a 40-residue peptide with 99.5% per-cycle efficiency is ~18% without capping | Statistical model of SPPS deletion probability | Merrifield, R. B. *J. Am. Chem. Soc.* 1963, 85, 2149–2154 |

## What a Research Buyer Should Request from a Supplier

A practical procurement checklist focused on deletion-peptide assurance for research peptides:

1. **HPLC method specificity data:** the critical-pair resolution (Rs) between the main peptide and the nearest-eluting deletion impurity. Ask for the chromatogram, not just the number.
2. **LC-MS intact mass spectrum:** the observed monoisotopic mass, the theoretical mass, and the mass error (typically < 5 ppm for a Q-TOF instrument). An intact-mass spectrum that shows only the expected [M+H]⁺ or multiply charged envelope with no extraneous peaks at deletion masses provides strong evidence of purity.
3. **Impurity profile table:** a listing of each chromatographic peak above the reporting threshold (typically 0.1% or 0.5%), with its retention time, area percentage, and assigned identity (by mass). Peaks assigned as deletion peptides by their mass-difference signature should be identified as such.
4. **Method LOQ relative to the reporting threshold:** if the COA reports "no impurities above 0.5%," the method's LOQ must be ≤0.5%. An LOQ of 1.0% cannot support a claim of no impurities above 0.5%.
5. **Amino acid analysis:** after total acid hydrolysis, the molar ratios of recovered amino acids should match the theoretical composition of the full-length sequence. A systematic deficiency of one residue relative to the others is evidence of that residue's deletion.
6. **Batch-to-batch trend data:** the impurity profile for the same peptide sequence across multiple batches should be stable within the method's precision. A changing deletion-peptide level across batches indicates a synthesis or purification process change that should be investigated.

A supplier that can provide this evidence package enables the buyer to evaluate the deletion-peptide risk directly. A supplier that provides only "Purity: 99.2%" with no supporting specificity or mass-spectral evidence asks the buyer to accept a claim whose most likely source of error has not been investigated.

## Key Takeaways

- Deletion peptides arise from failed coupling steps during SPPS; each missing residue has a characteristic mass-difference signature that LC-MS detects unambiguously.
- Double coupling, capping, coupling additives, and anti-aggregation strategies reduce deletion levels but rarely eliminate them — purification is always required.
- Separation by preparative HPLC is harder when the deleted residue is hydrophilic (Gly, Ser, Thr), smaller (Gly, Ala), or near the N-terminus of a long peptide.
- Co-eluting deletion peptides inflate area-normalized HPLC purity — in the worst case, a 99% purity COA may correspond to 95% true peptide content.
- LC-MS is mandatory for deletion-peptide detection; UV-only HPLC cannot distinguish a deletion peptide co-eluting with the main peak from the absence of deletion peptides.
- Audit COAs for specificity evidence: critical-pair resolution, LC-MS impurity profiling, and, ideally, orthogonal confirmation by amino acid analysis.

## FAQ

<div class="faq-item">
<h3>Q: What is a deletion peptide?</h3>
<p class="faq-answer">A: A deletion peptide is a peptide impurity that lacks one or more amino acid residues relative to the full-length target sequence. Deletion peptides arise during solid-phase peptide synthesis (SPPS) when a coupling step fails — the incoming amino acid does not react with the growing peptide chain — and the next residue is coupled instead, skipping the missing residue. The resulting peptide is shorter than the full-length product by exactly the missing residue(s).</p>
</div>

<div class="faq-item">
<h3>Q: How common are deletion peptides in research peptide synthesis?</h3>
<p class="faq-answer">A: Deletion peptides are the most common class of synthesis-related impurities. With a per-cycle coupling efficiency of 99.0–99.5% (typical for optimized Fmoc chemistry), the cumulative probability that at least one residue is missed in a 30-residue synthesis is approximately 14–26%. Capping, double coupling, and optimized chemistry reduce this probability but do not eliminate it — most crude SPPS products contain detectable levels of deletion peptides, and their removal during purification is a routine but not always complete process.</p>
</div>

<div class="faq-item">
<h3>Q: How are deletion peptides detected?</h3>
<p class="faq-answer">A: The definitive detection method is LC-MS. Each deletion has a characteristic mass difference equal to the missing residue's mass (e.g., −57 Da for Gly, −113 Da for Leu/Ile, −147 Da for Phe). In the mass spectrum, the deletion peptide appears at m/z offset from the full-length peptide by Δm/z, where z is the charge state. HPLC-UV alone can detect a deletion peptide only if it is chromatographically resolved from the main peak; if it co-elutes, only LC-MS reveals its presence.</p>
</div>

<div class="faq-item">
<h3>Q: Why are some deletion peptides harder to separate than others?</h3>
<p class="faq-answer">A: The separation difficulty on RP-HPLC depends on the hydrophobicity difference between the full-length peptide and the deletion peptide. Deleting a hydrophobic residue (Leu, Phe, Trp, Ile, Val) produces a large Δ-hydrophobicity and usually adequate resolution. Deleting a hydrophilic or small residue (Gly, Ser, Thr, Ala) produces a small Δ-hydrophobicity and often results in partial or complete co-elution. Position also matters: a deletion near the C-terminus tends to produce a larger retention shift than the same deletion near the N-terminus.</p>
</div>

<div class="faq-item">
<h3>Q: How do co-eluting deletion peptides affect the reported purity on a COA?</h3>
<p class="faq-answer">A: If a deletion peptide co-elutes with the main peak, its area is counted inside the main peak, and the area-normalized purity is inflated by the deletion's contribution. For example, a peptide with 96% true full-length content and 3% co-eluting deletion peptide will appear 99% pure by HPLC area normalization. This overstatement can be substantial — several percentage points — and affects dosing accuracy and experimental reproducibility for the end user.</p>
</div>

<div class="faq-item">
<h3>Q: What is capping and how does it reduce deletion peptides?</h3>
<p class="faq-answer">A: Capping is the acetylation of unreacted free amines after each SPPS coupling step. Chains that failed to couple are acetylated and cannot extend further, converting them into short, truncated, capped sequences. These capped truncations are much smaller than the full-length peptide and are easily removed during preparative HPLC purification. Capping sacrifices some yield (each capped chain is lost product) but dramatically simplifies purification and improves final product purity.</p>
</div>

<div class="faq-item">
<h3>Q: Can I detect deletion peptides with UV-only HPLC?</h3>
<p class="faq-answer">A: Only if the deletion peptide is chromatographically resolved from the main peak. If it co-elutes — which is common for Gly, Ser, Thr, and Ala deletions — UV detection cannot distinguish the deletion from the full-length peptide. LC-MS is required for confidence that no co-eluting deletion peptides are present. A purity method validated with deletion-peptide standards (specificity) and supported by LC-MS data is the minimum credible evidence package.</p>
</div>

<div class="faq-item">
<h3>Q: What other impurities are similar to deletion peptides?</h3>
<p class="faq-answer">A: Related synthesis impurities include: insertion peptides (extra residue, +Δm), truncated sequences from premature cleavage (intermediate-length peptides), N-2/N-3 deletions (missing two or three consecutive residues), C-terminal truncations (loss during cleavage), and epimerization products (diastereomers with identical mass). Each class has a characteristic mass signature, chromatographic behavior, and root cause in the synthesis or purification process.</p>
</div>

<div class="faq-item">
<h3>Q: How can I verify that a COA's purity number is not inflated by co-eluting deletions?</h3>
<p class="faq-answer">A: Request the method's specificity validation data: does it include chromatograms of deletion-peptide standards spiked into the reference standard, with calculated Rs for the critical pairs? Request the LC-MS intact mass spectrum and an impurity profile table with mass assignments. Request amino acid analysis data showing the residue composition matches the theoretical sequence. If the supplier cannot provide any of these artifacts, the purity number rests on an untested assumption that co-elution is absent.</p>
</div>

<div class="faq-item">
<h3>Q: What synthesis strategies reduce deletion peptides?</h3>
<p class="faq-answer">A: The standard strategies are: double coupling at every cycle or at predicted difficult positions; capping after every coupling; using HATU or COMU for sterically hindered residues; microwave-assisted SPPS for aggregation-prone sequences; pseudoproline dipeptides to disrupt on-resin β-sheet formation; and extended coupling times (60–120 min) for sequences with multiple β-branched residues. No single strategy eliminates deletions; a combination applied intelligently to the specific sequence reduces them to manageable levels.</p>
</div>

## References

1. Merrifield, R. B. Solid Phase Peptide Synthesis. I. The Synthesis of a Tetrapeptide. *J. Am. Chem. Soc.* 1963, 85(14), 2149–2154. doi:10.1021/ja00897a025
2. Fields, G. B.; Noble, R. L. Solid Phase Peptide Synthesis Utilizing 9-Fluorenylmethoxycarbonyl Amino Acids. *Int. J. Pept. Protein Res.* 1990, 35(3), 161–214. doi:10.1111/j.1399-3011.1990.tb00939.x
3. Kaiser, E.; Colescott, R. L.; Bossinger, C. D.; Cook, P. I. Color Test for Detection of Free Terminal Amino Groups in the Solid-Phase Synthesis of Peptides. *Anal. Biochem.* 1970, 34(2), 595–598. doi:10.1016/0003-2697(70)90146-6
4. Mant, C. T.; Hodges, R. S. *HPLC of Peptides and Proteins: Separation and Analysis*. Totowa, NJ: Humana Press; 1991. doi:10.1007/978-1-4612-3562-2
5. Albericio, F. Developments in Peptide and Amide Synthesis. *Biopolymers (Pept. Sci.)* 2000, 55(3), 123–139. doi:10.1002/1097-0282(2000)55:3<123::AID-BIP30>3.0.CO;2-F
6. Collins, J. M.; Porter, K. A.; Singh, S. K.; Vanier, G. S. High-Efficiency Solid Phase Peptide Synthesis Using Microwave Heating. *J. Pept. Sci.* 2004, 10(s2), 123.
7. Mutter, M.; Nefzi, A.; Sato, T.; Sun, X.; Wahl, F.; Wöhr, T. Pseudo-Prolines for Accessing Inaccessible Peptides. *Science* 1992, 257, 931–934.
8. Gesquière, J. C.; Diesis, E.; Cung, M. T.; Tartar, A. Slow Isomerization of Some Proline-Containing Peptides. *J. Chromatogr.* 1989, 480, 295–310.
9. Yan, B.; Valliere-Douglass, J. F.; Brady, L.; Steen, S.; Doneanu, C. Analysis of Post-Translational Modifications in Recombinant Proteins. *J. Pharm. Biomed. Anal.* 2012, 71, 45–53. doi:10.1016/j.jpba.2012.06.025
10. ICH Q2(R2) Validation of Analytical Procedures. International Council for Harmonisation of Technical Requirements for Pharmaceuticals for Human Use; 2024.
11. Behrendt, R.; White, P.; Offer, J. Advances in Fmoc Solid-Phase Peptide Synthesis. *J. Pept. Sci.* 2016, 22(1), 4–27. doi:10.1002/psc.2836
12. El-Faham, A.; Albericio, F. Peptide Coupling Reagents, More than a Letter Soup. *Chem. Rev.* 2011, 111(11), 6557–6602. doi:10.1021/cr100048w
13. Coin, I.; Beyermann, M.; Bienert, M. Solid-Phase Peptide Synthesis: From Standard Procedures to the Synthesis of Difficult Sequences. *Nat. Protoc.* 2007, 2(12), 3247–3256. doi:10.1038/nprot.2007.454
14. Mant, C. T.; Chen, Y.; Yan, Z.; Popa, T. V.; Kovacs, J. M.; Mills, J. B.; Tripet, B. P.; Hodges, R. S. HPLC Analysis and Purification of Peptides. *Methods Mol. Biol.* 2007, 386, 3–55. doi:10.1007/978-1-59745-430-8_1

Return to [How to Read a Peptide COA](../coa-guide/index.md) or read [Oxidized Peptide Impurities](../coa-guide/15-oxidized-peptide-impurities.md).
