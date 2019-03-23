#0 -> iterative; 1 -> recursive
flag = 1

def it_check_prime(n):
	k = int(n**0.5//1)
	for i in range(2,k+1):
		if n%i == 0:
			return False
	return True

def re_check_prime(n,a):
	if a == 1:
		return True
	elif n % a == 0:
		print(a)
		return False
	else:
		return re_check_prime(n,a-1)

n = int(input())

if flag == 0:
	print(it_check_prime(n))
else:
	print(re_check_prime(n,n-1))