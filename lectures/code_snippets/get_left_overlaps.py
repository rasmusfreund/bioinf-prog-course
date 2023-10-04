
def get_left_overlaps(overlaps, right):
    left_overlaps = []
    for left in overlaps:
        if left != right:
            left_overlaps.append(overlaps[left][right])
    return sorted(left_overlaps)





overlaps = {'Read1': {'Read3':  0, 'Read2':  1, 'Read5':  1, 'Read4': 0, 'Read6': 29},
            'Read3': {'Read1':  0, 'Read2':  0, 'Read5':  0, 'Read4': 1, 'Read6':  1},
            'Read2': {'Read1': 13, 'Read3':  1, 'Read5': 21, 'Read4': 0, 'Read6':  0},
            'Read5': {'Read1': 39, 'Read3':  0, 'Read2':  1, 'Read4': 0, 'Read6': 14},
            'Read4': {'Read1':  1, 'Read3':  1, 'Read2': 17, 'Read5': 2, 'Read6':  0},
            'Read6': {'Read1':  0, 'Read3': 43, 'Read2':  0, 'Read5': 0, 'Read4':  1}}

print(get_left_overlaps(overlaps, 'Read1'))