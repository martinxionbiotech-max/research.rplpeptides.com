---
title: Sample Size Determination and Power Analysis in Peptide Research
description: A definitive guide to statistical power analysis, effect size estimation, Type I/II error control, and sample size calculation using G*Power and related tools for rigorous peptide experimentation
---

# Sample Size Determination and Power Analysis in Peptide Research: From Effect Sizes to G*Power Implementation

## Executive Summary

Underpowered experiments are among the most pervasive and costly errors in biomedical research. A study with insufficient sample size cannot reliably detect real effects, wasting resources, animals, and investigator effort on experiments destined to produce inconclusive results. Conversely, overpowered studies consume unnecessary resources and may expose more subjects than required to experimental interventions. This article presents a comprehensive framework for sample size determination and statistical power analysis tailored to the design scenarios most common in peptide research: two-group comparisons of bioactivity, multi-group dose-response experiments, factorial optimization studies, and equivalence/non-inferiority testing for biosimilar peptides. We derive the mathematical relationships connecting sample size, effect size, significance level (α), and statistical power (1 − β), and provide practical protocols for sample size calculation using G*Power, R (`pwr`, `PowerUpR`), and Python (`statsmodels`). Real-world examples illustrate power analysis for common peptide experimental scenarios, including MIC determination for antimicrobial peptides, IC<sub>50</sub> comparisons across peptide variants, and stability study design. Special attention is given to the estimation of effect sizes from pilot data and published literature, the consequences of multiple testing on power, and strategies for sample size re-estimation in adaptive designs. Researchers accessing [RPL Peptides](https://rplpeptides.com) data resources and [RPL Peptides analytical services](https://data.rplpeptides.com) will find actionable workflows for prospectively powering their experiments.

## Background

### The Reproducibility Crisis and the Role of Statistical Power

The biomedical research enterprise has been shaken over the past two decades by mounting evidence that a substantial fraction of published findings cannot be replicated. Landmark surveys have estimated irreproducibility rates of 50–89% across preclinical research domains (Begley & Ellis, 2012; Prinz et al., 2011), with cumulative economic costs exceeding $28 billion annually in the United States alone (Freedman et al., 2015). While multiple factors contribute—publication bias, p-hacking, HARKing (hypothesizing after results are known), inadequate blinding, and reagent variability—insufficient statistical power is consistently identified as a proximal cause of failed replication. An underpowered study not only has a low probability of detecting real effects but, when it does yield a statistically significant result, that result is more likely to be a false positive or to substantially overestimate the true effect magnitude (Button et al., 2013).

The mechanism is counterintuitive but mathematically inescapable. When statistical power is low (e.g., 20%), only large effects achieve significance. But in a low-power study, even the effects that reach significance are sampled from the extreme tail of the sampling distribution, producing inflated effect size estimates. This "winner's curse" means that underpowered studies that happen to produce significant results systematically overstate effect sizes, setting up subsequent studies for failure when they are powered for the inflated estimate rather than the true (smaller) effect.

In peptide research, the consequences manifest concretely. A 2021 meta-analysis of antimicrobial peptide (AMP) studies found that mean sample sizes for in vivo efficacy experiments had not increased over two decades, remaining at n = 5–8 per group, yielding median power of only 35–45% to detect effect sizes typical of the field (Cohen's d ≈ 0.8–1.2) (Lazzaro et al., 2020). Hundreds of peptides reported as "promising" in the literature could not be distinguished from statistical noise. The culture is changing—journal editorial policies increasingly require prospective power analyses, funding agencies demand sample size justifications, and institutional animal care committees will not approve protocols without formal statistical justification of animal numbers—but the transition from post-hoc rationalization to prospective power planning remains incomplete.

### The Neyman-Pearson Framework and the Four Pillars of Power Analysis

Statistical power analysis rests on the Neyman-Pearson framework of hypothesis testing, which conceptualizes statistical inference as a decision between two competing hypotheses: the null hypothesis ($H_0$) and the alternative hypothesis ($H_1$). Every decision carries a risk of error, classified into two types:

| | $H_0$ True | $H_1$ True |
|---|---|---|
| **Fail to reject $H_0$** | Correct (1 − α) | Type II Error (β) |
| **Reject $H_0$** | Type I Error (α) | Correct (1 − β = Power) |

-   **Type I Error (α, false positive):** Rejecting the null hypothesis when it is true. Conventionally set at α = 0.05 (5% risk), though more stringent levels (α = 0.01 or α = 0.001) are appropriate for high-stakes decisions, exploratory studies with many comparisons, or confirmatory trials.
-   **Type II Error (β, false negative):** Failing to reject the null hypothesis when it is false. Conventionally set at β = 0.20 (20% risk), corresponding to statistical power of 0.80 (80%).
-   **Statistical Power (1 − β):** The probability of correctly rejecting the null hypothesis when the alternative hypothesis is true. A power of 0.80 means that, if the hypothesized effect truly exists, the study has an 80% chance of detecting it as statistically significant.

The four quantities—sample size ($n$), effect size ($\delta$), significance level ($\alpha$), and power ($1 - \beta$)—are mathematically interdependent: specifying any three determines the fourth. In prospective power analysis (a priori), $n$ is the unknown, solved from specified values of $\delta$, $\alpha$, and $1 - \beta$. This is the standard approach for experimental planning.

### Historical Context: From Cohen to G*Power

Jacob Cohen's (1988) *Statistical Power Analysis for the Behavioral Sciences* laid the intellectual groundwork for modern power analysis. Cohen introduced standardized effect size measures that remain in universal use: Cohen's *d* for two-group mean comparisons, Cohen's *f* for ANOVA, and Cohen's *w* for chi-square tests. He proposed conventional benchmarks: small ($d = 0.2$), medium ($d = 0.5$), and large ($d = 0.8$) effects. While these labels are useful heuristics, Cohen explicitly cautioned against their mindless application—what constitutes a "large" effect depends entirely on the scientific context. In peptide chemistry, a 2-fold change in antimicrobial activity ($d \approx 0.5$–0.8) may be biologically modest, whereas a 2-fold difference in pharmacokinetic half-life ($d \approx 1.5$–2.0) may be transformative.

G*Power, developed by Faul, Erdfelder, and colleagues at the University of Düsseldorf (Faul et al., 2007, 2009), operationalized Cohen's framework in freely available software that has become the *de facto* standard for power analysis in the life sciences. G*Power supports all major statistical test families (t-tests, F-tests, χ²-tests, z-tests, exact tests), provides both a priori and post-hoc power analyses, and includes graphical tools for exploring the sensitivity of power to parameter choices. The software's widespread adoption (>100,000 citations as of 2024) reflects its balance of statistical rigor and user accessibility, making it the primary tool recommended in [RPL Peptides](https://rplpeptides.com) training materials.

## Core Methodologies for Sample Size and Power Analysis

### Effect Size: The Engine of Power Analysis

Effect size quantifies the magnitude of the phenomenon under investigation, independent of sample size. Unlike p-values, which confound effect magnitude with sample size, effect sizes provide a standardized metric that enables comparison across studies and informs prospective power calculations. The most common effect size measures in peptide research are:

#### Cohen's d (Standardized Mean Difference)

$$d = \frac{\bar{X}_1 - \bar{X}_2}{s_{pooled}}$$

where $\bar{X}_1$ and $\bar{X}_2$ are group means and $s_{pooled}$ is the pooled standard deviation:

$$s_{pooled} = \sqrt{\frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}}$$

Cohen's $d$ expresses the difference between groups in units of standard deviation. A $d$ of 1.0 means the group means differ by one standard deviation—a substantial effect. For peptide bioactivity comparisons, effect sizes can be estimated from pilot data or published literature. For example, if a novel peptide analogue shows mean MIC of 4.0 μg/mL ($s = 1.2$, $n = 5$) versus a lead compound at 8.0 μg/mL ($s = 1.5$, $n = 5$):

$$s_{pooled} = \sqrt{\frac{(4)(1.2^2) + (4)(1.5^2)}{8}} = \sqrt{\frac{5.76 + 9.00}{8}} = 1.36$$

$$d = \frac{8.0 - 4.0}{1.36} = 2.94$$

This very large effect size suggests that even a modest sample size will provide adequate power. However, pilot estimates of $d$ are notoriously imprecise when based on small $n$; a 95% confidence interval for $d$ derived from $n = 5$ per group spans approximately ±1.2, meaning the "true" $d$ could be anywhere from ~1.7 to ~4.1. The prudent approach is to power for the lower bound of the confidence interval to ensure adequate power under conservative assumptions.

#### Cohen's f (for ANOVA and Factorial Designs)

$$f = \sqrt{\frac{\eta^2}{1 - \eta^2}}$$

where $\eta^2 = SS_{effect} / SS_{total}$ (eta-squared, the proportion of total variance attributable to the effect). Cohen's benchmarks for $f$ are 0.10 (small), 0.25 (medium), and 0.40 (large). For a peptide dose-response experiment with 4 dose levels, an $f$ of 0.35 (between medium and large) would be typical for a robust dose-response relationship.

#### Hedges' g (Bias-Corrected Standardized Mean Difference)

Hedges' $g$ applies a correction factor to Cohen's $d$ to produce an unbiased estimate of the population effect size, particularly important when $n < 20$:

$$g = d \times \left(1 - \frac{3}{4(n_1 + n_2) - 9}\right)$$

For $n_1 = n_2 = 5$, $d = 1.0$ becomes $g = 1.0 \times (1 - 3/31) = 0.903$. The correction is nontrivial and should be applied when reporting effect sizes from small-sample peptide experiments.

#### Eta-Squared ($\eta^2$) and Partial Eta-Squared ($\eta_p^2$)

For ANOVA models, $\eta^2$ measures the proportion of variance explained:

$$\eta^2 = \frac{SS_{effect}}{SS_{total}}$$

$$\eta_p^2 = \frac{SS_{effect}}{SS_{effect} + SS_{error}}$$

Partial $\eta^2$ excludes variance from other model terms from the denominator and is therefore always larger than $\eta^2$ in multi-factor designs. G*Power uses $f$ as the input effect size for ANOVA power calculations, with the conversion $f = \sqrt{\eta_p^2 / (1 - \eta_p^2)}$. When reporting $\eta_p^2$ from published studies, investigators at [RPL Peptides](https://rplpeptides.com) convert to $f$ for power analysis of follow-up experiments.

### Statistical Power Analysis by Experimental Design

#### Two-Group Comparisons (Independent Samples t-Test)

The most common design in peptide research—comparing a test peptide to a control or vehicle group—requires a two-sample t-test (assuming independent groups and approximately normal data). The sample size per group ($n$) for a two-sided t-test is:

$$n = \frac{2(z_{1-\alpha/2} + z_{1-\beta})^2}{d^2} + \frac{z_{1-\alpha/2}^2}{4}$$

where $z_{1-\alpha/2}$ is the critical value for the significance level (1.96 for $\alpha = 0.05$, two-tailed) and $z_{1-\beta}$ is the critical value for power (0.842 for 80% power, 1.282 for 90% power).

**Worked Example: Antimicrobial Peptide MIC Comparison**

A researcher wishes to compare the MIC of a novel antimicrobial peptide against that of the parent compound. Based on preliminary data:

-   Expected MIC difference: 2 μg/mL
-   Expected standard deviation: 1.5 μg/mL
-   Desired power: 0.80
-   Significance level: 0.05 (two-tailed)

Effect size: $d = 2 / 1.5 = 1.33$

$$n = \frac{2(1.96 + 0.842)^2}{1.33^2} + \frac{1.96^2}{4} = \frac{2(7.85)}{1.77} + 0.96 = 8.87 + 0.96 = 9.83$$

Rounding up, 10 subjects per group (20 total) are required. G*Power confirms this result: t-tests → Means: Difference between two independent means (two groups) → A priori: d = 1.33, α = 0.05, Power = 0.80, Allocation ratio N2/N1 = 1 → n1 = n2 = 10.

For smaller effect sizes more typical of subtle peptide modifications ($d = 0.6$):

$$n = \frac{2(1.96 + 0.842)^2}{0.6^2} + 0.96 = \frac{15.70}{0.36} + 0.96 = 43.61 + 0.96 \approx 45$$

The dramatic increase from 10 to 45 per group illustrates the inverse squared relationship between $d$ and $n$: halving $d$ quadruples the required sample size. This sensitivity underscores the importance of realistic effect size estimation.

**Table: Required Sample Size Per Group (Independent t-test, α = 0.05, Two-Tailed)**

| Cohen's d | Power = 0.80 | Power = 0.90 | Power = 0.95 |
|-----------|-------------|-------------|-------------|
| 0.2 (small) | 394 | 527 | 651 |
| 0.3 | 176 | 235 | 291 |
| 0.5 (medium) | 64 | 86 | 106 |
| 0.8 (large) | 26 | 35 | 43 |
| 1.0 | 17 | 23 | 28 |
| 1.2 | 12 | 17 | 20 |
| 1.5 | 9 | 11 | 14 |
| 2.0 | 6 | 7 | 9 |

The table starkly illustrates why peptide studies with $n = 3$–$4$ per group cannot reliably detect anything but massive effects ($d > 2.0$). At [RPL Peptides](https://rplpeptides.com), we recommend a minimum of $n = 6$ per group for two-group comparisons, which provides 80% power for $d \approx 1.7$—achievable for large peptide effects but inadequate for the moderate effects that characterize most peptide optimization studies.

#### Multi-Group Comparisons (One-Way ANOVA)

When comparing three or more peptide variants, dose levels, or time points, one-way ANOVA replaces the t-test. The required sample size depends on the number of groups ($k$), the effect size ($f$), and the desired power:

$$n = \frac{\lambda}{f^2}$$

where $\lambda$ is the noncentrality parameter of the F-distribution, obtained from tables or software for given $k$, $\alpha$, and power. G*Power automates this calculation.

**Worked Example: Alanine-Scanning Mutagenesis Study**

A researcher generates 7 alanine-substituted variants of a lead peptide plus the parent peptide, for $k = 8$ groups. Pilot data suggest a large effect ($f = 0.40$) with α = 0.05 and power = 0.80. G*Power output:

-   F-tests → ANOVA: Fixed effects, omnibus, one-way
-   Effect size $f$: 0.40
-   α: 0.05
-   Power: 0.80
-   Number of groups: 8
-   **Total sample size: 104** → approximately 13 per group

With post-hoc pairwise comparisons (Tukey HSD), the power for detecting specific group differences is lower than the omnibus power. For 28 pairwise comparisons among 8 groups, the Tukey-adjusted critical difference is larger, requiring the observed difference to be proportionally larger to achieve significance. Power for pairwise comparisons can be assessed in G*Power using the "post-hoc" analysis with the adjusted critical value.

#### Factorial Designs and Multi-Way ANOVA

For 2<sup>k</sup> factorial designs, power analysis addresses each effect (main effects and interactions) separately. The effect size $f$ for each term is:

$$f = \sqrt{\frac{\eta_p^2}{1 - \eta_p^2}}$$

where $\eta_p^2$ is the partial eta-squared for that term. Crucially, interactions typically have smaller effect sizes than main effects, requiring larger sample sizes for equivalent power. A practical rule: when planning a factorial experiment, power for the smallest interaction of interest.

**Worked Example: 2 × 3 Factorial (Peptide Formulation Study)**

Two formulation factors: buffer (phosphate vs. citrate, 2 levels) and pH (5.0, 7.0, 9.0, 3 levels), giving a 2 × 3 factorial (6 treatment combinations). The smallest interaction effect of interest is $f = 0.25$ (medium). G*Power:

-   F-tests → ANOVA: Fixed effects, special, main effects and interactions
-   Effect size $f$: 0.25
-   α: 0.05
-   Power: 0.80
-   Numerator df: (2−1)(3−1) = 2
-   Number of groups: 6
-   **Total sample size: 96** → 16 per group

#### Equivalence and Non-Inferiority Testing

Standard superiority testing cannot establish equivalence (that two peptides are "the same")—failure to reject $H_0$ is not evidence of no difference. Equivalence testing flips the hypotheses: $H_0$ is that the difference exceeds a predefined equivalence margin ($\Delta$), and $H_1$ is that the difference lies within $\pm\Delta$. This requires a larger sample size than superiority testing because the test is two one-sided tests (TOST) at $\alpha/2$ each.

For a two-group equivalence test of means with equivalence margin $\Delta = 0.5\sigma$:

$$n = \frac{2(z_{1-\alpha} + z_{1-\beta/2})^2}{(|\delta| - \Delta)^2 / \sigma^2}$$

for $\delta$ within the equivalence margin. For $\delta = 0$, $\Delta = 0.5\sigma$, $\alpha = 0.05$, power = 0.80:

$$n = \frac{2(1.645 + 1.282)^2}{0.5^2} = \frac{2(8.57)}{0.25} = 68.5$$

Thus, 69 per group—substantially more than the 10 per group needed for superiority testing with $d = 1.33$. Equivalence testing for peptide biosimilarity is resource-intensive and should be planned prospectively.

### G*Power: Practical Implementation

G*Power 3.1 (Faul et al., 2009) provides a graphical interface organized around test families. The basic workflow:

1.  **Select Test Family.** t-tests (means comparisons), F-tests (ANOVA, regression), χ²-tests (proportions, contingency tables), z-tests (proportions, correlations), Exact tests (nonparametric).

2.  **Select Statistical Test.** Within the family, choose the specific test matching the experimental design (e.g., "Means: Difference between two independent means (two groups)").

3.  **Select Type of Power Analysis.**
    -   *A priori:* Compute required sample size given α, power, and effect size. **Primary choice for experimental planning.**
    -   *Post-hoc:* Compute achieved power given α, effect size, and sample size. Useful for evaluating completed experiments or published studies.
    -   *Compromise:* Compute α and β given their ratio and effect size/sample size. Rarely used.
    -   *Criterion:* Compute α and decision criterion given effect size, power, and sample size. Useful for setting critical values in specific scenarios.
    -   *Sensitivity:* Compute the minimum detectable effect size given α, power, and sample size. Extremely useful for interpreting null results.

4.  **Input Parameters.** Enter effect size, α, power, allocation ratio ($N_2/N_1$ for two groups), and for ANOVA, numerator degrees of freedom and number of groups.

5.  **Calculate.** G*Power outputs required total sample size (and per-group sizes) along with critical t/F values.

**G*Power Example Script (R equivalent using `pwr` package):**

```r
library(pwr)

# Two-group comparison (independent t-test)
pwr.t.test(d = 0.8, sig.level = 0.05, power = 0.80, 
           type = "two.sample", alternative = "two.sided")
# Output: n = 25.5 per group → round to n = 26

# One-way ANOVA (4 groups, f = 0.30)
pwr.anova.test(k = 4, f = 0.30, sig.level = 0.05, power = 0.80)
# Output: n = 27.6 per group → round to n = 28

# Power curve: vary sample size
n_seq <- seq(10, 100, by = 5)
power_vals <- sapply(n_seq, function(n) {
  pwr.t.test(n = n, d = 0.5, sig.level = 0.05, 
             type = "two.sample", alternative = "two.sided")$power
})
plot(n_seq, power_vals, type = "l", lwd = 2,
     xlab = "Sample Size per Group", ylab = "Power",
     main = "Power Curve: d = 0.5, α = 0.05")
abline(h = 0.80, lty = 2, col = "red")
```

The power curve visualization is particularly instructive: power increases rapidly from low to moderate sample sizes but asymptotically approaches 1.0, with diminishing returns beyond ~85% power. The 80% convention represents a pragmatic balance between resource investment and inferential security.

### Sample Size Considerations for Specialized Peptide Experiments

#### Crossover Designs

Crossover designs, in which each subject receives multiple treatments in sequence, reduce between-subject variability by using subjects as their own controls. For a 2 × 2 crossover (two treatments, two periods), the sample size for detecting a treatment difference of $d$ is:

$$n = \frac{(z_{1-\alpha/2} + z_{1-\beta})^2 \sigma_d^2}{\delta^2}$$

where $\sigma_d^2$ is the within-subject variance of the treatment difference, typically (substantially) smaller than the between-subject variance. Crossover designs can achieve equivalent power with 50–75% fewer subjects than parallel-group designs, provided carryover effects are negligible and the condition is stable. For peptide pharmacokinetic studies with low within-subject variability ($CV_w \approx 15–25\%$), crossover designs of $n = 12$–$18$ subjects routinely achieve 90% power for detecting a 20% difference in AUC.

#### Repeated Measures and Longitudinal Designs

Peptide stability studies, time-course bioactivity experiments, and in vivo efficacy studies with multiple measurement time points require sample size calculations that account for the correlation among repeated measures. The variance of a treatment effect in a repeated measures design with $m$ measurement times and intra-subject correlation $\rho$ is:

$$\text{Var}(\hat{\delta}) = \frac{\sigma^2[1 + (m-1)\rho]}{n \cdot m}$$

The effective sample size is not $n \times m$ but a function of $\rho$: as $\rho \to 1$, repeated measures add no information beyond the first measurement; as $\rho \to 0$, each measure contributes independently. G*Power's "Repeated measures, within-between interaction" test under F-tests → ANOVA addresses these designs. For peptide degradation studies with high intra-assay correlation ($\rho > 0.8$), additional time points provide diminishing returns; increasing biological replicates is more power-efficient than increasing technical replicates.

#### Cluster-Randomized and Hierarchical Designs

When peptide treatments are administered to groups (e.g., treatment vs. control cages in animal studies, or 96-well plates with wells as experimental units), observations within clusters are correlated. The design effect inflates required sample size:

$$\text{Design Effect} = 1 + (m - 1) \cdot \text{ICC}$$

where $m$ is the average cluster size and ICC is the intraclass correlation coefficient. For an animal study with $m = 5$ mice per cage and ICC = 0.3 (moderate cage effects):

$$\text{Design Effect} = 1 + (5 - 1)(0.3) = 2.2$$

The sample size must be multiplied by 2.2, meaning 22 mice per group are required where 10 would suffice in a non-clustered design. Ignoring clustering produces grossly underpowered studies—a common error in preclinical peptide research recognized in the ARRIVE guidelines for animal experimentation (Percie du Sert et al., 2020).

### Power and Multiple Testing

Peptide research frequently involves multiple comparisons: many peptide variants tested against a control, many endpoints measured, many time points analyzed. Each additional comparison inflates the family-wise error rate (FWER, the probability of at least one Type I error among all tests). With 10 independent tests at α = 0.05, FWER = 1 − (0.95)<sup>10</sup> = 0.401—a 40% chance of at least one false positive.

Corrections for multiplicity (Bonferroni, Holm, Hochberg, Benjamini-Hochberg) control the error rate at the cost of reduced power. The Bonferroni-adjusted α for $m$ comparisons is $\alpha_{adj} = \alpha / m$. For 10 comparisons, $\alpha_{adj} = 0.005$. The sample size increase to maintain power at this stringent α level depends on the design, but for a two-group t-test with $d = 0.8$, power = 0.80:

-   Unadjusted (α = 0.05): $n = 26$ per group
-   Bonferroni (α = 0.005): $n = 42$ per group

The 60% increase in sample size required to maintain power after multiplicity correction is often unappreciated in peptide research. At [RPL Peptides](https://rplpeptides.com), our experimental design consultations emphasize treating multiple comparisons as a power issue from the outset: either specify a limited number of primary endpoints (reducing $m$) or increase sample size to compensate for multiplicity adjustment.

### Adaptive Designs and Sample Size Re-Estimation

Traditional power analysis requires an effect size estimate that may be uncertain, particularly in novel peptide research areas. Adaptive designs allow sample size re-estimation at an interim analysis without inflating the Type I error rate (provided the adaptation rule is prespecified). Two approaches are well-established:

**Blinded Sample Size Re-Estimation (BSSR).** At an interim point (e.g., after 50% of planned enrollment), the pooled variance estimate is updated without unblinding treatment assignments. If the estimated variance exceeds the planning value, sample size is increased to maintain target power. BSSR controls Type I error without α penalty because no treatment effect information is used to modify the design.

**Unblinded Sample Size Re-Estimation (UBSSR) with Combination Tests.** When unblinded interim results inform sample size adjustment, the final analysis must use a combination test (e.g., inverse normal method) or weighted test statistics to combine evidence from the pre- and post-adaptation stages. The α is partitioned between stages, and the final test statistic is a weighted combination of stage-wise p-values. This methodology, developed for clinical trials, is increasingly applied to larger preclinical programs.

Both approaches are computationally accessible: the `rpact` package in R and East software (Cytel) implement adaptive designs for a variety of endpoints. For peptide research programs with substantial resource investment (>$10,000 or >100 animals), adaptive designs offer a principled approach to sample size uncertainty.

## Research Evidence

| Study | Focus | Key Finding | Reference |
|-------|-------|-------------|-----------|
| Cohen (1988) | Foundational power analysis | Established standardized effect sizes (d, f, w) and conventional benchmarks | Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences*. 2nd ed. Erlbaum. |
| Faul et al. (2009) | G*Power software | Developed G*Power 3.1; validated across test families | Faul, F., et al. (2009). *Behav Res Methods*, 41(4), 1149–1160. |
| Button et al. (2013) | Power in neuroscience | Median power ~21%; low power inflates effect sizes and false positive rates | Button, K. S., et al. (2013). *Nat Rev Neurosci*, 14(5), 365–376. |
| Begley & Ellis (2012) | Reproducibility in preclinical research | Only 11% of landmark oncology studies replicated; power deficiency cited | Begley, C. G., & Ellis, L. M. (2012). *Nature*, 483(7391), 531–533. |
| Lazzaro et al. (2020) | AMP study meta-analysis | Median n = 5–8 per group; power 35–45% for typical effects | Lazzaro, B. P., et al. (2020). *Philos Trans R Soc B*, 375(1807), 20190584. |
| Freedman et al. (2015) | Economics of irreproducibility | $28B annual cost; power deficiency major contributor | Freedman, L. P., et al. (2015). *PLoS Biol*, 13(6), e1002165. |
| Lakens (2013) | Effect size reporting | Systematic guide to calculating and reporting effect sizes | Lakens, D. (2013). *Front Psychol*, 4, 863. |
| Percie du Sert et al. (2020) | ARRIVE 2.0 guidelines | Mandated sample size justification including power analysis | Percie du Sert, N., et al. (2020). *PLoS Biol*, 18(7), e3000410. |
| Jennison & Turnbull (2000) | Adaptive designs | Established group sequential and adaptive design methodology | Jennison, C., & Turnbull, B. W. (2000). *Group Sequential Methods*. Chapman & Hall. |
| Krzywinski & Altman (2013) | Power and sample size tutorial | Emphasized effect size uncertainty and conservative planning | Krzywinski, M., & Altman, N. (2013). *Nat Methods*, 10(12), 1139–1140. |
| Ioannidis (2005) | "Why Most Published Research Findings Are False" | Low power increases PPV of significant findings through winner's curse | Ioannidis, J. P. A. (2005). *PLoS Med*, 2(8), e124. |
| Cumming (2014) | New statistics (estimation, not testing) | Advocated estimation-based inference over NHST; effect sizes with CIs | Cumming, G. (2014). *Psychol Sci*, 25(1), 7–29. |

## Frequently Asked Questions

<div class="faq-item" markdown="1">

### What is the minimum sample size for a peptide study to be publishable?

There is no universal minimum, but journals increasingly expect sample sizes justified by power analysis rather than by convention. For two-group comparisons, $n = 3$ per group cannot achieve significance at α = 0.05 regardless of effect size (the minimum $p$-value from a t-test with $n = 3$ per group, assuming equal means and maximum separation, is $p = 0.10$ for a two-tailed test). At $n = 4$, significance is possible but requires $d > 2.5$, which is unrealistic for most peptide experiments. A minimum of $n = 5$–$6$ per group is our pragmatic floor at [RPL Peptides](https://rplpeptides.com), corresponding to 80% power for $d \approx 1.8$—achievable for robust effects but inadequate for the moderate effects typical of peptide optimization. Whenever possible, conduct a formal power analysis; when impossible (truly novel peptide, no effect size data), power for a conservative $d = 0.5$–$0.8$.

</div>

<div class="faq-item" markdown="1">

### How do I estimate effect size when I have no prior data?

When no pilot data exist, estimate effect size from: (a) **published literature on related peptides**—extract means and SDs from figures using WebPlotDigitizer, calculate $d$ or $\eta^2$, and adjust conservatively; (b) **minimally important difference (MID)**—what change in the response variable would be biologically or clinically meaningful, regardless of statistical significance? Then divide by an assumed SD; (c) **Cohen's benchmarks**—use $d = 0.5$ (medium) as a default with explicit acknowledgment that this is a placeholder. At [RPL Peptides](https://rplpeptides.com), we recommend the MID approach: a peptide that improves antimicrobial activity by 2-fold (log<sub>2</sub> difference of 1) may be the smallest effect worth pursuing, regardless of what pilot data show. Power for that MID; if the effect is larger, you have surplus power (welcome); if smaller, the result is not operationally meaningful anyway.

</div>

<div class="faq-item" markdown="1">

### What power should I target—80%, 90%, or higher?

Target 80% (β = 0.20) for exploratory/discovery-stage peptide research where Type II errors delay but do not terminate programs. Target 90% (β = 0.10) for confirmatory experiments that gate go/no-go decisions (e.g., selecting a lead peptide for IND-enabling studies). In practice, the incremental cost of increasing power from 80% to 90% is roughly 30–35% additional sample size—worthwhile when the cost of a false negative (discarding a truly active peptide) is high. At the resource-constrained extreme, 70% power may be the best achievable, but the limitations must be transparently acknowledged. At [RPL Peptides](https://rplpeptides.com), our standard is 80% for internal decision-making and 90% for external-facing (publication, regulatory) experiments.

</div>

<div class="faq-item" markdown="1">

### Should I use one-tailed or two-tailed tests in my power analysis?

Almost always use two-tailed tests in peptide research. One-tailed tests are appropriate only when a difference in the unexpected direction would be interpreted identically to no difference—that is, when the research question is strictly directional and there is zero scientific interest in a result in the opposite direction. Even in peptide optimization, where "new peptide is better than old peptide" is the directional hypothesis, a result in the opposite direction (new peptide is *worse*, potentially due to unexpected toxicity, aggregation, or degradation) is scientifically important and must be detectable. Two-tailed tests protect against this. Regulatory agencies (FDA, EMA) uniformly expect two-tailed testing; journals increasingly require justification for one-tailed tests.

</div>

<div class="faq-item" markdown="1">

### How do I handle dropout, missing data, or technical failures in power analysis?

Inflate the sample size to account for expected attrition. If pilot studies or laboratory experience suggests a 15% failure rate (failed synthesis, contaminated cultures, animal mortality, unanalyzable samples), divide the calculated sample size by (1 − 0.15) = 0.85. For $n = 20$ per group, the inflated target is $n = 20 / 0.85 = 24$ per group. This is separate from and in addition to the power-based inflation. Document the attrition rate assumption; if actual attrition differs during the experiment, report the effective sample size honestly. The [RPL Peptides data platform](https://data.rplpeptides.com) provides attrition-tracking templates that integrate with power calculations.

</div>

<div class="faq-item" markdown="1">

### Can I do a post-hoc power analysis to explain a non-significant result?

Post-hoc (retrospective) power analysis—computing power using the observed effect size—is logically circular and widely discouraged (Hoenig & Heisey, 2001). It simply maps the observed p-value onto the power curve: a non-significant result always corresponds to low post-hoc power, and a significant result to high post-hoc power—the calculation adds no new information. The appropriate post-hoc analysis is a **sensitivity analysis**: given the achieved sample size, what is the smallest effect size that the study had 80% power to detect? This defines the detection limit of the experiment. For example: "With $n = 8$ per group, we had 80% power to detect $d \geq 1.45$. Effects smaller than this would not have been detectable; therefore, absence of evidence for effects below this threshold should not be interpreted as evidence of absence."

</div>

<div class="faq-item" markdown="1">

### How do I determine sample size for nonparametric tests (Mann-Whitney, Kruskal-Wallis)?

Nonparametric tests have approximately 95% of the power of their parametric counterparts when the normality assumption holds (asymptotic relative efficiency, ARE = 3/π ≈ 0.955 for Mann-Whitney vs. t-test). To plan for a nonparametric test: (1) calculate sample size for the parametric equivalent; (2) divide by 0.95 to adjust for efficiency loss. For example, if a t-test requires $n = 26$ per group, a Mann-Whitney test requires $n = 26 / 0.95 \approx 28$ per group. G*Power includes exact power calculations for nonparametric tests under the "Exact" test family for small samples; for larger samples, the asymptotic adjustment is adequate.

</div>

<div class="faq-item" markdown="1">

### What is the relationship between p-value, effect size, and sample size?

The p-value is a function of both effect size and sample size: $p = f(\text{effect size} \times \sqrt{n})$. A trivial effect can achieve a small p-value with a large enough sample; a large effect can yield a large (non-significant) p-value with a small sample. This is why reporting effect sizes and confidence intervals is mandatory alongside p-values. A finding of $d = 0.15$ with $p = 0.001$ and $n = 1000$ per group represents a trivially small effect detected through overwhelming sample size; conversely, $d = 1.5$ with $p = 0.12$ and $n = 6$ per group may represent a substantial effect in an underpowered study. Neither p < 0.05 nor p > 0.05 is adequately informative without the accompanying effect size and precision.

</div>

<div class="faq-item" markdown="1">

### How do I handle sample size for factorial designs when I care about both main effects and interactions?

Power for each effect (each main effect, each interaction) in a factorial design is calculated separately. The effect with the smallest expected $f$ or the fewest degrees of freedom governs the overall sample size requirement. In peptide research, two-factor interactions often have smaller effect sizes than main effects and therefore require larger samples. A practical approach: (1) specify the smallest interaction effect of scientific interest; (2) calculate $n$ for that interaction; (3) use that $n$ for the entire experiment, which will provide adequate or surplus power for main effects. If a specific interaction is the primary hypothesis, power specifically for that interaction; if main effects are primary and interactions are secondary, power for the main effects and accept lower power for interaction detection.

</div>

<div class="faq-item" markdown="1">

### What sample size planning resources does RPL Peptides provide?

[RPL Peptides](https://rplpeptides.com) provides integrated power analysis support through the [RPL Peptides data platform](https://data.rplpeptides.com), including: (1) an interactive sample size calculator supporting t-tests, ANOVA, equivalence tests, and factorial designs with peptide-relevant defaults; (2) a curated library of effect sizes extracted from published peptide literature (MIC, IC<sub>50</sub>, pharmacokinetic parameters) to inform planning estimates; (3) G*Power template files (.gpa) for common peptide experimental designs; and (4) statistical consultation services for complex designs. Our design review process requires prospective power analysis documentation before initiation of resource-intensive experiments exceeding specified cost or animal-use thresholds.

</div>

## References

1.  Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences* (2nd ed.). Lawrence Erlbaum Associates. doi:10.4324/9780203771587

2.  Faul, F., Erdfelder, E., Buchner, A., & Lang, A. G. (2009). Statistical power analyses using G*Power 3.1: Tests for correlation and regression analyses. *Behavior Research Methods*, 41(4), 1149–1160. doi:10.3758/BRM.41.4.1149

3.  Faul, F., Erdfelder, E., Lang, A. G., & Buchner, A. (2007). G*Power 3: A flexible statistical power analysis program for the social, behavioral, and biomedical sciences. *Behavior Research Methods*, 39(2), 175–191. doi:10.3758/BF03193146

4.  Button, K. S., Ioannidis, J. P. A., Mokrysz, C., et al. (2013). Power failure: Why small sample size undermines the reliability of neuroscience. *Nature Reviews Neuroscience*, 14(5), 365–376. doi:10.1038/nrn3475

5.  Begley, C. G., & Ellis, L. M. (2012). Raise standards for preclinical cancer research. *Nature*, 483(7391), 531–533. doi:10.1038/483531a

6.  Ioannidis, J. P. A. (2005). Why most published research findings are false. *PLoS Medicine*, 2(8), e124. doi:10.1371/journal.pmed.0020124

7.  Freedman, L. P., Cockburn, I. M., & Simcoe, T. S. (2015). The economics of reproducibility in preclinical research. *PLoS Biology*, 13(6), e1002165. doi:10.1371/journal.pbio.1002165

8.  Lakens, D. (2013). Calculating and reporting effect sizes to facilitate cumulative science: A practical primer for t-tests and ANOVAs. *Frontiers in Psychology*, 4, 863. doi:10.3389/fpsyg.2013.00863

9.  Hoenig, J. M., & Heisey, D. M. (2001). The abuse of power: The pervasive fallacy of power calculations for data analysis. *The American Statistician*, 55(1), 19–24. doi:10.1198/000313001300339897

10. Krzywinski, M., & Altman, N. (2013). Points of significance: Power and sample size. *Nature Methods*, 10(12), 1139–1140. doi:10.1038/nmeth.2738

11. Cumming, G. (2014). The new statistics: Why and how. *Psychological Science*, 25(1), 7–29. doi:10.1177/0956797613504966

12. Percie du Sert, N., Hurst, V., Ahluwalia, A., et al. (2020). The ARRIVE guidelines 2.0: Updated guidelines for reporting animal research. *PLoS Biology*, 18(7), e3000410. doi:10.1371/journal.pbio.3000410

13. Jennison, C., & Turnbull, B. W. (2000). *Group Sequential Methods with Applications to Clinical Trials*. Chapman & Hall/CRC. doi:10.1201/9780367805326

14. Lazzaro, B. P., Zasloff, M., & Rolff, J. (2020). Antimicrobial peptides: Application informed by evolution. *Philosophical Transactions of the Royal Society B*, 375(1807), 20190584. doi:10.1098/rstb.2019.0584

15. Prinz, F., Schlange, T., & Asadullah, K. (2011). Believe it or not: How much can we rely on published data on potential drug targets? *Nature Reviews Drug Discovery*, 10(9), 712–713. doi:10.1038/nrd3439-c1

