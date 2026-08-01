---
title: "Understanding LC-MS Reports for Research Peptides"
description: "A comprehensive guide to reading Liquid Chromatography-Mass Spectrometry (LC-MS) reports, interpreting m/z spectra, and verifying peptide molecular weight."
category: "Quality Control"
tags: [LC-MS, Mass Spectrometry, Molecular Weight, Peptide Identity]
author: "RPL Peptides Research Team"
published: "2026-08-01"
---

# Understanding LC-MS Reports for Research Peptides

!!! info "Executive Summary"
    Liquid Chromatography-Mass Spectrometry (LC-MS) is the gold standard for confirming peptide molecular identity. While HPLC measures relative chromatographic purity, LC-MS measures the exact mass-to-charge ratio ($m/z$) of ionized molecules.

## ESI-MS Ionization Fundamentals
In Electrospray Ionization (ESI), peptides accept protons ($H^+$) during nebulization, forming multiply charged species in the gas phase:

$$\\frac{m}{z} = \\frac{M + z \\cdot 1.007276}{z}$$

Where:
- $M$ is the monoisotopic molecular mass of the neutral peptide.
- $z$ is the integer charge state ($+1, +2, +3, \\dots$).
- $1.007276$ is the mass of a proton ($H^+$).

### Example Charge State Calculation
For a peptide with monoisotopic mass $M = 4111.91\\text{ Da}$ (such as Semaglutide):
- $[M+3H]^{3+} = \\frac{4111.91 + 3(1.0073)}{3} = 1371.64\\text{ } m/z$
- $[M+4H]^{4+} = \\frac{4111.91 + 4(1.0073)}{4} = 1028.98\\text{ } m/z$

---

## TIC vs XIC Chromatograms

- **Total Ion Chromatogram (TIC)**: Plots total ion signal intensity across all scanned $m/z$ ratios against time.
- **Extracted Ion Chromatogram (XIC)**: Filters exclusively for $m/z$ signals corresponding to the calculated target peptide mass, isolating the analyte from background noise.

---

## Frequently Asked Questions

### What is the difference between Monoisotopic Mass and Average Mass?
Monoisotopic mass is calculated using the exact mass of the most abundant naturally occurring isotope for each element ($^{1}H, ^{12}C, ^{14}N, ^{16}O, ^{32}S$). Average mass is calculated using atomic weights averaged over natural isotopic abundances. High-resolution LC-MS reports monoisotopic mass.

---

## Related Guides in this Cluster
- [How to Read a Peptide COA](index.md)
- [Common Peptide Impurities](05-common-peptide-impurities.md)
- [How Laboratories Calculate HPLC Purity](16-how-laboratories-calculate-hplc-purity.md)
