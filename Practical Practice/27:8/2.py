#bubble sort 
def bubbleSort(l): 
    for i in range(len(l)):
        swap = False 
        for j in range(len(l)-1-i): 
            if l[j] > l[j+1]: 
                l[j], l[j+1] = l[j+1], l[j] 
                swap = True 
        if not swap: 
            break 
    return l 


l = [5, 1, 7, 4, 0]
print(bubbleSort(l))


'''
difference between sort and sorted 
one is inplace 
the other one returns a sorted list 



def bubbleSort1(l): 
    for i in range(len(l)): 
        swap = False  
        for j in range(i+1, len(l)): 
            if l[i] > l[j]: 
                l[i], l[j] = l[j], l[i]
                swap = True 
        if not swap: 
            break 
    return l 

'''