def bubbleSort(L):
    for i in range(len(L)-1):
        swap = False
        for j in range(len(L)-1-i):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
                swap = True
        if not swap:
            break    
    return L

'''
L = input().split(" ")
print(bubbleSort(L))
'''