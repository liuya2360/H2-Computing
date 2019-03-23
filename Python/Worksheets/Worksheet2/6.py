#0 -> iterative; 1 -> recursive
flag = 0

n = int(input())

def it_function(n):
	result = 1
	for i in range(1, n+1):
		result *= i
	return result

def re_function(n):
	if n == 1:
		return 1
	return re_function(n-1)*n

if flag == 0:
	print(it_function(n))
else:
	print(re_function(n))