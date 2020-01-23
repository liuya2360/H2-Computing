#bask k to denary
def k2d(a, k): 
    mapping = "0123456789ABCDEF"
    result = 0
    for i in range(len(a)):
        result += mapping.index(a[i]) * pow(k, len(a)-i-1)
    return result

print(k2d("1000", 2)) 
