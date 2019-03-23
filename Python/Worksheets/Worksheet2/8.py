#0 -> iterative; 1 -> recursive
flag = 0

def it_cnt(n):
	cnt = 0
	while n != 0:
		cnt += 1
		n //= 10
	return cnt

def re_cnt(n):
	if n == 0:
		return 0
	n //= 10
	return re_cnt(n)+1


n = int(input())

if flag == 0:
	print(it_cnt(n))
else:
	print(re_cnt(n))