def linearSearch1(L, t):
    for i in range(len(L)):
        if L[i] == t:
            return i
    return -1