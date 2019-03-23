#0 -> iterative; 1 -> recursive
flag = 0

def it_function(x,n):
	result = 1
	for i in range(n):
		result *= x
	return result

def re_function(x,n):
	if n == 1:
		return x
	return re_function(x,n-1)*x

x = int(input())
n = int(input())

if flag == 0:
	print(it_function(x,n))
else:
	print(re_function(x,n))