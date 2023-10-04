
def get_overlap(left, right):
    len_left = len(left)
    len_right = len(right)
    max_overlap = min(len_left, len_right)
    for i in range(max_overlap):
        o = max_overlap - i
        if left[-o:] == right[:o]:
            return left[-o:]
    return ''

def get_overlap(left, right):
    max_overlap = min(len(left), len(right))
    for i in range(max_overlap, 0, -1):
        if left[-i:] == right[:i]:
            return left[-i:]
    return ''