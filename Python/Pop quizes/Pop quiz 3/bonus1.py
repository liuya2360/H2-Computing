def find_special_problems(n, k, p):
	pages = []
	flag = True
	p_cnt = p[:]
	cnt = 0#pages
	i = 0#chapter
	pages.append([])
	while flag:
		#print("pages", pages)
		#print("cnt", cnt)
		#print("i", i)
		while int(p[i]) > 0:
			p[i] = int(p[i]) - 1
			#print("p[i]", p[i])
			if len(pages[cnt]) == k:
				cnt += 1
				pages.append([])
				#print("cnt", cnt)
			pages[cnt].append(int(p_cnt[i])-int(p[i]))
		cnt += 1
		i += 1
		pages.append([])
		if i == n:
			flag = False

	cnt_special = 0
	#page number 
	for i in range(len(pages)):
		#question number 
		for j in range(len(pages[i])):
			if pages[i][j] == i+1:
				#print(pages[i][j], "i", i+1)
				cnt_special += 1
	return cnt_special

n = int(input())
k = int(input())
p = input().split(" ")
#print(p)

print(find_special_problems(n, k, p))

			