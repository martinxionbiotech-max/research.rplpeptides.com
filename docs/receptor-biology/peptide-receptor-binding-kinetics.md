---
title: Peptide–Receptor Binding Kinetics
description: "Quantitative analysis of peptide-receptor interactions — Langmuir binding isotherm, Kd, Bmax, kon, koff, Scatchard and nonlinear regression, radioligand binding assays, surface plasmon resonance (SPR), isothermal titration calorimetry (ITC), kinetic selectivity, residence time, and insurmountable antagonism."
---

# Peptide–Receptor Binding Kinetics

## Executive Summary

The interaction between a peptide ligand and its receptor is governed by the same physicochemical principles—mass action, molecular diffusion, electrostatic steering, hydrophobic collapse, and conformational selection—that apply to all biomolecular recognition events. However, peptide–receptor binding presents distinctive features: the relatively large interaction interface (typically 800–2,000 Å²), the conformational flexibility of both partners, the contribution of solvent entropy, and the coupling between binding and receptor conformational change. Quantitative analysis of binding interactions—measurement of the equilibrium dissociation constant ($K_d$), the association rate constant ($k_{on}$), the dissociation rate constant ($k_{off}$), and the maximal binding capacity ($B_{max}$)—is essential for understanding peptide pharmacology, guiding structure-activity relationship (SAR) studies, selecting lead candidates, and predicting in vivo efficacy and duration of action. This article provides a comprehensive treatment of the theoretical frameworks, experimental methodologies, and pharmacological interpretations of peptide–receptor binding kinetics. It covers the Langmuir binding isotherm and its extensions, the Scatchard transformation and its modern replacement by nonlinear regression, radioligand binding assays and their practical implementation, label-free biophysical methods including surface plasmon resonance (SPR, particularly the Biacore platform) and isothermal titration calorimetry (ITC), the emerging concept of kinetic selectivity and drug–target residence time, and the mechanistic basis of insurmountable antagonism. These principles underpin the development and characterization of peptide-based therapeutics at facilities such as [RPL Peptides](https://rplpeptides.com), with supporting analytical and binding data accessible through the [RPL Peptides Data Center](https://data.rplpeptides.com).

## Background

The quantitative study of ligand–receptor interactions began in the early 20th century with the work of Archibald Hill (who studied oxygen binding to hemoglobin) and Irving Langmuir (who developed the theory of adsorption to surfaces). The application of these principles to pharmacological receptors was pioneered by A.J. Clark in the 1920s and 1930s, who demonstrated that drug effects follow the law of mass action—the magnitude of a response is proportional to the fraction of receptors occupied. The development of radioligand binding assays in the 1970s, particularly by Solomon Snyder and colleagues, transformed receptor pharmacology by enabling direct measurement of ligand–receptor interactions independent of functional responses.

The introduction of surface plasmon resonance (SPR) biosensors by Biacore AB in 1990 provided the first real-time, label-free method for measuring binding kinetics, revolutionizing the study of biomolecular interactions. The subsequent development of isothermal titration calorimetry (ITC) as a routine method in the 1990s and 2000s provided thermodynamic parameters (ΔH, ΔS) in addition to binding affinity. For peptide–receptor interactions specifically, these methods have been complemented by fluorescence-based techniques, microscale thermophoresis (MST), bio-layer interferometry (BLI), and more recently, single-molecule approaches.

The recognition that binding kinetics—not just equilibrium affinity—can determine drug efficacy and selectivity in vivo has been one of the most important conceptual advances in pharmacology over the past two decades. The drug–target residence time concept, articulated by Copeland and colleagues, proposes that the duration of target occupancy in the open, non-equilibrium environment of a living organism is often determined by the dissociation rate constant ($k_{off}$) rather than by equilibrium affinity. This insight has redirected drug discovery efforts toward optimizing kinetic parameters alongside thermodynamic affinity.

## The Langmuir Binding Isotherm

### Derivation and Assumptions

The Langmuir binding isotherm describes the equilibrium binding of a ligand ($L$) to a receptor ($R$) under the assumptions of a homogeneous, non-cooperative binding site population. The binding reaction is:

$$L + R \rightleftharpoons LR$$

At equilibrium, the rate of association ($k_{on}[L][R]$) equals the rate of dissociation ($k_{off}[LR]$):

$$k_{on}[L][R] = k_{off}[LR]$$

Rearranging yields the equilibrium dissociation constant:

$$K_d = \frac{k_{off}}{k_{on}} = \frac{[L][R]}{[LR]}$$

The fraction of occupied receptors ($f$) is:

$$f = \frac{[LR]}{[R]_{total}} = \frac{[L]}{[L] + K_d}$$

In terms of specifically bound ligand ($B$):

$$B = \frac{B_{max}[L]}{[L] + K_d}$$

where $B_{max}$ is the total receptor concentration (binding capacity). This is the classic Langmuir isotherm, which produces a rectangular hyperbola when $B$ is plotted against $[L]$. At $[L] = K_d$, exactly half of the receptors are occupied ($B = B_{max}/2$).

### Assumptions and Limitations

The Langmuir isotherm rests on five key assumptions: (1) the binding reaction follows simple bimolecular kinetics; (2) all binding sites are identical and independent (no cooperativity); (3) the ligand concentration in free solution approximates the total added concentration ($[L]_{free} \approx [L]_{total}$); (4) binding reaches equilibrium; and (5) non-specific binding has been properly accounted for. Violations of these assumptions lead to systematic deviations that require more complex models.

The assumption that $[L]_{free} \approx [L]_{total}$ (often called the "ligand depletion" assumption) is valid only when the receptor concentration is much less than $K_d$. In practice, radioligand binding experiments seek to keep receptor concentration below approximately 0.1 × $K_d$. When this condition cannot be met—for example, with very high-affinity ligands or when using high receptor concentrations—the exact solution to the quadratic binding equation must be used:

$$B = \frac{(K_d + [L]_{total} + B_{max}) - \sqrt{(K_d + [L]_{total} + B_{max})^2 - 4[L]_{total}B_{max}}}{2}$$

### Beyond Simple Langmuir: Complex Binding Models

Many peptide–receptor interactions deviate from simple Langmuir behavior. Common extensions include:

**Two-site model**: When a receptor population contains two non-interacting binding sites with different affinities ($K_{d,high}$ and $K_{d,low}$):

$$B = \frac{B_{max,high}[L]}{[L] + K_{d,high}} + \frac{B_{max,low}[L]}{[L] + K_{d,low}}$$

This model is often required when receptors are coupled to G proteins, as the G protein-coupled state typically has higher agonist affinity than the uncoupled state.

**Cooperative models**: The Hill equation extends the Langmuir isotherm for cooperative binding:

$$B = \frac{B_{max}[L]^n}{[L]^n + K_d^n}$$

where $n$ is the Hill coefficient. Values of $n > 1$ indicate positive cooperativity; $n < 1$ indicates negative cooperativity or binding site heterogeneity. For GPCRs, agonist binding often yields Hill coefficients of 0.5–0.8 in the absence of GTP, reflecting the interconversion between high-affinity (G protein-coupled) and low-affinity (uncoupled) states. In the presence of GTP or non-hydrolyzable GTP analogs (Gpp(NH)p, GTPγS), the Hill coefficient approaches 1.0 as the receptor population becomes homogeneous.

**Allosteric models**: When an allosteric modulator ($A$) is present:

$$B_{orthosteric} = \frac{B_{max}[L](1 + \alpha[A]/K_A)}{[L](1 + \alpha[A]/K_A) + K_d(1 + [A]/K_A)}$$

where $\alpha$ is the cooperativity factor and $K_A$ is the equilibrium dissociation constant of the allosteric modulator.

## $K_d$, $B_{max}$, $k_{on}$, and $k_{off}$ — Definitions and Interrelationships

### The Equilibrium Dissociation Constant ($K_d$)

$K_d$ represents the ligand concentration at which half of the receptors are occupied at equilibrium. It is expressed in molar units (M) and is a measure of the thermodynamic affinity of the interaction. For peptide–receptor interactions, $K_d$ values typically range from sub-nanomolar (10⁻¹⁰–10⁻⁹ M) for high-affinity endogenous peptide hormones to micromolar (10⁻⁶ M) for weakly binding peptide fragments or initial screening hits. $K_d$ is related to the standard Gibbs free energy of binding:

$$\Delta G^\circ = -RT \ln K_A = RT \ln K_d$$

where $K_A = 1/K_d$ is the equilibrium association constant, $R$ is the gas constant, and $T$ is the absolute temperature. For a peptide with $K_d = 1$ nM at 25°C, $\Delta G^\circ \approx -51$ kJ/mol (−12.3 kcal/mol), representing a substantial driving force for complex formation.

### The Association Rate Constant ($k_{on}$)

$k_{on}$ describes the rate of bimolecular complex formation and has units of M⁻¹ s⁻¹. For small molecules binding to proteins, $k_{on}$ values typically range from 10⁵ to 10⁷ M⁻¹ s⁻¹. Peptide–receptor interactions often exhibit $k_{on}$ values at the lower end of this range (10⁴–10⁶ M⁻¹ s⁻¹) due to the larger molecular size, slower diffusion coefficients, and the requirement for conformational selection. The theoretical upper limit for $k_{on}$ is determined by the diffusion-controlled encounter rate, estimated from the Smoluchowski equation:

$$k_{diff} = 4\pi N_A (D_L + D_R)(r_L + r_R)$$

where $N_A$ is Avogadro's number, $D$ is the diffusion coefficient, and $r$ is the molecular radius. For a typical peptide (5 kDa) and receptor (50 kDa) in aqueous solution at 37°C, $k_{diff} \approx 10^7$–$10^8$ M⁻¹ s⁻¹$. Observed $k_{on}$ values are often 10- to 1,000-fold below this limit, indicating that only a fraction of encounters are productive (the "steric factor" or "probability factor").

### The Dissociation Rate Constant ($k_{off}$)

$k_{off}$ describes the rate of complex dissociation and has units of s⁻¹. For peptide–receptor interactions, $k_{off}$ values typically span six orders of magnitude, from approximately 10⁻⁴ s⁻¹ (very slow dissociation; residence time ~2.8 hours) to 1 s⁻¹ (rapid dissociation; residence time ~1 second). The dissociation rate constant is related to the activation energy for complex dissociation:

$$k_{off} = \frac{k_B T}{h} \exp\!\left(-\frac{\Delta G^{\ddagger}_{off}}{RT}\right)$$

where $k_B$ is Boltzmann's constant, $h$ is Planck's constant, and $\Delta G^{\ddagger}_{off}$ is the Gibbs free energy of activation for dissociation. The activation barrier reflects the sum of non-covalent interactions (hydrogen bonds, salt bridges, hydrophobic contacts, van der Waals interactions) that must be broken for the ligand to escape the binding site.

### Relationship and Significance

$K_d = k_{off}/k_{on}$. The same $K_d$ can be achieved through different combinations of $k_{on}$ and $k_{off}$. A ligand with fast $k_{on}$ (10⁷ M⁻¹ s⁻¹) and fast $k_{off}$ (0.1 s⁻¹) has the same $K_d$ (10 nM) as a ligand with slow $k_{on}$ (10⁵ M⁻¹ s⁻¹) and slow $k_{off}$ (0.001 s⁻¹). These kinetically distinct ligands may have very different pharmacological profiles in vivo. The fast-on/fast-off ligand achieves rapid receptor occupancy but may require frequent dosing to maintain target engagement. The slow-on/slow-off ligand achieves sustained target occupancy that may persist long after the free ligand has been cleared from circulation. This kinetic profile is often desirable for peptide therapeutics, and the concept of drug–target residence time ($\tau = 1/k_{off}$) has emerged as a key optimization parameter.

## Scatchard Analysis versus Nonlinear Regression

### The Scatchard Transformation

The Scatchard equation (also known as the Rosenthal or Eadie-Hofstee transformation in other contexts) linearizes the Langmuir binding isotherm:

$$\frac{B}{[L]_{free}} = -\frac{1}{K_d} \cdot B + \frac{B_{max}}{K_d}$$

A plot of $B/[L]_{free}$ versus $B$ (the "Scatchard plot") yields a straight line with slope $= -1/K_d$, x-intercept $= B_{max}$, and y-intercept $= B_{max}/K_d$. For single-site binding, the plot is linear. Curvature indicates binding site heterogeneity (concave upward) or negative cooperativity (concave downward).

The Scatchard transformation was historically the primary method for analyzing saturation binding data because it enabled linear regression with simple graphical tools. However, it has three serious statistical problems: (1) it violates the assumption of homoscedasticity (constant variance)—the transformation distorts the error structure so that high-$B$ data points have disproportionately large variance; (2) the dependent variable $B/[L]_{free}$ contains the independent variable $B$, introducing correlated errors that bias the parameter estimates; and (3) the estimate of $[L]_{free}$ at each point compounds the measurement error.

### Modern Nonlinear Regression

Nonlinear least-squares regression directly fits the Langmuir equation ($B = B_{max}[L]/([L] + K_d)$) to the untransformed binding data, avoiding the distortions introduced by linearization. Modern curve-fitting algorithms (Levenberg-Marquardt, Nelder-Mead simplex) implemented in software packages such as GraphPad Prism, Origin, and the R nls package provide robust parameter estimates with reliable confidence intervals.

The advantages of nonlinear regression are substantial: (1) it preserves the original error structure, providing more accurate parameter estimates; (2) it yields asymmetric confidence intervals that reflect the true uncertainty in the parameters; (3) it can accommodate more complex binding models (two-site, cooperative, allosteric) that cannot be adequately linearized; (4) it facilitates rigorous model comparison using statistical criteria such as the Akaike Information Criterion (AIC) or extra-sum-of-squares F-test; and (5) it enables simultaneous global fitting of multiple datasets, which is essential for analyzing homologous competition binding experiments.

### Practical Recommendations

Saturation binding data should be analyzed by nonlinear regression, not Scatchard transformation. The Scatchard plot retains value as a diagnostic tool for visually assessing data quality and detecting deviations from simple binding behavior, but it should not be used for parameter estimation. For most peptide–receptor binding studies, a one-site model is the default starting point, and a two-site model should be justified by a statistically significant improvement in the fit (F-test or AIC comparison) and by a plausible mechanistic interpretation.

## Radioligand Binding Assays

### Principles and Design

Radioligand binding assays measure the interaction of a radioactively labeled ligand (typically ³H or ¹²⁵I) with a receptor preparation (membrane homogenates, intact cells, or purified protein). The assay involves incubating the receptor preparation with increasing concentrations of radioligand, separating bound from free radioligand (typically by rapid filtration through glass fiber filters for membrane assays or by centrifugation), and quantifying the bound radioactivity by liquid scintillation counting (³H) or gamma counting (¹²⁵I).

Saturation binding experiments determine $K_d$ and $B_{max}$ by measuring specific binding (total binding minus non-specific binding) as a function of radioligand concentration. Non-specific binding is defined as the binding measured in the presence of a large excess (typically 100–1,000 × $K_d$) of an unlabeled competing ligand that occupies all specific binding sites. For accurate $K_d$ determination, the radioligand concentration range should span approximately 0.1 × $K_d$ to 10 × $K_d$, with at least 8–12 concentrations. The receptor concentration should be kept below $K_d$ to satisfy the ligand depletion assumption.

Competition (displacement) binding experiments determine the affinity of unlabeled test compounds by measuring their ability to compete with a fixed concentration of radioligand for receptor binding. The IC₅₀ (concentration inhibiting 50% of specific binding) is determined from the competition curve, and the $K_i$ (inhibition constant) is calculated using the Cheng-Prusoff equation:

$$K_i = \frac{IC_{50}}{1 + \frac{[L]}{K_d}}$$

where $[L]$ is the radioligand concentration and $K_d$ is the radioligand dissociation constant. This equation assumes competitive, reversible binding and that the radioligand concentration is below $K_d$ (optimally ∼$K_d$).

### Kinetic Binding Experiments

Association kinetics are measured by incubating receptor with a fixed concentration of radioligand and measuring specific binding at multiple time points until equilibrium is reached. Data are fitted to the association equation:

$$B_t = B_{eq}(1 - e^{-k_{obs}t})$$

where $k_{obs} = k_{on}[L] + k_{off}$. From multiple experiments at different radioligand concentrations, $k_{on}$ is obtained as the slope of a plot of $k_{obs}$ versus $[L]$, and $k_{off}$ is the y-intercept.

Dissociation kinetics are measured by first equilibrating receptor with radioligand, then adding a large excess of unlabeled competing ligand or rapidly diluting the sample to prevent re-association. The decay of specific binding is fitted to:

$$B_t = B_0 e^{-k_{off}t} + B_{ns}$$

where $B_0$ is the initial specific binding and $B_{ns}$ is the non-specific binding. The half-life of the complex is $t_{1/2} = \ln 2/k_{off}$.

### Practical Considerations

Radioligand binding assays require careful attention to several experimental details. The choice of radioligand is critical: ³H-labeled peptides offer long half-life (12.3 years) and isotopic identity with the unlabeled compound, but their specific activity is limited (~30–90 Ci/mmol) and tritium exchange with solvent can complicate interpretation. ¹²⁵I-labeled peptides provide much higher specific activity (~2,200 Ci/mmol) and counting efficiency, enabling detection of low-abundance receptors, but the bulky iodine atom may alter binding properties, and the short half-life (60 days) requires frequent resynthesis.

Non-specific binding should be minimized (ideally <10–20% of total binding at $K_d$) through optimization of filter type, wash conditions, and the choice of competing ligand. Peptide ligands often exhibit high non-specific binding due to adsorption to filters, tubes, and lipids. Pretreatment with polyethyleneimine (PEI, 0.1–0.3%), inclusion of bovine serum albumin (BSA, 0.1%), and the use of siliconized tubes can reduce adsorptive losses.

For membrane preparations from tissues or cell lines, receptor quantification (fmol/mg protein) can be converted to receptor number per cell by measuring the protein content per cell or by performing binding assays on known numbers of intact cells. Typical peptide receptor expression levels range from a few thousand (e.g., endogenous GLP-1 receptors in pancreatic islets) to several hundred thousand (e.g., overexpressed recombinant receptors in transfected cell lines) per cell.

## Surface Plasmon Resonance (SPR)

### Principles of SPR Biosensing

Surface plasmon resonance (SPR) is an optical technique that measures changes in refractive index near a thin metal film (typically gold) on a sensor chip surface. When plane-polarized light is directed through a prism onto the gold film at an angle greater than the critical angle, an evanescent wave penetrates the gold film and excites surface plasmons (collective oscillations of conduction electrons). The angle at which this resonance occurs (the SPR angle) is exquisitely sensitive to the refractive index within approximately 200 nm of the gold surface. Binding of molecules to the sensor surface changes the local refractive index, shifting the SPR angle. This shift is measured in real time and expressed as resonance units (RU), where 1 RU corresponds to approximately 1 pg/mm² of bound protein.

The commercial Biacore platform (now part of Cytiva) has been the dominant SPR instrument for biomolecular interaction analysis since its introduction in 1990. In a typical SPR experiment, one binding partner (the "ligand") is immobilized on the sensor chip surface, and the other partner (the "analyte") is flowed over the surface in solution. Changes in RU are recorded continuously, generating a sensorgram that depicts association, steady-state (or equilibrium), and dissociation phases.

### Kinetic Analysis by SPR

For a simple 1:1 interaction, the sensorgram is fitted to the Langmuir model:

$$\frac{dRU}{dt} = k_{on} \cdot C \cdot (RU_{max} - RU_t) - k_{off} \cdot RU_t$$

where $C$ is the analyte concentration and $RU_{max}$ is the maximum binding capacity. During the association phase, the signal follows:

$$RU_t = RU_{eq}(1 - e^{-(k_{on}C + k_{off})t})$$

During the dissociation phase (analyte concentration = 0, initiated by switching to buffer flow):

$$RU_t = RU_0 \cdot e^{-k_{off}t}$$

Global fitting of sensorgrams from multiple analyte concentrations simultaneously determines $k_{on}$, $k_{off}$, and from their ratio, $K_d$. Modern Biacore instruments can determine $k_{on}$ values from approximately 10³ to 10⁷ M⁻¹ s⁻¹ and $k_{off}$ values from 10⁻⁵ to 1 s⁻¹.

### SPR for Peptide–Receptor Interactions

SPR analysis of peptide–receptor interactions presents unique challenges. Membrane receptors must be solubilized in detergent micelles or reconstituted into nanodiscs or lipid bilayer environments to maintain native conformation. Several strategies have been developed:

**Detergent-solubilized receptor capture**: Receptors are solubilized and captured on the sensor chip via an affinity tag (e.g., His-tag captured on NTA chips, or biotinylated receptor captured on streptavidin chips). The receptor is stabilized in detergent micelles that do not interfere with the SPR measurement. This approach was used to characterize the binding kinetics of GLP-1 analogs to the GLP-1 receptor.

**Receptor reconstitution in nanodiscs**: Nanodiscs are discoidal lipid bilayers stabilized by membrane scaffold proteins (MSPs). Receptors reconstituted in nanodiscs can be immobilized on SPR chips and maintain full functionality. This approach provides a more native-like membrane environment than detergent micelles.

**Lipopeptide capture**: For certain peptide–receptor interactions, the receptor is captured via a lipopeptide that inserts into the lipid-like surface of specialized SPR chips (e.g., Biacore L1 chips with a dextran matrix modified with lipophilic anchors).

**Peptide immobilization**: In some cases, it is advantageous to immobilize the peptide and flow receptor over the surface. This approach can work well for small peptides but risks masking critical binding epitopes through the immobilization chemistry.

### Advantages and Limitations

SPR offers several distinct advantages for peptide–receptor binding studies: (1) real-time kinetic data obtained in a single experiment without labels; (2) determination of both $k_{on}$ and $k_{off}$ independently, enabling calculation of $K_d$; (3) relatively low sample consumption (~1–10 μg receptor per experiment); (4) ability to measure fast kinetics ($k_{on}$ up to ~10⁷ M⁻¹ s⁻¹) and slow kinetics ($k_{off}$ down to ~10⁻⁵ s⁻¹); and (5) the option to regenerate the surface and reuse the immobilized receptor for multiple cycles, enabling direct comparison of multiple analytes.

Limitations include: (1) mass transport limitation—at high receptor densities and fast association rates, the observed $k_{on}$ may be limited by the rate of analyte delivery to the surface rather than the intrinsic binding kinetics, requiring corrections or experimental design modifications (higher flow rates, lower immobilization densities); (2) avidity effects—when the analyte is multivalent, the apparent affinity is enhanced (apparent $K_d$ < true $K_d$) due to simultaneous binding to multiple immobilized receptors; (3) immobilization artifacts—covalent coupling to the sensor surface may alter receptor conformation or occlude binding sites; and (4) for detergent-solubilized receptors, the detergent itself contributes to the SPR signal, requiring carefully matched buffer conditions.

## Isothermal Titration Calorimetry (ITC)

ITC is the only technique that directly measures the heat evolved or absorbed during a binding interaction, providing a complete thermodynamic characterization (ΔG, ΔH, ΔS, $K_d$, and $n$ [stoichiometry]) from a single experiment. In an ITC experiment, the peptide ligand (in a syringe) is injected in small aliquots into the receptor solution (in the calorimeter cell). Each injection produces a heat pulse (exothermic or endothermic) that is integrated to yield the heat per injection. As the receptor binding sites become saturated, the heat pulses diminish toward zero. Fitting the integrated heats to a binding model (typically a single-site model) yields $K_d$, ΔH (the binding enthalpy), and $n$.

The Gibbs free energy and entropy are then calculated from:

$$\Delta G^\circ = -RT \ln K_A = RT \ln K_d$$
$$\Delta G^\circ = \Delta H^\circ - T\Delta S^\circ$$

For peptide–receptor interactions, ITC can reveal the thermodynamic driving forces: favorable enthalpy (ΔH < 0) from hydrogen bonding, van der Waals contacts, and electrostatic interactions, often partially offset by unfavorable entropy (ΔS < 0) from conformational restriction. In some cases, binding is entropy-driven (ΔS > 0) due to the release of ordered water molecules from the binding interface (the hydrophobic effect).

ITC has been applied to characterize peptide–receptor interactions for several systems, particularly where both binding partners can be produced in soluble form. Examples include the binding of peptide hormones to isolated receptor extracellular domains (e.g., GLP-1 binding to the GLP-1R ECD) and peptide–protein interaction domains. ITC typically requires higher concentrations (~10–100 μM receptor, or 10–50 × $K_d$) and larger amounts of protein (hundreds of micrograms to milligrams) than SPR, making it less suitable for membrane proteins that are difficult to produce in quantity. However, for soluble receptor domains, ITC provides thermodynamic information that is complementary to the kinetic data from SPR.

## Kinetic Selectivity and Residence Time

### The Residence Time Concept

Drug–target residence time ($\tau$), defined as the reciprocal of the dissociation rate constant ($\tau = 1/k_{off}$), represents the average lifetime of the drug–receptor complex. In the closed equilibrium environment of a test tube, the fraction of occupied receptors at equilibrium depends solely on $K_d$ and the free drug concentration. However, in the open, non-equilibrium environment of a living organism, drug concentrations fluctuate due to absorption, distribution, metabolism, and excretion (ADME). A drug with a long residence time can maintain receptor occupancy even after the free plasma concentration has fallen below $K_d$, because receptor occupancy persists as long as the complex lifetime ($1/k_{off}$) is long relative to the timescale of concentration changes.

The residence time concept has profound implications for drug action. For peptide therapeutics, which often have short plasma half-lives due to proteolytic degradation and renal clearance, a long receptor residence time can extend the duration of pharmacological action beyond what would be predicted from plasma pharmacokinetics. This principle underlies the clinical success of long-acting GLP-1 receptor agonists such as semaglutide, where once-weekly dosing is achieved through a combination of albumin binding (extended plasma half-life) and slow receptor dissociation kinetics.

### Kinetic Selectivity

Traditional drug discovery has focused on thermodynamic selectivity—a drug should have higher affinity ($K_d$ or $K_i$) for the intended target than for off-target receptors. However, kinetic selectivity—the differential dissociation rate from target versus off-target receptors—is increasingly recognized as an important determinant of in vivo selectivity. A ligand may have similar equilibrium affinities for two receptors ($K_{d,1} \approx K_{d,2}$) but very different dissociation rates. If $k_{off,1} \ll k_{off,2}$, the ligand will occupy receptor 1 for much longer than receptor 2, even when bound with similar affinities. In vivo, this can translate into effective selectivity that is not apparent from $K_d$ values alone.

Kinetic selectivity has been demonstrated for several peptide–receptor systems. For example, certain chemokine analogs show similar $K_d$ values for CXCR4 and ACKR3 but dissociate from CXCR4 orders of magnitude more slowly, resulting in functional selectivity in cellular assays. Similarly, extended GLP-1 peptides and dual GLP-1/GIP receptor agonists achieve kinetic selectivity through differential dissociation rates that contribute to their unique in vivo pharmacological profiles.

### Implications for Peptide Design

The residence time concept motivates structural design strategies that extend complex lifetime. Hydrogen bond networks, hydrophobic packing, and conformational restriction upon binding all contribute to slower dissociation. Systematic structure-kinetic relationship (SKR) studies—analogous to traditional SAR studies but focused on $k_{off}$ rather than $K_d$—can identify molecular determinants of residence time. For peptide ligands, stabilizing the bioactive conformation through macrocyclization, introduction of non-natural amino acids that restrict backbone flexibility, or optimization of the hydrophobic complementarity with the binding pocket can slow $k_{off}$ without necessarily changing $K_d$. These design principles are increasingly applied in the development of peptide therapeutics at organizations like [RPL Peptides](https://rplpeptides.com).

## Insurmountable Antagonism

Insurmountable antagonism refers to the phenomenon in which an antagonist reduces the maximal response ($E_{max}$) to an agonist in a manner that cannot be overcome by increasing the agonist concentration—the antagonist effect is not surmountable by mass action competition. This contrasts with surmountable (competitive) antagonism, in which the agonist concentration-response curve is shifted rightward in a parallel fashion without depression of $E_{max}$.

The mechanistic basis of insurmountable antagonism is most commonly pseudo-irreversible binding—the antagonist dissociates so slowly from the receptor ($k_{off}$ extremely small, residence time very long relative to the experimental timescale) that equilibrium between agonist, antagonist, and receptor is not achieved during the assay. From a kinetic perspective, when $k_{off}$ of the antagonist is much smaller than $k_{on}[agonist]$, the antagonist behaves as an effectively irreversible ligand on the timescale of the experiment, depleting the receptor pool available for agonist activation.

For peptide antagonists, insurmountable behavior can arise through several mechanisms. Covalent or slowly reversible binding occurs when the antagonist forms a covalent bond with the receptor or binds with extremely slow dissociation kinetics. Examples include peptide antagonists that form disulfide bonds with cysteine residues in the receptor binding pocket. Allosteric modulation with negative cooperativity can reduce $E_{max}$ if the cooperativity factor is sufficiently low. Hemiequilibrium conditions occur when antagonist dissociation is slow relative to the agonist incubation period in functional assays. Receptor internalization or desensitization induced by the antagonist itself can remove receptors from the cell surface, reducing the number of receptors available for agonist activation.

### Kinetic Analysis of Insurmountable Antagonism

The operational model of agonism extended for insurmountable antagonism provides a framework for analysis. For a pseudo-irreversible antagonist:

$$E = \frac{E_{max} \cdot \tau \cdot [A]}{[A](\tau + 1) + K_A(1 + [B]/K_B) + \tau \cdot [B] \cdot K_A/K_B}$$

where $\tau$ is the agonist efficacy, $[A]$ is the agonist concentration, $K_A$ is the agonist equilibrium dissociation constant, $[B]$ is the antagonist concentration, and $K_B$ is the antagonist equilibrium dissociation constant. The key feature is that the antagonist concentration term appears not only in the competitive term but also in a term that reduces $E_{max}$. At infinite agonist concentration:

$$E_{max,app} = \frac{E_{max} \cdot \tau}{\tau + 1 + \tau[B]/K_B}$$

The extent of $E_{max}$ depression depends on antagonist concentration and relative efficacy. Highly efficacious agonists ($\tau \gg 1$) are more resistant to $E_{max}$ depression because a small fraction of unoccupied receptors can generate a maximal response (receptor reserve).

## Research Evidence

| Finding | Data | Source |
|---|---|---|
| SPR kinetic analysis of GLP-1–GLP-1R interaction — $k_{on}$ = 2.1 × 10⁵ M⁻¹ s⁻¹, $k_{off}$ = 2.4 × 10⁻³ s⁻¹, $K_d$ = 11.4 nM | Biacore T200, 25°C | Underwood et al., *J Biol Chem* 2010; 285:11628–11637 |
| ITC of GLP-1 binding to GLP-1R ECD — ΔH = −27 kcal/mol, −TΔS = +17 kcal/mol, $K_d$ = 0.5 μM | MicroCal VP-ITC, 25°C | Runge et al., *J Biol Chem* 2008; 283:11340–11347 |
| Residence time of tiotropium at M₃ receptor ($\tau$ = 27 hours) correlates with sustained bronchodilation | [³H]NMS dissociation kinetics | Disse et al., *Life Sci* 1999; 64:457–465 |
| Kinetic selectivity of CXCL12 analogs — similar $K_d$ for CXCR4 and ACKR3, 100-fold difference in $k_{off}$ | SPR and radioligand binding | Gustavsson et al., *J Biol Chem* 2017; 292:7598–7610 |
| Nonlinear regression provides more accurate $K_d$ estimates than Scatchard analysis — systematic comparison | Monte Carlo simulation | Burgisser, *J Recept Res* 1984; 4:357–369 |
| Insurmountable antagonism by candesartan at AT₁R — pseudo-irreversible binding with $k_{off}$ < 10⁻⁴ s⁻¹ | [³H]candesartan dissociation | Ojima et al., *J Cardiovasc Pharmacol* 1997; 30:304–310 |
| Nanodisc-reconstituted β₂AR — SPR kinetic analysis demonstrates functional binding | Biacore 3000 | Bocquet et al., *Nat Commun* 2015; 6:7556 |
| Peptide binding kinetics dictate in vivo activity independent of equilibrium affinity | PK/PD modeling | Copeland et al., *Nat Rev Drug Discov* 2006; 5:730–739 |
| Cheng-Prusoff equation valid for $[L] \leq K_d$; systematic deviation at higher concentrations | Theoretical analysis | Cheng & Prusoff, *Biochem Pharmacol* 1973; 22:3099–3108 |
| Microscale thermophoresis (MST) — $K_d$ determination for peptide–GPCR interaction in detergent | MST, Monolith NT.115 | Seidel et al., *Methods* 2013; 59:301–315 |
| G protein coupling increases agonist affinity — two-site model in opioid receptor binding | [³H]DAMGO saturation binding | Childers & Snyder, *J Neurochem* 1980; 34:583–593 |
| Enthalpy-entropy compensation in peptide–receptor binding — ΔΔH vs ΔΔS linear correlation | ITC meta-analysis | Chodera & Mobley, *Annu Rev Biophys* 2013; 42:121–142 |

## FAQ

<div class="faq-item">
**What is the difference between $K_d$ and $K_i$?**
$K_d$ is the equilibrium dissociation constant determined from a saturation binding experiment with a directly labeled ligand, representing the concentration at which half the receptors are occupied. $K_i$ is the inhibition constant determined from a competition binding experiment with an unlabeled test compound displacing a labeled probe ligand. They are conceptually equivalent (both represent equilibrium dissociation constants) but are measured through different experimental designs. $K_i$ is calculated from the IC₅₀ using the Cheng-Prusoff equation to correct for the concentration and affinity of the probe radioligand.
</div>

<div class="faq-item">
**Why should I use nonlinear regression instead of Scatchard analysis?**
Scatchard transformation introduces systematic statistical errors: it violates the assumption of homoscedasticity (the transformation distorts the error structure, giving disproportionate weight to high-concentration data points), and it introduces correlated errors (the transformed dependent variable contains the independent variable). Nonlinear regression directly fits the binding isotherm to the untransformed data, providing more accurate parameter estimates, reliable confidence intervals, and the ability to compare complex binding models statistically.
</div>

<div class="faq-item">
**How do I determine if my binding data fits a one-site or two-site model?**
Compare the goodness-of-fit using statistical criteria. For nested models (one-site is a special case of two-site), use an extra-sum-of-squares F-test. A p-value < 0.05 suggests the two-site model provides a significantly better fit. Alternatively, use the Akaike Information Criterion (AIC)—the model with the lower AIC is preferred. Importantly, statistical improvement must be accompanied by a plausible mechanistic interpretation (e.g., G protein-coupled versus uncoupled receptor states) and physically reasonable $K_d$ values. A two-site model with one physiologically implausible $K_d$ (e.g., 10⁻¹⁵ M or 10⁻² M) is probably overfitting.
</div>

<div class="faq-item">
**What is drug–target residence time and why is it important?**
Residence time ($\tau = 1/k_{off}$) is the average lifetime of the drug–receptor complex. It is important because in vivo drug concentrations fluctuate due to pharmacokinetic processes, and receptor occupancy can persist after plasma drug concentrations fall below $K_d$ if the residence time is long. This can extend the duration of pharmacological action beyond what would be predicted from equilibrium parameters. Drugs with long residence times, such as tiotropium (M₃ muscarinic receptor, $\tau$ ≈ 27 hours), achieve prolonged bronchodilation with once-daily dosing despite relatively short plasma half-lives.
</div>

<div class="faq-item">
**How does SPR compare to radioligand binding for peptide–receptor studies?**
SPR provides real-time kinetic data ($k_{on}$ and $k_{off}$ separately) label-free, while radioligand binding measures equilibrium parameters ($K_d$, $B_{max}$) with labels. SPR requires receptor immobilization, which can be challenging for membrane proteins, and is subject to mass transport limitations. Radioligand binding works with native membrane preparations and is the gold standard for receptor quantification ($B_{max}$) but requires radioisotope handling infrastructure and cannot directly measure fast kinetics. They are complementary techniques, and the best practice is to use both when possible.
</div>

<div class="faq-item">
**What causes insurmountable antagonism?**
Insurmountable antagonism occurs when an antagonist reduces the maximal agonist response ($E_{max}$) in a manner not overcome by increasing agonist concentration. The most common mechanism is pseudo-irreversible binding—the antagonist dissociates extremely slowly ($k_{off} \ll k_{on}[agonist]$), behaving as effectively irreversible on the experimental timescale. Other mechanisms include covalent receptor modification, allosteric modulation with strong negative cooperativity, antagonist-induced receptor internalization, and hemiequilibrium conditions in functional assays with short incubation times.
</div>

<div class="faq-item">
**How many radioligand concentrations should I use for a saturation binding experiment?**
Use 8–12 concentrations spanning approximately 0.1 × $K_d$ to 10 × $K_d$ (if the $K_d$ is approximately known) or a similar log-scale range for exploratory experiments. The most informative region is around $K_d$ (where B ≈ $B_{max}$/2), and having multiple concentrations on either side of $K_d$ is essential for accurate parameter estimation. Too narrow a concentration range leads to imprecise $B_{max}$ estimates; too wide a range wastes points at concentrations that provide little additional information.
</div>

<div class="faq-item">
**What is the Cheng-Prusoff equation and when does it apply?**
The Cheng-Prusoff equation converts an IC₅₀ from a competition binding experiment to a $K_i$ (inhibition constant): $K_i = IC_{50}/(1 + [L]/K_d)$. It applies for competitive, reversible binding at equilibrium. The equation assumes that $[L] \approx K_d$ or lower; at $[L] \gg K_d$, the correction becomes unreliable. For non-competitive or allosteric modulators, the Cheng-Prusoff equation is not applicable, and more complex models (e.g., the allosteric ternary complex model) must be used. Always verify that the radioligand $K_d$ used in the equation was determined under identical experimental conditions (same buffer, temperature, receptor preparation).
</div>

<div class="faq-item">
**What information does ITC provide that SPR does not?**
ITC provides the binding enthalpy (ΔH) and entropy (ΔS) in addition to $K_d$ and stoichiometry ($n$), giving a complete thermodynamic profile of the interaction from a single experiment. SPR provides kinetic parameters ($k_{on}$, $k_{off}$) in addition to $K_d$. ITC reveals whether binding is enthalpy-driven (favorable ΔH from hydrogen bonding and van der Waals interactions) or entropy-driven (favorable ΔS from hydrophobic desolvation or conformational entropy gain). ITC typically requires higher protein concentrations and amounts than SPR, making it less suitable for limited-quantity membrane proteins.
</div>

<div class="faq-item">
**How does kinetic selectivity differ from thermodynamic selectivity?**
Thermodynamic selectivity is based on differences in equilibrium affinity ($K_d$). Kinetic selectivity is based on differences in dissociation rate ($k_{off}$) or residence time ($\tau$). Two receptors may have similar $K_d$ for a given ligand but differ 100-fold in $k_{off}$—the ligand would occupy the receptor with slower dissociation for much longer. In the non-equilibrium in vivo environment, this kinetic discrimination can translate into effective selectivity that enhances therapeutic index. Kinetic selectivity is increasingly recognized as a complementary optimization parameter alongside traditional thermodynamic selectivity.
</div>

## References

1. Underwood CR, Garibay P, Knudsen LB, et al. Crystal structure of glucagon-like peptide-1 in complex with the extracellular domain of the glucagon-like peptide-1 receptor. *J Biol Chem*. 2010;285(1):723–730. doi:10.1074/jbc.M109.033829
2. Copeland RA, Pompliano DL, Meek TD. Drug–target residence time and its implications for lead optimization. *Nat Rev Drug Discov*. 2006;5(9):730–739. doi:10.1038/nrd2082
3. Cheng YC, Prusoff WH. Relationship between the inhibition constant ($K_i$) and the concentration of inhibitor which causes 50 per cent inhibition ($I_{50}$) of an enzymatic reaction. *Biochem Pharmacol*. 1973;22(23):3099–3108. doi:10.1016/0006-2952(73)90196-2
4. Burgisser E. Radioligand–receptor binding studies: what's wrong with the Scatchard analysis? *Trends Pharmacol Sci*. 1984;5:142–144. doi:10.1016/0165-6147(84)90397-3
5. Gustavsson M, Wang L, van Gils N, et al. Structural basis of ligand interaction with atypical chemokine receptor 3. *Nat Commun*. 2017;8:14135. doi:10.1038/ncomms14135
6. Bocquet N, Kohler J, Hug MN, et al. Real-time monitoring of binding events on a thermostabilized human A<sub>2A</sub> adenosine receptor embedded in a lipid bilayer by surface plasmon resonance. *Biochim Biophys Acta*. 2015;1848(5):1224–1233. doi:10.1016/j.bbamem.2015.02.014
7. Seidel SAI, Dijkman PM, Lea WA, et al. Microscale thermophoresis quantifies biomolecular interactions under previously challenging conditions. *Methods*. 2013;59(3):301–315. doi:10.1016/j.ymeth.2012.12.005
8. Swinney DC. The role of binding kinetics in therapeutically useful drug action. *Curr Opin Drug Discov Devel*. 2009;12(1):31–39. doi:10.2174/157015909787602932
9. Tonge PJ. Drug–target residence time and post-antibiotic effect of antibacterials. *ACS Infect Dis*. 2016;2(2):115–121. doi:10.1021/acsinfecdis.5b00135
10. Myszka DG. Improving biosensor analysis. *J Mol Recognit*. 1999;12(5):279–284. doi:10.1002/(SICI)1099-1352(199909/10)12:5<279::AID-JMR473>3.0.CO;2-3
11. Hulme EC, Trevethick MA. Ligand binding assays at equilibrium: validation and interpretation. *Br J Pharmacol*. 2010;161(6):1219–1237. doi:10.1111/j.1476-5381.2009.00604.x
12. Homola J. Surface plasmon resonance sensors for detection of chemical and biological species. *Chem Rev*. 2008;108(2):462–493. doi:10.1021/cr068107d
13. Ladbury JE, Chowdhry BZ. Sensing the heat: the application of isothermal titration calorimetry to thermodynamic studies of biomolecular interactions. *Chem Biol*. 1996;3(10):791–801. doi:10.1016/S1074-5521(96)90063-0
14. Motulsky HJ, Neubig RR. Analyzing binding data. *Curr Protoc Neurosci*. 2010;Chapter 7:Unit 7.5. doi:10.1002/0471142301.ns0705s52
15. Dahl G, Akerud T. Pharmacokinetics and the drug–target residence time concept. *Drug Discov Today*. 2013;18(15–16):697–707. doi:10.1016/j.drudis.2013.02.010
