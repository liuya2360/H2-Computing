def k2d(s, k):
	mapping = "0123456789ABCDEF"
	result = 0
	for i in range(len(s)): 
		result += (mapping.index(s[i])+1) * k**(len(s)-i-1)
	return result