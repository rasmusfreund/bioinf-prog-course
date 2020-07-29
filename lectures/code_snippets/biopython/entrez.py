import sys
from Bio import Entrez, SeqIO

Entrez.email = 'kaspermunch@birc.au.dk'

entrez_query = 'FOXP2[Gene] AND Homo[Organism]'

handle = Entrez.esearch(db="nucleotide", term=entrez_query, retmax=3, idtype="acc")
results = Entrez.read(handle)
handle.close()

handle = Entrez.efetch(db="nucleotide", id=results["IdList"], rettype='fasta', retmode="text")
records = SeqIO.parse(handle, "fasta")
for rec in records:
	#print(rec)
	SeqIO.write(rec, sys.stdout, format='fasta')


