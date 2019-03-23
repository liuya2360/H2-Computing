#0 -> iterative; 1 -> recursive
flag = 0

def it_mean(s):
	summ = 0.0
	for i in s:
		summ += float(i)
	return summ/len(s)

def re_mean(s):
	if len(s) == 1:
		return float(s[0])
	return (re_mean(s[1:])*(len(s)-1) + float(s[0]))/len(s)

s = input()
s = s.split(" ")

if flag == 0:
	print(it_mean(s))
else:
	print(re_mean(s))