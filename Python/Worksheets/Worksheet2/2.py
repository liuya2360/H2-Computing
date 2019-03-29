#0 -> iterative; 1 -> recursive
flag = 1

#need to account for the cases when a or b or both are negative 

def it_product(a,b):
	result = 0
	for i in range(a):
		result += b
	return result

def re_product(a,b):
	if b == 0:
		return a
	else:
		global result
		re_product(a,b-1)
		result += a
	return result

a = int(input())
b = int(input())

if flag == 0:
	print(it_product(a,b))
else:
	print(re_product(a,b))