def linear_search(A, t): 
  for i in range(len(A)): 
    if A[i] == t: 
      return i 
  return -1

'''
A = [1, 2, 3]
print(linear_search(A, 4))
''' 

def linear_search_ceiling(A, t): 
  temp = -1
  for i in range(len(A)): 
    if A[i] > t: 
      if temp == -1: 
        temp = i; 
      else: 
        if A[i]-t < A[temp]-t: 
          temp = i 
  if temp == -1: 
    return -1 
  else: 
    return A[temp], temp

'''
A = [1,3,5,7,9]
print(linear_search_ceiling(A, 3))
'''

def bin_search(A, t):
    start = 0
    end = len(A)-1
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == t:
            return mid
        elif A[mid] > t:
            end = mid - 1
        else:
            start = mid + 1
    return -1

def bin_search_dupl(A, target):
    start = 0
    end = len(A)-1
    left = -1
    right = -1 
    while start <= end:
        mid = (start + end)//2
        if A[mid] == target:
            if mid == 0:
                left = mid 
            else: 
                for i in range(mid-1, start-1, -1):
                    if A[i] != target:
                        left = i+1
                        break 
            if mid == len(A)-1:
                right = mid 
            else: 
                for i in range(mid+1, end+1):
                    if A[i] != target:
                        right = i-1
                        break 
            return left, right
        elif A[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return -1

'''
A = [1,2,3,3,4,5,5,6] 
print(bin_search_dupl(A, 3))
print("done") 
'''

def qsort(A):
    if len(A) < 2:
        return A 
    left = []
    right = []
    pivot = A[0]
    for i in range(1, len(A)):
        if A[i] < pivot:
            left.append(A[i])
        else:
            right.append(A[i])
    return qsort(left) + [pivot] + qsort(right)

'''
A = [0,19,2,4]
print(qsort(A))
'''

def qsort_inplace(A):
    if len(A) < 2:
        return A
    else:
        return qsort_inplace_rec(A, 0, len(A))

def qsort_inplace_rec(A, left, right): 
    if right - left < 2:
        return A
    pivot = left
    lp = pivot+1
    rp = right-1 
    while lp <= rp:
        print(A[lp], A[pivot]) 
        while A[lp] < A[pivot]:
            lp += 1
        while A[rp] > A[pivot]:
            rp -= 1
        A[lp], A[rp] = A[rp], A[lp] 
        lp += 1
        rp -= 1
    temp = A[pivot] 
    for i in range(pivot, lp-1):
        A[i] = A[i+1]
    A[lp-1] = temp 
    
    if pivot - left > 1:
        A = qsort_inplace_rec(A, left, pivot)
    if right - pivot > 1: 
        A = qsort_inplace_rec(A, pivot+1, right)
    return A


A = [0,19,2,5,3,11,9,4]
print(qsort_inplace(A))


