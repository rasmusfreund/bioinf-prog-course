

def n50(lengths):
    total = sum(lengths)
    sorted_lengths = sorted(lengths, reverse=True)
    running_sum = 0
    for l in sorted_lengths:
        running_sum += l
        if running_sum >= total/2:
            return l




contig_lengths = [12, 20, 1, 5, 8, 3, 1]

print(n50(contig_lengths))