
IUPAC = {'T': 'T',
         'A': 'A',
         'G': 'G',
         'C': 'C',
         'N': 'GATC' }


def test_motif(s, m):
    for i in range(len(s)):
        base = s[i]
        iupac_letter = m[i]
        allowed_bases = IUPAC[iupac_letter]
        if base not in allowed_bases:
            return False
    return True




print(test_motif('GATC', 'GNTC'))
























# def test_motif(s, m):
#     print(s, m)
#     for i in range(len(m)):
#         base = s[i]
#         code = m[i]
#         allowed_bases = IUPAC[code]
#         if base not in allowed_bases:
#             return False
#     return True



# def find_motifs(seq, motif):
#     matches = []
#     k = len(motif)
#     for i in range(len(seq)-k+1):
#         kmer = seq[i:i+k]
# #        print(kmer, test_motif(kmer, motif))
#         if test_motif(kmer, motif):
#             matches.append(i)
#     return matches

# motif = 'GNTC'
# seq = 'AAAAGCTCAAAAAAGTTCA'

# print(test_motif('GGTC', 'GNTC'))

# print(find_motifs(seq, motif))