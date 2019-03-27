def findOccurance(n,d):
	cnt = 0
	for i in range(1, n+1):
		i_string = str(i)
		for j in i_string:
			if j == str(d):
				cnt += 1
	return cnt

n = int(input("input n:"))
d = int(input("input d:"))

print(findOccurance(n, d))