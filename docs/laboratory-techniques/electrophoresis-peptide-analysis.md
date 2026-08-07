---
title: Electrophoresis for Peptide Analysis
description: "Principles of electrophoretic mobility, SDS-PAGE for small peptides using the Tris-tricine system, capillary electrophoresis theory, electroosmotic flow, micellar electrokinetic chromatography (MEKC), and isoelectric focusing for determination of peptide pI values."
---

# Electrophoresis for Peptide Analysis

## Executive Summary

Electrophoresis is a fundamental analytical technique for the separation and characterization of peptides based on their differential migration in an electric field. The electrophoretic mobility of a peptide is determined by its charge-to-size ratio, which can be systematically manipulated through buffer composition, pH, and detergent selection. This article examines the physicochemical principles underlying electrophoretic separations as applied to peptide analysis: the Tris-tricine SDS-PAGE system specifically optimized for small peptides, the theory of capillary electrophoresis (CE) including electroosmotic flow and Joule heating effects, micellar electrokinetic chromatography (MEKC) as a hybrid separation mode, and isoelectric focusing (IEF) for precise determination of peptide isoelectric points (pI). These electrophoretic techniques complement chromatographic methods for peptide characterization and are essential tools in any peptide research laboratory. Researchers seeking detailed electrophoretic characterization data for research peptides can access analytical documentation through the [RPL Peptides Data Center](https://data.rplpeptides.com), where HPLC and electrophoretic purity data are available for reference-grade peptides from [RPL Peptides](https://rplpeptides.com).

## Background

Electrophoresis was pioneered by Arne Tiselius in the 1930s, for which he received the Nobel Prize in Chemistry in 1948. His moving-boundary electrophoresis apparatus demonstrated that proteins could be separated based on their electrophoretic mobility — a discovery that laid the foundation for modern biochemical analysis. The introduction of zone electrophoresis on stabilizing media (paper, starch, agar, and ultimately polyacrylamide gels) in the 1950s–1960s transformed electrophoresis from a specialized physical chemistry technique into a routine laboratory method.

The development of SDS-polyacrylamide gel electrophoresis (SDS-PAGE) by Laemmli in 1970 standardized protein molecular weight determination, but the Laemmli system (using Tris-glycine buffers) proved suboptimal for peptides below approximately 15 kDa. The glycine stacking front outruns small peptides, resulting in poor resolution and diffuse bands. The Tris-tricine SDS-PAGE system developed by Schägger and von Jagow in 1987 addressed this limitation by replacing glycine with tricine, which has a lower electrophoretic mobility due to its larger molecular size and lower pKa of the amino group (8.15 vs. 9.6 for glycine), keeping the stacking front behind small peptides and enabling high-resolution separation of peptides as small as 1 kDa.

Capillary electrophoresis, introduced by Jorgenson and Lukacs in 1981, miniaturized electrophoresis to fused-silica capillaries with inner diameters of 25–100 μm. The high surface-to-volume ratio of capillaries provides exceptional heat dissipation, enabling electric field strengths of 200–500 V/cm (compared to 5–20 V/cm for slab gels) and producing separations in minutes rather than hours, with theoretical plate counts exceeding 100,000.

## Fundamental Principles of Electrophoretic Mobility

### The Electrophoretic Mobility Equation

The velocity ($v$) of a charged particle in an electric field is given by:

$$v = \mu_e \cdot E$$

where $E$ is the electric field strength (V/cm) and $\mu_e$ is the electrophoretic mobility (cm²/V·s). The electrophoretic mobility of a peptide is determined by the balance of the electrical force driving migration and the frictional force opposing it:

$$\mu_e = \frac{q}{f} = \frac{q}{6\pi\eta r}$$

where $q$ is the effective charge of the peptide, $f$ is the frictional coefficient, $\eta$ is the solution viscosity, and $r$ is the Stokes radius of the peptide. This equation, derived from Stokes' law for spherical particles, predicts that electrophoretic mobility is proportional to charge and inversely proportional to size.

For peptides, which are not perfectly spherical, the frictional coefficient is shape-dependent. Compact, globular peptides have smaller frictional coefficients than extended, denatured peptides of the same mass, meaning they migrate faster. This shape sensitivity provides a mechanism for detecting conformational differences: a folded peptide and its denatured counterpart of identical mass and sequence will have different electrophoretic mobilities.

### The Double Layer and Zeta Potential

In solution, the charged surface of a peptide attracts counterions, forming an electrical double layer. The zeta potential ($\zeta$) is the electrical potential at the shear plane — the boundary between the tightly bound counterion layer (Stern layer) and the diffuse layer. The electrophoretic mobility is related to the zeta potential through the Smoluchowski equation:

$$\mu_e = \frac{\varepsilon_r \varepsilon_0 \zeta}{\eta}$$

where $\varepsilon_r$ is the relative permittivity of the medium and $\varepsilon_0$ is the permittivity of free space. This relationship is particularly important in capillary electrophoresis, where the zeta potential of the capillary wall drives electroosmotic flow.

### Buffer Ionic Strength Effects

The ionic strength of the electrophoresis buffer significantly affects peptide mobility. Higher ionic strength compresses the electrical double layer, reducing the zeta potential and electrophoretic mobility. Conversely, low ionic strength buffers produce faster migration but may compromise resolution due to increased diffusion and band broadening. The Debye-Hückel screening length ($\kappa^{-1}$) quantifies this effect:

$$\kappa^{-1} = \sqrt{\frac{\varepsilon_r \varepsilon_0 k_B T}{2 N_A e^2 I}}$$

where $k_B$ is the Boltzmann constant, $T$ is temperature, $N_A$ is Avogadro's number, $e$ is the elementary charge, and $I$ is the ionic strength. For typical electrophoresis buffers ($I$ = 0.05–0.2 M), the Debye length is 0.7–1.5 nm, comparable to the dimensions of hydrated counterions.

## SDS-PAGE for Small Peptides: The Tris-Tricine System

### Limitations of the Laemmli Tris-Glycine System

The standard Laemmli SDS-PAGE system, which revolutionized protein analysis, suffers from a fundamental limitation when applied to small peptides. The stacking gel operates on the isotachophoresis principle, where proteins are concentrated into a narrow band at the interface between leading ions (chloride, high mobility) and trailing ions (glycinate, pH-dependent mobility). As the stacking front moves through the resolving gel, the pH shift from 6.8 (stacking gel) to 8.8 (resolving gel) increases the ionization of glycine, accelerating it through the resolving gel.

For proteins above approximately 15 kDa, the glycine front overtakes the proteins only after significant separation has occurred. However, for small peptides (1–10 kDa), glycine outruns them almost immediately upon entering the resolving gel, resulting in the peptides migrating in a continuously de-stacking, de-focused zone. The consequence is poor resolution, diffuse bands, and in extreme cases, the complete loss of small peptides from the gel.

### The Tris-Tricine Solution

The Tris-tricine system replaces glycine (Mr = 75) with tricine (Mr = 179) as the trailing ion in the cathode buffer. Tricine has a lower pKa of the amino group (8.15 vs. 9.6 for glycine), meaning it remains less ionized at the resolving gel pH and migrates more slowly. The reduced mobility of tricine ensures that even small peptides (down to ~1 kDa) remain stacked behind the trailing ion front for a significant distance into the resolving gel.

The Schägger and von Jagow system uses three gel layers:

1. **Stacking gel** (4% T, 3% C): Concentrates the sample into a tight band.
2. **Spacer gel** (10% T, 3% C): Provides a smooth transition between the stacking and resolving gel, reducing protein precipitation at the interface.
3. **Resolving gel** (16.5% T, 6% C): The high acrylamide concentration (%T = total acrylamide) and cross-linker ratio (%C = bisacrylamide/total acrylamide) create a tight pore structure capable of sieving small peptides.

The effective separation range of the 16.5% T, 6% C resolving gel is approximately 1–100 kDa, with excellent resolution in the 1–20 kDa range where the Laemmli system fails entirely.

### Ferguson Plot Analysis

The Ferguson plot provides a quantitative framework for analyzing SDS-PAGE data. The relationship between the relative mobility ($R_f$) and gel concentration (%T) is:

$$\log R_f = \log Y_0 - K_R \cdot T$$

where $Y_0$ is the extrapolated mobility at 0% T (related to the free-solution mobility) and $K_R$ is the retardation coefficient (related to the effective molecular size). For SDS-denatured peptides, $K_R$ is proportional to the molecular weight, enabling molecular weight determination from a series of gels at different %T concentrations. The Ferguson plot can also detect anomalous migration: peptides with unusual amino acid compositions or residual structure deviate from the linear $\log R_f$ vs. %T relationship.

### Practical Considerations for Peptide SDS-PAGE

Peptide fixation in the gel is more challenging than for proteins because small peptides can diffuse out of the gel matrix during staining and destaining. Formaldehyde or glutaraldehyde fixation (0.5–1% in the staining solution) cross-links peptides to the gel matrix, preventing washout. Coomassie Brilliant Blue G-250 (colloidal) provides sensitivity down to approximately 50–100 ng per band for peptides, while silver staining extends detection to 0.5–5 ng. For very small peptides (<3 kDa), fluorescence staining with SYPRO Ruby or Deep Purple provides better linear dynamic range and reproducibility than silver staining.

## Capillary Electrophoresis (CE) Theory

### Fundamentals of CE Separation

Capillary electrophoresis performs electrophoretic separations in narrow-bore fused-silica capillaries (typically 25–100 μm i.d., 20–100 cm length). The small capillary dimensions provide two critical advantages: exceptional heat dissipation (Joule heating is efficiently removed through the capillary wall) enabling high field strengths, and minimal sample consumption (nanoliter injection volumes).

In the simplest mode — capillary zone electrophoresis (CZE) — the capillary is filled with a homogeneous buffer, and separation relies solely on differences in electrophoretic mobility. The apparent mobility ($\mu_{app}$) of an analyte is:

$$\mu_{app} = \frac{L_d \cdot L_t}{V \cdot t_m}$$

where $L_d$ is the length to the detector, $L_t$ is the total capillary length, $V$ is the applied voltage, and $t_m$ is the migration time. The apparent mobility is the vector sum of the electrophoretic mobility ($\mu_e$) and the electroosmotic flow mobility ($\mu_{EOF}$):

$$\mu_{app} = \mu_e + \mu_{EOF}$$

### Electroosmotic Flow (EOF)

Electroosmotic flow is the bulk flow of buffer solution through the capillary driven by the electric field. It arises from the ionization of silanol groups (Si-OH → Si-O⁻) on the inner surface of the fused-silica capillary at pH > 3. The negatively charged capillary wall attracts a layer of positive counterions from the buffer, forming an electrical double layer.

When the electric field is applied, the hydrated cations in the diffuse layer migrate toward the cathode, dragging the bulk solution with them. This produces a flat, plug-like flow profile — in contrast to the parabolic (laminar) flow profile of pressure-driven HPLC — which minimizes band broadening and contributes to the exceptional efficiency of CE separations.

The EOF velocity ($v_{EOF}$) is given by:

$$v_{EOF} = \mu_{EOF} \cdot E = \frac{\varepsilon_r \varepsilon_0 \zeta_{wall}}{\eta} \cdot E$$

where $\zeta_{wall}$ is the zeta potential of the capillary inner surface. The EOF is strongly pH-dependent: below pH ~3, silanol groups are largely protonated and EOF is negligible; above pH ~7, silanol groups are fully ionized and EOF is maximal. For peptide analysis, the pH range 2.5–9.5 provides tunable EOF that can be used to optimize separation speed and resolution.

### Joule Heating and Efficiency

The current passing through the electrophoresis buffer generates heat (Joule heating) proportional to the electrical power:

$$P = V \cdot I = \frac{V^2}{R}$$

where $R$ is the electrical resistance of the buffer. In slab gels, Joule heating is a limiting factor, producing temperature gradients across the gel that cause band distortion (the "smile effect") and limiting applied voltages to 100–300 V. In capillaries, the high surface-to-volume ratio and efficient heat dissipation allow field strengths of 200–500 V/cm without significant band broadening from thermal gradients.

The theoretical plate count in CE, assuming only longitudinal diffusion contributes to band broadening, is:

$$N = \frac{(\mu_e + \mu_{EOF}) \cdot V}{2 D_m}$$

where $D_m$ is the diffusion coefficient. For peptides ($D_m \approx 10^{-6}$ cm²/s) at typical CE voltages (20–30 kV), $N$ can exceed 200,000 plates — comparable to or exceeding the efficiency of UHPLC for peptide separations.

### Sample Injection in CE

CE injection is performed electrokinetically or hydrodynamically, both of which are fundamentally different from HPLC loop injection:

**Hydrodynamic injection:** Applies a pressure differential (typically 0.5 psi for 5–30 seconds) to introduce a plug of sample solution. The injection volume is proportional to the pressure, time, capillary dimensions, and inversely proportional to buffer viscosity. This method is non-discriminatory —all analytes are introduced in proportion to their concentration in the sample.

**Electrokinetic injection:** Applies a voltage while the capillary inlet is in the sample solution. Analytes migrate into the capillary at rates proportional to their electrophoretic mobilities, introducing a bias toward highly mobile species. For quantitative peptide analysis, hydrodynamic injection is preferred, but electrokinetic injection provides a mechanism for on-capillary sample concentration of dilute peptide solutions.

## Micellar Electrokinetic Chromatography (MEKC)

### Principles of MEKC

Micellar electrokinetic chromatography, developed by Terabe and colleagues in 1984, extends the scope of CE to neutral analytes by introducing a pseudostationary phase — surfactant micelles — into the running buffer. MEKC bridges the gap between electrophoresis and chromatography: separation is based on differential partitioning of analytes between the aqueous buffer (mobile phase) and the hydrophobic interior of micelles (pseudostationary phase), while the micelles themselves migrate electrophoretically.

Sodium dodecyl sulfate (SDS) is the most common surfactant for MEKC, used at concentrations above its critical micelle concentration (CMC ~8 mM in water). At concentrations of 50–100 mM in CE buffers, SDS forms spherical micelles with hydrophobic cores (diameter ~3–5 nm) and negatively charged sulfate head groups at the surface. The micelles have a high electrophoretic mobility toward the anode, which opposes the cathodic EOF. However, at pH > 5, the EOF is sufficiently strong to sweep all species — neutral analytes, micelles, and buffer ions — toward the cathode at different rates.

### The MEKC Retention Factor

The retention factor in MEKC ($k'$) is defined analogously to chromatography:

$$k' = \frac{t_R - t_0}{t_0 \cdot (1 - t_R/t_{mc})}$$

where $t_0$ is the migration time of an unretained marker (EOF marker, typically methanol), $t_{mc}$ is the migration time of the micelle (marked by a hydrophobic dye such as Sudan III), and $t_R$ is the analyte migration time. Neutral analytes elute between $t_0$ (no partitioning into micelles) and $t_{mc}$ (complete partitioning into micelles). For charged peptides, the migration is the sum of electrophoretic and partitioning contributions, providing an additional dimension of selectivity.

### Resolution in MEKC

The resolution equation for MEKC incorporates both chromatographic and electrophoretic contributions:

$$Rs = \frac{\sqrt{N}}{4} \cdot \frac{\alpha - 1}{\alpha} \cdot \frac{k'_2}{1 + k'_2} \cdot \frac{1 - t_0/t_{mc}}{1 + (t_0/t_{mc}) \cdot k'_1}$$

The final term, unique to MEKC, represents the "elution window" — the range of times between $t_0$ and $t_{mc}$ within which neutral analytes can be resolved. A wider elution window (larger $t_{mc}/t_0$ ratio) provides greater resolving power. The elution window can be expanded by: increasing SDS concentration (moderately), adding organic modifiers (which increase $t_{mc}$ by reducing micelle partitioning of the marker), or using polymeric surfactants that cannot be destroyed by organic solvents.

### Applications to Peptide Analysis

MEKC is particularly valuable for peptide separations where the charge difference between closely related species is insufficient for CZE resolution. For example, peptide diastereomers (identical mass and sequence but different stereochemistry at one or more residues) have identical charge and nearly identical hydrodynamic volume, producing no separation in CZE or SDS-PAGE. However, their differential partitioning into micelles, mediated by subtle differences in side-chain exposure, can provide baseline separation in MEKC.

MEKC with chiral surfactants (bile salts, cyclodextrin-modified micelles) enables enantiomeric separation of peptides containing D-amino acids — an important application in peptide drug quality control where racemization during synthesis must be detected and quantified.

## Isoelectric Focusing for pI Determination

### The Theory of Isoelectric Focusing

Isoelectric focusing (IEF) separates peptides based on their isoelectric point (pI) — the pH at which the net charge of the peptide is zero. A pH gradient is established in a gel or capillary using a mixture of carrier ampholytes (low molecular weight polyamino-polycarboxylic acids with closely spaced pI values), and the peptide migrates under the electric field until it reaches the pH region where its net charge is zero.

At the isoelectric point:

$$\sum q_i(pH = pI) = 0$$

where the sum is over all ionizable groups on the peptide: N-terminal amine, C-terminal carboxyl, and side chains of Asp, Glu, His, Cys, Tyr, Lys, and Arg. The theoretical pI of a peptide can be calculated from its amino acid sequence using the Henderson-Hasselbalch equation for each ionizable group, but the agreement between calculated and experimental pI values depends on accurate pKa values for amino acid residues in the peptide context, which can differ from free amino acid values by 0.5–1.0 pH units due to microenvironmental effects.

### Resolution in IEF

The resolution of IEF is determined by the slope of the pH gradient and the diffusion coefficient of the peptide:

$$\Delta(pI) = 3 \sqrt{\frac{D_m \cdot (d(pH)/dx)}{E \cdot (-d\mu_e/d(pH))}}$$

where $d(pH)/dx$ is the pH gradient slope, $E$ is the field strength, and $-d\mu_e/d(pH)$ is the mobility slope at the pI (a measure of how rapidly the peptide's charge changes with pH near its pI). This equation predicts that resolution improves with higher field strengths and shallower pH gradients, explaining why narrow-range immobilized pH gradient (IPG) strips can resolve peptides differing by as little as 0.001 pI units.

### Capillary Isoelectric Focusing (cIEF)

In capillary IEF, the entire capillary is filled with a mixture of sample and carrier ampholytes, and focusing is performed with the capillary ends immersed in anolyte (acid) and catholyte (base). After focusing, the focused zones must be mobilized past the detector — either by pressure (chemical mobilization, adding salt to one electrode reservoir) or by EOF (for uncoated capillaries). cIEF provides rapid (15–30 minute) pI determination with exceptional resolution and minimal sample consumption.

### Peptide-Specific IEF Considerations

Small peptides present unique challenges for IEF. Very small peptides (<2 kDa) may diffuse rapidly from their focused position, compromising resolution. The addition of 5–10% glycerol to the gel or ampholyte solution increases viscosity and reduces diffusion. Peptides with extreme pI values (<3 or >10) may be poorly focused with standard carrier ampholyte mixtures designed for the 3–10 pH range; specialty ampholytes (pH 2.5–5 or pH 9–11) are available for these cases. Hydrophobic peptides may precipitate at their pI, producing artifactual bands or lost signal; the inclusion of non-ionic detergents (0.1% NP-40 or Triton X-100) or 6 M urea helps maintain peptide solubility during focusing.

## Research Evidence

Experimental validation of electrophoretic principles for peptide analysis has been extensive. The table below summarizes key contributions:

| Technique | Peptide System | Key Finding | Reference |
|-----------|---------------|-------------|-----------|
| Tris-tricine SDS-PAGE | Cytochrome c fragments (1–12 kDa) | Resolution of peptides as small as 1 kDa with linear MW-log mobility relationship | Schägger & von Jagow (1987) |
| CZE of peptides | Synthetic model peptides | Optimization of pH and buffer for peptide charge-based separations; theoretical plate counts >500,000 | Grossman et al. (1989) |
| MEKC for peptide separations | Tryptic digest peptides | MEKC resolves neutral and charged peptides simultaneously; orthogonal to RP-HPLC selectivity | Terabe et al. (1989) |
| CE-MS for peptide analysis | Protein digests | CE-MS provides complementary sequence coverage to LC-MS, preferentially detecting hydrophilic peptides | Moini (2007) |
| Capillary IEF for pI | Recombinant protein charge variants | cIEF resolves deamidation variants with ΔpI < 0.05 units; correlation with IEX data | Wu et al. (2001) |
| Ferguson plot analysis | SDS-denatured peptides | Linear log(Rf) vs. %T relationship for SDS-peptide complexes; anomalous migration for Pro-rich sequences | Neville (1971) |
| Joule heating in CE | Model buffer systems | Quantitative model of temperature gradients in CE; optimal capillary diameters for peptide separations | Grushka et al. (1989) |
| CE-LIF for trace peptide detection | Fluorescently labeled peptides | Attomole detection limits for CE with laser-induced fluorescence detection | Kennedy et al. (2001) |

## Current Understanding

Contemporary peptide electrophoresis integrates multiple modalities to provide comprehensive characterization. The complementary nature of slab-gel electrophoresis (visual, semi-quantitative, multiple samples in parallel) and capillary electrophoresis (automated, quantitative, high efficiency, mass spectrometer-compatible) means that both approaches remain essential in the peptide research laboratory.

In analytical method development for peptide therapeutics, electrophoretic methods are increasingly mandated alongside chromatographic methods. The ICH Q6B guideline for biotechnology products specifies that electrophoretic purity should be assessed by at least two orthogonal methods — typically reduced and non-reduced SDS-PAGE, IEF, or CE — with CE-SDS (capillary electrophoresis with SDS) increasingly replacing slab-gel SDS-PAGE in regulated environments due to superior quantitation and automation.

Microchip electrophoresis, where CE channels are fabricated on glass or polymer chips using photolithography, represents a rapidly advancing technology. Microchip CE achieves separations in seconds rather than minutes, consumes picoliter sample volumes, and can integrate sample preparation, separation, and detection on a single platform. For high-throughput peptide screening applications, microchip CE with fluorescence detection offers unparalleled speed and sensitivity.

The combination of CE with mass spectrometry (CE-MS) via electrospray ionization interfaces provides a powerful tool for peptide analysis. CE-MS is particularly effective for highly hydrophilic and multiply charged peptides that are poorly retained on reverse-phase columns, enabling deeper proteome coverage when used as a complement to LC-MS. Sheathless CE-MS interfaces, where the separation capillary itself serves as the electrospray emitter, achieve attomole sensitivity for peptide detection.

## Future Research Directions

- Development of peptide-specific capillary coatings (neutral, cationic, zwitterionic) that eliminate EOF variability and protein adsorption while maintaining high-efficiency separations for basic and hydrophobic peptides
- Integration of microchip CE with tandem mass spectrometry for single-cell peptidomics, enabling characterization of the peptidome from individual cells in heterogeneous tissues
- Application of machine learning to predict peptide electrophoretic mobility from sequence, incorporating contributions from secondary structure, post-translational modifications, and buffer-specific effects
- Development of capillary isoelectric focusing with native mass spectrometry detection, enabling direct pI determination of intact non-covalent peptide complexes without denaturation
- Implementation of multi-dimensional CE-CE systems (e.g., cIEF × CZE) for comprehensive peptide mapping with peak capacities exceeding 10,000
- Design of novel fluorogenic substrates for in-gel detection of specific peptide-modifying enzymes (kinases, proteases, deacetylases) directly after electrophoretic separation
- Advancement of preparative-scale free-flow electrophoresis for continuous purification of synthetic peptide libraries based on charge and size
- Exploration of non-aqueous capillary electrophoresis for analysis of hydrophobic, membrane-active peptides in organic solvent systems
- Integration of microdialysis sampling with online CE analysis for real-time monitoring of extracellular peptide concentrations in vivo
- Development of standardized, quantitative CE-SDS methods for peptide purity assessment that meet ICH Q2(R1) validation requirements for pharmaceutical quality control

## Frequently Asked Questions

!!! info ""
    **About RPL Peptides:** [RPL Peptides](https://rplpeptides.com) provides research-grade peptides with comprehensive analytical characterization. Electrophoretic purity data, including SDS-PAGE and capillary electrophoresis results, are available for appropriate peptide products through the [RPL Peptides Data Center](https://data.rplpeptides.com).

<div class="faq-container">
<div class="faq-section">

<div class="faq-item">
<h3 class="faq-question">Why can't I use standard Laemmli SDS-PAGE for small peptides?</h3>
<p>The standard Laemmli system uses glycine as the trailing ion, which overtakes small peptides (<15 kDa) early in the resolving gel due to its higher mobility at the resolving gel pH. Once overtaken, small peptides migrate in a continuously de-stacking environment, producing diffuse, poorly resolved bands. The Tris-tricine system solves this by replacing glycine with tricine, which has a lower pKa (8.15 vs. 9.6) and larger molecular size, keeping the stacking front behind small peptides throughout the separation. For peptides <5 kDa, the Tris-tricine 16.5% T, 6% C resolving gel is strongly recommended.</p>
</div>

<div class="faq-item">
<h3 class="faq-question">What is electroosmotic flow (EOF) and why is it important in peptide CE?</h3>
<p>Electroosmotic flow is the bulk movement of buffer solution through a capillary driven by the electric field, caused by the ionization of silanol groups on the capillary wall creating a negatively charged surface that attracts a mobile layer of cations. EOF is crucial in CE because it provides a flat, plug-like flow profile (vs. parabolic for pressure-driven flow) that minimizes band broadening, and it can sweep both positively and negatively charged analytes past a single detector. For peptide CE, EOF can be tuned by pH: above pH ~7, EOF is strong and sweeps all peptides to the cathode; below pH ~3, EOF is negligible and only positively charged peptides migrate past the detector. Coatings (neutral polymers) can be used to completely suppress EOF when desired.</p>
</div>

<div class="faq-item">
<h3 class="faq-question">How does MEKC separate neutral peptides that CZE cannot resolve?</h3>
<p>In CZE, neutral analytes all migrate at the EOF velocity and co-elute as a single peak. MEKC introduces SDS micelles as a pseudostationary phase — neutral peptides partition into the hydrophobic micelle interior to varying degrees based on their hydrophobicity. The micelles themselves migrate electrophoretically toward the anode (opposing the cathodic EOF), creating a separation window between the EOF marker ($t_0$) and the micelle marker ($t_{mc}$). Neutral peptides elute between these limits based on their partition coefficient into the micelles, enabling separation of peptides with identical charge states that would be indistinguishable in CZE.</p>
</div>

<div class="faq-item">
<h3 class="faq-question">What is the Ferguson plot and how is it used for peptide molecular weight determination?</h3>
<p>The Ferguson plot is a graph of log(relative mobility, $R_f$) versus gel concentration (%T), generated by running the same peptide sample on multiple SDS-PAGE gels of different acrylamide concentrations. The slope, $K_R$ (retardation coefficient), is proportional to the effective molecular size of the SDS-peptide complex, and the y-intercept, log $Y_0$, relates to the free-solution mobility. For most SDS-denatured peptides, $K_R$ is linearly proportional to log(molecular weight), providing a size estimate. The Ferguson plot can also detect peptides with anomalous SDS binding — sequences with high proline content or unusual charge distributions — which deviate from the standard calibration curve.</p>
</div>

<div class="faq-item">
<h3 class="faq-question">How does Joule heating affect peptide CE separations, and how is it managed?</h3>
<p>Joule heating arises from the electrical power dissipated as heat when current flows through the resistive electrophoresis buffer ($P = VI$). In CE, heat is generated uniformly across the capillary cross-section but dissipates at the wall, creating a parabolic temperature gradient (coolest at the wall, hottest at the center). This gradient produces viscosity and density variations that cause natural convection and band broadening. CE manages Joule heating through small capillary diameters (25–75 μm) that maximize surface-to-volume ratio for heat dissipation, and by using low-conductivity buffers (zwitterionic buffers such as CAPS, Tricine). The Ohm's Law plot (current vs. voltage) is used to identify the onset of significant Joule heating — the linear region represents efficient heat dissipation, and the deviation from linearity signals that cooling is no longer adequate.</p>
</div>

<div class="faq-item">
<h3 class="faq-question">Why do calculated and experimental pI values sometimes differ for peptides?</h3>
<p>Discrepancies between calculated (theoretical) and experimental pI values arise because pKa values of ionizable groups are influenced by the local chemical environment in the folded or partially folded peptide. Neighboring charged residues shift pKa values through electrostatic effects (e.g., a nearby positive charge stabilizes the deprotonated form, lowering the effective pKa), hydrogen bonding to backbone amides alters ionization equilibria, and solvent exposure — buried residues experience a lower effective dielectric constant, shifting pKa values. For small, unstructured peptides, calculated pI values using standard pKa sets (e.g., Expasy ProtParam with the Bjellqvist scale) typically agree within ±0.3 pH units of experimental IEF values. For folded peptides, deviations of 0.5–1.0 pH units are common and reflect the importance of protein context in modulating ionization behavior.</p>
</div>

<div class="faq-item">
<h3 class="faq-question">What are the advantages of capillary electrophoresis over slab-gel electrophoresis for peptide analysis?</h3>
<p>CE offers several advantages: (1) higher efficiency (100,000–500,000 theoretical plates vs. 1,000–5,000 for slab gels) due to the plug-like EOF profile and efficient heat dissipation; (2) automation — CE instruments perform automated injection, separation, detection, and data analysis for unattended runs; (3) quantitative accuracy — UV or fluorescence detection provides direct on-capillary quantitation without staining/destaining variability; (4) speed — separations complete in 5–30 minutes vs. 1–4 hours for slab gels; (5) minimal sample consumption — nL injection volumes vs. μL for slab gels; (6) direct MS coupling via electrospray ionization for online peptide identification. Slab gels retain advantages for parallel analysis of multiple samples and for preparative-scale band excision.</p>
</div>

<div class="faq-item">
<h3 class="faq-question">How do I choose between CZE, MEKC, and cIEF for peptide separation?</h3>
<p>The choice depends on the separation goal: <strong>CZE</strong> is the first choice for separating peptides that differ in charge-to-size ratio — it is the simplest CE mode and provides the highest efficiency. <strong>MEKC</strong> is indicated when peptides have identical or very similar charge-to-size ratios (e.g., diastereomers, neutral peptide derivatives) or when both neutral and charged peptides are present in the same sample. <strong>cIEF</strong> is specifically for determining peptide pI values and for separating charge variants such as deamidation products or phosphorylation isoforms. For comprehensive characterization, combining CZE-MS (for peptide identification and quantitation) with cIEF (for pI determination) provides orthogonal information on peptide identity and quality.</p>
</div>

<div class="faq-item">
<h3 class="faq-question">What causes peptide loss during SDS-PAGE staining, and how can it be prevented?</h3>
<p>Small peptides (<5 kDa) can diffuse out of the polyacrylamide gel matrix during the aqueous steps of staining and destaining because they are not effectively trapped by the gel pores. Prevention strategies include: (1) fixation with 0.5–1% glutaraldehyde or formaldehyde for 30–60 minutes before staining, which covalently cross-links peptides to the gel matrix; (2) using rapid staining protocols (e.g., 1-hour colloidal Coomassie) that minimize aqueous exposure time; (3) reducing the gel thickness (0.5–0.75 mm) to accelerate staining and destaining; (4) using fluorescence stains (SYPRO Ruby) that require minimal destaining; (5) increasing the gel concentration to 20% T for very small peptides to tighten pore size. Some peptide loss is inherent due to the open pore structure required for electrophoresis — alternative techniques such as CE should be considered for quantitative recovery of very small peptides.</p>
</div>

<div class="faq-item">
<h3 class="faq-question">How does the electrokinetic injection bias affect quantitative peptide CE analysis?</h3>
<p>Electrokinetic injection introduces analyte-specific bias because peptides migrate into the capillary at rates proportional to their individual electrophoretic mobilities. More mobile peptides (high charge, small size) are preferentially injected relative to less mobile peptides, distorting the apparent composition of the sample. The magnitude of the bias depends on the injection voltage and time, the buffer conductivity, and the specific mobilities of the analytes. For quantitative work, hydrodynamic injection (pressure-based) is preferred because it introduces a representative aliquot of the sample regardless of analyte mobility. When electrokinetic injection must be used (e.g., for on-capillary sample concentration), internal standards with mobilities matching the analytes of interest are essential for quantitative accuracy.</p>
</div>

</div>
</div>

## References

<ol class="references">
<li>Schägger H, von Jagow G. Tricine-sodium dodecyl sulfate-polyacrylamide gel electrophoresis for the separation of proteins in the range from 1 to 100 kDa. <em>Anal Biochem</em>. 1987;166(2):368-379. doi:10.1016/0003-2697(87)90587-2</li>
<li>Laemmli UK. Cleavage of structural proteins during the assembly of the head of bacteriophage T4. <em>Nature</em>. 1970;227(5259):680-685. doi:10.1038/227680a0</li>
<li>Jorgenson JW, Lukacs KD. Zone electrophoresis in open-tubular glass capillaries. <em>Anal Chem</em>. 1981;53(8):1298-1302. doi:10.1021/ac00231a037</li>
<li>Terabe S, Otsuka K, Ichikawa K, Tsuchiya A, Ando T. Electrokinetic separations with micellar solutions and open-tubular capillaries. <em>Anal Chem</em>. 1984;56(1):111-113. doi:10.1021/ac00265a031</li>
<li>Grossman PD, Colburn JC, Lauer HH, et al. Application of free-solution capillary electrophoresis to the analytical scale separation of proteins and peptides. <em>Anal Chem</em>. 1989;61(11):1186-1194. doi:10.1021/ac00186a004</li>
<li>Weinberger R. <em>Practical Capillary Electrophoresis</em>. 2nd ed. San Diego: Academic Press; 2000.</li>
<li>Righetti PG. <em>Isoelectric Focusing: Theory, Methodology and Applications</em>. Amsterdam: Elsevier; 1983.</li>
<li>Moini M. Capillary electrophoresis mass spectrometry and its application to the analysis of biological mixtures. <em>Anal Bioanal Chem</em>. 2002;373(6):466-480. doi:10.1007/s00216-002-1295-x</li>
<li>Simpson RJ. <em>Proteins and Proteomics: A Laboratory Manual</em>. Cold Spring Harbor: CSHL Press; 2003.</li>
<li>Neville DM. Molecular weight determination of protein-dodecyl sulfate complexes by gel electrophoresis in a discontinuous buffer system. <em>J Biol Chem</em>. 1971;246(20):6328-6334.</li>
<li>Wu J, Li SC, Watson A. Optimizing separation conditions for proteins and peptides in capillary electrophoresis using an experimental design approach. <em>J Chromatogr A</em>. 1998;817(1-2):163-171. doi:10.1016/S0021-9673(98)00426-9</li>
<li>Hjertén S. Free zone electrophoresis. <em>Chromatogr Rev</em>. 1967;9(2):122-219. doi:10.1016/0009-5907(67)80003-6</li>
<li>Dolnik V. Capillary electrophoresis of proteins 2003–2005. <em>Electrophoresis</em>. 2006;27(1):126-141. doi:10.1002/elps.200500567</li>
<li>Righetti PG, Gelfi C. Capillary isoelectric focusing and the determination of isoelectric points of proteins and peptides. <em>J Capillary Electrophor</em>. 1997;4(2):47-59.</li>
<li>Smith RD, Loo JA, Edmonds CG, Barinaga CJ, Udseth HR. New developments in biochemical mass spectrometry: electrospray ionization. <em>Anal Chem</em>. 1990;62(9):882-899. doi:10.1021/ac00208a002</li>
</ol>
