file = open("iris.data.txt", "r") 

L = []
for line in file:
	L.append(line.strip().split(","))

#print(len(L))
#print(len(L[0]))

file.close()