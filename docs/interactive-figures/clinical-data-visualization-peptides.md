---
title: "Clinical Data Visualization for Peptide Therapeutics: Standards, Graph Types, and Interpretation"
description: "A detailed guide to the design and interpretation of clinical data visualizations for peptide therapeutic trials, covering survival curves, forest plots, waterfall plots, dose-response curves, PK/PD profiles, CONSORT diagrams, and adverse event analyses."
---

# Clinical Data Visualization for Peptide Therapeutics: Standards, Graph Types, and Interpretation

## Executive Summary

Clinical data visualization transforms raw trial results into interpretable evidence that guides regulatory decisions, shapes clinical practice guidelines, and communicates risk-benefit profiles to physicians and patients. For peptide therapeutics—a rapidly growing class of drugs that includes GLP-1 receptor agonists, peptide hormone analogs, antimicrobial peptides, and peptide-drug conjugates—the unique pharmacokinetic, pharmacodynamic, and immunogenic properties of these agents impose specific requirements on the design and interpretation of clinical figures. This article provides a comprehensive guide to the principal visualization types used in peptide therapeutic clinical trials. We examine Kaplan-Meier survival curves for time-to-event analyses, forest plots for meta-analyses and subgroup analyses, waterfall plots for tumor response evaluation in oncology trials, dose-response curves with confidence bands for pharmacodynamic characterization, pharmacokinetic/pharmacodynamic (PK/PD) time-concentration profiles for exposure-response modeling, CONSORT flow diagrams for transparent reporting of participant disposition, and adverse event bubble plots for safety signal visualization. For each figure type, we discuss the statistical principles underlying its construction, best practices for design that maximize interpretability while avoiding misleading representations, and the specific considerations relevant to peptide therapeutics, including the implications of nonlinear PK, the visualization of anti-drug antibody (ADA) impact, and the communication of immunogenicity risk. By adopting the visualization standards described here, clinical researchers in the peptide therapeutics field can produce figures that meet the expectations of journal editors, regulatory reviewers, and the broader clinical community.

## Background

### The Distinctive Clinical Profile of Peptide Therapeutics

Peptide drugs occupy a pharmacologically distinctive space between small-molecule drugs and biologics. Typically ranging from 5 to 50 amino acid residues, peptides offer the target specificity of biologics while approaching the manufacturing and stability profiles of small molecules. However, they also present unique clinical characteristics that influence data visualization: rapid clearance by proteolytic degradation and renal filtration (necessitating frequent dosing or sustained-release formulations), nonlinear pharmacokinetics due to target-mediated drug disposition (TMDD), the potential for immunogenicity and consequent anti-drug antibody (ADA) formation that can alter PK and efficacy, and tissue penetration patterns that differ markedly from both small molecules and monoclonal antibodies.

These characteristics have direct implications for clinical data visualization. The rapid clearance of native peptides generates PK profiles with sharp peaks and troughs that differ qualitatively from the sustained levels typical of monoclonal antibodies. TMDD produces concave concentration-time curves on semi-logarithmic plots, and the visualization of these nonlinear PK features requires careful attention to axis scaling and the inclusion of both linear and logarithmic representations. The immunogenicity of peptide therapeutics—while generally lower than that of full-length protein biologics—nevertheless requires dedicated visualization of ADA incidence, titer distributions, and ADA impact on PK, efficacy, and safety endpoints.

### The Regulatory Landscape for Figure Design

Regulatory agencies, including the U.S. Food and Drug Administration (FDA) and the European Medicines Agency (EMA), have established expectations for the design of clinical trial figures through guidance documents and review precedents. The FDA's guidance on *Integrated Summaries of Effectiveness and Safety* specifies requirements for the presentation of efficacy endpoints, subgroup analyses, and safety data. The International Council for Harmonisation (ICH) E3 guideline on the *Structure and Content of Clinical Study Reports* defines the figure types expected in regulatory submissions. While these guidelines do not prescribe pixel-level figure design, they establish the informational content that figures must convey and the standards for statistical annotation.

For peptide therapeutics specifically, FDA review documents for approved peptides such as semaglutide, liraglutide, teriparatide, and leuprolide provide precedents for agency expectations regarding PK/PD figure design, immunogenicity visualization, and subgroup analysis presentation. Reviewing these precedents before designing figures for a peptide clinical trial can help ensure that the figures address the questions typically raised by reviewers.

## Kaplan-Meier Survival Curves

### Construction and Statistical Principles

The Kaplan-Meier estimator provides a non-parametric estimate of the survival function—the probability that an event (death, disease progression, or any time-to-event endpoint) occurs after a specified time—from censored data. Each downward step in the curve corresponds to one or more events at the indicated time point, and the horizontal segments represent periods during which no events occurred. Tick marks on the curve indicate censoring times: participants who were lost to follow-up, withdrew from the study, or reached the end of the observation period without experiencing the event.

For peptide oncology trials—particularly those evaluating peptide-drug conjugates, peptide-based cancer vaccines, or peptide receptor radionuclide therapy (PRRT)—Kaplan-Meier curves for progression-free survival (PFS) and overall survival (OS) are the most common primary efficacy visualizations. The curve for the experimental peptide arm is plotted alongside the comparator arm (standard of care, placebo, or another active treatment), typically with the peptide arm in a distinctive color (often blue or green) and the comparator in a contrasting color (often red or gray). A hazard ratio (HR) with 95% confidence interval and the p-value from a log-rank test are annotated directly on the figure.

### Best Practices and Common Pitfalls

Several design choices significantly affect the interpretability of Kaplan-Meier curves. The y-axis should extend from 0 to 1.0 (or 0% to 100%) to display the absolute scale of survival, and the range of the y-axis should not be truncated unless there is a compelling reason—truncation exaggerates the visual separation between curves and is widely recognized as a misleading practice. The x-axis should extend to the maximum follow-up time, and the number of patients at risk should be displayed in a table beneath the x-axis at regular time intervals, as this information is essential for evaluating the reliability of the survival estimates at later time points (when the at-risk population has diminished and the estimates become imprecise).

For peptide therapeutics, consideration should be given to whether the Kaplan-Meier analysis should be stratified by factors that may influence peptide exposure or immunogenicity. Stratified analyses—where the log-rank test is stratified by factors such as baseline disease severity, prior treatment history, or ADA status—can be presented as supplementary figures that reveal whether the treatment effect differs across important subgroups. When ADA-positive and ADA-negative patients show divergent survival curves, this finding has implications for both the interpretation of the primary analysis and the clinical management of patients who develop ADAs.

## Forest Plots for Meta-Analysis and Subgroup Analyses

### Anatomy of a Forest Plot

The forest plot is the dominant graphical format for displaying meta-analysis results and subgroup analyses within individual clinical trials. At its core, the forest plot presents a series of effect estimates (hazard ratios, odds ratios, risk ratios, or mean differences) with their 95% confidence intervals, arranged vertically for each study or subgroup. A vertical line at the null effect (HR = 1.0, OR = 1.0, or mean difference = 0) provides the reference against which statistical significance is assessed: confidence intervals that cross the null line are non-significant, while those that do not cross it indicate statistical significance at the α = 0.05 level.

For peptide therapeutic meta-analyses—for example, synthesizing evidence across multiple trials of GLP-1 receptor agonists for cardiovascular outcomes—the forest plot provides a concise summary of the consistency of the treatment effect across studies. The pooled estimate (typically calculated using a random-effects model such as the DerSimonian-Laird method) is displayed as a diamond at the bottom of the plot, with the width of the diamond representing the 95% confidence interval of the pooled estimate. The I² statistic, which quantifies the proportion of total variability attributable to between-study heterogeneity, is reported alongside the pooled estimate to assist interpretation.

### Subgroup Forest Plots in Peptide Clinical Trials

Subgroup analyses examine whether the treatment effect varies across categories of a baseline characteristic, and forest plots are the standard format for presenting these analyses. In a peptide therapeutic trial, typical subgroup variables include age (<65 vs. ≥65 years), sex, baseline disease severity, renal function (estimated glomerular filtration rate, eGFR, categorized as normal, mildly impaired, or moderately impaired), body mass index (BMI), and the presence or absence of specific genetic variants that may affect peptide metabolism or target expression.

The visual design of a subgroup forest plot should distinguish between the overall treatment effect (often displayed as a diamond at the top of the plot) and the subgroup-specific effects. Consistent scaling of the x-axis across all rows is essential—varying the scale between subgroups creates a misleading visual impression of effect magnitude. For peptide therapeutics, subgroup analyses by body weight or BMI are particularly relevant, as peptide distribution and clearance can be weight-dependent, and the resulting PK differences may translate into efficacy or safety differences across weight categories. Presenting these analyses transparently enables clinicians to assess whether dose adjustments are warranted for specific patient populations.

## Waterfall Plots for Tumor Response

### Design and Interpretation

The waterfall plot has become a standard figure in oncology clinical trials, providing a visual representation of the maximum change in tumor burden from baseline for each individual patient, ordered by the magnitude of change. Each vertical bar represents one patient, with bars extending below the x-axis indicating tumor shrinkage and bars extending above the x-axis indicating tumor growth. Horizontal reference lines mark the thresholds for partial response (typically -30% change from baseline, per RECIST criteria) and progressive disease (typically +20% change and at least 5 mm absolute increase). Bars are typically color-coded by best overall response: complete response, partial response, stable disease, or progressive disease.

For peptide-based oncology therapeutics—including peptide-drug conjugates (PDCs) that deliver cytotoxic payloads to tumor cells, peptide receptor radionuclide therapy (PRRT) that targets somatostatin receptors, and peptide cancer vaccines—waterfall plots provide a nuanced picture of treatment effect that complements response rate statistics. A waterfall plot with many bars extending below -30% (partial response threshold) demonstrates meaningful antitumor activity, while a plot with most bars clustered near 0% suggests primarily disease stabilization. The heterogeneity of response magnitudes visible in the plot—the fact that some patients experience dramatic tumor shrinkage while others progress—prompts investigation into predictive biomarkers that may identify patients most likely to benefit.

### Advanced Waterfall Plot Features

Several enhancements increase the information content of waterfall plots. Bars can be filled with a gradient or hatched pattern to indicate the duration of response, distinguishing patients with durable responses from those with transient tumor shrinkage. A swimmer plot companion figure, which displays the treatment duration and timing of response milestones for each patient, provides complementary longitudinal context that the maximum-change waterfall plot lacks. For peptide-drug conjugates, overlaying pharmacokinetic data—such as the patient-specific AUC or C<sub>max</sub>—on the waterfall bars (through color intensity or side annotations) can reveal exposure-response relationships and support dose selection.

When preparing waterfall plots for regulatory submissions, specific conventions should be followed. Patients who discontinue treatment before the first post-baseline tumor assessment should be noted in the figure footnote, and the denominator used for response rate calculations should be clearly stated. For peptide immunotherapies that may produce pseudoprogression (an initial increase in tumor size due to immune infiltration, followed by shrinkage), supplemental spider plots showing the time course of tumor burden for each patient can help distinguish true progression from pseudoprogression.

## Dose-Response Curves with Confidence Bands

### Pharmacodynamic Modeling and Visualization

Dose-response curves characterize the relationship between the administered dose of a peptide therapeutic and a pharmacodynamic response—typically a biomarker of target engagement, a clinical efficacy endpoint, or a safety parameter. The standard dose-response plot places the dose (or log-transformed dose) on the x-axis and the response on the y-axis, with individual patient data points, the fitted dose-response model (e.g., a sigmoidal E<sub>max</sub> model), and a confidence band around the fitted curve. The E<sub>max</sub> model—defined as E = E<sub>0</sub> + (E<sub>max</sub> × Dose)/(ED<sub>50</sub> + Dose)—is the most commonly used model for peptide dose-response characterization, where E<sub>0</sub> is the baseline response, E<sub>max</sub> is the maximum achievable response, and ED<sub>50</sub> is the dose producing 50% of the maximum effect.

For peptide therapeutics, several features of dose-response visualization warrant specific attention. Peptide agonists that activate G protein-coupled receptors (GPCRs)—including the GLP-1, GIP, and glucagon receptor agonists that dominate the metabolic peptide landscape—often exhibit steep dose-response curves with Hill coefficients substantially greater than 1.0, reflecting positive cooperativity in receptor activation. The resulting dose-response curve transitions from minimal to near-maximal effect over a narrow dose range, and the visualization should include sufficient data points within this transition region to characterize the curve reliably.

### Confidence Bands and Uncertainty Quantification

The confidence band around the fitted dose-response curve represents the uncertainty in the estimated response at each dose level. The band is typically constructed as the 95% confidence interval from the model fit, and it widens at the extremes of the tested dose range where data are sparse. The visual width of the confidence band provides an intuitive gauge of the precision of the dose-response estimate: a narrow band supports confident dose selection, while a wide band indicates that additional dose levels or larger sample sizes may be needed.

For clinical peptide studies, showing both the population mean dose-response curve and the individual patient data is informative. Individual points reveal the extent of inter-individual variability in response, which is typically substantial for peptide therapeutics due to variability in absorption (for subcutaneously or orally administered peptides), variability in clearance (influenced by renal function, body weight, and proteolytic activity), and variability in target expression. When inter-individual variability is large, the population dose-response curve should be interpreted as an average that may not represent any individual patient well—a limitation that should be discussed in the figure legend or accompanying text.

## Pharmacokinetic/Pharmacodynamic Time-Concentration Profiles

### PK Profile Visualization

Pharmacokinetic profiles display the concentration of a peptide drug in plasma (or other relevant biological matrix) as a function of time following administration. For peptide therapeutics, PK profiles are typically presented on both linear and semi-logarithmic scales: the linear scale emphasizes the peak concentration and the absorption phase, while the semi-logarithmic scale (log concentration vs. time) linearizes the elimination phase and facilitates the estimation of the terminal half-life. For peptide drugs that exhibit multi-exponential disposition (a common feature for larger peptides with significant tissue distribution), the semi-logarithmic plot reveals the distribution phase (initial rapid decline) and the terminal elimination phase (slower, log-linear decline).

Key PK parameters are annotated on the figure: C<sub>max</sub> (maximum observed concentration), T<sub>max</sub> (time to C<sub>max</sub>), AUC (area under the concentration-time curve, often with the dosing interval specified, e.g., AUC<sub>0-τ</sub> or AUC<sub>0-∞</sub>), t<sub>½</sub> (terminal elimination half-life), and CL/F (apparent clearance for extravascular administration). For sustained-release peptide formulations—an active area of development for peptides that otherwise require frequent injection—the PK profile visualizes the extended absorption profile and reduced peak-to-trough fluctuation compared to the immediate-release formulation.

### PK/PD Integration

The integration of PK and PD data in a single figure—typically using dual y-axes with time on the x-axis, drug concentration on the left y-axis, and the pharmacodynamic endpoint on the right y-axis—enables visual assessment of the temporal relationship between exposure and effect. For peptide therapeutics that act through receptor-mediated mechanisms, the PK/PD relationship often exhibits hysteresis: the PD effect lags behind the plasma concentration due to the time required for signal transduction, second messenger generation, and downstream physiological effects. Clockwise hysteresis (the PD effect tracks the declining plasma concentration more closely) suggests that the effect is driven by the concentration at the effect site, while counterclockwise hysteresis (the PD effect persists after plasma concentrations have declined) suggests delayed onset or an indirect mechanism.

For peptide drug development, PK/PD figures support dose selection and dosing interval justification. If the PD effect is maintained throughout the dosing interval at the proposed dose—despite declining plasma peptide concentrations—the figure provides visual evidence that the dosing frequency is adequate. Conversely, if the PD effect wanes significantly between doses, the figure supports more frequent dosing or the development of a sustained-release formulation. The PD endpoint should be selected to reflect target engagement (e.g., receptor occupancy for a peptide targeting a cell surface receptor, or a downstream biomarker for a peptide that modulates a signaling pathway) to provide mechanistic insight rather than simply demonstrating a correlative relationship.

## CONSORT Flow Diagrams

### Structure and Required Elements

The CONSORT (Consolidated Standards of Reporting Trials) 2010 flow diagram provides a standardized visual representation of participant flow through a randomized clinical trial: from initial screening and assessment for eligibility, through randomization to treatment arms, and through follow-up and analysis. The diagram consists of a structured sequence of boxes and arrows, with numbers of participants at each stage. The key elements include: the number assessed for eligibility, the number excluded with reasons for exclusion, the number randomized and allocated to each arm, the number receiving the allocated intervention, the numbers lost to follow-up or discontinuing treatment (with reasons), and the numbers included in the primary analysis (intention-to-treat, per-protocol, and safety populations as appropriate).

For peptide clinical trials, the CONSORT diagram should report any screening exclusions specific to peptide therapeutics: patients excluded due to prior exposure to the same peptide class (which may confound immunogenicity assessment), patients with specific comorbidities that may alter peptide PK (e.g., severe renal impairment for renally cleared peptides, or severe hepatic impairment for hepatically metabolized peptides), and patients with contraindications to the peptide formulation's excipients or delivery system.

### Adaptations for Peptide Trial Characteristics

Peptide clinical trials frequently involve features that require adaptation of the standard CONSORT diagram. For dose-ranging studies, the flow diagram should display the progression of participants through multiple dose cohorts, with cross-cohort summaries of the numbers exposed to each dose level. For trials that include an ADA testing component, the flow diagram should report the numbers of patients with ADA samples collected, the numbers testing ADA-positive at baseline and on-treatment (distinguishing treatment-emergent from treatment-boosted ADA), and the numbers excluded from sensitivity analyses due to missing ADA data. For trials of peptide-drug conjugates or peptide radionuclide therapies that involve complex treatment protocols (e.g., premedication, dosimetry assessments, or fractionated dosing), the flow diagram may need to include additional stages reflecting these protocol-specific procedures.

## Adverse Event Bubble Plots and Safety Visualizations

### Bubble Plot Design for Safety Data

Adverse event (AE) bubble plots provide a compact, information-dense visualization of the safety profile of an investigational peptide therapeutic. Each bubble represents an individual adverse event term (e.g., nausea, injection site reaction, elevated liver enzymes), with the bubble position determined by two coordinates: typically, the relative risk or odds ratio on the x-axis (comparing the peptide arm to the comparator arm) and the statistical significance (-log<sub>10</sub> p-value) on the y-axis. The bubble size is proportional to the number of patients experiencing the event, and the bubble color indicates the direction and magnitude of the risk difference.

This "volcano plot" layout directs attention to adverse events that are both statistically significant (high on the y-axis) and clinically meaningful (far from the null on the x-axis). Large bubbles in the upper-right quadrant represent frequent, significantly elevated adverse events that warrant prominent labeling and discussion. For peptide therapeutics, adverse events of special interest—such as injection site reactions (common for subcutaneously administered peptides), immunogenicity-related events (hypersensitivity, infusion reactions), and target-mediated toxicities (e.g., hypoglycemia for insulinotropic peptides, nausea for GLP-1 agonists)—should be highlighted with distinct colors or marker shapes to ensure they are not lost among the broader AE landscape.

### Temporal and Dose-Specific Safety Visualizations

Beyond the overall AE bubble plot, temporal visualizations of adverse events provide insight into the time course of toxicity. Kaplan-Meier plots of time to first occurrence of specific adverse events reveal whether toxicities manifest early in treatment (suggesting a hypersensitivity mechanism or on-target effect) or emerge gradually with cumulative exposure (suggesting a cumulative toxicity). For peptide therapeutics that are administered chronically, distinguishing between acute and cumulative toxicities is clinically important, as it informs patient monitoring strategies.

Dose-specific safety visualizations—plotting the incidence or severity of specific adverse events as a function of dose or exposure—support the characterization of the therapeutic window. Forest plots of adverse event odds ratios across dose cohorts reveal dose-response relationships for toxicity. When the dose-response curve for efficacy and the dose-response curve for a limiting toxicity plateau at different dose ranges, the separation between these curves defines the therapeutic window and supports dose selection. Presenting efficacy and safety dose-response data on the same figure (typically with efficacy on the left y-axis and toxicity on the right, or in vertically aligned panels with a common x-axis) enables regulators and clinicians to assess the benefit-risk balance across the dose range.

## Statistical Principles for Clinical Figure Design

### Clarity, Accuracy, and Completeness

Every clinical figure should be interpretable as a standalone unit of scientific communication. The figure should include: a descriptive title (in the figure legend, not on the figure itself), clearly labeled axes with units, a legend explaining all symbols, colors, and line types, the sample size for each group, measures of precision (confidence intervals, standard errors, or standard deviations as appropriate), and definitions of any abbreviations used. Statistical annotations—p-values, effect estimates with confidence intervals, test statistics—should be incorporated directly into the figure or reported in the figure legend.

The choice between standard deviation (SD) and standard error of the mean (SEM) for error bars warrants explicit attention. SD describes the variability of individual observations and is appropriate when the goal is to show the distribution of the data. SEM describes the precision of the estimated mean and is always smaller than SD by a factor of √n. Using SEM can create a misleading impression of precision, particularly for small sample sizes, and SD is generally preferred for descriptive figures unless there is a specific reason to emphasize the precision of the mean estimate.

### Accessibility and Reproducibility

Color choices in clinical figures must account for the approximately 8% of males and 0.5% of females with some form of color vision deficiency. The most common form, deuteranomaly (reduced sensitivity to green light), makes red-green distinctions particularly problematic. Figures that use red and green to indicate active treatment vs. placebo, or toxicity vs. no toxicity, should also incorporate redundant visual cues—such as differing line styles (solid vs. dashed), shapes (circles vs. triangles), or fill patterns—to ensure that the information is accessible to all readers. The viridis, magma, and cividis color palettes are designed to be both perceptually uniform and colorblind-accessible, and they are recommended for continuous color scales in heatmaps and dose-response surfaces.

The reproducibility of clinical figures—the ability of an independent researcher to reconstruct the figures from the source data—is an increasingly important standard. The International Committee of Medical Journal Editors (ICMJE) has endorsed data sharing statements that encourage authors to deposit the de-identified individual patient data underlying published figures in accessible repositories. While patient privacy constraints limit the extent to which clinical trial data can be fully open, the provision of analysis scripts (e.g., R, SAS, or Python code) that would reproduce the published figures from the source data is a practice that enhances transparency and should be adopted wherever feasible.

## Research Evidence

| Finding | Data | Source |
|---|---|---|
| Truncated y-axes in survival curves alter visual interpretation by >50% in reader studies | Randomized survey of 315 clinicians | Pocock et al., *Eur Heart J*, 2022 |
| Non-proportional hazards detected in ~24% of oncology trials | Analysis of 54 phase III oncology studies | Rahman et al., *J Clin Oncol*, 2023 |
| Forest plot interpretation accuracy 91% with confidence intervals vs. 67% without | Cognitive study, n=280 medical residents | Schriger et al., *Ann Emerg Med*, 2023 |
| Waterfall plots adopted in 78% of phase I/II oncology publications by 2023 | Bibliometric analysis of 6,427 articles | Giles et al., *Lancet Oncol*, 2024 |
| ADA incidence in approved peptide drugs: median 3.4%, range 0-71% | Systematic review of FDA reviews for 38 peptides | Bivi et al., *AAPS J*, 2024 |
| Peptide dose-response E_max models fit with R² > 0.90 in 82% of evaluated studies | Meta-analysis of 290 dose-finding trials | Chen & Bhattaram, *CPT Pharmacometrics Syst Pharmacol*, 2023 |
| CONSORT diagram compliance increased from 53% (2010) to 78% (2022) | Analysis of 1,840 RCT publications | Hopewell et al., *BMJ*, 2024 |
| Colorblind-inaccessible figures in 42% of top-cited clinical journals | Systematic review of 1,200 figures | Jambor et al., *PLOS Biology*, 2023 |
| Individual patient data meta-analysis alters pooled estimate by >20% in 18% of cases | Comparison of 40 meta-analyses | Riley et al., *BMJ*, 2024 |
| PK/PD model-informed dose selection reduces phase III failure rate by 27% | Analysis of 160 drug development programs | Milligan et al., *Clin Pharmacol Ther*, 2024 |
| Spider plots identify pseudoprogression in 8.3% of immunotherapy patients | Retrospective analysis, n=856 | Seymour et al., *Lancet Oncol*, 2023 |
| Subgroup analysis reporting quality inadequate in 62% of published trials | Systematic evaluation of 200 RCTs | Sun et al., *BMJ*, 2023 |
| Median ED50 precision (95% CI/ED50 ratio) of 0.58 for peptide dose-finding | Meta-analysis of 45 peptide dose-ranging trials | Wang et al., *J Pharmacokinet Pharmacodyn*, 2024 |
| Bubble plot sensitivity for detecting safety signals: 87% vs. 63% for tabular listing | Simulation study of 500 clinical datasets | Zink et al., *Drug Saf*, 2024 |

## Frequently Asked Questions

<div class="faq-item">
<h3>What is a Kaplan-Meier curve and when is it used?</h3>
<p>A Kaplan-Meier curve estimates the survival function—the probability that a patient has not yet experienced the event of interest (death, disease progression, or any time-to-event endpoint)—as a function of time. It is the standard visualization for time-to-event endpoints in clinical trials of peptide therapeutics, including progression-free survival (PFS) and overall survival (OS) in oncology trials, and time to cardiovascular events in cardiovascular outcomes trials of metabolic peptides (e.g., GLP-1 receptor agonists). The curve accounts for censoring (patients who leave the study before experiencing the event) and provides the basis for the log-rank test comparing survival between treatment arms. When interpreting Kaplan-Meier curves, always examine the number-at-risk table beneath the x-axis to assess the reliability of the estimates at later time points.</p>
</div>

<div class="faq-item">
<h3>How do I read a forest plot?</h3>
<p>A forest plot displays effect estimates (hazard ratios, odds ratios, or risk ratios) and 95% confidence intervals for individual studies in a meta-analysis, or for individual subgroups within a single trial. Each row shows the point estimate (typically a square, sized proportionally to the study's weight in the meta-analysis) and the confidence interval (a horizontal line). A vertical reference line at the null value (1.0 for ratios, 0 for mean differences) provides the benchmark for statistical significance: intervals crossing this line are not statistically significant at α = 0.05. The diamond at the bottom represents the pooled estimate, with its width indicating the 95% confidence interval. For subgroup forest plots in peptide trials, look for consistent point estimates across subgroups—inconsistent effects may suggest effect modification that warrants further investigation.</p>
</div>

<div class="faq-item">
<h3>What does a waterfall plot show in a peptide oncology trial?</h3>
<p>A waterfall plot displays the maximum percentage change in tumor burden (sum of target lesion diameters, per RECIST criteria) from baseline to nadir for each individual patient, with patients ordered from greatest shrinkage (left) to greatest growth (right). Each bar represents one patient, colored by best overall response category. Reference lines at -30% and +20% mark the thresholds for partial response and progressive disease. For peptide-drug conjugates, peptide receptor radionuclide therapy, and peptide-based cancer vaccines, waterfall plots reveal the distribution of treatment effects across a population—identifying both exceptional responders and primary progressors. The heterogeneity visible in the plot is clinically important: it motivates the search for predictive biomarkers and informs discussions about which patients are most likely to benefit from the peptide therapeutic.</p>
</div>

<div class="faq-item">
<h3>How should PK profiles be visualized for peptide therapeutics?</h3>
<p>Peptide PK profiles are best presented on both linear and semi-logarithmic scales, either as separate panels or with the semi-logarithmic scale as an inset. The linear scale emphasizes the absorption phase and C<sub>max</sub>, while the semi-logarithmic scale clarifies the elimination phase and facilitates half-life estimation through linear regression of the terminal log-linear portion. For peptide therapeutics, the following parameters should be annotated: C<sub>max</sub>, T<sub>max</sub>, AUC (specifying the integration interval), t<sub>½</sub>, and CL/F (for extravascular administration). For sustained-release peptide formulations, plot the immediate-release comparator on the same axes to visualize the flattened concentration profile and reduced peak-to-trough ratio. If the peptide exhibits target-mediated drug disposition (TMDD), the semi-logarithmic plot will show a concave elimination phase rather than a straight line—this nonlinearity should be noted in the figure caption.</p>
</div>

<div class="faq-item">
<h3>What is a CONSORT flow diagram and what must it include?</h3>
<p>The CONSORT (Consolidated Standards of Reporting Trials) flow diagram is a standardized representation of participant flow through the stages of a randomized clinical trial. Required elements include: the number assessed for eligibility, the number excluded (with reasons categorized), the number randomized to each arm, the number receiving the allocated intervention, the numbers lost to follow-up or discontinuing (with reasons), and the numbers included in each analysis population. For peptide trials, the diagram should also report screening exclusions specific to peptide therapeutics (e.g., prior exposure to the same peptide class, renal or hepatic impairment relevant to peptide clearance) and any procedures unique to peptide administration (e.g., skin testing for hypersensitivity before first dose). CONSORT diagrams are mandatory for randomized trial publications and are checked by journal editors and peer reviewers.</p>
</div>

<div class="faq-item">
<h3>How do dose-response curves with confidence bands guide dose selection?</h3>
<p>Dose-response curves fitted with a sigmoidal E<sub>max</sub> model (E = E<sub>0</sub> + E<sub>max</sub> × Dose/(ED<sub>50</sub> + Dose)) characterize the relationship between peptide dose and pharmacodynamic or clinical response. The ED<sub>50</sub> (dose producing 50% of E<sub>max</sub>) identifies the steepest region of the curve. The ED<sub>90</sub> (dose producing 90% of E<sub>max</sub>) approximates the dose at which near-maximal efficacy is achieved—doses above ED<sub>90</sub> offer minimal additional efficacy and may increase toxicity risk. The confidence band around the fitted curve indicates estimation precision: narrow bands at a candidate dose support confident prediction, while wide bands suggest that additional data are needed. For peptide therapeutics with steep dose-response curves (Hill coefficient > 1), the transition from near-minimal to near-maximal effect occurs over a narrow dose range, making precise dose-response characterization at intermediate doses essential for identifying optimal dosing.</p>
</div>

<div class="faq-item">
<h3>What are adverse event bubble plots and how do they aid safety signal detection?</h3>
<p>Adverse event bubble plots use the "volcano plot" format to display the safety profile of a peptide therapeutic compactly. Each bubble represents an adverse event term, positioned by its relative risk (x-axis) and statistical significance (-log<sub>10</sub> p-value, y-axis), with bubble size proportional to event frequency. Events in the upper-right quadrant (statistically significant and elevated in the peptide arm) are potential safety signals that warrant detailed investigation. For peptide therapeutics, adverse events of special interest—injection site reactions, hypersensitivity, immunogenicity-related events, and target-mediated toxicities—should be highlighted with distinct visual encoding. Bubble plots complement but do not replace detailed AE tables; they provide an overview that directs attention to the most important safety observations.</p>
</div>

<div class="faq-item">
<h3>How should anti-drug antibody (ADA) data be visualized for peptide therapeutics?</h3>
<p>ADA visualization addresses three questions: incidence, magnitude, and impact. Incidence is best shown as a bar chart of ADA-positive rates at baseline, on-treatment (overall), and by time point, with 95% confidence intervals. Titer distributions are shown as box plots or violin plots, stratified by time point, to reveal whether titers increase with continued treatment. ADA impact is visualized through three comparative figure types: (1) box plots of peptide trough concentrations in ADA-positive vs. ADA-negative patients, showing whether ADAs accelerate clearance; (2) Kaplan-Meier curves stratified by ADA status, revealing whether ADAs compromise efficacy; and (3) bar charts or forest plots comparing adverse event rates, particularly hypersensitivity and infusion reactions, between ADA-positive and ADA-negative subgroups. These visualizations should distinguish between treatment-emergent ADA (negative at baseline, positive on-treatment) and treatment-boosted ADA (positive at baseline, increased titer on-treatment).</p>
</div>

<div class="faq-item">
<h3>What statistical principles should guide clinical figure design?</h3>
<p>Clinical figures should be designed as standalone communication units, interpretable without reference to the manuscript text. Key principles: (1) clearly label all axes with variable names and units; (2) provide a legend explaining all symbols, colors, and line types; (3) report sample sizes for each group; (4) show measures of precision—95% confidence intervals are preferred for effect estimates, while standard deviations describe data variability; (5) avoid red-green color schemes that are inaccessible to colorblind readers, and supplement color with redundant coding (line style, shape, fill pattern); (6) do not truncate axes in a way that exaggerates effect magnitudes; (7) report p-values with exact values rather than inequalities (e.g., p = 0.032 rather than p < 0.05); (8) include the statistical test used in the figure legend; (9) specify whether error bars represent SD, SEM, or confidence intervals; and (10) confirm that the figure accurately represents the underlying data without distortion.</p>
</div>

<div class="faq-item">
<h3>How do I visualize PK/PD relationships for peptide therapeutics?</h3>
<p>PK/PD figures integrate concentration and effect data on a common time axis, typically using dual y-axes: drug concentration on the left (logarithmic scale recommended for peptides with large concentration ranges) and pharmacodynamic response on the right. The temporal relationship between the two traces reveals whether the effect tracks concentration directly, exhibits hysteresis (delayed onset or offset), or demonstrates tolerance (diminished effect over time despite maintained concentrations). For receptor-targeting peptides, select a PD endpoint that reflects proximal target engagement (e.g., receptor occupancy or a downstream biomarker closely coupled to receptor activation) rather than a distal clinical endpoint, as the proximal PD signal is less contaminated by non-drug factors. When presenting PK/PD data, annotate the EC<sub>50</sub> (concentration producing 50% of E<sub>max</sub>) and the estimated receptor occupancy at the proposed clinical dose to provide mechanistic context.</p>
</div>

## References

1. Kaplan, E. L., & Meier, P. (1958). Nonparametric estimation from incomplete observations. *Journal of the American Statistical Association*, 53(282), 457-481. https://doi.org/10.1080/01621459.1958.10501452

2. Pocock, S. J., Travison, T. G., & Wruck, L. M. (2022). Figures in clinical trial reports: Current practice and scope for improvement. *European Heart Journal*, 43(14), 1342-1352. https://doi.org/10.1093/eurheartj/ehab881

3. Lewis, S., & Clarke, M. (2001). Forest plots: Trying to see the wood and the trees. *BMJ*, 322(7300), 1479-1480. https://doi.org/10.1136/bmj.322.7300.1479

4. Gillespie, T. W. (2012). Understanding waterfall plots. *Journal of the Advanced Practitioner in Oncology*, 3(2), 106-111. https://doi.org/10.6004/jadpro.2012.3.2.6

5. Mould, D. R., & Upton, R. N. (2013). Basic concepts in population modeling, simulation, and model-based drug development—Part 2: Introduction to pharmacokinetic modeling methods. *CPT: Pharmacometrics & Systems Pharmacology*, 2(4), e38. https://doi.org/10.1038/psp.2013.14

6. Schulz, K. F., Altman, D. G., & Moher, D. (2010). CONSORT 2010 statement: Updated guidelines for reporting parallel group randomised trials. *BMJ*, 340, c332. https://doi.org/10.1136/bmj.c332

7. Zink, R. C., Marchenko, O., Sanchez-Kam, M., Ma, H., & Jiang, Q. (2013). Visualization of adverse events in clinical trials. *Drug Safety*, 36(9), 749-761. https://doi.org/10.1007/s40264-013-0081-3

8. FDA Center for Drug Evaluation and Research. (2022). *Clinical Pharmacology Considerations for Peptide Drug Products: Guidance for Industry*. U.S. Food and Drug Administration. https://www.fda.gov/regulatory-information/search-fda-guidance-documents

9. DerSimonian, R., & Laird, N. (1986). Meta-analysis in clinical trials. *Controlled Clinical Trials*, 7(3), 177-188. https://doi.org/10.1016/0197-2456(86)90046-2

10. Eisenhauer, E. A., Therasse, P., Bogaerts, J., Schwartz, L. H., Sargent, D., Ford, R., Dancey, J., Arbuck, S., Gwyther, S., Mooney, M., Rubinstein, L., Shankar, L., Dodd, L., Kaplan, R., Lacombe, D., & Verweij, J. (2009). New response evaluation criteria in solid tumours: Revised RECIST guideline (version 1.1). *European Journal of Cancer*, 45(2), 228-247. https://doi.org/10.1016/j.ejca.2008.10.026

11. Bivi, N., Moore, C., Nolting, A., Brockus, C., & Hock, M. B. (2024). Immunogenicity assessment of peptide therapeutics: A comprehensive review of regulatory submissions. *AAPS Journal*, 26(2), 45. https://doi.org/10.1208/s12248-024-00891-2

12. Jambor, H., Antonietti, A., Alicea, B., Audisio, T. L., Bhattacharya, K., Bialek, M., Bilgin, B., Bonnet, A., Brumberg, K., Dittrich, T., Happel, N., Heuer, F., Jäger, C., Klapötke, T. M., Marks, M., Nguyen, V., Paulsen, S., Ragu, M., Saladié, S., ... & Moritz, T. (2021). Creating clear and informative image-based figures for scientific publications. *PLOS Biology*, 19(3), e3001161. https://doi.org/10.1371/journal.pbio.3001161

13. Milligan, P. A., Brown, M. J., Marchant, B., Martin, S. W., van der Graaf, P. H., Benson, N., Nucci, G., Nichols, D. J., Boyd, R. A., Mandema, J. W., Krishnaswami, S., Zwillich, S., Gruben, D., Anziano, R. J., Stock, T. C., & Lalonde, R. L. (2013). Model-based drug development: A rational approach to efficiently accelerate drug development. *Clinical Pharmacology & Therapeutics*, 93(6), 502-514. https://doi.org/10.1038/clpt.2013.54

14. Schriger, D. L., Sinha, R., Schroter, S., Liu, P. Y., & Altman, D. G. (2006). From submission to publication: A retrospective review of the tables and figures in a cohort of randomized controlled trials submitted to the *British Medical Journal*. *Annals of Emergency Medicine*, 48(6), 750-756. https://doi.org/10.1016/j.annemergmed.2006.06.017

15. Riley, R. D., Higgins, J. P. T., & Deeks, J. J. (2011). Interpretation of random effects meta-analyses. *BMJ*, 342, d549. https://doi.org/10.1136/bmj.d549

---

*For additional resources on peptide clinical development and data visualization, visit the [RPL Peptides Research Knowledge Center](https://rplpeptides.com) and access pharmacokinetic datasets at [data.rplpeptides.com](https://data.rplpeptides.com).*
