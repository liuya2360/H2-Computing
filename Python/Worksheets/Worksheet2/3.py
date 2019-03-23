#0 -> iterative; 1 -> recursive
flag = 0

def it_sum(n):
	result = 0
	for i in range(n+1):
		result += i
	return result

def re_sum(n):
	if n == 1:
		return 1
	else:
		return re_sum(n-1)+n

n = int(input())

if flag == 0:
	print(it_sum(n))
else:
	print(re_sum(n))