

MAT = {'A': {'A': 2, 'T': 0, 'G': 0, 'C': 0},
       'T': {'A': 0, 'T': 2, 'G': 0, 'C': 0},
       'G': {'A': 0, 'T': 0, 'G': 2, 'C': 0},
       'C': {'A': 0, 'T': 0, 'G': 0, 'C': 2}}

G = -1


def score(a, b):
    if len(a) == 0 and len(b) == 0:
        return 0
    possible = []
    if len(a) > 0 and len(b) > 0:
        s = score(a[:-1], b[:-1]) + MAT[a[-1]][b[-1]]
        possible.append(s)
    if len(a) > 0 and len(b) >= 0:
        s = score(a[:-1], b) + G
        possible.append(s)
    if len(a) >= 0 and len(b) > 0:
        s = score(a, b[:-1]) + G
        possible.append(s)
    return max(possible)


print('4 bases', score('ATCA', 'GATA'))
print('5 bases', score('ATCAT', 'GATAA'))
print('6 bases', score('ATCATT', 'GATAAT'))
print('7 bases', score('ATCATTA', 'GATAATC'))
print('8 bases', score('ATCATTAA', 'GATAATCA'))
print('9 bases', score('ATCATTAAC', 'GATAATCAC'))
print('10 bases', score('ATCATTAACT', 'GATAATCACT'))
