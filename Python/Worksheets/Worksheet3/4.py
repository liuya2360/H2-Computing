file = open("primes1000000.txt", "r")

prime = []
for row in file:
	prime.append(row)

i = input()
if i in prime:
	print("True")
else:
	print("False")

file.close()