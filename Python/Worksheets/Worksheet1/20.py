ith = int(input("Select the prime number you want (i.e., an integer): "))
print("Prime number " + str(ith) + ": ", end="")

def check_prime(a):
	b = int((a**0.5) // 1)
	#print(b)
	for i in range(2, b+1):
		if a % i == 0:
			return 0
	return 1

cnt = 0
p_number = 1
while cnt != ith:
	p_number += 1
	result = check_prime(p_number)
	#print(p_number, "result", result)
	if result == 1:
		cnt += 1

print(p_number)