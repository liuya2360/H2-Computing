#T1W1 Revision
#Q2

#linear search function
def search(l, target): 
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1
