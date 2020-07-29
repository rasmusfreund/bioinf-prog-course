
def n50(lengths):
	sorted_lengths = sorted(lengths)
	total = sum(lengths)

	cum_tot = 0
	for l in sorted_lengths:
		cum_tot += l
		if cum_tot > total/2:
			return l



contigs = [1, 3,  8, 12, 20, 1, 5]

n50_stat = n50(contigs)
print(n50_stat)