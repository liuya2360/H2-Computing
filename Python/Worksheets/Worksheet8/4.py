def quicksort(L):
    if len(L) <= 1:
        return L
    less = []
    more = []
    pivot = L[0]
    for i in range(1,len(L)):
        if L[i] < pivot:
            less.append(L[i])
        else: 
            more.append(L[i])
    return quicksort(less) + [pivot] + quicksort(more)

    '''
    #write quick sort in one line using list comprehension 
    return L if len(L)<2 else(quicksort([L[i] for i in range(1,len(L)) if L[i]<L[0]])+[l[0]]+quicksort([L[i] for i in range(1,len(L) if L[i]>L[0])]))
    '''

'''
L = input().split(" ")
print(quicksort(L))
'''