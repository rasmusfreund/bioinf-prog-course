
IUPAC = {'T': 'T',
         'A': 'A',
         'G': 'G',
         'C': 'C',
         'N': 'GATC' }


def test_motif(s, m):
    for i in range(len(m)):
        base = s[i]
        code = m[i]
        allowed_bases = IUPAC[code]
        if base not in allowed_bases:
            return False
    return True

def find_motifs(seq, motif):
    matches = []
    k = len(motif)
    for i in range(len(seq)-k+1):
        kmer = seq[i:i+k]
        if test_motif(kmer, motif):
            matches.append(i)
    return matches

find_motifs('AGTCGAATATAATACCTATAATCCC', 'TAATA')















    
# def find_motifs(seq, motif):
#     matches = []
#     k = len(motif)
#     for i in range(len(seq)-k+1):
#         kmer = seq[i:i+k]




# def test_motif(s, m):
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
#         if test_motif(kmer, motif):
#             matches.append(i)
#     return matches