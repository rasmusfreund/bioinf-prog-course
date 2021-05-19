# Motivation

Identifying candidate genes 
Millions of people live with Parkinsons disease (PD)
Progressive incurable disease affecting the nervous system
Shaking, and affects talking and walking, involuntary movement.
Complex and multifactorial
Heritable/genetic component, close relative of people with PD have higher risk. 15% of PD patients have a parent, sibling or child with PD.
but cannot be attributed to a single gene. Likely multiple genes interacting with environmental conditions, such as tobacco smoke.
PD symptoms result from death of a population of brain cells in the sunstiantia migraine part of the brain. This normally produces the neutrotransmitter dopamine. The cause of the cell death is not clear. Some patients have defects in particular genes, but in most cases no such simple explanation can be found. 

Look up PD and see what you can find

Genome wide association study (GWAS).
Only identifies genomic regions, not genes. 
Then candidate genes in those regions must be identified for new insights into causes of the disease and how it can be treated.
Associates genomic regions with disease phenotypes such as PD.
Do et al. Link to paper. And have them look at figure.

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