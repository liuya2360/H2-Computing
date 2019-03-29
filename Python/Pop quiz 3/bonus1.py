def find_special_problems(n, k, p):
	n = int(n)
	k = int(k)
	cnt = 0
	chapter_page = []
	cnt_temp = 0
	for i in range(n):
		chapter_page.append(cnt_temp)
		if int(p[i])%k == 0:
			cnt_temp += int(p[i])//k
		else:
			cnt_temp += int(p[i])//k+1
	chapter_page.append(cnt_temp)
	for i in range(n):
		for j in range(int(p[i])):
			