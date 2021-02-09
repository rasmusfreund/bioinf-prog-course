
def leaves(tree):
    if type(tree) is str:
        return [tree]
    return leaves(tree[0]) + leaves(tree[1])


tree = [[['A', 'C'],'B'],['E', 'D']]

print(leaves(tree))    