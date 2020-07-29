

from Bio.Blast import NCBIWWW, NCBIXML
from Bio import SeqIO

# Parse the fasta file with the query sequence:
fasta_parser = SeqIO.parse("orchid.fasta", "fasta")
query = next(fasta_parser)

# Blast using the query sequence:
blast_handle = NCBIWWW.qblast("blastn", "nt", query.seq)
# Read the blast results
blast_output = blast_handle.read()

# Write results to a file:
result_file = open("blast_output.xml", "w")
result_file.write(blast_output)
result_file.close()

# Read in 
result_file = open("blast_output.xml", 'r')
blast_records = NCBIXML.parse(result_file)

# Print (or do something else) with the blast results:
for blast_record in blast_records:
	for alignment in blast_record.alignments:
	    for hsp in alignment.hsps:
	        if hsp.expect < 0.0001:
	            print('****Alignment****')
	            print('sequence:', alignment.title)
	            print('length:', alignment.length)
	            print('e value:', hsp.expect)
	            print(hsp.query[0:50] + '...')
	            print(hsp.match[0:50] + '...')
	            print(hsp.sbjct[0:50] + '...')


