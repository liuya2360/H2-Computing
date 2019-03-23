#0 -> iterative; 1 -> recursive
flag = 0

def it_sum(s):
	summ = 0
	for i in s:
		summ += int(i)
	return summ

def re_sum(s):
	if len(s) == 1:
		return int(s[0])
	return re_sum(s[1:])+int(s[0])

s = input()
s = s.split(" ")

if flag == 0:
	print(it_sum(s))
else:
	print(re_sum(s))