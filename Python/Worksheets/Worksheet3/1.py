file = open("PERFECT_SQUARES.TXT", "w") 

def check_square(n):
	x = int(n**0.5)
	if n == x**2:
		return True
	else:
		return False

n = int(input())

for i in range(1, n+1):
	if check_square(i):
		file.write(str(i)+"\n")

file.close()