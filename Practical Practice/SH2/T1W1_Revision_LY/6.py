#T1W1
# quick sort

def qsort(l):
    if len(l) < 2:
        return l
    else:
        less = []
        more = []
        pivot = l[0]
        for i in range(1, len(l)):
            if l[i] <= pivot:
                less.append(l[i])
            else:
                more.append(l[i])
        return qsort(less) + [pivot] + qsort(more) 
