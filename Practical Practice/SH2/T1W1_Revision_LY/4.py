#T1W1
#Bubble sort function

def bubble_sort(l):
    for i in range(1, len(l)):
        swap = False 
        for j in range(i): 
            if l[j] > l[i]:
                l[j], l[i] = l[i], l[j]
                swap = True
        if not swap:
            return l
    return l 
