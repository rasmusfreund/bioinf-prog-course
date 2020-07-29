
def count_kmers(seq, k):
	counts = {}
	for i in range( len(seq)-k+1):
	    mer = seq[i:i+k]
	    if mer not in counts:
	    	counts[mer] = 0
	    counts[mer] = counts[mer] + 1
	return counts

def nr_different_kmers(seq, k):
	counts = count_kmers(seq, k)
	nr = len(counts)
	return nr

def most_common_kmer(seq, k):
	result = []
	counts = count_kmers(seq, k)
	max_count = max(counts.values())
	for mer in counts:
		if counts[mer] == max_count:
			result.append(mer)
	return result

def shared_kmers(seq1, seq2, k):
	cnt1 = count_kmers(seq1, k)
	cnt2 = count_kmers(seq2, k)
	shared = []
	for mer in cnt1:
		if mer in cnt2:
			shared.append(mer)
	return shared




def sequence_similarity(seq1, seq2):
	same = 0
	total = len(seq1)
	for idx in range(len(seq1)):
		if seq1[idx] == seq2[idx]:
			same = same + 1
	fraction = same / total
	return fraction



seq1 = 'GCTA'
seq2 = 'GCAA'

similarity = sequence_similarity(seq1, seq2)

print(similarity)



















# def count_kmers(seq, k):
# 	counts = {}
# 	for i in range(len(seq)-k+1):
# 		mer = seq[i:i+k]
# 		if mer not in counts:
# 			counts[mer] = 0
# 		counts[mer] = counts[mer] + 1
# 	return counts


# def nr_different_kmers(seq, k):
# 	counts = count_kmers(seq, k)
# 	nr = len(counts)
# 	return nr


# def most_common_kmer(seq, k):
# 	counts = count_kmers(seq, k)
# 	max_count = max(counts.values())
# 	lst = []
# 	for mer in counts:
# 		if counts[mer] == max_count:
# 			lst.append(mer)
# 	return lst


# def shared_kmers(seq1, seq2, k):
# 	counts1 = count_kmers(seq1, k)
# 	counts2 = count_kmers(seq2, k)
# 	lst = []
# 	for mer in counts1:
# 		if mer in counts2:
# 			lst.append(mer)
# 	return lst


# #######################################


# seq = 'GAGAGAGCTA'
# k = 3
# print(len(seq))
# for i in range(len(seq)-k+1):
# 	print(i)


# kmer_counts = count_kmers(seq, 3)
# print(kmer_counts)

# nr_kmers = nr_different_kmers(seq, 3)
# print(nr_kmers)

# common = most_common_kmer(seq, 3)
# print(common)

# seq2 = 'GAGAGAGCAA'

# shared = shared_kmers(seq, seq2, 3)
# print(shared)
