#0 -> iterative; 1 -> recursive
flag = 1

def it_print(n):
	for i in range(0, n+1):
		print(i)
def re_print(n):
	if n == 0:
		print(n)
		return 0
	else:
		re_print(n-1)
		print(n)

n = int(input())
if flag == 0:
	it_print(n)
else:
	re_print(n)