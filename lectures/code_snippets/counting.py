
def count_bases(dna):
	counts = {}
	for base in dna:
		if base not in counts:
			counts[base] = 0
		counts[base] = counts[base] + 1
	return counts


def sequence_counts(names, sequences):
    result = {}
    for idx in range(len(names)):
    	seq_name = names[idx]
    	seq = sequences[idx]
    	result[seq_name] = count_bases(seq)

    return result


names = ['seqA', 'seqB', 'seqC', "mogens"]
sequences = ['AGTCGA', 'CCTCGT', 'ATTCGT', 'ARG']

stats = sequence_counts(names, sequences)
print(stats)

