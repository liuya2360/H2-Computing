#0 -> iterative; 1 -> recursive
flag = 0

def it_common_devisor(N):
	N.sort()
	for i in range(N[0],1,-1):
		f = 0
		for j in N:
			if j % i != 0:
				f = 1
				break
		if f == 0:
			return i
	return 1

def re_common_devisor(N, a):
	if a == 1:
		return 1
	else:
		flag1 = 0
		for i in N:
			if i % a != 0:
				flag1 = 1
				break
		if flag1:
			re_common_devisor(N, a-1)
		else:
			print(a)

N = input()
N = N.split(" ")
N = list(map(int,N))

if flag == 0:
	print(it_common_devisor(N))
else:
	N.sort()
	re_common_devisor(N, N[0])