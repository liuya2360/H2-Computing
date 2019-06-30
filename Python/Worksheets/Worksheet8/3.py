def insertionSort(L):
    for i in range(1, len(L)):
    	for j in range(i, 0, -1): 
    		if L[j] < L[j-1]:
    			L[j], L[j-1] = L[j-1], L[j]
    return L