#0 -> iterative; 1 -> recursive
flag = 1

def it_fibo(n):
	cnt = 1
	f0 = 1
	f1 = 1
	while cnt != n:
		cnt += 1
		f = f0 + f1
		#print("f"+str(cnt), f)
		f0 = f1
		f1 = f
	return f1

def re_fibo(n):
	if n == 1:
		return 1
	if n == 0:
		return 1
	else:
		return re_fibo(n-1) + re_fibo(n-2)

n = int(input())

if flag == 0:
	print(it_fibo(n))
else:
	print(re_fibo(n))