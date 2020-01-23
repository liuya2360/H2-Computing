def merge_sort(array):
    if len(array) < 2:
        return array
    mid = len(array)//2
    return merge(merge_sort(array[:mid]), merge_sort(array[mid:]))

def merge(A, B):
    ret = []
    while len(A) and len(B):
        if A[0] < B[0]:
            ret.append(A[0])
            A.pop(0)
        else:
            ret.append(B[0])
            B.pop(0)
    if len(A) == 0:
        ret = ret + B
    else:
        ret = ret + A
    return ret

'''
A = [5,1,6,7,4,9,0]
print(merge_sort(A)) 
'''
