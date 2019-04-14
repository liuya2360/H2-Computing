def binarySearch2(L, t):
    start = 0
    end = len(L)-1
    while start <= end:
        mid = (start-end) // 2
        if L[mid] == t: 
            return mid
        elif L[mid] > t:
            start = mid + 1
        else: 
            end = mid - 1
    return -1