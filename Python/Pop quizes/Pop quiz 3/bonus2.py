def get_dist(x1,y1,x2,y2):
	dist = ((x1-x2)**2+(y1-y2)**2)**0.5
	return dist


def check_rectangle(a):
	n = len(a)#number of points
	cnt_rec = 0
	for i in range(len(a)-3):
		for j in range(i+1, len(a)-2):
			for k in range(j+1, len(a)-1):
				for l in range(k+1, len(a)):
					dis_i_j = get_dist(a[i][0],a[i][1],a[j][0],a[j][1])
					dis_k_l = get_dist(a[k][0],a[k][1],a[l][0],a[l][1])
					dis_i_k = get_dist(a[i][0],a[i][1],a[k][0],a[k][1])
					dis_j_l = get_dist(a[j][0],a[j][1],a[l][0],a[l][1])
					dis_i_l = get_dist(a[i][0],a[i][1],a[l][0],a[l][1])
					dis_j_k = get_dist(a[j][0],a[j][1],a[k][0],a[k][1])
					if dis_i_j == dis_k_l and dis_i_k == dis_j_l and dis_i_l == dis_j_k:
						cnt_rec += 1
						#print("!",i,j,k,l)

	return cnt_rec


n = [(0,1), (1,0), (1,1), (1,2), (2,1), (2,2)]
print(check_rectangle(n))