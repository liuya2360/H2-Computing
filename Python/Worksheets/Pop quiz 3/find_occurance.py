def findOccurance(n,d):
	cnt = 0
	s = str(n)
	for i in range(len(n)):
		if i == 0:
			if int(s[i]) > int(d):
				cnt += 10**(len(s[i+1:]))
			if int(s[i]) == int(d):
				cnt += int(s[i+1:])+1
		if i != 0 and i != len(n)-1:
			if int(s[i]) > int(d):
				cnt += (int(s[:i])+1)*(10**(len(s[i+1:])))
			elif int(s[i]) == int(d):
				cnt += int(s[:i])*(10**(len(s[i+1:]))) + int(s[i+1:])+1
			else:
				cnt += int(s[:i])*(10**(len(s[i+1:])))
		if i == len(n)-1:
			if int(s[i]) > int(d):
				cnt += (int(s[:i])+1)*(10**(len(s[i+1:])))
			else:
				cnt += (int(s[:i]))*(10**(len(s[i+1:])))
	return cnt

n = input("input n:")
d = input("input d:")

print(findOccurance(n, d))