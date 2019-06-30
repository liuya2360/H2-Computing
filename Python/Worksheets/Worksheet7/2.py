def d2k(d, k):
	mapping = "0123456789ABCDEF"
	result = ""
	while d != 0:
		digit = d % k
		d//=k
		result = mapping[digit] + result
	return result