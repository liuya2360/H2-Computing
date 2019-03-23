#0 -> iterative; 1 -> recursive
flag = 0

def it_print(n):
	for i in range(n+1):
		print(n-i)

def re_print(n):
	print(n)
	if n == 0:
		return
	re_print(n-1)
	

n = int(input())

if flag == 0:
	it_print(n)
else:
	re_print(n)