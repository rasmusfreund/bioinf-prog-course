
def quicksort(lst, low, high):
    if low < high: # kun hvis dellisten har mindst to elementer
        deler = partition(lst, low, high)
        quicksort(lst, low, deler-1)
        quicksort(lst, deler+1, high)

def partition(lst, low, high):
    deler = high # deler (delekort)
    g = low # grøn pil
    for r in range(low, high): # flytter rød pil
        if lst[r] <= lst[deler]:
            lst[g], lst[r] = lst[r], lst[g] # byt rød og grøn            
            g += 1 # flyt grøn pil
    lst[g], lst[deler] = lst[deler], lst[g] # byt grøn med deler
    return g



numbers = [4, 2,4,5,1,4,3]
quicksort(numbers, 0, len(numbers)-1)
print(numbers)
