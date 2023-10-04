# Genome-wide association studies ★

## Genetic disease association {-}

## Testing association {-}

## Genome-wide association {-}

## Do it yourself: Exploring an association with Parkinsons disease {-}

The purpose of this exercise is to expose you to the different kinds of information that are stored in databases relevant to bioinformatics. It takes experience and skill to navigate the user interface of these databases. Here you will see a few of the important ones, but there are many more. I have put a list at the end of this exercise with some additional relevant ones. Browse them at your harts content.

The [MacGuffin](https://en.wikipedia.org/wiki/MacGuffin) of this exercise is Parkinsons disease (PD). Millions of people live with PD, which is a progressive incurable disease affecting the nervous system resulting in shaking, involuntary movement and trouble talking and walking. PD is a complex and multifactorial disease with a heritable component: close relative of people with PD have higher risk. 15% of PD patients have a parent, sibling or child with PD. However, unlike other genetic diseases like cystic fibrosis, where a single gene is responsible, the risk of developing PD is determined by small contributions of many different genes. These genes interact with environmental conditions, such as tobacco smoke. PD symptoms are induced by death certain brain cells in the sunstiantia migraine part of the brain that normally produces the neurotransmitter dopamine.

In the study published in by Do at al. 2011, the authors searched for genes contributing to the risk of developing PD. They genotyped 3,426 PD patients (cases) and 29,624 healthy controls for 522,782 single nucleotide polymorphisms SNPs. A SNP is a position in the genome where the nucleotide differ between individuals in a population because some carry a recent mutation (G) and others carry the ancestral variant (A). Simply put, they considered each of the 522,782 SNPs to see if the occurrence of one of the alleles was significantly more often found among the individuals with PD than among healthy controls. Knowing only the number of cases and controls and the total numbers of A and G alleles, the expected number of A and G alleles found among cases and controls can be computed (E.g. the expected number of cases with the A allele is $(3426 * 23615) / 33050 \approx 2448$):

|---:|---:|---:|---:|
|   |  **A**   | **G** | Totals | 
| *Cases* | **2448**   | **978** | 3426 |
| *Controls* | **21167** | **8456** | 29624 |
| Totals | 23615 | 9434 | 33050 | 

This corresponds to an expected frequency of Allele A of 40% in both cases and controls. In the study the they observed the following numbers in each group;

|---:|---:|---:|---:|
|   | *Allele 1*   | *Allele 2* | Totals | 
| *Cases* | **2320**   | **1106** | 3426 |
| *Controls* | **21295** | **8328** | 29624 |
| Totals | 23615 | 9434 | 33050 | 
  
Corresponding to a 48% frequency of allele A among cases and a  39% frequency among controls. To test the statistical significance of this deviation from the expectation, we can perform a [Chi-square test](https://en.wikipedia.org/wiki/Chi-squared_test)to compute the p-value for the above case. The test statistic is very simple:

$$ \sum \frac{(observed - expected)^2}{expected} $$

Under the null-hypothesis, the test statistic follows a chi-square distribution with 1 degree of freedom. You can even do this in Python using the `chi2_contingency` from the `script.stats` library. Try it out and see what the p-value is in this case:

```python
from scipy.stats import chi2_contingency
observed = [[2320, 1106],
			[21295, 8328]]
stat, p_value, deg_free, expected = chi2_contingency(observed, correction=False)
print(p_value)
```

The p-value is probably something like 3e-07, which you may think is really small. Normally we use 0.05 as our significance cutoff - the probability of wrongly rejecting our null hypothesis of no association. Since there is a 0.05 probably in every test, we need to divide our significance cutoff by the number of tests to get the significance cutoff needed to only wrongly reject the null-hypothesis with 0.05 probability after doing all 522,782 tests. This cutoff is $0.05 / 522782 = 9.56e-08$. This adjustment of the significance cutoff is called [Bonferroni correction](https://en.wikipedia.org/wiki/Bonferroni_correction) overcorrects a bit, but the correction shows that even p-values as low as the one you computed above is only just significant in a GWAS. 

That is pretty much what GWAS is. There are some additional nuts and bolts required to take biases into account. Accounting for cases and controls not being sampled in the same way. You can probably imagine why the SNPs determining eye color would show up as associated with PD if all cases were sampled in Spain and all controls in Finland. However, we will gloss over those details here.

The SNPs associated with PD are not themselves involved in PD, but they mark a genomic neighborhood that is inherited along with the SNP. The closer a gene is to an associated SNP, the more likely it is that the gene is inherited along with the SNP. So it this genomic neighborhood that we should search for genes playing a role in the development of PD. Such candidate genes must be identified for new insights into causes of the disease and how it can be treated. The following part the of the exercise, but is meant to take you though some of the motions that a scientist would go through to search relevant genes in the region. 

- Each known SNP has a unique accession number that identifies it.
- The SNP identified by Do et al. has accession number *rs11868035*
- To explore the genomic neighbourhood of this SNP we use the [UCSC genome browser](https://genome-euro.ucsc.edu/cgi-bin/hgGateway?redirect=manual&source=genome.ucsc.edu). 
- The genome browser saves your preferences across sessions so if you have tried this service before before you can reset the browser to the default settings to align the views with this exercise. Click the Genome Browser->Reset All User Settings option in the top menu bar. However, be aware that this action will remove all custom tracks and will clear all track filter and configuration settings that may have modified.
- Under "Find Position" select the most recent human genome assembly (hg38) and paste in rs11868035 under "Position/Search Term" and click GO.
- On the resulting listing click the top link under "NHGRI-EBI Catalog of Published Genome-Wide Association Studies". 
- Familiarise yourself with the browser view. 
- Notice the SNP shown in the middle of the "NHGRI-EBI Catalog of Published Genome-Wide Association Studies" track. 
- Notice the scale shown at the top of the view. What part of the genome is shown? The chromosome ideogram at the top also shows with a red marker what part of the chromosome is shown. Use the zoom buttons to zoom out so you can see a see roughly 1,000 kilobases (1,000,000 base pairs) of the genome.
- The view is divided into tracks. Mousing over the right margin of each track will highlight it in green, and right-clicking will show customisation settings for each track. By holding and dragging on the grey bars furthest to the right, you can even reorder tracks as you please. 
- Scrolling down below the view, you can see a large number of tracks you can enable to show in the view. 
- In the "Phenotype and Literature" section find the dropdown labelled OMIM Genes and chose the view mode "Pack". Similarly, in the "Expression" section find and enable the track called GNF Atlas 2. Finally, "Mapping and Sequencing", find the Publications track and choose the "Dense" view mode. Now click any of the "Refresh" buttons to update the view with the selected tracks.
- If you click the grey bar on the right of each track, you are redirected to a page explaining the track.

- 

> In part I of the exercise, the UCSC "Genes" track has been replaced by "GENCODE v29". If you do not see the "GENCODE v29" track or the "RefSeq Genes" and "Human mRNAs" tracks, scroll down to the drop-down menus under "Gene and Gene Predictions" and select "GENCODE v29" and "NCBI RefSeq". The "Human mRNAs" track can be found under "mRNA and EST". Unfortunately, the GAD view and the Publications track are no longer available.


**Have them read a GWAS review**

Part of the exercise could be to make chi-square tests for the subset of SNPs in the region to see if they get something similar to 

```python
import matplotlib.pyplot as plt

pvalues = [1,2,3]
coordinates = [1,2,1]
plt.scatter(pvalues, coordinates)
plt.title('Plot 1')
plt.show()

pvalues = [1,2,3]
coordinates = [1,2,3]
plt.scatter(pvalues, coordinates)
plt.title('Plot 2')
plt.show()
```