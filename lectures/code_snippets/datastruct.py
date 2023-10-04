

def count_bases(dna):
    counts = {}
    for base in dna:
        if base not in counts:
            counts[base] = 0
        counts[base] = counts[base] + 1
    return counts

names = ['seqA', 'seqB', 'seqC']
sequences = ['AGTCGA', 'CCTCGT', 'ATTCGT']

all_counts = {}
for i in range(len(names)):
    name = names[i]
    seq = sequences[i]
    base_counts = count_bases(seq)
    all_counts[name] = base_counts

print(all_counts)
