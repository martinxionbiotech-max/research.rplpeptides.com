---
title: "Analytical Data Visualization in Peptide Science: Chromatograms, Spectra, and Statistical Graphics"
description: "A comprehensive guide to visualizing analytical chemistry data for peptides — HPLC chromatogram interpretation, mass spectrometry plots, CD spectra, NMR contours, and statistical analysis graphics."
slug: analytical-data-visualization
category: Interactive Figures
tags: [Analytical Chemistry, HPLC, Mass Spectrometry, CD Spectroscopy, NMR, Statistical Graphics, Data Visualization]
author: RPL Peptides Research Team
published: 2026-08-07
---

# Analytical Data Visualization in Peptide Science: Chromatograms, Spectra, and Statistical Graphics

## Executive Summary

Analytical data visualization transforms raw detector signals and spectral acquisitions into interpretable evidence of peptide identity, purity, and structural integrity. This article provides a systematic guide to the visualization conventions, interpretation strategies, and publication standards for the four central analytical techniques in peptide characterization: reversed-phase HPLC chromatograms, mass spectrometry data (LC-MS and MS/MS), circular dichroism (CD) spectroscopy, and nuclear magnetic resonance (NMR) spectroscopy. We also address the statistical graphics — box plots, PCA scores plots, and control charts — that underpin analytical method validation and quality-by-design workflows. Each section provides practical annotation and overlay strategies that bridge the gap between raw instrument output and the polished, information-dense figures expected by journals and regulatory reviewers. For peptides produced under rigorous analytical quality control standards, [RPL Peptides](https://rplpeptides.com) provides full analytical documentation, with downloadable COA data available at [data.rplpeptides.com](https://data.rplpeptides.com).

## Background

Analytical chemistry is the evidentiary backbone of peptide science. Every claim about a peptide — its sequence, its purity, its folded state, its stability — rests on an analytical measurement, and every analytical measurement is communicated through a figure. The chromatogram on a Certificate of Analysis, the mass spectrum in a characterization report, the CD spectrum in a folding study, and the NMR HSQC contour plot in a structure paper are not merely images; they are arguments. A well-designed analytical figure makes its argument clear and its evidence accessible. A poorly designed one buries critical information under default software settings, inadequate annotation, or misleading axis scaling.

The field has matured considerably in the past two decades. Where early peptide characterization papers relied on single-wavelength HPLC traces and low-resolution mass spectra, modern analytical workflows integrate multiple orthogonal techniques into unified visualization frameworks. A contemporary peptide characterization figure might overlay UV chromatographic traces at three wavelengths, annotate the integrated peaks with MS-identified masses, and include an inset showing the deconvoluted mass spectrum — all in a single multipanel figure. This integration reflects a deeper truth: no single analytical technique is sufficient, and the most informative visualizations are those that synthesize evidence across techniques.

This article is organized by technique, with each section covering instrument fundamentals, data interpretation, figure design principles, and common pitfalls. The statistical graphics section at the end addresses the visualization needs of method validation, batch analysis, and stability studies — the quantitative context that surrounds every analytical measurement.

## HPLC Chromatogram Visualization

### The Anatomy of a Publication-Quality Chromatogram

A reversed-phase HPLC chromatogram plots detector response (absorbance units, mAU) against time (minutes). For peptide analysis at 214–220 nm (the peptide bond absorption region), a properly annotated figure communicates more than purity — it reveals retention behavior, peak symmetry, baseline quality, and the presence or absence of closely eluting impurities.

The essential annotations on a publication-quality chromatogram include:

1. **Axis labels with units**: "Time (min)" on the x-axis, "Absorbance at 214 nm (mAU)" on the y-axis.
2. **Detection wavelength**: Prominently stated, because purity at 214 nm differs from purity at 280 nm.
3. **Main peak label**: The retention time (tR) and integrated area or area percent.
4. **Impurity peak annotations**: Retention times and relative areas for any peaks exceeding 0.1% of total area.
5. **Integration marks**: Tick marks or vertical lines at peak boundaries. Their placement directly determines the reported purity.
6. **Baseline trace**: The chromatogram should include a blank injection overlay or an inset showing baseline noise level and drift.
7. **Column and method summary**: Column dimensions, particle size, mobile phase composition, gradient profile, flow rate, and temperature — either in the figure legend or as a compact table inset.

### Multi-Wavelength Overlay Techniques

Peptide purity assessment at a single wavelength can be misleading. Co-eluting impurities with different UV absorption profiles may escape detection. The solution is multi-wavelength chromatogram overlay, which displays the same chromatographic run monitored at multiple wavelengths — typically 214 nm (peptide bond), 254 nm (aromatic side chains, particularly Phe and Trp), and 280 nm (Tyr and Trp).

A multi-wavelength overlay figure follows a specific visual grammar:

- Each wavelength trace is rendered in a distinct color: 214 nm in blue, 254 nm in green, 280 nm in red.
- Traces share a common time axis but may have independent y-axes (stacked vertically) or, more commonly, a single y-axis normalized to the main peak height at 214 nm. The latter approach makes relative absorbance differences immediately apparent.
- If an impurity peak at a given retention time appears at 214 nm but is absent or reduced at 254 or 280 nm, it likely lacks aromatic residues — consistent with a deletion peptide or a truncated synthesis byproduct.
- Conversely, an impurity that appears disproportionately large at 280 nm relative to 214 nm may contain oxidized Trp or Tyr residues, which absorb more strongly at 280 nm than their reduced counterparts.

The overlay strategy also applies to purity verification across orthogonal methods. A figure panel combining an HPLC-UV trace with the corresponding total ion chromatogram (TIC) from LC-MS can demonstrate that all UV-detectable components have been mass-identified, closing the mass-balance loop.

### Gradient Profile Annotation

For gradient elution methods, the gradient profile (% organic phase vs. time) should be overlaid on the chromatogram as a dashed or dotted line, plotted against a secondary y-axis on the right side of the figure. This annotation serves two purposes: it reveals whether the peptide elutes during the gradient ramp (desirable) or during the column wash at high organic (undesirable, suggesting inadequate retention), and it allows the reader to assess whether the impurity peaks are well-resolved from the gradient endpoints.

The annotation should include:

- Starting %B, ramp rate (%B/min), final %B, and hold time.
- The column void time (t₀) marked as a vertical dashed line, calculated from column volume and flow rate: t₀ = V_column / flow rate (for a 4.6 × 250 mm column, V_column ≈ 2.5 mL; at 1.0 mL/min, t₀ ≈ 2.5 min).
- The gradient delay volume, if known, which offsets the apparent gradient arrival time.

### Peak Purity and Diode Array Detection Visualization

Diode array detection (DAD) captures full UV spectra across the chromatographic peak, enabling peak purity assessment. Visualization of DAD data typically takes one of two forms:

**Peak purity contour plot**: The x-axis is retention time, the y-axis is wavelength (210–400 nm), and the color intensity represents absorbance. A pure component produces a single, symmetrical contour centered on the peak apex. An impure peak shows multiple, overlapping contour maxima, often with asymmetrical shapes.

**Overlaid UV spectra at multiple time points**: UV spectra extracted from the leading edge, apex, and trailing edge of the chromatographic peak are normalized to the apex maximum and overlaid. For a pure compound, all three spectra superimpose perfectly. For a co-eluting mixture, the spectra differ — the leading-edge spectrum may show increased absorbance at longer wavelengths, while the trailing edge may differ in its short-wavelength profile.

The peak purity index (or match factor) reported by the instrument software quantifies spectral similarity across the peak; values above 990 (out of 1000) generally indicate a spectrally pure peak. This value should be reported in the figure caption alongside the chromatogram.

## Mass Spectrometry Data Visualization

### Full-Scan Mass Spectrum Presentation

A full-scan mass spectrum (MS¹) plots relative abundance (or intensity) against mass-to-charge ratio (m/z). For peptide characterization, the spectrum should be presented with clear annotation of the following:

- **Charge state envelope**: Multiply charged ions ([M+nH]ⁿ⁺) produce a characteristic series of peaks. Each peak's m/z is related to the molecular mass M by m/z = (M + n × 1.0078)/n, where 1.0078 Da is the mass of a proton. The charge state envelope is the visual signature of electrospray ionization of peptides.
- **Base peak**: The most intense peak, normalized to 100% relative abundance. All other peaks are reported as percentages of this maximum.
- **Isotopic distribution**: For charge states z ≤ 5, the isotopic peaks (M, M+1, M+2, etc.) should be resolved. The spacing between adjacent isotopic peaks equals 1/z Da, providing an independent charge state determination.
- **Adduct ions**: Sodium (+22 Da), potassium (+38 Da), and ammonium (+17 Da) adducts may appear alongside protonated ions. Sodium adducts are particularly common when glassware or mobile phase contains sodium salts.

The figure should span an m/z range that captures all charge states, typically 100–2000 m/z for ESI-MS of peptides up to ~5000 Da. The y-axis label should read "Relative Abundance (%)" and the x-axis "m/z."

### Deconvolution Spectra

Because multiply charged ions complicate direct mass assignment, most peptide mass spectra are presented alongside a deconvoluted (zero-charge) spectrum that transforms the charge state envelope into a single peak at the neutral molecular mass. The deconvolution algorithm (typically MaxEnt or ReSpect in Waters MassLynx, or the Bayesian reconstruct tool in Thermo BioPharma Finder) should be specified in the figure legend.

The deconvoluted spectrum is plotted as relative abundance vs. mass (Da), with the main peak annotated with the monoisotopic mass (M) and, in brackets, the average mass. The mass accuracy — the difference between the measured mass and the theoretical mass based on the peptide sequence — should be reported in ppm:

$$ \text{Mass accuracy (ppm)} = \frac{M_{\text{measured}} - M_{\text{theoretical}}}{M_{\text{theoretical}}} \times 10^6 $$

For high-resolution instruments (Q-TOF, Orbitrap), mass accuracy below 5 ppm is expected and provides strong evidence of correct sequence assignment.

### MS/MS Fragmentation Spectra

Tandem mass spectrometry (MS/MS) fragments a selected precursor ion and records the masses of the resulting product ions. For peptide sequencing, collision-induced dissociation (CID) primarily produces b-ions (N-terminal fragments) and y-ions (C-terminal fragments). The MS/MS spectrum is the core evidence for peptide sequence confirmation.

Visualization conventions for MS/MS spectra include:

- **Annotated fragment ions**: b-ions and y-ions are labeled on the spectrum. b-ions are typically shown in blue and y-ions in red, with the ion series index (b₂, b₃, ..., y₂, y₃, ...) placed adjacent to the peak.
- **Sequence coverage map**: An inset or companion panel showing the peptide sequence with b-ion and y-ion cleavage sites marked above and below the sequence, respectively. Confirmed ions are highlighted; missing ions are grayed out.
- **Neutral loss peaks**: Loss of water (−18 Da) or ammonia (−17 Da) from fragment ions produces satellite peaks offset from the main b/y series. These are annotated as bₙ−H₂O or yₙ−NH₃.
- **Precursor ion**: The selected precursor m/z, charge state, and isolation window are reported in the figure caption.

For publication, the spectrum should be normalized so that the most intense fragment ion corresponds to 100% relative abundance. The m/z axis should zoom to the diagnostically informative region (typically 100 Da through just above the precursor m/z).

### Mirror Plots for Comparative MS/MS

When comparing MS/MS spectra — for example, confirming that a synthetic peptide fragment matches a reference standard or a database entry — mirror plots provide the clearest visualization. The experimental spectrum is plotted upward (positive intensity) and the reference spectrum downward (negative intensity). Matching peaks align vertically; unmatched peaks point in opposite directions.

The mirror plot is annotated with the match score (typically a dot product or spectral correlation coefficient between 0 and 1, where >0.7 indicates a good match) and the key matched fragments labeled. This format is standard in proteomics data repositories and is increasingly expected in peptide characterization reports.

### Extracted Ion Chromatograms (XICs)

An extracted ion chromatogram (XIC; also called extracted ion current or mass chromatogram) plots the intensity of ions within a narrow m/z window (±0.02 Da for high-resolution instruments) over chromatographic time. XICs are used to track specific peptide species through a chromatographic run, and they are particularly valuable for:

- **Confirming peak identity**: Does a UV peak at tR = 18.4 min correspond to the expected peptide mass? The XIC at that mass should show a peak at the same retention time.
- **Detecting co-eluting species**: If the UV trace shows a single peak but two different XICs (e.g., [M+3H]³⁺ for the target peptide and [M+3H]³⁺ for an oxidized variant) both peak at the same retention time, co-elution is confirmed.
- **Quantifying impurities by MS response**: Where UV absorbance may differ, MS ion current provides an orthogonal abundance estimate.

A well-designed XIC figure overlays the TIC and the XICs of interest on a single panel, with the TIC shown as a gray background trace and each XIC displayed in a distinct color. The m/z extraction window is reported in the legend.

## Circular Dichroism Spectroscopy Visualization

### Secondary Structure Signatures in CD Spectra

Circular dichroism (CD) spectroscopy measures the differential absorption of left- and right-circularly polarized light as a function of wavelength. For peptides and proteins, the far-UV CD spectrum (190–260 nm) is dominated by the peptide bond chromophore and reports on secondary structure content.

The characteristic CD signatures are:

- **α-Helix**: Double minima at 222 nm (n → π* transition) and 208 nm (π → π* transition), with a positive maximum near 192 nm.
- **β-Sheet**: Single minimum near 215–218 nm and a positive maximum near 195 nm.
- **Random coil / disordered**: Minimum near 195–200 nm with low ellipticity above 210 nm.
- **Polyproline II (PPII) helix**: A minimum near 200 nm and a weak positive band near 220 nm. The PPII conformation is characteristic of collagen triple helices and many short proline-rich peptides.

CD data are conventionally reported as mean residue ellipticity [θ] (deg·cm²·dmol⁻¹) on the y-axis versus wavelength (nm) on the x-axis. The conversion from raw ellipticity (θ in millidegrees) to mean residue ellipticity is:

$$ [\theta] = \frac{\theta \times M}{10 \times C \times l \times n} $$

where M is the molecular weight (g/mol), C is the concentration (mg/mL), l is the path length (cm), and n is the number of residues. Proper normalization to mean residue ellipticity is essential because it allows direct comparison of CD spectra between peptides of different lengths and concentrations.

### Thermal Denaturation CD Plots

Temperature-dependent CD spectroscopy monitors the loss of secondary structure as the peptide is heated, providing a measure of conformational stability. The most common visualization is a plot of ellipticity at a single diagnostic wavelength (typically 222 nm for α-helical content) versus temperature.

The resulting sigmoidal curve reveals:

- The **melting temperature (Tm)**: the midpoint of the unfolding transition, where folded and unfolded populations are equal. Reported as the temperature at which θ(T) = (θ_folded + θ_unfolded)/2.
- **Cooperative vs. non-cooperative unfolding**: A sharp, sigmoidal transition (spanning <20°C) indicates cooperative two-state unfolding typical of well-folded structures. A broad, shallow transition suggests non-cooperative melting or a molten-globule intermediate.
- **Reversibility**: The heating and cooling curves should be overlaid. Superposition of the two curves demonstrates reversible folding; hysteresis indicates irreversible aggregation.

A publication-quality thermal melt figure includes the raw CD signal versus temperature (symbols showing every data point collected), a fit to a two-state unfolding model (solid line), and a vertical dashed line at the Tm. The fit parameters (Tm, ΔH, ΔS) should be reported in the legend.

### Buffer Subtraction and Baseline Correction

CD spectra are sensitive to buffer composition because many buffer components (chloride, phosphate, Tris, HEPES) absorb in the far-UV. Every CD figure must report the buffer composition and explicitly state that a buffer blank spectrum has been subtracted. The high-tension (HT) voltage — a measure of the photomultiplier tube gain — should be monitored and reported: HT above 700 V generally indicates excessive absorbance and unreliable data.

A rigorous CD figure preparation protocol includes:

1. Collect the sample spectrum (3–5 accumulations, 50 nm/min scan speed, 1 nm bandwidth).
2. Collect the buffer blank spectrum under identical conditions.
3. Subtract the blank from the sample.
4. Apply mild smoothing (Savitzky-Golay filter, window 5–9 points) if the signal-to-noise ratio is poor, but always report the smoothing parameters.
5. Convert to mean residue ellipticity.
6. Plot with error bars showing the standard deviation across accumulations.

## NMR Contour Plots and Spectral Visualization

### 2D NMR Spectrum Visualization

Two-dimensional NMR spectra (COSY, TOCSY, NOESY, HSQC) are visualized as contour plots: the two frequency axes (F1 and F2, both in ppm) define the plane, and contour lines connect points of equal intensity. The diagonal and cross-peaks encode through-bond and through-space correlations that enable resonance assignment and structure determination.

Peptide NMR visualization follows well-established conventions:

- **Projections**: One-dimensional projections along each axis are often displayed adjacent to the contour plot, providing a reference for the chemical shift dispersion.
- **Chemical shift referencing**: Spectra should be referenced to an internal standard (DSS at 0 ppm, or TSP) or to the water resonance at the experimental temperature. The referencing method should be stated.
- **Peak annotation**: For assigned spectra, cross-peaks are labeled with the residue and atom (e.g., "Ala3 Hα-HN" for the intraresidue COSY cross-peak of Ala3, or "I27 HN – L26 Hα" for a sequential NOE cross-peak).
- **Positive and negative contours**: In phase-sensitive spectra, positive and negative peaks are drawn in different colors (typically black/blue for positive, red for negative). This is critical for NOESY spectra acquired at short mixing times, where diagonal peaks are positive and cross-peaks are negative at small-molecule tumbling rates.
- **Spectral width and carrier position**: The spectral width in each dimension and the transmitter (carrier) frequency offset should be reported in the caption.

### HSQC as a Structural Fingerprint

The ¹H-¹⁵N HSQC (heteronuclear single quantum coherence) spectrum is the most information-dense single spectrum for a ¹⁵N-labeled peptide. Each residue (except proline, which lacks an amide proton) produces one cross-peak at its unique (¹H, ¹⁵N) chemical shift. The HSQC therefore serves as a "fingerprint" of the folded state:

- **A well-folded peptide** exhibits sharp, well-dispersed cross-peaks spread over a wide chemical shift range (¹H: 6.5–10 ppm; ¹⁵N: 105–130 ppm).
- **An unfolded peptide** shows collapsed chemical shift dispersion, with most amide protons clustered between 7.8 and 8.5 ppm.
- **Titration or ligand-binding studies** are visualized as HSQC overlay figures in which the unbound spectrum (black) is overlaid with successive addition spectra (colored), and peak movements (chemical shift perturbations, CSPs) are tracked.

CSP analysis is quantified as:

$$ \Delta\delta = \sqrt{(\Delta\delta_{\text{H}})^2 + (0.154 \times \Delta\delta_{\text{N}})^2} $$

where the scaling factor 0.154 accounts for the larger chemical shift range of ¹⁵N relative to ¹H. Residues with Δδ above a significance threshold (typically the average plus one standard deviation) are mapped onto the peptide structure as a CSP heatmap.

### Stacked 1D Spectra and Titration Plots

For peptides accessible by 1D ¹H NMR (typically those <30 residues without isotope labeling), titration experiments are visualized as stacked spectra. The baseline spectrum (free peptide) is shown at the bottom, and successive spectra with increasing concentration of a binding partner are stacked upward with a vertical offset.

Key design considerations for stacked NMR plots:

- The vertical offset between spectra should be uniform and sufficient to prevent overlap (typically 1.5–2× the tallest peak height).
- The order of spectra should follow increasing titrant concentration, with concentrations labeled on the right side or in the legend.
- Spectra are best plotted in a muted color (gray or navy) to avoid visual fatigue, with one or two "representative" spectra highlighted in bold color.
- The region of interest (amide region for peptide backbone, methyl region for side-chain contacts) should be expanded in an inset, because stacked full spectra can be difficult to read in detail.

## Data Overlay and Annotation Strategies

### The Principle of Orthogonal Confirmation

The most persuasive analytical figures for peptide characterization overlay data from orthogonal techniques. The principle is simple: if two independent analytical methods provide consistent evidence, confidence in the conclusion increases multiplicatively. The practical implementation is overlay annotation.

Common overlay strategies include:

| Overlay Type | Data Sources | What It Communicates |
|-------------|-------------|---------------------|
| HPLC-UV + TIC | UV chromatogram at 214 nm + total ion chromatogram from MS | Confirms that all UV peaks have been mass-identified |
| HPLC + MS peak labels | Chromatogram with m/z values annotated on each peak | Provides immediate mass identity alongside chromatographic purity |
| CD + secondary structure deconvolution | Experimental CD spectrum + fitted curves for each structural component | Shows how well the experimental data are explained by the secondary structure model |
| UV spectrum + MS | HPLC peak UV spectrum + MS/MS spectrum from the same retention time | Provides both chromatographic and mass-spectrometric evidence of identity |
| NMR HSQC overlay | Free + bound HSQC spectra | Visualizes chemical shift perturbations upon ligand binding |

### Annotation Best Practices

Annotations make the difference between a raw instrument trace and a scientific figure. The following practices apply across all analytical visualization types:

1. **Use vector-based annotation whenever possible**. Export figures as SVG or EPS and add labels in a vector graphics editor (Inkscape, Adobe Illustrator) rather than using the instrument software's built-in text tool, which often produces low-resolution rasterized labels.

2. **Consistent font and sizing**. All text in analytical figures should use a sans-serif font (Arial, Helvetica, or the open-source equivalent) at 7–9 pt for labels and 8–10 pt for axis titles. Mixed fonts in a single figure are a hallmark of unpolished instrument output.

3. **Align annotations to peaks, not arbitrary positions**. Retention time labels should be placed adjacent to the peak apex. Mass labels should be placed above the corresponding peak. The reader should not have to trace a connecting line to identify which annotation belongs to which feature.

4. **Report integration boundaries explicitly**. For chromatograms, the integration marks (vertical tick marks or dashed lines) should be included in the figure. If the integration method has been modified from the default, this must be noted — it often affects the reported purity.

5. **Include scale bars for critical measurements**. For MS/MS spectra showing diagnostic fragment ions, a scale bar showing 10% relative abundance helps the reader assess the significance of small fragments. For NMR contour plots, a one-dimensional projection scale bar aids interpretation.

6. **Figure legends must be self-contained**. A reader should be able to understand the figure without referring to the main text. The legend should state: the peptide sequence (or sample identifier), the instrument and conditions, the key observations, and any data processing applied.

## Statistical Graphics for Analytical Chemistry

### Box Plots and Violin Plots for Batch Analysis

Batch-to-batch consistency is a critical quality metric for peptide manufacturing. Box plots provide a compact visualization of purity distribution across batches:

- **Central line**: median purity.
- **Box**: interquartile range (IQR, 25th–75th percentile).
- **Whiskers**: extend to the most extreme data point within 1.5 × IQR of the box.
- **Outlier points**: individual data points beyond the whiskers, labeled with the batch number.

For small datasets (<30 batches), individual data points should be overlaid as jittered scatter points on the box plot, providing a complete view of the distribution rather than hiding it behind summary statistics.

Violin plots extend box plots by showing the probability density of the data, revealing whether the purity distribution is unimodal (expected for a well-controlled process) or multimodal (indicating distinct sub-populations, perhaps from different synthetic routes or purification protocols).

### Principal Component Analysis (PCA) Scores Plots

PCA scores plots are the standard visualization for multivariate analytical data — for example, the peak areas of multiple impurities across many batches, or the intensities of MS fragments across samples. The first two principal components typically capture the majority of variance in the data, and plotting PC1 vs. PC2 with samples colored by an explanatory variable (batch, synthesis method, storage condition, etc.) reveals clustering patterns that indicate systematic differences.

A publication-quality PCA scores plot includes:

- **Explained variance percentages** on the axis labels: "PC1 (47.2%)" and "PC2 (23.8%)."
- **Loading vectors**: arrows from the origin showing the contribution of original variables to the principal components. Long arrows indicate variables that contribute strongly; their direction points toward sample clusters characterized by high values of that variable.
- **Confidence ellipses**: 95% confidence ellipses (Hotelling's T²) for each group, assuming multivariate normality.
- **Group labels**: placed adjacent to cluster centroids, not overlapping any data point.

### Control Charts for Method Performance

Control charts (Shewhart charts) monitor analytical method performance over time by tracking key metrics — retention time, theoretical plate count, tailing factor, or system suitability check standard purity — against statistically defined control limits.

The control chart plots the metric on the y-axis against run number or date on the x-axis, with the following horizontal lines:

- **Center line**: the mean of the metric over an initial "in-control" period (typically 20–25 runs).
- **Upper and lower control limits (UCL, LCL)**: mean ± 3σ, where σ is the standard deviation of the in-control data. Assuming normally distributed data, 99.73% of points should fall within these limits.
- **Upper and lower warning limits (UWL, LWL)**: mean ± 2σ. Points outside these limits signal a developing trend that may require investigation.

A system suitability failure is visualized as a point outside the control limits — typically rendered as a red data point with the run number annotated. A systematic trend (e.g., seven consecutive points on the same side of the center line) indicates instrument drift and should be investigated even if no single point exceeds the control limits.

### The Stability-Indicating Impurity Profile

For peptide stability studies (ICH Q1A-compliant forced degradation, accelerated stability, and long-term stability), the most informative visualization is the stability-indicating impurity profile: a stacked bar chart showing the area percent of the main peak and each identified impurity at each time point (T0, T1 month, T3 months, T6 months, etc.).

Each bar represents a time point. Within each bar, the main peak area percent occupies the bottom segment (in a neutral color such as gray), and each impurity occupies a stacked segment above it, colored by identity (e.g., oxidation products in blue, deamidation products in orange, hydrolysis products in red, unknown impurities in black). The total height of each bar is 100%.

This visualization immediately communicates:

- The rate of main peak loss (the shrinking gray segment).
- The relative rates of formation of different degradation products.
- The emergence of new impurities not present at T0.
- Mass balance: if the total area decreases, non-UV-active degradation products or insoluble precipitates may be forming.

The same format can display purity data across synthesis batches, comparing the impurity profile of a new synthetic route against an established one.

## Research Evidence

The visualization strategies described in this article are grounded in analytical chemistry methodology, regulatory guidance, and the statistical principles of data visualization.

| Study | Key Finding | Relevance to Analytical Data Visualization |
|-------|------------|---------------------------------------------|
| Snyder, Kirkland & Dolan (2010) | Introduction to Modern Liquid Chromatography | The definitive text on HPLC method development, including chromatogram interpretation and integration parameter selection |
| ICH Q2(R2) (2023) | Validation of Analytical Procedures | Regulatory framework defining LOD, LOQ, linearity, and precision reporting — the statistical basis for all quantitative analytical figures |
| Kelly, Jess & Price (2005) | How to study proteins by circular dichroism | Standard protocols for CD data collection, processing, and secondary structure content estimation — the foundation of CD figure design |
| Wishart (2011) | Interpreting protein chemical shift data | Comprehensive guide to protein NMR chemical shift referencing, referencing conventions, and CSP analysis for binding studies |
| Chambers et al. (2012) | A cross-platform toolkit for mass spectrometry and proteomics | Data processing pipeline for MS data, including charge state deconvolution, peak picking, and format conversion for visualization |
| Tabb et al. (2007) | MyriMatch: highly accurate tandem mass spectral peptide identification | Statistical scoring of peptide-spectrum matches; established the mirror plot convention for comparative MS/MS visualization |
| Krissinel & Henrick (2004) | Secondary-structure matching (SSM), a new tool for fast protein structure alignment | Standardized secondary structure classification that underpins CD spectral deconvolution algorithms |
| Wishart et al. (1995) | ¹H, ¹³C and ¹⁵N chemical shift referencing in biomolecular NMR | Established the IUPAC-recommended chemical shift referencing standards (DSS, TSP) used in all NMR figure axes |
| MassLynx & UNIFI (Waters Corp.) | Software for LC-MS data acquisition and processing | Industry-standard platform for LC-MS chromatogram and spectrum visualization; the source of most instrument-generated analytical figures |
| Tufte (2001) | The Visual Display of Quantitative Information | The foundational text on data visualization design principles — data-ink ratio, chartjunk elimination, and small multiples — directly applicable to analytical figure design |
| Dolan (2002–2015) | LC Troubleshooting (monthly column, LCGC) | Practical guidance on chromatogram artifact identification — ghost peaks, baseline disturbances, and integration artifacts |
| Yu et al. (2019) | Ggtree: an R package for visualization and annotation of phylogenetic trees | Demonstrated the power of layered annotation in R-based scientific visualization, applicable to CD and chromatogram overlay design |
| Greenfield (2006) | Using circular dichroism spectra to estimate protein secondary structure | Reference dataset and deconvolution algorithms (CDSSTR, CONTIN, SELCON3) that transform raw CD data into secondary structure content figures |
| Box, Hunter & Hunter (2005) | Statistics for Experimenters | Classical reference on statistical graphics for quality control; established the control chart limits and trend detection rules used in analytical method monitoring |
| Van Belle (2011) | Statistical Rules of Thumb | Practical guidelines for statistical graphics including error bar representation, axis scaling, and the relationship between sample size and visualization complexity — directly informs analytical figure design |

## Frequently Asked Questions

<div class="faq-container">

<div class="faq-item" markdown="1">
### What wavelength should I use when displaying my HPLC chromatogram?

The choice of detection wavelength depends on what you want to communicate. For purity assessment, 214–220 nm is standard because it captures the peptide bond absorption (n → π* transition) and detects most peptide-related impurities. For peptides containing aromatic residues (Phe, Tyr, Trp), 254 nm or 280 nm provides complementary information — impurities that are visible at 214 nm but absent at 280 nm likely lack aromatic residues and may be deletion peptides. The best practice is to display at least two wavelengths: 214 nm for comprehensive impurity detection and 280 nm for aromatic residue confirmation. Always report the wavelength(s) in the axis label and figure legend because purity numbers from different wavelengths are not interchangeable. A peptide that is 97.2% pure at 214 nm might be 98.5% pure at 280 nm, or vice versa, depending on the UV absorption profiles of the impurities.
</div>

<div class="faq-item" markdown="1">
### How do I know if my integration parameters are correct?

Correct integration is visible in the chromatogram itself. The integration marks (vertical tick marks or dashed lines) should start and end at the baseline — not inside the peak, not extending into the next peak, and not truncating peak tails prematurely. A peak that has been "skimmed" (tangent-skimmed off a larger peak) should show the baseline drawn as a tangent line touching the peak tail at a defined point, not arbitrarily. The noise threshold should be set so that baseline noise is not integrated as peaks, but genuine impurity peaks above the limit of quantitation (LOQ) are captured. If changing the slope sensitivity (threshold) by ±20% changes the reported purity by more than 0.5%, the integration parameters are not robust and should be re-optimized. The integration parameters used — slope sensitivity, peak width, baseline mode, and any manual reintegrations — must be documented and stored with the data. For peptides purchased with a COA, the integration marks on the printed chromatogram are your visual check: if they cut into the peak or merge impurities into the main peak, question the purity number.
</div>

<div class="faq-item" markdown="1">
### What is the difference between the total ion chromatogram (TIC) and the UV chromatogram in LC-MS?

The total ion chromatogram (TIC) records the sum of all ion currents detected by the mass spectrometer as a function of time. The UV chromatogram records absorbance at a specific wavelength. They measure fundamentally different properties, and they should not be expected to match perfectly. Compounds that ionize efficiently in electrospray will show a larger MS peak relative to their UV peak; compounds that absorb strongly in the UV but ionize poorly will show the opposite. The TIC is also noisier than a UV trace because it sums noise across the entire m/z range. The true power of LC-MS is not in the TIC but in the extracted ion chromatograms (XICs), which trace specific m/z values through the chromatographic run — these should show peaks at retention times matching the UV trace. A modern peptide characterization figure often shows the UV trace with XICs for the target peptide and key impurities overlaid, rather than relying on the TIC alone.
</div>

<div class="faq-item" markdown="1">
### How do I convert raw CD data (millidegrees) to mean residue ellipticity?

The conversion uses the formula [θ] = (θ_raw × M) / (10 × C × l × n), where θ_raw is the measured ellipticity in millidegrees, M is the molecular weight in g/mol (Da = g/mol for practical purposes), C is the peptide concentration in mg/mL, l is the cuvette path length in cm (typically 0.1 cm for far-UV CD), and n is the number of residues. For example, a 20-residue peptide with M = 2500 Da at 0.2 mg/mL in a 0.1 cm cell: if θ_raw at 222 nm = −15 millidegrees, then [θ]₂₂₂ = (−15 × 2500) / (10 × 0.2 × 0.1 × 20) = −9375 deg·cm²·dmol⁻¹. This conversion is essential because it normalizes for concentration, path length, and peptide length, allowing direct comparison between different peptides and with literature reference spectra. A common mistake is to use the peptide concentration in mg/mL when the formula actually requires it in mg/mL already — double-check your units carefully.
</div>

<div class="faq-item" markdown="1">
### Why does my NMR HSQC spectrum have positive and negative peaks?

In a phase-sensitive ¹H-¹⁵N HSQC experiment, positive and negative peaks convey different information about the NH₂ groups. Backbone amide (NH) cross-peaks appear with one phase (typically positive, black or blue contours), while side-chain NH₂ groups of asparagine and glutamine residues appear with the opposite phase (negative, red contours) because of the different coherence transfer pathway for NH₂ groups. This phase discrimination is actually a useful feature — it allows you to identify Asn and Gln side-chain resonances at a glance. If you see a negative (red) cross-peak in an HSQC of a peptide that contains no Asn or Gln residues, it may indicate an arginine side-chain NH (the guanidinium NH₂ group) or, if it appears as a pair of cross-peaks at the same ¹⁵N chemical shift, an artifact. The phase of the spectrum must be stated in the figure caption, typically as "Positive contours (blue) represent backbone amides; negative contours (red) represent side-chain NH₂ groups."
</div>

<div class="faq-item" markdown="1">
### What is chemical shift perturbation (CSP) analysis and how is it visualized?

Chemical shift perturbation analysis monitors the movement of NMR cross-peaks when a peptide binds a ligand, metal ion, or another macromolecule. As the binding partner is titrated in, residues at the binding interface experience changes in their local magnetic environment, causing their HSQC cross-peaks to shift. The combined chemical shift change, Δδ = √[(Δδ_H)² + (0.154 × Δδ_N)²], is plotted as a bar chart along the peptide sequence (residue number on x-axis, Δδ on y-axis). Residues with Δδ above the average plus one standard deviation are considered significantly perturbed and are mapped onto the 3D peptide structure as a heatmap (red for high perturbation, blue for low perturbation). This visualization — a CSP bar chart paired with a structure heatmap — is the standard method for mapping binding interfaces and is expected in any peptide NMR binding study.
</div>

<div class="faq-item" markdown="1">
### How should I visualize impurity profiles across multiple batches?

The most effective approach uses a grouped or stacked bar chart format. For grouped bars, each batch is a group on the x-axis, and within each group, the main peak purity, total impurities, and the largest single impurity are shown as adjacent bars. For stacked bars, each batch is a single bar with the main peak as the bottom segment (gray) and individual impurities stacked above, each in its own color. The stacked format is preferred for stability studies because it shows the evolution of the impurity profile over time. Add a horizontal dashed line at the specification limit (e.g., 95% purity) so that failing batches are immediately visible. Color consistency is critical: if "oxidation product" is blue in one figure, it must be blue in all figures throughout the report or publication. Include a table of the underlying data alongside the figure so that readers can extract exact purity values.
</div>

<div class="faq-item" markdown="1">
### What software can I use to create publication-quality analytical figures?

For chromatograms and mass spectra, the instrument vendor software (Waters MassLynx/UNIFI, Thermo Xcalibur/FreeStyle, Agilent MassHunter, Bruker Compass) can export vector-format files (PDF, SVG, EPS). These should be opened in a vector graphics editor (Inkscape is free and open-source; Adobe Illustrator is the commercial standard) for final annotation, label alignment, and formatting. For CD spectra, export the data as text (two-column ASCII: wavelength, ellipticity) and plot using matplotlib (Python), ggplot2 (R), GraphPad Prism, or Origin. For NMR, export spectra from TopSpin, MNova, or Sparky as publication-resolution images and overlay annotations. For statistical graphics, R with ggplot2 provides the most flexible and reproducible pipeline. The key principle across all tools is: export raw data, plot in a general-purpose graphing environment with full control over axes, fonts, and annotations, and finish in a vector graphics editor. Relying on instrument software for final figures almost always produces substandard results because these tools prioritize data acquisition over figure aesthetics.
</div>

<div class="faq-item" markdown="1">
### How do I combine multiple analytical techniques into a single figure?

Multi-panel figures that combine HPLC, MS, and CD data follow the journal's formatting guidelines, but a general template works well: Panel A shows the HPLC-UV chromatogram with peak annotations; Panel B shows the full-scan mass spectrum with the charge state envelope labeled; Panel C shows the deconvoluted mass spectrum with mass accuracy; and Panel D shows the CD spectrum with secondary structure content estimates. Each panel is labeled with a bold capital letter (A, B, C, D) in the upper-left corner. Panels share a consistent font, color palette, and line weight. If the same peptide is analyzed across all panels, the peptide name or identifier appears only in the overall figure legend, not in every panel. Cross-referencing between panels — for example, drawing a bracket from a peak in Panel A to the corresponding mass in Panel B — enhances the narrative but should be used sparingly to avoid visual clutter. The combined figure should tell a single story: "This peptide is pure (HPLC), has the correct mass (MS), and is properly folded (CD)."
</div>

<div class="faq-item" markdown="1">
### What are the ICH guidelines for analytical figure documentation in regulatory submissions?

The ICH guidelines do not prescribe specific figure formats but establish the information that figures must communicate. ICH Q2(R2) (Validation of Analytical Procedures) requires reporting of specificity, linearity, range, accuracy, precision (repeatability and intermediate precision), detection limit (LOD), and quantitation limit (LOQ) for each analytical procedure. Figures supporting these validation parameters should include: calibration curves with individual data points, residuals plots (residuals vs. concentration, to assess linearity), and accuracy/recovery plots. ICH Q1A(R2) (Stability Testing) expects stability-indicating impurity profiles as described above, with clear labeling of time points, storage conditions, and specification limits. ICH Q3A(R2) (Impurities in New Drug Substances) requires reporting of all impurities above the reporting threshold (0.05–0.1% depending on daily dose), which means chromatograms must be annotated down to at least this level. All figures in regulatory submissions must be legible when printed in black and white — use distinct line styles (solid, dashed, dotted) in addition to color.
</div>

</div>

## References

1. Snyder, L. R., Kirkland, J. J., & Dolan, J. W. (2010). *Introduction to Modern Liquid Chromatography* (3rd ed.). Wiley. DOI: [10.1002/9780470508183](https://doi.org/10.1002/9780470508183)

2. ICH Harmonised Guideline. (2023). *Validation of Analytical Procedures Q2(R2)*. International Council for Harmonisation of Technical Requirements for Pharmaceuticals for Human Use. https://www.ich.org/page/quality-guidelines

3. Kelly, S. M., Jess, T. J., & Price, N. C. (2005). How to study proteins by circular dichroism. *Biochimica et Biophysica Acta (BBA) - Proteins and Proteomics*, 1751(2), 119–139. DOI: [10.1016/j.bbapap.2005.06.005](https://doi.org/10.1016/j.bbapap.2005.06.005)

4. Wishart, D. S. (2011). Interpreting protein chemical shift data. *Progress in Nuclear Magnetic Resonance Spectroscopy*, 58(1-2), 62–87. DOI: [10.1016/j.pnmrs.2010.07.004](https://doi.org/10.1016/j.pnmrs.2010.07.004)

5. Chambers, M. C., Maclean, B., Burke, R., Amodei, D., Ruderman, D. L., Neumann, S., Gatto, L., Fischer, B., Pratt, B., Egertson, J., Hoff, K., Kessner, D., Tasman, N., Shulman, N., Frewen, B., Baker, T. A., Brusniak, M. Y., Paulse, C., Creasy, D., … Mallick, P. (2012). A cross-platform toolkit for mass spectrometry and proteomics. *Nature Biotechnology*, 30(10), 918–920. DOI: [10.1038/nbt.2377](https://doi.org/10.1038/nbt.2377)

6. Tabb, D. L., Fernando, C. G., & Chambers, M. C. (2007). MyriMatch: highly accurate tandem mass spectral peptide identification by multivariate hypergeometric analysis. *Journal of Proteome Research*, 6(2), 654–661. DOI: [10.1021/pr0604054](https://doi.org/10.1021/pr0604054)

7. Krissinel, E., & Henrick, K. (2004). Secondary-structure matching (SSM), a new tool for fast protein structure alignment in three dimensions. *Acta Crystallographica Section D*, 60(12), 2256–2268. DOI: [10.1107/S0907444904026460](https://doi.org/10.1107/S0907444904026460)

8. Wishart, D. S., Bigam, C. G., Yao, J., Abildgaard, F., Dyson, H. J., Oldfield, E., Markley, J. L., & Sykes, B. D. (1995). ¹H, ¹³C and ¹⁵N chemical shift referencing in biomolecular NMR. *Journal of Biomolecular NMR*, 6(2), 135–140. DOI: [10.1007/BF00211777](https://doi.org/10.1007/BF00211777)

9. Tufte, E. R. (2001). *The Visual Display of Quantitative Information* (2nd ed.). Graphics Press. ISBN: 978-1930824133.

10. Dolan, J. W. (2002–2015). LC Troubleshooting (monthly column). *LCGC North America*. https://www.chromatographyonline.com/

11. Yu, G., Smith, D. K., Zhu, H., Guan, Y., & Lam, T. T.-Y. (2019). ggtree: an R package for visualization and annotation of phylogenetic trees with their covariates and other associated data. *Methods in Ecology and Evolution*, 8(1), 28–36. DOI: [10.1111/2041-210X.12628](https://doi.org/10.1111/2041-210X.12628)

12. Greenfield, N. J. (2006). Using circular dichroism spectra to estimate protein and peptide secondary structure. *Nature Protocols*, 1(6), 2876–2890. DOI: [10.1038/nprot.2006.202](https://doi.org/10.1038/nprot.2006.202)

13. Box, G. E. P., Hunter, J. S., & Hunter, W. G. (2005). *Statistics for Experimenters: Design, Innovation, and Discovery* (2nd ed.). Wiley. DOI: [10.1002/0470074336](https://doi.org/10.1002/0470074336)

14. Van Belle, G. (2011). *Statistical Rules of Thumb* (2nd ed.). Wiley. DOI: [10.1002/9780470377966](https://doi.org/10.1002/9780470377966)

15. Wishart, D. S., & Sykes, B. D. (1994). Chemical shifts as a tool for structure determination. *Methods in Enzymology*, 239, 363–392. DOI: [10.1016/S0076-6879(94)39014-2](https://doi.org/10.1016/S0076-6879(94)39014-2)

---

*For research peptides supported by comprehensive analytical documentation — including HPLC chromatograms, LC-MS spectra, and certificates of analysis — visit [RPL Peptides](https://rplpeptides.com). Browse and download analytical data packages at the [RPL Peptides Data Portal](https://data.rplpeptides.com).*

Return to [Interactive Figures](index.md).
