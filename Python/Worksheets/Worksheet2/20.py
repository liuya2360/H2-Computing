#0 -> iterative; 1 -> recursive
flag = 0

def it_hanoi(n,A):
	if n == 2:
		print("["+str(A[0])+","+str(A[1])+"]")
		print("["+str(A[0])+","+str(A[2])+"]")
		print("["+str(A[1])+","+str(A[2])+"]")
		return 0
	else:
		B = [A[0],A[2],A[1]]
		#print("A", A)
		#print("B", B)
		it_hanoi(n-1,B)
		print("["+str(A[0])+","+str(A[2])+"]")
		C = [A[1],A[0],A[2]]
		#print("A", A)
		#print("B", B)
		it_hanoi(n-1,C)

n = int(input())

A = [1,2,3]
if flag == 0:
	it_hanoi(n,A)
'''
if flag == 1:
	re_hanoi(n,A)
'''