#insertion sort recursive version 

def insertion_sort_rec(L): 
    return outerLoop(L, 0)

def outerLoop(L, p): 
    if p == len(L): 
        print(L)
        return L 
    else: 
        L = innerLoop(L, p)
        outerLoop(L, p+1)

def innerLoop(L, i): 
    if i < 1: 
        return L 
    else: 
        if L[i] < L[i-1]: 
            L[i-1], L[i] = L[i], L[i-1]
        return innerLoop(L, i-1)

l = [5, 1, 7, 4, 0]
print(insertion_sort_rec(l)) 
