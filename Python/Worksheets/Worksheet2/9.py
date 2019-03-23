#0 -> iterative; 1 -> recursive
flag = 0

def it_reverse(s):
	for i in range(len(s)):
		print(s[len(s)-1-i], end="")

def re_reverse(s):
	if len(s) == 1:
		print(s[0], end="")
		return
	else:
		re_reverse(s[1:])
		print(s[0], end="")

s = input()

if flag == 0:
	it_reverse(s)
else:
	re_reverse(s)

print("")