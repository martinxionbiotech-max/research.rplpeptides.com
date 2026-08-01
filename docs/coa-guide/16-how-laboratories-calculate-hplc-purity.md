---
title: "How Laboratories Calculate HPLC Purity: Area Normalization vs External Standards"
description: "Detailed breakdown of Area Percent Normalization vs Weight/Weight Assay percentage in chromatographic quality control."
category: "Purity Calculation"
tags: [Area Normalization, Response Factor, Assay, HPLC Purity]
author: "RPL Peptides Research Team"
published: "2026-08-01"
---

# How Laboratories Calculate HPLC Purity: Area Normalization vs External Standards

!!! info "Executive Summary"
    Purity calculation method choice directly affects reported percentage values on a Certificate of Analysis (COA).

## Area Percent Normalization Formula

$$\\text{Purity (\\%)} = \\frac{A_{\\text{main}}}{\\sum_{i=1}^{n} A_i} \\times 100$$

## Corrected Purity with Relative Response Factors ($RRF$)

$$\\text{Corrected Purity (\\%)} = \\frac{\\frac{A_{\\text{main}}}{RRF_{\\text{main}}}}{\\sum_{i=1}^{n} \\frac{A_i}{RRF_i}} \\times 100$$

Where $RRF_i$ is the relative UV response factor of impurity $i$ at $214\\text{ nm}$ compared to the main peptide.

---

## Related Guides in this Cluster
- [How to Read a Peptide COA](index.md)
- [Peak Area vs Peak Height](03-peak-area-vs-peak-height.md)
