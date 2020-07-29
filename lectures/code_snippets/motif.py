
IUPAC = {'T': 'T',
         'A': 'A',
         'G': 'G',
         'C': 'C',
         'M': 'AC',
         'R': 'AG',
         'W': 'AT',
         'S': 'CG',
         'Y': 'CT',
         'K': 'GT',
         'V': 'ACG',
         'H': 'ACT',
         'D': 'AGT',
         'B': 'CGT',
         'X': 'GATC',
         'N': 'GATC' }


def test_motif(s, m):
    for i in range(len(m)):
        if s[i] not in IUPAC[m[i]]:
            return False
    return True


motif = 'SNTM'
seq =   'GATC'

result = test_motif(seq, motif)
print(result)





# def find_motifs(seq, motif):
#     matches = []
#     k = len(motif)
#     for i in range(len(seq)-k+1):
#         kmer = seq[i:i+k]
#         if test_motif(kmer, motif):
#             matches.append(i)
#     return matches



# motif = 'SNTM'
# seq =   'AAAAAAGATCAAAAAAGATCAAA'

# result = find_motifs(seq, motif)
# print(result)