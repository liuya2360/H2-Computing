#0 -> iterative; 1 -> recursive
flag = 0

def it_powerset(A):
	n = 2**len(A)
	#print(n)
	#print(len(A))
	for i in range(n):
		#print("i", i)
		temp = []
		for j in range(len(A)-1,-1,-1):
			#print("j",j)
			if i // (2**(j)) == 1:
				temp.append(A[j])
				#print("temp",temp)
				i -= 2**j
		print(temp)


A = input().split(" ")
if flag == 0:
	it_powerset(A)