
from Bio import SeqIO

# parsing a fasta file:
for seq_record in SeqIO.parse("orchid.fasta", "fasta"):
    print(seq_record.id)
    print(seq_record.seq)
    print(len(seq_record))
    print('-' * 30)

# parsing a genbank file and write new file as fasta:
for seq_record in SeqIO.parse("orchid.gbk", "genbank"):
    SeqIO.write(seq_record, 'tmp.fasta', 'fasta')
