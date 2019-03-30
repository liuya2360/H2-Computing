file = open("PERFECT_SQUARES.TXT", "a") 

n = int(input())
m = int(input())

for i in range(1, m+1):
	file.write(str(n+i)+"\n")

file.close()