#0 -> iterative; 1 -> recursive
flag = 1

def it_min(s):
	minn = 0
	for i in range(len(s)):
		if float(s[i]) < float(s[minn]):
			minn = i
	return s[minn]

def re_min(s):
	if len(s) == 1:
		return s[0]
	elif float(s[0]) > float(re_min(s[1:])):
		return(re_min(s[1:]))
	else:
		return s[0]


s = input()
s = s.split(" ")

if flag == 0:
	print(it_min(s))
else:
	print(re_min(s))