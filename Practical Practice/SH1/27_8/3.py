#quick sort 

def qsort(l): 
    if len(l) < 2: 
        return l
    else: 
        mid = l[0] 
        left = []
        right = []
        for i in range(1, len(l)): 
            if l[i] < mid: 
                left.append(l[i]) 
            else: 
                right.append(l[i])
        return qsort(left) + [mid] + qsort(right) 
    
l = [5, 1, 7, 4, 0]
print(qsort(l))
