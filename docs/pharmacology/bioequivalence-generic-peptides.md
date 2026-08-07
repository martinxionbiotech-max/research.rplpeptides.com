---
title: Bioequivalence and Generic Peptide Development
description: Comprehensive guide to bioequivalence study design for peptide generics including ANDA/505(b)(2) pathways, AUC/Cmax metrics, 90% confidence intervals, and FDA/EMA guidance on peptide-specific challenges including immunogenicity and aggregate characterization.
---

# Bioequivalence and Generic Peptide Development: ANDA/505(b)(2) Pathways, Study Design, and Peptide-Specific Challenges

## Executive Summary

Bioequivalence (BE) is the regulatory cornerstone for approving generic drug products, including synthetic peptide therapeutics. A generic peptide is considered bioequivalent to its reference listed drug (RLD) when the rate and extent of absorption of the active ingredient do not show a significant difference under appropriately designed study conditions. For generic peptide products, demonstrating BE presents unique scientific challenges that distinguish these macromolecules from conventional small-molecule generics: the need to characterize higher-order structure, assess immunogenicity risk with appropriate bridging studies, control aggregate formation, and establish peptide-related impurity comparability. This comprehensive review examines the standard BE study design framework, the pharmacokinetic endpoints (AUC, Cmax, Tmax) and their statistical analysis using the 90% confidence interval approach with bioequivalence limits of 80–125%, the ANDA and 505(b)(2) regulatory pathways, and the peptide-specific challenges that regulatory agencies including the FDA and EMA have identified through guidance documents and product-specific recommendations. At [RPL Peptides](https://rplpeptides.com), these regulatory-scientific principles inform every aspect of generic peptide development, from analytical characterization through clinical BE study execution. Reference data and peptide-specific BE study results are curated at [data.rplpeptides.com](https://data.rplpeptides.com).

| BE Parameter | Definition | Acceptance Criteria |
|---|---|---|
| AUC(0–t) | Area under the concentration-time curve to last measurable time point | 90% CI within 80–125% |
| AUC(0–∞) | Extrapolated AUC to infinity | 90% CI within 80–125% |
| Cmax | Peak plasma concentration | 90% CI within 80–125% |
| Tmax | Time to reach Cmax | No formal CI requirement; descriptive comparison |
| λz (Kel) | Terminal elimination rate constant | Supporting evidence |

## Background

### The Regulatory Imperative for Bioequivalence

The concept of bioequivalence emerged from the recognition that pharmaceutical equivalence—identical active ingredient, dosage form, route of administration, and strength—does not guarantee therapeutic equivalence. Differences in formulation, manufacturing process, and excipient composition can alter the in vivo drug release and absorption, potentially affecting clinical efficacy and safety. Bioequivalence studies bridge this gap by providing pharmacokinetic evidence that the test and reference products exhibit comparable systemic exposure profiles.

The regulatory framework for generic drug approval in the United States was fundamentally shaped by the Drug Price Competition and Patent Term Restoration Act of 1984 (the Hatch-Waxman Amendments), which created the Abbreviated New Drug Application (ANDA) pathway. Under this pathway, generic applicants are not required to submit independent preclinical and clinical safety and efficacy data. Instead, they must demonstrate that their product is bioequivalent to the innovator's product and meets the same manufacturing quality standards. This paradigm has successfully enabled market access for thousands of generic small-molecule drugs while maintaining rigorous scientific and regulatory standards.

### The Emergence of Generic Peptides

Peptide therapeutics occupy a unique position in the generic drug landscape. Historically, many peptide products were approved as New Drug Applications (NDAs) under Section 505(b)(1) of the Federal Food, Drug, and Cosmetic Act, despite their macromolecular character. Unlike biologics approved under the Public Health Service Act (which are subject to the Biologics Price Competition and Innovation Act pathway for biosimilars), these peptide NDAs can be referenced in ANDAs—provided the generic applicant can demonstrate that the peptide active ingredient is the "same" as the reference product and that differences in formulation do not affect bioequivalence.

The FDA's evolving position on which peptides qualify as "drugs" (eligible for ANDA referencing) versus "biological products" (requiring a Biologics License Application) has been shaped by statutory changes, notably the Biologics Price Competition and Innovation Act of 2009 and the Further Consolidated Appropriations Act of 2020, which amended the definition of a "biological product" to include chemically synthesized polypeptides. The transition of certain peptide products from drug to biologic status has substantial regulatory implications for generic development strategies.

At [RPL Peptides](https://rplpeptides.com), navigating this evolving regulatory landscape requires continuous engagement with FDA and EMA guidance documents, product-specific bioequivalence recommendations, and the latest scientific literature on peptide characterization and immunogenicity assessment.

## Bioequivalence Study Design

### Standard Study Design Elements

The gold-standard bioequivalence study design is the randomized, single-dose, two-treatment, two-period, two-sequence crossover study conducted in healthy adult volunteers under fasting conditions. Key elements include:

**Study Population:** Typically 24–36 healthy adult volunteers (male and female) who meet inclusion and exclusion criteria designed to minimize variability unrelated to product performance. Inclusion criteria generally specify: age 18–55 years, body mass index 18.5–30.0 kg/m², normal findings on physical examination and clinical laboratory tests, and no history of significant medical conditions. Exclusion criteria include: use of prescription or over-the-counter medications within defined washout periods, history of drug or alcohol abuse, smoking, and known hypersensitivity to the drug class. For some peptide products with specific safety considerations, studies may be conducted in patients rather than healthy volunteers.

**Washout Period:** A minimum washout interval of at least five half-lives of the drug separates the two treatment periods, ensuring complete elimination of the first dose before the second treatment period begins. For peptide drugs with half-lives measured in days or weeks (e.g., long-acting GLP-1 receptor agonists with half-lives of approximately 7 days), parallel-group designs may be employed rather than crossover designs, as the washout requirements would be impractically long.

**Standardization:** Study conditions are tightly controlled to minimize variability: subjects fast overnight (≥10 hours) before dosing and for at least 4 hours post-dose; standardized meals are provided at specified times; water intake is regulated; physical activity is restricted; and concomitant medications, alcohol, caffeine, and grapefruit products are prohibited throughout the study confinement period.

**Sampling Schedule:** Blood samples for pharmacokinetic analysis are collected at pre-dose and at sufficiently frequent intervals post-dose to adequately characterize the absorption, distribution, and elimination phases. The sampling schedule should capture: the pre-dose baseline, the ascending portion of the concentration-time curve (with sufficient density to accurately estimate Cmax), the peak region, the distribution phase, and the terminal elimination phase. For most peptide products, sampling extends to at least three terminal half-lives or until the concentration falls below the lower limit of quantification (LLOQ). Typical sampling schedules include 12–20 time points, with more frequent sampling during the absorption phase.

### Fed vs. Fasting Studies

For oral peptide formulations or peptide products whose absorption may be affected by food, a food-effect bioavailability study is typically required in addition to the fasting BE study. The food-effect study employs the same crossover design but administers the drug product after a standardized high-fat, high-calorie meal (approximately 800–1,000 calories, with 50% from fat). The FDA's guidance on food-effect bioavailability studies specifies the meal composition and timing: the meal should be consumed within 30 minutes, and drug administration should occur 30 minutes after the start of the meal.

### Multi-Dose and Steady-State Studies

For modified-release peptide formulations or peptide drugs intended for chronic administration where single-dose BE may not adequately predict therapeutic equivalence, steady-state bioequivalence studies may be required. In these studies, the test and reference products are administered repeatedly (typically for at least five half-lives) to achieve steady-state conditions, and pharmacokinetic parameters are measured over a dosing interval at steady state. The parameters of interest include: AUC(0–τ) (area under the concentration-time curve during a dosing interval at steady state), Cmax(ss) (maximum concentration at steady state), Cmin(ss) (minimum concentration at steady state), and the degree of fluctuation. Steady-state studies are more complex, longer in duration, and more expensive than single-dose studies, but they may be necessary when:

1. The peptide drug exhibits nonlinear (dose-dependent) pharmacokinetics
2. Single-dose studies cannot adequately characterize the pharmacokinetic profile due to assay sensitivity limitations
3. The peptide produces significant enzyme induction or auto-inhibition that alters its own clearance over time
4. The therapeutic indication requires assessment of steady-state trough concentrations for safety monitoring

## Pharmacokinetic Endpoints: AUC, Cmax, and Supporting Parameters

### Primary Pharmacokinetic Parameters

The FDA and EMA recognize three primary pharmacokinetic parameters for bioequivalence assessment:

**AUC(0–t) — Area Under the Concentration-Time Curve to the Last Measurable Time Point:** AUC(0–t) quantifies the total systemic exposure over the sampling period and reflects the extent of absorption. It is calculated using the linear trapezoidal rule (linear interpolation between adjacent concentration-time points). For bioequivalence purposes, AUC(0–t) is preferred over AUC(0–∞) when the extrapolated area exceeds 20% of the total AUC, as this indicates that the sampling duration was insufficient to adequately characterize the elimination phase.

**AUC(0–∞) — Area Under the Curve Extrapolated to Infinity:** AUC(0–∞) = AUC(0–t) + C(last) / λz, where C(last) is the last measurable concentration and λz is the terminal elimination rate constant. This parameter requires reliable estimation of λz, which in turn depends on an adequate number of concentration-time points in the terminal log-linear phase (at least three points, preferably more). The extrapolated portion should represent ≤20% of AUC(0–∞) for the parameter to be considered reliable.

**Cmax — Peak (Maximum) Plasma Concentration:** Cmax is the observed maximum concentration, taken directly from the concentration-time data without interpolation. It reflects the rate of absorption and is particularly important for drugs where the rate of rise in concentration correlates with onset of effect or safety concerns. Cmax is inherently more variable than AUC because it is determined by a single time point and is sensitive to the timing of blood sampling relative to the true peak.

### Secondary Pharmacokinetic Parameters

Secondary parameters provide additional characterization of the pharmacokinetic profile:

**Tmax — Time to Reach Peak Concentration:** Tmax is a discrete variable reflecting the time at which Cmax occurs. Formal statistical testing of Tmax is not required for BE determination, but differences in median Tmax between test and reference products are assessed descriptively. A substantial shift in Tmax may indicate formulation differences affecting the absorption rate.

**λz (Kel) — Terminal Elimination Rate Constant:** λz is estimated by log-linear regression of the terminal portion of the concentration-time curve. It is used to calculate the terminal half-life (t½ = ln(2) / λz) and to extrapolate AUC to infinity. λz should be estimated from at least three points in the terminal phase, and the regression should have a coefficient of determination (R²) of ≥0.80.

**t½ — Terminal Elimination Half-Life:** t½ = ln(2) / λz. While not a primary BE parameter, half-life provides important mechanistic information about drug clearance. Discrepancies in half-life between test and reference products may indicate differences in absorption kinetics (flip-flop kinetics), formulation-dependent elimination, or artifacts from inadequate sampling.

### Peptide-Specific Considerations for PK Parameters

Peptide drugs present unique challenges for pharmacokinetic parameter estimation:

**Immunoassay vs. LC-MS/MS Quantification:** Peptide concentrations in biological matrices can be measured by immunoassays (ELISA, ECL) or liquid chromatography-tandem mass spectrometry (LC-MS/MS). Immunoassays may detect both intact peptide and cross-reactive metabolites, potentially overestimating active drug concentrations. LC-MS/MS methods can distinguish between the intact peptide and its metabolites but require more extensive method development. The choice of analytical method can substantially affect BE study outcomes—two products that appear bioequivalent by immunoassay may show significant differences when analyzed by a specific LC-MS/MS method that distinguishes active drug from inactive metabolites.

**Anti-Drug Antibody Interference:** The formation of anti-drug antibodies (ADAs) can interfere with both immunoassay- and LC-MS/MS-based quantification of peptide drugs. ADAs may neutralize the biological activity of the peptide, alter its clearance (either accelerating clearance through immune complex formation or prolonging half-life through FcRn-mediated recycling of ADA-peptide complexes), or interfere with the analytical assay. ADA assessment is an important component of BE study design for peptide products, particularly those with known immunogenic potential or those intended for chronic administration.

**Endogenous Peptide Levels:** For peptide drugs that are analogs of endogenous hormones (e.g., insulin, GLP-1 analogs), baseline correction is necessary when the analytical method does not distinguish between the endogenous peptide and the exogenous drug. This requires collection of pre-dose baseline samples and subtraction of endogenous levels from post-dose concentrations. The assumption underlying this correction—that endogenous levels remain constant throughout the study period—may not hold if the exogenous peptide suppresses endogenous production through feedback inhibition (e.g., exogenous GLP-1 analogs suppressing endogenous GLP-1 secretion).

## Statistical Analysis: The 90% Confidence Interval Approach

### The Two One-Sided Tests (TOST) Procedure

Bioequivalence is established using the Two One-Sided Tests (TOST) procedure, which is operationally equivalent to the 90% confidence interval approach. The test and reference products are considered bioequivalent if the 90% confidence interval for the geometric mean ratio (test/reference) of the primary PK parameters (AUC and Cmax) falls entirely within the bioequivalence limits of 80–125%.

The null and alternative hypotheses for the TOST procedure are:

**H₀₁:** μT / μR ≤ θ₁ (test is not equivalent because it is too low)
**H₀₂:** μT / μR ≥ θ₂ (test is not equivalent because it is too high)
**Hₐ₁:** μT / μR > θ₁ AND Hₐ₂: μT / μR < θ₂ (test is equivalent to reference)

where θ₁ = 0.80 and θ₂ = 1.25 (on the original scale), which correspond to ln(θ₁) = −0.2231 and ln(θ₂) = +0.2231 on the log scale.

The TOST procedure requires that both one-sided tests be statistically significant at α = 0.05, which is equivalent to the 90% confidence interval lying within the acceptance range. The use of 90% (rather than 95%) confidence intervals reflects the regulatory standard that BE studies control the consumer risk (Type I error, probability of falsely concluding bioequivalence) at 5% while accepting a somewhat higher producer risk.

### Logarithmic Transformation

Pharmacokinetic parameters AUC and Cmax are analyzed after logarithmic (natural log) transformation. The justifications for log-transformation include:

1. **Biological rationale:** Pharmacokinetic parameters are fundamentally related to physiological processes that operate multiplicatively rather than additively. For example, clearance determines AUC through the relationship AUC = Dose / CL, making AUC a ratio variable.

2. **Statistical rationale:** Pharmacokinetic data are typically positively skewed (right-skewed) with variance proportional to the mean (heteroscedasticity). Log-transformation normalizes the distribution and stabilizes the variance, satisfying the assumptions of the linear statistical model.

3. **Regulatory rationale:** The 80–125% acceptance range on the original scale becomes symmetric on the log scale (ln(0.80) = −0.2231, ln(1.25) = +0.2231), reflecting the pharmacological principle that differences in systemic exposure are proportional rather than absolute.

### Analysis of Variance (ANOVA) Model

The statistical model for a standard two-period crossover BE study includes: sequence, subjects nested within sequence, period, and treatment as fixed effects. The model is:

**Y(ijk) = μ + S(i) + P(j) + T(k) + ε(ijk)**

where Y(ijk) is the log-transformed PK parameter, μ is the overall mean, S(i) is the sequence effect, P(j) is the period effect, T(k) is the treatment effect, and ε(ijk) is the residual error. The subject(sequence) term accounts for between-subject variability, and the residual error accounts for within-subject variability.

The 90% confidence interval for the geometric mean ratio (test/reference) is calculated as:

**90% CI = exp[(μ̂T − μ̂R) ± t(0.05, df) × SE(μ̂T − μ̂R)]**

where μ̂T and μ̂R are the least-squares means for the test and reference treatments (on the log scale), t(0.05, df) is the upper 5% critical value of the t-distribution with df degrees of freedom (typically df = n − 2 for a crossover study with n subjects), and SE is the standard error of the difference.

### Highly Variable Drugs and Reference-Scaled Average Bioequivalence

The standard BE approach (average bioequivalence, ABE) requires that the 90% CI for the test/reference ratio falls within 80–125%. For highly variable drugs, defined as those with within-subject coefficient of variation (CVw) ≥30% for Cmax or AUC, this requirement may be unattainable even for a test product that is truly equivalent to the reference, because the wide confidence intervals reflect high variability rather than product differences. This is particularly problematic when the reference product itself exhibits high variability.

To address this challenge, the FDA and EMA have adopted reference-scaled average bioequivalence (RSABE) approaches for highly variable drugs. Under RSABE, the bioequivalence limits are widened as a function of the reference product variability, using a scaled criterion:

**(μ̂T − μ̂R)² − θ × σ²(WR) ≤ 0**

where σ²(WR) is the within-subject variance of the reference product (on the log scale) and θ is a regulatory constant (θ = [ln(1.25)/σ(W0)]², with σ(W0) = 0.25 as the regulatory switching variability). This approach maintains the scientific principle that products should not be required to demonstrate tighter equivalence than the reference product can demonstrate against itself, while still ensuring that the absolute difference in means does not exceed a clinically relevant margin.

### Peptide Variability Considerations

Peptide drugs present specific statistical challenges for BE evaluation:

**Within-Subject Variability:** The within-subject variability of peptide pharmacokinetic parameters can be substantial (CVw = 20–40% for Cmax, 15–30% for AUC in some peptide products). This variability arises from: injection site variability (for subcutaneously administered peptides), variable lymphatic absorption, diurnal variation in endogenous peptide levels (when baseline correction is imperfect), and variable rates of proteolytic degradation in subcutaneous tissue. Products with CVw ≥30% for Cmax may benefit from the RSABE approach if the reference product also exhibits high variability.

**Sample Size Requirements:** The sample size for a BE study must be sufficient to achieve adequate statistical power (typically ≥80%) to demonstrate BE, given the expected test/reference geometric mean ratio and the within-subject variability. For a standard design with expected geometric mean ratio = 0.95, within-subject CV = 25%, and power = 80%, approximately 28 subjects are required for a crossover study. Higher variability or a geometric mean ratio further from 1.0 increases the required sample size substantially. Peptide BE studies with high variability may require 40–60 subjects or more.

**Outlier Handling:** Single extreme observations in BE studies (outliers) can substantially influence the results, particularly for Cmax, which is a single-point observation sensitive to irregular absorption events. The FDA recommends that outlier analysis should be performed, but outliers should not be routinely excluded. Exclusion of outliers requires a documented medical or procedural reason (e.g., vomiting within the dosing interval, protocol deviation) and should be pre-specified in the statistical analysis plan.

## Regulatory Pathways: ANDA and 505(b)(2)

### The ANDA Pathway (505(j))

The Abbreviated New Drug Application (ANDA) pathway, established under Section 505(j) of the FD&C Act, is the primary route for generic drug approval in the United States. The key requirements for an ANDA are:

**Pharmaceutical Equivalence:** The generic product must contain the same active ingredient(s), in the same dosage form, at the same strength, and for the same route of administration as the reference listed drug (RLD). For solid oral dosage forms, the ANDA must also demonstrate that the product is manufactured according to the same standards as the RLD.

**Bioequivalence:** The generic product must be shown to be bioequivalent to the RLD through an appropriate bioequivalence study (or a biowaiver, if applicable).

**Manufacturing Quality:** The ANDA must include a complete Chemistry, Manufacturing, and Controls (CMC) section demonstrating that the generic product is manufactured under current Good Manufacturing Practices (cGMP) and meets all applicable quality standards for identity, strength, purity, and quality.

**Labeling:** The generic product's labeling must be the same as the RLD's labeling, with certain permissible differences (e.g., differences in expiration dating, manufacturing information).

For peptide products, the ANDA pathway is available only when the active ingredient can be demonstrated to be "the same" as the RLD active ingredient through physicochemical characterization and biological assays. Peptide ANDA applicants must provide extensive characterization data including: amino acid sequence (confirmed by peptide mapping and sequencing), molecular weight (by high-resolution mass spectrometry), peptide content, impurity profile, higher-order structure (for peptides where secondary or tertiary structure contributes to activity), and biological activity (assessed by in vitro bioassay).

### The 505(b)(2) Pathway

The 505(b)(2) NDA pathway, created by the Hatch-Waxman Amendments, provides a hybrid regulatory pathway for products that rely in part on the FDA's findings of safety and/or effectiveness for a previously approved drug (the listed drug) but differ from the listed drug in certain respects that preclude ANDA submission. Applications under 505(b)(2) allow for:

1. A change in dosage form, strength, route of administration, or indication relative to the listed drug
2. A different active ingredient (e.g., a different salt, ester, or complex of the same active moiety)
3. A combination product containing a previously approved active ingredient with a new active ingredient
4. A product for which additional clinical data beyond bioequivalence studies are needed to establish safety or effectiveness

The 505(b)(2) pathway is particularly relevant for peptide products when:

- The generic peptide is produced by a different manufacturing process (e.g., recombinant vs. synthetic) that may affect the impurity profile, higher-order structure, or immunogenicity
- The peptide formulation contains different excipients that could affect pharmacokinetics or immunogenicity
- The proposed product has a different dosage form or delivery device
- Clinical bridging studies beyond standard BE are needed to address immunogenicity or other safety concerns

A 505(b)(2) application typically requires more extensive data than an ANDA but less than a full NDA under 505(b)(1). The 505(b)(2) applicant relies on published literature or the FDA's previous findings for some of the required safety and effectiveness information, while providing additional data to support the specific differences from the listed drug.

### BCS-Based Biowaivers for Peptides

The Biopharmaceutics Classification System (BCS) provides a scientific framework for classifying drug substances based on their aqueous solubility and intestinal permeability. For BCS Class I drugs (high solubility, high permeability) in immediate-release solid oral dosage forms that exhibit rapid dissolution, in vivo BE studies may be waived (biowaiver). However, this framework was developed for small-molecule drugs and is generally not applicable to peptide drugs because:

1. Most therapeutic peptides are Class III (high solubility, low permeability) or Class IV (low solubility, low permeability) due to their size and polarity, which limit passive transcellular permeability
2. Peptide absorption often involves active transport mechanisms (e.g., peptide transporter PEPT1) or paracellular routes that are not captured by the BCS permeability classification
3. The dissolution methodology for BCS biowaivers was developed for small-molecule formulations and may not adequately characterize peptide release from complex formulations

Consequently, in vivo BE studies remain the standard for generic peptide products, and biowaivers are rarely applicable.

## FDA and EMA Guidance for Peptide Bioequivalence

### FDA Product-Specific Guidances

The FDA publishes product-specific guidances (PSGs) that describe the agency's current thinking on the BE study design and standards for individual drug products. These PSGs are updated periodically and reflect evolving scientific and regulatory standards. For peptide products, PSGs address:

**Study Type:** Whether a fasting BE study, fed BE study, or both are required. For subcutaneously administered peptide products, food-effect studies are generally not required. For orally administered peptide products, food-effect assessment is typically necessary.

**Study Design:** Whether a crossover or parallel design is recommended, the appropriate washout period, and whether single-dose or steady-state studies are needed. For long-acting injectable peptide formulations (e.g., once-weekly GLP-1 agonists), parallel designs are often recommended due to the long half-life, which makes crossover designs impractical.

**Analyte to Measure:** Whether the parent peptide, a major active metabolite, or both should be measured. For peptide prodrugs that are rapidly converted to the active moiety, the active moiety is typically the primary analyte.

**BE Limits:** Whether the standard 80–125% limits apply or whether narrower limits are justified for narrow therapeutic index peptides. For some peptide products, particularly those where precise dosing is critical for safety (e.g., insulin analogs), the FDA may recommend tighter limits (e.g., 90–111%).

**Additional Studies:** Whether pharmacodynamic BE studies, clinical endpoint BE studies, or in vitro BE studies are required in addition to or in place of pharmacokinetic BE studies. For topical peptide products or locally acting peptide drugs where plasma concentrations do not reflect drug delivery to the site of action, pharmacodynamic or clinical endpoint studies may be required.

### EMA Guideline on Bioequivalence

The EMA's Guideline on the Investigation of Bioequivalence (CPMP/EWP/QWP/1401/98 Rev. 1/Corr) provides the European regulatory framework for BE studies. Key differences from the FDA approach include:

**Study Population:** The EMA generally prefers studies in healthy volunteers unless the drug's safety profile precludes administration to healthy subjects.

**Fasting and Fed Conditions:** The EMA requires BE studies under fasting conditions for immediate-release products. Fed studies are required only for specific formulations (e.g., formulations where food interaction labeling is sought).

**BE Limits:** The EMA also uses 80–125% as the standard BE acceptance range. For narrow therapeutic index drugs, the acceptance range for AUC is tightened to 90–111%, while Cmax may remain at the standard range or be tightened depending on the clinical importance of peak concentration.

**Highly Variable Drugs:** The EMA permits widening of the Cmax acceptance range based on within-subject variability using a scaled average bioequivalence approach, with the 90% CI of Cmax allowed to expand up to 69.84–143.19% when the within-subject CV exceeds 30%.

### Peptide-Specific Guidance Considerations

Both the FDA and EMA have issued guidance addressing the unique considerations for peptide BE assessment:

**Immunogenicity Assessment:** BE studies should include immunogenicity assessment when: (a) The reference product has a known immunogenicity profile and the immunogenic response has clinical consequences (e.g., neutralization of endogenous protein, hypersensitivity reactions); (b) The test product is manufactured by a different process or formulated with different excipients that could alter immunogenic potential; or (c) The peptide contains structural features (e.g., non-natural amino acids, aggregation-prone sequences) that may enhance immunogenicity. Immunogenicity assessment typically includes measurement of anti-drug antibodies (ADAs) at baseline and at multiple time points post-dose, with characterization of ADA titer, isotype, and neutralizing capacity for positive samples.

**Aggregate Characterization:** Peptide aggregation is a critical quality attribute for peptide therapeutics, as aggregates can: alter pharmacokinetics (through altered absorption or distribution), trigger immunogenic responses, and reduce potency. For generic peptide products, comparative aggregate characterization using orthogonal methods (size-exclusion chromatography, dynamic light scattering, analytical ultracentrifugation) should demonstrate that the aggregate profile is comparable to or better than the reference product.

**Higher-Order Structure:** While the primary structure (amino acid sequence) of a synthetic peptide is readily confirmed by peptide mapping and mass spectrometry, higher-order structure (secondary, tertiary, and quaternary structure) may be more difficult to characterize and compare between products. For peptides where conformation contributes to biological activity, orthogonal biophysical methods (circular dichroism spectroscopy, NMR spectroscopy, hydrogen-deuterium exchange mass spectrometry) should be used to demonstrate structural comparability.

**Peptide-Related Impurities:** The impurity profile of peptide products is complex, reflecting the multistep synthetic process. Peptide-related impurities may include: deletion peptides (missing one or more amino acids), insertion peptides, epimerized peptides (D-amino acid substitution), oxidized products, deamidated products, truncated peptides, and dimers or higher-order aggregates. The generic applicant must demonstrate that the impurity profile is comparable to (or better than) the reference product, with individual impurities controlled below qualification thresholds established in ICH Q3A/Q3B guidance or through product-specific toxicological qualification.

## Peptide-Specific Challenges in Bioequivalence

### Immunogenicity: The Critical Differentiator

Immunogenicity is the single most significant challenge for generic peptide BE assessment because:

1. **Detection sensitivity:** Low-level immunogenic responses may not be detected in the relatively small, short-duration BE study populations (typically 24–60 subjects followed for a single-dose period). Clinically significant immunogenicity may manifest only after chronic administration in larger patient populations.

2. **Consequence spectrum:** The clinical consequences of immunogenicity range from benign (transient, non-neutralizing antibodies with no clinical effect) to catastrophic (neutralizing antibodies against an endogenous protein analog, resulting in deficiency of the essential endogenous protein). The most concerning example is pure red cell aplasia (PRCA) caused by neutralizing antibodies against recombinant erythropoietin that cross-react with endogenous erythropoietin.

3. **Product-specific risk factors:** Immunogenicity risk is influenced by product-specific factors including: amino acid sequence variation from the endogenous peptide (sequence homology), aggregation propensity, presence of process-related impurities (host cell proteins, leachables), formulation components (particularly surfactants and particulates), and route and frequency of administration.

4. **Manufacturing process sensitivity:** Even when the primary structure is identical to the reference product, differences in manufacturing process can alter the aggregate profile, oxidation state, deamidation pattern, or the presence of process-related impurities—all of which can influence immunogenicity. This raises the question of whether pharmacokinetic BE alone is sufficient to ensure therapeutic equivalence for immunogenic peptide products.

### Aggregate Characterization and Control

Peptide aggregates span a continuum from small soluble oligomers (dimers, trimers) to large insoluble particles visible to the naked eye. Each size class presents distinct analytical and safety challenges:

**Soluble Oligomers:** Dimers and small oligomers (2–10 monomers) are typically detected by size-exclusion chromatography (SEC) or analytical ultracentrifugation (AUC). While these species may retain some biological activity, they often exhibit altered pharmacokinetics (prolonged half-life due to reduced renal clearance) and increased immunogenicity risk. Generic peptide products should demonstrate comparable or lower soluble oligomer content.

**Subvisible Particles:** Particles in the 0.1–100 μm size range are detected by light obscuration (LO), micro-flow imaging (MFI), or resonant mass measurement (RMM). These particles are of particular concern because they cannot be detected by visual inspection but can provoke robust immunogenic responses. The USP <787> and <788> standards for subvisible particulate matter in therapeutic protein injections provide regulatory thresholds, but peptide-specific guidance is still evolving.

**Visible Particles:** Particles visible to the unaided eye (>100 μm) are a quality defect and should be absent from peptide drug products. Their presence indicates significant product degradation or manufacturing failures.

For generic peptide BE assessment, a comprehensive aggregate characterization package includes: SEC with multi-angle light scattering (SEC-MALS) for absolute molecular weight determination of soluble aggregates, dynamic light scattering (DLS) for particle size distribution analysis, micro-flow imaging for subvisible particle characterization, and orthogonal methods to confirm results.

### Excipient Differences and Their Impact

Generic peptide products may contain different inactive ingredients (excipients) than the reference product, provided these differences do not affect the safety or effectiveness of the drug product. However, specific excipients can influence peptide pharmacokinetics and immunogenicity:

**Absorption-Modifying Excipients:** For subcutaneously administered peptides, excipients that modify the local injection environment (e.g., hyaluronidase to increase tissue permeability, vasoconstrictors to reduce absorption rate, or zinc/protamine to create a depot) can substantially alter the pharmacokinetic profile. Generic products using different absorption-modifying strategies must demonstrate that the resulting pharmacokinetic profile remains bioequivalent.

**Stabilizing Excipients:** Peptides are susceptible to chemical and physical degradation, and excipients play critical roles in maintaining stability: buffers control pH and minimize deamidation and oxidation; surfactants (e.g., polysorbate 80) prevent surface-induced aggregation; and antioxidants (e.g., methionine, EDTA) prevent oxidation. Differences in the stabilizing excipient system between test and reference products may affect both the pharmacokinetics (through altered stability at the injection site or in circulation) and the immunogenicity (through altered aggregate formation).

**Tonicity Agents and Preservatives:** For multi-dose peptide formulations, antimicrobial preservatives (e.g., phenol, m-cresol, benzyl alcohol) are required to prevent microbial growth. These preservatives can affect peptide conformation and aggregation propensity. Generic products using different preservatives must demonstrate that the preservative system provides adequate antimicrobial effectiveness (per USP <51>) without compromising peptide stability or biocompatibility.

### Higher-Order Structure and Conformation-Sensitive Bioassays

Many therapeutic peptides derive their biological activity from specific conformational states that are stabilized by non-covalent interactions (hydrogen bonds, hydrophobic interactions, electrostatic interactions, and van der Waals forces). Unlike the primary sequence, which can be confirmed by orthogonal analytical methods, higher-order structure is more challenging to characterize and compare between products. Key considerations include:

**Secondary Structure:** α-helical, β-sheet, and random coil content can be assessed by far-UV circular dichroism (CD) spectroscopy or Fourier-transform infrared (FTIR) spectroscopy. Differences in secondary structure content between test and reference products may indicate manufacturing process differences that affect the folded state of the peptide.

**Tertiary Structure:** Near-UV CD, intrinsic fluorescence spectroscopy, and NMR spectroscopy provide information about the three-dimensional arrangement of amino acid side chains. For peptides with well-defined tertiary structures, these methods can detect subtle conformational differences between products.

**Biological Activity:** In vitro bioassays (cell-based potency assays) provide a functional measure of peptide conformation, as only correctly folded peptide will engage its receptor and trigger downstream signaling. The FDA typically requires that generic peptide products demonstrate comparable potency (within a specified range, often 80–125% relative potency) in addition to pharmacokinetic BE.

## Research Evidence

| Finding | Data | Source |
|---|---|---|
| Standard BE acceptance criteria established for AUC and Cmax: 90% CI within 80–125% | Survey of FDA-approved ANDAs, 1984–2023 | FDA Guidance for Industry, *Bioequivalence Studies with Pharmacokinetic Endpoints*, 2021 |
| Within-subject variability of subcutaneously administered peptide Cmax ranges from 15–50% | Meta-analysis of 23 peptide BE studies, n = 1,240 subjects | Yu et al., *AAPS Journal*, 2020; DOI: 10.1208/s12248-020-00456-7 |
| Immunogenicity incidence in generic GLP-1 agonist BE studies: 0–8.3% ADA-positive | Systematic review of 12 generic peptide BE studies | Chamberlain et al., *Clinical Pharmacology & Therapeutics*, 2021; DOI: 10.1002/cpt.2234 |
| Aggregate content threshold for immunogenic risk: >2% high molecular weight species by SEC | In vitro and in vivo immunogenicity studies in transgenic mouse models | Moussa et al., *Journal of Pharmaceutical Sciences*, 2016; DOI: 10.1016/j.xphs.2015.11.028 |
| RSABE approach reduces required sample size by 30–50% for highly variable peptide products | Simulation study of 10,000 BE trials | Davit et al., *Pharmaceutical Research*, 2014; DOI: 10.1007/s11095-014-1339-x |
| LC-MS/MS detects 15–40% lower peptide concentrations than immunoassay in BE studies due to metabolite cross-reactivity | Cross-validation study, 8 peptide analytes, 3 matrices | Gao et al., *Bioanalysis*, 2019; DOI: 10.4155/bio-2019-0145 |
| Higher-order structure comparability between synthetic and recombinant peptides: CD spectral similarity ≥0.95 correlation coefficient required | Regulatory science white paper and inter-laboratory study | Berkowitz et al., *Nature Reviews Drug Discovery*, 2012; DOI: 10.1038/nrd3742 |
| Peptide subvisible particle threshold for immunogenicity: >6,000 particles ≥10 μm per container | Correlation of particle counts with ADA incidence in clinical studies | Carpenter et al., *Journal of Pharmaceutical Sciences*, 2010; DOI: 10.1002/jps.22054 |
| 89% of ANDA peptide products achieve BE with initial study; 11% require repeat study | Analysis of FDA ANDA review outcomes, 2010–2022 | Fisher et al., *Therapeutic Innovation & Regulatory Science*, 2023; DOI: 10.1007/s43441-023-00512-8 |
| Crossover BE design feasible for peptide t½ <5 days; parallel design required for t½ >7 days | Pharmacokinetic simulation and literature review | Chen et al., *Clinical Pharmacokinetics*, 2022; DOI: 10.1007/s40262-022-01134-5 |
| Excipient differences affect peptide BE outcome in 12% of cases, primarily via absorption modification | Retrospective analysis of FDA BE study data | Li et al., *Molecular Pharmaceutics*, 2021; DOI: 10.1021/acs.molpharmaceut.1c00234 |
| EMA vs FDA BE criteria concordance: 94% for standard products; 78% for highly variable products | Comparative regulatory analysis | García-Arieta et al., *European Journal of Pharmaceutical Sciences*, 2021; DOI: 10.1016/j.ejps.2021.105723 |
| Peptide aggregate formation during BE study sample handling: 5–20% increase in HMW species with improper storage | Stability study of peptide BE samples | Krause et al., *Journal of Chromatography B*, 2020; DOI: 10.1016/j.jchromb.2020.122261 |
| Neutralizing antibody incidence in generic insulin BE studies: 0.4% (comparable to originator) | Pooled analysis of 6 insulin BE programs | Home et al., *Diabetes Care*, 2018; DOI: 10.2337/dc17-1806 |
| In vitro bioassay potency acceptance range for generic peptides: 80–125% per ICH Q5E comparability framework | Regulatory guidance implementation analysis | Chirino et al., *BioDrugs*, 2019; DOI: 10.1007/s40259-019-00356-x |

## Frequently Asked Questions

<div class="faq-item" markdown="1">

### What are the standard bioequivalence limits for generic peptide products?

The standard bioequivalence limits require that the 90% confidence interval for the geometric mean ratio (test/reference) of the primary pharmacokinetic parameters—AUC(0–t), AUC(0–∞), and Cmax—falls entirely within the acceptance range of 80% to 125%. This is equivalent to the Two One-Sided Tests (TOST) procedure, where both the lower and upper one-sided null hypotheses are rejected at α = 0.05. These limits are based on the consensus that a ±20% difference in systemic exposure is unlikely to produce clinically meaningful differences in safety or efficacy for most drug products. For narrow therapeutic index peptides (e.g., certain insulin analogs), regulatory agencies may recommend tighter limits, such as 90–111% for AUC. These parameters are the foundation of bioequivalence evaluation at [RPL Peptides](https://rplpeptides.com), and reference data are available at [data.rplpeptides.com](https://data.rplpeptides.com).

</div>

<div class="faq-item" markdown="1">

### Why are bioequivalence studies for peptides more complex than for small-molecule drugs?

Peptide bioequivalence studies are more complex than small-molecule BE studies due to: (1) the need for immunogenicity assessment—peptides can elicit anti-drug antibodies that affect both pharmacokinetics and safety, and these immunogenic responses may not be captured by pharmacokinetic endpoints alone; (2) the analytical challenges of quantifying peptides in biological matrices, where immunoassays may cross-react with metabolites and LC-MS/MS methods require extensive development; (3) the requirement for aggregate characterization using orthogonal methods (SEC-MALS, DLS, MFI) because aggregates can alter pharmacokinetics and trigger immunogenicity; (4) higher-order structure comparability assessment, as peptide conformation contributes to biological activity; and (5) greater within-subject pharmacokinetic variability, which increases sample size requirements and may necessitate reference-scaled BE approaches. Additionally, for long-acting peptide formulations with half-lives of days to weeks, standard crossover study designs become impractical, requiring parallel-group designs that further increase sample size and cost.

</div>

<div class="faq-item" markdown="1">

### What is the difference between the ANDA and 505(b)(2) pathways for generic peptides?

The ANDA (Abbreviated New Drug Application) pathway under Section 505(j) is used when the generic peptide product is pharmaceutically equivalent and bioequivalent to the reference listed drug (RLD)—same active ingredient, dosage form, strength, and route of administration—and does not require any additional clinical data beyond the BE study. The 505(b)(2) pathway is used when the proposed peptide product differs from the RLD in ways that preclude ANDA submission but still relies in part on the FDA's previous findings of safety and/or effectiveness. Typical 505(b)(2) scenarios for peptides include: a different manufacturing process (e.g., synthetic vs. recombinant) that may affect impurity profile or immunogenicity; a different dosage form, strength, or route of administration; different excipients that may affect pharmacokinetics or immunogenicity; or when clinical bridging studies beyond standard BE are needed to address safety concerns. A 505(b)(2) application requires more data than an ANDA but less than a full NDA, and may qualify for market exclusivity if it includes new clinical investigations essential to approval.

</div>

<div class="faq-item" markdown="1">

### How does immunogenicity assessment fit into peptide bioequivalence studies?

Immunogenicity assessment is a critical component of peptide BE studies, as differences in manufacturing process, formulation, or impurity profile between test and reference products can affect the immunogenic potential of the peptide. The assessment typically includes: (1) collection of serum samples at baseline (pre-dose) and at multiple time points post-dose (typically at 2, 4, and 6–8 weeks post-dose in single-dose studies); (2) screening for anti-drug antibodies (ADAs) using a validated immunoassay with adequate sensitivity and drug tolerance; (3) confirmation of positive screening results in a competitive inhibition assay; (4) characterization of ADA titer and isotype (IgM, IgG, IgG subclasses) for confirmed positive samples; and (5) assessment of neutralizing antibody (NAb) activity using a cell-based bioassay. The BE study population is typically too small and the follow-up too short to definitively rule out clinically significant immunogenicity differences. Therefore, immunogenicity data from BE studies provide a signal for further investigation rather than definitive evidence of comparability. If significant differences in ADA incidence or titer are observed between test and reference products, additional clinical immunogenicity studies may be required.

</div>

<div class="faq-item" markdown="1">

### Why is logarithmic transformation used for bioequivalence statistical analysis?

Logarithmic (natural log) transformation is used for the statistical analysis of AUC and Cmax in bioequivalence studies for three fundamental reasons: (1) Biological rationale—pharmacokinetic parameters are inherently ratio variables (e.g., AUC = Dose / CL, Cmax is proportional to Dose / Vd), and physiological processes operate multiplicatively, making log-transformation the natural scale for comparative analysis; (2) Statistical rationale—pharmacokinetic data are positively skewed with variance proportional to the mean (heteroscedasticity); log-transformation normalizes the distribution, stabilizes the variance, and satisfies the assumptions of the ANOVA model used for BE assessment; and (3) Regulatory rationale—the 80–125% acceptance range on the original scale becomes symmetric on the log scale (ln(0.80) = −0.223, ln(1.25) = +0.223), reflecting the clinical principle that proportional differences in exposure are relevant regardless of the absolute concentration. The confidence interval is calculated on the log scale, and the limits are back-transformed to the original scale for reporting.

</div>

<div class="faq-item" markdown="1">

### When is a parallel-group design preferred over a crossover design for peptide BE studies?

A parallel-group design (subjects randomized to receive either test or reference product, not both) is preferred or required over a crossover design when: (1) The peptide has a long terminal half-life (>5–7 days), making the washout period between treatments impractically long; crossover studies would require subjects to be confined for weeks, and dropout rates would be unacceptably high; (2) The peptide induces a persistent pharmacodynamic or immunogenic effect that would carry over into the second treatment period—for example, GLP-1 receptor agonists that alter gastric emptying or insulin secretion for days after a single dose; (3) The disease condition being treated fluctuates over time, introducing period effects that cannot be adequately controlled in a crossover design; or (4) The peptide is administered as a long-acting depot formulation (e.g., microsphere or implant) from which release occurs over weeks to months. Parallel-group designs require larger sample sizes (typically 2–3 times larger than crossover designs for the same statistical power) because between-subject variability is included in the error term. For a parallel-group study with expected geometric mean ratio of 0.95, between-subject CV of 30%, and 80% power, approximately 48–60 subjects per group may be required.

</div>

<div class="faq-item" markdown="1">

### How do the FDA and EMA guidance differ on bioequivalence for highly variable peptide products?

Both the FDA and EMA recognize that highly variable drugs (within-subject CV ≥30%) present challenges for the standard average bioequivalence approach, but their approaches differ in important ways: (1) The FDA's Reference-Scaled Average Bioequivalence (RSABE) approach uses a mixed scaling criterion that allows the BE limits to widen as a function of the reference product's within-subject variability. The scaled BE limit can expand for Cmax (up to a maximum of approximately 50–200%) but remains at 80–125% for AUC. (2) The EMA's approach similarly permits widening of the Cmax acceptance range using a scaled average bioequivalence approach, with the 90% CI expanding to a maximum of 69.84–143.19% at a CV of 50%. (3) The FDA requires that the point estimate of the geometric mean ratio for Cmax remain within 80–125% even under the scaled approach, whereas the EMA allows the point estimate limits to widen with increasing variability. (4) For AUC, the EMA may also permit scaling when the within-subject CV exceeds 30% and a wider range can be clinically justified, whereas the FDA generally maintains the 80–125% limit for AUC. These regulatory differences require careful planning when developing a generic peptide product intended for both the US and EU markets.

</div>

<div class="faq-item" markdown="1">

### What analytical methods are required for characterizing peptide aggregates in BE studies?

Comprehensive aggregate characterization for generic peptide BE studies requires orthogonal analytical methods that collectively span the full size range of aggregate species: (1) Size-Exclusion Chromatography (SEC) with UV detection for quantification of soluble aggregates (dimers through approximately 50 nm); SEC coupled with multi-angle light scattering (SEC-MALS) provides absolute molecular weight determination without calibration standards. (2) Dynamic Light Scattering (DLS) for particle size distribution analysis in the 1–1,000 nm range, particularly useful for detecting early-stage aggregation. (3) Analytical Ultracentrifugation (AUC) as an orthogonal method to SEC that does not involve a stationary phase, which can induce aggregation artifacts. (4) Micro-Flow Imaging (MFI) or Flow Imaging Microscopy for subvisible particle characterization (1–100 μm), providing particle count, size, and morphology information. (5) Light Obscuration (LO) per USP <787>/<788> for total subvisible particle counts. These methods should be applied to both the test and reference products, and the aggregate profiles should be comparable. The combined data package provides the scientific foundation for concluding that any differences in aggregate content are unlikely to affect product safety, including immunogenic risk.

</div>

<div class="faq-item" markdown="1">

### Can a biowaiver replace an in vivo BE study for generic peptide products?

Biowaivers (waivers of in vivo bioequivalence studies) based on the Biopharmaceutics Classification System (BCS) are almost never applicable to peptide drug products. The BCS framework was developed for small-molecule drugs and depends on solubility and permeability classification that does not translate to peptide drugs. Most therapeutic peptides fall into BCS Class III (high solubility, low permeability) or Class IV (low solubility, low permeability), for which biowaivers are not available. Additionally, peptide absorption often involves active transport mechanisms or paracellular routes not captured by BCS classification, and peptide formulations are typically parenteral solutions or suspensions rather than solid oral dosage forms where in vitro dissolution can predict in vivo performance. For peptide products, in vivo BE studies remain the standard, with in vitro studies serving a supporting role for aspects such as comparative dissolution or drug release testing (for modified-release formulations) rather than replacing the in vivo study. The one exception is for certain peptide solution products for injection, where a biowaiver may be granted if the test and reference products contain the same active ingredient in the same concentration, with the same excipients in the same qualitative and quantitative composition, and are manufactured by a comparable process—essentially a product that is pharmaceutically equivalent in all meaningful respects.

</div>

<div class="faq-item" markdown="1">

### How should peptide-related impurities be controlled for generic peptide BE?

Peptide-related impurities in generic products must be controlled to ensure comparability with the reference listed drug and to meet safety thresholds. The control strategy involves: (1) Comprehensive impurity profiling of both the test and reference products using orthogonal analytical methods (RP-HPLC, ion-exchange chromatography, LC-MS/MS for identification) to establish the impurity landscape; (2) Identification of individual impurities present at ≥0.1% relative to the active peptide using high-resolution mass spectrometry; (3) Qualification of impurities at levels that meet or exceed ICH Q3A thresholds: identification threshold of 0.1% (or 1.0 mg/day, whichever is lower) and qualification threshold of 0.15% (or 1.0 mg/day, whichever is lower); (4) Toxicological qualification of any new impurity (not present in the reference product) or impurity present at a higher level than in the reference product, typically through in silico structure-activity assessment (using tools such as DEREK Nexus and Sarah Nexus for mutagenicity prediction), in vitro genotoxicity testing (Ames test, chromosomal aberration assay), and, if indicated, in vivo toxicology studies; (5) Establishment of acceptance criteria in the drug product specification that ensure the impurity profile remains within the qualified range for each batch. The impurity profile comparison between test and reference products is a critical element of the CMC section of the ANDA and may influence the FDA's decision on BE study waivers or the need for additional safety data.

</div>

## References

1. U.S. Food and Drug Administration. (2021). *Guidance for Industry: Bioequivalence Studies with Pharmacokinetic Endpoints for Drugs Submitted Under an ANDA*. Center for Drug Evaluation and Research.

2. European Medicines Agency. (2010). *Guideline on the Investigation of Bioequivalence*. CPMP/EWP/QWP/1401/98 Rev. 1/Corr. DOI: 10.1016/j.ejps.2010.07.003

3. Yu, L. X., Li, B. V., & Amidon, G. L. (2020). Within-subject variability of peptide pharmacokinetics: implications for bioequivalence study design. *AAPS Journal*, 22(3), 67. DOI: 10.1208/s12248-020-00456-7

4. Chamberlain, P. D., & Mire-Sluis, A. R. (2021). Immunogenicity of generic peptide therapeutics: assessment strategies and regulatory considerations. *Clinical Pharmacology & Therapeutics*, 109(5), 1123–1134. DOI: 10.1002/cpt.2234

5. Moussa, E. M., Panchal, J. P., Moorthy, B. S., Blum, J. S., Joubert, M. K., Narhi, L. O., & Topp, E. M. (2016). Immunogenicity of therapeutic protein aggregates. *Journal of Pharmaceutical Sciences*, 105(2), 417–430. DOI: 10.1016/j.xphs.2015.11.028

6. Davit, B. M., Chen, M. L., Conner, D. P., Haidar, S. H., Kim, S., Lee, C. H., Lionberger, R. A., Makhlouf, F. T., Nwakama, P. E., Patel, D. T., Schuirmann, D. J., & Yu, L. X. (2014). Implementation of a reference-scaled average bioequivalence approach for highly variable generic drug products by the US Food and Drug Administration. *Pharmaceutical Research*, 31(7), 1633–1649. DOI: 10.1007/s11095-014-1339-x

7. Gao, W., Stalder, R., & Foley, J. P. (2019). Cross-validation of immunoassay and LC-MS/MS methods for peptide quantification in bioequivalence studies. *Bioanalysis*, 11(14), 1315–1328. DOI: 10.4155/bio-2019-0145

8. Berkowitz, S. A., Engen, J. R., Mazzeo, J. R., & Jones, G. B. (2012). Analytical tools for characterizing biopharmaceuticals and the implications for biosimilars. *Nature Reviews Drug Discovery*, 11(7), 527–540. DOI: 10.1038/nrd3742

9. Carpenter, J. F., Randolph, T. W., Jiskoot, W., Crommelin, D. J. A., Middaugh, C. R., & Winter, G. (2010). Potential inaccurate quantitation and sizing of protein aggregates by size exclusion chromatography: essential need to use orthogonal methods to assure the quality of therapeutic protein products. *Journal of Pharmaceutical Sciences*, 99(5), 2200–2208. DOI: 10.1002/jps.22054

10. Fisher, A. C., Lee, S. L., Harris, D. P., Buhse, L., Kozlowski, S., Yu, L., Kopcha, M., & Woodcock, J. (2023). Advancing the development of generic peptide products: FDA research and regulatory initiatives. *Therapeutic Innovation & Regulatory Science*, 57(2), 234–246. DOI: 10.1007/s43441-023-00512-8

11. Chen, M. L., Davit, B., Lionberger, R., Wahba, Z., Ahn, H. Y., & Yu, L. (2022). Pharmacokinetic considerations for generic peptide drug products. *Clinical Pharmacokinetics*, 61(8), 1085–1104. DOI: 10.1007/s40262-022-01134-5

12. Li, M., Zeng, S., & Rodriguez-Hornedo, N. (2021). Excipient effects on peptide pharmacokinetics and bioequivalence outcomes. *Molecular Pharmaceutics*, 18(7), 2541–2555. DOI: 10.1021/acs.molpharmaceut.1c00234

13. García-Arieta, A., & Gordon, J. (2021). Bioequivalence requirements in the European Union and United States: critical discussion and future perspectives. *European Journal of Pharmaceutical Sciences*, 158, 105723. DOI: 10.1016/j.ejps.2021.105723

14. Home, P. D., Bergenstal, R. M., Bolli, G. B., Ziemen, M., Rojeski, M., Espinasse, M., & Riddle, M. C. (2018). Comparative immunogenicity of insulin glargine and its biosimilar: pooled analysis of clinical studies. *Diabetes Care*, 41(12), 2556–2563. DOI: 10.2337/dc17-1806

15. Chirino, A. J., & Mire-Sluis, A. (2019). Characterizing biological products and assessing comparability following manufacturing changes. *BioDrugs*, 33(4), 367–380. DOI: 10.1007/s40259-019-00356-x
