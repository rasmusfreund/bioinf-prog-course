
def count(tree):
    if type(tree) is str:
        return 1
    return count(tree[0]) + count(tree[1])


tree = [[['A', 'C'],'B'],['E', 'D']]

print(count(tree))