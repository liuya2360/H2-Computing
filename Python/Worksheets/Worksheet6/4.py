def linearSearch2(L, t):
    ans = None
    for i in range(len(L)):
        if L[i] > t:
            temp = L[i]
            if ans == None:
                ans = temp
            elif ans > temp:
                ans = temp
    return ans