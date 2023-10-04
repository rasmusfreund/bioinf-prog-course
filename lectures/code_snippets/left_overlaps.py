

def get_left_overlaps(overlaps, right):
    left_overlaps = []
    for left in overlaps:
        if right in overlaps[left]:
            left_overlaps.append(overlaps[left][right])
    return sorted(left_overlaps)

    