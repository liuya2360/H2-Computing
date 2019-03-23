s = input("Enter sentence to encrypt: ")
a = int(input("Enter shift value: "))

print("The encoded phrase is: ", end="")
for i in s:
	if ord(i) < 65 or ord(i) > 122 or (ord(i) > 90 and ord(i) < 97):
		ascii_i = ord(i)
	elif ord(i) >= 65 and ord(i) <= 90:
		ascii_i = ord(i) + a
		if ascii_i > 90:
			ascii_i = ascii_i % 90 + 64
	elif ord(i) >= 97 and ord(i) <= 122:
		ascii_i = ord(i) + a
		if ascii_i > 122:
			ascii_i = ascii_i % 122 + 96
	print(chr(ascii_i), end="")

print("")