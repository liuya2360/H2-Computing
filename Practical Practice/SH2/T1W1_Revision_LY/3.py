#T1W1
#Binary Search Function

def binary_search(l, target):
    start = 0
    end = len(l)
    while start <= end:
        mid = (start+end)//2
        if mid == target:
            return mid
        elif mid < target:
            start = mid +1
        else:
            end = mid -1
    return -1
