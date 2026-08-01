---
title: "Peak Area vs Peak Height in HPLC Purity Calculations"
description: "Discover why chromatographic peak area integration is mathematically required for peptide purity calculations instead of peak height."
category: "Analytical Chemistry"
tags: [Peak Area, Peak Height, HPLC Purity, Integration]
author: "RPL Peptides Research Team"
published: "2026-08-01"
---

# Peak Area vs Peak Height in HPLC Purity Calculations

!!! info "Executive Summary"
    Chromatographic purity calculations use integrated peak area rather than peak height because peak height varies significantly with column degradation, flow rate fluctuations, and band broadening.

## Mathematical Integration Formula

$$\\text{Area } (A) = \\int_{t_1}^{t_2} I(t) \\, dt$$

Where $I(t)$ is the detector intensity at time $t$, integrated between peak start $t_1$ and peak end $t_2$.

For a Gaussian chromatographic peak:

$$\\text{Area} \\approx H \\times W_{0.5}$$

Where $H$ is peak height and $W_{0.5}$ is peak width at half-height.

---

## Why Peak Height Fails for Purity Determination

As an analytical column ages, band broadening increases peak width while reducing peak height. However, the total number of absorbed photons (and thus total integrated peak area) remains constant for a fixed mass of analyte.

| Factor | Effect on Peak Height | Effect on Peak Area |
| :--- | :--- | :--- |
| **Column Aging** | Decreases | Remains Constant |
| **Flow Rate Decrease** | Increases | Remains Constant |
| **Temperature Increase** | Increases | Remains Constant |

---

## Related Guides in this Cluster
- [How to Read a Peptide COA](index.md)
- [How Laboratories Calculate HPLC Purity](16-how-laboratories-calculate-hplc-purity.md)
