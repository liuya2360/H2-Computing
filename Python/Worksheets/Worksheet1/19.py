s = input("Input a number: ")
n = int(input("Number of significant figures: "))

flag = 0
out = ""
last_d = None #last digit
flag0 = 0 #to check if there is a "."
for i in s:
	if flag == 2:
		if int(i) >= 5:
			last_d += 1
		out += str(last_d)
		n -= 1
		break
	if n == 1:
		flag = 2
		last_d = int(i)
	if flag == 0:
		out += i
	if flag == 1:
		n -= 1
		#print(n, out)
		out += i
	if i == ".":
		flag = 1
		flag0 = 1
	#print("out", out)

if flag0 == 0:
	out += "."
#print(n)

if n > 0:
	while n != 0:
		n -= 1
		out += "0"

print("The value " + str(s) + " rounded to " + str(n) + " significant figures is: " + str(out))