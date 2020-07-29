

from Bio.Seq import Seq

my_seq = Seq("ATGATAGGAGTATAA")
print(my_seq)

print(my_seq.reverse_complement())

print(my_seq.translate())
print(my_seq.transcribe())
