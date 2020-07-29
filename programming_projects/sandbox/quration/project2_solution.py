


ex_s1 = "AGTCGACGGATGAACCTCCACTTACACTATCTT"
ex_s2 = "TGTCTACGGTTGATCCTGCACGTACAGTATCAT"

ex_q1 = '707915609164612603160290247832979' 
ex_q2 = '059565606246285080270942561713910'

# unit test that they have entered the right sequences 


# 1 find length of sequence
def find_length(s):
    return len(s)
    
# 2 compare length to make sure the lengths of sequence and qualities are the same
def compare_length(sequence, qualities):
    return len(sequence) == len(qualities)

# 3 count bases
def count_bases(sequence):
    d = dict()
    for b in sequence:
        if b not in d:
            d[b] = 0
        d[b] += 1
    return d   # NB the key, value pairs will not necessarily appear in this order.

# 4 count differences
def count_differences(s1, s2):
    diffs = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diffs += 1
    return diffs

# # 5 NB:  the function must return a SORTED list of triplets (sorted(result))
# def find_shared_triplets(sequence1, sequence2):
#     result = list()
#     for i in range(len(sequence1)-2):
#         triplet = sequence1[i:i+3]
#         if triplet in sequence2:
#             result.append(triplet)
#     return sorted(result)


# 5 reverse the sequence
def reverse_seq(s):
    #return s[::-1]
    result = list()
    for i in range(len(s)):
        result.append(s[-i-1])
    return ''.join(result)

# 6
def reverse_complement_seq(s):
    #return s[::-1]
    mapping = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    result = list()
    for i in range(len(s)):
        result.append(mapping[s[-i-1]])
    return ''.join(result)

# 7 find all CpG sites. NB: return the indexes of the C base in the CpG site!
def find_cpg_sites(s):
    result = list()
    for i in range(len(s)-1):
        if s[i] == 'C' and s[i+1] == 'G':
            result.append(i)
    return result

# 8 find orthologous CpG sites
def find_orthologous_cpg_sites(s1, s2):
    result = list()
    l = find_cpg_sites(s1)
    for i in find_cpg_sites(s2):
        if i in l:
            result.append(i)
    return result

# 9 covert string to list of integers
def string_to_list_of_integers(qualities): ## DEN HER KAN DE BARE FAA GRATIS
    return list(map(int, qualities))

# 10 mean quality for each seq
def average_quality(q):
    return sum(string_to_list_of_integers(q))/float(len(q))


# 11
def average_quality_difference(qualities):
    if len(qualities) < 2:
        return None
    tot = 0.0
    q = string_to_list_of_integers(qualities)
    for i in range(len(q)-1):
        diff = q[i] - q[i+1]
        if diff < 0:
            diff = diff * -1
        tot += diff
    return tot / (len(q)-1)


# 12 average qualality by base. NB: should only include bases in the sequence and nore report zero for missing bases
def average_quality_by_base(sequence, qualities):
    # d = dict()
    # for b, q in zip(list(sequence), string_to_list_of_integers(qualities)):
    #     d.setdefault(b, []).append(q)
    # for k, v in d.items():
    #     d[k] = sum(v)/float(len(v))
    # return d
    q = string_to_list_of_integers(qualities)
    l = list(sequence)
    d = dict()
    for b, q in zip(l, q):
        if b not in d:
            d[b] = list()
        d[b].append(q)
    result = dict()
    for k, v in d.items():
        result[k] = sum(v)/float(len(v))
    return result

# 13 average quality for bases in CpG dinucleotides
def average_quality_for_cpg_sites(s, q):

    qual_integers = string_to_list_of_integers(q)
    tot = 0
    cpg_sites = find_cpg_sites(s)
    for i in cpg_sites:
        tot += qual_integers[i] + qual_integers[i+1]

    return tot / len(cpg_sites) / 2

# 14
def mask_low_quality_bases(sequence, qualities, minimum_qual):

    result = list()
    for b, q in zip(sequence, qualities):
        if int(q) < minimum_qual:
            result.append('N')
        else:
            result.append(b)
    return ''.join(result)

# 15 compute min qualtiy (the smallest of q1[i] and q2[i]) at each site
def lowest_qualities_at_position(q1, q2):
    return [min(int(x), int(y)) for x, y in zip(q1, q2)]

# 16compute min quality at homs and hets.
def average_lowest_quality_at_homo_and_hetero(sequence1, sequence2, qualities1, qualities2):

    hom = []
    het = []
    for i, m in enumerate(lowest_qualities_at_position(qualities1, qualities2)):
        if sequence1[i] == sequence2[i]:
            hom.append(m)
        else:
            het.append(m)
    return [sum(hom)/len(hom), sum(het)/len(het)] # NB: musr return two values, a tuple

# 17 inner dict for next. NB: for bases not found the count must be zero
def count_bases_with_a_quality(sequence, qualities, qual):

    qual_integers = string_to_list_of_integers(qualities)
    result = {'A':0, 'T':0, 'C':0, 'G':0}
    for b, q in zip(sequence, qual_integers):
        if q == qual:
            # if b not in result:
            #     result[b] = 0
            result[b] += 1
    return result

# 18 dict of dict outer quality innner base. NB: ALL qualities must be represented in the structures
def count_bases_by_quality(sequence, qualities):

    result = {}
    qual_integers = string_to_list_of_integers(qualities)
    for q in range(10):
        result[q] = count_bases_with_a_quality(sequence, qualities, q)
    return result

# split into list without Ns
# def get_unmasked_sequence(sequence):

#     def find_next(i, s):
#         for i in range(i, len(sequence)):
#             if sequence[i] in s:
#                 return i
#         return i+1

#     bases = 'AGTCagtc'
#     nonbases = 'Nn'
#     start = find_next(0, bases)
#     end = find_next(start, nonbases)
#     result = []
#     while start + 1 < end:
#         result.append(sequence[start:end])
#         start = find_next(end, bases)
#         end = find_next(start, nonbases)
#     return result

# 19
def get_unmasked_sequence(sequence):

    result = []
    sublist = []
    for b in sequence:
        if b == 'N':
            if sublist:
                result.append(''.join(sublist))
                sublist = []
        else:
            sublist.append(b)
    if sublist:
        result.append(''.join(sublist))
    return result

# 20 find longest stretch without Ns, Should return None if there is no unmasked sequence
# def average_quality_of_unmasked_sequence(sequence, qualities, cut):
#     masked = mask_low_quality_bases(sequence, qualities, cut)
#     quals = []
#     for i, b in enumerate(masked):
#         if b != 'N':
#             quals.append(int(qualities[i]))
#     if quals:
#         return sum(quals) / len(quals)
# #
def mask_sequence_sequence_pair(sequence1, sequence2, qualities1, qualities2, cut):

    mask1 = mask_low_quality_bases(sequence1, qualities1, cut)
    mask2 = mask_low_quality_bases(sequence2, qualities2, cut)
    l1 = []
    l2 = []
    for i in range(len(mask1)):
        if mask1[i] == 'N' or mask2[i] == 'N':
            l1.append('N')
            l2.append('N')
        else:
            l1.append(mask1[i])
            l2.append(mask2[i])
    return [''.join(l1), ''.join(l2)]


if __name__ == "__main__":

    print(find_length(ex_s1))
    print(compare_length(ex_s1, ex_s2))
    print(count_bases(ex_s1))
    print(count_differences(ex_s1, ex_s2))

    print("#", average_quality_difference('125'))
#    print(find_shared_triplets(ex_s1, ex_s2))

    print(reverse_seq("ACTG"))
    print(reverse_complement_seq("ACTG"))

    print(find_cpg_sites('CGAGCGAACG'))


    print(find_orthologous_cpg_sites('CGAGCGAACG', 'CGAGAGAACG'))

    print(average_quality('12'))


    print(average_quality_by_base(ex_s1, ex_q1))


    print(average_quality_for_cpg_sites(ex_s1, ex_q1))

    
    print(mask_low_quality_bases('AGCT', '2134', 2))


    print(lowest_qualities_at_position('1234', '4321'))
    print(average_lowest_quality_at_homo_and_hetero('AAAA', 'TAAT', '1234', '4321'))


    print(count_bases_with_a_quality(ex_s1, ex_q1, 9))

    print(count_bases_by_quality(ex_s1, ex_q1))[9]

    print(get_unmasked_sequence("AAANNTTNGGG"))


    print(mask_sequence_pair(ex_s1, ex_s2, ex_q1, ex_q2, 2))